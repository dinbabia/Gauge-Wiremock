"""
These are just sample tests for wiremock.
"""

import os

from getgauge.python import step, data_store
from smart_assertions import soft_assert, verify_expectations

from step_impl.utils.send_request import get


def assert_mock_data_is_correct(actual_data):

    expected_data = data_store.scenario.request_body

    print(f"expected_data: {expected_data}")
    print(f"actual_data: {actual_data}")

    soft_assert(
        len(expected_data['create']) == len(actual_data),
        "[FAIL] len(expected_data['create']): {} != len(actual_data): {}"
        .format(len(expected_data['create']), len(actual_data))
    )

    for key in expected_data['create'].keys():
        soft_assert(
            expected_data['create'].get(key) == actual_data.get(key),
            "[FAIL] expected_data['create'].get({}): {} != actual_data.get({}): {}"
            .format(key, expected_data['create'].get(key), key, actual_data.get(key))
        )

    verify_expectations()

@step("Get user mock data")
def step_impl():
    user_id = data_store.scenario.request_body['create'].get('user_id')
    endpoint = f"/user/{user_id}/details"

    endpoint = os.getenv("api_host") + os.getenv("api_port") + endpoint
    print(f"endpoint: {endpoint}")

    response = get(
        endpoint = endpoint
        )
    assert_mock_data_is_correct(actual_data= response.json())


