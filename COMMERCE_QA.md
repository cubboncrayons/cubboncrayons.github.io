# Cubbon Crayons · Commerce QA & 9+/10 launch checklist

Last revised: 2026-11-24

## Current product setup
- Five individual A4 Kannada–English downloadable story PDFs, listed at ₹49 each.
- Product URLs are linked from the GitHub Pages website to Payhip.
- Five-story bundle **not activated**. The collection section describes what exists, but does not claim a discounted bundle can be bought.
- Free family activities remain free.
- The checkout provider, not GitHub Pages, handles payment and digital downloads.

## Priority 2 · Genuine customer trust
- [x] Explain format, previews, printing and support before checkout.
- [x] Publish the contact/support and refund routes.
- [x] Clarify external checkout in Terms, Refunds and Business & Support.
- [ ] Verify legal business operator's name, business address and applicable registration/tax disclosures; publish accurate details.
- [ ] Verify direct customer-service and grievance contact information.
- [ ] Collect real, permissioned parent reviews. Never generate fictional testimonials.
- [ ] Align age recommendations across website, Payhip storefront and individual listings (website currently 2–5, storefront was observed as 2–3 on 2026-11-24).

## Priority 3 · Measurement
- [x] Use readable campaign labels in outbound homepage Payhip links: utm_source=cubboncrayons, utm_medium=website, utm_campaign=stories.
- [x] Document this use of campaign labels in Privacy Policy.
- [ ] Confirm whether Payhip retains/exposes campaign attribution; if not, configure a legitimate no-cookie or consent-managed analytics platform before claiming website conversion tracking.
- [ ] Record weekly: website sessions, story preview interactions, Payhip product visits, checkout initiations if provided, completed orders, refunds, gross revenue and average order value.
- [ ] Distinguish Instagram campaign links from website links using campaign tags. Avoid putting customer identifiers or children's data in URLs.
- [ ] Review analytic service privacy requirements and update CSP, Privacy Policy and consent flow (if required) before activation.

## Priority 4 · Real bundle
- [x] Present five available story covers and honest combined single-item cost (5 × ₹49 = ₹245).
- [ ] Configure a Payhip 5-story bundle only after confirming all five PDF versions and bundle download behavior.
- [ ] Test proposed ₹179 bundle price against margins, processor fees and actual parent interest; do not describe as an active offer until checkout is live.
- [ ] Replace the not-yet-available text only after verifying a working bundle product URL and correct delivery.

## Priority 5 · Mobile QA
- [x] 2-column small-phone card layout, 1-column on very narrow screens.
- [x] Responsive trust panels and bundle image layout.
- [x] Visible keyboard focus and reduced-motion compatibility.
- [ ] Real iOS Safari and Android Chrome tests at 320, 375, 390, 414, 768 and 1024 CSS px.
- [ ] Confirm no horizontal overflow, clipping, overlapping site navigation or mis-taps.
- [ ] Verify product page links, checkout navigation, download delivery, PDF opening and actual print accuracy from mobile.

## Exit criterion
Commercial readiness may be rated 9+/10 only when checkout, customer contact disclosures, delivery, live responsive design, product claims, and attribution are verified using real customer-like tests. Passing code-only checks does not establish a 9+/10 real-world launch.
