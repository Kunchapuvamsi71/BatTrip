import os
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

ENV_FILE = os.path.join(BASE_DIR, ".env")

load_dotenv(ENV_FILE)


class Config:
    MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_USER = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
    MYSQL_DATABASE = os.getenv(
        "MYSQL_DATABASE",
        "battrip_spiderroam"
    )
    MYSQL_PORT = int(
        os.getenv("MYSQL_PORT", "3306")
    )
