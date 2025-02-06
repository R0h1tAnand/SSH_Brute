# SSH_Brute

# SSH Brute Force Tool

This is a simple SSH brute force tool written in Python that attempts to guess the SSH login password of a target machine. The program uses a list of possible passwords (provided in a wordlist file) and tries each password until it successfully logs in or runs out of options.

## Requirements

- Python 3.x
- `paramiko` library
- `pwn` library

You can install the required libraries using the following command:

```bash
pip install paramiko pwntools
```

Example Command:

```bash
python ssh_bruteforce.py -i 192.168.1.100 -u root -w /path/to/password_list.txt
```
