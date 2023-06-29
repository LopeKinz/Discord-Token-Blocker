# discord-token-blocker
This repository contains a Python script called main.py that helps you monitor the access to your Discord token file and block any unauthorized programs from accessing it.

# Prerequisites
Before running the script, make sure you have the following installed:

* Python 3.x
* psutil library (pip install psutil)
# Usage
* Clone this repository and navigate to the project directory.
* Open main.py in a text editor.
* Replace "path/to/discord/token/file" with the actual path to your Discord token file.
* Save the changes.
* Open a terminal or command prompt and navigate to the project directory.
* Run the script by executing the following command:
```
python main.py
```
* The script will start monitoring the programs accessing the Discord token file.
* If a program other than Discord or Chrome attempts to access the file, the script will print a message indicating an unauthorized access and proceed to block the program's access.
* You can leave the script running while you use Discord, ensuring the security of your token file.
* Note: It is important to ensure that you have the necessary permissions to block programs using the taskkill command

# Disclaimer
Please use this script responsibly and in accordance with the terms and conditions of the platforms and services you are using. We are not responsible for any misuse of the script or any implications it may have.
