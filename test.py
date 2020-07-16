import discord
from discord import utils

import config

class MyClient(discord.Client):
	async def on_ready(self):
		print('Logge on as {0}!'.format(self.user))

	async def on_raw_reaction_add(self, payload):
		if payload.message_id == config.POST_ID:
			channel = self.get_channel(payload.channel_id) # получаем объект канала
			message = await channel.fetch_message(payload.message_id) # получаем объект сообщения
			member = utils.get(message.guild.members, id=payload.user_id) # получаем объект пользавателя

			try:
				emoji = str(payload.emoji)
				role = utils.get(message.guild.roles, id=config.ROLES[emoji])

				if(len([i for i in member.roles if i.id not in config.EXCROLES]) <= config.MAX_ROLES_PER_USER):
					await member.add_roles(role)
					print('[SUCCESS] User {0.display_name} has been granted with role {1.name}'.format(member, role))
				else:
					await message.remove_reaction(payload.emoji, member)
					print('[ERROR] Too many roles for user {0.display_name}'.format(member))

			except KeyError as e:
				print('[ERROR] KeyError, no role found for ' + emoji)
			except Exception as e:
				print(repr(e))

	async def on_raw_reaction_remove(self, payload):
		channel = self.get_channel(payload.channel_id)
		message = await channel.fetch_message(payload.message_id)
		member = utils.get(message.guild.members, id=payload.user_id)

		try:
			emoji = str(payload.emoji) # емоджик который выбрал юзер
			role = utils.get(message.guild.roles, id=config.ROLES[emoji]) # объект выброой роли (если есть)

			await member.remove_roles(role)
			print('[SUCCESS] Role {1.name} has been remove for user {0.display_name}'.format(member, role))

		except KeyError as e:
			print('[ERROR] KeyError, on role found for ' + emoji)
		except Exception as e:
			print(repr(e))

	async def on_message(self, message):
		print('Message from {0.author}: {0.content}'.format(message))

#RUN
client = MyClient()
client.run(config.TOKEN)
import discord
from discord import utils

import config

class MyClient(discord.Client):
	async def on_read(self):
		print('Logged on as {0}!'.format(self.user))

	async def on_raw_reaction_add(self, payload):
		if payload.message_id == config.POST_ID:
			channel = self.get_channel(payload.channel_id)
			message = await channel.fetch_message(payload.message_id)
			member = utils.get(message.guild.members, id=payload.user_id)

			try:
				emoji = str(payload.emoji) # эмоджик который выбрал юзер
				role = utils.get(message.guild.roles, id=config.ROLES[emoji]) # объект выбранной роли (если есть)
			
				if(len([i for i in member.roles if i.id not in config.EXCROLES]) <= config.MAX_ROLES_PER_USER):
					await member.add_roles(role)
					print('[SUCCESS] User {0.display_name} has been granted with role {1.name}'.format(member, role))
				else:
					await message.remove_reaction(payload.emoji, member)
					print('[ERROR] Too many roles for user {0.display_name}'.format(member))
			
			except KeyError as e:
				print('[ERROR] KeyError, no role found for ' + emoji)
			except Exception as e:
				print(repr(e))

	async def on_raw_reaction_remove(self, payload):
		channel = self.get_channel(payload.channel_id) # получаем объект канала
		message = await channel.fetch_message(payload.message_id) # получаем объект сообщения
		member = utils.get(message.guild.members, id=payload.user_id) # получаем объект пользователя который поставил реакцию

		try:
			emoji = str(payload.emoji) # эмоджик который выбрал юзер
			role = utils.get(message.guild.roles, id=config.ROLES[emoji]) # объект выбранной роли (если есть)

			await member.remove_roles(role)
			print('[SUCCESS] Role {1.name} has been remove for user {0.display_name}'.format(member, role))

		except KeyError as e:
			print('[ERROR] KeyError, no role found for ' + emoji)
		except Exception as e:
			print(repr(e))

#RUN
client = MyClient()
client.run(config.TOKEN)