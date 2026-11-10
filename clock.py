"""Выводит текущее время в терминале. Остановка: Ctrl+C."""
import time
from datetime import datetime


def main() -> None:
    try:
        while True:
            now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
            print(f"\r{now}", end="", flush=True)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nВыход.")


if __name__ == "__main__":
    main()
