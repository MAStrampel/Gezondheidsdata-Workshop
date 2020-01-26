#!/usr/bin/env python3

import time
import random
import hashlib
import shutil
import os
import signal
import sys
from ast import literal_eval

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

os.system('') #enable VT100 Escape Sequence for WINDOWS 10 Ver. 1607

def get_ip(command):
    print("Hostname           IP-adress")
    print("============================")
    print(command[1], "     51.91.18.131:51494\n")

def connect(command):
    print("Connecting to ", command[1], "..", sep="")
    temp = random.randint(3,7)
    for _ in range(temp):
        print("Establishing connection | ", end="\r")
        time.sleep(0.5)
        print("Establishing connection / ", end="\r")
        time.sleep(0.5)
        print("Establishing connection ——", end="\r")
        time.sleep(0.5)
        print("Establishing connection \\ ", end="\r")
        time.sleep(0.5)
    print(f"{bcolors.OKGREEN}Succesfully connected to {bcolors.BOLD}", command[1], f"{bcolors.ENDC}{bcolors.OKGREEN} at {bcolors.BOLD}", command[2], f"{bcolors.ENDC}{bcolors.OKGREEN}.{bcolors.ENDC}\n", sep="")

def packet_sniff():
    print("Sniffing for data..")
    rand = [random.randint(3, 13) for _ in range(5)]
    time.sleep(rand[0])
    print(f"\n{bcolors.OKGREEN}Found binary username segment:{bcolors.ENDC} 01100001 01100100 01101101")
    time.sleep(rand[1])
    print(f"{bcolors.OKGREEN}Found hexadecimal username segment:{bcolors.ENDC} 0x142")
    time.sleep(rand[2])
    print(f"\n{bcolors.OKGREEN}Found sha256 hash:{bcolors.ENDC} 88b1a67eeec1d71822a9666318ee4eb6c5836b93633b15648490278fd93f5deb")
    time.sleep(rand[3])
    print("\nSaving non-identifiable data to dump.txt\n")
    try:
	##########################
	# CHANGE FILEPATHS BELOW #
	##########################
        shutil.move("C:/.../Biotech/dump.txt", "C:/.../Biotech/Workshop/dump.txt")
    except:
        pass
    lines = open('dump.txt').readlines()
    random.shuffle(lines)
    open('dump.txt', 'w').writelines(lines)

    time.sleep(rand[4])

def bin_to_txt(binary):
    temp = " ".join(binary)
    binary = "".join(binary)
    binary = binary.strip()
    p = set(binary)
    if p == {'0', '1'} or p == {'0'} or p == {'1'}:
        decimal = ''.join(chr(int(binary[i*8:i*8+8],2)) for i in range(len(binary)//8))
        print(f"{bcolors.OKGREEN}Conversion succesful.{bcolors.ENDC}")
        print(temp, "==", decimal, "\n")
    else:
        print(f"{bcolors.FAIL}Conversion failed, input string not binary.{bcolors.ENDC}\n")

def hex_to_dec(hex):
    try:
        dec = literal_eval(hex)
        print(f"{bcolors.OKGREEN}Conversion succesful.{bcolors.ENDC}")
        print(hex, "==", dec, "\n")
    except:
        print(f"{bcolors.FAIL}Conversion failed, input string not hexadecimal.{bcolors.ENDC}\n")

def get_password(command):
    count = 0
    flag = 0

    try:
        passwords = open(command[1], "r")
    except:
        print(f"{bcolors.FAIL}File {bcolors.BOLD}'",command[1],f"'{bcolors.ENDC}{bcolors.FAIL} not found.{bcolors.ENDC}\n", sep="")
        return

    for word in passwords:
        enc_word = word.encode('utf-8')
        digest = hashlib.sha256(enc_word.strip()).hexdigest()
        count += 1

        if digest == command[2]:
            flag = 1
            print(f"\n{bcolors.OKGREEN}Password cracked:{bcolors.ENDC}", word, end="")
            print("Checked", count, "entries.\n")
            break

    if flag == 0:
        print(f"{bcolors.WARNING}Password not in wordlist.\n{bcolors.ENDC}")

def login():
    usr = input("\nUsername: ")
    psswrd = input("Password: ")
    print("\nAttempting login..")
    temp = random.random()*3
    time.sleep(temp)
    if usr == "adm322" and psswrd == "$dXqhASs.a23k.L/":
        print(f"{bcolors.OKGREEN}Login succesful.\n{bcolors.ENDC}")
        return True
    else:
        print(f"{bcolors.FAIL}Login failed, username or password incorrect. Please try again.\n{bcolors.ENDC}")
        return False

def lspre():
    print("~/ggd/files/regions/")
    print(f"{bcolors.OKBLUE}\nggdAmsterdam{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}ggdFlevoland{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}ggdGooiAndVecht{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}ggdHaaglanden{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}ggdHollandsMidden{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}ggdHollandsNoorden{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}ggdKennemerland{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}ggdNieuwegein{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}ggdNoordEnOostGelderland{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}ggdRotterdamRijnmond{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}ggdUtrecht{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}ggdZaanstreekWaterland\n{bcolors.ENDC}")

def lspost():
    print("~/ggd/files/regions/ggdAmsterdam/")
    print("")
    for i in range(100000, 2400000, 100000):
        print(f"{bcolors.OKBLUE}ggdAmsterdam_patient_recs_", i, f".xlsx{bcolors.ENDC}", sep="")

    print("")

def data_dl(command):
    print("Downloading ", command[1], "...", sep="")
    print("[                    ] 0%", end="\r")
    time.sleep(0.33)
    print("[====                ] 19%", end="\r")
    time.sleep(0.33)
    print("[========            ] 38%", end="\r")
    time.sleep(0.33)
    print("[============        ] 60%", end="\r")
    time.sleep(0.33)
    print("[================    ] 81%", end="\r")
    time.sleep(0.33)
    print("[====================] 100%", end="\r")
    print(f"\n{bcolors.OKGREEN}Download complete.\n{bcolors.ENDC}")
    try:
	##########################
	# CHANGE FILEPATHS BELOW #
	##########################
        shutil.move("C:/.../Biotech/ggdAmsterdam_patient_recs_1200000.xlsx", "C:/.../Biotech/Workshop/ggdAmsterdam_patient_recs_1200000.xlsx")
    except:
        pass

def helper():
    print(f"\n Command        | Usage ({bcolors.OKBLUE}blue{bcolors.ENDC} fields mandatory)         | Description")
    print("================|=======================================|===========================================================")
    print(f" bin_to_txt     | bin_to_txt {bcolors.OKBLUE}[binary]{bcolors.ENDC}                   | Converts given {bcolors.OKBLUE}[binary value]{bcolors.ENDC} to a string\n")
    print(f" cd             | cd {bcolors.OKBLUE}[destination]{bcolors.ENDC}                      | Changes current directory to {bcolors.OKBLUE}[destination]{bcolors.ENDC}\n")
    print(f" connect        | connect {bcolors.OKBLUE}[hostname] [IP-adress]{bcolors.ENDC}        | Connects to {bcolors.OKBLUE}[hostname]{bcolors.ENDC} at {bcolors.OKBLUE}[IP-adress]{bcolors.ENDC}\n")
    print(f" data_dl        | data_dl {bcolors.OKBLUE}[filename]{bcolors.ENDC} -f[from] -t[to]    | Download all data in {bcolors.OKBLUE}[filename]{bcolors.ENDC} between [from] and [to]\n")
    print(f" get_ip         | get_ip {bcolors.OKBLUE}[hostname]{bcolors.ENDC}                     | Gets the IP-adress of {bcolors.OKBLUE}[hostname]{bcolors.ENDC}\n")
    print(f" get_password   | get_password {bcolors.OKBLUE}[filename] [hash]{bcolors.ENDC}        | Find password using in {bcolors.OKBLUE}[filename]{bcolors.ENDC} using sha256 {bcolors.OKBLUE}[hash]{bcolors.ENDC}\n")
    print(f" help           | help                                  | Shows a list of valid commands and their usage\n")
    print(f" hex_to_dec     | hex_to_dec {bcolors.OKBLUE}[hexadecimal]{bcolors.ENDC}              | Converts given {bcolors.OKBLUE}[hexadecimal value]{bcolors.ENDC} to a decimal value\n")
    print(f" login          | login                                 | Logs into currently connected server's database\n")
    print(f" ls             | ls                                    | Lists all files and folder in current directory\n")
    print(f" packet_sniff   | packet_sniff                          | Sniffs currently connected server for data packets\n")
    print(f" quit           | quit                                  | Allows user to quit current program\n\n")

def quitter():
    while True:
        print("\nQuit the program?")
        temp = input("[y]es/[n]o: ")
        if temp == "yes" or temp == "y" or temp == "[y]es":
            # print("\nExit out of terminal?")
            # temp2 = input("[y]es/[n]o: ")
            # if temp2 == "yes" or temp2 == "y" or temp2 == "[y]es":
            #     os.kill(os.getppid(), signal.SIGHUP)
            # elif temp2 == "no" or temp2 == "n" or temp2 == "[n]o":
            #     quit()
            quit()
        elif temp == "no" or temp == "n" or temp == "[n]o":
            print("Quitting cancelled.\n")
            return
        print(f"{bcolors.WARNING}Invalid input.{bcolors.ENDC}")

def usage_incor(command):
    print(f"{bcolors.WARNING}Usage for {bcolors.BOLD}'", command[0], f"'{bcolors.ENDC}{bcolors.WARNING} command invalid. See 'help' for correct usage.\n{bcolors.ENDC}", sep="")



print("\nStarting password cracker..")
time.sleep(1)
print(f"{bcolors.OKGREEN}Done.\n{bcolors.ENDC}")
cdflag = 0
connect_flag = 0 # DONT FORGET TO SET BACK TO 0 AFTER TESTING
try:
    ##########################
    # CHANGE FILEPATHS BELOW #
    ##########################
    shutil.move("C:/.../Biotech/Workshop/dump.txt", "C:/.../Biotech/dump.txt")
except:
    pass
try:
    ##########################
    # CHANGE FILEPATHS BELOW #
    ##########################
    shutil.move("C:/.../Biotech/Workshop/ggdAmsterdam_patient_recs_1200000.xlsx", "C:/.../Biotech/ggdAmsterdam_patient_recs_1200000.xlsx")
except:
    pass

while True:
    cmd_found = 0
    command = [input("Command input: ")]
    command = (command[0].split())
    if command[0] == "get_ip" and len(command) != 2:
        usage_incor(command)
        cmd_found = 1
    elif command[0] == "get_ip" and command[1] == "server.ggd.nl":
        get_ip(command)
        cmd_found = 1
    elif command[0] == "get_ip":
        print(f"{bcolors.FAIL}Get ip failed, server {bcolors.BOLD}'", command[1], f"'{bcolors.ENDC}{bcolors.FAIL} not found.\n{bcolors.ENDC}", sep="")
        cmd_found = 1

    if command[0] == "connect" and len(command) != 3:
        usage_incor(command)
        cmd_found = 1
    elif command[0] == "connect" and connect_flag > 0:
        print(f"{bcolors.WARNING}Already connected to 'server.ggd.nl'.\n{bcolors.ENDC}")
        cmd_found = 1
    elif command[0] == "connect" and command[1] == "server.ggd.nl" and command[2] == "51.91.18.131:51494":
        connect(command)
        cmd_found = 1
        connect_flag = 1
    elif command[0] == "connect":
        print(f"{bcolors.FAIL}Failed to connect, make sure hostname and ip are correct.\n{bcolors.ENDC}")
        cmd_found = 1

    if command[0] == "packet_sniff" and len(command) != 1:
        usage_incor(command)
        cmd_found = 1
    elif command[0] == "packet_sniff" and connect_flag == 1:
        packet_sniff()
        cmd_found = 1
    elif command[0] == "packet_sniff" and connect_flag < 1:
        print(f"{bcolors.FAIL}Packet sniffing failed, not connected.\n{bcolors.ENDC}")
        cmd_found = 1

    if command[0] == "bin_to_txt" and len(command) == 1:
        usage_incor(command)
        cmd_found = 1
    elif command[0] == "bin_to_txt":
        bin_to_txt(command[1:])
        cmd_found = 1

    if command[0] == "hex_to_dec" and len(command) != 2:
        usage_incor(command)
        cmd_found = 1
    elif command[0] == "hex_to_dec":
        hex_to_dec(command[1])
        cmd_found = 1

    if command[0] == "get_password" and len(command) != 3:
        usage_incor(command)
        cmd_found = 1
    elif command[0] == "get_password" and command[1] == "dump.txt":
        get_password(command)
        cmd_found = 1
    elif command[0] == "get_password":
        print(f"{bcolors.FAIL}Get password failed, file {bcolors.BOLD}'",command[1],f"'{bcolors.ENDC}{bcolors.FAIL} not found.\n{bcolors.ENDC}", sep="")
        cmd_found = 1

    if command[0] == "login" and len(command) != 1:
        usage_incor(command)
        cmd_found = 1
    elif command[0] == "login" and connect_flag < 1:
        print(f"{bcolors.FAIL}Login failed, not connected.\n{bcolors.ENDC}")
        cmd_found = 1
    elif command[0] == "login" and connect_flag == 1:
        if login() == True:
            connect_flag = 2
        cmd_found = 1
    elif command[0] == "login" and connect_flag == 2:
        print(f"{bcolors.WARNING}Already logged in as 'adm322'.\n{bcolors.ENDC}")
        cmd_found = 1

    if command[0] == "ls" and len(command) != 1:
        usage_incor(command)
        cmd_found = 1
    elif command[0] == "ls" and connect_flag == 1:
        print(f"{bcolors.FAIL}Permission denied, not logged in.\n{bcolors.ENDC}")
        cmd_found = 1
    elif command[0] == "ls" and connect_flag == 0:
        print(f"{bcolors.FAIL}Listing failed, not connected.\n{bcolors.ENDC}")
        cmd_found = 1
    elif command[0] == "ls" and cdflag == 0:
        lspre()
        cmd_found = 1
    elif command[0] == "ls" and cdflag == 1:
        lspost()
        cmd_found = 1

    if command[0] == "cd" and len(command) != 2:
        usage_incor(command)
        cmd_found = 1
    elif command[0] == "cd" and connect_flag == 1:
        print(f"{bcolors.FAIL}Permission denied, not logged in.\n{bcolors.ENDC}")
        cmd_found = 1
    elif command[0] == "cd" and connect_flag == 0:
        print(f"{bcolors.FAIL}Listing failed, not connected.\n{bcolors.ENDC}")
        cmd_found = 1
    elif command[0] == "cd" and command[1] == "ggdAmsterdam":
        print("")
        cdflag = 1
        cmd_found = 1
    elif command[0] == "cd":
        print(f"{bcolors.FAIL}Directory change failed, directory {bcolors.FAIL}'", command[1], f"'{bcolors.ENDC}{bcolors.FAIL} not found.\n{bcolors.ENDC}", sep="")
        cmd_found = 1

    if command[0] == "data_dl" and len(command) not in [2, 4]:
        usage_incor(command)
        cmd_found = 1
    elif command[0] == "data_dl" and connect_flag == 1:
        print(f"{bcolors.FAIL}Permission denied, not logged in.\n{bcolors.ENDC}")
        cmd_found = 1
    elif command[0] == "data_dl" and connect_flag == 0:
        print(f"{bcolors.FAIL}Download failed, not connected.\n{bcolors.ENDC}")
        cmd_found = 1
    elif command[0] == "data_dl" and len(command) == 2:
        print(f"{bcolors.FAIL}Download failed, file too large.\n{bcolors.ENDC}")
        cmd_found = 1
    elif command[0] == "data_dl" and command[1] == "ggdAmsterdam_patient_recs_1200000.xlsx" and command[2] == "-f1165476" and command[3] == "-t1165606":
        data_dl(command)
        cmd_found = 1
    elif command[0] == "data_dl":
        print(f"{bcolors.FAIL}Download failed, could not download file with provided boundry flags.\n{bcolors.ENDC}")
        cmd_found = 1

    if command[0] == "help" and len(command) != 1:
        usage_incor(command)
        cmd_found = 1
    elif command[0] == "help":
        helper()
        cmd_found = 1

    if command[0] == "quit" and len(command) != 1:
        usage_incor(command)
        cmd_found = 1
    elif command[0] == "quit":
        quitter()
        cmd_found = 1

    if cmd_found == 0:
        print(f"{bcolors.WARNING}Invalid command, type {bcolors.BOLD}'help'{bcolors.ENDC}{bcolors.WARNING} for command list.\n{bcolors.ENDC}")
