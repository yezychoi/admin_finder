#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

class AdminFinder:
    def __init__(self, url, count=10000, file="admin_page.txt"):
        self.url = url
        self.count = count
        self.file = file

    def run(self):
        pages = open(self.file, 'r', encoding="utf-8").readlines()
        pages = pages[:self.count]
        result = {}
        for page in pages:
            res = self.check_page(url, page.strip())
            if res not in result:
                result[res] = []
            result[res].append(url + '/' + page.strip())

        result = dict(sorted(result.items()))
        with open("result.txt", "w", encoding="utf-8") as f:
            for key in result:
                f.write("status code: " + str(key) + "\n")
                f.write("-" * 30 + "\n")
                f.write("\n".join(result[key]))
                f.write("\n")

    def check_page(self, url: str, page):
        try:
            url = url + '/' + page
            res = requests.get(url, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}).status_code
            return res
        except Exception as e:
            print(e)
            exit()

print('\033[35m ' + 46 * '-' + '\033[0m')
print('\033[35m __  __       __    ____     __  __    \033[0m')
print('\033[35m/\\ \\/\\ \\    /\'__`\\ /\\_ ,`\\  /\\ \\/\\ \\   \033[0m')
print('\033[35m\\ \\ \\_\\ \\  /\\  __/\\/_/  /_ \\ \\ \\_\\ \\  \033[0m')
print('\033[35m \\/`____ \\ \\ \\____\\  /\\____\\ \\/`____ \\ \033[0m')
print('\033[35m  `/___/> \\ \\/____/  \\/____/  `/___/> \\ \033[0m')
print('\033[35m     /\\___/                      /\\___/ \033[0m')
print('\033[35m     \\/__/                       \\/__/  \033[0m')
print('\033[35m ' + 46 * '-' + '\033[0m')
print('                            ')
url = input('\033[33m  ✧ URL (http(s)://example.com) ➳♡゛\033[0m')
# 아냐 눈나의 AdminFinder를 객체화 합니다(객체화시 url 값을 인자로 전달,나머지 매개변수 2개는 디폴트값 있음 헤으응...)
anya_machine = AdminFinder(url, 100)
print('                            ')
anya_machine.run()
print('\033[36m ˚✧₊⁎ Save result.txt ⁎⁺˳✧˚\033[0m')
print('\033[36m ✎﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏\033[0m')
print()
