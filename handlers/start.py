from aiogram import Router, types
from aiogram.filters import Command

router = Router()

# /start
@router.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer('Hello!')

@router.message(Command('help'))
async def cmd_helpme(message: types.Message):
    await message.answer('''
/start - greating
/status - check up CPU, RAM, Disk and uptime
/alert - turn on/off notifies
/execute - safety execute command
''')
