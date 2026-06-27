/* shrinkiatry.com — shared behavior. Progressive enhancement only. */
(function () {
  "use strict";

  /* ---- Theme (light/dark) with persistence ---- */
  var root = document.documentElement;
  var KEY = "shrinkiatry-theme";
  function setTheme(t, persist) {
    root.setAttribute("data-theme", t);
    var btn = document.querySelector("[data-theme-toggle]");
    if (btn) {
      btn.setAttribute("aria-pressed", String(t === "dark"));
      btn.setAttribute("aria-label", t === "dark" ? "Switch to light mode" : "Switch to dark mode");
    }
    if (persist) { try { localStorage.setItem(KEY, t); } catch (e) {} }
  }
  function initTheme() {
    var saved = null;
    try { saved = localStorage.getItem(KEY); } catch (e) {}
    if (saved === "light" || saved === "dark") { setTheme(saved, false); return; }
    var prefersDark = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
    setTheme(prefersDark ? "dark" : "light", false);
  }
  initTheme();
  document.addEventListener("click", function (e) {
    var t = e.target.closest("[data-theme-toggle]");
    if (!t) return;
    var current = root.getAttribute("data-theme") === "dark" ? "dark" : "light";
    setTheme(current === "dark" ? "light" : "dark", true);
  });

  /* ---- Mobile navigation ---- */
  var toggle = document.querySelector(".menu-toggle");
  var nav = document.getElementById("primary-nav");
  var backdrop = document.querySelector(".nav-backdrop");
  function openNav(open) {
    if (!nav) return;
    nav.setAttribute("data-open", String(open));
    if (backdrop) backdrop.setAttribute("data-open", String(open));
    if (toggle) toggle.setAttribute("aria-expanded", String(open));
    document.body.style.overflow = open ? "hidden" : "";
  }
  if (toggle) toggle.addEventListener("click", function () {
    openNav(nav.getAttribute("data-open") !== "true");
  });
  if (backdrop) backdrop.addEventListener("click", function () { openNav(false); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") openNav(false); });

  /* ---- Operating Room filtering ---- */
  var filters = document.querySelectorAll("[data-or-filter]");
  if (filters.length) {
    var cards = document.querySelectorAll("[data-or-card]");
    filters.forEach(function (f) {
      f.addEventListener("click", function () {
        var val = f.getAttribute("data-or-filter");
        filters.forEach(function (x) { x.setAttribute("aria-pressed", String(x === f)); });
        cards.forEach(function (c) {
          var tags = (c.getAttribute("data-or-tags") || "").split(" ");
          c.hidden = !(val === "all" || tags.indexOf(val) !== -1);
        });
        var live = document.getElementById("or-status");
        if (live) {
          var shown = Array.prototype.filter.call(cards, function (c) { return !c.hidden; }).length;
          live.textContent = shown + (shown === 1 ? " topic" : " topics") + " shown.";
        }
      });
    });
  }

  /* ---- Copy email links feedback (contact) ---- */
  document.addEventListener("click", function (e) {
    var c = e.target.closest("[data-copy]");
    if (!c) return;
    var text = c.getAttribute("data-copy");
    if (navigator.clipboard) {
      navigator.clipboard.writeText(text).then(function () {
        var old = c.textContent;
        c.textContent = "Copied";
        setTimeout(function () { c.textContent = old; }, 1600);
      });
    }
  });

  /* ---- Mark current year ---- */
  var y = document.querySelector("[data-year]");
  if (y) y.textContent = new Date().getFullYear();

  /* ---- Translate menu (machine translation via Google Translate) ---- */
  (function () {
    var anchor = document.querySelector(".network-bar__links");
    if (!anchor) return;
    var langs = [
      ["Español", "es"], ["Português", "pt"], ["Français", "fr"],
      ["Deutsch", "de"], ["Italiano", "it"], ["中文", "zh-CN"],
      ["العربية", "ar"], ["हिन्दी", "hi"],
      ["日本語", "ja"], ["Русский", "ru"]
    ];
    var bar = document.createElement("div");
    bar.className = "langbar";
    var label = document.createElement("span");
    label.className = "langbar__label";
    label.textContent = "Translate this page:";
    bar.appendChild(label);
    langs.forEach(function (l) {
      var a = document.createElement("a");
      a.textContent = l[0];
      a.setAttribute("lang", l[1]);
      a.href = "https://translate.google.com/translate?sl=en&tl=" + l[1] + "&u=" + encodeURIComponent(location.href);
      a.target = "_blank";
      a.rel = "noopener noreferrer";
      bar.appendChild(a);
    });
    anchor.parentNode.insertBefore(bar, anchor.nextSibling);
  })();
})();
