
import copy

from getgauge.python import step, data_store, Messages

from step_impl.utils.string_formatter import string_format


def get_request_tags(scenario_test_case : dict):
    """
    Get the request_tag value from the scenario_test_case

    Examples: (csv value)
        * "Australia"
            = [ "Australia" ]
        * "Australia|Philippines"
            = [ "Australia" , "Philippines" ]

    Args:
        scenario_test_case (dict) : The current scenario test case
    Return:
        list : A list of request tags.
    """
    request_tags = scenario_test_case['request_tag']
    request_tags = str(request_tags).split("|")
    print(f"request_tags: {request_tags}")
    return request_tags


def fill_request_body( key : str, values : list, request_tags : list, request_body : dict ):
    """
    Fill the request body dictionary according to the data written in csv.
    Also we use the string formatter to format the values.

    Args:
        key (str) : The current key in the iterated test case dictionary.
        values (list) : The current values in the iterated test case dictionary. List if it contains a separator '|'.
        request_tags (list) : The request tags from the test case dictionary
        request_body (dict) : The dictionary that we need to fill up again until iteration in test case dictionary is done.
    Return:
        dict : The dictionary that we have filled up
    """
    for index, val in enumerate(values):

        # Check if value is empty in the csv file. If empty, then skip/continue the loop. (Not included in the request body)
        if val == '':
            continue

        # Check if value is <null>, <empty>, etc and convert it to its correct value. Else return original value
        format_value = string_format(val)

        if len(values) == 1:
            # Add the SAME VALUE in ALL Request Tags
            # e.g.
            # FROM: name = "QA"
            # TO: name(create) = QA
            for tag in request_tags:
                request_body[tag][key] = format_value
        else:
            # Add the SPECIFIC VALUE in EACH Request Tag
            # e.g.
            # FROM: name = "QA|QA TESTER"
            # TO: name(create) = QA, name(update) = QA TESTER
            request_body[request_tags[index]][key] = format_value

    return request_body


@step("Prepare current test case <testCase>")
def step_impl(testCase):
    # Get the specific test case from the data_store.spec.test_case_dict
    scenario_test_case = copy.deepcopy(data_store.spec.test_case_dict[testCase])

    # Get the request_tag values from our test case
    request_tags = get_request_tags(scenario_test_case)

    # remove request_tag field to reduce iteration in next step
    del scenario_test_case['request_tag']

    # Create our empty request body
    request_body = dict()

    # Add our request tags to the request_body as key
    for request_tag in request_tags: request_body[request_tag] = {}

    # Iterate each key-value of the test_case/row
    for key, value in scenario_test_case.items():

        # If value contains "|", then separate them. e.g. user|stylist -> ['user', 'stylist']
        values : list = value.split("|")

        # Check if length of values is not 1 or does not have the same number of separator with request_tag
        if len(values) not in [len(request_tags), 1]:
                raise RuntimeError(f"Field name: '{key}' has different number of separator with request_tag.")

        # Fill the request_body
        request_body = fill_request_body( key, values, request_tags, request_body)

    data_store.scenario.request_body = request_body
    Messages.write_message(f"data_store.scenario.request_body: {data_store.scenario.request_body}")
    print(f"data_store.scenario.request_body:\n{data_store.scenario.request_body}")
