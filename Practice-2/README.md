# About 

This `Practice #2` was about to create two scripts one of them in Bash and the other one in Powershell, the conditions was both scripts has to had:

* a var
* a if condition
* a loop
* one function with a parameter

## Bash Script 
This script has two options 

### Option 1
Directories for CTF competitions, usage `DirCreator CTF dirName`
The purpose of this option is to forget about to create directories manually at the moment you are doing your writeups. The script will create 4 directories (in the path you were) for the common categories in CTF competitions 

### Option 2
A directory for a pentest within a port scan, usage `DirCreator Pentest dirName`
In this option the script will create just one directory after that will ask to user for an IP address to scan, then it will check for open ports in range 10 to 500 where open ports during the scan will be written into a file called `Scan.txt`, then will create a file called `notes.txt` for anything you want to take note during the pentest

## PowerShell Script

