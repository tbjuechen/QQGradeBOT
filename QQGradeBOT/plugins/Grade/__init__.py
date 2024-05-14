from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot,MessageEvent,MessageSegment
from nonebot_plugin_alconna import UniMessage

# import QQGradeBOT.plugins.Grade.config

import requests

grade = on_command('打分')

@grade.handle()
async def update_photo(bot: Bot, message:MessageEvent):
    # message = MessageSegment.image(file = 'http://irain.cc:2024/photo')
    url = 'http://irain.cc:2024/photo'
    response = requests.get(url)
    img_data = response.content
    await UniMessage.image(raw=img_data).send()
    
    
