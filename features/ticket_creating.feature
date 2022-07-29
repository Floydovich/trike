# Created by Ilyas at 7/21/2022
Feature: Creating a bug ticket
  As a developer,
  I want to be able create a bug report,
  So I can save it and fix the bug later.

  Scenario Outline: Submitting a new ticket
    Given the new ticket form is opened
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

  Scenario: Adding one more ticket
    Given there are tickets submitted earlier
    | kind    | title                       |
    | Bug     | I need more tickets!        |
    | Feature | I need even more tickets!!! |

    And the new ticket form is opened
    When I enter the title List shows only one ticket.
    And I submit the ticket
    Then the ticket list on home page is opened
    And the list displays the title List shows only one ticket.
    And the earlier tickets are still in the list
