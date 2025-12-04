from dotenv import load_dotenv
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv()


def env(key, default=None):
    return os.getenv(key, default)
