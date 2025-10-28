Feature: Validate Health Endpoints of SRCNet Services

  Scenario Outline: Verify service health endpoint returns status UP
    Given the Site Capabilities API health endpoint "<url>"
    When the user sends a GET request
    Then the response status code should be 200
    And the response should contain the status "UP"

    Examples:
      | url                                                      |
      | https://site-capabilities.srcnet.skao.int/api/v1/ping     |