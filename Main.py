"""
File: main.py
Description: <This module tests the functionality of the classes>
Author: <Anita Maratheftis>
ID: <110467133>
Username: <maray160>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Hacker import Hacker
from Asset import Asset
from Rig import Rig

def test_encryption():
    """
    - Hackers and Rigs are created
    - TEST: whether it will encrypt two items in a row without a second security chip
    - Display storage to see whether items were encrypted
    :return:
    """
    # Create two hackers, and acquire rigs for both
    hacker = Hacker("xxx_(rypt0")
    hacker.acquire_rig("H4CKeR")
    target_hacker = Hacker("xxx_D3(rypt0")
    target_hacker.acquire_rig("target_rig")
    # Printing target hacker object and rig storage to show inventory prior to encrypting
    print(target_hacker)
    print(target_hacker.get_rig())

    # Encrypt assets, testing twice to show if it will encrypt without security chip
    target_hacker.encrypt_assets("Data Spike")
    target_hacker.encrypt_assets("Data Spike")

    # Printing target hacker and rig storage to show inventory after encrypting
    print(target_hacker)
    print(target_hacker.get_rig())


def test_transferring_encrypted_items():
    """
    - Hackers and Rigs are created
    - Target encrypts asset
    - Hacker launches data spikes
    - TEST: To see whether the target hacker had their encrypted assets transferred
    :return:
    """
    # Create two hackers, and acquire rigs for both
    hacker = Hacker("xxx_(rypt0")
    hacker.acquire_rig("H4CKeR")
    target_hacker = Hacker("xxx_D3(rypt0")
    target_hacker.acquire_rig("target_rig")

    # Target hacker encrypts an asset
    target_hacker.encrypt_assets("Data Spike")

    # Hacker launches data spikes
    hacker.launch_data_spike(target_hacker.get_rig())
    hacker.launch_data_spike(target_hacker.get_rig())

    # Encrypted asset remains in target rig storage due to it being encrypted
    print(target_hacker.get_rig())



def test_decryption():
    """
    - Hackers and rigs are created
    - Inventory and storage displayed prior to encryption
    - Target hacker encrypts
    - Assets are Generated
    - Security Chip is transferred from storage to inventory
    - Inventory is displayed again
    - Target hacker decrypts
    - Rig storage displayed to show changes
    :return:
    """
    # Create two hackers, and acquire rigs for both
    hacker = Hacker("xxx_(rypt0")
    hacker.acquire_rig("H4CKeR")
    target_hacker = Hacker("xxx_D3(rypt0")
    target_hacker.acquire_rig("target_rig")

    # Printing target hacker object and rig storage to show inventory prior to encrypting
    print(target_hacker)
    print(target_hacker.get_rig())

    # Encrypt a Data Spike
    target_hacker.encrypt_assets("Data Spike")

    # Generate assets to gain another security chip
    for i in range(1, 10):
        target_hacker.get_rig().generate_assets()

    # Transfer Security chip to inventory
    target_hacker.transfer_an_asset("Security Chip", target_hacker.get_rig().get_storage(), target_hacker.get_inventory())

    # Display target hacker inventory and storage to show changes from the transfer
    print(target_hacker.display_inventory())
    print(target_hacker.get_rig())

    # Decrypt a Data Spike
    target_hacker.decrypt_assets("Data Spike")

    # Display rig storage
    print(target_hacker.get_rig())

def test_battles():
    """
    - Hackers and rigs created
    - Both rigs storage displayed prior to data spikes
    - Hacker launches data spikes
    - Display hacker inventory
    - Check of trace level
    - Check of rig condition
    - Upgrade rig
    - Check of rig condition after upgrading
    :return:
    """
    # Create two hackers and both acquire rigs
    hacker = Hacker("xxx_(rypt0")
    hacker.acquire_rig("H4CKeR")
    target_hacker = Hacker("xxx_D3(rypt0")
    target_hacker.acquire_rig("target_rig")

    # Check rig storage of hacker and target hacker
    print(hacker.get_rig())
    print(target_hacker.get_rig())

    # Launch two data spikes at target rig
    hacker.launch_data_spike(target_hacker.get_rig())
    hacker.launch_data_spike(target_hacker.get_rig())

    # Display inventory of hacker to show transfer of assets after rig was broken
    print(hacker.display_inventory())

    # Show trace level
    print(hacker.get_trace())

    # Show target hacker's condition
    print(target_hacker.get_rig().rig_condition())

    # Upgrade hacker rig and show condition
    hacker.upgrade_my_rig()
    print(hacker.get_rig().rig_condition())


def test_upgrade():
    """
    - Hacker is created
    - TEST: Hacker tries to upgrade without a rig
    - Hacker acquires rig
    - Check of condition
    - Upgrade Rig
    - Check of condition after upgrade
    - Generate assets
    - Transfer Hardware Patches to inventory
    - TEST: Upgrading to max level
    :return:
    """
    # Creating a Hacker object
    hacker = Hacker("xxx_(rypt0")

    # Trying to upgrade rig without a rig object
    hacker.upgrade_my_rig()

    # Creating a rig object
    hacker.acquire_rig("Rig1")

    # Showing upgrade level
    print(hacker.get_rig().rig_condition())

    # Upgrading with rig
    hacker.upgrade_my_rig()

    # Showing upgrade level
    print(hacker.get_rig().rig_condition())

    # Generate assets to gain another hardware patch
    for i in range(1, 30):
        hacker.get_rig().generate_assets()

    # Transfer Hardware Patch to inventory
    hacker.transfer_an_asset("Hardware Patch", hacker.get_rig().get_storage(), hacker.get_inventory())
    hacker.transfer_an_asset("Hardware Patch", hacker.get_rig().get_storage(), hacker.get_inventory())
    hacker.transfer_an_asset("Hardware Patch", hacker.get_rig().get_storage(), hacker.get_inventory())

    # Upgrading rig and displaying level after upgrading - testing max upgrades
    hacker.upgrade_my_rig()
    print(hacker.get_rig().rig_condition())
    hacker.upgrade_my_rig()
    print(hacker.get_rig().rig_condition())
    hacker.upgrade_my_rig()
    print(hacker.get_rig().rig_condition())
    hacker.upgrade_my_rig()


def test_trace_level():
    """
    - Create two hackers and rigs
    - Display hacker rig storage
    - Hacker launches multiple data spikes
    - Display hacker rig storage
    - Generate assets
    - Launch additional data spikes
    - Display trace level
    - TEST: Reduce trace without a CryptoToken
    - Display inventory
    - Transfer CryptoToken to inventory
    - Display inventory after transferring CryptoToken
    - Reduce Trace level
    - Display Trace level
    :return:
    """
    # Create two hackers and both acquire rigs
    hacker = Hacker("xxx_(rypt0")
    hacker.acquire_rig("H4CKeR")
    target_hacker = Hacker("xxx_D3(rypt0")
    target_hacker.acquire_rig("target_rig")

    # Display rig storage
    print(hacker.get_rig())

    # Launch data spikes
    hacker.launch_data_spike(target_hacker.get_rig())
    hacker.launch_data_spike(target_hacker.get_rig())
    hacker.launch_data_spike(target_hacker.get_rig())

    # Display rig storage
    print(hacker.get_rig())

    # Generate assets
    for i in range(1, 30):
        hacker.get_rig().generate_assets()

    # Display rig storage
    print(hacker.get_rig())

    # Launch Data Spikes
    hacker.launch_data_spike(target_hacker.get_rig())
    hacker.launch_data_spike(target_hacker.get_rig())
    hacker.launch_data_spike(target_hacker.get_rig())
    hacker.launch_data_spike(target_hacker.get_rig())

    # Display hacker trace level
    print(hacker.get_trace())

    # Attempt to reduce trace without CryptoToken
    hacker.reduce_trace()
    print(hacker.get_trace())

    # Display inventory before transferring asset
    print(hacker.display_inventory())

    # Transfer a CryptoToken from rig storage to hacker inventory
    hacker.transfer_an_asset("CryptoToken", hacker.get_rig().get_storage(), hacker.get_inventory())
    print(hacker.display_inventory())

    # Reduce educe trace level and Display trace level
    hacker.reduce_trace()
    print(hacker.get_trace())

def test_rig():
    """
    - Hacker is created
    - Inventory scanned and CryptoToken removed
    - TEST: hacker tries to acquire rig without CryptoToken
    :return:
    """
    # Create hacker object
    hacker = Hacker("hack")

    # Scan inventory and remove asset
    hacker.scan_inventory("CryptoToken")

    # Try to acquire a rig without a CryptoToken
    hacker.acquire_rig("rig1")

def test_conditions():
    """
    - Hackers and rigs created
    - Data spikes launched by target hacker
    - Check condition of hacker
    - Upgrade hacker rig
    - Check condition of hacker after upgrade
    - Generate assets
    - Transfer CryptoToken to inventory
    - Repair rig
    - TEST: Try to repair again after already repairing
    - Display hacker rig condition
    - Target hacker launches another data spike
    - Display hacker rig condition after data spike
    :return:
    """
    # Create two hackers and both acquire rigs
    hacker = Hacker("xxx_(rypt0")
    hacker.acquire_rig("H4CKeR")
    target_hacker = Hacker("xxx_D3(rypt0")
    target_hacker.acquire_rig("target_rig")

    # Launch data spikes
    target_hacker.launch_data_spike(hacker.get_rig())

    # Test condition of target rig
    print(hacker.get_rig().rig_condition())

    # Upgrade Hacker's rig
    hacker.upgrade_my_rig()

    # Display rig condition after upgrade
    print(hacker.get_rig().rig_condition())

    # Generate assets
    for i in range(1, 30):
        hacker.get_rig().generate_assets()

    # Transfer a CryptoToken to inventory
    hacker.transfer_an_asset("CryptoToken", hacker.get_rig().get_storage(), hacker.get_inventory())

    # Repair rig
    hacker.repair_my_rig()

    # Try to repair again
    hacker.repair_my_rig()

    # Display rig condition after repair and upgrade
    print(hacker.get_rig().rig_condition())

    # Launch data spike
    target_hacker.launch_data_spike(hacker.get_rig())

    # Display rig condition after Data Spike
    print(hacker.get_rig().rig_condition())


def main():
    test_encryption()
    test_decryption()
    test_battles()
    test_upgrade()
    test_trace_level()
    test_rig()
    test_conditions()
    test_transferring_encrypted_items()



if __name__ == "__main__":
    main()