"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Asset:
    def __init__(self, name, description):
        self.__name = name
        self.__description = description
        self.__encrypted = False

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def is_encrypted(self):
        return self.__encrypted

    def encrypt(self):
        self.__encrypted = True

    def decrypt(self):
        self.__encrypted = False

    def __str__(self):
        if self.is_encrypted():
            return_string = f"<{self.__name}> : <{self.__description}> [Encrypted]"
        else:
            return_string = f"<{self.__name}> : <{self.__description}>"

        return return_string