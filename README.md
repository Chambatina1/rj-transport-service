# R&J Transport Service Inc — Website

Bilingual (EN/ES) static website for **R&J Transport Service Inc** — heavy towing and freight trucking in Orlando, FL since 2004.

- **Address:** 4980 Patch Rd, Orlando, FL 32822
- **Phone:** (407) 595-9726 · 24 hour service
- **Email:** rjtransportusa@gmail.com · **USDOT:** 1328058
- **Service area:** all of Florida, neighboring states (GA, AL) and further north (Carolinas, Tennessee)

## How the site is built

Every HTML page is **generated** by `tools/build.py` (Python 3, standard library only). Do not edit the HTML files by hand — edit the content and re-run the build:

```bash
python3 tools/build.py      # regenerates all pages + sitemap.xml
python3 -m http.server 8000 # preview at http://localhost:8000
```

| Path | Purpose |
|---|---|
| `tools/build.py` | Business facts (NAP), page templates, home/towing/freight/contact pages, schema, sitemap |
| `tools/content.py` | Service-area pages and blog posts (EN + ES) |
| `assets/site.css`, `assets/site.js` | Shared styles and script (menu, quote form) |
| `img/`, `media/` | Real company photos (fleet, wrecker, loads) and the home hero video collage (`media/hero-collage.mp4`/`.webm`, poster `img/hero-collage.*`). The video loads only on fast connections without reduced-motion. Neighbor signs are cropped/blurred. |

### Pages (each in English and Spanish, linked with hreflang)
Home · Heavy Towing · Freight & Contracts · Service Areas (Orlando, Tampa, Miami, Jacksonville, Southeast) · Contact · Blog (3 posts)

### Adding a blog post
Add an entry to `BLOG_POSTS` in `tools/content.py` (both `en` and `es`), run the build, commit.

### Quote form
Requests are sent through FormSubmit (`SITE["form_endpoint"]` in `tools/build.py`) to rjtransportusa@gmail.com. **One-time step:** after the site is live, submit the form once; FormSubmit emails an activation link to that inbox — click it. If the endpoint is emptied, the form falls back to SMS (mobile) or shows the request text (desktop).

## Deploy (Render)
`render.yaml` deploys the repo root as a static site. Custom domain: `www.rjtransportservicesinc.com` (see `CNAME`).
