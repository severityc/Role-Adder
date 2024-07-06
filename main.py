import discord
from discord.ext import commands

TOKEN = ''

ROLE_ID = ur_role_id 
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name='addroles', help='Add roles to users from ids.txt')
async def add_roles(ctx):
    try:
        with open('ids.txt', 'r') as file:
            user_ids = file.read().splitlines()

        guild = ctx.guild

        for user_id in user_ids:
            user = guild.get_member(int(user_id))
            if user:
                role = guild.get_role(ROLE_ID)
                await user.add_roles(role)
                await ctx.send(f"Added role to user {user.name}#{user.discriminator}")
            else:
                await ctx.send(f"User with ID {user_id} not found")

    except FileNotFoundError:
        await ctx.send("File ids.txt not found")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

bot.run(TOKEN)
