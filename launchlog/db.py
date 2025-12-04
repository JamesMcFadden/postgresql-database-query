# launchlog/db.py (psycopg 3 version)
import os

import psycopg
from psycopg.rows import dict_row


def get_connection():
    conn = psycopg.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
        dbname=os.getenv("DB_NAME", "launchdb"),
        user=os.getenv("DB_USER", "launchuser"),
        password=os.getenv("DB_PASSWORD", "launchpass"),
        row_factory=dict_row,  # rows behave like dicts: row["mission_name"]
    )
    return conn
