from aiogram import Router, types
from aiogram.filters import Command

router = Router()
allowed_command = ['ls', 'pwd', 'whoami', 'uname', 'df', 'free']

# /execute
