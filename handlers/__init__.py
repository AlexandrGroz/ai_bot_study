from aiogram import Dispatcher
from .guest_welcome import guest_welcome_router


def register_all_routers(dp: Dispatcher):
    dp.include_router(guest_welcome_router)

