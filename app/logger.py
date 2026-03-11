import logging

def setup_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    #Logger for console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    #Logger for file
    file_handler = logging.FileHandler('app.log', mode = 'w')
    file_handler.setLevel(logging.DEBUG)

    #Format for logs
    formatter = logging.Formatter(
        '{asctime} - {levelname} - {message}',
        style = '{',
        datefmt = '%Y-%m-%d %H:%M'
    )
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    #Avoid duplicate logs (Since handlers get added every time application starts up)
    if not logger.handlers:
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
