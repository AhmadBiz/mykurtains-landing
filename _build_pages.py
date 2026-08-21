#!/usr/bin/env python3
"""Build the standalone pages (contact, faq, about, privacy, thank-you) in EN + FR.

These URLs existed on the old Wix site and are still indexed by Google, so they
keep their original paths. Run after editing content:  python3 _build_pages.py
"""
import os, json, html

SITE = "https://www.mykurtains.com"
GTM = "GTM-53NZB6T9"
TEL = "+14384020559"
TEL_PRETTY = "+1 (438) 402-0559"
EMAIL = "hello@mykurtains.com"
WA = "https://wa.me/14384020559"
CAL_EN = "https://calendly.com/mykurtains/mykurtains-consultation"
CAL_FR = "https://calendly.com/mykurtains/consultation"
UPDATED = "2026-08-20"

# ---------------------------------------------------------------- head/chrome

CONSENT = """    <!-- Consent Mode v2 (Law 25): default = denied until the visitor chooses. Runs BEFORE GTM. -->
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    (function(){
      var saved = null; try { saved = localStorage.getItem('mk_consent'); } catch(e){}
      var granted = saved === 'granted';
      gtag('consent', 'default', {
        ad_storage: granted ? 'granted' : 'denied',
        ad_user_data: granted ? 'granted' : 'denied',
        ad_personalization: granted ? 'granted' : 'denied',
        analytics_storage: granted ? 'granted' : 'denied',
        functionality_storage: 'granted',
        security_storage: 'granted',
        wait_for_update: 500
      });
      window.__mkConsent = saved; // 'granted' | 'denied' | null (not chosen yet)
      // Meta Pixel doesn't follow Google Consent Mode, and GTM's fbq('init') resets Meta's own
      // consent flag. So gate at the network level: while not granted, fbq is a sink that drops
      // every call. On Accept we hand off to Meta's canonical bootstrap and GTM's tag re-inits.
      window.__mkPixelGranted = granted;
      if (!granted) {
        var sink = function(){ /* dropped: no consent */ };
        sink.callMethod = null; sink.queue = []; sink.push = sink; sink.loaded = true; sink.version = '2.0';
        window.fbq = window._fbq = sink;
      }
    })();
  </script>
  <!-- Google Tag Manager (loads GA4 + Meta Pixel; configured in GTM) -->
  <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','""" + GTM + """');</script>
  <!-- End Google Tag Manager -->"""

LOGO_SVG = ('<svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">'
            '<circle cx="32" cy="32" r="26" stroke="currentColor" stroke-width="3"/>'
            '<g stroke="currentColor" stroke-width="3" stroke-linecap="round">'
            '<line x1="9" y1="32" x2="29.5" y2="32"/><line x1="34.5" y1="32" x2="55" y2="32"/>'
            '<line x1="32" y1="9" x2="32" y2="55"/><line x1="25" y1="10.1" x2="25" y2="53.9"/>'
            '<line x1="39" y1="10.1" x2="39" y2="53.9"/>'
            '<line x1="18" y1="32" x2="18" y2="50.25"/><line x1="46" y1="13.75" x2="46" y2="32"/>'
            '</g></svg>')

WA_SVG = ('<svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">'
          '<path d="M12.04 2c-5.46 0-9.9 4.44-9.9 9.9 0 1.75.46 3.45 1.32 4.95L2 22l5.28-1.38a9.86 9.86 0 004.76 1.22h.004c5.46 0 9.9-4.44 9.9-9.9 0-2.64-1.03-5.13-2.9-7A9.82 9.82 0 0012.04 2zm5.8 14.2c-.24.68-1.42 1.32-1.95 1.36-.5.05-.98.24-3.33-.7-2.8-1.1-4.6-3.96-4.74-4.14-.14-.18-1.15-1.53-1.15-2.92s.73-2.07.98-2.35c.26-.28.56-.35.75-.35.18 0 .37 0 .53.01.17.01.4-.06.62.47.24.56.8 1.95.87 2.1.07.14.12.3.02.48-.1.18-.14.3-.28.46-.14.16-.3.36-.42.48-.14.14-.28.29-.12.57.16.28.72 1.18 1.54 1.9 1.06.94 1.95 1.24 2.23 1.38.28.14.44.12.6-.07.18-.2.7-.8.88-1.08.18-.28.36-.24.6-.14.24.09 1.55.73 1.82.86.26.14.44.2.5.32.06.11.06.66-.18 1.34z"/></svg>')

LANG = {
    "en": {
        "home": "index.html", "other_home": "index-fr.html",
        "nav": [("#collections", "Collections"), ("#why", "Why Us"), ("#process", "How It Works"),
                ("#gallery", "Gallery"), ("#reviews", "Reviews")],
        "guides": "Guides", "guides_href": "blog/index.html",
        "switch": "FR", "switch_label": "Voir le site en français",
        "cta": "Free Consultation", "cta_long": "Book Free Consultation",
        "mobile_lang": "Voir en français →",
        "f_tag": "High style, low cost. Custom blinds, curtains &amp; smart film, made and installed across Montreal.",
        "f_explore": "Explore", "f_touch": "Get in touch", "f_follow": "Follow",
        "f_guides": "Guides &amp; advice",
        "f_area": "Serving Montréal, Laval &amp; the South Shore · Mon–Sat by appointment",
        "f_made": "Made with care for beautiful windows.",
        "f_contact": "Contact", "f_faq": "FAQ", "f_about": "About", "f_privacy": "Privacy",
        "wa_label": "Message us on WhatsApp",
        "cal": CAL_EN, "locale": "en_CA",
    },
    "fr": {
        "home": "index-fr.html", "other_home": "index.html",
        "nav": [("#collections", "Collections"), ("#why", "Pourquoi nous"), ("#process", "Comment ça marche"),
                ("#gallery", "Galerie"), ("#reviews", "Avis")],
        "guides": "Guides", "guides_href": "blog/fr/index.html",
        "switch": "EN", "switch_label": "View the site in English",
        "cta": "Consultation gratuite", "cta_long": "Réserver ma consultation",
        "mobile_lang": "View in English →",
        "f_tag": "Haut style, bas prix. Stores, rideaux et film intelligent sur mesure, fabriqués et installés partout à Montréal.",
        "f_explore": "Explorer", "f_touch": "Nous joindre", "f_follow": "Suivez-nous",
        "f_guides": "Guides &amp; conseils",
        "f_area": "Montréal, Laval et la Rive-Sud · Du lundi au samedi, sur rendez-vous",
        "f_made": "Fait avec soin pour de belles fenêtres.",
        "f_contact": "Nous joindre", "f_faq": "FAQ", "f_about": "À propos", "f_privacy": "Confidentialité",
        "wa_label": "Écrivez-nous sur WhatsApp",
        "cal": CAL_FR, "locale": "fr_CA",
    },
}


def chrome(lang, up, slug):
    """Nav + footer for a page `up` levels below the site root."""
    L = LANG[lang]
    home = up + L["home"]
    # the same page in the other language: /contact/ <-> /contact/fr/
    alt = "../" if lang == "fr" else "fr/"

    nav_links = "".join(f'<a href="{home}{h}">{t}</a>' for h, t in L["nav"])
    mob_links = "".join(f'<a href="{home}{h}">{t}</a>' for h, t in L["nav"])
    guides = up + L["guides_href"]

    nav = f"""  <header class="nav nav--light scrolled" id="nav">
    <div class="nav__inner container">
      <a href="{home}" class="brand" aria-label="My Kurtains"><span class="brand__mark" aria-hidden="true">{LOGO_SVG}</span><span class="brand__name">My<em>Kurtains</em></span></a>
      <nav class="nav__links" aria-label="Primary">{nav_links}<a href="{guides}">{L['guides']}</a></nav>
      <div class="nav__cta">
        <a href="{alt}" class="btn btn--ghost btn--sm lang-switch" hreflang="{'en' if lang=='fr' else 'fr'}" aria-label="{L['switch_label']}">{L['switch']}</a>
        <a href="tel:{TEL}" class="btn btn--ghost btn--sm">438&nbsp;402&nbsp;0559</a>
        <a href="{home}#contact" class="btn btn--solid btn--sm" data-calendly>{L['cta']}</a>
      </div>
      <button class="nav__toggle" id="navToggle" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
    <div class="nav__mobile" id="navMobile">{mob_links}<a href="{guides}">{L['guides']}</a>
      <a href="{alt}" hreflang="{'en' if lang=='fr' else 'fr'}" class="nav__mobile-lang">{L['mobile_lang']}</a>
      <a href="{home}#contact" class="btn btn--solid" data-calendly>{L['cta_long']}</a>
    </div>
  </header>"""

    footer = f"""  <footer class="footer">
    <div class="container footer__inner">
      <div class="footer__brand"><span class="brand__name">My<em>Kurtains</em></span><p>{L['f_tag']}</p></div>
      <nav class="footer__col" aria-label="Sitemap"><h4>{L['f_explore']}</h4><a href="{home}#collections">Collections</a><a href="{guides}">{L['f_guides']}</a><a href="{up}about/{'fr/' if lang=='fr' else ''}">{L['f_about']}</a><a href="{up}faq/{'fr/' if lang=='fr' else ''}">{L['f_faq']}</a></nav>
      <nav class="footer__col" aria-label="Contact"><h4>{L['f_touch']}</h4><a href="tel:{TEL}">{TEL_PRETTY}</a><a href="mailto:{EMAIL}">{EMAIL}</a><a href="{WA}" target="_blank" rel="noopener">WhatsApp</a><a href="{up}contact/{'fr/' if lang=='fr' else ''}">{L['f_contact']}</a></nav>
      <div class="footer__col"><h4>{L['f_follow']}</h4><div class="footer__social"><a href="https://www.instagram.com/mykurtains/" target="_blank" rel="noopener">Instagram</a><a href="https://www.facebook.com/mykurtains" target="_blank" rel="noopener">Facebook</a></div></div>
    </div>
    <div class="footer__bar container"><span>© <span id="year"></span> My Kurtains — Montreal, QC</span><span class="footer__area">{L['f_area']}</span><span><a href="{up}privacy/{'fr/' if lang=='fr' else ''}">{L['f_privacy']}</a></span></div>
  </footer>
  <a href="{WA}" class="fab" target="_blank" rel="noopener" aria-label="{L['wa_label']}">{WA_SVG}</a>
  <script src="{up}script.js"></script>"""
    return nav, footer


def render(lang, slug, title, desc, hero_eyebrow, hero_h1, hero_lede, body,
           schema=None, noindex=False, wide=False):
    L = LANG[lang]
    up = "../" if lang == "en" else "../../"
    en_url = f"{SITE}/{slug}/"
    fr_url = f"{SITE}/{slug}/fr/"
    canonical = en_url if lang == "en" else fr_url
    nav, footer = chrome(lang, up, slug)

    robots = '\n  <meta name="robots" content="noindex, follow" />' if noindex else ""
    alts = "" if noindex else f"""
  <link rel="alternate" hreflang="en" href="{en_url}" />
  <link rel="alternate" hreflang="fr" href="{fr_url}" />
  <link rel="alternate" hreflang="x-default" href="{en_url}" />"""
    ld = ""
    if schema:
        ld = '\n  <script type="application/ld+json">' + json.dumps(schema, ensure_ascii=False) + '</script>'

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="theme-color" content="#141210" />
{CONSENT}
  <title>{title}</title>
  <meta name="description" content="{desc}" />{robots}
  <link rel="canonical" href="{canonical}" />{alts}
  <meta property="og:type" content="website" />
  <meta property="og:locale" content="{L['locale']}" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:url" content="{canonical}" />
  <meta property="og:site_name" content="My Kurtains" />
  <meta property="og:image" content="{SITE}/assets/og-image.jpg" />
  <meta name="twitter:card" content="summary_large_image" />{ld}
  <link rel="icon" href="{up}assets/favicon.svg" type="image/svg+xml" />
  <link rel="icon" type="image/png" sizes="32x32" href="{up}assets/favicon-32.png" />
  <link rel="icon" type="image/png" sizes="192x192" href="{up}assets/favicon-192.png" />
  <link rel="apple-touch-icon" sizes="180x180" href="{up}assets/apple-touch-icon.png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..700;1,9..144,400&family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="{up}styles.css" />
  <link rel="stylesheet" href="{up}blog/blog.css" />
  <link rel="stylesheet" href="https://assets.calendly.com/assets/external/widget.css" />
  <script src="https://assets.calendly.com/assets/external/widget.js" async></script>
</head>
<body>
  <!-- Google Tag Manager (noscript) -->
  <noscript><iframe src="https://www.googletagmanager.com/ns.html?id={GTM}" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
  <!-- End Google Tag Manager (noscript) -->

{nav}

  <main>
    <section class="blog-hero">
      <div class="container">
        <p class="eyebrow">{hero_eyebrow}</p>
        <h1 class="section__title">{hero_h1}</h1>
        <p class="section__lede">{hero_lede}</p>
      </div>
    </section>

{body}
  </main>

{footer}
</body>
</html>
"""


# ---------------------------------------------------------------- form markup

def form_html(lang):
    if lang == "en":
        opts = ["Curtains &amp; Drapes", "Roller Blinds", "Roman Shades", "Day &amp; Night / Zebra",
                "Honeycomb Blinds", "Motorized", "Blockout Blind", "Heavy-Duty (Outdoor) Blinds",
                "Smart Film", "Not sure yet — help me choose"]
        t = dict(name="Name", ph_name="Your name", phone="Phone or email",
                 ph_phone="How can we reach you?", interest="I&rsquo;m interested in",
                 msg="Message <span>(optional)</span>",
                 ph_msg="Number of windows, timeline, anything helpful…",
                 submit="Request my free consultation")
    else:
        opts = ["Rideaux &amp; draperies", "Stores enrouleurs", "Stores bateau", "Jour &amp; nuit / Zébré",
                "Stores alvéolaires", "Motorisé", "Store Blockout", "Stores robustes (extérieur)",
                "Film intelligent", "Je ne sais pas encore — aidez-moi à choisir"]
        t = dict(name="Nom", ph_name="Votre nom", phone="Téléphone ou courriel",
                 ph_phone="Comment vous joindre ?", interest="Je suis intéressé(e) par",
                 msg="Message <span>(facultatif)</span>",
                 ph_msg="Nombre de fenêtres, échéancier, tout détail utile…",
                 submit="Demander ma consultation gratuite")
    options = "".join(f"<option>{o}</option>" for o in opts)
    return f"""          <form class="contact__form" id="contactForm" novalidate>
            <input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true" />
            <div class="field">
              <label for="name">{t['name']}</label>
              <input type="text" id="name" name="name" autocomplete="name" required placeholder="{t['ph_name']}" />
            </div>
            <div class="field">
              <label for="phone">{t['phone']}</label>
              <input type="text" id="phone" name="phone" required placeholder="{t['ph_phone']}" />
            </div>
            <div class="field">
              <label for="interest">{t['interest']}</label>
              <select id="interest" name="interest">{options}</select>
            </div>
            <div class="field">
              <label for="message">{t['msg']}</label>
              <textarea id="message" name="message" rows="3" placeholder="{t['ph_msg']}"></textarea>
            </div>
            <button type="submit" class="btn btn--solid btn--lg btn--block">{t['submit']}</button>
            <p class="contact__note" id="formNote" role="status"></p>
          </form>"""


def methods_html(lang):
    if lang == "en":
        return f"""          <div class="contact__methods">
            <a class="method" href="tel:{TEL}"><span class="method__ic">📞</span><span><strong>Call us</strong>{TEL_PRETTY}</span></a>
            <a class="method" href="{WA}" target="_blank" rel="noopener"><span class="method__ic">💬</span><span><strong>WhatsApp</strong>Text us anytime</span></a>
            <a class="method" href="mailto:{EMAIL}"><span class="method__ic">✉️</span><span><strong>Email</strong>{EMAIL}</span></a>
          </div>"""
    return f"""          <div class="contact__methods">
            <a class="method" href="tel:{TEL}"><span class="method__ic">📞</span><span><strong>Appelez-nous</strong>{TEL_PRETTY}</span></a>
            <a class="method" href="{WA}" target="_blank" rel="noopener"><span class="method__ic">💬</span><span><strong>WhatsApp</strong>Écrivez-nous en tout temps</span></a>
            <a class="method" href="mailto:{EMAIL}"><span class="method__ic">✉️</span><span><strong>Courriel</strong>{EMAIL}</span></a>
          </div>"""


def booking_html(lang):
    L = LANG[lang]
    tag = "★ Fastest — pick a time" if lang == "en" else "★ Le plus rapide — choisissez une heure"
    div = "or send us the details" if lang == "en" else "ou envoyez-nous les détails"
    url = (L["cal"] + "?hide_event_type_details=1&amp;hide_gdpr_banner=1"
           "&amp;background_color=fbf8f3&amp;text_color=17130f&amp;primary_color=a67c3d")
    return f"""        <div class="contact__booking reveal">
          <div class="booking__primary">
            <span class="booking__tag">{tag}</span>
            <div class="calendly-inline-widget" data-url="{url}" style="min-width:300px;height:640px;"></div>
          </div>
          <div class="booking__divider"><span>{div}</span></div>
{form_html(lang)}
        </div>"""


# ---------------------------------------------------------------- FAQ content

FAQ = {
    "en": [
        ("Is the in-home consultation really free?",
         "<p>Yes — completely free, with no obligation to buy. We come to you, bring physical samples, "
         "measure every window and give you a written quote. If you decide it isn't for you, that's "
         "genuinely fine; there's no fee and no pressure.</p>"),
        ("How soon can I book a visit?",
         "<p>Right away. Pick any open slot on our calendar and it's confirmed instantly — most people "
         "book a visit within the same week. If nothing suits you, call or WhatsApp us at "
         f"{TEL_PRETTY} and we'll find a time that works.</p>"),
        ("What actually happens during the visit?",
         "<p>It takes about 45 minutes. We look at each window, ask how you use the room, and show you "
         "fabric and material samples in daylight — colour looks very different on a screen. Then we "
         "measure precisely and quote you on the spot, so you leave knowing the real price.</p>"),
        ("Do you have a showroom I can visit?",
         "<p>No — and that's deliberate. We're a mobile company: instead of asking you to drive to a "
         "showroom and judge fabric under store lighting, we bring the showroom to your home, where "
         "you'll actually see the material against your own walls and light. It also means we don't "
         "carry retail overhead, which is a large part of why our prices are lower than a storefront's.</p>"),
        ("How long until my blinds are installed?",
         "<p>Everything is made to measure, so there's a production window — typically around 10 days "
         "from the moment your order is confirmed. Large or specialty orders can take a little longer; "
         "we'll always give you a realistic date at the consultation rather than an optimistic one.</p>"),
        ("Is installation included?",
         "<p>Yes. Professional installation is included free with every order, across our whole service "
         "area. Our installer mounts everything, checks the operation of each blind and takes the "
         "packaging away with them.</p>"),
        ("Which areas do you serve?",
         "<p>The Greater Montreal area — the island of Montréal, Laval, the South Shore, and the West "
         "Island. If you're just outside and not sure, ask us; we travel further for larger projects.</p>"),
        ("Can everything be motorized?",
         "<p>Yes — every product we make can be motorized, including curtains. Motors can be "
         "rechargeable-battery or hardwired, and can be controlled by remote, by app, or through Alexa "
         "and Google Home. It's also the safest choice for homes with children or pets, since it "
         "removes hanging cords entirely.</p>"),
        ("I need a room to be completely dark. What do you recommend?",
         "<p>A regular blackout blind still leaks light around the edges. For true darkness — nurseries, "
         "shift workers, home cinema — ask about our <strong>Blockout Blind</strong>: it's framed and "
         "edge-sealed so no light escapes at the sides. Honeycomb blackout with side channels is a good "
         "alternative.</p>"),
        ("Do you do balconies, patios and outdoor spaces?",
         "<p>Yes — our Heavy-Duty Blinds are built for exterior use: wind, sun and Montreal weather. "
         "They're popular for balconies, terraces and covered patios, and they can be motorized too.</p>"),
        ("What about very large, arched or oddly shaped windows?",
         "<p>Everything is custom-made, so unusual shapes and oversized windows are normal work for us. "
         "Bring them up when you book and we'll come prepared.</p>"),
        ("Do you serve customers in French and English?",
         "<p>Absolutely — we work in both languages, on the phone, in person and in writing. "
         "<a href=\"fr/\">Cette page existe aussi en français.</a></p>"),
    ],
    "fr": [
        ("La consultation à domicile est-elle vraiment gratuite ?",
         "<p>Oui — entièrement gratuite, sans aucune obligation d'achat. Nous nous déplaçons chez vous, "
         "apportons des échantillons, mesurons chaque fenêtre et vous remettons une soumission écrite. "
         "Si vous décidez que ce n'est pas pour vous, aucun problème : aucuns frais, aucune pression.</p>"),
        ("Dans combien de temps puis-je réserver une visite ?",
         "<p>Immédiatement. Choisissez une plage libre dans notre calendrier et c'est confirmé sur-le-champ "
         "— la plupart des clients obtiennent une visite dans la même semaine. Si rien ne vous convient, "
         f"appelez-nous ou écrivez-nous sur WhatsApp au {TEL_PRETTY} et nous trouverons un moment.</p>"),
        ("Que se passe-t-il concrètement pendant la visite ?",
         "<p>Comptez environ 45 minutes. Nous regardons chaque fenêtre, vous demandons comment vous "
         "utilisez la pièce, et vous montrons les échantillons de tissu à la lumière du jour — les "
         "couleurs sont très différentes à l'écran. Ensuite nous prenons les mesures exactes et vous "
         "remettons la soumission sur place : vous connaissez le vrai prix avant notre départ.</p>"),
        ("Avez-vous une salle de montre où je peux aller ?",
         "<p>Non — et c'est un choix. Nous sommes une entreprise mobile : plutôt que de vous faire "
         "déplacer pour juger un tissu sous un éclairage de magasin, nous apportons la salle de montre "
         "chez vous, où vous voyez la matière contre vos propres murs et votre propre lumière. Cela nous "
         "évite aussi les frais d'un local commercial — une bonne partie de la raison pour laquelle nos "
         "prix sont plus bas.</p>"),
        ("Combien de temps avant l'installation ?",
         "<p>Tout est fabriqué sur mesure, il y a donc un délai de production — généralement autour de "
         "10 jours à partir de la confirmation de votre commande. Les grandes commandes ou les produits "
         "spécialisés peuvent demander un peu plus de temps ; nous vous donnons toujours une date "
         "réaliste lors de la consultation.</p>"),
        ("L'installation est-elle incluse ?",
         "<p>Oui. L'installation professionnelle est incluse gratuitement avec chaque commande, partout "
         "dans notre zone de service. Notre installateur pose le tout, vérifie le fonctionnement de "
         "chaque store et repart avec les emballages.</p>"),
        ("Quels secteurs desservez-vous ?",
         "<p>Le Grand Montréal — l'île de Montréal, Laval, la Rive-Sud et l'Ouest-de-l'Île. Si vous êtes "
         "juste à l'extérieur, demandez-nous : nous nous déplaçons plus loin pour les projets d'envergure.</p>"),
        ("Est-ce que tout peut être motorisé ?",
         "<p>Oui — tous nos produits peuvent être motorisés, rideaux compris. Les moteurs peuvent être à "
         "pile rechargeable ou câblés, et se commandent par télécommande, par application, ou via Alexa "
         "et Google Home. C'est aussi le choix le plus sécuritaire avec de jeunes enfants ou des animaux, "
         "puisqu'il élimine complètement les cordons.</p>"),
        ("Je veux une pièce complètement noire. Que recommandez-vous ?",
         "<p>Un store occultant ordinaire laisse toujours passer la lumière sur les côtés. Pour une "
         "obscurité totale — chambre de bébé, travail de nuit, cinéma maison — demandez notre "
         "<strong>store Blockout</strong> : il est encadré et scellé sur les bords, donc aucune lumière "
         "ne s'échappe. Un store alvéolaire occultant avec glissières latérales est une bonne solution "
         "de rechange.</p>"),
        ("Faites-vous les balcons, terrasses et espaces extérieurs ?",
         "<p>Oui — nos stores robustes sont conçus pour l'extérieur : vent, soleil et météo montréalaise. "
         "Ils sont très populaires pour les balcons, terrasses et patios couverts, et peuvent aussi être "
         "motorisés.</p>"),
        ("Et les très grandes fenêtres, les cintrées ou les formes inhabituelles ?",
         "<p>Tout est fabriqué sur mesure : les formes inhabituelles et les grandes dimensions font "
         "partie de notre quotidien. Mentionnez-le au moment de réserver et nous arriverons préparés.</p>"),
        ("Servez-vous la clientèle en français et en anglais ?",
         "<p>Tout à fait — nous travaillons dans les deux langues, au téléphone, en personne et par "
         "écrit. <a href=\"../\">This page is also available in English.</a></p>"),
    ],
}


def strip_tags(s):
    out, depth = [], 0
    for ch in s:
        if ch == "<":
            depth += 1
        elif ch == ">":
            depth -= 1
        elif depth == 0:
            out.append(ch)
    return html.unescape("".join(out)).strip()


def faq_page(lang):
    items = FAQ[lang]
    details = "".join(
        f"<details><summary>{q}</summary>{a}</details>" for q, a in items)
    schema = {
        "@context": "https://schema.org", "@type": "FAQPage",
        "inLanguage": lang,
        "mainEntity": [
            {"@type": "Question", "name": strip_tags(q),
             "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
            for q, a in items],
    }
    if lang == "en":
        title = "FAQ — Custom Blinds & Curtains in Montreal | My Kurtains"
        desc = ("Answers about our free in-home consultation, pricing, installation time, motorization, "
                "blackout options and the areas we serve across Greater Montreal.")
        eyebrow, h1 = "Frequently asked questions", "Everything you're about to <em>ask us.</em>"
        lede = ("The questions we get most, answered plainly. If yours isn't here, call, WhatsApp or "
                "email us — a real person replies.")
        cta_h, cta_p, cta_b = ("Still have a question?",
                               "Book a free consultation and ask us in person — no obligation, no pressure.",
                               "Book a free consultation")
    else:
        title = "FAQ — Stores et rideaux sur mesure à Montréal | My Kurtains"
        desc = ("Réponses sur la consultation gratuite à domicile, les prix, les délais d'installation, "
                "la motorisation, l'occultation totale et nos secteurs desservis dans le Grand Montréal.")
        eyebrow, h1 = "Foire aux questions", "Tout ce que vous alliez <em>nous demander.</em>"
        lede = ("Les questions qu'on nous pose le plus, avec des réponses claires. Si la vôtre n'y est "
                "pas, appelez, écrivez sur WhatsApp ou envoyez un courriel — une vraie personne répond.")
        cta_h, cta_p, cta_b = ("Une autre question ?",
                               "Réservez une consultation gratuite et posez-la-nous en personne — sans obligation.",
                               "Réserver une consultation gratuite")

    home = "../index.html" if lang == "en" else "../../index-fr.html"
    body = f"""    <section class="section" style="padding-top:0">
      <div class="container" style="max-width:760px">
        <div class="post-body faq">{details}</div>
      </div>
    </section>

    <section class="post-cta">
      <div class="container post-cta__inner">
        <div><h2>{cta_h}</h2><p>{cta_p}</p></div>
        <a href="{home}#contact" class="btn btn--solid btn--lg" data-calendly>{cta_b}</a>
      </div>
    </section>
"""
    return render(lang, "faq", title, desc, eyebrow, h1, lede, body, schema=schema)


# ------------------------------------------------------------ contact content

def contact_page(lang):
    if lang == "en":
        title = "Contact Us — My Kurtains | Custom Blinds in Montreal"
        desc = ("Call, WhatsApp or email My Kurtains, or book a free in-home consultation online. "
                "Serving Montréal, Laval, the South Shore and the West Island.")
        eyebrow, h1 = "Contact", "Let's talk about your <em>windows.</em>"
        lede = ("Book a free in-home consultation, or just reach out — we answer quickly and we won't "
                "put you through a call centre.")
        h2 = "Reach us directly"
        hours_h = "Hours &amp; service area"
        hours = ("<p><strong>Monday to Saturday, by appointment.</strong> We're a mobile company — "
                 "we come to you, anywhere in the Greater Montreal area: the island of Montréal, Laval, "
                 "the South Shore and the West Island.</p>"
                 "<p>Evening and weekend appointments are available, which is usually when it's easiest "
                 "to see how your rooms really get light.</p>")
    else:
        title = "Nous joindre — My Kurtains | Stores sur mesure à Montréal"
        desc = ("Appelez, écrivez sur WhatsApp ou par courriel, ou réservez une consultation gratuite à "
                "domicile en ligne. Montréal, Laval, la Rive-Sud et l'Ouest-de-l'Île.")
        eyebrow, h1 = "Nous joindre", "Parlons de vos <em>fenêtres.</em>"
        lede = ("Réservez une consultation gratuite à domicile, ou écrivez-nous simplement — nous "
                "répondons vite, et jamais par centre d'appels.")
        h2 = "Nous joindre directement"
        hours_h = "Heures &amp; secteurs desservis"
        hours = ("<p><strong>Du lundi au samedi, sur rendez-vous.</strong> Nous sommes une entreprise "
                 "mobile — nous nous déplaçons chez vous, partout dans le Grand Montréal : l'île de "
                 "Montréal, Laval, la Rive-Sud et l'Ouest-de-l'Île.</p>"
                 "<p>Des rendez-vous en soirée et la fin de semaine sont possibles — c'est souvent le "
                 "meilleur moment pour voir comment la lumière entre vraiment chez vous.</p>")

    schema = {
        "@context": "https://schema.org", "@type": "ContactPage",
        "inLanguage": lang,
        "url": f"{SITE}/contact/" if lang == "en" else f"{SITE}/contact/fr/",
        "mainEntity": {
            "@type": "HomeAndConstructionBusiness",
            "@id": f"{SITE}/#business",
            "name": "My Kurtains",
            "telephone": "+1-438-402-0559",
            "email": EMAIL,
            "url": f"{SITE}/",
            "areaServed": [{"@type": "City", "name": n} for n in
                           ["Montréal", "Laval", "Longueuil", "Brossard", "Pointe-Claire"]],
        },
    }

    body = f"""    <section class="section contact" id="contact" style="padding-top:0">
      <div class="container contact__inner">
        <div class="contact__copy reveal">
          <h2 class="section__title" style="font-size:clamp(1.6rem,2.6vw,2.1rem)">{h2}</h2>
{methods_html(lang)}
          <div class="post-body" style="margin-top:2rem">
            <h3>{hours_h}</h3>
            {hours}
          </div>
        </div>
{booking_html(lang)}
      </div>
    </section>
"""
    return render(lang, "contact", title, desc, eyebrow, h1, lede, body, schema=schema)


# -------------------------------------------------------------- about content

def about_page(lang):
    if lang == "en":
        title = "About My Kurtains — Custom Blinds & Curtains, Montreal"
        desc = ("We're a Montreal mobile blinds company: we bring the samples to your home, measure, "
                "quote on the spot and install free. High style, low cost — here's how that works.")
        eyebrow, h1 = "About us", "We brought the showroom <em>to your living room.</em>"
        lede = ("My Kurtains is a Montreal custom window-covering company built around one idea: buying "
                "blinds should be simple, honest and affordable.")
        body_inner = f"""
        <h2>Why we started</h2>
        <p>Buying custom window coverings used to mean driving to a showroom, judging fabric under
        fluorescent lighting, waiting days for a quote, and then discovering that installation was an
        extra line on the invoice. It was slow, opaque and more expensive than it needed to be.</p>
        <p>We thought the whole thing could be turned inside out. So we did: we don't have a store.
        We come to you.</p>

        <h2>How it actually works</h2>
        <p>You pick a time on our calendar. We arrive with fabric and material samples and look at your
        windows with you — in your light, against your walls, in the room you actually live in. We
        measure every window precisely, talk through what each material would do for that room, and give
        you a written quote before we leave. Everything is then made to measure and
        <strong>installed free</strong> by our own installer.</p>
        <p>That's the whole process. No showroom trip, no waiting a week for a number, no surprise
        installation fee.</p>

        <div class="callout"><strong>Why we can charge less</strong><p>A retail showroom is expensive:
        rent, staff, stock sitting on shelves. We carry none of that. Being mobile is not just more
        convenient for you — it's a large part of why our prices come in below a storefront's for the
        same quality.</p></div>

        <h2>What we make</h2>
        <p>Roller blinds, curtains and drapes, Roman shades, day &amp; night (zebra) blinds, honeycomb
        (cellular) shades, our edge-sealed <strong>Blockout Blind</strong> for total darkness,
        heavy-duty blinds for balconies and terraces, and switchable smart film for glass that needs to
        turn private on demand.</p>
        <p><strong>Every single one of them can be motorized</strong> — by remote, by app, or through
        Alexa and Google Home. Motorization also removes hanging cords, which makes it the safe choice
        in homes with young children or pets.</p>

        <h2>The part we're proud of</h2>
        <p>We hold a 5.0 rating across roughly 80 Google reviews. Read a few and you'll notice they tend
        to mention the same things: we show up when we say we will, the quote is the price, and the
        install is clean. That's the business, really.</p>
        <p>We work in English and French, and we serve the island of Montréal, Laval, the South Shore
        and the West Island.</p>
"""
        cta_h, cta_p, cta_b = ("See it for yourself.",
                               "Free in-home consultation. Samples, measurements and an honest quote — no obligation.",
                               "Book a free consultation")
    else:
        title = "À propos de My Kurtains — Stores et rideaux sur mesure, Montréal"
        desc = ("Une entreprise mobile de stores à Montréal : nous apportons les échantillons chez vous, "
                "mesurons, soumissionnons sur place et installons gratuitement. Haut style, bas prix.")
        eyebrow, h1 = "À propos", "Nous avons apporté la salle de montre <em>dans votre salon.</em>"
        lede = ("My Kurtains est une entreprise montréalaise de couvre-fenêtres sur mesure bâtie autour "
                "d'une idée : acheter des stores devrait être simple, honnête et abordable.")
        body_inner = f"""
        <h2>Pourquoi nous avons commencé</h2>
        <p>Acheter des couvre-fenêtres sur mesure, c'était se déplacer en salle de montre, juger un
        tissu sous un néon, attendre des jours pour une soumission, puis découvrir que l'installation
        était une ligne de plus sur la facture. Lent, opaque, et plus cher que nécessaire.</p>
        <p>Nous étions convaincus qu'on pouvait renverser tout ça. Alors nous l'avons fait : nous
        n'avons pas de magasin. C'est nous qui venons à vous.</p>

        <h2>Comment ça se passe</h2>
        <p>Vous choisissez une plage horaire dans notre calendrier. Nous arrivons avec les échantillons
        de tissus et de matériaux, et nous regardons vos fenêtres avec vous — dans votre lumière, contre
        vos murs, dans la pièce où vous vivez réellement. Nous mesurons chaque fenêtre avec précision,
        nous expliquons ce que chaque matériau donnerait dans cette pièce, et nous vous remettons une
        soumission écrite avant de partir. Tout est ensuite fabriqué sur mesure et
        <strong>installé gratuitement</strong> par notre propre installateur.</p>
        <p>C'est tout le processus. Aucun déplacement, aucune attente d'une semaine pour un prix, aucun
        frais d'installation surprise.</p>

        <div class="callout"><strong>Pourquoi nos prix sont plus bas</strong><p>Une salle de montre
        coûte cher : loyer, personnel, inventaire immobilisé. Nous n'avons rien de tout ça. Être mobile
        n'est pas seulement plus pratique pour vous — c'est une grande partie de la raison pour laquelle
        nos prix sont inférieurs à ceux d'un magasin, à qualité égale.</p></div>

        <h2>Ce que nous fabriquons</h2>
        <p>Stores enrouleurs, rideaux et draperies, stores bateau, stores jour &amp; nuit (zébrés),
        stores alvéolaires, notre <strong>store Blockout</strong> scellé sur les bords pour une
        obscurité totale, stores robustes pour balcons et terrasses, et film intelligent commutable
        pour les vitrages qui doivent devenir opaques sur demande.</p>
        <p><strong>Chacun d'entre eux peut être motorisé</strong> — par télécommande, par application,
        ou via Alexa et Google Home. La motorisation élimine aussi les cordons pendants, ce qui en fait
        le choix sécuritaire avec de jeunes enfants ou des animaux.</p>

        <h2>Ce dont nous sommes fiers</h2>
        <p>Nous maintenons une note de 5,0 sur environ 80 avis Google. Lisez-en quelques-uns et vous
        remarquerez qu'ils reviennent sur les mêmes points : nous arrivons quand nous l'avons dit, la
        soumission est le prix final, et l'installation est propre. C'est ça, notre métier.</p>
        <p>Nous servons notre clientèle en français et en anglais, sur l'île de Montréal, à Laval, sur
        la Rive-Sud et dans l'Ouest-de-l'Île.</p>
"""
        cta_h, cta_p, cta_b = ("Voyez par vous-même.",
                               "Consultation gratuite à domicile. Échantillons, mesures et soumission honnête — sans obligation.",
                               "Réserver une consultation gratuite")

    schema = {
        "@context": "https://schema.org", "@type": "AboutPage",
        "inLanguage": lang,
        "url": f"{SITE}/about/" if lang == "en" else f"{SITE}/about/fr/",
        "mainEntity": {"@id": f"{SITE}/#business"},
    }
    home = "../index.html" if lang == "en" else "../../index-fr.html"
    body = f"""    <section class="section" style="padding-top:0">
      <div class="container" style="max-width:760px">
        <div class="post-body">{body_inner}      </div>
      </div>
    </section>

    <section class="post-cta">
      <div class="container post-cta__inner">
        <div><h2>{cta_h}</h2><p>{cta_p}</p></div>
        <a href="{home}#contact" class="btn btn--solid btn--lg" data-calendly>{cta_b}</a>
      </div>
    </section>
"""
    return render(lang, "about", title, desc, eyebrow, h1, lede, body, schema=schema)


# ------------------------------------------------------------ privacy content

def privacy_page(lang):
    if lang == "en":
        title = "Privacy Policy — My Kurtains"
        desc = ("How My Kurtains collects, uses and protects your personal information, in line with "
                "Quebec's Law 25 and Canada's PIPEDA.")
        eyebrow, h1 = "Privacy", "Your information, <em>handled properly.</em>"
        lede = ("We collect as little as we can, we tell you what we do with it, and you can ask us to "
                "delete it at any time.")
        inner = f"""
        <p><em>Last updated: {UPDATED}</em></p>

        <h2>Who we are</h2>
        <p>My Kurtains is a custom window-covering business operating in the Greater Montreal area,
        Quebec, Canada. For any question about this policy or your personal information, contact us at
        <a href="mailto:{EMAIL}">{EMAIL}</a> or {TEL_PRETTY}.</p>

        <h2>What we collect</h2>
        <p>Only what we need to answer you and do the work:</p>
        <ul>
          <li><strong>When you fill in our contact form:</strong> your name, your phone number or email
          address, the product you're interested in, and anything you write in the message field.</li>
          <li><strong>When you book a consultation:</strong> the information you enter into our booking
          tool (Calendly) — typically name, email, phone and appointment time.</li>
          <li><strong>When you become a customer:</strong> the address where the installation takes
          place, your window measurements, and your order details.</li>
          <li><strong>When you browse the site:</strong> if — and only if — you accept cookies, standard
          analytics and advertising data such as pages viewed, approximate location (city level), device
          and browser type, and how you arrived at the site.</li>
        </ul>
        <p>We do not ask for, and do not want, sensitive information such as government ID numbers. We
        do not store credit card numbers on this website.</p>

        <h2>Why we use it</h2>
        <ul>
          <li>To reply to your enquiry and arrange your consultation.</li>
          <li>To measure, manufacture, deliver and install your order.</li>
          <li>To provide after-sales service and honour any warranty.</li>
          <li>With your consent, to measure how our website and advertising perform, and to show you
          relevant ads.</li>
        </ul>

        <h2>Cookies and tracking</h2>
        <p>Our site uses Google Analytics 4 and the Meta (Facebook) Pixel, loaded through Google Tag
        Manager, to understand how people find and use the site and to measure our advertising.</p>
        <p><strong>These are switched off until you accept them.</strong> When you first arrive, nothing
        analytics- or advertising-related runs; Google Consent Mode is set to "denied" and the Meta Pixel
        is blocked outright. Only if you press <em>Accept</em> do they load. You can change your mind at
        any time using the <em>Cookies</em> link in the footer, or by clearing your browser storage for
        this site. Essential cookies needed to make the site function are always on.</p>

        <h2>Who else sees your information</h2>
        <p>We do not sell your personal information. We share it only with the service providers who
        make the site and our business run:</p>
        <ul>
          <li><strong>Web3Forms</strong> — delivers our contact-form submissions to our email.</li>
          <li><strong>Calendly</strong> — handles consultation bookings.</li>
          <li><strong>Google</strong> (Analytics, Tag Manager, Ads) — website measurement and
          advertising, only with your consent.</li>
          <li><strong>Meta</strong> (Facebook, Instagram) — advertising measurement, only with your
          consent.</li>
          <li><strong>Vercel</strong> — hosts this website.</li>
          <li>Our manufacturing and installation partners, who receive only the measurements and
          delivery details needed to complete your order.</li>
        </ul>
        <p>We may also disclose information where the law requires it.</p>

        <h2>Where your information is stored</h2>
        <p>Some of these providers store and process data outside Quebec, including in the United
        States and the European Union. That means your information may be subject to the laws of those
        jurisdictions. We only use established providers that offer contractual protections for personal
        information. If you would rather not have your information handled this way, contact us by phone
        instead of using the website forms.</p>

        <h2>How long we keep it</h2>
        <p>Enquiries that don't become orders are kept for up to two years, in case you come back to us.
        Customer records are kept as long as needed for warranty and for the periods Quebec law requires
        for business records. Analytics data is retained according to the default retention period of
        the tool, up to 14 months. You can ask us to delete your information sooner.</p>

        <h2>Your rights</h2>
        <p>Under Quebec's Law 25 and Canada's PIPEDA, you have the right to:</p>
        <ul>
          <li>know what personal information we hold about you, and get a copy of it;</li>
          <li>have inaccurate information corrected;</li>
          <li>withdraw your consent to marketing or tracking at any time;</li>
          <li>ask us to delete your personal information, subject to what we must keep by law;</li>
          <li>make a complaint to the <em>Commission d'accès à l'information du Québec</em> if you
          believe we've handled your information improperly.</li>
        </ul>
        <p>To exercise any of these, email <a href="mailto:{EMAIL}">{EMAIL}</a>. We respond within 30
        days, as the law requires.</p>

        <h2>Person in charge of privacy</h2>
        <p>The person responsible for the protection of personal information at My Kurtains can be
        reached at <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

        <h2>Security</h2>
        <p>This site is served entirely over HTTPS. We limit access to personal information to the people
        who need it to do their job, and we ask the same of our service providers. No system is perfect,
        but we take this seriously.</p>

        <h2>Children</h2>
        <p>Our services are for adults. We don't knowingly collect personal information from children.</p>

        <h2>Changes to this policy</h2>
        <p>If we change how we handle personal information, we'll update this page and change the date
        at the top.</p>
"""
    else:
        title = "Politique de confidentialité — My Kurtains"
        desc = ("Comment My Kurtains recueille, utilise et protège vos renseignements personnels, "
                "conformément à la Loi 25 du Québec et à la LPRPDE.")
        eyebrow, h1 = "Confidentialité", "Vos renseignements, <em>traités correctement.</em>"
        lede = ("Nous recueillons le strict minimum, nous vous disons ce que nous en faisons, et vous "
                "pouvez demander leur suppression en tout temps.")
        inner = f"""
        <p><em>Dernière mise à jour : {UPDATED}</em></p>

        <h2>Qui nous sommes</h2>
        <p>My Kurtains est une entreprise de couvre-fenêtres sur mesure qui exerce ses activités dans le
        Grand Montréal, au Québec (Canada). Pour toute question sur cette politique ou sur vos
        renseignements personnels, écrivez-nous à <a href="mailto:{EMAIL}">{EMAIL}</a> ou appelez au
        {TEL_PRETTY}.</p>

        <h2>Ce que nous recueillons</h2>
        <p>Uniquement ce dont nous avons besoin pour vous répondre et faire le travail :</p>
        <ul>
          <li><strong>Quand vous remplissez notre formulaire :</strong> votre nom, votre numéro de
          téléphone ou courriel, le produit qui vous intéresse et le contenu de votre message.</li>
          <li><strong>Quand vous réservez une consultation :</strong> les renseignements saisis dans
          notre outil de réservation (Calendly) — généralement nom, courriel, téléphone et heure du
          rendez-vous.</li>
          <li><strong>Quand vous devenez client :</strong> l'adresse où a lieu l'installation, les
          mesures de vos fenêtres et les détails de votre commande.</li>
          <li><strong>Quand vous naviguez sur le site :</strong> si — et seulement si — vous acceptez les
          témoins, des données standards d'analyse et de publicité : pages consultées, localisation
          approximative (ville), type d'appareil et de navigateur, et provenance de votre visite.</li>
        </ul>
        <p>Nous ne demandons pas de renseignements sensibles comme des numéros de pièces d'identité
        gouvernementales. Aucun numéro de carte de crédit n'est conservé sur ce site.</p>

        <h2>Pourquoi nous les utilisons</h2>
        <ul>
          <li>Pour répondre à votre demande et organiser votre consultation.</li>
          <li>Pour mesurer, fabriquer, livrer et installer votre commande.</li>
          <li>Pour assurer le service après-vente et honorer la garantie.</li>
          <li>Avec votre consentement, pour mesurer la performance de notre site et de notre publicité,
          et vous présenter des annonces pertinentes.</li>
        </ul>

        <h2>Témoins et suivi</h2>
        <p>Notre site utilise Google Analytics 4 et le pixel Meta (Facebook), chargés via Google Tag
        Manager, pour comprendre comment les gens trouvent et utilisent le site et pour mesurer notre
        publicité.</p>
        <p><strong>Tout cela est désactivé tant que vous n'avez pas accepté.</strong> À votre arrivée,
        rien lié à l'analyse ou à la publicité ne s'exécute : le mode Consentement de Google est réglé
        à « refusé » et le pixel Meta est bloqué complètement. Ce n'est qu'en cliquant sur
        <em>Accepter</em> qu'ils se chargent. Vous pouvez changer d'avis en tout temps par le lien
        <em>Témoins</em> au bas des pages, ou en effaçant le stockage de votre navigateur pour ce site.
        Les témoins essentiels au fonctionnement du site sont toujours actifs.</p>

        <h2>Qui d'autre voit vos renseignements</h2>
        <p>Nous ne vendons pas vos renseignements personnels. Nous les partageons uniquement avec les
        fournisseurs qui font fonctionner le site et notre entreprise :</p>
        <ul>
          <li><strong>Web3Forms</strong> — achemine les envois du formulaire vers notre courriel.</li>
          <li><strong>Calendly</strong> — gère les réservations de consultation.</li>
          <li><strong>Google</strong> (Analytics, Tag Manager, Ads) — mesure du site et publicité,
          uniquement avec votre consentement.</li>
          <li><strong>Meta</strong> (Facebook, Instagram) — mesure publicitaire, uniquement avec votre
          consentement.</li>
          <li><strong>Vercel</strong> — héberge ce site.</li>
          <li>Nos partenaires de fabrication et d'installation, qui ne reçoivent que les mesures et les
          détails de livraison nécessaires à votre commande.</li>
        </ul>
        <p>Nous pouvons aussi divulguer des renseignements lorsque la loi l'exige.</p>

        <h2>Où vos renseignements sont conservés</h2>
        <p>Certains de ces fournisseurs conservent et traitent des données à l'extérieur du Québec,
        notamment aux États-Unis et dans l'Union européenne. Vos renseignements peuvent donc être soumis
        aux lois de ces territoires. Nous faisons affaire uniquement avec des fournisseurs établis
        offrant des protections contractuelles pour les renseignements personnels. Si vous préférez
        éviter ce traitement, communiquez avec nous par téléphone plutôt que par les formulaires du
        site.</p>

        <h2>Durée de conservation</h2>
        <p>Les demandes qui ne mènent pas à une commande sont conservées jusqu'à deux ans, au cas où
        vous reveniez vers nous. Les dossiers clients sont conservés le temps nécessaire à la garantie
        et selon les délais exigés par la loi québécoise pour les documents d'entreprise. Les données
        d'analyse sont conservées selon la période par défaut de l'outil, jusqu'à 14 mois. Vous pouvez
        demander une suppression plus rapide.</p>

        <h2>Vos droits</h2>
        <p>En vertu de la Loi 25 du Québec et de la LPRPDE, vous avez le droit :</p>
        <ul>
          <li>de savoir quels renseignements personnels nous détenons à votre sujet et d'en obtenir une
          copie ;</li>
          <li>de faire corriger des renseignements inexacts ;</li>
          <li>de retirer votre consentement au marketing ou au suivi en tout temps ;</li>
          <li>de demander la suppression de vos renseignements, sous réserve de ce que la loi nous
          oblige à conserver ;</li>
          <li>de porter plainte auprès de la <em>Commission d'accès à l'information du Québec</em> si
          vous estimez que nous avons mal traité vos renseignements.</li>
        </ul>
        <p>Pour exercer l'un de ces droits, écrivez à <a href="mailto:{EMAIL}">{EMAIL}</a>. Nous
        répondons dans les 30 jours, comme la loi l'exige.</p>

        <h2>Responsable de la protection des renseignements personnels</h2>
        <p>La personne responsable de la protection des renseignements personnels chez My Kurtains peut
        être jointe à <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

        <h2>Sécurité</h2>
        <p>Ce site est entièrement servi en HTTPS. Nous limitons l'accès aux renseignements personnels
        aux personnes qui en ont besoin pour leur travail, et nous exigeons la même chose de nos
        fournisseurs. Aucun système n'est parfait, mais nous prenons cela au sérieux.</p>

        <h2>Enfants</h2>
        <p>Nos services s'adressent aux adultes. Nous ne recueillons pas sciemment de renseignements
        personnels auprès d'enfants.</p>

        <h2>Modifications</h2>
        <p>Si nous changeons notre façon de traiter les renseignements personnels, nous mettrons cette
        page à jour et modifierons la date en haut.</p>
"""
    body = f"""    <section class="section" style="padding-top:0">
      <div class="container" style="max-width:720px">
        <div class="post-body">{inner}      </div>
      </div>
    </section>
"""
    return render(lang, "privacy", title, desc, eyebrow, h1, lede, body)


# ---------------------------------------------------------- thank-you content

def thanks_page(lang):
    if lang == "en":
        title = "Thank you — My Kurtains"
        desc = "Thanks for getting in touch with My Kurtains. Here's what happens next."
        eyebrow, h1 = "Thank you", "That's booked. <em>Talk soon.</em>"
        lede = "We've got your details. Here's exactly what happens from here."
        inner = f"""
        <h2>What happens next</h2>
        <ol>
          <li><strong>You'll get a confirmation.</strong> Check your email — if you booked a
          consultation, the invitation includes the time and a link to reschedule if you need to.</li>
          <li><strong>We arrive with samples.</strong> At the appointment we look at each window in your
          own light, measure precisely, and talk through what suits the room.</li>
          <li><strong>You get your quote on the spot.</strong> Written, complete, installation included.
          No waiting, no surprise fees.</li>
        </ol>
        <p>If anything changes, or you thought of a question in the meantime, just call or WhatsApp us
        at <a href="tel:{TEL}">{TEL_PRETTY}</a> — we'd rather hear from you than leave you wondering.</p>

        <h2>While you wait</h2>
        <p>Our guides walk through every blind we make — how each one works, and the honest pros and
        cons. They're the fastest way to arrive at your consultation knowing what you want.</p>
"""
        b1, b2 = "Browse the guides", "Back to home"
        g, h = "../blog/index.html", "../index.html"
    else:
        title = "Merci — My Kurtains"
        desc = "Merci d'avoir communiqué avec My Kurtains. Voici la suite des choses."
        eyebrow, h1 = "Merci", "C'est réservé. <em>À très bientôt.</em>"
        lede = "Nous avons vos coordonnées. Voici exactement ce qui se passe maintenant."
        inner = f"""
        <h2>La suite des choses</h2>
        <ol>
          <li><strong>Vous recevrez une confirmation.</strong> Vérifiez vos courriels — si vous avez
          réservé une consultation, l'invitation contient l'heure et un lien pour la déplacer au
          besoin.</li>
          <li><strong>Nous arrivons avec les échantillons.</strong> Au rendez-vous, nous regardons
          chaque fenêtre dans votre lumière, nous mesurons avec précision et nous discutons de ce qui
          convient à la pièce.</li>
          <li><strong>Vous obtenez votre soumission sur place.</strong> Écrite, complète, installation
          incluse. Aucune attente, aucun frais surprise.</li>
        </ol>
        <p>Si quelque chose change, ou si une question vous vient entre-temps, appelez-nous ou écrivez
        sur WhatsApp au <a href="tel:{TEL}">{TEL_PRETTY}</a> — nous préférons vous parler plutôt que de
        vous laisser dans le doute.</p>

        <h2>En attendant</h2>
        <p>Nos guides passent en revue chaque store que nous fabriquons — comment il fonctionne, avec
        ses avantages et ses inconvénients réels. C'est la façon la plus rapide d'arriver à votre
        consultation en sachant ce que vous voulez.</p>
"""
        b1, b2 = "Voir les guides", "Retour à l'accueil"
        g, h = "../../blog/fr/index.html", "../../index-fr.html"

    body = f"""    <section class="section" style="padding-top:0">
      <div class="container" style="max-width:680px">
        <div class="post-body">{inner}      </div>
        <div class="nf__actions" style="display:flex;gap:.8rem;flex-wrap:wrap;margin-top:2rem">
          <a href="{g}" class="btn btn--solid btn--lg">{b1}</a>
          <a href="{h}" class="btn btn--ghost btn--lg">{b2}</a>
        </div>
      </div>
    </section>
"""
    return render(lang, "thank-you", title, desc, eyebrow, h1, lede, body, noindex=True)


# ------------------------------------------------------------------- assemble

BUILDERS = {
    "contact": contact_page,
    "faq": faq_page,
    "about": about_page,
    "privacy": privacy_page,
    "thank-you": thanks_page,
}

if __name__ == "__main__":
    n = 0
    for slug, fn in BUILDERS.items():
        for lang in ("en", "fr"):
            d = slug if lang == "en" else os.path.join(slug, "fr")
            os.makedirs(d, exist_ok=True)
            with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
                f.write(fn(lang))
            n += 1
    print(f"built {n} pages")
