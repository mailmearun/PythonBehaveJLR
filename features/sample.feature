Feature: Sample Feature

  Scenario: Test Home page title
    Given user launch the url
    When verify the home page title is ""

  Scenario: Verify Links under Company Tab
    Given user launch the url
    When user click on Company Tab
    Then user is able to verify the below links under Company Tab
    |Links_Under_Company_Tab|
    |Leadership|
    |Governance|
    |Strategy|
    |Modern Luxury|
    |Electrification|
    |Sustainability|
    |Enterprise|


  Scenario: Sample API test using requests library
    Given Execute Get API using endpoint ""
    When verify the response code is '200'
    Then verify the pet id in response