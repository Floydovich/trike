# Created by Ilyas at 7/28/2022
Feature: Ticket list and selection
  As a developer
  I want to be able to view ticket list
  So I can see how many tickets there are,
    what kind are they and choose a ticket to work on

  Scenario: View the ticket list
    Given there are two created tickets
      | kind    | title                       | description         |
      | Bug     | Can't open ticket detail    | Bug description     |
      | Feature | Edit the ticket description | Feature description |
    When the home page is opened
    Then the ticket kinds are in the list
    And the ticket titles are in the list
    And the ticket statuses are in the list

  Scenario: Picking a ticket from the list
    Given there is a created ticket
    And the home page is opened
    When I pick a ticket from the list
    Then the browser opens the ticket detail
