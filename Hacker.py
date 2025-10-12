"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Hacker:
    def __init__(self, rig):
        self.name = "xxx_(rYPT"
        self.crypto_token = 1
        self.rig = rig
        self.trace_level = 0


    def acquire_rig(self, num):
        if num > 0:
            self.rig = self.rig + 1
            self.crypto_token = self.crypto_token - 1
            print("You have activated a new rig")
        else:
            print("You do not have enough tokens to acquire a new rig. Try again later")


    def trace(self):
        pass



hacker = Hacker(0)
hacker.acquire_rig(1)