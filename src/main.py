# custom libraries
from lib.app import App

# builtin libraries
import sys
import logging

def main():
    if len(sys.argv) >= 2:

        # remove the file name
        sys.argv.pop(0)
        
        # create an app    
        app = App()        

        # send command to app
        return print(app.app(sys))

    else:
        return print('try: python main.py help')


if __name__ == '__main__':

   logging.basicConfig(filename='wb.log', level=logging.ERROR)

   try:
        main()
   except:
        logging.error("Exception occurred", exc_info=True)
        raise
