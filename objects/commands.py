from imports import *

class Command:
    connect = ["piactl", "connect"]
    
    class get:
        command = ["piactl", "get"]
        
        regions = command + ["regions"]
        region = command + ["region"]
        connectionstate = command + ["connectionstate"]
    
    class set:
        command = ["piactl", "set"]
        
        region = command + ["region"]