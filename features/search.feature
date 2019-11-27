@search
Feature: Search for space
  As a customer
  I want to search for a space
  so that I can choose my interested space to do advertising

  Scenario Outline: Search for space
    Given I am on homepage
    When I type "<location>" in the search input field on "<pageName>" page
    And I click the search button on "<pageName>" page
    Then I Should be on the search result page

    Examples:
      |location |pageName |
      |Sydney   |homepage |
      |Perth    |homepage |

  Scenario Outline: Search for space 2
    Given I am on homepage
    When I type "<location>" in the search input field on "<pageName>" page
    And I click the search button on "<pageName>" page
    Then I Should be on the search result page

    Examples:
      |location    |pageName |
      |Melbourne   |homepage |

#  Scenario Outline: Search for space with geo locations
#    Given I am on searchpage
#    When I type "<location>" in the search input field on "<pageName>" page
#    And I click the search button on "<pageName>" page
#    Then I Should be on the search result page
#    Examples:
#      |location |pageName    |gmw_address[0]|gmw_distance|gmw_units|gmw_form|gmw_per_page|gmw_lat     |gmw_lng            |gmw_px |action  |
#      |Melbourne|searchpage  |Sydney            |50          |metric   |1       |51          |-33.8688197 |151.20929550000005 |pt     |gmw_post|
#
