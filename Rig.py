"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import random
from Asset import Asset

class Rig:
    def __init__(self, name):
        self.__name = name
        self.__damage_counter = 0
        self.__broken_state = False
        self.__storage = []
        data_spike1 = Asset("Data Spike", "This is used to launch an attack on a Target Rig")
        self.store_asset(data_spike1)
        data_spike2 = Asset("Data Spike", "This is used to launch an attack on a Target Rig")
        self.store_asset(data_spike2)
        removable_drive = Asset("Removable Drive", "Used for extraction of assets")
        self.store_asset(removable_drive)
        self.__removable_drive = 1
        self.__upgrade_level = 0

    def rig_repair(self):
        if self.__damage_counter == 0:
            repaired = False
        else:
            self.__damage_counter = 0
            self.__broken_state = False
            repaired = True
        return repaired

    def store_asset(self, asset):
        self.__storage.append(asset)

    def get_storage(self):
        return self.__storage

    def get_rig_name(self):
        return self.__name

    def generate_assets(self):
        r_num = random.randint(1,5)
        if r_num == 1:
            asset1 = Asset("CryptoToken", "This is used to acquire and repair rigs")
            self.__storage.append(asset1)
        elif r_num == 2:
            asset2 = Asset("Data Spike", "This is used to launch an attack on a Target Rig")
            self.__storage.append(asset2)
        elif r_num == 3:
            asset3 = Asset("Removable Drive", "Used for extraction of assets")
            self.__storage.append(asset3)
        elif r_num == 4:
            asset4 = Asset("Security Chip", "This is used to encrypt or decrypt assets")
            self.__storage.append(asset4)
        elif r_num == 5:
            asset5 = Asset("Hardware Patch", "This is used to upgrade rigs")
            self.__storage.append(asset5)



    def rig_condition(self):
        # Initialise condition variable, assign words depending on condition
        condition = ""
        if self.__damage_counter == 0:
            condition = "Pristine"
        elif self.__damage_counter == 1 or self.__damage_counter == 2:
            condition = "Fragile"
        elif self.__damage_counter == 3 or self.__damage_counter == 4:
            condition = "Damaged"
        elif self.__damage_counter == 5:
            condition = "Broken"

        return f"{condition} (Level {self.__upgrade_level})"

    def is_broken(self):
        return self.__broken_state


    def take_damage(self):
        self.__damage_counter = self.__damage_counter + 1
        if self.__damage_counter == self.__upgrade_level + 2:
            self.__broken_state = True


    def consume_asset(self, asset):
        for item in self.__storage:
            if item == asset:
                self.__storage.remove(asset)
                break

    def get_upgrade_level(self):
        return self.__upgrade_level

    def increment_upgrade_level(self):
        if self.__upgrade_level < 4:
            self.__upgrade_level = self.__upgrade_level + 1
        else:
            print("This rig is fully upgraded (Level 4).")

    def __str__(self):
        string = f""
        for item in self.__storage:
            string = string + f"{item}\n"
        return string