# Created by Ilyas at 7/24/2022
Feature: Updating a bug ticket
  As a developer
  I want to review a bug
  So I can update it or close it later


  Scenario Outline: Viewing a ticket detail

    Given the <kind> ticket with <title> and <description> is createad
    When the ticket detail page is opened
    Then the page contains the kind <kind>
    And the page contains the title <title>
    And the page contains the description <description>

    Examples:
      | kind    | title  | description     |
      | Bug     | First  | This is awful   |
      | Feature | Second | This is awesome |


  Scenario Outline: Changing the ticket status

    Given the ticket status is <current_status>
    And the ticket detail page is opened
    When I mark the ticket as <next_status>
    Then the ticket status is changed to <next_status>

    Examples:
      | current_status | next_status |
      | PENDING        | IN REVIEW   |
      | IN REVIEW      | CLOSED      |
      | CLOSED         | PENDING     |
