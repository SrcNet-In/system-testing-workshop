from typing import List, Dict, Any

all_test_results: List[Dict[str, Any]] = []

def pytest_runtest_makereport(item, call):
    """
    Pytest hook to collect test results after each test call.
    Only collects results from the actual test call (not setup/teardown).
    """
    if call.when != "call":
        return
    print("make report is called")