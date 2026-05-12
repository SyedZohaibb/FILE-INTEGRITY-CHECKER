import os
import hashlib
import json

FOLDER = "files"
BASELINE = "hashes.json"


def get_hash(file_path):

    sha = hashlib.sha256()

    with open(file_path, "rb") as file:

        data = file.read()
        sha.update(data)

    return sha.hexdigest()


def scan_files():

    hashes = {}

    for file_name in os.listdir(FOLDER):

        path = os.path.join(FOLDER, file_name)

        if os.path.isfile(path):

            hashes[file_name] = get_hash(path)

    return hashes


def save_hashes(hashes):

    with open(BASELINE, "w") as file:

        json.dump(hashes, file, indent=4)


def load_hashes():

    if not os.path.exists(BASELINE):

        return {}

    with open(BASELINE, "r") as file:

        return json.load(file)


def check_changes():

    old_hashes = load_hashes()

    new_hashes = scan_files()

    for file in old_hashes:

        if file not in new_hashes:

            print(file + " was deleted")

        elif old_hashes[file] != new_hashes[file]:

            print(file + " was modified")

    for file in new_hashes:

        if file not in old_hashes:

            print(file + " is a new file")


print("1. Create Baseline")
print("2. Check Files")

choice = input("Enter choice: ")


if choice == "1":

    hashes = scan_files()

    save_hashes(hashes)

    print("Baseline created successfully")


elif choice == "2":

    check_changes()


else:

    print("Invalid choice")