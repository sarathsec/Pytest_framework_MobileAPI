"""
    logging_module.py
    =================
    This module provides a class for logging modules.

    copyright: (c) 2023 by EFICAA_ENSMART_Solutions.
"""
import logging


class LoggingModule:
    """
        This class has related all logging modules
    """

    def __init__(self, log_file):
        """
            Initializes a LoggingModule instance.

            log_file: A string representing the file path where logs should be saved.
        """
        self.log_file = log_file
        self.logging = logging

    def start_logs(self, log_file):
        """
            Starts logging and returns a logger object.

            log_file: A string representing the file path where logs should be saved.
            return: A logger object.
        """
        # Create a logger instance
        logger = self.logging.getLogger()

        # Set the logging level to INFO
        logger.setLevel(self.logging.INFO)

        # Create a FileHandler instance to write the log messages to a file
        file_handler = self.logging.FileHandler(log_file)

        # Create a Formatter instance to format the log messages
        formatter = self.logging.Formatter('/ %(asctime)s - %(levelname)s - %(message)s')

        # Set the Formatter instance on the FileHandler instance
        file_handler.setFormatter(formatter)

        # Add the FileHandler instance to the logger instance
        logger.addHandler(file_handler)

        return logger, self.logging, file_handler

    def stop_logs(self, logger, file_handler):
        """
            Stops logging and shuts down the log file.

            param logger: A logger object.
            param file_handler: A FileHandler object.
        """
        logger.removeHandler(file_handler)

        # shutdown the log file after completion logs
        self.logging.shutdown()
