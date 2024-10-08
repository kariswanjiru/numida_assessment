import logging

# Configure the logging system
logging.basicConfig(
    level=logging.DEBUG,  # Set the lowest severity level to DEBUG
    format="%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),  # Log to a file named 'app.log'
        logging.StreamHandler(),  # Also log to the console
    ],
)


def get_logger(name):
    """
    Create and return a logger with the specified name.

    Parameters
    ----------
    name : str
        The name of the logger, typically __name__ from the calling module.

    Returns
    -------
    logger
        Configured logger instance.
    """
    return logging.getLogger(name)
