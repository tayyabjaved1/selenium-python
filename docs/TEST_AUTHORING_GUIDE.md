# Test authoring guide

## Writing a scenario

1. Add a `.feature` file under `features/<area>/`, tagged natively
   (`@elements`, `@forms`, `@bookstore`, plus `@regression`/`@ui`/`@api`).
   Tags are Gherkin's own mechanism (`behave --tags=@regression`) -- do not
   invent a parallel convention in step text.
2. Write the scenario in Given/When/Then, one behaviour per scenario. Each
   step should read as a sentence a non-engineer could follow; the *how*
   belongs in the step definition, not the feature file.
3. Add step definitions in `features/steps/<area>_steps.py`. A step
   function's only job is to call a page object method or an API client
   method -- never raw Selenium calls inline in a step. If a step needs new
   page-object behaviour, add that method to the page object, not to the
   step file.
4. Generate test data through a factory (`src/data/factories/`) or builder
   (`src/data/builders/`), never hand-written literals in a step file --
   see `docs/DATA_FACTORY_GUIDE.md`.

## One step, one page-object call

```python
@when("I submit the generated student profile")
def step_submit_practice_form(context):
    context.student = StudentFactory.create()
    context.practice_form_page.submit(context.student)
```

Keep step definitions thin for the same reason Playwright's suite keeps
`test.step()` blocks thin: the feature file is the readable specification,
the page object is where the DOM knowledge lives, and the step definition
is just the wire between them.

## Running a subset

```bash
behave --tags=@elements              # one area
behave --tags=@regression            # by suite
behave features/forms                # one feature file
behave -n "Submits a dynamically"    # by scenario name
```

## Assert real behaviour, not implementation details

Prefer assertions against what a user would actually see (modal text,
output panel text, the collection returned by the API) over internal state.
Every `expect_*`/`assert` in a page object checks the outcome DemoQA itself
renders -- never a mocked or assumed response.
