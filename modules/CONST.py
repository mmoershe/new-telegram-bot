import os 
from dotenv import load_dotenv
load_dotenv()


#################
# ENV VARIABLES #
#################
token_env: str | None = os.getenv("TOKEN")
chat_id_env: str | None = os.getenv("CHAT_ID")
assert token_env is not None and chat_id_env is not None, "Couldn't find a valid TOKEN and/or valid CHAT_ID in the environment variables."

TOKEN: str = token_env
CHAT_ID: str = chat_id_env




###############
# DIRECTORIES #
###############
MODULES_DIRECTORY: str = os.path.dirname(__file__)
BASE_DIRECTORY: str = os.path.dirname(MODULES_DIRECTORY)
