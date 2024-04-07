# import pytest
# import tabulate
# from tabulate import tabulate
# import logging
# from cloud_interface.cloud_interface_module import CloudInterfaceModule

# logger = logging.getLogger(__name__)
# base_url = "http://172.16.15.24:8083"

# def test_par(tests_to_execute):
#     logger.info(tests_to_execute)
#     logger.info("Test_parameters")
#      # Format the test parameters as a table
#     table_data = [
#         ("Parameter", "Value"),
#         ("testcase_id", tests_to_execute.get("testcase_id", "")),
#         ("endpoint", tests_to_execute.get("endpoint", "")),
#         ("operation", tests_to_execute.get("operation", "")),
#         ("headers", str(tests_to_execute.get("headers", ""))),
#         ("query_parameters", str(tests_to_execute.get("query_parameters", ""))),
#         ("expected_output", str(tests_to_execute.get("expected_output", ""))),
#     ]

#     # Log the table
#     logger.info("\n" + tabulate(table_data, headers="firstrow", tablefmt="grid"))
    
#     endpoint = f"{base_url}{tests_to_execute['endpoint']}"
#     logger.info(f"Endpoint is {endpoint}")
#     cloud_intf_module = CloudInterfaceModule()
#     [actual_status_code, content, execution_time, timestamp] = cloud_intf_module.request(
#                                 method=tests_to_execute["operation"],
#                                 url=endpoint, 
#                                 params={'port': tests_to_execute["query_parameters"]["port"]})
    
#     remarks = (
#         "PASS" if str(tests_to_execute.get("expected_output", {}).get("status_code", "")) == actual_status_code else "FAIL"
#         )
    
#     table_data = [
#         ("Parameter", "Value"),
#         ("testcase_name",tests_to_execute.get("testcase_name","")),
#         ("testcase_id", tests_to_execute.get("testcase_id", "")),
#         ("endpoint", tests_to_execute.get("endpoint", "")),
#         ("operation", tests_to_execute.get("operation", "")),
#         ("headers", str(tests_to_execute.get("headers", ""))),
#         ("query_parameters", str(tests_to_execute.get("query_parameters", ""))),
#         ("expected_output", str(tests_to_execute.get("expected_output", ""))),
#         ("actual_status_code",str(actual_status_code)),
#         ("REMARKS",remarks),
#         ("execution_time",execution_time),
#         ("timestamp",timestamp),
#     ]

#     # Log the table
#     logger.info("\n" + tabulate(table_data, headers="firstrow", tablefmt="grid"))

#     logger.info("Response_content")
    
#     logger.info(content)
#     assert 1 == 1
    
    
    
# # Perform assertions
#     expected_status_code = int(tests_to_execute["expected_output"]["status_code"])
#     assert expected_status_code == actual_status_code,f"Expected status code: {expected_status_code}, Actual status code: {actual_status_code}"
    
#     remarks = (
#         "PASS" if expected_status_code == actual_status_code else "FAIL"
#         )
#     table_data = [
#         ("Parameter", "Value"),
#         ("testcase_name",tests_to_execute.get("testcase_name","")),
#         ("testcase_id", tests_to_execute.get("testcase_id", "")),
#         ("endpoint", tests_to_execute.get("endpoint", "")),
#         ("operation", tests_to_execute.get("operation", "")),
#         ("headers", str(tests_to_execute.get("headers", ""))),
#         ("query_parameters", str(tests_to_execute.get("query_parameters", ""))),
#         ("expected_output", str(tests_to_execute.get("expected_output", ""))),
#         ("actual_status_code",str(actual_status_code)),
#         ("REMARKS",remarks),
#         ("execution_time",execution_time),
#         ("timestamp",timestamp),
#     ]

#     # Log the table
#     logger.info("\n" + tabulate(table_data, headers="firstrow", tablefmt="grid"))

#     logger.info("Response_content")
    
#     logger.info(content)
#     assert 1 == 1
    
###############################################################################################################
import pytest
import tabulate
from tabulate import tabulate
import logging
from cloud_interface.cloud_interface_module import CloudInterfaceModule

logger = logging.getLogger(__name__)
base_url = "http://172.16.15.24:8083"

def test_par(tests_to_execute):
    logger.info(tests_to_execute)
    logger.info("Test_parameters")
    print("MY INPUT DATA")
    # Format the test parameters as a table
    table_data = [
        ("Parameter", "Value"),
        ("MY INPUT DATA",""),
        ("testcase_id", tests_to_execute.get("testcase_id", "")),
        ("testcase_name", tests_to_execute.get("testcase_name", "")),
        ("endpoint", tests_to_execute.get("endpoint", "")),
        ("operation", tests_to_execute.get("operation", "")),
        ("headers", str(tests_to_execute.get("headers", ""))),
        ("query_parameters", str(tests_to_execute.get("query_parameters", ""))),
        ("expected_output", str(tests_to_execute.get("expected_output", ""))),
    ]

    # Log the table
    logger.info("\n" + tabulate(table_data, headers="firstrow", tablefmt="grid"))
    
    endpoint = f"{base_url}{tests_to_execute['endpoint']}"
    logger.info(f"Endpoint is {endpoint}")
    
    cloud_intf_module = CloudInterfaceModule()
    [actual_status_code, content, execution_time, timestamp] = cloud_intf_module.request(
        method=tests_to_execute["operation"],
        url=endpoint, 
        params={'port': tests_to_execute["query_parameters"]["port"]}
    )
    
    remarks = "PASS" if str(actual_status_code) == str(tests_to_execute.get("expected_output", {}).get("status_code", "")) else "FAIL"
    
    # Log the table before the assertion
    table_data = [
        ("Parameter", "Value"),
        ("MAIN RESULTS AFTER ASSERTION",""),
        ("service_name",tests_to_execute.get("service_name","")),
        ("testcase_name", str(tests_to_execute.get("testcase_name", ""))),
        ("Hyperlink",endpoint),
        ("testcase_id", tests_to_execute.get("testcase_id", "")),
        ("endpoint", tests_to_execute.get("endpoint", "")),
        ("operation", tests_to_execute.get("operation", "")),
        ("headers", str(tests_to_execute.get("headers", ""))),
        ("query_parameters", str(tests_to_execute.get("query_parameters", ""))),
        ("expected_output", str(tests_to_execute.get("expected_output", ""))),
        ("actual_status_code", str(actual_status_code)),  # Include actual_status_code in the table
        ("REMARKS", remarks),
        ("execution_time", execution_time),
        ("timestamp", timestamp),
    ]

    # Log the table
    logger.info("\n" + tabulate(table_data, headers="firstrow", tablefmt="grid"))

    # Perform assertions
    expected_status_code = int(tests_to_execute["expected_output"]["status_code"])
    assert actual_status_code == expected_status_code, f"Expected status code: {expected_status_code}, Actual status code: {actual_status_code}"

    logger.info("Response_content")
    logger.info(content)

