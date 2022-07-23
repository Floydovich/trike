Feature: Bug report
  As a developer,
  I want to be able create a bug report,
  So I can save and fix it later.

  Scenario: Opening the home page
    Given the browser is opened
    When I move to the home page
    Then the browser title is "trike"
    And there is "Bugs and features" heading on the page

  Scenario: Creating and submitting a new ticket
    Given the home page is opened
    When I write the ticket title
    And I add some text to the ticket description
    And I click the submit button
    Then the browser opens the home page again
    And I see the ticket title in the list on page