"""
Central configuration module.
Reads BOT_TOKEN, ADMIN_ID, STATS_PATH from environment variables
or from a .env file at project root.
"""

from pathlib import Path
import os
from dotenv import load_dotenv

# load .env beside README / requirements.txt
project_root = Path(__file__).resolve().parent.parent
load_dotenv(project_root / ".env")

TOKEN: str = os.getenv("BOT_TOKEN", "")
if not TOKEN:
    raise RuntimeError("BOT_TOKEN not set in environment or .env")

ADMIN: int = int(os.getenv("ADMIN_ID", "0"))
STATS: str = os.getenv("STATS_PATH", "../stats.json")

__all__ = ["TOKEN", "ADMIN", "STATS"]
