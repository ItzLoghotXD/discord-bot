from aiohttp import web
from plugins import web_server

from discord import Intents
from discord import Client
from discord.ext import commands
from datetime import datetime

from config import LOGGER, PRIFIX, PORT

class Bot(Client):

    # Event: Bot is ready
    async def on_ready(self):
        self.LOGGER = LOGGER
        self.uptime = datetime.now()
        name = self.user.name
        print(f'Logged in as {name}')

        self.LOGGER(name).info(f"Bot is Running..!\n\nCreated by: https://github.com/ItzLoghotXD")

        #web-response
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

intents = Intents.default()
intents.message_content = True

bot = commands.Bot(intents=intents, command_prefix=PRIFIX)
bot = Bot(intents=intents)
