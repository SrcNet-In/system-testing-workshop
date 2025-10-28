import requests
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
import logging

scenarios('../backend_test_demo/test_srcnet_api_health.feature')

@pytest.fixture
def context():
    return {}

@given(parsers.parse('the Site Capabilities API health endpoint "{url}"'))
def api_endpoint(context , url):
    pass

@when("the user sends a GET request")
def send_request(context):
    pass

@then("the response status code should be 200")
def verify_status(context):
    pass

@then(parsers.parse('the response should contain the status "{status}"'))
def verify_service_status(context , status):
    pass
