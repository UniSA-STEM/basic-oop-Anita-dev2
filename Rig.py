"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Rig:
    def __init__(self):
        self.name = "rig"
        self.damage_counter = 0
        self.broken_state = False
        self.storage = 0
        self.data_spikes = 2
        self.removable_drive = 1
        self.upgrade_level = 0


    def rig_repair(self):
        pass



    def rig_upgrade(self):
        pass

    def rig_condition(self):
        # Initialise condition variable, assign words depending on condition
        condition = ""
        if self.damage_counter == 0:
            condition = "Pristine"
        elif self.damage_counter == 1 or self.damage_counter == 2:
            condition = "Fragile"
        elif self.damage_counter == 3 or self.damage_counter == 4:
            condition = "Damaged"
        elif self.damage_counter == 5:
            condition = "Broken"

        print(f"{condition} (Level {self.upgrade_level})")

rig = Rig()
rig.rig_condition()