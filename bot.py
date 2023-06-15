import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.members = True
intents.message_content = True  # Добавьте эту строку

bot = commands.Bot(command_prefix='!', intents=intents)

def choose_role():
    roles = ['бот', 'сап', 'мид', 'топ', 'лес']
    return random.sample(roles, 5)

@bot.event
async def on_ready():
    print(f'Bot is ready.')

@bot.command()
async def choose_roles(ctx, *users):
    if len(users) < 5:
        await ctx.send("Недостаточно пользователей.")
        return
    
    participants = random.sample(users, 5)
    roles = choose_role()
    
    for participant, role in zip(participants, roles):
        await ctx.send(f'{participant} получает роль {role}.')


def main():
    bot.run('MTExODk5NzE4Mjk4NTU0MzgyMA.G-C1Da.f4C9h0i3v_fqCSil-3017k9B1YHJqYx5lJNEx0')

if __name__ == '__main__':
    main()
