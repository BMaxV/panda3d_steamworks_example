from direct.showbase.ShowBase import ShowBase

from direct.gui.DirectGui import OnscreenText
import os
#os.add_dll_directory(os.getcwd())

from steamworks import STEAMWORKS


class MyThing:
    def __init__(self,inventory=None):
        a=1
        
        steamworks = STEAMWORKS()
        steamworks.initialize()

        my_steam64 = steamworks.Users.GetSteamID()
        my_steam_level = steamworks.Users.GetPlayerSteamLevel()
    
        #my_steam64="12345Bob"
        #my_steam_level="3"
    
        print(f'Logged on as {my_steam64}, level: {my_steam_level}')
        #print('Is subscribed to current app?', steamworks.Apps.IsSubscribed())
        T=OnscreenText(text="steamID"+str(my_steam64), 
                    scale=0.05,
                    pos=(-0.3, 0, -0.8))
                    
        T=OnscreenText(text="steamlevel"+str(my_steam_level), 
                    scale=0.05,
                    pos=(0.3, 0, -0.8))
        
class Wrapper:    
    def __init__(self):
        self.b = ShowBase()
        self.mything = MyThing()
        
        
def main():
    W = Wrapper()
    while True:
        W.b.taskMgr.step()
        
if __name__ == "__main__":
    main()
