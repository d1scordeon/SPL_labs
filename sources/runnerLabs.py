import logging
from sources.lab1 import lab1
from sources.lab2 import lab2
from sources.lab3 import lab3
from sources.lab4 import lab4
from sources.lab5 import lab5
from sources.lab6 import lab6
from sources.lab7 import lab7
from sources.lab8 import lab8

def init_logging():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s', filename='app.log', filemode='w')

def main():
    init_logging()
    logging.info("Application starting...")

    try:
        # Running each lab's main function
        lab1.main()
        lab2.main()
        lab3.main()
        lab4.main()
        lab5.main()
        lab6.main()
        lab7.main()
        lab8.main()

        logging.info("All labs executed successfully.")
    except Exception as e:
        logging.critical("Unhandled exception while running application: %s", e)

    logging.info("Application stopped")

if __name__ == "__main__":
    main()
