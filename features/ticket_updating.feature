# Created by Ilyas at 7/24/2022
Feature: Working on a bug ticket
  As a developer
  I want to read about a bug
  So I can start working to fix it

  Scenario Outline: Switching the ticket status
    Given the ticket status is <current_status>
    And the ticket detail page is opened
    When I mark the ticket as <next_status>
    Then the ticket status is changed to <next_status>

    Examples:
      | current_status | next_status |
      | PENDING        | IN REVIEW   |
      | IN REVIEW      | CLOSED      |

  # Scenario when the ticket is closed and the user cannot switch status any longer
