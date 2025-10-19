"""
File: Rig.py
Description: <This module defines the Rig class and its methods>
Author: <Anita Maratheftis>
ID: <110467133>
Username: <maray160>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import random
from Asset import Asset

class Rig:
    """
    This is the Rig class. It takes in name as a parameter. It has the following attributes:
    - Name
    - Damage Counter
    - Broken State
    - Storage
    - Upgrade Level
    The rig storage is initialised as an empty list, then has three assets appended to the list for
    when the rig is instantiated
    """
    def __init__(self, name):
        self.__name = name
        self.__damage_counter = 0
        self.__broken_state = False
        self.__storage = []
        data_spike1 = Asset("Data Spike", "This is used to launch an attack on a Target Rig")
        self.store_asset(data_spike1)
        data_spike2 = Asset("Data Spike", "This is used to launch an attack on a Target Rig")
        self.store_asset(data_spike2)
        removable_drive = Asset("Removable Drive", "This is used for extraction of assets")
        self.store_asset(removable_drive)
        self.__upgrade_level = 0

    def rig_repair(self):
        """
        This method takes the damage counter and determined whether the rig needs to be repaired,
        and if so, it resets the broken state and damage counter
        :return: Boolean
        """
        if self.__damage_counter == 0:
            repaired = False
        else:
            self.__damage_counter = 0
            self.__broken_state = False
            repaired = True
        return repaired

    def store_asset(self, asset):
        """
        This method takes an asset as a parameter and appends the asset to storage
        :param asset:
        :return:
        """
        self.__storage.append(asset)

    def get_storage(self):
        """
        This is a getter for storage
        :return:
        """
        return self.__storage

    def get_damage_counter(self):
        """
        This is a getter for damage counter
        :return:
        """
        return self.__damage_counter

    def get_rig_name(self):
        """
        This is a getter for name
        :return:
        """
        return self.__name

    def generate_assets(self):
        """
        This method generates a random number, and assigns the result to one of five assets.
        It then appends that asset to the rig storage
        :return:
        """
        # Generate random number and assign to assets, then append to storage
        r_num = random.randint(1,5)
        if r_num == 1:
            asset1 = Asset("CryptoToken", "This is used to acquire and repair rigs")
            self.__storage.append(asset1)
        elif r_num == 2:
            asset2 = Asset("Data Spike", "This is used to launch an attack on a Target Rig")
            self.__storage.append(asset2)
        elif r_num == 3:
            asset3 = Asset("Removable Drive", "This is used for extraction of assets")
            self.__storage.append(asset3)
        elif r_num == 4:
            asset4 = Asset("Security Chip", "This is used to encrypt or decrypt assets")
            self.__storage.append(asset4)
        elif r_num == 5:
            asset5 = Asset("Hardware Patch", "This is used to upgrade rigs")
            self.__storage.append(asset5)



    def rig_condition(self):
        """
        This method determines the condition based on percentage of health, so it
        applies to all levels of health
        :return:
        """
        # Initialise condition variable, assign words depending on condition
        condition = ""
        if self.__damage_counter == 0:
            condition = "Pristine"
        # Check percentage of health based on level
        elif self.__damage_counter / (self.__upgrade_level + 2)  < 0.5:
            condition = "Fragile"
        elif self.__damage_counter / (self.__upgrade_level + 2) < 1:
            condition = "Damaged"
        elif self.__damage_counter == self.__upgrade_level + 2:
            condition = "Broken"

        # Display result to user
        return f"{condition} (Level {self.__upgrade_level})"

    def is_broken(self):
        """
        This method returns the broken state
        :return:
        """
        return self.__broken_state


    def take_damage(self):
        """
        This method increments the damage by one. It tests based on max health,
        and if the rig is broken it sets broken state to True
        :return:
        """
        # Increment damage counter by 1
        self.__damage_counter = self.__damage_counter + 1
        # If the damage counter equals the upgrade level + 2 (indicating max damage per level), reset broken state
        if self.__damage_counter == self.__upgrade_level + 2:
            self.__broken_state = True


    def consume_asset(self, asset):
        """
        This method takes an asset as a parameter and removes it from storage if it is in storage.
        :param asset:
        :return:
        """
        for item in self.__storage:
            if item == asset:
                self.__storage.remove(asset)
                break

    def get_upgrade_level(self):
        """
        This is a getter for upgrade level
        :return:
        """
        return self.__upgrade_level

    def increment_upgrade_level(self):
        """
        This method increases upgrade level unless it is already at max upgrade
        :return:
        """
        # If the rig is below the max level, increment level by 1
        if self.__upgrade_level < 4:
            self.__upgrade_level = self.__upgrade_level + 1
        else:
            # Display to user that it is already at max level
            print("This rig is fully upgraded (Level 4).")

    def __str__(self):
        """
        This is the string method for Rig
        :return:
        """
        string = f""
        for item in self.__storage:
            string = string + f"{item}\n"
        return string