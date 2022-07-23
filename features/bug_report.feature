Feature: Bug report
  As a developer,
  I want to be able create a bug report,
  So I can save and fix it later.

  Scenario: Opening the home page
    Given the browser is opened
    When I move to the home page
    Then the browser title is "trike"
    And the page heading says "No reported bugs"

  Scenario: Creating and submitting a new ticket
    Given the home page is opened
    When I write the ticket title "Cannot create a ticket"
    And I add some text to the ticket description and submit
    Then the page heading now says "Reported bugs: 1"
    And the first ticket in the list has title "Cannot create a ticket"