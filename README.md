## Password_Locker

## Author
Cynthia Ouma

## Description
This is a site where users can store their sign up and login details. The users can also create new accounts, generate passwords as well as create their own passwords. The users can also delete their accounts from the site.


## User Stories
The user would like to do the following :

1. To create an account for the application or log into the application.
2. Store my existing acounts login details for various accounts that i have registered for.
3. Generate new password for an account that i haven't registered for and store it with the account name.
4. Delete stored account login details that i do now want anymore.
5. Copy my credentials to the clipboard

## Installation / Setup instruction
The application requires the following installations to operate
python3.8
pyperclip
pip


## Cloning
Open Terminal {Ctrl+Alt+T}

git clone https://github.com/CynthiaOuma12673/password-locker.git

cd Password_Locker

code . or atom . based on the text editor you have.

## Running the Application
1. To run the application, open the cloned file in terminal and run the following commands:

  $ chmod +x run.py
  $ ./run.py
2. To run test for the application $ python3.8 user_test.py

## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
|Open the application on the terminal | Run the command ```$ ./run.py```|Hello Welcome to your Accounts Password Store... <br>* CA ---  Create New Account * LI ---  Have An Account |
|Select  CA| input username and password| Hello ```username```, Your account has been created succesfully! Your password is: ```password```|
|Select LI  | Enter your password and username you signed up with| Abbreviations menu to help you navigate through the application|
|Store a new credential in the application| Enter ```CS```|Enter Account, username, password<br>choose ```tp``` to enter your password or ```gp``` for the application to generate a password for you |
|Display all stored credentials | Enter ```DS```|A list of all credentials that has been stored or ```You don't have any credentials saved yet``` |
|Find a stored credential based on account name|Enter ```FS```| Enter the Account Name you want to search for and returns the account details|
|Delete an existing credential that you don't want anymore|Enter ```D```|Enter the account name of the Credentials you want to delete and returns true if the account has been deleted and false if the account doesn't exixt|
|Exit the application| Enter ```D```| The application exits|




## Technologies Used

python3.8

## Known Bugs
There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information
If you have any question or contributions, please email me at [oumacynthia817@gmail.com]

## License
MIT License:
Copyright (c) 2022 Password Locker
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Authors Info Slack Profile - Cynthia Ouma
