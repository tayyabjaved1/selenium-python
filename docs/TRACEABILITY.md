# Traceability

Which page object and data factory back each scenario -- so a page-object
change makes it obvious which scenarios to re-run manually if CI isn't
available.

| Scenario | Page object / API client | Data factory |
|---|---|---|
| Submits the text box form and shows the result in the output panel | `TextBoxPage` | `FormFactory.text_box()` |
| Submits a dynamically generated student profile | `PracticeFormPage` | `StudentFactory.create()` |
| Creates a unique user, adds a catalog book and verifies the collection | `BookStoreClient` | `UserFactory.bookstore_user()`, `BookFactory.first()` |
