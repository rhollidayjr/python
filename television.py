class Television():
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    
    def __init__(self) -> None:
        status = False
        muted = False
        volume = MIN_VOLUME
        channel = MIN_CHANNEL
        
    def power(self):
        
    def mute(self):
        
    def channel_up(self):

    def channel_down(self):
        
    def volume_up(self):
        
    def volume_down(self):
        
    def __str__(self) -> str:
        """
        Method to show the tv status.
        :return: tv status.
        """
        print(f'Power = {status}, Channel = {channel}, Volume = {volume}')