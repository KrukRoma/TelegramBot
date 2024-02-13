from aiogram.types import BotCommand

listOfCommands = [
    BotCommand(command="menu", description="Show all of functions"),
    BotCommand(command="start", description="Start bot"),
    BotCommand(command="help", description="Help"),
    BotCommand(command="echo", description="Reply your message"),
    BotCommand(command="duck", description="Return random duck image"),
    BotCommand(command="cat", description="Return random cat image"),
    BotCommand(command="dog", description="Return random dog image"),
    BotCommand(command="clearbit", description="Return clearbit logo"),
    BotCommand(command="photo", description="Return photo")
]