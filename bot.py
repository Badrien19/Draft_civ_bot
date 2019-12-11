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
	await ctx.send(f'Nombre tirer: {tirage}')


@client.command()
async def draft(ctx, nb: int=9, * args):
	l_civilisation = [
		'Phénicien', 'Allemagne', 'Canada', 'Periclès', 'Chine', 'Amérique', 'Brésil', 'Géorgie', 'Inca', 'Indonésie',
		'Chandragupta', 'Nubie', 'Ottoman', 'Khmer', 'Mali', 'Australie', 'Macédoine', 'France', 'France-Eléonore',
		'Scythie', 'Pologne', 'Perse', 'Japon', 'Mapuche', 'Arabie', 'Sumer', 'Angleterre-Eléonore', 'Egypte',
		'Russie',
		'Hongrie', 'Cree', 'Ecosse', 'Angleterre', 'Espagne', 'Gorgo', 'Norvège', 'Mongolie', 'Gandhi', 'Suède',
		'Zoulou',
	]
	for ban in args:
		l_civilisation.remove(ban)
		print(f'ban {ban}')
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

client.run('xxxxxx')

#
#'Frédéric Barberousse', 'Theodore Roosevelt', 'Victoria', 'Saladin', 'Pierre II', 'Qin Shi Huang',
#'Alphonse Ier du Kongo', 'Cléopâtre', 'Philippe II', 'Catherine de Médicis', 'Périclès', 'Gorgô', 'Gandhi',
#'Houjou Tokimune', 'Harald Hardrada', 'Trajan', 'Pierre Ier le Grand', 'Tomyris', 'Gilgamesh', 'Moctezuma Ier',
#'Amanitoré',
## dlc
#'Hedwige', 'Alexandre le grand', 'Cyrus II', 'Dyah Gitarja', 'Jayavrman', 'John Curtin', 'Aminatoré',
## gathering storm
#'Wilfrid Laurier', 'Kupe', 'Mansa Moussa', 'Matthias Corvinus', 'Pachacuti', 'Eleanor of Aquitaine',
#"Aliénor d'Aquitaine", 'Lautaro', 'Dido',
## Rise and fall
#'Seondeok', 'Wilhelmine', 'Gengis Khan', 'Tamar', 'Chandgragupta', 'Poundmaker', 'Toqui', 'Robert the Bruce',
#'Shaka',
