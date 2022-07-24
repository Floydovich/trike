# Created by Ilyas at 7/24/2022
Feature: Working on a bug ticket
  As a developer
  I want to read about a bug
  So I can start working to fix it

  Scenario Outline: Selecting a ticket from the list
    Given there are two tickets in the list on the home page
    When I click on the ticket called <title>
    Then the browser opens the ticket's detail page <id>
    And the page contains the title <title>
    And the page contains the description <description>

    Examples:
      |id | title   | description   |
      | 1 | Title 1 | Description 1 |
      | 2 | Title 2 | Description 2 |
