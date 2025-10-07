from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram import types, Bot
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

model_name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    device=-1 
)



guest_welcome_router = Router(name="guest_welcome")

@guest_welcome_router.message(Command("start"))
async def guest_welcome(message: Message, state: FSMContext):
    await message.answer("Hello!")


@guest_welcome_router.message()
async def generate_text(message: types.Message, bot: Bot):
    await bot.send_chat_action(message.chat.id, "typing")
    
    generated_text = generator(
        message.text,
        max_length=100,
        num_return_sequences=1,
        temperature=0.7,
        repetition_penalty=1.5
    )[0]['generated_text']

    await message.answer(generated_text[:4096])
        