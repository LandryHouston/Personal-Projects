import time
from termcolor import colored

# Change to while true statement and ask user for countdown timer #

countdown = [
    "10",
    "09",
    "08",
    "07",
    "06",
    "05",
    "04",
    "03",
    "02",
    "01",
]

for second in countdown:
    time.sleep(1)
    print(second, end="\r")

time.sleep(1)

print(colored("BLASTOFF!", ("red"), attrs=["bold"]))

time.sleep(3)
start = [
    "Ready?",
    "Set?",
]

for second in start:
    time.sleep(1)
    print(colored(second, ("yellow")))
time.sleep(1)
print(colored("GO!", ("green"), attrs=["bold"]))
