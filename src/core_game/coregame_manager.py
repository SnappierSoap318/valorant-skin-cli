'''
async manager calls to coregame to update session
session keeps track of inmatch/map/other data about live match
'''
import asyncio 

from .session import Session

# important imports or something
from ..flair_management.skin_manager.skin_manager import Skin_Manager

# task imports 
from .async_tasks import randomize

class Coregame_Manager:

    def __init__(self,client):
        self.client = client
        self.skin_manager = Skin_Manager(self.client)
        self.session = Session(self.client,self.skin_manager)

    async def update_session_routine(self):
        presence = await self.session.update()

    async def main_loop(self):
        await self.update_session_routine()