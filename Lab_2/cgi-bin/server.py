import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

dir = 'C:\\University\\Web\\Lab_2\\'  # место, где находятся файлы html и подкаталог cgi-bin
port = 8080
os.chdir(dir)  # перейти в корневой каталог HTML
httpd = ("", port)  # имя хоста и номер порта
httpd = HTTPServer(httpd, CGIHTTPRequestHandler)
httpd.serve_forever()  # запустить как бесконечный фоновый процесс