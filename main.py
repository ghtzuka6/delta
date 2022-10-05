import discord, os, json
from discord.ext import commands

with open("config.json") as f:
   data = json.load(f)
   token = data["token"] 
   
class discordbot(commands.AutoShardedBot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(command_prefix="*",
                         intents=intents,
                         help_command=None,
                         owner_ids=[371224177186963460, 990633882644791318], 
                       
  activity=discord.Game(name="*help"))

    async def setup_hook(self):
        for file in os.listdir("./cogs"):
            if file.endswith(".py"):
                await self.load_extension("cogs." + file[:-3])
                print(f"loaded cog {file[:-3]}")

        await self.load_extension("jishaku")

    async def on_ready(self):
        print("Bot Back To Alive")


bot = discordbot()
bot.run(token)
