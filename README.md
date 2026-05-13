# FILE-INTEGRITY-CHECKER

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: SYED ZOHAIB ABDUS SALAM

*INTERN ID*:CTIS9474

*DOMAIN*: CYBER SECURITY & ETHICAL HACKING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

*OUTPUT*

<img width="1365" height="719" alt="Image" src="https://github.com/user-attachments/assets/a31512d4-f8d9-4ee8-90f5-c2eccfb202e3" />

This project is a File Integrity Checker developed using Python. The main purpose of this project is to check whether files have been modified, deleted, or newly added. It helps in maintaining the security and integrity of important files by comparing their current state with previously saved information. This project is simple and suitable for beginners because it introduces important concepts like file handling, hashing, and cybersecurity basics.

The main tool used in this project is Python because it is easy to learn and widely used for automation and security-related tasks. Python provides built-in libraries that make the development process simple. One of the important libraries used is hashlib. This module is used to generate hash values for files using the SHA-256 algorithm. A hash value is like a digital fingerprint of a file. Every file has a unique hash, and even a small change in the file content produces a completely different hash value. This helps in identifying whether a file has been changed or not.

Another module used is os. This library helps the program interact with the operating system. It is used to access folders, scan files, and read directory contents. The project also uses json to store hash values in a JSON file. JSON format is easy to read and store data, which makes it suitable for saving the baseline file hashes.

The editor platform used for this project is Visual Studio Code. VS Code is a popular code editor developed by Microsoft. It provides useful features such as syntax highlighting, integrated terminal, debugging support, and extensions for different programming languages. In this project, VS Code is used to write the Python code, create project folders, and execute the program using the terminal. The Python extension in VS Code makes coding easier for beginners by identifying errors and improving code readability.

The working process of this project is simple. First, the program scans all files inside a selected folder and generates their hash values. These hash values are then stored in a JSON file called the baseline. Later, when the program is executed again, it recalculates the current hashes of the files and compares them with the stored baseline hashes. If a file hash changes, the program reports that the file has been modified. If a file is missing, it reports that the file was deleted. Similarly, if a new file is found, it reports it as a newly added file.

This project has many practical applications. It is useful in cybersecurity to detect unauthorized changes in important files. Organizations use similar systems to monitor system files and prevent malware attacks or hacking attempts. It is also useful in system administration to monitor server files and configuration files. In data protection, integrity checking ensures that files are not corrupted or changed during storage or transfer. The project can also be used in educational environments to help students understand hashing, file handling, and basic security concepts.

Overall, this project is a beginner-friendly implementation of file integrity monitoring. It helps in learning important programming and cybersecurity concepts while providing practical experience with Python and file management techniques.
