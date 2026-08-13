# My Kurtains — Website

A modern, fast, single-page marketing site for **My Kurtains**, Montreal's custom blinds & curtains studio.
*High style, low cost — custom motorized & manual blinds with free professional installation.*

## ✨ Features

- **Zero build step** — pure HTML, CSS and vanilla JS. Open it and it works.
- Fully responsive, mobile-first, with a glassmorphic sticky nav.
- Scroll-reveal animations, animated hero, marquee, hover micro-interactions.
- Sections: hero, collections, why-us, process, gallery, reviews, contact form + footer.
- Floating WhatsApp button and a lead form that hands off to WhatsApp.
- Accessible: semantic HTML, reduced-motion support, keyboard-friendly nav.
- SEO + Open Graph tags for good link previews.

## 📁 Structure

```
.
├── index.html      # all page markup
├── styles.css      # design system + all styles
├── script.js       # nav, scroll-reveal, form handoff
├── assets/
│   └── favicon.svg
└── README.md
```

## 🚀 Run locally

No dependencies. Either open `index.html` directly, or serve it:

```bash
python3 -m http.server 8000
```

Then visit http://localhost:8000

## 🌐 Deploy

Drag-and-drop or connect the repo to any static host:

- **Vercel** — `vercel` (or import the repo, framework: *Other*)
- **Netlify** — drag the folder into the dashboard, or connect the repo
- **GitHub Pages** — Settings → Pages → deploy from `main` / root
- **Cloudflare Pages** — connect repo, build command: *(none)*, output dir: `/`

Point your `mykurtains.com` DNS at the host once deployed.

## 🔧 Customize

| What | Where |
|------|-------|
| Colors / fonts / spacing | CSS variables at the top of `styles.css` (`:root`) |
| Phone / WhatsApp / email | Search `4384020559` and `hello@mykurtains.com` in `index.html` |
| Photos | `<img src="…">` URLs (currently Unsplash placeholders — swap for real project photos) |
| Reviews | `#reviews` section in `index.html` |
| Social links | Footer `#` links in `index.html` |

### Wire up the contact form

The form currently opens a pre-filled WhatsApp message so no lead is lost. To receive
submissions by email instead, point it at a service like **Formspree**, **Netlify Forms**,
or **Web3Forms** — swap the handler in `script.js` for a `fetch()` to your endpoint.

## 📝 Notes

- Replace the Unsplash placeholder images with real photos of your work for the biggest impact.
- Add real Instagram/Facebook URLs in the footer.
- Optional: add a Google Reviews widget for live star ratings.
