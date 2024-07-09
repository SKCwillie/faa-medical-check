import os
import time
from functions import login, parse_html

if __name__ == '__main__':
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')
    sleep = os.getenv('SLEEP')
    while True:
        try:
            html = login(email, password)
            parse_html(html)
            time.sleep(SLEEP * 60)
        except:
            print('Error running automation . . . ')
            print('Trying again later')
            time.sleep(SLEEP * 60)
