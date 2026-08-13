/* ============================================================
   My Kurtains — interactions
   ============================================================ */
(function () {
  "use strict";

  // Page language ("fr" on index-fr.html, else "en"). Drives the Calendly
  // event and the form's user-facing strings.
  var FR = (document.documentElement.lang || "en").toLowerCase().slice(0, 2) === "fr";

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
      if (window.Calendly && typeof window.Calendly.initPopupWidget === "function") {
        e.preventDefault();
        window.Calendly.initPopupWidget({ url: CALENDLY_URL });
      }
    });
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

  /* ---- contact form (front-end only demo) ---- */
  const form = document.getElementById("contactForm");
  const note = document.getElementById("formNote");
  if (form) {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const name = form.name.value.trim();
      const contact = form.phone.value.trim();
      if (!name || !contact) {
        note.textContent = FR
          ? "Ajoutez votre nom et une façon de vous joindre, s’il vous plaît."
          : "Please add your name and a way to reach you.";
        note.className = "contact__note err";
        return;
      }
      // No backend wired yet — hand off to WhatsApp / email so the lead isn't lost.
      const interest = form.interest.value;
      const message = form.message.value.trim();
      const head = FR ? "Nouvelle demande de consultation" : "New consultation request";
      const lName = FR ? "Nom" : "Name";
      const lContact = FR ? "Coordonnées" : "Contact";
      const lInterest = FR ? "Intéressé(e) par" : "Interested in";
      const lNotes = FR ? "Notes" : "Notes";
      const body = `${head}:%0A${lName}: ${encodeURIComponent(name)}%0A${lContact}: ${encodeURIComponent(contact)}%0A${lInterest}: ${encodeURIComponent(interest)}%0A${lNotes}: ${encodeURIComponent(message || "—")}`;

      note.textContent = FR
        ? "Merci ! Ouverture de WhatsApp pour confirmer vos détails…"
        : "Thanks! Opening WhatsApp so we can confirm your details…";
      note.className = "contact__note ok";
      form.reset();

      setTimeout(() => {
        window.open(`https://wa.me/14384020559?text=${body}`, "_blank", "noopener");
      }, 600);
    });
  }
})();
