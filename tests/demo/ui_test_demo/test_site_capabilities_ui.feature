# Created by sayan_roy on 27/10/25
Feature: Validate Site Capabilities API UI Page

  Scenario Outline: Verify the documentation page title is displayed correctly
    Given the user navigates to "<url>"
    When the page is loaded
    Then the page title should be "Site Capabilities API Operator Documentation"


    Examples:
      | url                                                           |
      | https://site-capabilities.srcnet.skao.int/api/v1/www/docs/oper#overview |
