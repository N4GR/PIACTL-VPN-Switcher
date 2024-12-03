from imports import *

# Local imports
from modules.issue import Issue
from modules.config import Configs

from objects.commands import Command

def RandomConnect():
    # Get a random region from region list.
    random_region = random.choice(issue.regions)
    
    # Create region set command.
    command = Command.set.region + [random_region]
    
    # Connect to new regions.
    issue.command(command)
    
    # Check if VPN successfully set region.
    new_region = issue.command(Command.get.region).rstrip("\n")
    
    if random_region == new_region:
        print(f"Successfully switched region: {new_region}")
    else:
        print(f"Couldn't connect to region: {random_region}")
    
    # Wait 2 seconds for VPN to connect to new region.
    time.sleep(config.connecting.ConnectionRetrySleep)
    
    # Check if connected to VPN server.
    is_connected = issue.connected()
    
    if is_connected == False: # If the VPN isn't connected.
        while True:
            issue.command(Command.connect) # Attempt to connect.
            
            checker = 0 # Counts how many times it has tried to connect.
            if issue.connected is False:
                if checker == config.connecting.ConnectionRetryCount: # If it has checked 5 times, break the loop.
                    print("Unable to connect.")
                    break
                
                checker += 1
                
                time.sleep(config.connecting.ConnectionRetrySleep) # Sleep in between tries.
            else: # If it's connected, break from loop!
                print("Successfully connected!") 
                break
    else: # If it's connected, tell them!
        print("Successfully connected!")
    
if __name__ == "__main__":
    configs = Configs()
    config = configs.configs
    
    issue = Issue()
    
    while True:
        RandomConnect()
        time.sleep(config.connecting.RegionChangeInterval)