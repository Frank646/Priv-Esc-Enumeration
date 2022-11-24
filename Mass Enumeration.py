import os
import time

#Windows mass enumeration

print("________    _________   _________                            ")
print("\_____  \  /   _____/  /   _____/_____   ____   ____   ______")
print(" /   |   \ \_____  \   \_____  \\____ \_/ __ \_/ ___\ /  ___/")
print("/    |    \/        \  /        \  |_> >  ___/\  \___ \___ \ ")
print("\_______  /_______  / /_______  /   __/ \___  >\___  >____  >")
print("        \/        \/          \/|__|        \/     \/     \/ ")

os.system('systeminfo | findstr /B /C:"OS Name" /C:"OS Version" ')
# You can use this program to identify the name and the current version of the operating systems
# This can be used to then expand the enumeration search for specifics entities.

print(" ________    _________  __________         __         .__                   ")
print(" \_____  \  /   _____/  \______   \_____ _/  |_  ____ |  |__   ____   ______")
print("  /   |   \ \_____  \    |     ___/\__  \\   __\/ ___\|  |  \_/ __ \ /  ___/")
print(" /    |    \/        \   |    |     / __ \|  | \  \___|   Y  \  ___/ \___ \ ")
print(" \_______  /_______  /   |____|    (____  /__|  \___  >___|  /\___  >____  >")
print("         \/        \/                   \/          \/     \/     \/     \/ ")

os.system("wmic qfe get Caption,Description,HotFixID,InstalledOn")
#This will gather all system patches that are on the OS.
# You can then use the results to exploit the operating system depending on what exploit is patched.

print("   _____                .__    .__  __                 __                        ")
print("  /  _  \_______   ____ |  |__ |__|/  |_  ____   _____/  |_ __ _________   ____  ")
print(" /  /_\  \_  __ \_/ ___\|  |  \|  \   __\/ __ \_/ ___\   __\  |  \_  __ \_/ __ \ ")
print("/    |    \  | \/\  \___|   Y  \  ||  | \  ___/\  \___|  | |  |  /|  | \/\  ___/ ")
print("\____|__  /__|    \___  >___|  /__||__|  \___  >\___  >__| |____/ |__|    \___  >")
print("        \/            \/     \/              \/     \/                        \/ ")

os.system("wmic os get osarchitecture || echo %PROCESSOR_ARCHITECTURE%")
#This will identify the architecture of the operating system
#And of which how many bits can be processded or transmitted.
#This can aid you in directly executing code onto the CPU
#without the need of OS check

print("                              _________                                    __  .__               ")
print("  ____ ______   ____   ____   \_   ___ \  ____   ____   ____   ____  _____/  |_|__| ____   ____   ______")
print(" /  _ \\____ \_/ __ \ /    \  /    \  \/ /  _ \ /    \ /    \_/ __ \/ ___\   __\  |/  _ \ /    \ /  ___/")
print("(  <_> )  |_> >  ___/|   |  \ \     \___(  <_> )   |  \   |  \  ___|  \___|  | |  (  <_> )   |  \\___ \ ")
print(" \____/|   __/ \___  >___|  /  \______  /\____/|___|  /___|  /\___  >___  >__| |__|\____/|___|  /____  >")
print("       |__|        \/     \/          \/            \/     \/     \/    \/                    \/     \/ ")

os.system("netstat -ano")
# This will allow you to watch open ports so you can exploit
# any poor network that is misconfigured.

print("   .___      .__                                                      ")
print("  __| _/______|__|__  __ ___________  ________ __   ___________ ___.__.")
print(" / __ |\_  __ \  \  \/ // __ \_  __ \/ ____/  |  \_/ __ \_  __ <   |  |")
print("/ /_/ | |  | \/  |\   /\  ___/|  | \< <_|  |  |  /\  ___/|  | \/\___  |")
print("\____ | |__|  |__| \_/  \___  >__|   \__   |____/  \___  >__|   / ____|")
print("     \/                     \/          |__|           \/       \/     ")

os.system("driverquery")
# This will gather all drivers that are in use within the machine.
# Allowing you to exploit any untrusted or outdated drivers
# that manufactuers no longer offer support for.
