import os
import re
import sys

# Paths
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES_DIR = os.path.join(REPO_ROOT, "_pages")

LANGS = ["id", "en", "ja"]
SLUGS = {
    "main": "/{lang}/main/",
    "3e": "/{lang}/3e/",
    "about": "/{lang}/about/",
    "contact": "/{lang}/contact/",
    "portfolio-psychology": "/{lang}/portfolio/psychology/",
    "portfolio-hr": "/{lang}/portfolio/hr/",
    "portfolio-japanese": "/{lang}/portfolio/japanese/",
    "portfolio-coding": "/{lang}/portfolio/coding/",
    "portfolio-data-analysis": "/{lang}/portfolio/data-analysis/",
    "portfolio-design": "/{lang}/portfolio/design/",
    "portfolio-illustration": "/{lang}/portfolio/illustration/",
    "portfolio-writing": "/{lang}/portfolio/writing/",
    "portfolio-music": "/{lang}/portfolio/music/",
    "portfolio-second-brain": "/{lang}/portfolio/second-brain/",
    "portfolio-sport": "/{lang}/portfolio/sport/",
    "portfolio-cooking": "/{lang}/portfolio/cooking/"
}

EXPECTED_PERMALINKS = set()
for lang in LANGS:
    for slug, p in SLUGS.items():
        EXPECTED_PERMALINKS.add(p.format(lang=lang))

errors = {}
warnings = {}

def add_error(file, msg):
    if file not in errors:
        errors[file] = []
    errors[file].append(msg)

def add_warning(file, msg):
    if file not in warnings:
        warnings[file] = []
    warnings[file].append(msg)

jp_regex = re.compile(r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FAF]')
def mask_match(match):
    s = match.group(0)
    return ''.join('\n' if c == '\n' else ' ' for c in s)

# 1. Kelengkapan halaman
for lang in LANGS:
    for slug in SLUGS.keys():
        expected_file = f"{lang}-{slug}.md"
        file_path = os.path.join(PAGES_DIR, expected_file)
        if not os.path.exists(file_path):
            add_error(expected_file, "File tidak ada (hilang di bahasa ini).")

# 2. Permalink & 3. Link internal
if os.path.exists(PAGES_DIR):
    for filename in os.listdir(PAGES_DIR):
        if not filename.endswith(".md"):
            continue
            
        file_path = os.path.join(PAGES_DIR, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Parse front matter
        fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
        if fm_match:
            fm = fm_match.group(1)
            # Find permalink
            permalink_match = re.search(r"^permalink:\s*(.+)$", fm, re.MULTILINE)
            if permalink_match:
                permalink = permalink_match.group(1).strip().strip("'\"")
                
                parts = filename[:-3].split("-", 1)
                if len(parts) == 2 and parts[0] in LANGS and parts[1] in SLUGS:
                    expected_p = SLUGS[parts[1]].format(lang=parts[0])
                    if permalink != expected_p:
                        add_error(filename, f"Permalink salah. Diharapkan: {expected_p}, ditemukan: {permalink}")
            else:
                add_error(filename, "Front matter tidak memiliki permalink.")
        else:
            add_error(filename, "Front matter tidak ditemukan.")
            
        # Check internal links
        md_links = re.findall(r"\[[^\]]*\]\(([^)]+)\)", content)
        html_links = re.findall(r'(?:href|src)=["\']([^"\']+)["\']', content)
        
        all_links = md_links + html_links
        for link in all_links:
            url = link.split("#")[0].strip()
            
            # Skip empty or external URLs
            if not url or url.startswith("http://") or url.startswith("https://") or url.startswith("mailto:"):
                continue
                
            if url.startswith("/id/") or url.startswith("/en/") or url.startswith("/ja/"):
                if url not in EXPECTED_PERMALINKS:
                    add_error(filename, f"Link rusak ke halaman internal: {url}")
            else:
                # Assets Check
                if "/assets/" in url or url.startswith("assets/"):
                    url_clean = url.split("?")[0]
                    if url_clean.startswith("/"):
                        url_clean = url_clean[1:]
                    
                    # Prevent going out of bounds, replace / with os.sep
                    asset_path = os.path.normpath(os.path.join(REPO_ROOT, url_clean.replace("/", os.sep)))
                    if not os.path.exists(asset_path):
                        add_error(filename, f"Link rusak ke aset: {url}")

        # 4. Check Japanese text without lang="ja" in id and en pages
        if filename.startswith("id-") or filename.startswith("en-"):
            text_masked = re.sub(r'^---\s*\n.*?\n---\s*\n', mask_match, content, flags=re.DOTALL)
            text_masked = re.sub(r'```.*?```', mask_match, text_masked, flags=re.DOTALL)
            text_masked = re.sub(r'`[^`]*`', mask_match, text_masked)
            text_masked = re.sub(r'<([a-zA-Z0-9\-]+)[^>]*\blang=["\']?(?:ja|ja-JP)["\']?[^>]*>.*?</\1>', mask_match, text_masked, flags=re.DOTALL)
            
            lines = text_masked.split('\n')
            original_lines = content.split('\n')
            
            for i, line in enumerate(lines):
                if jp_regex.search(line):
                    orig = original_lines[i]
                    if 'lang="ja"' in orig or "lang='ja'" in orig or 'lang="ja-JP"' in orig or "lang='ja-JP'" in orig:
                        continue
                    if i + 1 < len(original_lines) and re.search(r'^\{:.*lang=["\']?(ja|ja-JP)["\']?.*\}', original_lines[i+1].strip()):
                        continue
                        
                    snippet = orig.strip()
                    if len(snippet) > 100:
                        snippet = snippet[:97] + "..."
                    add_warning(filename, f"Baris {i+1}: {snippet}")

has_errors = len(errors) > 0
has_warnings = len(warnings) > 0

if has_warnings:
    print("PERINGATAN: Teks Jepang tanpa atribut lang=\"ja\" ditemukan:")
    for f, msgs in warnings.items():
        print(f"\n[{f}]")
        for m in msgs:
            print(f"  - {m}")
    print("\n" + "-"*50 + "\n")

if has_errors:
    print("Ditemukan masalah pada konsistensi bahasa/link:")
    for f, msgs in errors.items():
        print(f"\n[{f}]")
        for m in msgs:
            print(f"  - {m}")
    sys.exit(1)
else:
    print("Pengecekan bahasa selesai: Tidak ada masalah konsistensi atau link rusak.")
    sys.exit(0)
