import datetime
import requests
import logging

class CloudInterfaceModule:
    """
     CloudInterfaceModule class is to communicate with the web services

        attributes
        ----------
            This class having attributes
            method (str): ("get", "options", "head", "post", "put", "patch", or "delete").
            url (str): url name
            params (str): query parameters for request
            data (str): pass the data through request
            headers (str): request headers('accept', 'content-type', 'authorization',....)

        methods
        -------
            This class having two methods
            request(): sending api request to get the response
    """
    @staticmethod
    def log(s):
        logger = logging.getLogger(__name__)
        logger.info(s)

    def __init__(self):
        """
            Constructor method of the class CloudInterfaceModule.
        """
        self.log("Creating an instance of CloudInterfaceModule class")

    def request(self, method, url, params=None, data=None, headers=None):
        """
            method: ("GET", "OPTIONS", "HEAD", "POST", "PUT", "PATCH", or "DELETE").
            url: Base-url
            params (str): query parameters for request
            data (str): pass the data through request
            headers: request headers('Accept', 'Content-Type', 'Authorization',....)
            return (str): 'status_code & content of the Response & None'
        """
        try:
            # New session object is created using requests.Session()
            session = requests.Session()

            timestamp = str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))

            # HTTP request is constructed using the values of instance variables
            response = session.request(method=method, url=url, params=params,
                                       data=data, headers=headers)

            execution_time = response.elapsed.total_seconds()

            # Getting the status_code of the 'Response'
            actual_status_code = response.status_code

            # Getting the content of the 'Response'
            content = response.content

            # returns the status_code, content of the response
            return actual_status_code, content, execution_time, timestamp

        except requests.exceptions.RequestException as error:
            self.log(f"Exception occurred while making a request to"
                                   f" {url}. Error: {str(error)}")
            return None, None