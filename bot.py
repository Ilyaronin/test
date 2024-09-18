import discord
from discord.ext import commands
import os
import random
import requests
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
#решение проблем с экологией
idea = ['Декоративные горшки для растений', 'Органайзеры для канцелярии',
        'Подставки под горячее', 'Кормушки для птиц']

sorting = {
    'бутылка': 'Переработка',
    'журнал': 'Переработка',
    'пластиковый пакет': 'Переработка',
    'еды': 'Компостирование (если это органические отходы), иначе в обычную урну',
    'лампочка': 'Переработка'}

materials = {'древесина':'10 лет', 'одежда':'3 года', 'резина':'100 лет',
             'пластиковая бутылка':'100-200 лет', 'губка':'200 лет',
             'стекло':'более 1000 лет'}
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def идеи(ctx):
    ideas = random.choice(idea)
    await ctx.send(ideas)

@bot.command()
async def сортировать(ctx, *, item: str):
    item = item.lower()
    if item in sorting:
        await ctx.send(f'Для предмета "{item}" рекомендуется: {sorting[item]}')

@bot.command()
async def разложение(ctx, *, material: str):
    material = material.lower()
    if material in materials:
        await ctx.send(f'Предмет: "{material}" разложение: {materials[material]}')
#базовые команды
@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)
        
@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)
#картинки
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('dog')
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)




bot.run("token")
