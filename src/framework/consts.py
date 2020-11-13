from datetime import timedelta
from pathlib import Path

SERVER_RUNNING_BANNER = """
+----------------------------------------+
|             SERVER WORKS!              |
+----------------------------------------+

Visit http://{host}:{port}

..........................................
"""

dir_static = (Path(__file__).parent.parent / "static").resolve()
dir_db = (Path(__file__).parent.parent.parent / "db").resolve()
file_user_db = (dir_db / "db_users.json").resolve()

USER_COOKIE = "z37user"

USER_TTL = timedelta(minutes=5)

DATE_TIME_FMT = "%Y-%m-%d %H:%M:%S"
