"""
File: Asset.py
Description: <This module defines the Asset class and its methods>
Author: <Anita Maratheftis>
ID: <110467133>
Username: <maray160>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Asset:
    def __init__(self, name, description):
        """
        This is the Asset class. It takes in parameters of name and description.
        It also has the encrypted attribute, which by default is set to false.
        :param name:
        :param description:
        """
        self.__name = name
        self.__description = description
        self.__encrypted = False

    def get_name(self):
        """
        This is a getter for name
        :return:
        """
        return self.__name

    def get_description(self):
        """
        This is a getter for description
        :return:
        """
        return self.__description

    def is_encrypted(self):
        """
        This is a check if an asset is encrypted
        :return:
        """
        return self.__encrypted

    def encrypt(self):
        """
        This sets the encrypted attribute to true
        :return:
        """
        self.__encrypted = True

    def decrypt(self):
        """
        This sets the encrypted attribute to false
        :return:
        """
        self.__encrypted = False

    def __str__(self):
        """
        This is the string method
        :return:
        """
        if self.is_encrypted():
            return_string = f"<{self.__name}> : <{self.__description}> [Encrypted]"
        else:
            return_string = f"<{self.__name}> : <{self.__description}>"

        return return_string