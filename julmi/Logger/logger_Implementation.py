import logging

# Create a logger
import logging

def setup_logger(name="CustomLogger", log_file=r"julmi\Logger\app.log", level=logging.DEBUG):
    """
    Sets up a logger with the specified name, log file, and logging level.

    Args:
        name (str): Name of the logger.
        log_file (str): File to log messages to.
        level (int): Logging level (e.g., logging.INFO, logging.DEBUG).

    Returns:
        logging.Logger: Configured logger instance.
    """
    # Create a logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create a file handler to log messages to a file
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(level)

    # Create a console handler to log messages to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)

    # Define a formatter for the log messages
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Add the formatter to the handlers
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

def stop_logger(logger):
    """
    Stops the logger and removes all handlers.

    Args:
        logger (logging.Logger): Logger instance to stop.
    """
    for handler in logger.handlers[:]:
        handler.close()
        logger.removeHandler(handler)

# Example usage
logger = setup_logger()

logger.info("Logger is set up and ready to use.")
logger.debug("Logger is set up and ready to use.")
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')

stop_logger(logger)