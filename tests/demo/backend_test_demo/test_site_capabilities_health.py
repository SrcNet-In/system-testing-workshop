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
    # context['url'] =  url
    pass

@when("the user sends a GET request")
def send_request(context):
    # api = context['url']
    # response = requests.get(api)
    # logging.info(f"Sent GET request to {api}, received status {response.status_code}")
    # context["response"] = response
    pass

@then("the response status code should be 200")
def verify_status(context):
    # assert context["response"].status_code == 200
    pass

@then(parsers.parse('the response should contain the status "{status}"'))
def verify_service_status(context , status):
    # data = context["response"].json()
    # assert data["status"] == status
    pass
