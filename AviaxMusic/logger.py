import logging

def LOGGER(name=None):
    return logging.getLogger(name or "AviaxMusic")
