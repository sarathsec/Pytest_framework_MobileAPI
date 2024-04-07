import subprocess
import sys
from datetime import datetime
import sys
from datetime import datetime

def run_test_suite(suite_names, service_names):
    timestamp = datetime.now().strftime('%Y_%m_%d_%H.%M.%S')
    path = r"D:\FRAMEWORK RELATED FOLDERS\PYTEST\Pytest_framework_MobileAPI\tests\reports"
    
    for suite_name in suite_names:
        for service_name in service_names:
            # Replace spaces in service name with underscores for a clean filename
            service_name_for_filename = service_name.replace(" ", "_")

            # Construct the filename with the suite name, service name, and timestamp
            filename = f"report_{suite_name}_{service_name_for_filename}_{timestamp}.html"
            full_path = path + "\\" + filename  # Construct the full path
            
            # Construct and execute the pytest command
            command = (
                f"pytest test_param.py -s --suite_name {suite_name} --service_name {service_name} "
                f"--html=\"{full_path}\""
            )
            subprocess.run(command, shell=True)



if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python run_suite.py <suite_names> <service_names>")
        sys.exit(1)

    suite_names_argument = sys.argv[1].split(",")  # Split suite_names by comma
    service_names_argument = sys.argv[2].split(",")  # Split service_names by comma

    run_test_suite(suite_names_argument, service_names_argument)



