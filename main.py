from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram import Router
from fastapi import FastAPI, Request
from aiogram.types import Update, BotCommand
import uvicorn
from config import BOT_TOKEN, WEBHOOK_PATH, WEBHOOK_URL
from handlers import register_all_routers

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher()
router = Router()

# Регистрируем роутеры
register_all_routers(dp)
app = FastAPI()

@app.post(WEBHOOK_PATH)
async def telegram_webhook(req: Request):
    data = await req.json()
    print(data)
    update = Update.model_validate(data)
    await dp.feed_update(bot, update)
    return {"ok": True}

# TODO: change commands
@app.on_event("startup")
async def on_startup():
    print(f"Setting webhook to: {WEBHOOK_URL}")
    await bot.set_webhook(WEBHOOK_URL)
    print("Bot started!")

@app.on_event("shutdown")
async def on_shutdown():
    await bot.delete_webhook()
    await bot.session.close()
    print("Bot stopped!")

@app.get("/")
async def root():
    return {"status": "Bot is running"}
