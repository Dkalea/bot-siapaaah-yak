import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def boszen(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}bosen?liburan dong,ko malah les')

@bot.command()
async def contoh_mendaur_ulang_sampah(ctx):
    await ctx.send(f'''1.Kardus dan Sedotan Bekas Menjadi Kotak Tisu.
2.Botol Bekas dan Kain Perca Jadi Tempat Pensil.
3.Toples Bekas Menjadi Toples Serbaguna.''')

@bot.command()
async def tips_mengurangi_sampah(ctx):
    await ctx.send(f'''1.biasakan membawa tas belanja/botol minum saat keluar rumah
2.tidak menggunakan sedotan plastik
3.recycle
4.tidak membeli makanan dr luar''')


@bot.command()
async def cara_mendaur_ulang_sampah(ctx):
    await ctx.send(f'''1.Pemilahan dan Pemisahan
                   2.Menggunakan Kontainer Daur Ulang
                   3.Mengurangi Penggunaan Bahan Sulit Didaur Ulang
                   4.Mengikuti Panduan dan Peraturan Setempat''')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def mem(ctx):
    with open('M2L1/Slide4.jpg', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

bot.run("")
