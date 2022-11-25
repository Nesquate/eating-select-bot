import discord
from discord.ext import commands


class EatWhatBot(commands.Bot):
    def __init__(self, intents: discord.Intents):
        super().__init__(command_prefix="?", intents=intents)

    async  def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("-----")