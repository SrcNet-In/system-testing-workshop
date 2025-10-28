# Created by sayan_roy at 27/10/25
Feature: Validate public placeholder api response

  Scenario Outline: Verify JSONPlaceholder returns post details correctly
    Given the API endpoint "<url>"
    When the user sends a GET request
    Then the response status code should be 200
    And the response should contain the title "<title>"

    Examples:
      | url                                          | title                                                                      |
      | https://jsonplaceholder.typicode.com/posts/1 | sunt aut facere repellat provident occaecati excepturi optio reprehenderit |