# R & J Transport Service Inc — Website

Landing page for **R & J Transport Service Inc**, an intrastate trucking company based in Orlando, Florida.

- **Address:** 3803 Redditt Rd, Orlando, FL 32822
- **Phone:** (407) 595-9726
- **USDOT:** #1328058 · In business since 2018
- **Service area:** Florida intrastate only — Orlando → Miami, Orlando → Tampa, statewide

## What's inside

| File | Purpose |
|---|---|
| `index.html` | The entire site (HTML + CSS + JS, no build step) |
| `img/hero.jpg` | Hero background (semi truck at dusk, optimized) |
| `img/freight.jpg` | "Why choose us" section photo |
| `render.yaml` | One-click deploy config for Render |
| `robots.txt` / `sitemap.xml` | SEO basics |

## Run locally

```bash
cd rj-transport-services
python3 -m http.server 8000
# open http://localhost:8000
```

## Deploy on Render

1. Push this repo to GitHub.
2. On [Render](https://render.com): **New → Blueprint**, pick this repo (the `render.yaml` is picked up automatically), or **New → Static Site** and set the publish directory to the repo root.
3. Point the custom domain `rjtransportservicesinc.com` to the Render URL (Render provides the DNS records / CNAME).

## Notes

- All facts on the site (name, address, phone, USDOT, routes, hours) come from the company. No testimonials or statistics were invented.
- The two photos are web-sourced placeholders — for best results, replace `img/hero.jpg` and `img/freight.jpg` with photos of the company's own trucks (same filenames, no code changes needed).
