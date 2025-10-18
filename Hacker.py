"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
from Rig import Rig


class Hacker:
    def __init__(self, name):
        self.__name = name
        self.__inventory = []
        self.__crypto_token1 = Asset("CryptoToken", "This is used to acquire and repair rigs")
        self.__inventory.append(self.__crypto_token1)
        self.__hardware_patch = Asset("Hardware Patch", "This is used to upgrade rigs")
        self.__inventory.append(self.__hardware_patch)
        self.__security_chip = Asset("Security Chip", "This is used to encrypt or decrypt assets")
        self.__inventory.append(self.__security_chip)
        self.__rig = 0
        self.__trace_level = 0


    def acquire_rig(self, rig_name):
        """
        This method allows the Hacker to acquire a rig provided that the hacker
        has a CryptoToken in their inventory.
        :param rig_name:
        :return: None
        """
        if self.get_trace() < 5:
            found = False
            for item in self.__inventory:
                # Check for CryptoToken in inventory, print to user whether action was successful or not
                if item.get_name() == "CryptoToken":
                    self.__rig = Rig(rig_name)
                    self.__inventory.remove(item)
                    print("You have activated a new rig")
                    found = True
                    break
            if not found:
                print("You do not have enough tokens to acquire a new rig")
        else:
            print("Your trace level is too high!")

    def encrypt_assets(self, asset_name):
        """
        This method encrypts an asset provided that the hacker has a security chip in their inventory
        :param asset_name:
        :return:
        """
        # Check for Security Chip in inventory, if yes, proceeds to checks for if there is a match in asset and whether the
        # asset is already encrypted. If it is not, the method encrypts the asset and consumes the security chip
        if self.get_trace() < 5:
            found_asset = False
            sec_chip = False
            for item in self.__inventory:
                if item.get_name() == "Security Chip":
                    sec_chip = True
                    for item_to_encrypt in self.__rig.get_storage():
                        if item_to_encrypt.get_name() == asset_name and not item_to_encrypt.is_encrypted():
                            found_asset = True
                            item_to_encrypt.encrypt()
                            self.__inventory.remove(item)
                            break
                if found_asset:
                    break
            if not sec_chip:
                print("You do not have any security chips.")
            elif not found_asset:
                print(f"There is no unencrypted {asset_name}(s)")
        else:
            print("Your trace level is too high!")

    def decrypt_assets(self, asset_name):
        """
        This method decrypts an asset provided that the hacker has a security chip in their inventory
        :param asset_name:
        :return:
        """
        # Check for Security Chip in inventory, if yes, proceeds to checks for if there is a match in asset and  whether the
        # asset is already decrypted. If it is not, the method decrypts the asset and consumes the security chip
        if self.get_trace() < 5:
            found_asset = False
            sec_chip = False
            for item in self.__inventory:
                if item.get_name() == "Security Chip":
                    sec_chip = True
                    for item_to_encrypt in self.__rig.get_storage():
                        if item_to_encrypt.get_name() == asset_name and item_to_encrypt.is_encrypted():
                            found_asset = True
                            item_to_encrypt.encrypt()
                            self.__inventory.remove(item)
                            break
                if found_asset:
                    break
            if not sec_chip:
                print("You do not have any security chips.")
            elif not found_asset:
                print(f"There is no encrypted {asset_name}(s)")
        else:
            print("Your trace level is too high!")


    def get_rig(self):
        """
        Getter for self.__rig
        :return:
        """
        return self.__rig

    def launch_data_spike(self, target_rig):
        """
        This method launches data spikes provided that certain criteria is met. First, the trace level of the hacker is checked.
        If the trace level is less than 5 (the max), the next check is that the hacker has a Data Spike, if yes, this is removed from the inventory.
        If the target rig is broken, the hacker must have a Removable Drive to be able to extract assets from the target rig.
        If the target assets are not encrypted, the assets are added into the rig storage and removed from the target rig storage.
        :param target_rig:
        :return:
        """
        if self.get_trace() < 5:
            for item in self.__rig.get_storage():
                 if item.get_name() == "Data Spike":
                    target_rig.take_damage()
                    self.__rig.consume_asset(item)
                    break

            if target_rig.is_broken():
                for item in self.__rig.get_storage():
                    if item.get_name() == "Removable Drive":
                        self.__rig.consume_asset(item)
                        for item2 in target_rig.get_storage()[:]:
                            if not item2.is_encrypted():
                                self.__inventory.append(item2)
                                target_rig.consume_asset(item2)
                        break
        else:
            print("Your trace level is too high!")

    def get_inventory(self):
        return self.__inventory

    def trace(self):
        if self.__trace_level < 5:
            self.__trace_level = self.__trace_level + 1

    def get_trace(self):
        return self.__trace_level

    def reduce_trace(self):
        if self.__trace_level > 0:
            for item in self.__inventory:
                if item.get_name() == "CryptoToken":
                    self.__trace_level = 0
                    self.__inventory.remove(item)

    def repair_my_rig(self):
        for item in self.__inventory:
            if item.get_name() == "CryptoToken":
                if self.__rig.rig_repair():
                    self.__inventory.remove(item)
                    print("Repair complete")
                else:
                    print("No repair needed")
            else:
                print("Insufficient funds to repair")


    def upgrade_my_rig(self):
        for item in self.__inventory:
            if item.get_name() == "Hardware Patch":
                self.__rig.increment_upgrade_level()
                self.__inventory.remove(item)
                break


    def transfer_all_assets(self, list1, list2):
        for item in list1[:]:
            if not item.is_encrypted():
                list1.remove(item)
                list2.append(item)



    def transfer_an_asset(self, asset, list1, list2):
        for item in list1:
            if item.get_name() == asset:
                list1.remove(item)
                list2.append(item)
            else:
                print(f"{item} was not found")


    def scan_inventory(self, asset):
        for item in self.__inventory:
            if item.get_name() == asset:
                self.__inventory.remove(item)
                print(f"{item} has been removed from inventory")
            else:
                print(f"{item} not in inventory")



    def __str__(self):
        inventory = ""
        for items in self.__inventory:
            inventory = inventory + f"{items}\n"
        return f"<Hacker Name: {self.__name}> : <Rig Name: {self.__rig.get_rig_name()}> : <Trace Level: {self.__trace_level}> \n<Inventory>\n{inventory}"

