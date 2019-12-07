import os
import discord

client = discord.Client()

TOKEN_AUTH = "YOUR_USER_TOKEN"


async def steal_emojis():
    while True:
        source = input("Enter in source discord id (server to copy emojis from):\n")
        source_guild = None
        for guild in client.guilds:
            if str(guild.id) == source:
                source_guild = guild
        if source_guild:
            print("Found {} successfully. Loading Emojis.".format(source_guild.name))
        else:
            print("Did not find that server, please check the id.")
            continue
        emojis = source_guild.emojis
        if len(emojis) > 0:
            print("Found {} emojis.".format(len(emojis)))
        else:
            print("We did not find any emojis.")
            continue
        path = os.getcwd() + '\\' + "emojis" + '\\'
        try:
            os.mkdir(path)
        except:
            pass
        for emoji in emojis:
            await emoji.url.save(path + "{}.png".format(emoji.name))
        print("Emojis saved.")
        break
    exit()


async def upload_emojis():
    destination = input("Enter in the destination discord id. You must have permission to upload emojis:\n")
    destination_guild = None
    for guild in client.guilds:
        if str(guild.id) == destination:
            destination_guild = guild
    if destination_guild:
        print("Found {} successfully.".format(destination_guild.name))
    pass
    path = os.getcwd() + '\\' + "emojis" + '\\'
    emoji_files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    for file in emoji_files:
        with open(path + file, 'rb') as image:
            bytes = image.read()
            name = os.path.basename(file).split('.')[0]
            await destination_guild.create_custom_emoji(name=name, image=bytes)
            print("Uploaded {}.".format(name))
    print("Emoji upload complete")
    exit()


@client.event
async def on_ready():
    print('=====================')
    print('Discord Emoji Stealer')
    print('github.com/cxmplex')
    print("=====================\n")
    option = input("Please select an option:\n[1] = Steal Emojis || [2] = Upload Emojis\n")
    while option not in ["1", "2"]:
        print("You did not choose an option.")
        option = input("Please select an option:\n[1] = Steal Emojis || [2] = Upload Emojis\n")
    if option == "1":
        await steal_emojis()
    else:
        await upload_emojis()


client.run(TOKEN_AUTH, bot=False)
