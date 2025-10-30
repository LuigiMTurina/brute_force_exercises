# Santander/DIO Cybersecurity Bootcamp - Pentest & Malware Dev Labs
In this repository I show the initial results of my studies on the Santander and DIO Cibersecurity Bootcamp, completed in 2025\

------------------------------------------------------------------

# 1. Security and pentesting

**Lab Environment**\
**-->** Attacker Machine: Kali Linux (IP: 192.168.56.103)\
**-->** Target Machine: Metasploitable 2 (IP: 192.168.56.102)

**Tools Used**\
**-->** nmap\
**-->** Enum4linux\
**-->** Medusa\
**-->** FTP & smbclient\

------------------------------------------------------------------

**There are a total of three exercises:**\
**-->** FTP service attack\
**-->** HTTP website attack\
**-->** SMB service attack\

**All of them have followed a similar process:**\
**-->** Enumeration\
**-->** Brute Force Attack with Medusa\

## 1.1 FTP ATTACK
   
### 1.1.1 ENUMERATION: Searching for available services"

**Method:** Nmap\
**Code:** `nmap -sV -p 21,22,80,445,139 192.168.56.102`

> In this step I identified which services and ports were open for an attack, using the flag "sV" for identify the version of each service, and the flag "p" to select which ports I wanted to analyse

### 1.1.2 WORDLISTS: Creating the wordlists

**Method:** Echo\
**Code:** `echo -e 'user\nmsfadmin\nadmin\nroot\nadministrator' > users.txt`

> After it, I created the wordlists that were used by Medusa to try an access, giving to it the list of users and passwords that I wanted for it to use

### 1.1.3 ATTACK: Trying the access with Medusa

**Method:** Medusa\
**Code:** `medusa -h 192.168.56.102 -U users.txt -P pass.txt -M ftp -t 6`

> Next, I executed the brute-force attack using Medusa giving the list of users (flag "U"), the passwords (flag "P") and the target service (flag "M")

### 1.1.4 ACCESS: Using the results

**Method:** FTP\
**Code:** `ftp 192.168.56.102`

> In the end, I used the result found by Medusa to access the FTP service, giving the right user and password\
![Linux terminal with access to ftp service](https://github.com/LuigiMTurina/brute_force_exercises/blob/master/ftp_attack/ftp_login.png)

## 1.2 HTTP Website Attack

### 1.2.1 ACCESS: Analyzing the website

**Link:** 192.168.56.102/dvwa/login.php

> Opening the website by the link, I used the inspect mode, and navigated to the Network tab, to understand the data that I needed to perform the login\
![DVWA website with login refused](https://github.com/LuigiMTurina/brute_force_exercises/blob/master/dvwa_attack/dvwa_failed.png)

## 1.2.2 WORDLISTS: Creating the wordlists

**Method:** Echo

> I created the wordlists to use with Medusa and try the login

## 1.2.3 ATTACK: Trying the access

**Method:** Medusa\
**Code:** 
```
medusa -h 192.168.56.102 -U dvwa_users.txt -P dvwa_pass.txt -M http \
-m PAGE: '/dvwa/login.php/' \
-m FORM: 'username=^USER^&password=^PASS^&login=Login' \
-m FAIL: 'Login failed' \
-m SUCCESS: 'Welcome' -t 6
```

> I directioned the Medusa to attack the HTTP service (flag "M"), providing the SITE targeted, the FORM data and the FAIL signal ("m" flags)

## 1.2.4 ACCESS: Entering into the panel

> After get the login data, I finally got into the administrative pannel\
![Successful login at the DVWA website](https://github.com/LuigiMTurina/brute_force_exercises/blob/master/dvwa_attack/dvwa_login.png)

## 1.3 SMB Attack

### 1.3.1 Enumeration: Enumerating the users

**Method:** Enum4linux\
**Code:** `enum4linux -a 192.168.56.102`

> Here, despite of enumerating the services, I needed to enumerate the users, so I used the Enum4linux testing all of the forms os enumerating (flag "a")

### 1.3.2 WORDLISTS: Creating the wordlists

**Method:** Echo

> Knowing about the users found by Enum4linux, I created the wordlist of users with the names founded, and also creating a wordlist for the passwords

### 1.3.3 SPRAYING: Spraying the password

**Method:** Medusa\
**Code:** `medusa -h 192.168.56.102 -U smb_users.txt -P smb_pass.txt -M smbnt -t 2 -T 50`

> I realized the password spraying with Medusa, focusing on the SMB service, and obtaining the correct passwords to access

### 1.3.4 ACCESS: Entering at the service

**Method:** SMB CLient\
**Code:** `smbclient -L //192.168.56.102 -U msfadmin`

> I entered at the SMB service with the client, giving the user founded by the Enum4linux (flag "U"), obtaining access\
![Access to the SMB service](https://github.com/LuigiMTurina/brute_force_exercises/blob/master/pass_spray_attack/spray_login.png)\


------------------------------------------------------------------

# 2. Malware and Keylogger programming

**Tools Used**\
**-->** VS Code\
**-->** Python\

------------------------------------------------------------------

**There are a total of two exercises:**\
**-->** Malware programming\
**-->** Keylogger programming\

## 2.1 Malware

---
**DISCLAIMER: This code was developed for educational purposes only, as part of my cybersecurity studies. It should not be used for malicious activities. I am not responsible for any misuse of this code.**
---

### 2.1.1 Library import: Starting the code 

> I started importing the cryptography.fernet library at the VS Code terminal, needed to the cryptographing process

### 2.1.2 Listing the functions: Creating the program logic

> After it, I created the program logic by writing the functions\
> `gerar_chave`: Function to generate the decryption key\
> `carregar_chave`: Function to read the decryption key\
> `criptografar_arquivo`: Function to realize the cryptographing process\
> `encontrar_arquivos`: Function to find the files to cryptography, ignoring the own program\
> `criar_mensagem_resgate`: Function to create the rescue message\
> `main`: Main function of the program

### 2.1.3 Creating the decryption program: The user recovery method

> With the cryptography program done, I started to code the decryption program, by writing the functions. The most part of the program holds the same funcitons of the other program, only changing one function
> `descriptografar_arquivo`: Function to decrypt the files

### 2.1.4 Realizing the cryptography: Putting the program in execution

> With the VS Code terminal, I executed the program with the following code\
> `python ransomware.py`\
> It generated the rescue message "LEIA ISSO.txt" and the decryption key "chave.key"

### 2.1.5 Recovering the files: Realizing the decrypt

> Finally, I performed the decryption process running the decryption program, recovering the files\
> `python descriptografar.py`

## 2.2 Keylogger

### 2.2.1 Library installing: Building the environment

>  I started downloading the pynput, the library needed to monitor keyboard activity\
> `pip install pynput`

### 2.2.2 Ignore list: keyboard keys to be ignored

> So, I made a list of keys that should be ignored by the program, named "IGNORAR"

### 2.2.3 Listing the functions: Creating the program logic

> After it, I created the program logic by writing the functions\
> `on_press`: Function to write the keys typped by the user, putting a specific logic to some keys\
> And also creating a listener, to monitorating the keyboard activity

### 2.2.4 Executing the program: Starting the monitoration

> Finally, I put the program at exxecution by running it\
> `python keylogger.pyw`\
> Using the "pyw" type to the program might run at the background. The file "documento.txt" started to be watched, and everything that was wrote were recorded at the "log.txt" file\

------------------------------------------------------------------

# 3. Key Learnings

Through these exercises, I was able to gain practical experience in:
* **Reconnaissance and Enumeration:** Using tools like Nmap and Enum4linux to gather critical information about target systems.
* **Brute-Force Attacks:** Understanding and executing credential attacks on common services like FTP, HTTP, and SMB with Medusa.
* **Python for Cybersecurity:** Applying Python to develop basic offensive tools, understanding file manipulation, cryptography, and system monitoring.
* **Ethical Hacking Methodology:** Following a structured process of information gathering, exploitation, and post-exploitation.
