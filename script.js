/* ============================================================
   My Kurtains — interactions
   ============================================================ */
(function () {
  "use strict";

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
    "https://calendly.com/mykurtains/mykurtains-consultation?hide_gdpr_banner=1&background_color=fbf8f3&text_color=17130f&primary_color=a67c3d";
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
        note.textContent = "Please add your name and a way to reach you.";
        note.className = "contact__note err";
        return;
      }
      // No backend wired yet — hand off to WhatsApp / email so the lead isn't lost.
      const interest = form.interest.value;
      const message = form.message.value.trim();
      const body = `New consultation request:%0AName: ${encodeURIComponent(name)}%0AContact: ${encodeURIComponent(contact)}%0AInterested in: ${encodeURIComponent(interest)}%0ANotes: ${encodeURIComponent(message || "—")}`;

      note.textContent = "Thanks! Opening WhatsApp so we can confirm your details…";
      note.className = "contact__note ok";
      form.reset();

      setTimeout(() => {
        window.open(`https://wa.me/14384020559?text=${body}`, "_blank", "noopener");
      }, 600);
    });
  }
})();
