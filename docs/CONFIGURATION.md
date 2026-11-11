# Configuration

All runtime config is environment variables, loaded via `python-dotenv` in
`src/core/config.py`. Copy `.env.example` to `.env` and adjust locally; CI
sets these as job env vars instead (see `.github/workflows/ci.yml`).

| Variable | Default | Meaning |
|---|---|---|
| `BASE_URL` | `https://demoqa.com` | Base URL every page object and the API client resolve against |
| `HEADLESS` | `true` | Whether Chrome launches headless (`--headless=new`) |
| `BROWSER` | `chrome` | Reserved for a future multi-browser driver factory; only Chrome is implemented |
| `IMPLICIT_WAIT_SECONDS` | `0` | Selenium's implicit wait -- kept at 0 deliberately; explicit `WebDriverWait` calls in page objects are the real wait strategy, not a blanket implicit one |
| `EXPLICIT_WAIT_SECONDS` | `10` | Timeout used by every `WebDriverWait` in the page objects |

`behave.ini`'s `[behave.userdata]` section mirrors `base_url`/`headless`
for discoverability from `behave --tags=...` runs, but `src/core/config.py`
(the `.env` file) is the actual source of truth read by the code.
