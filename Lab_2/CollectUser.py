# -*- coding: cp1251 -*-

import lxml
import urllib.request
import requests
from bs4 import BeautifulSoup

parser_result = u'����-���'
print(type(parser_result))
BASE_URL = 'http://www.weblancer.net/projects/'

def main():
    #proxy = {'http': 'http://102.32.3.1:8080',
    #        'https': 'http://102.32.3.1:4444'}
    #response = requests.get('http://devacademy.ru/', proxies=proxy)

    response = requests.get('http://www.metal-tracker.com')

    # �����
    print(response.status_code)  # ��� ������
    print(response.headers)  # ��������� ������
    print(response.content)  # ���� ������

    # ������
    print(response.request.headers)  # ��������� ������������ � ��������
    r = requests.get('http://www.metal-tracker.com/user/login.html', auth=('Plag_test', 'asdfghjkl'))
    print(r.status_code)
    #print(r.headers['content-type'])
    print(r.encoding)
    print(r.text)
    with requests.Session() as s:
        s.get('http://httpbin.org/get')
    #print(r.json())

if __name__ == '__main__':
    main()