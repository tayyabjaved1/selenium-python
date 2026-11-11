# Module catalog

Centralized, not one README per module -- matches `demoqa-playwright-framework`
and `core-pw-e2e-tests`. One source of truth for what each UI area covers,
how it's navigated, and what's known not to work.

| Module | Page object | Feature file | Scope |
|---|---|---|---|
| Elements | `src/pages/elements/text_box_page.py` | `features/elements/text_box.feature` | Text Box form submit + output panel |
| Forms | `src/pages/forms/practice_form_page.py` | `features/forms/practice_form.feature` | Practice Form submit + confirmation modal |
| Book Store (API) | `src/api/bookstore_client.py` | `features/bookstore/bookstore_api.feature` | Account creation, add book, collection verification -- no browser |

## Elements

- **Scope**: `/text-box` -- fills all four fields, submits, verifies the
  output panel echoes every value back.
- **Navigation**: `TextBoxPage.open()` -- `BasePage` handles ad dismissal
  and the "Text Box" heading wait.
- **Selectors**: Full Name, Email, Current Address use their placeholder
  text. Permanent Address has no placeholder or accessible label on
  DemoQA's markup -- selected by its raw `#permanentAddress` id instead,
  documented inline in the page object.
- **Test data**: `FormFactory.text_box()` -- generated via `CommonGenerator`.
- **Known limitations**: none found in live testing.

## Forms

- **Scope**: `/automation-practice-form` -- fills the full student profile
  fields the submit flow uses, submits, verifies the confirmation modal.
- **Navigation**: `PracticeFormPage.open()`.
- **Selectors**: most fields use placeholder text. Gender/hobbies radios
  are visually hidden on DemoQA's markup -- only the `<label>` is
  interactable, selected by its visible text via XPath. The date-of-birth
  input (`#dateOfBirthInput`) has no accessible label of its own.
- **Known bug worked around**: calling `.clear()` on the date-of-birth
  input nulls react-datepicker's internal state and crashes the page
  entirely (`Cannot read properties of null (reading 'getMonth')` in the
  browser console). Fixed by select-all + overtype (`Ctrl+A` then type)
  instead of `.clear()`.
- **Known bug worked around**: DemoQA re-renders an ad slot asynchronously
  as the page is scrolled through, which can intercept the Submit button's
  click at its exact on-screen coordinates even immediately after ad
  dismissal ran and found nothing to remove -- this was reproduced live,
  not assumed. Fixed by scrolling the button into view, re-running ad
  dismissal, and falling back to a JS click
  (`execute_script("arguments[0].click()")`) if the native click is still
  intercepted, since a JS click bypasses the browser's own
  visibility/overlap check.
- **Test data**: `StudentFactory.create()` / `StudentBuilder` for
  scenario-specific overrides (gender, address).

## Book Store (API)

- **Scope**: creates a unique DemoQA account via the public Book Store API,
  adds the first catalog book, verifies it appears in the account's
  collection.
- **No browser**: tagged `@api`; `features/environment.py`'s
  `before_scenario` hook skips building a Selenium driver for this tag.
- **Test data**: `UserFactory.bookstore_user()` for the account,
  `BookFactory.first()` for the book.
- **Self-cleaning**: `after_scenario` deletes the created account
  regardless of pass/fail, since this hits demoqa.com's real shared API.
- **Known limitations**: none found in live testing.
