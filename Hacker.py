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
        self.__inventory = []
        crypto_token1 = Asset("CryptoToken", "CryptoToken")
        self.__inventory.append(crypto_token1)
        self.__rig = 0
        self.__trace_level = 0


    def acquire_rig(self, rig_name):
        for item in self.__inventory:
            if item.get_name() == "CryptoToken":
                self.__rig = Rig(rig_name)
                self.__inventory.remove(item)
                print("You have activated a new rig")
            else:
                print("You do not have enough tokens to acquire a new rig")

    def encrypt_assets(self, asset_name):
        for item in self.__rig.get_storage():
            if item.get_name() == "Security Chip":
                for item_to_encrypt in self.__rig.get_storage():
                    if item_to_encrypt.get_name() == asset_name and not item_to_encrypt.is_encrypted():
                        item_to_encrypt.encrypt()
                        self.__rig.consume_asset(item)
                        break
        print(f"There is no unencrypted {asset_name}(s)")

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
        return self.__rig

    def launch_data_spike(self, target_rig):
        for item in self.__rig.get_storage():
             if item.get_name() == "Data Spike":
                target_rig.take_damage()
                self.__rig.consume_asset(item)
                break

        if target_rig.is_broken():
            for item in self.__rig.get_storage():
                if item.get_name() == "Removable Drive":
                    self.__rig.consume_asset(item)
                    '''storage_size = len(target_rig.get_storage()) - 1
                    for index in range(storage_size, -1, -1):
                        if not target_rig.get_storage()[index].is_encrypted():
                            self.__rig.store_asset(target_rig.get_storage()[index])
                            target_rig.consume_asset(target_rig.get_storage()[index])'''
                    for item2 in target_rig.get_storage()[:]:
                        if not item2.is_encrypted():
                            self.__rig.store_asset(item2)
                            target_rig.consume_asset(item2)
                    break



    def add_asset(self, asset_name):
        if asset_name == "Data Spike":
            asset = Asset("Data Spike", "CryptoToken")
            self.__inventory.append(asset)
        elif asset_name == "patch":
            asset = Asset("patch", "CryptoToken")
            self.__inventory.append(asset)
        elif asset_name == "token":
            asset = Asset("token", "CryptoToken")
            self.__inventory.append(asset)
        elif asset_name == "chip":
            asset = Asset("chip", "CryptoToken")
            self.__inventory.append(asset)

    def get_inventory(self):
        return self.__inventory

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


