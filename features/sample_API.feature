Feature: Sample API Test Feature

  Scenario: Sample GET API test
    Given Execute Get API using endpoint "v2/pet/123"
    When verify the response code is "200"
    Then verify the data in response
      | id  | name   | status    |
      | 123 | doggie | available |

