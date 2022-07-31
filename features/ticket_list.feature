# Created by Ilyas at 7/28/2022
Feature: Ticket list and selection

  Scenario: View the ticket list
    Given there are two created tickets
      | kind    | title                       | description         |
      | Bug     | Can't open ticket detail    | Bug description     |
      | Feature | Edit the ticket description | Feature description |
    When the home page is opened
    Then the ticket kinds are in the list
    And the ticket titles are in the list
    And the ticket statuses are in the list

  Scenario: Selecting a ticket from the list
    Given there is a created ticket
    And the home page is opened
    When I select a ticket from the list
    Then the browser opens the ticket detail
