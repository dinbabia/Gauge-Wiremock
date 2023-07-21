"""
Contains all the hooks during gauge tests.
- before_spec
- after_spec
- before_scenario
- etc.
"""
import time

from getgauge.python import \
    before_spec, before_scenario, data_store, DictObject

from step_impl.utils.csv_reader import \
    extract_csv_file_from_spec, parse_csv_to_gauge_table


@before_spec
def before_spec_hook(context):
    print("SPEC - START : " + context.specification.name)

    # Mark Timestamp (this timestamp can be used in the string formatter)
    data_store.suite.time = time.time()
    data_store.suite.timestamp = str(int(data_store.suite.time * 1000))

    # Create Dictionary Object to save our test cases in a dictionary
    test_case_dict = DictObject()

    # Extract the csv file name written in the specification i.e. table:specs/.../.../..csv
    csv_file = extract_csv_file_from_spec(context.specification)

    # Check if csv file path is found
    if csv_file:
        # Parse the csv
        table = parse_csv_to_gauge_table(csv_file)

        # Create an empty variable for test case name
        test_case_name = ''

        # Iterate each row of the csv
        for row_data in table.rows:

            # Iterate each column of the current row
            for column_index, column_name in enumerate(table.headers):

                # testCase field will be the "key" in our test_case_dict for the current row
                if "testCase" in str(column_name):
                    column_name = "testCase"
                    test_case_name = str(row_data[column_index])
                    test_case_dict[test_case_name] = {}
                else:

                    # When the "testCase" key is now in the test_case_dict, add all data to this dictionary
                    test_case_dict[test_case_name][str(column_name)] = str(row_data[column_index])

        # save dictionary to data store
        data_store.spec.test_case_dict = test_case_dict

    else:
        raise Exception("Csv file not found. Please check the table stated in the specification.")


@before_scenario
def before_scenario_hook(context):
    print("SCENARIO - START : " + context.scenario.name)

    # Mark Timestamp (this timestamp can be used in the string formatter)
    data_store.scenario.time = time.time()
    data_store.scenario.timestamp = str(int(data_store.scenario.time * 1000))


