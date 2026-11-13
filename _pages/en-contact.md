---
layout: single
title: "Contact"
permalink: /en/contact/
lang: en
change_lang_text: "Change language"
---

Want to chat, collaborate, or just say hi? Choose the most comfortable path below.

<style>
html:is([lang="id"], [lang="en"], [lang="ja"]) body.layout--single #main .page__content .contact-group {
  margin: 2.5rem 0;
}
html:is([lang="id"], [lang="en"], [lang="ja"]) body.layout--single #main .page__content .contact-group h2 {
  margin: 0 0 1.25rem 0;
  padding: 0 0 0.75rem 0;
  border: none;
  border-bottom: 1px solid var(--sumi-divider);
  font-family: "Noto Serif", "Noto Serif JP", Georgia, serif;
  font-size: 22px;
  line-height: 30px;
  font-weight: 400;
  color: var(--sumi-text);
}
html:is([lang="id"], [lang="en"], [lang="ja"]) body.layout--single #main .page__content .contact-links {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1rem;
  margin: 0;
  padding: 0;
  list-style: none;
  width: 100%;
  box-sizing: border-box;
}
@media (min-width: 768px) {
  html:is([lang="id"], [lang="en"], [lang="ja"]) body.layout--single #main .page__content .contact-links {
    grid-template-columns: repeat(2, minmax(0, 1fr));
    grid-auto-rows: 1fr;
  }
}
html:is([lang="id"], [lang="en"], [lang="ja"]) body.layout--single #main .page__content .contact-links li {
  margin: 0;
  padding: 0;
  min-width: 0;
  display: flex;
}
html:is([lang="id"], [lang="en"], [lang="ja"]) body.layout--single #main .page__content a.contact-btn,
html:is([lang="id"], [lang="en"], [lang="ja"]) body.layout--single #main .page__content a.contact-btn:visited,
html:is([lang="id"], [lang="en"], [lang="ja"]) body.layout--single #main .page__content a.contact-btn:hover,
html:is([lang="id"], [lang="en"], [lang="ja"]) body.layout--single #main .page__content a.contact-btn-col,
html:is([lang="id"], [lang="en"], [lang="ja"]) body.layout--single #main .page__content a.contact-btn-col:visited,
html:is([lang="id"], [lang="en"], [lang="ja"]) body.layout--single #main .page__content a.contact-btn-col:hover {
  width: 100%;
  min-width: 0;
  min-height: 44px;
  padding: 1rem;
  border: 1px solid var(--sumi-divider) !important;
  background: none !important;
  color: var(--sumi-text) !important;
  font-family: "Plus Jakarta Sans", system-ui, sans-serif;
  font-size: 15px;
  line-height: 26px;
  font-weight: 400;
  text-decoration: none !important;
  box-sizing: border-box;
}
html:is([lang="id"], [lang="en"], [lang="ja"]) body.layout--single #main .page__content a.contact-btn {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  justify-content: space-between;
  column-gap: 1rem;
  row-gap: 0.25rem;
}
html:is([lang="id"], [lang="en"], [lang="ja"]) body.layout--single #main .page__content a.contact-btn-col {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  gap: 0.5rem;
}
@media (hover: hover) {
  html:is([lang="id"], [lang="en"], [lang="ja"]) body.layout--single #main .page__content a.contact-btn:hover,
  html:is([lang="id"], [lang="en"], [lang="ja"]) body.layout--single #main .page__content a.contact-btn-col:hover {
    background: none !important;
    color: var(--sumi-accent) !important;
    border-color: var(--sumi-accent) !important;
    text-decoration: none !important;
  }
  html:is([lang="id"], [lang="en"], [lang="ja"]) body.layout--single #main .page__content a.contact-btn:hover .contact-platform,
  html:is([lang="id"], [lang="en"], [lang="ja"]) body.layout--single #main .page__content a.contact-btn:hover .contact-text,
  html:is([lang="id"], [lang="en"], [lang="ja"]) body.layout--single #main .page__content a.contact-btn-col:hover .contact-platform,
  html:is([lang="id"], [lang="en"], [lang="ja"]) body.layout--single #main .page__content a.contact-btn-col:hover .contact-text {
    color: var(--sumi-accent) !important;
  }
}
html:is([lang="id"], [lang="en"], [lang="ja"]) body.layout--single #main .page__content a.contact-btn:focus,
html:is([lang="id"], [lang="en"], [lang="ja"]) body.layout--single #main .page__content a.contact-btn-col:focus {
  outline: none;
}
html:is([lang="id"], [lang="en"], [lang="ja"]) body.layout--single #main .page__content a.contact-btn:active,
html:is([lang="id"], [lang="en"], [lang="ja"]) body.layout--single #main .page__content a.contact-btn:focus-visible,
html:is([lang="id"], [lang="en"], [lang="ja"]) body.layout--single #main .page__content a.contact-btn-col:active,
html:is([lang="id"], [lang="en"], [lang="ja"]) body.layout--single #main .page__content a.contact-btn-col:focus-visible {
  background: none !important;
  color: var(--sumi-accent) !important;
  border-color: var(--sumi-accent) !important;
  text-decoration: none !important;
}
html:is([lang="id"], [lang="en"], [lang="ja"]) body.layout--single #main .page__content a.contact-btn:active .contact-platform,
html:is([lang="id"], [lang="en"], [lang="ja"]) body.layout--single #main .page__content a.contact-btn:active .contact-text,
html:is([lang="id"], [lang="en"], [lang="ja"]) body.layout--single #main .page__content a.contact-btn:focus-visible .contact-platform,
html:is([lang="id"], [lang="en"], [lang="ja"]) body.layout--single #main .page__content a.contact-btn:focus-visible .contact-text,
html:is([lang="id"], [lang="en"], [lang="ja"]) body.layout--single #main .page__content a.contact-btn-col:active .contact-platform,
html:is([lang="id"], [lang="en"], [lang="ja"]) body.layout--single #main .page__content a.contact-btn-col:active .contact-text,
html:is([lang="id"], [lang="en"], [lang="ja"]) body.layout--single #main .page__content a.contact-btn-col:focus-visible .contact-platform,
html:is([lang="id"], [lang="en"], [lang="ja"]) body.layout--single #main .page__content a.contact-btn-col:focus-visible .contact-text {
  color: var(--sumi-accent) !important;
}
html:is([lang="id"], [lang="en"], [lang="ja"]) body.layout--single #main .page__content a.contact-btn:focus-visible,
html:is([lang="id"], [lang="en"], [lang="ja"]) body.layout--single #main .page__content a.contact-btn-col:focus-visible {
  outline: 2px solid var(--sumi-text) !important;
  outline-offset: 2px !important;
}
html:is([lang="id"], [lang="en"], [lang="ja"]) body.layout--single #main .page__content .contact-platform {
  flex-shrink: 0;
  margin: 0;
  font-family: "Plus Jakarta Sans", system-ui, sans-serif;
  font-size: 15px;
  line-height: 26px;
  font-weight: 600;
  color: var(--sumi-text);
}
html:is([lang="id"], [lang="en"], [lang="ja"]) body.layout--single #main .page__content .contact-text {
  min-width: 0;
  max-width: 100%;
  margin: 0 0 0 auto;
  font-family: "Plus Jakarta Sans", system-ui, sans-serif;
  font-size: 15px;
  line-height: 26px;
  font-weight: 400;
  color: var(--sumi-text-secondary);
  text-align: right;
  word-break: normal;
  overflow-wrap: break-word;
}
html:is([lang="id"], [lang="en"], [lang="ja"]) body.layout--single #main .page__content .yt-header {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: baseline;
  column-gap: 1rem;
  row-gap: 0.25rem;
  width: 100%;
}
html:is([lang="id"], [lang="en"], [lang="ja"]) body.layout--single #main .page__content .yt-desc {
  margin: 0;
  width: 100%;
  font-family: "Plus Jakarta Sans", system-ui, sans-serif;
  font-size: 15px;
  line-height: 26px;
  font-weight: 400;
  color: var(--sumi-text-secondary);
  overflow-wrap: break-word;
}
</style>

<div class="contact-group">
  <h2 id="professional">Professional</h2>
  <ul class="contact-links">
    <li>
      <a href="https://www.linkedin.com/in/mizoridh" class="contact-btn" target="_blank" rel="noopener noreferrer">
        <span class="contact-platform">LinkedIn</span>
      </a>
    </li>
    <li>
      <a href="https://www.wantedly.com/id/muhammad_ali_ridho" class="contact-btn" target="_blank" rel="noopener noreferrer">
        <span class="contact-platform">Wantedly</span>
      </a>
    </li>
    <li>
      <a href="https://github.com/mizoarkatamarenaldy" class="contact-btn" target="_blank" rel="noopener noreferrer">
        <span class="contact-platform">GitHub</span>
        <span class="contact-text">@mizoarkatamarenaldy</span>
      </a>
    </li>
  </ul>
</div>

<div class="contact-group">
  <h2 id="direct-message">Direct Message</h2>
  <ul class="contact-links">
    <li>
      <a href="mailto:mizoarkatamarenaldy@gmail.com" class="contact-btn" target="_blank" rel="noopener noreferrer">
        <span class="contact-platform">Email</span>
        <span class="contact-text">mizoarkatamarenaldy@gmail.com</span>
      </a>
    </li>
    <li>
      <a href="https://wa.me/6283866291451" class="contact-btn" target="_blank" rel="noopener noreferrer">
        <span class="contact-platform">WhatsApp</span>
        <span class="contact-text">WhatsApp Business</span>
      </a>
    </li>
    <li>
      <a href="https://discord.com/users/620568059446296586" class="contact-btn" target="_blank" rel="noopener noreferrer">
        <span class="contact-platform">Discord</span>
        <span class="contact-text">mizoarkatamarenaldy</span>
      </a>
    </li>
    <li>
      <a href="https://line.me/ti/p/~mizoarkatamarenaldy" class="contact-btn" target="_blank" rel="noopener noreferrer">
        <span class="contact-platform">LINE</span>
        <span class="contact-text">mizoarkatamarenaldy</span>
      </a>
    </li>
  </ul>
</div>

<div class="contact-group">
  <h2 id="social">Social</h2>
  <ul class="contact-links">
    <li>
      <a href="https://www.instagram.com/mizoarkatamarenaldy/" class="contact-btn" target="_blank" rel="noopener noreferrer">
        <span class="contact-platform">Instagram</span>
        <span class="contact-text">@mizoarkatamarenaldy</span>
      </a>
    </li>
    <li>
      <a href="https://www.threads.com/@mizoarkatamarenaldy" class="contact-btn" target="_blank" rel="noopener noreferrer">
        <span class="contact-platform">Threads</span>
        <span class="contact-text">@mizoarkatamarenaldy</span>
      </a>
    </li>
    <li>
      <a href="https://tiktok.com/@mizoarkatamarenaldy" class="contact-btn" target="_blank" rel="noopener noreferrer">
        <span class="contact-platform">TikTok</span>
        <span class="contact-text">@mizoarkatamarenaldy</span>
      </a>
    </li>
    <li>
      <a href="https://x.com/mizoarkrenaldy" class="contact-btn" target="_blank" rel="noopener noreferrer">
        <span class="contact-platform">X</span>
        <span class="contact-text">@mizoarkrenaldy</span>
      </a>
    </li>
    <li>
      <a href="https://facebook.com/MizoArkatamaRenaldy" class="contact-btn" target="_blank" rel="noopener noreferrer">
        <span class="contact-platform">Facebook</span>
        <span class="contact-text">Mizo Arkatama Renaldy</span>
      </a>
    </li>
    <li>
      <a href="https://id.quora.com/profile/Mizo-Arkatama-Renaldy/" class="contact-btn" target="_blank" rel="noopener noreferrer">
        <span class="contact-platform">Quora</span>
        <span class="contact-text">Mizo Arkatama Renaldy</span>
      </a>
    </li>
  </ul>
</div>

<div class="contact-group">
  <h2 id="youtube">YouTube</h2>
  <ul class="contact-links">
    <li>
      <a href="https://www.youtube.com/@MizoArkatamaRenaldy" class="contact-btn-col" target="_blank" rel="noopener noreferrer">
        <div class="yt-header">
          <span class="contact-platform">YouTube</span>
          <span class="contact-text">@MizoArkatamaRenaldy</span>
        </div>
        <div class="yt-desc">main channel, psychology and others</div>
      </a>
    </li>
    <li>
      <a href="https://www.youtube.com/@MizoAR" class="contact-btn-col" target="_blank" rel="noopener noreferrer">
        <div class="yt-header">
          <span class="contact-platform">YouTube</span>
          <span class="contact-text">@MizoAR</span>
        </div>
        <div class="yt-desc">gaming</div>
      </a>
    </li>
    <li>
      <a href="https://www.youtube.com/@MizoKoubou" class="contact-btn-col" target="_blank" rel="noopener noreferrer">
        <div class="yt-header">
          <span class="contact-platform">YouTube</span>
          <span class="contact-text">@MizoKoubou</span>
        </div>
        <div class="yt-desc">other random stuff</div>
      </a>
    </li>
  </ul>
</div>
