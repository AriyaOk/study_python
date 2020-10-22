from pathlib import Path

SERVER_RUNNING_BANNER = """
+----------------------------------------+
|             SERVER WORKS!              |
+----------------------------------------+

Visit http://{host}:{port}

..........................................
"""

dir_static = (Path(__file__).parent.parent / "static").resolve()
file_scc = "styles.css"
file_logo = "ariyaOk.gif"  # "logo.png"
file_index = "index.html"
