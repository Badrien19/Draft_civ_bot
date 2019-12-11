# bot.py
import discord
import random
from discord import Game
from discord.ext import commands

client = discord.Client()
client = commands.Bot(command_prefix = '.', case_insensitive=True)

l_civilisation = [
		'Frédéric Barberousse', 'Theodore Roosevelt', 'Victoria', 'Saladin', 'Pierre II', 'Qin Shi Huang',
		'Alphonse Ier du Kongo','Cléopâtre', 'Philippe II', 'Catherine de Médicis', 'Périclès', 'Gorgô', 'Gandhi',
		'Hōjō Tokimune', 'Harald Hardrada', 'Trajan', 'Pierre Ier le Grand', 'Tomyris','Gilgamesh', 'Moctezuma Ier',
		# dlc
		'Hedwige', 'Alexandre le grand','Cyrus II', 'Dyah Gitarja','Jayavrman','John Curtin', 'Aminatoré',
		# gathering storm
		'Wilfrid Laurier', 'Kupe', 'Mansa Moussa', 'Matthias Corvinus', 'Pachacuti',
		# Rise and fall
		'Seondeok', 'Wilhelmine', 'Gengis Khan', 'Tamar', 'Chandgragupta', 'Poundmaker', 'Toqui', 'Robert the Bruce', 'Shaka',
	]
	# 41 civ
@client.command(name = 'civ',
				aliases=['civilization', 'civilisation', 'civ6'])
async def draft(ctx):
	random.shuffle(l_civilisation)
	i = 0
	a = 0
	for a in 9
		await ctx.send(f'Joueur {i}: {l_civilisation[i]}, {l_civilisation[i+1]}, {l_civilisation[i+2]}, {l_civilisation[i+3]}')
		i += 4
		a += 1

client.run('NjUxNTQ4MjY4MDMwODUzMTY0.XfDlrg.25e2eN4nrsGSXInxjeOWWlKVW-w')