Feature: Bug report
  As a developer,
  I want to be able create a bug report,
  So I can save it and fix the bug later.

  Scenario: Opening the home page
    Given the browser is opened
    When I move to the home page
    Then the browser title is "trike"
    And the page heading says "No reported bugs"

  Scenario: Submitting a new bug reporting ticket
    Given the home page is opened
    When I write the ticket title "Cannot create a ticket"
    And I add some text to the ticket description and submit
    Then the first ticket in the list says "Cannot create a ticket"

  Scenario: Adding one more bug reporting ticket
  This is needed for test triangulation which ensures that page will
  have all the tickets the users submit
    Given the home page has one submitted ticket
    When I submit a new ticket with title and description
    Then the second ticket title is shown on the page
    And the first ticket is still there
