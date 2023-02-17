# custom libraries
from lib import app

# builtin libraries
import sys


def main():
    if len(sys.argv) >= 2:

        # remove the file name
        sys.argv.pop(0)

        # send command to app
        return print(app.app(sys))

    else:
        return print('try: python main.py help')


if __name__ == '__main__':
    main()
