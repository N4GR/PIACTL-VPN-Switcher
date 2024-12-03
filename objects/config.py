class Config:
    """Config object.
    
    Attributes:
        connecting (Config.Connecting): Connecting object containing connection-related configs.
    """
    def __init__(self, config: dict):
        """Config object initialiser.
        
        Args:
            config (dict): Dictionary of config retrieved from config.yaml.
        """
        self.connecting = self.Connecting(config["Connecting"])
    
    class Connecting:
        """Connecting object.
        
        Attributes:
            RegionChangeInterval (int): The time in between region changes.
            ConnectionRetryCount (int): The amount of retries to attempt before failure.
            ConnectionRetrySleep (int): Time in between testing connection state.
        
        """
        def __init__(self, connecting_config: dict):
            """Connection object initialiser.
            
            Args:
                connecting_config (dict): Dictionary from config.yaml "Connecting."
            """
            self.RegionChangeInterval = connecting_config["RegionChangeInterval"]
            self.ConnectionRetryCount = connecting_config["ConnectionRetryCount"]
            self.ConnectionRetrySleep = connecting_config["ConnectionRetrySleep"]