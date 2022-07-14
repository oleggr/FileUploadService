import os
from datetime import datetime


def getCurrDateAndTime():
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


def getCurrDate():
    return datetime.now().strftime("%Y-%m-%d")


LOGS_FOLDER = 'logs/'


class FileController:

    @staticmethod
    def _createPath(filepath: str):
        try:
            os.makedirs(os.path.dirname(filepath))
        except OSError as error:
            print("Error while creating path to log file", error)

    @staticmethod
    def writeToFile(filepath: str, message):
        if not os.path.exists(os.path.dirname(filepath)):
            FileController._createPath(filepath)

        if isinstance(message, str):
            FileController._writeString(filepath, message)
        elif isinstance(message, list):
            FileController._writeArray(filepath, message)

    @staticmethod
    def _writeString(filepath: str, message: str):
        with open(filepath, 'a', encoding='utf-8') as file:
            file.write(message + '\n')

    @staticmethod
    def _writeArray(filepath: str, message: list):
        with open(filepath, 'a') as file:
            for x in message:
                file.write(x)


class logger:

    log_name_pattern = 'logfile_%s.log'

    @staticmethod
    def info(event: str):
        """Write log with info severity.

        @param event Occurred event description.
        """
        message = "INFO | " + getCurrDateAndTime() + " | " + event
        print(message)
        FileController.writeToFile(logger.getLogFilename(), message)

    @staticmethod
    def alert(event: str):
        """Write log with alert severity.

        @param event Occurred error description.
        """
        message = "ALERT | " + getCurrDateAndTime() + " | " + event
        print(message)
        FileController.writeToFile(logger.getLogFilename(), message)

    @staticmethod
    def getLogFilename():
        """Construct log filename by pattern and date."""
        return LOGS_FOLDER + logger.log_name_pattern % getCurrDate()
