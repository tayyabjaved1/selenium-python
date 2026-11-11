# Changelog

## 0.1.0

- Rebuilt from an empty repository as a Selenium + Python + Behave (BDD)
  e2e framework targeting demoqa.com, matching `demoqa-playwright-framework`'s
  layer-first architecture (`src/core`, `src/pages`, `src/api`, `src/data`)
  and docs-as-code governance (`docs/MODULE_CATALOG.md`,
  `docs/DOCUMENTATION_POLICY.md`, CI docs-check gate).
- Three scenarios, each live-verified against demoqa.com: Elements/Text Box
  (UI), Forms/Practice Form (UI), Book Store (API, no browser).
- Allure reporting via `allure-behave`, with screenshot-on-failure attached
  in `features/environment.py`'s `after_scenario` hook.
- Found and fixed two real demoqa.com bugs during live verification (not
  assumed): clearing the Practice Form's date-of-birth input crashes
  react-datepicker's internal state (worked around with select-all +
  overtype instead of `.clear()`); the Submit button's click is
  intermittently intercepted by an asynchronously-reloading ad slot even
  after on-load ad dismissal (worked around with scroll-into-view +
  re-dismiss + a JS-click fallback). Both documented in
  `docs/MODULE_CATALOG.md`'s Forms section.
