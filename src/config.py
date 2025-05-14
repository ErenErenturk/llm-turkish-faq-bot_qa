import os

MODE = os.getenv("APP_MODE", "dev")

def log(message):
    if MODE == "dev":
        print(f"[LOG] {message}")
