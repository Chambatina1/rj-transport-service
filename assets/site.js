/* R&J Transport Service Inc — small site script (menu + quote form). No dependencies. */
(function () {
  "use strict";
  var PHONE = "+14075959726";

  /* Mobile menu */
  var burger = document.querySelector(".burger");
  var menu = document.getElementById("mmenu");
  if (burger && menu) {
    burger.addEventListener("click", function () {
      var open = menu.classList.toggle("open");
      burger.setAttribute("aria-expanded", open ? "true" : "false");
    });
    menu.addEventListener("click", function (e) {
      if (e.target.tagName === "A") { menu.classList.remove("open"); burger.setAttribute("aria-expanded", "false"); }
    });
  }

  /* Hero video collage: load only when it helps (not on Save-Data, slow 2G/3G or reduced motion) */
  var vid = document.querySelector(".hero-video");
  if (vid) {
    var c = navigator.connection || {};
    var slow = c.saveData || /(^|-)2g|3g/.test(c.effectiveType || "");
    var still = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (!slow && !still) {
      /* 1080p on large/hi-dpi screens, 720p elsewhere; WebM only if H.264 is unsupported */
      var big = Math.max(window.innerWidth, window.innerHeight) * (window.devicePixelRatio || 1) >= 1300 && window.innerWidth >= 900;
      var src = big ? vid.getAttribute("data-src-hd") : vid.getAttribute("data-src");
      if (!vid.canPlayType('video/mp4; codecs="avc1.4D401F"')) src = vid.getAttribute("data-src-webm");
      vid.src = src;
      vid.addEventListener("playing", function () { vid.classList.add("playing"); });
      var p = vid.play(); if (p && p.catch) p.catch(function () {});
    }
  }

  /* Photo carousels: arrows, dots, counter, gentle autoplay (paused on interaction / reduced motion) */
  document.querySelectorAll(".carousel").forEach(function (car) {
    var track = car.querySelector(".car-track");
    var slides = track.querySelectorAll(".car-slide");
    var count = car.querySelector(".car-count");
    var dotsBox = car.querySelector(".car-dots");
    var n = slides.length, cur = 0, timer = null, stopped = false;
    var dots = [];
    for (var i = 0; i < n; i++) {
      var d = document.createElement("button");
      d.type = "button"; d.tabIndex = -1;
      (function (k) { d.addEventListener("click", function () { stop(); go(k); }); })(i);
      dotsBox.appendChild(d); dots.push(d);
    }
    function go(k) {
      k = (k + n) % n;
      var s = slides[k];
      track.scrollTo({ left: s.offsetLeft - (track.clientWidth - s.clientWidth) / 2, behavior: "smooth" });
    }
    function mark(k) {
      cur = k;
      count.textContent = (k + 1) + " / " + n;
      dots.forEach(function (d, j) { d.className = j === k ? "on" : ""; });
    }
    var raf = null;
    track.addEventListener("scroll", function () {
      if (raf) return;
      raf = requestAnimationFrame(function () {
        raf = null;
        var mid = track.scrollLeft + track.clientWidth / 2, best = 0, bd = 1e9;
        for (var j = 0; j < n; j++) {
          var c = slides[j].offsetLeft + slides[j].clientWidth / 2, dd = Math.abs(c - mid);
          if (dd < bd) { bd = dd; best = j; }
        }
        if (best !== cur) mark(best);
      });
    }, { passive: true });
    car.querySelector(".car-prev").addEventListener("click", function () { stop(); go(cur - 1); });
    car.querySelector(".car-next").addEventListener("click", function () { stop(); go(cur + 1); });
    track.addEventListener("keydown", function (e) {
      if (e.key === "ArrowRight") { e.preventDefault(); stop(); go(cur + 1); }
      if (e.key === "ArrowLeft") { e.preventDefault(); stop(); go(cur - 1); }
    });
    function stop() { stopped = true; if (timer) { clearInterval(timer); timer = null; } }
    ["pointerdown", "touchstart", "wheel", "focusin"].forEach(function (ev) { car.addEventListener(ev, stop, { passive: true }); });
    mark(0);
    var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (!reduce && "IntersectionObserver" in window) {
      new IntersectionObserver(function (es) {
        es.forEach(function (en) {
          if (stopped) return;
          if (en.isIntersecting && !timer) timer = setInterval(function () { go(cur + 1); }, 4500);
          else if (!en.isIntersecting && timer) { clearInterval(timer); timer = null; }
        });
      }, { threshold: 0.5 }).observe(car);
      car.addEventListener("mouseenter", function () { if (timer) { clearInterval(timer); timer = null; } });
      car.addEventListener("mouseleave", function () { if (!stopped && !timer) timer = setInterval(function () { go(cur + 1); }, 4500); });
    }
  });

  var form = document.getElementById("quote-form");
  if (!form) return;
  var es = form.getAttribute("data-lang") === "es";
  var T = es ? {
    sending: "Enviando…", ok: "¡Gracias! Recibimos su solicitud. Un despachador le contactará pronto.",
    err: "No pudimos enviar el formulario. Llámenos al (407) 595-9726 o escriba a rjtransportusa@gmail.com.",
    req: "Por favor complete nombre y teléfono.",
    sms: "Abriendo su app de mensajes con la solicitud lista para enviar…",
    desk: "Llámenos al (407) 595-9726 o envíe este mensaje por texto a ese número:\n\n",
    head: "Solicitud de cotización - R&J Transport", tow: "Grúa", freight: "Carga",
    dep: "\n\nSiguiente paso: envíe el depósito de $100 por Zelle al (407) 595-9726 (R&J Transport Service Inc.). La grúa sale cuando recibimos el depósito."
  } : {
    sending: "Sending…", ok: "Thank you! We received your request. A dispatcher will contact you shortly.",
    err: "We couldn't send the form. Please call (407) 595-9726 or email rjtransportusa@gmail.com.",
    req: "Please fill in your name and phone.",
    sms: "Opening your messaging app with the request ready to send…",
    desk: "Call us at (407) 595-9726, or text this message to that number:\n\n",
    head: "Quote request - R&J Transport", tow: "Towing", freight: "Freight",
    dep: "\n\nNext step: send the $100 Zelle deposit to (407) 595-9726 (R&J Transport Service Inc.). The tow truck rolls once the deposit is received."
  };

  /* Towing / freight toggle */
  function setMode(m) {
    form.setAttribute("data-mode", m);
    var r = document.getElementById(m === "tow" ? "m-tow" : "m-freight");
    if (r) r.checked = true;
  }
  form.querySelectorAll('input[name="service"]').forEach(function (r) {
    r.addEventListener("change", function () { setMode(r.value); });
  });
  document.querySelectorAll('a[data-mode]').forEach(function (a) {
    a.addEventListener("click", function () { setMode(a.getAttribute("data-mode")); });
  });

  var status = form.querySelector(".form-status");
  function show(msg, ok) {
    status.textContent = msg;
    status.className = "form-status show" + (ok ? " ok" : "");
  }

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var data = new FormData(form);
    if (data.get("_gotcha")) return;
    if (!String(data.get("name") || "").trim() || !String(data.get("phone") || "").trim()) { show(T.req); return; }
    var mode = form.getAttribute("data-mode");
    var keys = mode === "tow"
      ? ["name", "company", "phone", "email", "location", "vehicle", "message"]
      : ["name", "company", "phone", "email", "pickup", "delivery", "freight_type", "frequency", "message"];
    var payload = { service: mode === "tow" ? T.tow : T.freight, page: location.href };
    var lines = [T.head + " (" + payload.service + ")"];
    keys.forEach(function (k) {
      var v = String(data.get(k) || "").trim();
      payload[k] = v;
      if (v) lines.push(k.replace("_", " ") + ": " + v);
    });
    var text = lines.join("\n");
    payload._subject = T.head + " (" + payload.service + ")";
    payload._template = "table";
    payload._captcha = "false";
    var endpoint = form.getAttribute("data-endpoint");
    var btn = form.querySelector('button[type="submit"]');

    if (endpoint) {
      btn.disabled = true; show(T.sending);
      fetch(endpoint, { method: "POST", headers: { "Content-Type": "application/json", "Accept": "application/json" }, body: JSON.stringify(payload) })
        .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
        .then(function (j) {
          /* FormSubmit answers HTTP 200 with success "false" while the inbox is not activated: treat that as a failure */
          if (!j || String(j.success) !== "true") throw new Error((j && j.message) || "not sent");
          show(T.ok + (mode === "tow" ? T.dep : ""), true); form.reset(); setMode(mode);
        })
        .catch(function () { show(T.err); })
        .then(function () { btn.disabled = false; });
      return;
    }
    /* No endpoint configured yet: hand the request to SMS (mobile) or show it (desktop). */
    if (/Android|iPhone|iPad|iPod/i.test(navigator.userAgent)) {
      show(T.sms, true);
      window.location.href = "sms:" + PHONE + "?&body=" + encodeURIComponent(text);
    } else {
      show(T.desk + text);
    }
  });
})();
