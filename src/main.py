from os import chdir
from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent
chdir(CURRENT_DIR)


def main():
    print("Hello World")


if __name__ == "__main__":
    main()
