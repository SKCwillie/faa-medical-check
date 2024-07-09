import os
import time
from dotenv import load_dotenv
from functions import login, parse_html

if __name__ == '__main__':
    load_dotenv()
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')

    while True:
        try:
            html = login(email, password)
            parse_html(html)
            time.sleep(30 * 60)
        except:
            print('Error running automation . . . ')
            print('Trying again later')
            time.sleep(30 * 60)
