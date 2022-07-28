# Created by Ilyas at 7/28/2022
Feature: Ticket list and ticket selection

  Scenario: Opening the home page
    Given the browser is opened
    When I move to the home page
    Then the browser title is "trike"
    And the page heading says "List of bugs"

  Scenario Outline: View a ticket detail
    Given the list contains two created tickets
      | title                      | description                   |
      | Can't open ticket detail   | Bug description               |
      | Can't edit the description | Outdated ticket's description |

    When I click on the ticket with the title <title>
    Then the browser opens the ticket <id> detail page
    And the page contains the title <title>
    And the page contains the description <description>

    Examples:
      | id | title                      | description                   |
      | 1  | Can't open ticket detail   | Bug description               |
      | 4  | Can't edit the description | Outdated ticket's description |
