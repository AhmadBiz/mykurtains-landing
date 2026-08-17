#!/usr/bin/env python3
"""
Generates the blog post HTML files from POSTS below using one shared template.
Run:  python3 blog/_build_posts.py
The generated files are committed; this script is just the authoring tool.
"""
import json, os, html

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = "https://www.mykurtains.com"

# ---------------------------------------------------------------- i18n
LANG = {
  "en": dict(code="en", dir="", up="../", blogdir="blog/", other="fr", other_dir="fr/", other_label="FR", other_aria="Voir ce guide en français",
    site_home="../index.html", nav=[("../index.html#collections","Collections"),("../index.html#why","Why Us"),("../index.html#process","How It Works"),("index.html","Guides"),("../index.html#reviews","Reviews")],
    phone_btn="438&nbsp;402&nbsp;0559", consult="Free Consultation", book="Book Free Consultation", book_long="Book a free consultation",
    contact="../index.html#contact", brand_tag="High style, low cost. Custom blinds, curtains &amp; smart film, made and installed across Montreal.",
    f_explore="Explore", f_collections="Collections", f_guides="Guides &amp; advice", f_how="How It Works", f_reviews="Reviews", f_contact="Get in touch", f_follow="Follow",
    f_bar="Made with care for beautiful windows.", f_city="Montreal, QC", wa_aria="Message us on WhatsApp",
    kind_guide="Product guide", kind_advice="Advice", crumb_guides="Guides", crumb_advice="Advice", home="Home",
    read="min read", updated="Updated Aug 2026", city="Montreal, QC", pros="Pros", cons="Cons", glance="At a glance", faq="Frequently asked questions",
    all_guides="All product guides", talk_h="Prefer to talk?", talk_p="Call or WhatsApp us — we answer fast.", keep="Keep reading", related="Related guides",
    read_more="Read →", title_suffix=" | My Kurtains Montreal", site_name="My Kurtains", locale="en_CA"),
  "fr": dict(code="fr", dir="fr/", up="../../", blogdir="blog/fr/", other="en", other_dir="", other_label="EN", other_aria="Read this guide in English",
    site_home="../../index-fr.html", nav=[("../../index-fr.html#collections","Collections"),("../../index-fr.html#why","Pourquoi nous"),("../../index-fr.html#process","Comment ça marche"),("index.html","Guides"),("../../index-fr.html#reviews","Avis")],
    phone_btn="438&nbsp;402&nbsp;0559", consult="Consultation gratuite", book="Réserver une consultation gratuite", book_long="Réserver une consultation gratuite",
    contact="../../index-fr.html#contact", brand_tag="Beaucoup de style, à petit prix. Stores, rideaux et film intelligent, fabriqués et installés partout à Montréal.",
    f_explore="Explorer", f_collections="Collections", f_guides="Guides et conseils", f_how="Comment ça marche", f_reviews="Avis", f_contact="Nous joindre", f_follow="Suivez-nous",
    f_bar="Conçu avec soin pour de belles fenêtres.", f_city="Montréal, QC", wa_aria="Écrivez-nous sur WhatsApp",
    kind_guide="Guide produit", kind_advice="Conseils", crumb_guides="Guides", crumb_advice="Conseils", home="Accueil",
    read="min de lecture", updated="Mis à jour août 2026", city="Montréal, QC", pros="Avantages", cons="Inconvénients", glance="En un coup d’œil", faq="Questions fréquentes",
    all_guides="Tous les guides produits", talk_h="Vous préférez parler ?", talk_p="Appelez-nous ou écrivez-nous sur WhatsApp — on répond vite.", keep="À lire aussi", related="Guides connexes",
    read_more="Lire →", title_suffix=" | My Kurtains Montréal", site_name="My Kurtains", locale="fr_CA"),
}
GUIDES_FR = [
    ("honeycomb-blinds.html", "Stores alvéolaires"),
    ("roller-blinds.html", "Stores enrouleurs"),
    ("curtains-and-drapes.html", "Rideaux et draperies"),
    ("roman-shades.html", "Stores bateau"),
    ("day-and-night-zebra-blinds.html", "Jour et nuit (zébrés)"),
    ("motorized-blinds.html", "Stores motorisés"),
    ("blackout-blinds.html", "Store Blockout"),
    ("outdoor-blinds.html", "Stores extérieurs"),
    ("smart-film.html", "Film intelligent"),
]

GUIDES = [
    ("honeycomb-blinds.html", "Honeycomb blinds"),
    ("roller-blinds.html", "Roller blinds"),
    ("curtains-and-drapes.html", "Curtains &amp; drapes"),
    ("roman-shades.html", "Roman shades"),
    ("day-and-night-zebra-blinds.html", "Day &amp; night (zebra)"),
    ("motorized-blinds.html", "Motorized blinds"),
    ("blackout-blinds.html", "Blockout Blind"),
    ("outdoor-blinds.html", "Outdoor blinds"),
    ("smart-film.html", "Smart film"),
]

LOGO = '<svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="32" cy="32" r="26" stroke="currentColor" stroke-width="3"/><g stroke="currentColor" stroke-width="3" stroke-linecap="round"><line x1="9" y1="32" x2="29.5" y2="32"/><line x1="34.5" y1="32" x2="55" y2="32"/><line x1="32" y1="9" x2="32" y2="55"/><line x1="25" y1="10.1" x2="25" y2="53.9"/><line x1="39" y1="10.1" x2="39" y2="53.9"/><line x1="18" y1="32" x2="18" y2="50.25"/><line x1="46" y1="13.75" x2="46" y2="32"/></g></svg>'
WA = '<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M12.04 2c-5.46 0-9.9 4.44-9.9 9.9 0 1.75.46 3.45 1.32 4.95L2 22l5.28-1.38a9.86 9.86 0 004.76 1.22h.004c5.46 0 9.9-4.44 9.9-9.9 0-2.64-1.03-5.13-2.9-7A9.82 9.82 0 0012.04 2zm5.8 14.2c-.24.68-1.42 1.32-1.95 1.36-.5.05-.98.24-3.33-.7-2.8-1.1-4.6-3.96-4.74-4.14-.14-.18-1.15-1.53-1.15-2.92s.73-2.07.98-2.35c.26-.28.56-.35.75-.35.18 0 .37 0 .53.01.17.01.4-.06.62.47.24.56.8 1.95.87 2.1.07.14.12.3.02.48-.1.18-.14.3-.28.46-.14.16-.3.36-.42.48-.14.14-.28.29-.12.57.16.28.72 1.18 1.54 1.9 1.06.94 1.95 1.24 2.23 1.38.28.14.44.12.6-.07.18-.2.7-.8.88-1.08.18-.28.36-.24.6-.14.24.09 1.55.73 1.82.86.26.14.44.2.5.32.06.11.06.66-.18 1.34z"/></svg>'


def dots(n):
    return '<span class="dots">' + ''.join('<i class="on"></i>' if i < n else '<i></i>' for i in range(5)) + '</span>'


def render(p, lang="en"):
    L = LANG[lang]
    slug = p["slug"]
    is_guide = p["type"] == "guide"
    kind = L["kind_guide"] if is_guide else L["kind_advice"]
    crumb = L["crumb_guides"] if is_guide else L["crumb_advice"]
    url = f"{SITE}/{L['blogdir']}{slug}"
    alt_url = f"{SITE}/blog/{LANG[L['other']]['dir']}{slug}"
    up = L["up"]
    guides = GUIDES if lang == "en" else GUIDES_FR

    article_ld = {
        "@context": "https://schema.org", "@type": "Article", "inLanguage": lang,
        "headline": p["title"], "description": p["description"], "image": p["image"].replace("../assets", f"{SITE}/assets"),
        "author": {"@type": "Organization", "name": "My Kurtains"},
        "publisher": {"@type": "Organization", "name": "My Kurtains",
                      "logo": {"@type": "ImageObject", "url": f"{SITE}/assets/favicon.svg"}},
        "datePublished": "2026-08-15", "dateModified": "2026-08-15", "mainEntityOfPage": url,
    }
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage",
              "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]}

    proscons = ""
    if p.get("pros"):
        proscons = (f'<div class="proscons"><div class="pros"><h4>{L["pros"]}</h4><ul>' +
                    ''.join(f'<li>{x}</li>' for x in p["pros"]) +
                    f'</ul></div><div class="cons"><h4>{L["cons"]}</h4><ul>' +
                    ''.join(f'<li>{x}</li>' for x in p["cons"]) + '</ul></div></div>')

    glance = ""
    if p.get("glance"):
        rows = ""
        for k, v in p["glance"]:
            if isinstance(v, tuple):
                rows += f'<tr><th>{k}</th><td>{dots(v[0])} &nbsp;{v[1]}</td></tr>'
            else:
                rows += f'<tr><th>{k}</th><td>{v}</td></tr>'
        glance = f'<h2>{L["glance"]}</h2><table class="specs">{rows}</table>'

    faq_html = f'<h2>{L["faq"]}</h2><div class="faq">' + ''.join(
        f'<details><summary>{html.escape(q)}</summary><p>{a}</p></details>' for q, a in p["faq"]) + '</div>'

    aside_links = ''.join(
        '<li><a href="%s"%s>%s</a></li>' % (f, ' class="is-current"' if f == slug else '', n) for f, n in guides)

    related = ''.join(
        f'<a class="post-card" href="{r["href"]}"><div class="post-card__img"><img src="{r["img"].replace("../assets", up + "assets")}" alt="" loading="lazy" /></div>'
        f'<div class="post-card__body"><div class="post-card__meta"><span class="tag">{r["tag"]}</span><span>{r["cat"]}</span></div>'
        f'<h3>{r["title"]}</h3><p>{r["blurb"]}</p><span class="post-card__more">{L["read_more"]}</span></div></a>' for r in p["related"])

    nav_links = ''.join(f'<a href="{h}">{t}</a>' for h, t in L["nav"])
    lang_btn = f'<a href="{"../" if lang=="en" else ""}{"fr/" if lang=="en" else "../"}{slug}" class="btn btn--ghost btn--sm lang-switch" hreflang="{L["other"]}" aria-label="{L["other_aria"]}">{L["other_label"]}</a>'
    # fix: EN post -> fr/<slug>; FR post -> ../<slug>
    lang_btn = f'<a href="{("fr/" if lang=="en" else "../")}{slug}" class="btn btn--ghost btn--sm lang-switch" hreflang="{L["other"]}" aria-label="{L["other_aria"]}">{L["other_label"]}</a>'
    img_src = p["image"].replace("../assets", up + "assets")

    nav = f"""
  <header class="nav nav--light scrolled" id="nav">
    <div class="nav__inner container">
      <a href="{L['site_home']}" class="brand" aria-label="My Kurtains"><span class="brand__mark" aria-hidden="true">{LOGO}</span><span class="brand__name">My<em>Kurtains</em></span></a>
      <nav class="nav__links" aria-label="Primary">{nav_links}</nav>
      <div class="nav__cta">{lang_btn}<a href="tel:+14384020559" class="btn btn--ghost btn--sm">{L['phone_btn']}</a><a href="{L['contact']}" class="btn btn--solid btn--sm" data-calendly>{L['consult']}</a></div>
      <button class="nav__toggle" id="navToggle" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
    <div class="nav__mobile" id="navMobile">{nav_links}
      <a href="{("fr/" if lang=="en" else "../")}{slug}" hreflang="{L['other']}" class="nav__mobile-lang">{L['other_aria']} →</a>
      <a href="{L['contact']}" class="btn btn--solid" data-calendly>{L['book']}</a>
    </div>
  </header>"""

    footer = f"""
  <footer class="footer">
    <div class="container footer__inner">
      <div class="footer__brand"><span class="brand__name">My<em>Kurtains</em></span><p>{L['brand_tag']}</p></div>
      <nav class="footer__col" aria-label="Sitemap"><h4>{L['f_explore']}</h4><a href="{L['site_home']}#collections">{L['f_collections']}</a><a href="index.html">{L['f_guides']}</a><a href="{L['site_home']}#process">{L['f_how']}</a><a href="{L['site_home']}#reviews">{L['f_reviews']}</a></nav>
      <nav class="footer__col" aria-label="Contact"><h4>{L['f_contact']}</h4><a href="tel:+14384020559">+1 (438) 402-0559</a><a href="mailto:hello@mykurtains.com">hello@mykurtains.com</a><a href="https://wa.me/14384020559" target="_blank" rel="noopener">WhatsApp</a></nav>
      <div class="footer__col"><h4>{L['f_follow']}</h4><div class="footer__social"><a href="https://www.instagram.com/mykurtains/" target="_blank" rel="noopener">Instagram</a><a href="https://www.facebook.com/mykurtains" target="_blank" rel="noopener">Facebook</a></div></div>
    </div>
    <div class="footer__bar container"><span>© <span id="year"></span> My Kurtains — {L['f_city']}</span><span>{L['f_bar']}</span></div>
  </footer>
  <a href="https://wa.me/14384020559" class="fab" target="_blank" rel="noopener" aria-label="{L['wa_aria']}">{WA}</a>"""

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="theme-color" content="#141210" />
  <title>{html.escape(p["title"])}{L['title_suffix']}</title>
  <meta name="description" content="{html.escape(p["description"])}" />
  <link rel="canonical" href="{url}" />
  <link rel="alternate" hreflang="en" href="{SITE}/blog/{slug}" />
  <link rel="alternate" hreflang="fr" href="{SITE}/blog/fr/{slug}" />
  <link rel="alternate" hreflang="x-default" href="{SITE}/blog/{slug}" />
  <meta property="og:type" content="article" />
  <meta property="og:locale" content="{L['locale']}" />
  <meta property="og:title" content="{html.escape(p["title"])}" />
  <meta property="og:description" content="{html.escape(p["og"])}" />
  <meta property="og:image" content="{p["image"].replace("../assets", SITE + "/assets")}" />
  <script type="application/ld+json">{json.dumps(article_ld, ensure_ascii=False)}</script>
  <script type="application/ld+json">{json.dumps(faq_ld, ensure_ascii=False)}</script>
  <link rel="icon" href="{up}assets/favicon.svg" type="image/svg+xml" />
  <link rel="icon" type="image/png" sizes="32x32" href="{up}assets/favicon-32.png" />
  <link rel="icon" type="image/png" sizes="192x192" href="{up}assets/favicon-192.png" />
  <link rel="apple-touch-icon" sizes="180x180" href="{up}assets/apple-touch-icon.png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..700;1,9..144,400&family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="{up}styles.css" />
  <link rel="stylesheet" href="{"../" if lang=="fr" else ""}blog.css" />
  <link rel="stylesheet" href="https://assets.calendly.com/assets/external/widget.css" />
  <script src="https://assets.calendly.com/assets/external/widget.js" async></script>
</head>
<body>
{nav}
  <main>
    <section class="post-hero">
      <div class="container post-hero__inner">
        <div>
          <nav class="crumbs" aria-label="Breadcrumb"><a href="{L['site_home']}">{L['home']}</a><span>/</span><a href="index.html">{crumb}</a><span>/</span><span>{p["crumb"]}</span></nav>
          <p class="eyebrow" style="margin-top:1.2rem">{kind}</p>
          <h1>{p["h1"]}</h1>
          <p class="lede">{p["lede"]}</p>
          <div class="post-hero__meta"><span>{p["read"]} {L['read']}</span><span>{L['updated']}</span><span>{L['city']}</span></div>
        </div>
        <figure class="post-hero__media"><img src="{img_src}" alt="{html.escape(p["alt"])}" /></figure>
      </div>
    </section>

    <div class="container post-layout">
      <article class="post-body">
{p["body"].replace("../assets", up + "assets")}
{proscons}
{glance}
{p.get("body2","").replace("../assets", up + "assets")}
{faq_html}
      </article>

      <aside class="post-aside">
        <div class="aside-card aside-card--dark">
          <h4>{p["aside_h"]}</h4>
          <p>{p["aside_p"]}</p>
          <a href="{L['contact']}" class="btn btn--solid" data-calendly>{L['book_long']}</a>
        </div>
        <div class="aside-card"><h4>{L['all_guides']}</h4><ul class="aside-links">{aside_links}</ul></div>
        <div class="aside-card"><h4>{L['talk_h']}</h4><p>{L['talk_p']}</p>
          <a href="tel:+14384020559" class="btn btn--ghost" style="margin-bottom:.6rem">+1 (438) 402-0559</a>
          <a href="https://wa.me/14384020559" target="_blank" rel="noopener" class="btn btn--ghost">WhatsApp</a></div>
      </aside>
    </div>

    <section class="post-cta">
      <div class="container post-cta__inner">
        <div><h2>{p["cta_h"]}</h2><p>{p["cta_p"]}</p></div>
        <a href="{L['contact']}" class="btn btn--solid btn--lg" data-calendly>{L['book_long']}</a>
      </div>
    </section>

    <section class="related">
      <div class="container">
        <header class="section__head section__head--left"><p class="eyebrow">{L['keep']}</p><h2 class="section__title">{L['related']}</h2></header>
        <div class="posts__grid">{related}</div>
      </div>
    </section>
  </main>
{footer}
  <script src="{up}script.js"></script>
</body>
</html>
"""


# ============================================================================
# CONTENT
# ============================================================================
IMG = {
    "roller": "../assets/roller.jpg",
    "curtains": "https://images.unsplash.com/photo-1493809842364-78817add7ffb?auto=format&fit=crop&w=1200&q=80",
    "roman": "../assets/roman.jpg",
    "zebra": "../assets/zebra.jpg",
    "motor": "https://images.unsplash.com/photo-1598928506311-c55ded91a20c?auto=format&fit=crop&w=1200&q=80",
    "blackout": "../assets/blockout.jpg",
    "outdoor": "https://images.unsplash.com/photo-1571003123894-1f0594d2b5d9?auto=format&fit=crop&w=1200&q=80",
    "film": "https://images.unsplash.com/photo-1524758631624-e2822e304c36?auto=format&fit=crop&w=1200&q=80",
    "honey": "../assets/honeycomb.jpg",
    "living": "https://images.unsplash.com/photo-1493809842364-78817add7ffb?auto=format&fit=crop&w=1200&q=80",
    "bedroom": "https://images.unsplash.com/photo-1502005229762-cf1b2da7c5d6?auto=format&fit=crop&w=1200&q=80",
    "calm": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?auto=format&fit=crop&w=1200&q=80",
    "measure": "https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=1200&q=80",
    "condo": "https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?auto=format&fit=crop&w=1200&q=80",
}


def rel(href, img, tag, cat, title, blurb):
    return {"href": href, "img": img.replace("w=1200", "w=800"), "tag": tag, "cat": cat, "title": title, "blurb": blurb}


R = {
    "honey": rel("honeycomb-blinds.html", IMG["honey"], "Guide", "Honeycomb", "Honeycomb (Cellular) Blinds", "The most energy-efficient blind."),
    "roller": rel("roller-blinds.html", IMG["roller"], "Guide", "Roller", "Roller Blinds: The Complete Guide", "Clean, minimal, versatile."),
    "curtains": rel("curtains-and-drapes.html", IMG["curtains"], "Guide", "Curtains", "Curtains &amp; Drapes", "Fabrics, fullness and the drop."),
    "roman": rel("roman-shades.html", IMG["roman"], "Guide", "Roman", "Roman Shades", "Tailored folds, quiet luxury."),
    "zebra": rel("day-and-night-zebra-blinds.html", IMG["zebra"], "Guide", "Zebra", "Day &amp; Night (Zebra) Blinds", "Privacy and daylight from one blind."),
    "motor": rel("motorized-blinds.html", IMG["motor"], "Guide", "Motorized", "Motorized Blinds: Worth It?", "What automation really adds."),
    "blackout": rel("blackout-blinds.html", IMG["blackout"], "Guide", "Blockout", "Blockout Blind: 100% Darkness", "A framed, edge-sealed shade — no light leaks."),
    "outdoor": rel("outdoor-blinds.html", IMG["outdoor"], "Guide", "Outdoor", "Outdoor Blinds", "Shade for patios and balconies."),
    "film": rel("smart-film.html", IMG["film"], "Guide", "Smart film", "Smart Film", "Privacy glass at a touch."),
    "vs": rel("blinds-vs-curtains.html", IMG["living"], "Advice", "Choosing", "Blinds vs Curtains", "Which is right for your room?"),
    "winter": rel("best-blinds-for-montreal-winters.html", IMG["bedroom"], "Advice", "Insulation", "Best Blinds for Montreal Winters", "What actually helps, ranked."),
    "nursery": rel("blackout-blinds-for-nursery.html", IMG["calm"], "Advice", "Sleep", "Blackout Blinds for a Nursery", "A parent’s guide to better naps."),
    "measure": rel("how-to-measure-windows-for-blinds.html", IMG["measure"], "Advice", "How-to", "How to Measure Windows for Blinds", "Inside vs outside mount."),
    "condo": rel("blinds-for-condos-and-apartments.html", IMG["condo"], "Advice", "Condos", "Best Blinds for Condos", "Privacy without losing the view."),
}

POSTS = [
# ---------------------------------------------------------------- HONEYCOMB
dict(slug="honeycomb-blinds.html", type="guide", crumb="Honeycomb blinds", read=7, image=IMG["honey"],
 alt="A top-down honeycomb blind: sheer at the top letting light in, blackout cells below",
 title="Honeycomb (Cellular) Blinds: How They Work, Pros & Cons",
 description="Honeycomb blinds explained: how the cellular design insulates your windows, single vs double cell, top-down/bottom-up, blackout options, honest pros and cons, and whether they're right for your Montreal home.",
 og="The most energy-efficient blind you can buy — and why Montreal winters make them worth it.",
 h1="Honeycomb blinds: the quiet <em>overachiever</em> of window coverings.",
 lede="They look soft and simple. Underneath, a row of air-filled cells is doing serious work — insulating your windows, softening light and muffling street noise. Here’s how they work, honestly what they’re good and bad at, and whether they belong in your home.",
 body="""
        <h2>What is a honeycomb blind?</h2>
        <p>Also called <strong>cellular shades</strong>, honeycomb blinds are made from pleated fabric bonded into a row of hexagonal cells — look at one from the side and you’ll see the honeycomb shape that gives them their name. Each cell traps a pocket of still air between your window and the room.</p>
        <p>That trapped air is the whole point. Still air is a poor conductor of heat, so a honeycomb blind acts like an extra layer of insulation on the glass — the same principle as a down jacket. Of every blind and shade type, cellular shades are consistently the best insulators.</p>
        <h2>How they work</h2>
        <p>The fabric is folded accordion-style and glued so the pleats form closed cells. Raise the shade and it stacks flat and small at the top; lower it and the cells open into their full depth. Because there are no slats or cords running through the fabric, the face is smooth and light passes through it evenly — no stripes, no glare lines.</p>
        <p>You choose the fabric opacity to set how much light comes through:</p>
        <ul>
          <li><strong>Sheer / light-filtering</strong> — a soft, glowing daylight, with daytime privacy.</li>
          <li><strong>Semi-opaque</strong> — more shade, still gentle light.</li>
          <li><strong>Blackout</strong> — an opaque lining inside the cell for near-total darkness (see below).</li>
        </ul>
        <h3>Single cell vs. double cell</h3>
        <p><strong>Single cell</strong> shades have one layer of pockets and are the everyday choice — light, slim and effective. <strong>Double cell</strong> shades nest a second row of cells inside the first, roughly doubling the insulating value and blocking a touch more sound. They’re a little thicker and cost more, so we recommend them for the coldest rooms: big north-facing windows, drafty older Montreal homes, and bedrooms above a garage.</p>
        <h3>Top-down / bottom-up</h3>
        <p>This is the honeycomb feature people fall in love with. The shade can be <em>lowered from the top</em> as well as raised from the bottom — so you can let daylight and sky in through the upper part of the window while keeping the lower part covered for privacy. It’s ideal for street-facing rooms and bathrooms. The photo at the top of this page shows exactly that: light through the top, blackout below.</p>
        <figure>
          <img src="../assets/honeycomb.jpg" alt="Honeycomb blind partially lowered from the top, showing the sheer upper section and blackout lower section" />
          <figcaption>A real installation of ours: top-down honeycomb, sheer above, blackout cells below.</figcaption>
        </figure>
        <h2>Honest pros and cons</h2>""",
 pros=["<strong>Best insulation of any blind</strong> — noticeably warmer in winter, cooler in summer, lower bills.", "<strong>Soft, even light</strong> with no slat lines or glare.", "<strong>Top-down / bottom-up</strong> privacy without losing daylight.", "<strong>Quiet room</strong> — the cells absorb some outside noise.", "<strong>Stacks very small</strong> when raised — you keep the whole view.", "<strong>Cordless and motorized</strong> options — clean look, child-safe.", "<strong>Blackout available</strong> for bedrooms and nurseries."],
 cons=["<strong>Less “decorative”</strong> than curtains or Roman shades — a clean, minimal look rather than a statement.", "<strong>Cleaning takes care</strong> — dust with a soft brush or vacuum on low; not machine-washable.", "<strong>Cells can trap insects or dust</strong> in the top pleats over years.", "<strong>Blackout needs side channels</strong> for true darkness (light leaks at the edges otherwise — see our <a href='blackout-blinds.html'>blackout guide</a>).", "<strong>Not for high-humidity outdoors</strong> — for balconies see <a href='outdoor-blinds.html'>outdoor blinds</a>."],
 glance=[("Insulation", (5, "Best in class")), ("Light control", (4, "Sheer to full blackout")), ("Privacy", (5, "Excellent, esp. top-down")), ("Style", (3, "Clean &amp; minimal")), ("Maintenance", (3, "Dust / vacuum gently")), ("Best rooms", "Bedrooms, living rooms, home offices, nurseries, north-facing &amp; large windows"), ("Options", "Single or double cell · sheer / semi / blackout · top-down/bottom-up · cordless · motorized")],
 body2="""
        <h2>Who they’re perfect for</h2>
        <p><strong>If your window is cold to stand near in January, this is your blind.</strong> Honeycomb shades are the answer for anyone who wants real comfort and lower heating bills without wrapping their windows in heavy curtains. They suit modern and minimalist interiors, and — with top-down/bottom-up — any room that faces the street or a neighbour.</p>
        <p>They’re also our go-to for <strong>bedrooms and nurseries</strong>, where the combination of blackout, insulation and quiet is hard to beat.</p>
        <div class="callout"><strong>Montreal tip</strong><p>Windows are usually the weakest point of a home’s insulation. On a large or older window, a double-cell honeycomb shade can make a room feel a full degree or two warmer at the same thermostat setting — you notice it most on the coldest nights.</p></div>
        <h2>When to choose something else</h2>
        <ul>
          <li>Want drama, softness or colour on the wall? Look at <a href="curtains-and-drapes.html">curtains &amp; drapes</a> or <a href="roman-shades.html">Roman shades</a>.</li>
          <li>Want to flick between privacy and full view many times a day? <a href="day-and-night-zebra-blinds.html">Day &amp; night (zebra) blinds</a> do that with one pull.</li>
          <li>Need the cheapest clean option for a kitchen or utility room? A <a href="roller-blinds.html">roller blind</a> is hard to beat.</li>
        </ul>""",
 faq=[("Are honeycomb blinds worth it in Montreal?", "Yes. Of all blind types, cellular shades do the most to cut heat loss through glass in winter and heat gain in summer. With our long heating season the comfort difference is noticeable — especially on big or north-facing windows."),
      ("Single cell or double cell — which should I get?", "Single cell for most rooms. Double cell for the coldest windows (large, north-facing, older single-pane) or where you also want a bit more sound dampening."),
      ("Can they be fully blackout?", "Yes — blackout cellular fabric has an opaque inner lining. For <em>total</em> darkness (nurseries, shift workers, home cinema) pair it with side channels so light can’t leak around the edges."),
      ("Are they child-safe?", "Yes — we recommend cordless or motorized operation, which removes hanging cords entirely."),
      ("How do I clean them?", "A soft duster or vacuum brush attachment on low. For marks, a damp (not wet) cloth dabbed gently. Avoid soaking the fabric."),
      ("Do you install them?", "Yes — professional installation is free and included with every order across Montreal. We measure on site so the fit is exact.")],
 aside_h="See honeycomb samples at home", aside_p="Free in-home consultation. We bring fabrics, measure your windows and give you an honest recommendation.",
 cta_h="Ready to feel the <em>difference</em> this winter?", cta_p="Book a free consultation. We’ll measure, bring honeycomb samples in single and double cell, and quote on the spot — installation included.",
 related=[R["winter"], R["blackout"], R["zebra"]]),
# ---------------------------------------------------------------- ROLLER
dict(slug="roller-blinds.html", type="guide", crumb="Roller blinds", read=6, image=IMG["roller"],
 alt="Roller blinds in a bright, modern room",
 title="Roller Blinds: The Complete Guide (Fabrics, Pros & Cons, Best Rooms)",
 description="Everything about roller blinds: how they work, the fabric types (sheer, easy-clean, jacquard, blackout), honest pros and cons, and the rooms they suit best. Custom-made and installed free in Montreal.",
 og="Clean, minimal and endlessly versatile — the fabric options, and where roller blinds shine.",
 h1="Roller blinds: the clean, <em>do-anything</em> classic.",
 lede="A single sheet of fabric on a tube. That simplicity is exactly why roller blinds are the most popular window covering in the world — and why the fabric you choose matters more than anything else.",
 body="""
        <h2>What is a roller blind?</h2>
        <p>A roller blind is one flat piece of fabric wound around an aluminium tube at the top of the window. Pull it down for cover, roll it up and it all but disappears into a slim cassette. No slats, no folds, no fuss — the fabric itself does all the work of controlling light and privacy.</p>
        <p>Because the mechanism is so simple, roller blinds are among the most affordable custom blinds — and because the fabric is a flat, uninterrupted panel, they’re the best canvas for pattern, texture and colour.</p>

        <h2>How they work</h2>
        <p>The tube sits in brackets at the top of the frame. A <strong>chain</strong>, a <strong>spring</strong> (cordless) or a <strong>motor</strong> turns the tube to raise and lower the fabric. A weighted bottom bar keeps the fabric flat and straight. Add a <strong>cassette</strong> (a neat housing) at the top and the roll is hidden completely.</p>
        <p>The real decision is the fabric — that’s what determines what your blind does:</p>
        <ul>
          <li><strong>Sheer / voile</strong> — soft, glowing daylight and daytime privacy. Beautiful in living rooms.</li>
          <li><strong>Light-filtering / dim-out</strong> — the everyday choice: reduces glare, gives privacy, still lets light through.</li>
          <li><strong>Easy-clean / moisture-resistant</strong> — wipe-clean fabrics for kitchens and bathrooms.</li>
          <li><strong>Jacquard &amp; textured</strong> — woven patterns and linen looks for a more decorative feel.</li>
          <li><strong>Blackout</strong> — a coated, opaque fabric for bedrooms; pair with side channels for total dark (see our <a href="blackout-blinds.html">blackout guide</a>).</li>
        </ul>

        <h3>Chain, cordless or motorized?</h3>
        <p><strong>Chain</strong> is the classic and the most economical. <strong>Cordless spring</strong> gives a clean look and is the child-safe choice for nurseries. <strong>Motorized</strong> lets you set schedules and control by remote, app or voice — see <a href="motorized-blinds.html">are motorized blinds worth it?</a></p>

        <h2>Honest pros and cons</h2>""",
 pros=["<strong>Most affordable</strong> custom blind — great value per window.", "<strong>Cleanest, most minimal</strong> look; nearly vanishes when raised.", "<strong>Huge fabric range</strong> — sheer to blackout, plain to patterned.", "<strong>Easy to keep clean</strong> — a flat surface, and wipeable fabrics exist.", "<strong>Great for wide windows</strong> and sliding doors.", "<strong>Cordless and motorized</strong> options."],
 cons=["<strong>Least insulating</strong> of the blind types — for warmth, see <a href='honeycomb-blinds.html'>honeycomb</a>.", "<strong>All-or-nothing light</strong> — no tilt like a slat blind, no sheer/solid mix like <a href='day-and-night-zebra-blinds.html'>zebra</a>.", "<strong>Light gaps at the sides</strong> unless you add channels or an outside mount.", "<strong>Plain by design</strong> — if you want softness and drape, look at <a href='curtains-and-drapes.html'>curtains</a> or <a href='roman-shades.html'>Roman shades</a>."],
 glance=[("Insulation", (2, "Modest")), ("Light control", (4, "Sheer to blackout by fabric")), ("Privacy", (4, "Depends on fabric")), ("Style", (3, "Clean, versatile")), ("Maintenance", (5, "Very easy")), ("Value", (5, "Best per window")), ("Best rooms", "Kitchens, bathrooms, offices, living rooms, wide windows"), ("Options", "Chain · cordless · motorized · cassette · side channels · dual (zebra)")],
 body2="""
        <h2>Who they’re perfect for</h2>
        <p><strong>If you want a clean, modern look on a sensible budget, start here.</strong> Roller blinds are our recommendation for kitchens and bathrooms (easy-clean fabrics), home offices (glare control), and anywhere you want the window to feel uncluttered. They’re also the go-to for very wide windows and patio doors where other styles get heavy.</p>
        <div class="callout"><strong>Pro tip</strong><p>Choose the fabric for the <em>job</em>, not just the colour: dim-out for living areas, blackout for bedrooms, moisture-resistant near water. We bring the full swatch book to your consultation so you can see them against your wall in your light.</p></div>
        <h2>When to choose something else</h2>
        <ul>
          <li>Cold window? A <a href="honeycomb-blinds.html">honeycomb blind</a> insulates far better.</li>
          <li>Want to switch between view and privacy all day? <a href="day-and-night-zebra-blinds.html">Zebra blinds</a> do it in one pull.</li>
          <li>Want warmth and softness on the wall? <a href="curtains-and-drapes.html">Curtains</a> or <a href="roman-shades.html">Roman shades</a>.</li>
        </ul>""",
 faq=[("Are roller blinds good for bedrooms?", "Yes, with a blackout fabric — and add side channels if you need total darkness. For the very best sleep environment, a blackout honeycomb also adds insulation and quiet."),
      ("Can roller blinds be cleaned?", "Easily. Dust or vacuum on low; wipe easy-clean fabrics with a damp cloth. They’re the lowest-maintenance blind type."),
      ("Do roller blinds block heat?", "Reflective and blackout fabrics reduce summer heat gain noticeably. For winter insulation, honeycomb (cellular) blinds are the better choice."),
      ("Are roller blinds child-safe?", "Yes — choose cordless (spring) or motorized operation, which removes hanging chains."),
      ("Do you install them?", "Yes — installation is free and included with every order across Montreal. We measure on site so the fit is exact.")],
 aside_h="See roller fabrics at home", aside_p="Free in-home consultation. We bring the swatch book, measure your windows and recommend the right fabric for each room.",
 cta_h="Clean look, honest price — <em>installed free.</em>", cta_p="Book a free consultation. We measure, bring fabric samples and quote on the spot.",
 related=[R["zebra"], R["blackout"], R["honey"]]),

# ---------------------------------------------------------------- CURTAINS
dict(slug="curtains-and-drapes.html", type="guide", crumb="Curtains & drapes", read=7, image=IMG["curtains"],
 alt="Floor-length curtains framing a bright bedroom window",
 title="Curtains & Drapes: Fabrics, Fullness and Getting the Drop Right",
 description="A complete guide to custom curtains and drapes: sheer vs blackout, lining, fullness, pleat styles, tracks vs rods, and how to measure the drop. Made to measure and installed free in Montreal.",
 og="Why curtains still win on softness and drama — and the measuring details that make or break them.",
 h1="Curtains &amp; drapes: softness, drama, and <em>getting the drop right.</em>",
 lede="Nothing changes the feel of a room like fabric falling from ceiling to floor. Curtains add warmth, height and a finished look no hard blind can match — if they’re made and hung properly. Here’s what actually matters.",
 body="""
        <h2>Curtains vs drapes — is there a difference?</h2>
        <p>Loosely: <strong>curtains</strong> are lighter, often unlined; <strong>drapes</strong> are heavier, lined, more formal. In practice we make both to measure and the choice is really about <em>fabric weight, lining and function</em>. Many rooms use a sheer curtain for daytime with a lined drape over it for evenings — the layered look you see in well-designed homes.</p>

        <h2>The decisions that matter</h2>
        <h3>1. Fabric &amp; opacity</h3>
        <ul>
          <li><strong>Sheer / voile</strong> — soft light, daytime privacy, airy feel.</li>
          <li><strong>Linen &amp; linen-look</strong> — relaxed, textured, very current.</li>
          <li><strong>Velvet &amp; heavy weaves</strong> — luxury, warmth, sound absorption.</li>
          <li><strong>Blackout-lined</strong> — bedrooms and media rooms.</li>
        </ul>
        <h3>2. Lining</h3>
        <p>Lining is what separates a curtain that looks good from one that looks <em>expensive</em>. It adds body so the fabric hangs in clean folds, protects the face fabric from sun fade, and — with thermal or blackout lining — adds insulation and darkness.</p>
        <h3>3. Fullness</h3>
        <p>Fullness is how much fabric you use versus the width of the window. Skimpy curtains are the most common mistake. We use roughly <strong>2× to 2.5× the track width</strong> so the curtains look generous both open and closed.</p>
        <h3>4. Heading (pleat) style</h3>
        <p><strong>Wave / S-fold</strong> — soft, even ripples; the modern favourite on a track. <strong>Pinch pleat</strong> — tailored, classic. <strong>Eyelet / grommet</strong> — casual, on a rod. <strong>Pencil pleat</strong> — traditional and economical.</p>
        <h3>5. Track vs rod, and mounting height</h3>
        <p>A <strong>ceiling-mounted track</strong> gives the cleanest, tallest look and glides silently — our usual recommendation. Mount high and wide: hanging curtains just above the window frame and extending past its sides makes both the window and the room look bigger.</p>
        <h3>6. The drop (length)</h3>
        <p><strong>Kiss the floor</strong> (about 1 cm above) for a crisp, tailored finish. <strong>Break</strong> (2–3 cm on the floor) for a relaxed, luxurious look. <strong>Puddle</strong> for full drama. Never halfway up the wall. Getting this exact is why we measure every window ourselves.</p>

        <h2>Honest pros and cons</h2>""",
 pros=["<strong>Unmatched softness, warmth and drama</strong> — transforms the feel of a room.", "<strong>Makes ceilings look taller</strong> and windows bigger when hung high and wide.", "<strong>Excellent insulation and sound absorption</strong> when lined.", "<strong>Endless fabric, colour and pattern</strong> choices.", "<strong>Layers beautifully</strong> with sheers or blinds.", "<strong>Motorized tracks</strong> available."],
 cons=["<strong>Take up wall space</strong> when open (the stack) — allow for it.", "<strong>Not ideal near water or cooking</strong> — kitchens and bathrooms suit blinds better.", "<strong>Dust and need periodic cleaning</strong>; check the fabric’s care.", "<strong>Cost more than a basic roller blind</strong> because of the fabric quantity and lining.", "<strong>Details are unforgiving</strong> — bad measurements show. (We measure for you.)"],
 glance=[("Insulation", (4, "Very good when lined")), ("Light control", (4, "Sheer to full blackout")), ("Privacy", (4, "Excellent when closed")), ("Style", (5, "The statement option")), ("Maintenance", (3, "Periodic cleaning")), ("Best rooms", "Living rooms, bedrooms, dining rooms, tall windows"), ("Options", "Sheer / linen / velvet / blackout · lined · wave / pinch / eyelet · track or rod · motorized")],
 body2="""
        <h2>Who they’re perfect for</h2>
        <p><strong>If you want the room to feel warm, finished and a little luxurious, curtains are the answer.</strong> They’re our first recommendation for living rooms and bedrooms, for tall or feature windows, and for anyone who finds hard blinds a bit clinical. Layer a sheer under a lined drape and you get soft daylight by day and cosy privacy by night.</p>
        <div class="callout"><strong>The layered look</strong><p>Our most-requested combination: a <em>sheer wave curtain</em> on a ceiling track for the daytime glow, with a <em>lined drape</em> in front for evenings — or a <a href="honeycomb-blinds.html">honeycomb blind</a> behind for insulation. Best of both, and it photographs beautifully.</p></div>
        <h2>When to choose something else</h2>
        <ul>
          <li>Kitchen, bathroom or a window right by the sink? A wipe-clean <a href="roller-blinds.html">roller blind</a>.</li>
          <li>Tight on wall space, or want a tailored fold instead of a drape? <a href="roman-shades.html">Roman shades</a>.</li>
          <li>Need insulation without the fabric volume? <a href="honeycomb-blinds.html">Honeycomb blinds</a>.</li>
        </ul>""",
 faq=[("How high should curtains be hung?", "As high as you can — ideally from the ceiling or just below it, and extending 15–25 cm past each side of the window. It makes the window and room look bigger."),
      ("Should curtains touch the floor?", "Yes, or nearly. ‘Kiss’ the floor (about 1 cm above) for tailored, or ‘break’ 2–3 cm onto it for a relaxed, luxe look. Curtains ending mid-wall look unfinished."),
      ("What is fullness?", "The ratio of fabric width to track width. We use around 2× to 2.5× so curtains look generous. Skimpy curtains are the number-one mistake."),
      ("Are curtains good for insulation?", "Lined curtains — especially thermal or blackout-lined — insulate very well and also absorb sound. For the best insulation of all, combine with a honeycomb blind."),
      ("Do you make and install them?", "Yes — every curtain is made to measure for your window and installed free across Montreal, tracks and all.")],
 aside_h="See fabrics in your light", aside_p="Free in-home consultation. We bring fabric samples and measure so the drop and fullness are exactly right.",
 cta_h="Fabric that falls <em>exactly</em> right.", cta_p="Book a free consultation. We measure every window, bring fabrics and lining samples, and install for free.",
 related=[R["roman"], R["vs"], R["honey"]]),

# ---------------------------------------------------------------- ROMAN
dict(slug="roman-shades.html", type="guide", crumb="Roman shades", read=6, image=IMG["roman"],
 alt="Elegant Roman shades framing a window",
 title="Roman Shades: Tailored Folds, Quiet Luxury (How They Work, Pros & Cons)",
 description="Roman shades explained: how they fold and stack, flat vs hobbled styles, lining and blackout options, honest pros and cons, and the rooms they suit. Made to measure and installed free in Montreal.",
 og="The soft, structured look — how they stack, which fabrics work, and the rooms they’re made for.",
 h1="Roman shades: the tailored fold that reads as <em>quiet luxury.</em>",
 lede="A Roman shade is fabric that folds up in neat horizontal pleats instead of rolling. You get the softness of a curtain with the tidy footprint of a blind — which is why designers reach for them again and again.",
 body="""
        <h2>What is a Roman shade?</h2>
        <p>A Roman shade is a flat panel of fabric with horizontal rods or seams stitched across the back. As you raise it, the fabric gathers into a stack of even folds at the top of the window; lower it and it hangs flat and smooth. It’s a blind made of curtain fabric — structured but soft.</p>

        <h2>How they work</h2>
        <p>Cords (or a motor) run up the back of the shade through rings on each fold rod. Pull, and the bottom rises fold by fold. Because it’s made from real drapery fabric, a Roman shade can be <strong>lined</strong> for body, <strong>thermally lined</strong> for insulation, or <strong>blackout-lined</strong> for bedrooms.</p>
        <h3>Styles</h3>
        <ul>
          <li><strong>Flat Roman</strong> — smooth, clean face when down; crisp folds when raised. The modern favourite; great for patterns.</li>
          <li><strong>Hobbled (looped / teardrop)</strong> — soft permanent folds even when fully lowered. Warmer, more traditional.</li>
          <li><strong>Relaxed</strong> — a gentle curve at the bottom hem for a casual, softer look (best on windows you rarely raise).</li>
        </ul>
        <h3>Fabric</h3>
        <p>Linen and linen-look weaves are the classic choice — texture without heaviness. Cotton and cotton blends take pattern well. Heavier weaves feel richer. Almost any drapery fabric works, which is where Roman shades beat every other blind for choice.</p>

        <h2>Honest pros and cons</h2>""",
 pros=["<strong>Softness and elegance</strong> of fabric, in a blind’s footprint.", "<strong>Huge fabric range</strong> — texture, colour, pattern.", "<strong>Can be lined</strong> — thermal or blackout — for insulation and darkness.", "<strong>Great in kitchens and small windows</strong> where curtains would be too much.", "<strong>Layers beautifully</strong> with sheers or curtains.", "<strong>Cordless and motorized</strong> options."],
 cons=["<strong>Folds stack at the top</strong> and cover part of the window when raised (unless mounted above the frame).", "<strong>Cost more than roller blinds</strong> — real fabric plus lining and construction.", "<strong>Not for very wide spans</strong> — over ~2 m they get heavy; consider two shades or curtains.", "<strong>Not ideal in steamy bathrooms</strong> unless the fabric is chosen carefully.", "<strong>Cleaning is dust/vacuum</strong> — not a wipe-down."],
 glance=[("Insulation", (4, "Very good when lined")), ("Light control", (4, "Filtering to blackout by lining")), ("Privacy", (4, "Excellent when down")), ("Style", (5, "Designer favourite")), ("Maintenance", (3, "Dust / vacuum")), ("Best rooms", "Living rooms, dining rooms, bedrooms, kitchens (with care), small &amp; feature windows"), ("Options", "Flat / hobbled / relaxed · lined / thermal / blackout · cordless · motorized")],
 body2="""
        <h2>Who they’re perfect for</h2>
        <p><strong>If you love the softness of fabric but want it neat, this is your blind.</strong> Roman shades are our pick for dining rooms, living rooms and bedrooms where curtains would be too much fabric, for kitchens (a washable-fabric flat Roman over the sink is a classic), and for anyone whose taste runs to “quietly expensive.”</p>
        <div class="callout"><strong>Mounting tip</strong><p>Mount the shade <em>above</em> the window frame (outside mount) so the raised stack sits over the wall, not over the glass. You keep the whole view and the window looks taller. We’ll advise on site.</p></div>
        <h2>When to choose something else</h2>
        <ul>
          <li>Very wide window or patio door? <a href="curtains-and-drapes.html">Curtains</a> or a <a href="roller-blinds.html">roller blind</a>.</li>
          <li>Top priority is insulation? A <a href="honeycomb-blinds.html">honeycomb blind</a>.</li>
          <li>Want to flick between view and privacy constantly? <a href="day-and-night-zebra-blinds.html">Zebra blinds</a>.</li>
        </ul>""",
 faq=[("Are Roman shades good for bedrooms?", "Yes — with a blackout lining they’re excellent, and they look softer than a hard blind. Add side channels or an outside mount to reduce light at the edges."),
      ("Flat or hobbled Roman shade?", "Flat for a clean, modern look (and for patterned fabric). Hobbled for a softer, more traditional feel with permanent folds."),
      ("Can Roman shades be motorized?", "Yes. Motorized Roman shades are quiet and very convenient on hard-to-reach or multiple windows."),
      ("Are they hard to clean?", "Dust or vacuum on low. Some fabrics can be spot-cleaned. They’re not a wipe-clean surface like a roller blind, so we steer kitchens toward washable fabrics."),
      ("Do you install them?", "Yes — made to measure and installed free across Montreal.")],
 aside_h="Feel the fabrics at home", aside_p="Free in-home consultation. We bring linen and cotton samples and measure so the folds sit exactly right.",
 cta_h="Tailored folds, <em>made to measure.</em>", cta_p="Book a free consultation. We measure, bring fabric samples and install for free.",
 related=[R["curtains"], R["honey"], R["blackout"]]),

# ---------------------------------------------------------------- ZEBRA
dict(slug="day-and-night-zebra-blinds.html", type="guide", crumb="Day & night (zebra)", read=6, image=IMG["zebra"],
 alt="Day and night zebra blinds with alternating sheer and solid bands",
 title="Day & Night (Zebra) Blinds Explained: How They Work, Pros & Cons",
 description="Zebra (day and night) blinds explained: how the alternating sheer and solid bands work, blackout versions, honest pros and cons, and which rooms they suit. Custom-made and installed free in Montreal.",
 og="Sheer and solid bands that glide past each other — privacy and daylight from one blind.",
 h1="Day &amp; night blinds: privacy and daylight from <em>one</em> blind.",
 lede="Also called zebra or dual blinds. Two layers of fabric striped with alternating sheer and solid bands slide past each other — line the sheers up for a soft view, line the solids up for privacy, and everything in between. It’s the blind that changes its mind with you.",
 body="""
        <h2>What is a day &amp; night blind?</h2>
        <p>Picture a roller blind whose fabric is a continuous loop, striped with alternating <strong>sheer</strong> and <strong>opaque</strong> bands. The loop runs down the front and back up behind, so the two layers overlap. Move the blind slightly and the bands shift against each other:</p>
        <ul>
          <li><strong>Sheer over sheer</strong> — an open, filtered view; daylight floods in.</li>
          <li><strong>Solid over sheer</strong> — full privacy, gentle light through the sheer layer.</li>
          <li><strong>Anywhere between</strong> — dial in exactly the light you want.</li>
        </ul>
        <p>You still roll it fully up like a normal roller blind when you want the window clear.</p>

        <h2>How they work</h2>
        <p>A chain, spring or motor moves the fabric loop around a tube. Because the mechanism is a roller, day &amp; night blinds have the same slim cassette, the same clean look and similar pricing to a good roller blind — with far more control. They come in <strong>light-filtering</strong> and <strong>blackout-band</strong> versions (the solid stripes are opaque, so with the bands aligned you get a very dark room — not quite total blackout, because the sheer stripes remain).</p>

        <h2>Honest pros and cons</h2>""",
 pros=["<strong>Privacy and view from one blind</strong> — no need for a sheer plus a blind.", "<strong>Infinitely adjustable</strong> light with a small movement.", "<strong>Modern, striped look</strong> that suits contemporary rooms.", "<strong>Roller-blind simplicity</strong> and slim cassette.", "<strong>Great value</strong> for the flexibility you get.", "<strong>Cordless and motorized</strong> options."],
 cons=["<strong>Not true blackout</strong> — the sheer bands always let a little light through. For total dark see the <a href='blackout-blinds.html'>Blockout Blind</a>.", "<strong>Modest insulation</strong> — like a roller blind. Cold window? <a href='honeycomb-blinds.html'>Honeycomb</a>.", "<strong>The stripes are a look</strong> — you either love it or you don’t.", "<strong>Two layers of fabric</strong> means a slightly bigger roll on very tall windows."],
 glance=[("Insulation", (2, "Modest")), ("Light control", (5, "Infinitely adjustable")), ("Privacy", (4, "Excellent (bands aligned)")), ("Style", (4, "Modern, striped")), ("Maintenance", (4, "Easy")), ("Value", (5, "Excellent")), ("Best rooms", "Living rooms, home offices, kitchens, street-facing rooms"), ("Options", "Light-filtering or blackout bands · chain / cordless / motorized · cassette")],
 body2="""
        <h2>Who they’re perfect for</h2>
        <p><strong>If your window faces the street or a neighbour and you keep wishing you could have the view <em>and</em> privacy, this is the blind.</strong> Day &amp; night blinds are our top recommendation for living rooms and home offices, and for anyone who fiddles with their blinds ten times a day and wants it to be effortless.</p>
        <div class="callout"><strong>Montreal favourite</strong><p>Zebra blinds are one of our most-installed products in city condos and duplexes — big windows, close neighbours, and a lot of light to manage. They solve all three.</p></div>
        <h2>When to choose something else</h2>
        <ul>
          <li>Need total darkness (bedroom, nursery)? A <a href="blackout-blinds.html">Blockout Blind</a> solution.</li>
          <li>Cold or north-facing window? <a href="honeycomb-blinds.html">Honeycomb blinds</a>.</li>
          <li>Prefer a plain, unstriped face? A <a href="roller-blinds.html">roller blind</a> with a sheer curtain.</li>
        </ul>""",
 faq=[("Are zebra blinds blackout?", "Blackout-band versions get a room very dark, but the sheer stripes always pass a little light — so not 100%. For nurseries and shift workers, choose the Blockout Blind — a framed shade that seals every edge."),
      ("Can you see through zebra blinds at night?", "With the solid bands aligned, no — the opaque stripes overlap and block the view in. With sheers aligned, some silhouette is visible when the room is lit, as with any sheer."),
      ("Are they good for big windows?", "Yes — they’re a roller mechanism, so they handle wide windows and patio doors well."),
      ("Chain or motorized?", "Both work well. Motorized is lovely here because you’ll adjust them often; a remote or schedule makes it effortless."),
      ("Do you install them?", "Yes — custom-made and installed free across Montreal.")],
 aside_h="Try the bands at home", aside_p="Free in-home consultation. We bring samples so you can see the sheer and blackout bands against your window.",
 cta_h="View by day, privacy by night — <em>one blind.</em>", cta_p="Book a free consultation. We measure, bring samples and install for free.",
 related=[R["roller"], R["condo"], R["blackout"]]),

# ---------------------------------------------------------------- MOTORIZED
dict(slug="motorized-blinds.html", type="guide", crumb="Motorized blinds", read=7, image=IMG["motor"],
 alt="Motorized blackout blinds in a serene bedroom",
 title="Motorized Blinds: Are They Worth It? (Costs, Options, Pros & Cons)",
 description="Motorized blinds explained: how they work, remote / app / voice control, schedules, battery vs hardwired, which blinds can be motorized, honest pros and cons and whether they're worth it. Installed free in Montreal.",
 og="Remotes, schedules, voice control — what motorization really adds, and what it costs.",
 h1="Motorized blinds: are they <em>actually</em> worth it?",
 lede="Press a button — or say a word — and every blind in the room glides into place. Motorization used to be a luxury add-on. Now it’s affordable, quiet and genuinely useful. Here’s what it adds, what it costs, and when it’s worth it.",
 body="""
        <h2>What are motorized blinds?</h2>
        <p>Any blind or curtain fitted with a small, quiet motor instead of a chain or cord. You control it with a <strong>remote</strong>, a <strong>wall switch</strong>, a <strong>phone app</strong>, or <strong>voice</strong> (Google, Alexa, Apple Home), and you can set <strong>schedules</strong> — open at sunrise, close at dusk, all automatically.</p>
        <p>We motorize <a href="roller-blinds.html">roller blinds</a>, <a href="day-and-night-zebra-blinds.html">zebra blinds</a>, <a href="honeycomb-blinds.html">honeycomb blinds</a>, <a href="roman-shades.html">Roman shades</a> and <a href="curtains-and-drapes.html">curtain tracks</a>.</p>

        <h2>How they work</h2>
        <h3>Power</h3>
        <ul>
          <li><strong>Rechargeable battery</strong> — the motor lives inside the tube; charge it a couple of times a year with a USB cable. No wiring, no electrician. Our most common choice.</li>
          <li><strong>Hardwired</strong> — powered from the mains; ideal for new builds or renovations where wiring is easy. Never needs charging.</li>
          <li><strong>Solar strip</strong> — a slim panel on the window keeps batteries topped up.</li>
        </ul>
        <h3>Control</h3>
        <p>A remote (single or multi-channel) is the simplest. Add a <strong>hub</strong> and you get app control, schedules and voice. Group blinds by room, set “Good morning” and “Movie” scenes, and control the whole home from your phone — even away.</p>

        <h2>What motorization is genuinely great for</h2>
        <ul>
          <li><strong>Hard-to-reach windows</strong> — high, behind furniture, over a sink or bath.</li>
          <li><strong>Many windows at once</strong> — one button, the whole living room.</li>
          <li><strong>Sleep &amp; routine</strong> — bedroom blackout opens gently at your wake time.</li>
          <li><strong>Energy &amp; sun</strong> — schedule shades to block afternoon sun in summer and let winter light in.</li>
          <li><strong>Security</strong> — blinds moving on schedule while you’re away makes the home look lived-in.</li>
          <li><strong>Child &amp; pet safety</strong> — no cords at all.</li>
        </ul>

        <h2>Honest pros and cons</h2>""",
 pros=["<strong>Effortless</strong> — especially with many, tall or awkward windows.", "<strong>Schedules and scenes</strong> that just happen.", "<strong>Cordless = safest</strong> for kids and pets, and the cleanest look.", "<strong>Works with smart homes</strong> — Google, Alexa, Apple.", "<strong>Adds real value</strong> to a home.", "<strong>Battery versions need no wiring.</strong>"],
 cons=["<strong>Costs more per blind</strong> than manual — the motor and control add to the price.", "<strong>Batteries need charging</strong> a few times a year (or go hardwired / solar).", "<strong>Another device</strong> — a hub for app/voice, remotes to keep track of.", "<strong>Motors can eventually need replacing</strong> (they last years, and are replaceable).", "<strong>Overkill for one small, easy window</strong> you rarely touch."],
 glance=[("Convenience", (5, "The whole point")), ("Safety", (5, "No cords")), ("Smart-home", (5, "App, voice, schedules")), ("Cost", (2, "Higher than manual")), ("Maintenance", (4, "Occasional charging")), ("Best for", "Multiple / tall / hard-to-reach windows, bedrooms, living rooms, home offices"), ("Options", "Battery · hardwired · solar · remote · wall switch · app · voice · schedules")],
 body2="""
        <h2>So — is it worth it?</h2>
        <p><strong>Yes, when you have more than a couple of windows in a room, any hard-to-reach window, or a bedroom you’d love to wake up to daylight in.</strong> That’s most Montreal living rooms and bedrooms. Where it’s <em>not</em> worth it: a single small window you rarely touch. Our honest advice is usually to motorize the rooms you live in most and keep manual blinds elsewhere — you get the convenience where it counts and keep the budget sensible.</p>
        <div class="callout"><strong>Good to know</strong><p>Motorization is decided per blind, and you can mix — motorized in the living room and bedroom, manual in the laundry. We’ll walk through it room by room at your consultation.</p></div>""",
 faq=[("How much do motorized blinds cost?", "The motor and controls add to the price of the blind — the amount depends on the blind type, size and whether you want a remote only or full app/voice control. We quote per window at your free consultation, with no obligation."),
      ("Do motorized blinds need an electrician?", "Not for battery-powered blinds — the most common choice — which we install like any blind and you charge via USB a few times a year. Hardwired options need mains power and suit renovations and new builds."),
      ("How long do the batteries last?", "Typically several months between charges with normal daily use. Solar strips can keep them topped up indefinitely."),
      ("Do they work with Google Home / Alexa / Apple Home?", "Yes, with a hub. You can then use voice, the app, schedules and scenes."),
      ("Which blinds can be motorized?", "Roller, zebra, honeycomb, Roman shades and curtain tracks — nearly everything we make."),
      ("Do you install them?", "Yes — installation and setup are free and included across Montreal.")],
 aside_h="See a motor in action", aside_p="Free in-home consultation. We’ll demo the remote and app, and advise which rooms are worth motorizing.",
 cta_h="Every blind, <em>one button.</em>", cta_p="Book a free consultation. We measure, demo the controls and install for free — no electrician needed for battery models.",
 related=[R["blackout"], R["honey"], R["zebra"]]),

# ---------------------------------------------------------------- BLOCKOUT
dict(slug="blackout-blinds.html", type="guide", crumb="Blockout Blind", read=6, image=IMG["blackout"],
 alt="A black framed Blockout Blind sealed into a bedroom window, blocking all light",
 title="Blockout Blind: The Framed Shade That Blocks 100% of Light",
 description="The Blockout Blind is a framed, edge-sealed shade that gives true 100% darkness — no light halo, no side leaks. How the frame works, who it's for, cordless and motorized options, honest pros and cons. Installed free in Montreal.",
 og="A framed, edge-sealed shade that blocks 100% of light — no halo, no leaks. Real darkness for real sleep.",
 h1="Blockout Blind: the shade that finally makes a room <em>completely</em> dark.",
 lede="Every “blackout” blind you’ve ever owned leaked light around the edges. The Blockout Blind doesn’t, and the reason is simple: it isn’t just a fabric — it’s a fabric inside a frame that seals every edge of the window. Here’s how it works and who it’s for.",
 body="""
        <h2>The problem with ordinary blackout blinds</h2>
        <p>Blackout fabric is fully opaque, but an ordinary blind hangs a few millimetres inside the frame. Light pours around those edges as bright bars — and on a summer morning in Montreal that halo arrives before 5 a.m. You can add channels, curtains and overlap to fight it, but you’re patching gaps that the blind itself creates.</p>
        <figure>
          <img src="../assets/roller-blackout.jpg" alt="A regular blackout roller blind with visible light gaps down both sides" />
          <figcaption>A standard blackout roller. Good fabric — but look at the light down both sides.</figcaption>
        </figure>

        <h2>What makes a Blockout Blind different</h2>
        <p>The Blockout Blind mounts a slim aluminium <strong>frame</strong> around the entire window opening. The blackout fabric runs <em>inside</em> that frame in tensioned side tracks, and the top and bottom seal against it. Every edge is closed — top, both sides and bottom — so there is simply nowhere for light to get in.</p>
        <ul>
          <li><strong>Sealed frame</strong> — the fabric edges live inside the tracks; no side gap, no bottom gap.</li>
          <li><strong>Tensioned, cordless</strong> — pull the bottom bar and it stays exactly where you leave it. No cords, no chains — child-safe by design.</li>
          <li><strong>Top-down or bottom-up</strong> — lower it from the top to let a little light in, or close it fully.</li>
          <li><strong>Inside or outside mount</strong> — inside needs about 2.5 cm (1&quot;) of recess depth; outside needs about 7.5 cm (3&quot;) of flat surface.</li>
          <li><strong>Motorized &amp; smart</strong> options — schedule it, control by app or voice.</li>
          <li><strong>Quieter and cooler</strong> — the sealed fabric also dampens outside noise and cuts summer heat gain.</li>
        </ul>
        <figure>
          <img src="../assets/blockout-sleep.jpg" alt="Someone sleeping soundly in a dark bedroom with a Blockout Blind on the window" />
          <figcaption>The result: a bedroom that is dark at 6 a.m. in June.</figcaption>
        </figure>

        <h2>Who it’s for</h2>
        <ul>
          <li><strong>Babies and toddlers</strong> — naps and early bedtimes in a bright season. See our <a href="blackout-blinds-for-nursery.html">nursery guide</a>.</li>
          <li><strong>Shift workers and night owls</strong> — real sleep at 10 a.m.</li>
          <li><strong>Light sleepers and migraine sufferers</strong>.</li>
          <li><strong>Home cinemas and gaming rooms</strong>.</li>
          <li><strong>Anyone in a bright condo</strong> with streetlights and neighbours’ windows.</li>
        </ul>

        <h2>Honest pros and cons</h2>""",
 pros=["<strong>Truly 100% dark</strong> — the frame seals every edge; no halo, no bars of light.", "<strong>Cordless and child-safe</strong> — a tensioned bar, nothing hanging.", "<strong>Top-down / bottom-up</strong> flexibility.", "<strong>Quieter, cooler room</strong> as a side effect of the seal.", "<strong>Motorized and smart-home ready.</strong>", "<strong>Made to measure</strong> for each window."],
 cons=["<strong>The frame is visible</strong> — slim and neat, but you see it around the window. Choose the finish to match your trim.", "<strong>Costs more than a plain blackout roller</strong> — you’re paying for the frame and the seal, which is exactly what delivers the darkness.", "<strong>Needs some depth or flat surface</strong> to mount the frame — we check at the consultation.", "<strong>Total darkness isn’t for living rooms</strong> — there, use a dim-out <a href='roller-blinds.html'>roller</a> or <a href='day-and-night-zebra-blinds.html'>zebra blind</a>."],
 glance=[("Darkness", (5, "100% — sealed frame")), ("Privacy", (5, "Absolute")), ("Insulation", (4, "Good; sealed edges help")), ("Noise", (4, "Noticeably quieter")), ("Style", (3, "Clean; frame visible")), ("Best rooms", "Bedrooms, nurseries, home cinemas, shift-worker rooms, bright condos"), ("Options", "Inside / outside mount · top-down/bottom-up · cordless · motorized · frame finishes")],
 body2="""
        <div class="callout"><strong>Blockout Blind vs. blackout roller + side channels</strong><p>You can get close to full darkness by adding side channels to a blackout roller — we do it often. The Blockout Blind is the purpose-built version: the frame <em>is</em> the channel system, top and bottom included, in one clean unit. If darkness is the whole point of the room, this is the one.</p></div>
        <h2>When to choose something else</h2>
        <ul>
          <li>Want darkness <em>and</em> maximum insulation on a cold window? A blackout <a href="honeycomb-blinds.html">honeycomb</a> with channels.</li>
          <li>Prefer a soft, decorative look? Blackout-lined <a href="curtains-and-drapes.html">curtains</a> or a <a href="roman-shades.html">Roman shade</a> (expect a little edge light).</li>
        </ul>""",
 faq=[("Is the Blockout Blind really 100% blackout?", "Yes. Unlike an ordinary blackout blind, the fabric runs inside a frame that seals the top, both sides and the bottom of the window, so there are no edges for light to leak around."),
      ("What is the difference between a Blockout Blind and a blackout roller?", "A blackout roller uses opaque fabric but hangs with small gaps at the sides where light gets in. A Blockout Blind puts the fabric inside a sealed frame with tensioned side tracks — no gaps."),
      ("Is it child-safe?", "Yes — it’s cordless. You move a tensioned bottom bar; there are no cords or chains."),
      ("Can it be motorized?", "Yes, with app, voice and schedule control — a lovely combination for a bedroom that opens gently at your wake time."),
      ("Does it fit my window?", "Inside mount needs about 2.5 cm of recess depth; outside mount needs about 7.5 cm of flat surface around the window. We confirm at your free consultation."),
      ("Do you install it?", "Yes — measured, made to size and installed free across Montreal.")],
 aside_h="See a Blockout Blind in person", aside_p="Free in-home consultation. We bring a sample so you can see the frame and the seal, and check your window depth.",
 cta_h="Sleep like it’s <em>midnight</em> at noon.", cta_p="Book a free consultation. We measure, confirm the mount and install for free.",
 related=[R["nursery"], R["honey"], R["motor"]]),

# ---------------------------------------------------------------- OUTDOOR
dict(slug="outdoor-blinds.html", type="guide", crumb="Outdoor blinds", read=5, image=IMG["outdoor"],
 alt="A covered outdoor patio with weatherproof blinds",
 title="Outdoor Blinds for Patios & Balconies: How They Work, Pros & Cons",
 description="Outdoor blinds and exterior shades explained: weatherproof fabrics, zip-track and cable systems, wind and sun ratings, honest pros and cons, and how they handle Montreal seasons. Installed free.",
 og="Extend your living space outside — weatherproof shade that handles Montreal seasons.",
 h1="Outdoor blinds: turn your patio into another <em>room.</em>",
 lede="Shade from the afternoon sun, shelter from a breeze, privacy from the neighbours — outdoor blinds make a balcony, terrace or patio usable for far more of the year. Here’s how the systems differ and what holds up in our climate.",
 body="""
        <h2>What are outdoor blinds?</h2>
        <p>Exterior roller shades made from <strong>weatherproof mesh or PVC fabrics</strong>, fitted to a pergola, balcony opening, patio cover or the outside of a window. Lower them to cut sun and glare, block wind and add privacy; raise them to open the space right up.</p>

        <h2>How they work</h2>
        <h3>The systems</h3>
        <ul>
          <li><strong>Zip-track (channel) blinds</strong> — the fabric edges run in side channels, so the shade sits taut, sealed and stable even in wind. The premium, most weatherproof option and the one we recommend for open balconies and pergolas.</li>
          <li><strong>Cable / wire-guided</strong> — the shade runs on tensioned cables; lighter and more economical, best for sheltered spots.</li>
          <li><strong>Exterior window shades</strong> — an outdoor roller fitted over the outside of a window to stop heat before it reaches the glass — the most effective way to keep a sun-facing room cool.</li>
        </ul>
        <h3>The fabrics</h3>
        <ul>
          <li><strong>Sunscreen mesh</strong> — blocks most UV and glare while keeping the view and airflow. The everyday choice.</li>
          <li><strong>Clear / tinted PVC</strong> — a wind and rain barrier that keeps the view; the “glass wall” look.</li>
          <li><strong>Blockout</strong> — full privacy and shade.</li>
        </ul>
        <p>Operate by crank, spring, or — very popular outdoors — <strong>motor</strong> with a wind sensor that raises the shade automatically in a gale.</p>

        <h2>Honest pros and cons</h2>""",
 pros=["<strong>Makes outdoor space usable</strong> in far more weather.", "<strong>Cuts heat and glare</strong> before it reaches your windows and furniture.", "<strong>Privacy</strong> from neighbours and the street.", "<strong>Wind and light-rain shelter</strong> with zip-track and PVC.", "<strong>Motorized with wind sensors</strong> for hands-off protection.", "<strong>Protects outdoor furniture</strong> from UV."],
 cons=["<strong>Montreal winters</strong> — most exterior fabrics should be raised in heavy snow and ice; we advise on seasonal use.", "<strong>Needs solid fixing points</strong> — a pergola, posts or a beam; not every balcony has them.", "<strong>Condo / strata rules</strong> may restrict exterior fittings — check first (we can help).", "<strong>Costs more than an interior blind</strong> — outdoor hardware is heavier-duty.", "<strong>Cleaning</strong> — hose down periodically."],
 glance=[("Sun &amp; glare", (5, "Excellent")), ("Wind shelter", (4, "Zip-track / PVC")), ("Privacy", (4, "Mesh to blockout")), ("Winter use", (2, "Raise in snow / ice")), ("Maintenance", (3, "Hose down")), ("Best for", "Patios, pergolas, balconies, terraces, sun-facing windows"), ("Options", "Zip-track · cable-guided · exterior window shade · mesh / PVC / blockout · crank / motor / wind sensor")],
 body2="""
        <h2>Who they’re perfect for</h2>
        <p><strong>If you have a patio, terrace or balcony you don’t use as much as you’d like because of sun, wind or the neighbours — this fixes it.</strong> Outdoor blinds are also the smartest answer for a room that overheats in summer: shading the glass from <em>outside</em> is far more effective than any interior blind.</p>
        <div class="callout"><strong>Montreal reality check</strong><p>Outdoor blinds are a three-season upgrade here. We spec fabrics and mounts for our freeze-thaw and advise on when to raise them for winter — most clients get May to October of extra living space, which is exactly when you want it.</p></div>""",
 faq=[("Do outdoor blinds survive Montreal winters?", "The hardware does; the fabric should generally be raised during heavy snow and ice. We spec systems for our climate and advise on seasonal use — think of them as a three-season upgrade."),
      ("Can I have outdoor blinds on a condo balcony?", "Often yes, but many buildings restrict exterior fittings. Check your bylaws first — we’re happy to help you present the request."),
      ("Which is better, zip-track or cable-guided?", "Zip-track for open, windy or exposed spaces — it seals the edges and stays taut. Cable-guided for sheltered spots and tighter budgets."),
      ("Can outdoor blinds be motorized?", "Yes, and it’s our usual recommendation outdoors — pair with a wind sensor so they retract automatically in strong gusts."),
      ("Do you install them?", "Yes — we survey your fixing points, spec the right system and install free across Montreal.")],
 aside_h="Get a site check", aside_p="Free consultation. We look at your patio or balcony, check fixing points and bylaws, and recommend the right system.",
 cta_h="Your patio, <em>three seasons</em> a year.", cta_p="Book a free consultation. We survey the space, spec the system and install for free.",
 related=[R["roller"], R["motor"], R["condo"]]),

# ---------------------------------------------------------------- SMART FILM
dict(slug="smart-film.html", type="guide", crumb="Smart film", read=5, image=IMG["film"],
 alt="A glass partition wall — the kind of surface switchable smart film is applied to",
 title="Smart Film: Privacy Glass at the Touch of a Button (How It Works, Pros & Cons)",
 description="Switchable smart film explained: how PDLC film turns clear glass frosted instantly, where it's used (bathrooms, offices, partitions, storefronts), pros and cons, and installation in Montreal.",
 og="Switchable film that turns clear glass frosted — how it works and where it’s brilliant.",
 h1="Smart film: privacy glass at the touch of a <em>button.</em>",
 lede="Clear one moment, frosted the next. Smart film turns any existing glass into switchable privacy glass — no blinds, no curtains, nothing to clean. It’s the most futuristic thing we install, and it’s surprisingly practical.",
 body="""
        <h2>What is smart film?</h2>
        <p>A thin, self-adhesive film applied to glass. Inside it is a layer of <strong>PDLC</strong> (polymer-dispersed liquid crystal). With power off, the crystals scatter light and the glass looks <strong>frosted</strong> — fully private. Apply a small current and the crystals align: the glass turns <strong>clear</strong> instantly. Flick a switch, use a remote, an app or a voice command.</p>

        <h2>How it works</h2>
        <p>We apply the film to your existing glass (windows, doors, partitions, shower screens, storefronts) and connect it to a small transformer. Control by:</p>
        <ul>
          <li><strong>Wall switch</strong> — simplest.</li>
          <li><strong>Remote or app</strong> — including scheduling.</li>
          <li><strong>Voice / smart home</strong> — “make the office private.”</li>
        </ul>
        <p>Frosted is the <em>default</em> (power off), so privacy is guaranteed even in a power cut. In clear mode the film is highly transparent with a slight haze — like very good glass. It also blocks most UV.</p>

        <h2>Where it’s brilliant</h2>
        <ul>
          <li><strong>Bathrooms &amp; ensuites</strong> — glass shower screens and windows that go private on demand.</li>
          <li><strong>Home offices &amp; meeting rooms</strong> — open when you want connection, private for a call.</li>
          <li><strong>Glass partitions</strong> — keep the light, control the view.</li>
          <li><strong>Storefronts &amp; clinics</strong> — privacy after hours or between clients.</li>
          <li><strong>Projection</strong> — in frosted mode the film doubles as a rear-projection screen.</li>
        </ul>

        <h2>Honest pros and cons</h2>""",
 pros=["<strong>Instant privacy</strong> — no blinds, no curtains, nothing in the way.", "<strong>Keeps the light</strong> even when private (frosted still glows).", "<strong>Zero cleaning</strong> — it’s just glass.", "<strong>Works on existing glass</strong> — no need to replace windows.", "<strong>Private by default</strong> — safe in a power cut.", "<strong>Blocks UV</strong>; can double as a projection screen.", "<strong>Smart-home ready.</strong>"],
 cons=["<strong>Not a blackout</strong> — frosted diffuses light, it doesn’t block it. For darkness see the <a href='blackout-blinds.html'>Blockout Blind</a>.", "<strong>Needs power</strong> — a low-voltage transformer and a discreet wire to the glass.", "<strong>Costs more per square metre</strong> than a blind.", "<strong>Slight haze in clear mode</strong> — barely noticeable, but not invisible.", "<strong>No thermal insulation</strong> to speak of."],
 glance=[("Privacy", (5, "Instant, total")), ("Light", (5, "Kept in both modes")), ("Darkness", (1, "None — not blackout")), ("Style", (5, "Sleek, invisible")), ("Maintenance", (5, "It’s glass")), ("Best for", "Bathrooms, offices, partitions, storefronts, clinics"), ("Options", "Wall switch · remote · app · voice · schedules · projection")],
 body2="""
        <div class="callout"><strong>Residential &amp; commercial</strong><p>We install smart film in homes — most often bathrooms and home offices — and in offices, clinics and stores across Montreal. Bring us the glass; we’ll tell you exactly what’s possible.</p></div>""",
 faq=[("Is smart film private at night with the lights on?", "Yes — in frosted mode you cannot see through it from either side, day or night. Silhouettes are not visible the way they are through a sheer."),
      ("Does smart film need power all the time?", "Only to be clear. Frosted (private) is the powered-off state, so it uses power only while you want transparency, and stays private in a power cut."),
      ("Can it go on my existing shower screen / window?", "In most cases yes — it’s applied to existing glass. We check the glass type and edges at a consultation."),
      ("Is it blackout?", "No. It gives privacy while still letting diffused light through. For darkness, pair it with a blackout blind or curtain."),
      ("Do you install it?", "Yes — we survey the glass, install the film and transformer, and connect your chosen controls, across Montreal.")],
 aside_h="See it switch, in person", aside_p="Free consultation. We assess your glass and show you a working sample.",
 cta_h="Clear. Frosted. <em>Your call.</em>", cta_p="Book a free consultation. We check your glass and quote on the spot.",
 related=[R["blackout"], R["condo"], R["motor"]]),

# ================================================================ ADVICE / SEO
dict(slug="blinds-vs-curtains.html", type="advice", crumb="Blinds vs curtains", read=6, image=IMG["living"],
 alt="A living room with layered window treatments",
 title="Blinds vs Curtains: Which Is Right for Your Room? (Room-by-Room Guide)",
 description="Blinds or curtains? A practical room-by-room comparison — light, privacy, insulation, cleaning, style and cost — plus why the best-looking homes usually layer both. Advice from a Montreal custom blinds studio.",
 og="A room-by-room answer, plus why the best-looking homes usually use both.",
 h1="Blinds vs curtains: which is right for <em>your</em> room?",
 lede="It’s the first question almost everyone asks us — and the honest answer is “it depends on the room.” Here’s the plain comparison, then a room-by-room verdict, then the trick designers use: both.",
 body="""
        <h2>The quick comparison</h2>
        <table class="specs">
          <tr><th></th><td><strong>Blinds</strong></td></tr>
          <tr><th>Look</th><td>Clean, tailored, minimal. Vanish when raised.</td></tr>
          <tr><th>Light control</th><td>Precise — from sheer to blackout; zebra and slats adjust by degrees.</td></tr>
          <tr><th>Insulation</th><td>Honeycomb: excellent. Roller/zebra: modest.</td></tr>
          <tr><th>Cleaning</th><td>Easy — dust or wipe.</td></tr>
          <tr><th>Wet rooms</th><td>Yes — easy-clean fabrics.</td></tr>
          <tr><th>Cost</th><td>Generally lower per window.</td></tr>
        </table>
        <table class="specs">
          <tr><th></th><td><strong>Curtains</strong></td></tr>
          <tr><th>Look</th><td>Soft, warm, dramatic. Make ceilings feel taller.</td></tr>
          <tr><th>Light control</th><td>Open or closed; sheers for filtering, blackout lining for dark.</td></tr>
          <tr><th>Insulation</th><td>Very good when lined; also absorb sound.</td></tr>
          <tr><th>Cleaning</th><td>Periodic; depends on fabric.</td></tr>
          <tr><th>Wet rooms</th><td>Not ideal.</td></tr>
          <tr><th>Cost</th><td>More fabric + lining, so usually higher.</td></tr>
        </table>

        <h2>Room by room</h2>
        <h3>Living room</h3>
        <p><strong>Both.</strong> A sheer curtain or <a href="day-and-night-zebra-blinds.html">zebra blind</a> for daytime light and privacy, with curtains for warmth and evenings. If you must pick one: curtains for a soft, finished room; a zebra blind for a modern one with big glass.</p>
        <h3>Bedroom</h3>
        <p><strong>Blackout is the priority</strong> — a <a href="blackout-blinds.html">blackout blind with side channels</a> does the job best, and blackout-lined curtains over it give the hotel look. Cold room? <a href="honeycomb-blinds.html">Blackout honeycomb</a>.</p>
        <h3>Kitchen &amp; bathroom</h3>
        <p><strong>Blinds.</strong> An easy-clean <a href="roller-blinds.html">roller</a> or a washable-fabric <a href="roman-shades.html">Roman shade</a>. Curtains and steam/splashes don’t mix. Bathroom with a glass shower? Consider <a href="smart-film.html">smart film</a>.</p>
        <h3>Home office</h3>
        <p><strong>Blinds</strong> — glare control matters most on a screen. A zebra or dim-out roller; honeycomb if the window is cold.</p>
        <h3>Dining room</h3>
        <p><strong>Curtains or Roman shades</strong> — softness and a bit of occasion.</p>
        <h3>Kids’ room / nursery</h3>
        <p><strong>Cordless blackout blind</strong> — safety and sleep. See the <a href="blackout-blinds-for-nursery.html">nursery guide</a>.</p>
        <h3>Patio door / very wide window</h3>
        <p><strong>Curtains on a track</strong> or a wide <a href="roller-blinds.html">roller</a>/zebra blind. Roman shades get heavy over ~2 m.</p>

        <h2>The designer answer: layer them</h2>
        <p>Walk through any well-designed home and you’ll notice most windows have <em>two</em> treatments: a functional layer for light and privacy (a blind or sheer) and a decorative layer for softness (curtains). You get precise control by day and warmth by night — and it photographs beautifully. It doesn’t have to be expensive: a simple roller or honeycomb behind a pair of lined curtains is a classic.</p>
        <div class="callout"><strong>Our honest rule of thumb</strong><p>Wet or high-use room → blind. Room you relax in → curtains (or both). Bedroom → blackout first, style second. Cold window → honeycomb, whatever else you add.</p></div>""",
 pros=None, cons=None, glance=None, body2="",
 faq=[("Are blinds or curtains better for insulation?", "Lined curtains insulate well; honeycomb (cellular) blinds insulate best of any single treatment. Combining a honeycomb blind with lined curtains is the warmest option of all."),
      ("Are blinds or curtains cheaper?", "Blinds are usually cheaper per window; curtains use more fabric plus lining. Layering both costs more but often replaces the need for a premium single treatment."),
      ("Can I have both blinds and curtains on one window?", "Yes — it’s the classic designer approach. A blind or sheer for function, curtains for softness. We do this combination constantly."),
      ("What’s best for a bedroom?", "Blackout. A blackout blind with side channels for real darkness, optionally with blackout-lined curtains over it. Add honeycomb if the room is cold."),
      ("Do you do both blinds and curtains?", "Yes — all custom-made, and we install everything free across Montreal.")],
 aside_h="Not sure? We’ll tell you honestly", aside_p="Free in-home consultation. We look at each room and recommend blinds, curtains or both — with samples.",
 cta_h="Blinds, curtains, or <em>both</em> — decided in your living room.", cta_p="Book a free consultation. We bring samples of everything and give you a straight answer, room by room.",
 related=[R["curtains"], R["roller"], R["honey"]]),

dict(slug="best-blinds-for-montreal-winters.html", type="advice", crumb="Blinds for Montreal winters", read=6, image=IMG["bedroom"],
 alt="A cosy bedroom in soft winter daylight",
 title="The Best Blinds for Montreal Winters (and Lower Heating Bills)",
 description="Windows lose a surprising amount of heat. Here's what actually helps in a Montreal winter, ranked — honeycomb blinds, lined curtains, layering, and the mounting details that matter — from a local custom blinds studio.",
 og="Windows lose a surprising amount of heat — here’s what actually helps, ranked.",
 h1="The best blinds for Montreal winters — <em>ranked.</em>",
 lede="Stand next to a window in January and you can feel it: cold pouring off the glass. Windows are the weakest link in a home’s insulation, and the right window covering makes a real, felt difference. Here’s what works, in order.",
 body="""
        <h2>Why windows matter so much</h2>
        <p>Even good double glazing insulates far worse than an insulated wall. A big or older window can be responsible for a large share of a room’s heat loss — which is why the area near the glass feels cold and why your heating runs harder. A window covering that traps still air against the glass slows that loss down.</p>

        <h2>Ranked: what actually helps</h2>
        <h3>1. Honeycomb (cellular) blinds — the winner</h3>
        <p>Cellular shades trap air in rows of closed pockets, and still air is a poor conductor of heat. Nothing else in the blinds world comes close. <strong>Double-cell</strong> honeycomb roughly doubles the effect again — that’s the pick for the coldest windows. Mount them <em>inside</em> the frame, close to the glass, so the trapped layer is sealed. Read the full <a href="honeycomb-blinds.html">honeycomb guide</a>.</p>
        <h3>2. Lined curtains — a close second, and warmer-feeling</h3>
        <p>Heavy, <strong>thermally lined</strong> curtains that hang to the floor and overlap the window generously create a big pocket of still air. They also absorb sound and make a room feel cosy. The details matter: floor length, wide overlap, and ideally a wraparound track so the sides seal. See <a href="curtains-and-drapes.html">curtains &amp; drapes</a>.</p>
        <h3>3. Layer the two — the warmest option of all</h3>
        <p>A honeycomb blind against the glass with lined curtains in front. Two trapped air layers, maximum comfort, and it looks like a designer did it. This is what we recommend for cold bedrooms and big living-room windows.</p>
        <h3>4. Roman shades, lined</h3>
        <p>A lined Roman shade helps meaningfully — more than a roller, less than honeycomb — and looks lovely.</p>
        <h3>5. Roller and zebra blinds — modest</h3>
        <p>A single fabric layer with gaps at the sides doesn’t trap much air. Still useful for privacy and glare, and blackout/thermal-backed fabrics help a bit — but if warmth is the goal, choose honeycomb.</p>

        <h2>The details that make it work</h2>
        <ul>
          <li><strong>Fit close to the glass</strong> — an inside mount with minimal gaps seals the air layer.</li>
          <li><strong>Close them at dusk</strong> — most heat is lost overnight; open on sunny days to catch free solar heat, especially south-facing.</li>
          <li><strong>Side channels</strong> on a honeycomb or blackout blind seal the edges — better insulation <em>and</em> darkness.</li>
          <li><strong>Automate it</strong> — <a href="motorized-blinds.html">motorized</a> blinds on a sunset/sunrise schedule do the closing for you.</li>
        </ul>
        <div class="callout"><strong>What clients tell us</strong><p>The most common comment after we install honeycomb blinds in an older Montreal home is some version of “the room just feels warmer.” It’s not imagination — it’s the cold draft off the glass being interrupted.</p></div>""",
 pros=None, cons=None, glance=None, body2="",
 faq=[("What are the warmest blinds?", "Honeycomb (cellular) blinds — double-cell for the coldest windows — mounted close to the glass. Layer lined curtains over them for maximum effect."),
      ("Do blinds really reduce heating bills?", "They reduce heat loss through the glass, so your heating runs less to hold the same temperature. The effect is biggest on large, old or north-facing windows, and most noticeable in comfort near the window."),
      ("Are curtains warmer than blinds?", "Thermally lined, floor-length curtains are very warm — comparable to a good honeycomb blind. Together they beat either alone."),
      ("Should blinds be open or closed in winter?", "Closed at night and on grey days to hold heat in; open on sunny days (especially south-facing) to let free solar warmth in. A motorized schedule makes this automatic."),
      ("Do you install honeycomb blinds in Montreal?", "Yes — custom-made and installed free across the island and surroundings.")],
 aside_h="Warm up the cold room", aside_p="Free in-home consultation. We check your windows and recommend the right combination for real winter comfort.",
 cta_h="Feel the difference <em>this</em> winter.", cta_p="Book a free consultation. We measure, bring honeycomb and lining samples, and install for free.",
 related=[R["honey"], R["curtains"], R["motor"]]),

dict(slug="blackout-blinds-for-nursery.html", type="advice", crumb="Blackout for a nursery", read=5, image=IMG["calm"],
 alt="A calm, minimalist room in soft light",
 title="Blackout Blinds for a Nursery: A Parent’s Guide to Better Naps",
 description="Choosing blackout blinds for a baby's room: cordless safety, real darkness (side channels), easy-clean fabrics, insulation, and quiet motorized options. Practical advice from a Montreal custom blinds studio.",
 og="Safety, darkness and durability — what to look for when the goal is sleep.",
 h1="Blackout blinds for a nursery: a parent’s guide to <em>better naps.</em>",
 lede="A dark room is one of the few things about baby sleep that’s actually within your control. Here’s how to get real darkness safely — and the details parents tell us they wish they’d known.",
 body="""
        <h2>The four things that matter</h2>
        <h3>1. Cordless. Always.</h3>
        <p>Dangling cords and chains are a strangulation hazard for babies and toddlers. Choose <strong>cordless (spring)</strong> or <strong>motorized</strong> operation — no loops, nothing to reach. This is non-negotiable in a nursery, and everything we recommend below is cordless.</p>
        <h3>2. Real darkness, not “dark-ish”</h3>
        <p>Blackout fabric alone leaks light around the edges — bright bars at 5 a.m. To get truly dark you want a blackout blind running in <strong>side channels</strong> (or a generous outside mount, ideally with blackout curtains over). Read <a href="blackout-blinds.html">how to actually get total darkness</a>.</p>
        <h3>3. Easy to clean</h3>
        <p>Nurseries get sticky. A <strong>blackout roller</strong> in a wipe-clean fabric is the practical winner. If the room is cold, a <strong>blackout honeycomb</strong> adds insulation and quiet — dust it gently.</p>
        <h3>4. Quiet operation</h3>
        <p>You will be leaving that room on tiptoe. Cordless springs are silent; good motors are whisper-quiet and let you open the blind slowly on a schedule so mornings are gentle rather than sudden.</p>

        <h2>Our nursery recommendation</h2>
        <ul>
          <li><strong>Blackout roller blind, cordless or motorized, with side channels</strong> — the tightest seal, easiest to clean, most economical.</li>
          <li><strong>Blackout honeycomb with channels</strong> if the room is cold or noisy — darkness plus insulation and sound dampening.</li>
          <li><strong>Optional:</strong> blackout-lined curtains over the top for softness and an extra light seal — mount the track high and wide, and keep them out of reach of a standing toddler.</li>
        </ul>
        <div class="callout"><strong>Small things that help</strong><p>Choose a light-coloured or patterned face fabric so the room stays cheerful by day. Ask for a bottom seal. And if you’re motorizing, set a “slow open” schedule for wake time — it works surprisingly well.</p></div>

        <h2>What to avoid</h2>
        <ul>
          <li>Any corded blind or chain within reach.</li>
          <li>Inside-mount blackout with no channels — you’ll get light halos.</li>
          <li>Heavy curtains a toddler can pull down — or mount them securely and high.</li>
        </ul>""",
 pros=None, cons=None, glance=None, body2="",
 faq=[("Are blackout blinds safe for a nursery?", "Yes, when they are cordless (spring) or motorized — no hanging cords or chains. Everything we recommend for nurseries is cordless."),
      ("How do I make a nursery completely dark?", "A blackout blind running in side channels (with a bottom seal), or an outside mount with generous overlap plus blackout curtains over it. Blackout fabric alone leaks at the edges."),
      ("Roller or honeycomb for a baby’s room?", "Roller for easiest cleaning and best value; honeycomb if the room is cold or noisy, because it adds insulation and quiet."),
      ("Can I set the blind to open at wake time?", "Yes — motorized blinds can open slowly on a schedule so mornings are gentle."),
      ("Do you install them?", "Yes — measured, fitted with channels where needed and installed free across Montreal.")],
 aside_h="Get the nursery truly dark", aside_p="Free in-home consultation. We check the window and spec a cordless, sealed blackout that actually works.",
 cta_h="Better naps start with a <em>darker</em> room.", cta_p="Book a free consultation. Cordless, sealed, easy-clean — measured and installed free.",
 related=[R["blackout"], R["honey"], R["motor"]]),

dict(slug="how-to-measure-windows-for-blinds.html", type="advice", crumb="How to measure", read=6, image=IMG["measure"],
 alt="Measuring a window frame for custom blinds",
 title="How to Measure Windows for Blinds (Inside vs Outside Mount, Step by Step)",
 description="How to measure a window for blinds: inside vs outside mount, the three-width rule, depth for cassettes and channels, common mistakes — and why we still come and measure for you free in Montreal.",
 og="The steps, the common mistakes — and why we still come and measure for you.",
 h1="How to measure windows for blinds — and the mistakes that <em>ruin</em> a fit.",
 lede="Custom blinds only look custom if the measurements are exact. Here’s exactly how it’s done, so you understand what a good fit needs — and why, for the real thing, we come and measure for you at no charge.",
 body="""
        <h2>First decide: inside or outside mount?</h2>
        <h3>Inside mount</h3>
        <p>The blind sits <em>inside</em> the window recess. Clean and tailored; shows off the trim; keeps the sill usable. Needs enough <strong>depth</strong> for the mechanism (a cassette or side channels need more) and a reasonably square opening. Small light gaps at the sides are normal — add channels for blackout.</p>
        <h3>Outside mount</h3>
        <p>The blind mounts on the wall or trim <em>over</em> the opening, larger than the window. Hides an out-of-square or shallow frame, makes the window look bigger, and gives better light block because the fabric overlaps the opening. The usual choice for curtains and Roman shades, and for blackout without channels.</p>

        <h2>Measuring an inside mount</h2>
        <ol>
          <li><strong>Width — measure three times.</strong> Top, middle and bottom of the recess. Frames are rarely square. Use the <em>narrowest</em> measurement.</li>
          <li><strong>Height — measure three times.</strong> Left, centre and right, from the top of the recess to the sill. Use the <em>longest</em> for a blind that should reach the sill.</li>
          <li><strong>Depth.</strong> Measure the recess depth. Each blind type needs a minimum depth to mount flush (a cassette or side channels need more). If it’s shallow, go outside mount.</li>
          <li><strong>Check for obstructions</strong> — handles, cranks, tiles, alarm sensors.</li>
          <li><strong>Don’t deduct anything.</strong> Give the exact opening size; the maker takes the correct clearance for that product.</li>
        </ol>

        <h2>Measuring an outside mount</h2>
        <ol>
          <li><strong>Width.</strong> Measure the opening and add overlap on each side — typically 5–8 cm per side (more for blackout).</li>
          <li><strong>Height.</strong> Decide where the top will mount (above the frame) and where the bottom should end (sill, or below it), and measure between.</li>
          <li><strong>Check the mounting surface</strong> is flat and solid, and that there’s room above the frame for the headrail.</li>
        </ol>

        <h2>Common mistakes we see</h2>
        <ul>
          <li>Measuring once, in the middle only — then finding the top is 8 mm narrower.</li>
          <li>Rounding to the nearest centimetre. Millimetres matter.</li>
          <li>Deducting clearance yourself, then the maker deducts again → gaps.</li>
          <li>Forgetting depth — the cassette won’t sit inside the recess.</li>
          <li>Ignoring the handle that swings into the blind.</li>
          <li>Using a cloth or bent tape — use a rigid steel tape.</li>
        </ul>

        <div class="callout"><strong>Here’s the thing</strong><p>You don’t need to do any of this. Every My Kurtains order includes a <strong>free in-home measure</strong> by the people who will install it — we take responsibility for the fit. This guide is here so you understand what “made to measure” really means, and so you can sanity-check anyone else’s work.</p></div>""",
 pros=None, cons=None, glance=None, body2="",
 faq=[("Do I measure the window or the blind size?", "Give the exact opening size (for inside mount) and let the manufacturer make the deductions for that specific product — never deduct yourself, or you’ll double-deduct and get gaps."),
      ("Inside or outside mount — which is better?", "Inside for a clean, tailored look if you have depth and a square frame. Outside to hide an out-of-square or shallow recess, make the window look larger, or improve light block."),
      ("How much overlap for an outside mount?", "Typically 5–8 cm each side and above the frame; more if you want blackout without side channels."),
      ("Why measure width in three places?", "Because window recesses are rarely perfectly square. Using the narrowest measurement ensures the blind fits everywhere."),
      ("Do you measure for me?", "Yes — a free in-home measure is included with every order across Montreal, done by our installers.")],
 aside_h="Skip the tape measure", aside_p="Free in-home measure and consultation. We measure every window ourselves and guarantee the fit.",
 cta_h="Made to measure means <em>we</em> measure.", cta_p="Book a free consultation. We come to you, measure precisely and install for free.",
 related=[R["roller"], R["honey"], R["vs"]]),

dict(slug="blinds-for-condos-and-apartments.html", type="advice", crumb="Blinds for condos", read=6, image=IMG["condo"],
 alt="A contemporary condo living room with floor-to-ceiling windows",
 title="Best Blinds for Condos & Apartments in Montreal (Privacy, Big Glass, Bylaws)",
 description="The best blinds for Montreal condos and apartments: privacy with close neighbours, floor-to-ceiling and wide windows, glare on screens, heat, syndicate/bylaw rules and rentals. Custom-made and installed free.",
 og="Big glass, close neighbours, strata rules — how to get privacy without losing the view.",
 h1="Best blinds for condos &amp; apartments: privacy without losing the <em>view.</em>",
 lede="Condo living in Montreal means a lot of glass, neighbours a few metres away, sun on the sofa at 4 p.m. — and a syndicate with opinions about what’s visible from outside. Here’s how to solve all of it.",
 body="""
        <h2>The condo problems, and what solves them</h2>
        <h3>Close neighbours → privacy without going dark</h3>
        <p><a href="day-and-night-zebra-blinds.html"><strong>Day &amp; night (zebra) blinds</strong></a> are the condo hero: line up the solid bands for privacy, the sheers for the view, in one movement. A sheer curtain on a track is the softer alternative. For bedrooms, a blackout blind — see below.</p>
        <h3>Floor-to-ceiling and very wide windows</h3>
        <p><strong>Roller and zebra blinds</strong> handle wide spans cleanly, and <strong>curtains on a ceiling track</strong> look stunning on tall glass. Motorization is worth it here — those are heavy blinds to hoist several times a day. Roman shades get heavy over ~2 m, so we split them or steer you elsewhere.</p>
        <h3>Sun and heat</h3>
        <p>West- and south-facing condos cook in summer. <strong>Solar/reflective roller fabrics</strong> cut heat and glare while keeping the view; <a href="honeycomb-blinds.html"><strong>honeycomb</strong></a> insulates against both summer heat and winter cold; <a href="outdoor-blinds.html"><strong>exterior shades</strong></a> on a balcony are the most effective of all (bylaws permitting).</p>
        <h3>Screens and glare</h3>
        <p>Working from home? A dim-out roller or a zebra blind on the home-office window keeps glare off the screen without shutting the daylight out.</p>
        <h3>Sleep in a bright city</h3>
        <p>Streetlights, neighbours’ lights, early sun: a <a href="blackout-blinds.html"><strong>blackout blind with side channels</strong></a> in the bedroom. Cold glass? Blackout honeycomb.</p>

        <h2>Bylaws, syndicates and rentals</h2>
        <ul>
          <li><strong>“Uniform exterior appearance” rules</strong> are common — many buildings require white or off-white on the street-facing side. Most of our fabrics have a neutral backing so you can have colour inside and white outside; we’ll check your rules with you.</li>
          <li><strong>Exterior fittings</strong> (outdoor blinds) usually need approval — we can help you present it.</li>
          <li><strong>Renting?</strong> Everything we install can be removed cleanly; inside mounts leave only small screw holes in the frame. Tension and no-drill options exist for some windows — ask us.</li>
        </ul>

        <h2>Our condo picks</h2>
        <ul>
          <li><strong>Living room:</strong> zebra blinds (or sheer curtains on a track), motorized if the glass is big.</li>
          <li><strong>Bedroom:</strong> blackout roller or honeycomb with side channels — cordless or motorized.</li>
          <li><strong>Home office:</strong> dim-out roller or zebra.</li>
          <li><strong>Balcony door:</strong> a wide roller/zebra or a curtain track.</li>
          <li><strong>Balcony itself:</strong> outdoor blinds, if the syndicate agrees.</li>
        </ul>
        <div class="callout"><strong>Montreal specific</strong><p>Many downtown and Griffintown towers have very tall glass and strict facade rules. We install in these buildings constantly — bring us your bylaws and we’ll pick fabrics that satisfy the syndicate <em>and</em> you.</p></div>""",
 pros=None, cons=None, glance=None, body2="",
 faq=[("What blinds are best for a condo with big windows?", "Zebra (day & night) or roller blinds for wide spans, curtains on a ceiling track for tall glass — and motorization, because big blinds are heavy to operate daily."),
      ("How do I get privacy without blocking the view?", "Zebra blinds: align the solid bands for privacy, the sheers for the view. Or a sheer curtain by day with a blind or drape for night."),
      ("My building requires white from outside — can I still have colour?", "Usually yes. Most of our fabrics have a neutral (white/off-white) backing, so you get colour inside and a uniform look outside. We’ll check your bylaws."),
      ("Can I install blinds in a rental?", "Yes — inside mounts leave only small screw holes, and no-drill options exist for some windows. Ask us."),
      ("Do you install in condo towers?", "Yes — all over Montreal, including buildings with strict facade rules and very tall glass. Installation is free.")],
 aside_h="Condo-savvy advice", aside_p="Free in-home consultation. Bring your bylaws — we’ll recommend blinds that work for your glass, your neighbours and your syndicate.",
 cta_h="Big glass, close neighbours, <em>solved.</em>", cta_p="Book a free consultation. We measure, check your building rules and install for free.",
 related=[R["zebra"], R["blackout"], R["outdoor"]]),
]

if __name__ == "__main__":
    for p in POSTS:
        with open(os.path.join(HERE, p["slug"]), "w", encoding="utf-8") as f:
            f.write(render(p, "en"))
        print("wrote", p["slug"])
    os.makedirs(os.path.join(HERE, "fr"), exist_ok=True)
    from _content_fr import POSTS_FR
    for p in POSTS_FR:
        with open(os.path.join(HERE, "fr", p["slug"]), "w", encoding="utf-8") as f:
            f.write(render(p, "fr"))
        print("wrote fr/" + p["slug"])
