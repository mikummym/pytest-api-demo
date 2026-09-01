import os


BASE_URL = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com").rstrip("/")
TIMEOUT = float(os.getenv("API_TIMEOUT", "10"))
