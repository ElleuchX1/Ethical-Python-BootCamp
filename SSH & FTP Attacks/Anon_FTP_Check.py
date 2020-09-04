#! /usr/bin/env python3

import ftplib
def login(host):
    try:
        login_ftp=ftplib.FTP(host)
        ftp.login('anonymous','')
        
        ftp.quit()
        return '|+| Logged in as Anonymous'
    except:
        return '|-| Failed to login as Anonymous '

def main():
    host=''
    print('[------------------]')
    while host ==''
        host=input('Please Enter Target Host: ')
    print('[------------------]')
    print(Login(host))


if __name__ == "__main__":
    main()

