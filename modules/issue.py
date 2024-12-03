from imports import *

# Local imports
from objects.commands import Command

class Issue:
    def __init__(self):
        self.regions = self.Regions(Command.get.regions)
    
    def command(self, args: list) -> str:
        result = subprocess.run(
            args,
            capture_output = True,
            text = True,
            check = True
        )
        
        return result.stdout
    
    def connected(self) -> bool:
        result = subprocess.run(
            Command.get.connectionstate,
            capture_output = True,
            text = True,
            check = True
        )
        
        if (
            "Disconnect" in result.stdout or
            "Reconnect" in result.stdout
        ):
            return False
        else:
            return True

    def Regions(self, args: list) -> list:
        output = self.command(args)
        output_list = output.split("\n")
        output_list.remove("auto") # Remove auto from list.
        
        return output_list[:-1] # everything but last, empty item.