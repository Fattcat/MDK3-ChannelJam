import time
import subprocess
import os

os.system("clear")
time.sleep(1)

print("-"*30)
print("[ - MDK3 Channel Jammer - ]")
print("-"*30 + "\n")

time.sleep(1)
print("Checking if script was statred with sudo ...")


# DEFFINITIONS --------------------
def CheckSudo():
    if os.geteuid() !=0:
        print("Scriot was NOT started with sudo\pls Sta>
        exit()
    else:
        print("Script was started woth sudo :D\nContinu>

def MDK3-JAM():
    subprocess.run(["mdk3", adapter, "d", "-c" , Specif>


CheckSudo()

print("\nLoading MDK3 CHANNEL JAMMER\n")
time.sleep(2)

print("Please sellect option\n")
print("[1] - Jam ONLY 1 speciffic channel")
print("[2] - Jam ALL channels (Pick CH to Pick CH)
print("[3] - Jam ALL channels (1 to 12)\n")
PickToJam = input("I will Pick --> ")

if PickToJam == "1":
    SpecifficChannel = input("Type channel number --> ")
    # Jam 1 chan
    exit()

elif PickToJam == "2":
    SpeccificChannel = input("Type channel number --> ")
    # Jam from sellected channel to sellected channel
    exit()

elif PickToJam =="3":
    # Jam all chans
    exit()
else:
    print("Sellected WRONG Option :" , PickToJam)
    exit()
