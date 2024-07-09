from browser import get_browser
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


def login(username, password):
    # Create Browser
    browser = get_browser()

    # Go to Disclaimer Page
    url = 'https://medxpress.faa.gov/MedXpress/Disclaimer.aspx'
    browser.get(url)

    # Disclaimer Page
    accept_button = browser.find_element(By.ID, 'ContentPlaceHolder1_btnAccept')
    accept_button.click()

    # Login Page
    email_field = browser.find_element(By.ID, 'txtUsername')
    email_field.send_keys(username)
    password_field = browser.find_element(By.ID, 'txtPassword')
    password_field.send_keys(password)
    login_button = browser.find_element(By.ID, 'ContentPlaceHolder1_btnLogin')
    login_button.click()

    # Terms of Service Page
    accept_box = browser.find_element(By.ID, 'ContentPlaceHolder1_ChkToSAccept')
    accept_box.click()
    submit_button = browser.find_element(By.ID, 'ContentPlaceHolder1_btnSubmit')
    submit_button.click()

    # FAA MedXPress Home
    app_status = browser.find_element(By.ID, 'lnk_ApplicationStatus')
    app_status.click()
    return browser.page_source


def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    try:
        in_review = soup.find('div', {'id': 'ContentPlaceHolder1_spInReview'})
        is_completed = soup.find('div', {'id': 'ContentPlaceHolder1_icCompleted'})
        faa_correspondence = soup.find('div', {'id': 'divMailedCorrespondence'})
        print('\n'*12)
        if 'action required' in str(html):
            print('Action may be needed; check status!')
        if 'underline' in str(in_review):
            print('Still In Review . . .')
        if 'underline' in str(is_completed):
            print('Medical may be completed; check status!')
        if 'table' in str(faa_correspondence):
            print('FAA may have sent a response; check status!')

    except:
        print('Error parsing HTML . . .')
        print('Trying again later.')
