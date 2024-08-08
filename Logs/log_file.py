import logging

def log_func():
    logger=logging.getLogger()
    filehandler=logging.FileHandler("..\\Logs\\current_logfile.log","w")
    formatter=logging.Formatter('%(asctime)s: %(levelname)s: %(module)s: %(funcName)s: %(message)s',datefmt='%d-%m-%Y  --  %I:%M:%S:%p')
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    logger.setLevel(logging.DEBUG)
    return logger