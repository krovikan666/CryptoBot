import discord
from coinmarketcap import Market
from auth import token
from market_ids import coin_to_id

client = discord.Client()
market = Market()


@client.event
async def on_ready():
    message = 'Taking over the world'
    print('The bot is ready!')
    await client.change_presence(game=discord.Game(name=message))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('`crypto'):
        split_message = message.content.split(' ')
        if len(message.content.split(' ')) == 1:
            await client.send_message(
                message.channel,
                'Please enter a command'
            )
            return
        elif len(message.content.split(' ')) == 2:
            currency = 'CAD'
        else:
            currency = message.content.split(' ')[2].upper()
        coin = split_message[1].upper()

        try:
            data = market.ticker(coin_to_id[coin], convert=currency)
        except KeyError:
            await client.send_message(
                message.channel,
                'Invalid cryptocurrency: {}'.format(coin)
            )
            return

        try:
            price = data['data']['quotes'][currency]['price']
        except KeyError:
            await client.send_message(
                message.channel,
                'Invalid fiat current: {}'.format(currency)
            )
            return

        await client.send_message(
            message.channel,
            'Price of {} in {} : ${:.2f}'.format(coin, currency, price)
        )
    else:
        return

client.run(token)