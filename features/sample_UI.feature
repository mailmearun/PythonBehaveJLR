Feature: Sample UI Test Feature

#  Scenario: Test Home page title
#    Given user launch the url
#    When verify the home page title is JLR Corporate Website

#  Scenario: Verify Links under Company Tab
#    Given user launch the url
#    When user hover on Company Tab
#    Then user is able to verify the below links under Company Tab
#    |Links_Under_Company_Tab|
#    |Leadership|
#    |Governance|
#    |Strategy|
#    |Modern Luxury|
#    |Electrification|
#    |Sustainability|
#    |Enterprise|


  Scenario Outline: Verify Link Navigation under Company Tab
    Given user launch the url
    When user hover on Company Tab
    Then click and verify the link <Company_Tab_Link> under Company Tab

    Examples:
    |Company_Tab_Link|
    |Leadership|
#    |Governance|
#    |Strategy|
#    |Modern Luxury|
#    |Electrification|
#    |Sustainability|
#    |Enterprise|