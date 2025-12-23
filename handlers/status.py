from aiogram import Router, types
from aiogram.filters import Command

import services.monitoring as Monitor

router = Router()


# /status
@router.message(Command('status'))
async def status(message: types.Message):
    await message.answer(f'''
CPU:
    Loading(%): {Monitor.CPU.load()}%
    Temperature: {Monitor.CPU.temp()}C

RAM:
    Total(GB): {Monitor.RAM.total()}GB
    Used(GB & %): {Monitor.RAM.used()}GB({Monitor.RAM.used_per()}%)
    Free(GB): {Monitor.RAM.free()}GB

DISK:
    Total(GB): {Monitor.DISK.total()}GB
    Used(GB & %): {Monitor.DISK.used()}GB({Monitor.DISK.used_per()}%)
    Free(GB): {Monitor.DISK.free()}GB

OTHER:
    Average_loading(%): {Monitor.SYSTEM.avr_load()}%
''')
