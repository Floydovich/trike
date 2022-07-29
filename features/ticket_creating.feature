# Created by Ilyas at 7/21/2022
Feature: Creating a bug ticket
  As a developer,
  I want to be able create a bug report,
  So I can save it and fix the bug later.

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

  Scenario Outline: Selection the ticket type
    Given the new ticket page is opened
    When I select to create a <ticket_type>
    And I press the submit button
    Then the ticket detail page is opened
    And the ticket type is <ticket_type>

    Examples:
    | ticket_type |
    | Bug         |
    | Feature     |