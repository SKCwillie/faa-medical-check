import os
from dotenv import load_dotenv
from functions import login, parse_html

if __name__ == '__main__':
    load_dotenv()
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')

    try:
        html = login(email, password)
        parse_html(html)
    except:
        print('Error running automation . . . ')
        print('Trying again later')
