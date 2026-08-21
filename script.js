/* ============================================================
   My Kurtains — interactions
   ============================================================ */
(function () {
  "use strict";

  // Page language ("fr" on index-fr.html, else "en"). Drives the Calendly
  // event and the form's user-facing strings.
  var FR = (document.documentElement.lang || "en").toLowerCase().slice(0, 2) === "fr";

  // ---- analytics helper (no-op if GA hasn't loaded / is blocked)
  // Pushes to the GTM dataLayer. GTM's GA4 tag forwards these to GA4, and Meta's
  // connection mirrors GA4 events to the Pixel/CAPI — so one push reaches both.
  var gaEvent = function (name, params) {
    try {
      window.dataLayer = window.dataLayer || [];
      var p = Object.assign({ event: name }, params || {});
      window.dataLayer.push(p);
    } catch (e) {}
  };

  const nav = document.getElementById("nav");
  const navToggle = document.getElementById("navToggle");
  const navMobile = document.getElementById("navMobile");

  /* ---- sticky nav background on scroll ---- */
  const onScroll = () => {
    if (window.scrollY > 40) nav.classList.add("scrolled");
    else nav.classList.remove("scrolled");
  };
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  /* ---- mobile menu ---- */
  const closeMenu = () => {
    navToggle.classList.remove("open");
    navMobile.classList.remove("open");
    navToggle.setAttribute("aria-expanded", "false");
  };
  navToggle.addEventListener("click", () => {
    const open = navToggle.classList.toggle("open");
    navMobile.classList.toggle("open", open);
    navToggle.setAttribute("aria-expanded", String(open));
  });
  navMobile.querySelectorAll("a").forEach((a) => a.addEventListener("click", closeMenu));

  /* ---- scroll reveal ---- */
  const revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) {
            e.target.classList.add("in");
            io.unobserve(e.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -8% 0px" }
    );
    revealEls.forEach((el) => io.observe(el));
  } else {
    revealEls.forEach((el) => el.classList.add("in"));
  }

  /* ---- Calendly popup on primary CTAs ---- */
  var CALENDLY_URL =
    "https://calendly.com/mykurtains/" +
    (FR ? "consultation" : "mykurtains-consultation") +
    "?hide_gdpr_banner=1&background_color=fbf8f3&text_color=17130f&primary_color=a67c3d";
  document.querySelectorAll("[data-calendly]").forEach(function (el) {
    el.addEventListener("click", function (e) {
      // If Calendly's widget is loaded, open the popup; otherwise let the
      // href="#contact" fallback scroll to the inline scheduler.
      gaEvent("book_consultation_click", { method: "calendly_popup", lang: FR ? "fr" : "en", location: (el.closest("header") ? "nav" : el.closest(".hero") ? "hero" : el.closest(".post-cta") ? "post_cta" : el.closest(".aside-card") ? "sidebar" : "other") });
      if (window.Calendly && typeof window.Calendly.initPopupWidget === "function") {
        e.preventDefault();
        window.Calendly.initPopupWidget({ url: CALENDLY_URL });
      }
    });
  });


  /* ---- Calendly: fire the SAME key event the old site used when a booking is
     actually completed (not just the button click), so reports stay continuous ---- */
  window.addEventListener("message", function (e) {
    try {
      if (e.origin && e.origin.indexOf("calendly.com") === -1) return;
      var ev = e.data && e.data.event;
      if (ev === "calendly.event_scheduled") {
        gaEvent("Booked_Calendly_Meeting", { lang: FR ? "fr" : "en", source: "website" });
        gaEvent("generate_lead", { method: "calendly_booking", lang: FR ? "fr" : "en" });
      }
    } catch (err) {}
  });

  /* ---- reviews carousel ---- */
  var track = document.getElementById("reviewsTrack");
  var revPrev = document.getElementById("revPrev");
  var revNext = document.getElementById("revNext");
  if (track && revPrev && revNext) {
    var page = function () { return Math.max(280, Math.round(track.clientWidth * 0.85)); };

    var updateArrows = function () {
      var maxScroll = track.scrollWidth - track.clientWidth;
      revPrev.disabled = track.scrollLeft <= 8;
      revNext.disabled = track.scrollLeft >= maxScroll - 8;
    };

    revPrev.addEventListener("click", function () { track.scrollBy({ left: -page(), behavior: "smooth" }); });
    revNext.addEventListener("click", function () { track.scrollBy({ left: page(), behavior: "smooth" }); });
    track.addEventListener("scroll", updateArrows, { passive: true });
    window.addEventListener("resize", updateArrows);
    track.scrollLeft = 0; // always start at the first review
    updateArrows();

    // drag-to-scroll (mouse / trackpad-press only; touch uses native scroll)
    var down = false, startX = 0, startLeft = 0, moved = 0;
    track.addEventListener("pointerdown", function (e) {
      if (e.pointerType === "touch") return;
      down = true; moved = 0; startX = e.clientX; startLeft = track.scrollLeft;
      track.classList.add("dragging");
    });
    track.addEventListener("pointermove", function (e) {
      if (!down) return;
      var dx = e.clientX - startX;
      moved = Math.max(moved, Math.abs(dx));
      track.scrollLeft = startLeft - dx;
    });
    var endDrag = function () {
      if (!down) return;
      down = false; track.classList.remove("dragging"); updateArrows();
    };
    track.addEventListener("pointerup", endDrag);
    track.addEventListener("pointercancel", endDrag);
    track.addEventListener("pointerleave", endDrag);
    // suppress accidental link/click after a real drag
    track.addEventListener("click", function (e) { if (moved > 6) { e.preventDefault(); } }, true);
  }

  /* ---- current year ---- */
  const yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  /* ---- contact form: emails hello@mykurtains.com via Web3Forms ---- */
  // Access key is tied to the destination inbox (safe to expose client-side).
  var WEB3FORMS_KEY = "c2581362-ef6a-4407-8387-f4eb78ae82cc";
  const form = document.getElementById("contactForm");
  const note = document.getElementById("formNote");
  if (form) {
    const submitBtn = form.querySelector('button[type="submit"]');
    const t = {
      missing: FR ? "Ajoutez votre nom et une façon de vous joindre, s’il vous plaît." : "Please add your name and a way to reach you.",
      sending: FR ? "Envoi en cours…" : "Sending…",
      ok: FR ? "Merci ! Votre demande est bien reçue — on vous répond d’ici un jour ouvrable." : "Thanks! We’ve got your request — we’ll be in touch within one business day.",
      okWa: FR ? "Vous préférez tout de suite ? Écrivez-nous sur WhatsApp." : "Prefer right now? Message us on WhatsApp.",
      fail: FR ? "Oups — l’envoi n’a pas fonctionné. Ouverture de WhatsApp pour ne pas perdre votre demande…" : "Hmm — that didn’t send. Opening WhatsApp so your request isn’t lost…",
      subject: FR ? "Nouvelle demande de consultation — mykurtains.com" : "New consultation request — mykurtains.com",
    };
    const waLink = (name, contact, interest, message) => {
      const head = FR ? "Nouvelle demande de consultation" : "New consultation request";
      const l = FR ? ["Nom", "Coordonnées", "Intéressé(e) par", "Notes"] : ["Name", "Contact", "Interested in", "Notes"];
      const body = `${head}:%0A${l[0]}: ${encodeURIComponent(name)}%0A${l[1]}: ${encodeURIComponent(contact)}%0A${l[2]}: ${encodeURIComponent(interest)}%0A${l[3]}: ${encodeURIComponent(message || "—")}`;
      return `https://wa.me/14384020559?text=${body}`;
    };

    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      const name = form.name.value.trim();
      const contact = form.phone.value.trim();
      const interest = form.interest.value;
      const message = form.message.value.trim();
      if (!name || !contact) {
        note.textContent = t.missing; note.className = "contact__note err"; return;
      }
      // honeypot: bots tick hidden fields; humans don't. (Use .checked — a
      // checkbox's .value is always "on", even when unchecked.)
      if (form.botcheck && form.botcheck.checked) return;

      note.textContent = t.sending; note.className = "contact__note";
      if (submitBtn) submitBtn.disabled = true;

      const payload = {
        access_key: WEB3FORMS_KEY,
        subject: t.subject,
        from_name: "My Kurtains website",
        name: name,
        contact: contact,
        interested_in: interest,
        message: message || "—",
        language: FR ? "fr" : "en",
        page: location.href,
      };

      try {
        const res = await fetch("https://api.web3forms.com/submit", {
          method: "POST",
          headers: { "Content-Type": "application/json", Accept: "application/json" },
          body: JSON.stringify(payload),
        });
        const data = await res.json().catch(() => ({}));
        if (!res.ok || !data.success) throw new Error(data.message || "send failed");

        note.innerHTML = t.ok + ' <a href="' + waLink(name, contact, interest, message) + '" target="_blank" rel="noopener">' + t.okWa + "</a>";
        note.className = "contact__note ok";
        form.reset();
        gaEvent("generate_lead", { method: "contact_form", interest: interest, lang: FR ? "fr" : "en" });
      } catch (err) {
        // Never lose a lead: fall back to the WhatsApp handoff.
        note.textContent = t.fail; note.className = "contact__note err";
        gaEvent("form_send_failed", { interest: interest, lang: FR ? "fr" : "en" });
        setTimeout(() => { window.open(waLink(name, contact, interest, message), "_blank", "noopener"); }, 700);
      } finally {
        if (submitBtn) submitBtn.disabled = false;
      }
    });
  }


  /* ---- Cookie consent (Québec Law 25) — minimal. Gates GA4 / Meta / Ads. ---- */
  (function () {
    var KEY = "mk_consent";
    var T = FR
      ? { body: "Nous utilisons des témoins pour mesurer l’audience et nos publicités.", accept: "Accepter", decline: "Refuser", link: "Témoins" }
      : { body: "We use cookies for analytics and advertising.", accept: "Accept", decline: "Decline", link: "Cookies" };
    var apply = function (granted) {
      var v = granted ? "granted" : "denied";
      try { localStorage.setItem(KEY, v); } catch (e) {}
      window.__mkConsent = v;
      if (typeof window.gtag === "function") window.gtag("consent", "update", { ad_storage: v, ad_user_data: v, ad_personalization: v, analytics_storage: v });
      // Meta Pixel: it was network-sunk while denied. On grant, a one-time reload lets GTM
      // initialise the real pixel cleanly (and fires PageView with consent). No reload on deny.
      if (granted && window.__mkPixelGranted === false) { setTimeout(function () { location.reload(); }, 150); return; }
      window.dataLayer = window.dataLayer || [];
      window.dataLayer.push({ event: granted ? "consent_granted" : "consent_denied" });
    };
    var el = null;
    var show = function () {
      if (el) { el.classList.add("is-open"); return; }
      el = document.createElement("div");
      el.className = "consent"; el.setAttribute("role", "dialog"); el.setAttribute("aria-live", "polite");
      el.innerHTML = '<p>' + T.body + '</p>' +
        '<button type="button" class="btn btn--ghost btn--sm" data-consent="deny">' + T.decline + '</button>' +
        '<button type="button" class="btn btn--solid btn--sm" data-consent="grant">' + T.accept + '</button>';
      document.body.appendChild(el);
      el.addEventListener("click", function (e) {
        var b = e.target.closest("[data-consent]"); if (!b) return;
        apply(b.getAttribute("data-consent") === "grant"); el.classList.remove("is-open");
      });
      requestAnimationFrame(function () { el.classList.add("is-open"); });
    };
    var bar = document.querySelector(".footer__bar");
    if (bar) { var a = document.createElement("a"); a.href = "#"; a.textContent = T.link; a.className = "consent__link";
      a.addEventListener("click", function (e) { e.preventDefault(); show(); }); bar.appendChild(a); }
    if (!window.__mkConsent) show();
  })();


  /* ---- Sticky mobile action bar: Call + Book, always a thumb away ---- */
  (function () {
    var bar = document.createElement("div");
    bar.className = "actbar"; bar.setAttribute("aria-label", FR ? "Actions rapides" : "Quick actions");
    var contactHref = (function () {
      // Link to the homepage contact section from wherever we are. Climb one level
      // per directory we're nested in: "/" -> "", "/faq/" -> "../", "/faq/fr/" and
      // "/blog/fr/x.html" -> "../../".
      var seg = location.pathname.split("/").filter(Boolean);
      if (seg.length && seg[seg.length - 1].indexOf(".") > -1) seg.pop(); // drop the file name
      var up = new Array(seg.length + 1).join("../");
      return up + (FR ? "index-fr.html" : "index.html") + "#contact";
    })();
    bar.innerHTML =
      '<a href="tel:+14384020559" class="actbar__call">' +
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.6a2 2 0 0 1-.5 2.1L8 9.7a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.8.3 1.7.5 2.6.7a2 2 0 0 1 1.7 2z"/></svg>' +
        '<span>' + (FR ? "Appeler" : "Call") + '</span></a>' +
      '<a href="' + contactHref + '" class="actbar__book" data-calendly>' + (FR ? "Consultation gratuite" : "Book free consultation") + '</a>';
    document.body.appendChild(bar);

    // Calendly popup on the Book button (same behaviour as the other CTAs)
    bar.querySelector("[data-calendly]").addEventListener("click", function (e) {
      gaEvent("book_consultation_click", { method: "calendly_popup", lang: FR ? "fr" : "en", location: "sticky_bar" });
      if (window.Calendly && typeof window.Calendly.initPopupWidget === "function") {
        e.preventDefault(); window.Calendly.initPopupWidget({ url: CALENDLY_URL });
      }
    });

    // Show once the hero has (mostly) scrolled past; hide while the contact/booking
    // section is on screen. Scroll-driven so it works everywhere; rAF-throttled.
    var hero = document.querySelector(".hero, .post-hero, .blog-hero");
    var contact = document.getElementById("contact");
    var ticking = false;
    var update = function () {
      ticking = false;
      var vh = window.innerHeight;
      var pastHero = true;
      if (hero) { var hr = hero.getBoundingClientRect(); pastHero = hr.bottom < vh * 0.35; }
      var overContact = false;
      if (contact) { var cr = contact.getBoundingClientRect(); overContact = cr.top < vh * 0.9 && cr.bottom > vh * 0.15; }
      var on = pastHero && !overContact;
      bar.classList.toggle("is-on", on); document.body.classList.toggle("has-actbar", on);
    };
    var onScrollBar = function () { if (!ticking) { ticking = true; requestAnimationFrame(update); } };
    window.addEventListener("scroll", onScrollBar, { passive: true });
    window.addEventListener("resize", onScrollBar);
    update();
  })();

  /* ---- contact taps: phone / WhatsApp / email ---- */
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("a[href]");
    if (!a) return;
    var h = a.getAttribute("href") || "";
    if (h.indexOf("tel:") === 0) gaEvent("phone_click", { lang: FR ? "fr" : "en" });
    else if (h.indexOf("wa.me") !== -1) gaEvent("whatsapp_click", { lang: FR ? "fr" : "en", location: a.classList.contains("fab") ? "floating_button" : "inline" });
    else if (h.indexOf("mailto:") === 0) gaEvent("email_click", { lang: FR ? "fr" : "en" });
  }, true);
})();
