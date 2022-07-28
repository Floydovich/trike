# Created by Ilyas at 7/24/2022
Feature: Working on a bug ticket
  As a developer
  I want to read about a bug
  So I can start working to fix it

  Scenario Outline: Changing the ticket status
    Given the ticket detail page is opened
    And the ticket status is PENDING
    When I mark the ticket as <status>
    Then the ticket status is changed to <status>

    Examples:
      | status    |
      | PENDING   |
      | IN REVIEW |
      | DONE      |
