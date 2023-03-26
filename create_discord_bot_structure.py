import os

folders = [
    "discord_bot/bot/cogs",
    "discord_bot/bot/utils",
    "discord_bot/data",
    "discord_bot/logs",
]

files = [
    "discord_bot/bot/cogs/__init__.py",
    "discord_bot/bot/utils/__init__.py",
    "discord_bot/bot/__init__.py",
    "discord_bot/bot/config.py",
    "discord_bot/bot/main.py",
    "discord_bot/.gitignore",
    "discord_bot/.env",
    "discord_bot/requirements.txt",
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for file in files:
    open(file, "w").close()
