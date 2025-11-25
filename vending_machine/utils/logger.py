import datetime

class Logger:
    @staticmethod
    def log(message: str):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[ЛОГ {timestamp}] {message}")
