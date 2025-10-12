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

    def acquire_rig(self, rig_name):
        if self.__crypto_token > 0:
            self.__rig = Rig(rig_name)
            self.__crypto_token = self.__crypto_token - 1
            print("You have activated a new rig")
        else:
            print("You do not have enough tokens to acquire a new rig")

        # create a target health, have 3 rounds of attacks under one spike
        # randomly generate damage, if damage breaks target, acquire a new asset (list, use random selector?)
    def launch_data_spike(self):
        pass

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


hacker = Hacker("Trent")
hacker.acquire_rig("rig1")
hacker.repair_my_rig()