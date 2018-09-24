from dotenv import load_dotenv
import os

# LOAD ENV file
load_dotenv()


REDIS_PASSWORD=os.getenv('REDIS_PASSWORD')
REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_DEFAULT_DB = os.getenv('REDIS_DEFAULT_DB')
REDIS_PORT = os.getenv('REDIS_PORT')
