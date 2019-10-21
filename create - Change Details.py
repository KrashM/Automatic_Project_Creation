import os
import sys
from github import Github

path = "path/to/folder"

username = ""
password = ""

def create():
    folderName = str(sys.argv[1])
    os.makedirs(path + str(folderName))
    user = Github(username, password).get_user()
    user.create_repo(folderName)
    print("Succesfully created repository {}".format(folderName))

if __name__ == "__main__":
    create()