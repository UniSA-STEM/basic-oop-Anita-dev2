"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import random
from Asset import Asset
from Rig import Rig


class Hacker:
    def __init__(self, name):
        self.__name = name
        self.__crypto_token = 2
        self.__rig = 0
        self.__trace_level = 0
        self.__inventory = []

    def acquire_rig(self, rig_name):
        if self.__crypto_token > 0:
            self.__rig = Rig(rig_name)
            self.__crypto_token = self.__crypto_token - 1
            print("You have activated a new rig")
        else:
            print("You do not have enough tokens to acquire a new rig")

    def get_rig(self):
        return self.__rig

    def launch_data_spike(self, target_rig):
         for item in self.__rig.get_storage():
             if item.get_name() == "Data Spike":
                target_rig.take_damage()
                self.__rig.consume_asset(item)
                break


    def trace(self):
        pass

    def repair_my_rig(self):
        if self.__crypto_token > 0:
            if self.__rig.rig_repair():
                self.__crypto_token = self.__crypto_token - 1
            else:
                print("No repair needed")
        else:
            print("Insufficient funds to repair")

    def upgrade_my_rig(self):
        # Needs hardware patch, increases rig level, storage size and decreases battle
        # need rig and hardware patch to execute
        pass


