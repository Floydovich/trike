# Created by Ilyas at 7/21/2022
Feature: Creating a new ticket
  As a developer,
  I want to be able create a bug report,
  So I can save it to review later.

  Scenario: Moving to the new ticket form
    Given the home page is opened
    When I go the new ticket form
    Then the ticket form is opened

  Scenario Outline: Submitting a new ticket
    Given the ticket form is opened
    When I select the kind <kind>
    And I enter the title <title>
    And I submit the ticket
    Then the ticket list on home page is opened
    And the list displays the kind <kind>
    And the list displays the title <title>

    Examples:
    | kind    | title                                      |
    | Bug     | I cannot create a new ticket. Help please. |
    | Feature | I want to be able to select a ticket kind. |
