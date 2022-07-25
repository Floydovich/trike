# Created by Ilyas at 7/24/2022
Feature: Working on a bug ticket
  As a developer
  I want to read about a bug
  So I can start working to fix it

  Scenario Outline: Selecting a ticket from the list
    Given there are tickets in the list on the home page
      | title                      | description                   |
      | Can't open ticket detail   | Bug description               |
      | Can't edit the description | Outdated ticket's description |
    When I click on the ticket called <title>
    Then the browser opens the ticket <id> detail page
    And the page contains the title <title>
    And the page contains the description <description>

    Examples:
      |id | title                      | description                   |
      | 1 | Can't open ticket detail   | Bug description               |
      | 4 | Can't edit the description | Outdated ticket's description |
