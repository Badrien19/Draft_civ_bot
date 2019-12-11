# -*-coding:Latin-1 -*
# bot.py
import discord
import random
from discord import Game
from discord.ext import commands
from math import floor
from random import randrange

client = discord.Client()
client = commands.Bot(command_prefix = '.', case_insensitive=True)

@client.command(name='random',
				aliases=['r', 'rand'])
async def rand(ctx, nb: int):
	tirage = randrange(1, nb+1)
	await ctx.send(f'Nombre tiré: {tirage}')


@client.command()
async def draft(ctx, nb: int=9, * args):
	l_civilisation = [
		'Phénicien', 'Allemagne', 'Canada', 'Periclès', 'Chine', 'Amérique', 'Brésil', 'Géorgie', 'Inca', 'Indonésie',
		'Chandragupta', 'Nubie', 'Ottoman', 'Khmer', 'Mali', 'Australie', 'Macédoine', 'France', 'France-Eléonore',
		'Scythie', 'Pologne', 'Perse', 'Japon', 'Mapuche', 'Arabie', 'Sumer', 'Angleterre-Eléonore', 'Egypte', 'Russie',
		'Hongrie', 'Cree', 'Ecosse', 'Angleterre', 'Espagne', 'Gorgo', 'Norvège', 'Mongolie', 'Gandhi', 'Suède', 'Zoulou',
	]
	for ban in args:
		l_civilisation.remove(ban)
		print(f'ban {ban}')
	if nb < 0:
		await ctx.send(':warning:Sérieux bro ?:warning:')
		return
	if nb > len(l_civilisation):
		await ctx.send(':warning:Il y a plus de joueurs que de civ...:warning:')
		return
	random.shuffle(l_civilisation)
	civ_per_player = int(floor(len(l_civilisation)/nb))
	print(civ_per_player)
	txt = f'Invocation de la draft;\n'
	for i in range(0,nb):
		txt += f":19: Draft {i+1}: "
		for x in range(0, civ_per_player):
			txt += f'{l_civilisation.pop()}'
			if x != civ_per_player-1:
				txt += ', '
		txt += '\n'
	await ctx.send(txt)

client.run('xxxx')
