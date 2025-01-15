import sys
import shutil
import os

fileName = sys.argv[1]
if not os.path.isfile(fileName):
    print(f"{fileName} does not exist")
backupName = fileName + "_copy"

shutil.copyfile(fileName, backupName)
print(f"Backup file created as {backupName}")

#try except error???
#read more about python builtin functions