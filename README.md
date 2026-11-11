# selenium-python

Selenium + Python + Behave (BDD) e2e framework for [demoqa.com](https://demoqa.com),
revamped from an empty repository to match `demoqa-playwright-framework`'s
layer-first architecture and docs-as-code governance -- same shape, different
stack: Gherkin `.feature` files instead of `.spec.ts`, page objects in plain
Python instead of TypeScript, Behave's native tags instead of Playwright's.

## Coverage

| Module | Scenario | Tags |
|---|---|---|
| Elements | Submits the text box form and shows the result in the output panel | `@elements @regression @ui` |
| Forms | Submits a dynamically generated student profile | `@forms @regression @ui` |
| Book Store (API) | Creates a unique user, adds a catalog book and verifies the collection | `@bookstore @api @regression` |

See `docs/MODULE_CATALOG.md` for what each module covers, including two
real demoqa.com bugs found and worked around during live verification.

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env

pytest              # unit tests for the data layer -- no browser, no network
behave              # the full BDD suite against demoqa.com
behave --tags=@elements   # one module
behave --tags=@api        # API-only, no browser spun up
```

Selenium 4's bundled Selenium Manager resolves a matching chromedriver
automatically -- no manual driver download or `webdriver-manager` needed,
as long as Chrome itself is installed.

## Allure reporting

```bash
behave -f allure_behave.formatter:AllureFormatter -o allure-results
allure serve allure-results   # requires the allure commandline tool
```

CI generates and uploads the Allure report as a build artifact on every
run (`.github/workflows/ci.yml`), installing the `allure` commandline tool
directly from its GitHub release rather than a third-party Docker action --
see `docs/CONFIGURATION.md` for why.

## Layout

```
src/
  core/      BasePage contract, Chrome driver factory, ad-overlay helper, env config
  pages/     page objects (elements/, forms/)
  api/       Book Store HTTP client (requests, no browser)
  data/      factories, builders, generators
features/
  <area>/*.feature   Gherkin scenarios
  steps/*.py         step definitions
  environment.py      driver lifecycle, screenshot-on-failure, self-cleaning API data
tests/unit/          pure-Python unit tests for the data layer
docs/                ARCHITECTURE, TEST_AUTHORING_GUIDE, MODULE_CATALOG, DATA_FACTORY_GUIDE,
                     FACTORY_CATALOG, API_GUIDE, CONFIGURATION, DOCUMENTATION_POLICY,
                     CHANGE_IMPACT_MATRIX, TRACEABILITY, TEST_CATALOG, templates/
scripts/             check_docs_changes.py -- the CI docs-governance gate
```

See `docs/ARCHITECTURE.md` for the full design and why each piece exists,
and `CONTRIBUTING.md` before adding a scenario.

## License

[MIT](LICENSE)
