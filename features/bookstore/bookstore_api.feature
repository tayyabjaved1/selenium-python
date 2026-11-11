@bookstore @api @regression
Feature: Book Store - API

  Background:
    Given a unique bookstore account exists

  Scenario: Creates a unique user, adds a catalog book and verifies the collection
    When I add the first catalog book to the account
    Then the book should appear in the account collection
