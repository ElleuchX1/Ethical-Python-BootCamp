#!/usr/bin/env python  
from sty import fg
import pexpect # https://pexpect.readthedocs.io/en/stable/index.html

# This script works only on linux. 
# https://pexpect.readthedocs.io/en/stable/overview.html#pexpect-on-windows
# pexpect.spawn and pexpect.run() are not available on Windows, as they rely on Unix
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
            child.expect(['#','/$']) # Add here whatever you need  ( '<' '<<'  )
            return child           
        else:
            print(fg.red+'|-| Opps, Something went wrong.. '+fg.rs) 
            exit(0)
    else:
        print(fg.red+'|-| Opps, Something went wrong.. '+fg.rs) 
        exit(0)   
def commands(child,ComString):
    child.sendline(ComString)
    child.expect(['#','/$']) # Add here whatever you need  ( '<' '<<'  )
    print(child.before)   
def main():
    print('|-------------------------------------------|')
    host,user,pw='','',''
    while host == '' or user == '' or pw ==''
        host=input('Enter the Target Host: ')
        user=input('Enter the Target User: ')
        pw=input('Enter the Target Password: ')
    print('|-------------------------------------------|')
    shell=connect2SSH(host,user,pw)
    commands(shell,'<Command1 ; Command2; ... >')
if __name__ == "__main__":
    main()
    
