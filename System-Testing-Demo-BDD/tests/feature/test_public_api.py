import requests
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
import logging
scenarios('../feature/test_public_api.feature')

@pytest.fixture
def context():
    return {}

@given(parsers.parse('the API endpoint "{url}"'))
def api_endpoint(context , url):
    context['url'] =  url

@when("the user sends a GET request")
def send_request(context):
    api = context['url']
    response = requests.get(api)
    logging.info(f"Sent GET request to {api}, received status {response.status_code}")
    context["response"] = response

@then("the response status code should be 200")
def verify_status(context):
    assert context["response"].status_code == 200

@then(parsers.parse('the response should contain the title "{title}"'))
def verify_title(context , title):
    data = context["response"].json()
    assert data["title"] == title