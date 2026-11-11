## <Module Name>

**Scope.** What user-visible capability does this module cover?

**Navigation.** Entry route(s)/`path`. Preconditions. Required role/account.

**Architecture.** Page object(s) (name each; confirm it extends `BasePage`
and implements `wait_for_loaded()` -- see `docs/ARCHITECTURE.md`). Factories/
builders used. API clients, if any.

**Test data.** Generated fields, required constraints, uniqueness,
overrides, and static reference data.

**Lifecycle.** Persisted resources, ownership, teardown, and unsupported
cleanup cases.

**Coverage** (`features/<module>/*.feature`): scenario description --
tag(s), e.g. `@regression @ui`.

**Known limitations.** Environment dependencies, unstable demo-site
behaviour, unimplemented scenarios, and any raw-selector fallback used
because an element has no accessible label/placeholder -- state why, and
whether it was reproduced live or assumed.

---

Add this section to `docs/MODULE_CATALOG.md` (and a row to its summary
table) in the same change that introduces the module -- see an existing
module's section there for a filled-in example.
