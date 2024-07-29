from dotenv import load_dotenv
import os

environment = {}


def load_environment():
    # load enviroment
    load_dotenv()

    environment["TIMEOUT"] = os.getenv("TIMEOUT")
    environment["LOG_LEVEL"] = 0 if os.getenv("LOG_LEVEL") is None else int(os.getenv("LOG_LEVEL"))

    environment["CVC5_PATH"] = os.getenv("CVC5_PATH")



    pass