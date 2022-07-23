Feature: Bug report
  As a developer,
  I want to report about a bug,
  So I can fix it later.

  Scenario: Opening the home page
    Given the browser is opened
    When the user moves to the home page
    Then browser has "trike" in the title
    And there is "Issues" heading on the page

#  Scenario: Navigate to the new ticket report page
#    Given the home page is opened
#    When the user clicks the new ticket button
#    Then the user navigates to the new ticket page
#
#  Scenario: Creating and submitting a new ticket
#    Given the new ticket form is opened
#    When the user writes the title
#    And the user adds text to the form
#    And the user clicks the submit button
#    Then the user is redirected to the issues list
#    And the user sees the ticket title in the list