import pytest
import yaml

def pytest_addoption(parser):
    parser.addoption("--suite_name", action="store", default="")
    parser.addoption("--service_name", action="store", default="")

def get_test_cases(service_name, suite_name, test_case_name=None):
    suite_file_path = f"D:\\FRAMEWORK RELATED FOLDERS\PYTEST\\Pytest_framework_MobileAPI\\test_data\\{suite_name}.yaml"
    tests_file_path = "D:\\FRAMEWORK RELATED FOLDERS\PYTEST\\Pytest_framework_MobileAPI\\test_data\\test.yaml"
    with open(suite_file_path, "r") as suite_test_cases:
        if test_case_name is None:
            suite_data = yaml.safe_load(suite_test_cases)
            test_case_list = suite_data["tests"][service_name]
            tests_in_service = None
            with open(tests_file_path, "r") as test_cases:
                test_data = yaml.safe_load(test_cases)
                tests_in_service = test_data["tests"][service_name]  # getting the 13 testcases of the specified Service name
            tests_to_execute = []
            for test_case_name in tests_in_service.keys():
                if test_case_name in test_case_list:
                    tests_to_execute.append(tests_in_service[test_case_name])
            return tests_to_execute
        if service_name == "" and suite_name == "":
            suite_data = yaml.safe_load(suite_test_cases)
            return suite_data["tests"]

def pytest_generate_tests(metafunc):
    suite_name = metafunc.config.getoption("--suite_name")
    service_name = metafunc.config.getoption("--service_name")
    print(f"Entered suite name is {suite_name} and service name is {service_name}")
    if "tests_to_execute" in metafunc.fixturenames:
        tests = get_test_cases(service_name, suite_name)
        metafunc.parametrize("tests_to_execute", tests)

    

