from colorama import Fore, Style  # Import libraries for colored text
import time
import re
import hashlib
import random
import ctypes
import sys
import os
import subprocess
Debug = True

def check_admin_privileges():
    """Check if the current script is running with administrative privileges."""
    if ctypes.windll.shell32.IsUserAnAdmin() != 0:
        print("Running with administrative privileges!")
    else:
      if Debug:
        print("Thank you for using krypted")
      else:
        print("This program requires administrator privileges to run properly.")
        print("Exiting..")
        import time
        time.sleep(2)
        exit()
def print_purple_text():
  """Prints the provided text in purple color."""
  print(Fore.MAGENTA)
  print("""                                                                     
@@@  @@@  @@@@@@@   @@@ @@@  @@@@@@@   @@@@@@@  @@@@@@@@  @@@@@@@   
@@@  @@@  @@@@@@@@  @@@ @@@  @@@@@@@@  @@@@@@@  @@@@@@@@  @@@@@@@@  
@@!  !@@  @@!  @@@  @@! !@@  @@!  @@@    @@!    @@!       @@!  @@@  
!@!  @!!  !@!  @!@  !@! @!!  !@!  @!@    !@!    !@!       !@!  @!@  
@!@@!@!   @!@!!@!    !@!@!   @!@@!@!     @!!    @!!!:!    @!@  !@!  
!!@!!!    !!@!@!      @!!!   !!@!!!      !!!    !!!!!:    !@!  !!!  
!!: :!!   !!: :!!     !!:    !!:         !!:    !!:       !!:  !!!  
:!:  !:!  :!:  !:!    :!:    :!:         :!:    :!:       :!:  !:!  
 ::  :::  ::   :::     ::     ::          ::     :: ::::   :::: ::  
 :   :::   :   : :     :      :           :     : :: ::   :: :  :   
                                                                    """)
  print(Style.RESET_ALL)  # Reset color after printing
def run_cmd_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"Command output:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing command '{cmd}': {e}")
def selection_menu():
    """Displays a red selection menu and returns the user's choice."""
    print(Fore.RED)  # Set red color for menu
    print("\nSelect an option:")
    print("1. Enter a IP to DDOS (for educational purposes only)")
    print("2. Get ip from discord user id")  # Placeholder for option 2
    print("3. (soon) teminate discord from userid")  # Placeholder for option 3
    print("4. (soon) teminate rblx acc from userid")  # Placeholder for option 4
    print("5. Exit")
    while True:
        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice in (1, 2, 3, 4, 5):
                return choice
            else:
                print("Invalid choice. Please enter 1-5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(Style.RESET_ALL)  # Reset color after menu

def is_valid_ip(ip):
    """Check if the given IP address is valid."""
    pattern = re.compile(r"^(\d{1,3}\.){3}\d{1,3}$")
    if pattern.match(ip):
        parts = ip.split(".")
        for part in parts:
            if int(part) < 0 or int(part) > 255:
                return False
        return True
    return False
def enter_fake_ip():
    """Prompts the user to enter a fake IP address."""
    while True:
        fake_ip = input("Enter a fake IP address (e.g., 192.168.1.1): ")
        textt = f"SENDING REQUESTS TO: {fake_ip}"
        if is_valid_ip(fake_ip):
            colors = [
                Fore.MAGENTA, Fore.RED, Fore.LIGHTMAGENTA_EX,
                Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX, Fore.WHITE,
                Fore.BLUE, Fore.LIGHTBLUE_EX
            ]
            start_time = time.time()
            while time.time() - start_time < 10:
                for color in colors:
                    print(f"{color}{textt}")
                    time.sleep(0.0001)  # Adjust the sleep time as needed
            print(Fore.GREEN + "Target offline.")
            break
        else:
            print(Fore.RED + "Not a valid IP address. Please try again.")

def generate_deterministic_ip(input_string):
    """Generate a deterministic IP address based on the input string."""
    hash_object = hashlib.md5(input_string.encode())
    hash_digest = hash_object.hexdigest()
    random.seed(hash_digest)
    
    # Generate realistic IP parts
    # Avoid reserved ranges by starting with 1-223 for the first octet (public IPs)
    first_octet = random.randint(1, 223)
    # Ensure the first octet does not result in a reserved range like 127.x.x.x
    if first_octet == 127:
        first_octet = 126
    
    # Generate the rest of the octets
    ip_parts = [first_octet, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    return ".".join(map(str, ip_parts))

def option_2():
    user_input = input("Enter targets userid or username: ")
    random_ip = generate_deterministic_ip(user_input)
    print(Fore.GREEN + f"The generated IP address for '{user_input}' is: {random_ip}")
    

def option_3():
    print("Coming soon...")

    # command = "Stop-Service -Name WinDefender"
    # try:
        # command = 'powershell -Command "Set-MPPreference -DisableRealtimeMonitoring $True"'
        # subprocess.run(command, shell=True, check=True)
        # print("Windows Defender real-time monitoring disabled successfully.")
    # except subprocess.CalledProcessError as e:
        # print(f"Failed to disable Windows Defender real-time monitoring: {e}")
    # try:
        
        # subprocess.run(["powershell", "-Command", command], shell=True, check=True)
        # print("Windows Defender service stopped successfully.")
    # except subprocess.CalledProcessError as e:
        # print(f"Failed to stop Windows Defender service: {e}")



def option_4():
    print("coming soon")
    


if __name__ == "__main__":
    check_admin_privileges()
    print_purple_text()
    
    while True:
        choice = selection_menu()
        if choice == 1:
            enter_fake_ip()
        elif choice == 2:
            option_2()
        elif choice == 3:
            option_3()
        elif choice == 4:
            option_4()
        elif choice == 5:
            print("Exiting...")
            break
