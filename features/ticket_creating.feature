Feature: Creating a bug ticket
  As a developer,
  I want to be able create a bug report,
  So I can save it and fix the bug later.

  Scenario: Opening the home page
    Given the browser is opened
    When I move to the home page
    Then the browser title is "trike"
    And the page heading says "List of bugs"

  Scenario: Submitting a new ticket
    Given the home page is opened
    When I enter the title Cannot create a ticket.
    And I enter the description
      """
      There is no way to create a bug report ticket. The app is
      still very raw and has no basic functionality at all.
      """
    And I press the submit button
    Then Cannot create a ticket. is displayed in the list

  Scenario: Adding one more ticket
    Given the page has submitted ticket
    When I enter the title List shows only one ticket.
    And I enter the description
        """
        When I create more than one ticket the page doesn't show all tickets.
        It only shows the first one.
        """
    And I press the submit button
    Then List shows only one ticket. is displayed in the list
    And the previously created ticket is still in the list
