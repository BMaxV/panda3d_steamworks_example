from direct.showbase.ShowBase import ShowBase

from vector import vector
from panda_interface_glue import panda_interface_glue
from panda_interface_glue import drag_main

import os
#os.add_dll_directory(os.getcwd())

from steamworks import STEAMWORKS


class Inventory:
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

        reset = panda_interface_glue.create_button(
            str(my_steam64), (-0.3, 0, -0.8), (0.05, 0.05, 0.05), print, ("hello there",))
        
        reset2 = panda_interface_glue.create_button(
            str(my_steam_level), (0.3, 0, -0.8), (0.05, 0.05, 0.05), print, ("hello there",))
        
class Wrapper:    
    def __init__(self):
        self.b = ShowBase()
        self.inventory=Inventory()
        self.output=[]
        
def main():
    W = Wrapper()
    while True:
        W.b.taskMgr.step()
        
if __name__ == "__main__":
    main()
