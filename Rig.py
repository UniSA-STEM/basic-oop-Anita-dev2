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
        self.__broken_state = True
        self.__storage = []
        data_spike1 = Asset("Data Spike", "Data Spike")
        self.store_asset(data_spike1)
        data_spike2 = Asset("Data Spike", "Data Spike")
        self.store_asset(data_spike2)
        removable_drive = Asset("Removable Drive", "Removable Drive")
        self.store_asset(removable_drive)
        security_chip = Asset("Security Chip", "Security Chip")
        self.store_asset(security_chip)
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