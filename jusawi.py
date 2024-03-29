# ===== Imports =====
import asyncio, os, discord, d20, time, get_character_sheet, re
from discord.ext import commands

# ===== Bot Config =====
prefix = 'j;'
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = prefix, intents = intents)

bot.remove_command("help")

# ===== Functions =====
def command_timestamp(cmd, ctx):
	return f"{time.asctime(time.localtime())} | Received `{cmd}` request by {ctx.author} from {ctx.guild}."

def embed(title = None, desc = None, color = (255, 255, 255), foot = None, img = None, auth = None, fields = None, buttons = None):
	r, g, b = color
	embed = discord.Embed(title = title, description = desc, color = discord.Color.from_rgb(r, g, b))
	embed.set_footer(foot)
	embed.set_thumbnail(img)
	embed.set_author(auth)
	if fields:
		for k in fields.keys():
			embed.add_field(k, fields[k], False)
	if buttons:
		for b in buttons:
			pass
			# TODO : buttons
	return embed

def get_spreadsheet_id(url):
	return re.findall("(d\/[a-zA-Z0-9-_]+)", url)[0].split('/')[1]

# ===== Asynchronous Functions (Commands) =====
@bot.event
async def on_ready():
	""" Readies the Discord client. """
	print(time.asctime(time.localtime()) + " | Jusawi-ko is online!")
	await bot.change_presence(activity = discord.Game(name = "Library of Ruina | j;help"))

@bot.command()
async def help(ctx):
	""" Display this message! """
	print(command_timestamp("help", ctx))
	await ctx.send("`Jusawi-ko Help!`\n```Help Menu:\nHelp - Display this message!\nAbout - About Jusawi-ko.\nPing - Request a ping!\nRoll (`r`) - Roll a dice!\nImport - Import a character sheet!\nUpdate - Update a character's sheet\nCharacter (`char`) - Display current character!\nSheet - Display the current\nRemove Character - Removes a character. Be careful!\nBreak (`br`) - Prints a scene break.\nChallenge Roll (`c`) - Roll a challenge roll!```")

	# Embed form
	'''
	cmd_name = ["Help", "About", "Ping", "Roll", "Import", "Update", "Character", "Sheet", "Remove Character", "Break"]
	cmd_desc = ["Display this message!", "About Jusawi-ko.", "Request a ping!", "Roll a dice!", "Import a character sheet!", "Update a character's sheet!", "Display current character!", "Display the current character's sheet!", "Removes a character. Be careful!", "Prints a scene break."]
	cmd_help = {cmd_name[i]: cmd_desc[i] for i in range(len(cmd_name))}
	await ctx.send(embed(title = "Jusawi-ko Help!", desc = "Help Menu", color = (255, 255, 255), foot = "Jusawi-ko is made by WolfPai!", fields = cmd_help))
	'''
@bot.command()
async def about(ctx):
	""" About Jusawi-ko. """
	print(command_timestamp("about", ctx))
	await ctx.send("`About Jusawi-ko!`\nJusawi-ko is a Discord bot designed to help with managing Project Moon Table Roleplay Game character. Currently uses the Community Rules 3.0\nOriginally designed for Kawazoi Office, with love! :heart:\nLook at the source code here: https://github.com/Wolf-Pai/jusawi-ko")

	'''
	about = {"About Jusawi-ko": "Jusawi-ko is a Discord bot designed to help with managing Project Moon Tabletop Roleplay Game characters. Currently uses the Community Rules 3.0\n\nOriginally designed for Kawazoi Office, with love :heart:.\nLook at the source code here: https://github.com/Wolf-Pai/jusawi-ko"}
	await ctx.send(embed("About Jusawi-ko!", "About", (255, 255, 255), "Jusawi-ko is made by WolfPai!", None, None, about))
	'''

@bot.command()
async def ping(ctx):
	""" Request a ping! """
	print(command_timestamp("ping", ctx))
	if round(bot.latency) < 10:
		await ctx.send(f"Ping: {round(bot.latency * 1000, 3)} ms\nThat's {round(10 / bot.latency)} times faster than a WARP Train!")
	elif round(bot.latency) == 10:
		await ctx.send(f"Ping: {round(bot.latency * 1000)} ms\nThat's... the same speed as a WARP Train!")
	else:
		await ctx.send(f"Ping: {round(bot.latency * 1000, 3)} ms\nThat's very slow... {round(10 / bot.latency)} times slower than a WARP Train.")

@bot.command(aliases = ['r'])
async def roll(ctx):
	""" Roll a dice! """
	print(command_timestamp("roll", ctx))
	try:
		await ctx.send(f"{str(d20.roll(ctx.message.content.split(sep = ' ', maxsplit = 1)[1]))}")
	except Exception as e:
		print(e)

@bot.command(aliases = ['c'])
async def challenge(ctx, stat):
	""" Roll a challenge roll! """
	print(command_timestamp("challenge", ctx))
	try:
		stat = stat.lower()
		if stat in "fortitude":
			pass
		elif stat in "prudence":
			pass
		elif stat in "justice":
			pass
		elif stat in "charm":
			pass
		elif stat in "insight":
			pass
		else:
			pass
	except Exception as e:
		print(e)

@bot.command(aliases = ['import'])
async def thank_you_cowts(ctx, url):
	""" Import a character sheet! """
	""" Thanks to CowTs for maintaining the Project Moon TTRPG Character Sheet! Jusawi-ko couldn't have been possible without you! """
	print(command_timestamp("import", ctx))
	try:
		with open("venv/playerdata", 'r') as datafile:
			for line in datafile:
				if line[0] == str(ctx.message.author.name) and list(json.loads(line).keys())[1] == get_spreadsheet_id(url):
					await ctx.send("This character already exists! Use the `update` command to update instead.")
				return
		with open("venv/playerdata", 'a') as datafile:
			data = [ctx.message.author.name, get_character_sheet.get_character(url)]
			datafile.write(str(data))
			with open("venv/activeplayer", 'a') as active:
				player = [ctx.message.author.name, list(data[1].keys())[0]]
				active.write(str(player))
			await ctx.send("Successful `import`!")
			return
	except Exception as e:
		print(e)
		await ctx.send("This isn't a URL...")

@bot.command()
async def update(ctx, charname):
	""" Update a character's sheet! """
	print(command_timestamp("update", ctx))
	try:
		with open("venv/playerdata", 'r') as datafile:
			line_i, line_j  = 0, 0
			for line in datafile:
				if line[0] == str(ctx.message.author.name) and line[1][get_spreadsheet_id(url)][0] == charname.lower():
					with open("venv/playerdata", 'w') as datafile:
						for line in datafile:
							if line_i != line_j:
								datafile.write(str(line))
					with open("venv/playerdata", 'a') as datafile:
						data = [ctx.message.author.name, get_character_sheet.get_character(url)]
						datafile.write(str(data))
					await ctx.send(charname + " updated!")
					return
				elif line[0] == str(ctx.message.author.name):
					# list all player characters, because char fail
					await ctx.send(charname + " doesn't seem to exist...\nHere's a list of your characters:\n")
					return
				line_i += 1

	except Exception as e:
		print(e)

@bot.command(aliases = ['char'])
async def character(ctx, *args):
	# Display with embed
	# Remember arg[1] is char, if none, default
	# On arg fail, do list chars with Number Select

	""" Display current character! """
	print(command_timestamp("character", ctx))
	try:
		with open("venv/activeplayer", 'r'):
			pass
		await ctx.send("Successful `char`!")
	except Exception as e:
		print(e)

@bot.command()
async def sheet(ctx, *args):
	# Somehow display with embed
	# Remember arg[1] is char, if none, default
	# On arg fail, do list chars with Number Select

	""" Display the current character's sheet! """
	print(command_timestamp("sheet", ctx))
	try:
		await ctx.send("Successful `sheet`!")
	except Exception as e:
		print(e)

@bot.command()
async def removecharacter(ctx, char):
	# Similar to the j;update r/w loop except requested
	# On fail, list chars !! NO SINGLE BUTTON: NUMBER !!

	""" Removes a character. Be careful! """

# def pin_message()
# Try and pin a message; usually will be used for init tracking

@bot.command(aliases = ['i', 'init'])
async def initiative(ctx):
	""" Initiates combat! """
	print(command_timestamp("init", ctx))
	try:
		await ctx.send("Init Begin!")
	except Exception as e:
		print(e)

@bot.command(aliases = ['break'])
async def br(ctx):
	""" Prints a scene break. """
	print(command_timestamp("break", ctx))
	try:
		await ctx.send("```\n\n\n```")
	except Exception as e:
		print(e)

# ===== Exception Handling =====
@roll.error
async def roll_error(ctx, error):
	""" Exception handling for `roll` """
	if isinstance(error, commands.CommandInvokeError):
		await ctx.send("Missing a dice!")

@challenge.error
async def challenge_error(ctx, error):
	""" Exception handling for `challenge` """
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send("Missing a stat for the challenge roll!")

@thank_you_cowts.error
async def import_error(ctx, error):
	""" Exception handling for `import` """
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send("Missing a spreadsheet URL!")

# ===== Start Discord Bot =====
with open(os.path.join(os.environ['VIRTUAL_ENV'] + '/discord_token.txt'), 'r') as token_file:
	token = token_file.read()
	bot.run(token)
