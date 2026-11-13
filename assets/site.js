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

  var form = document.getElementById("quote-form");
  if (!form) return;
  var es = form.getAttribute("data-lang") === "es";
  var T = es ? {
    sending: "Enviando…", ok: "¡Gracias! Recibimos su solicitud. Un despachador le contactará pronto.",
    err: "No pudimos enviar el formulario. Llámenos al (407) 595-9726.",
    req: "Por favor complete nombre y teléfono.",
    sms: "Abriendo su app de mensajes con la solicitud lista para enviar…",
    desk: "Llámenos al (407) 595-9726 o envíe este mensaje por texto a ese número:\n\n",
    head: "Solicitud de cotización - R&J Transport", tow: "Grúa", freight: "Carga"
  } : {
    sending: "Sending…", ok: "Thank you! We received your request. A dispatcher will contact you shortly.",
    err: "We couldn't send the form. Please call (407) 595-9726.",
    req: "Please fill in your name and phone.",
    sms: "Opening your messaging app with the request ready to send…",
    desk: "Call us at (407) 595-9726, or text this message to that number:\n\n",
    head: "Quote request - R&J Transport", tow: "Towing", freight: "Freight"
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
    var endpoint = form.getAttribute("data-endpoint");
    var btn = form.querySelector('button[type="submit"]');

    if (endpoint) {
      btn.disabled = true; show(T.sending);
      fetch(endpoint, { method: "POST", headers: { "Content-Type": "application/json", "Accept": "application/json" }, body: JSON.stringify(payload) })
        .then(function (r) { if (!r.ok) throw new Error(r.status); show(T.ok, true); form.reset(); setMode(mode); })
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
