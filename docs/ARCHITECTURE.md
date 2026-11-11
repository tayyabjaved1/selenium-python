# Architecture

Layer-first, matching `core-pw-e2e-tests` and `demoqa-playwright-framework`:
one folder per concern, not one folder per feature module. A page object and
the Gherkin scenario that drives it live in different top-level trees
(`src/pages/` vs `features/`), connected only through step definitions.

```
src/
  core/      BasePage contract, driver factory, ad-overlay helper, env config
  pages/     page objects, grouped by UI area (elements/, forms/)
  api/       HTTP clients for API-level scenarios (no browser involved)
  data/      factories, builders, generators -- test data has its own layer
features/
  <area>/*.feature   Gherkin scenarios, grouped the same way as src/pages/
  steps/*.py         step definitions -- the only code that may import both
                      a page object and a feature file's step text
  environment.py      behave hooks: driver lifecycle, screenshot-on-failure,
                       self-cleaning API data
tests/unit/          pure-Python unit tests for the data layer (no browser,
                     no Selenium -- fast feedback on factory/builder logic)
```

## BasePage contract

Every page object implements two things:

- `path: str` -- the route this page lives at, relative to `BASE_URL`.
- `wait_for_loaded() -> None` -- the one assertion that proves the page is
  actually ready, not just that `driver.get()` returned.

`BasePage.open()` is the only way a test should navigate to a page: it does
`driver.get()`, dismisses the ad overlay, then calls `wait_for_loaded()`, in
that order, every time. A page object itself is never responsible for
remembering to dismiss ads or wait for its own heading -- that discipline is
centralized once, in the base class, so no individual page can skip it.

## Why ad dismissal happens twice

`src/core/ad_overlay.py` removes DemoQA's known ad slots (`#fixedban`, the
Google ads iframe) once on page load via `BasePage.open()`. One scenario
(the Practice Form submit) also calls it again immediately before a click
far down the page -- live testing showed DemoQA re-renders an ad slot
asynchronously as the page is scrolled, intercepting the Submit button's
click at its exact coordinates even though the on-load dismissal had
already run and found nothing there. See `docs/MODULE_CATALOG.md`'s Forms
section and the inline comment in `practice_form_page.py` for the full
story, including why the fix also falls back to a JS click rather than
relying on overlay removal alone.

## Why API scenarios skip the browser

`features/environment.py`'s `before_scenario` hook only builds a Selenium
driver when the scenario is not tagged `@api`. The Book Store scenario
(`features/bookstore/bookstore_api.feature`) never touches the DOM, so
spinning up a browser for it would only slow the suite down for no
verification benefit.

## Self-cleaning test data

The Book Store scenario creates a real account against demoqa.com's shared
public API, and deletes it in `after_scenario` regardless of whether the
scenario passed or failed -- this suite runs against a site everyone else's
test suites also hit, so it cannot leave accounts behind on a failure path.
