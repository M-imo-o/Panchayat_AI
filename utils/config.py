import os
from dotenv import load_dotenv


load_dotenv()


GROQ_API_KEY = os.getenv("GROQ_API_KEY")


DATA_PATH = "Data/data_set.txt"


MODEL_NAME = "llama-3.1-8b-instant"