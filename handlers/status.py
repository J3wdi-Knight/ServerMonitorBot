from aiogram import Router, types
from aiogram.filters import Command
import psutil

router = Router()

GB = 1024 ** 3

def cpu():
    load = psutil.cpu_percent()
    temp = psutil.sensors_temperatures()['k10temp'][0].current

    return {
        'load_per': load,
        'temp': temp
    }

async def ram():
    total = round(psutil.virtual_memory().total / GB, 2)
    used = round(psutil.virtual_memory().used / GB, 2)
    used_per = psutil.virtual_memory().percent
    free = round(psutil.virtual_memory().available / GB, 2)

async def disk():
    total = round(psutil.disk_usage('/home').total / GB, 2)
    used = round(psutil.disk_usage('/home').used / GB, 2)
    used_per = psutil.disk_usage('/home').percent
    free = round(psutil.disk_usage('/home').free / GB, 2)

def syst():
    # Average system load on 1 minute(system load * core nums)
    avr_load = psutil.getloadavg()[0] * psutil.cpu_count()


# /status
@router.message(Command('status'))
async def status():
    message.answer(f'''
CPU:
    Loading(%): {cpu().load}%
    Temperature: {cpu().temp}C

RAM:
    Total(GB): {ram().load}GB
    Used(GB & %): {ram().used}GB({ram().used_per})
    Free(GB): {ram().free}GB

DISK:
    Total(GB): {disk().total}GB
    Used(GB & %): {disk().used}GB({disk().used_per})
    Free(GB): {disk().free}GB

OTHER:
    Average_loading(%): {syst().avr_load}
''')
