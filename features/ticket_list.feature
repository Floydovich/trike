# Created by Ilyas at 7/28/2022
Feature: Ticket list and selection

  Scenario: View the ticket list
    Given the list contains two created tickets
      | kind    | title                       | description         |
      | Bug     | Can't open ticket detail    | Bug description     |
      | Feature | Edit the ticket description | Feature description |
    When the home page is opened
    Then the ticket kinds are in the list
    And the ticket titles are in the list
    And the ticket statuses are in the list

#  Scenario Outline: View a ticket detail
#    When I click on the ticket with the title <title>
#    Then the browser opens the ticket detail page
#    And the page contains the title <title>
#    And the page contains the description <description>
#
#    Examples:
#      | title                      | description                   |
#      | Can't open ticket detail   | Bug description               |
#      | Can't edit the description | Outdated ticket's description |
