@forms @regression @ui
Feature: Forms - Practice Form

  Scenario: Submits a dynamically generated student profile
    Given I open the Practice Form page
    When I submit the generated student profile
    Then the confirmation modal should show the submitted profile
