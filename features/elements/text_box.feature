@elements @regression @ui
Feature: Elements - Text Box

  Scenario: Submits the text box form and shows the result in the output panel
    Given I open the Text Box page
    When I submit the text box form with generated data
    Then the output panel should show the submitted data
