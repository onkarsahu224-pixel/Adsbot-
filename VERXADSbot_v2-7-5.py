"""
verx ads bot – Professional Telegram Multi‑Account Advertising Bot
Optimized for Render (no file dependencies for sessions)
Owner: @owning07 | Support: t.me/verxchat | Channel: t.me/GAMERSX07
"""

# ==================== AUTO-INSTALL MISSING PACKAGES ====================
import subprocess, sys

def _install(pkg, import_name=None):
    name = import_name or pkg
    try:
        __import__(name)
    except ImportError:
        print(f"[setup] Installing {pkg} ...")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", pkg, "--quiet"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
        print(f"[setup] {pkg} installed.")

_install("cryptography")
_install("telethon")
_install("pyrogram")
_install("TgCrypto", "tgcrypto")
_install("groq")
_install("aiohttp")
# ======================================================================

# ==================== CONFIGURATION ====================
# All configurable items are placed here for easy customization

BOT_TOKEN = "8622570765:AAF93hU0av2-5CxjbyYH8DCTRMtp_D7gsBY"
OWNER_IDS = [7879101503]          # List of owner user IDs
OWNER_USERNAME = "Owning07"       # Owner's username (without @) for contact button
BOT_USERNAME = "VerxAdsbot"       # Your bot's username (without @) for name enforcement

# ==================== VERX LOGGER BOT CONFIG ====================
LOGGER_BOT_TOKEN   = "8415630862:AAFJFVhxxAgqkVi5B8Dx7wcScFV57i7MR04"
LOGGER_BOT_USERNAME = "verxloggerbot"
# All logs go to this chat ID (defaults to the first OWNER_ID — change if you have a dedicated log group)
LOGGER_TARGET_CHAT = 7879101503   # same as OWNER_IDS[0]; set to a group/channel ID if preferred

GROQ_API_KEY = "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"
API_ID = 30668518
API_HASH = "21074cfa32d2d0d8e18c95c0c0a72054"

# Required channels for access
REQUIRED_CHANNELS = [
    {"username": "GAMERSX07", "link": "https://t.me/GAMERSX07"},
    {"username": "verxchat", "link": "https://t.me/verxchat"}
]

# Paths
DB_PATH = "verx_ads.db"
ENCRYPTION_KEY_FILE = "encryption.key"

# Limits – Free vs Premium vs Elite
# Free
FREE_MAX_ACCOUNTS = 1
FREE_MAX_GROUPS = 5
FREE_MAX_MESSAGES = 1
FREE_MAX_TAGS = 5          # can view tagging but toggle is locked
FREE_AUTO_REPLY = False
FREE_SET_BIO = False       # bio auto-set globally; no custom
FREE_INTERVAL_CUSTOM = False
FREE_INTERVAL_MIN = 3600   # 1 hour minimum for free tier
FREE_TAGGING_LOCKED = True

# Premium
PREMIUM_MAX_ACCOUNTS = 3
PREMIUM_MAX_GROUPS = 10
PREMIUM_MAX_MESSAGES = 5
PREMIUM_MAX_TAGS = 5
PREMIUM_AUTO_REPLY = False
PREMIUM_SET_BIO = True
PREMIUM_INTERVAL_CUSTOM = False  # presets only
PREMIUM_INTERVAL_MIN = 300       # 5 min minimum
PREMIUM_TAGGING_LOCKED = False

# Elite
ELITE_MAX_ACCOUNTS = 10
ELITE_MAX_GROUPS = 30
ELITE_MAX_MESSAGES = 20
ELITE_MAX_TAGS = 20
ELITE_AUTO_REPLY = True
ELITE_SET_BIO = True
ELITE_INTERVAL_CUSTOM = True
ELITE_INTERVAL_MIN = 300   # 5 min safe floor — original 5s caused ban risk
ELITE_TAGGING_LOCKED = False

DEFAULT_INTERVAL = 3600    # 1 hour default (free-safe)
MIN_INTERVAL = 300         # 5 min absolute floor — anything lower = ban risk

# ==================== ANTI-BAN CONFIG ====================
# Random delay (seconds) between sending to each group — looks human
BATCH_DELAY_RANGE            = (20, 50)
# Extra sleep after a FloodWait clears — don't immediately retry
FLOOD_EXTRA_JITTER           = (45, 120)
# Delay before requesting the login OTP — prevents scripted-login detection
LOGIN_PRE_CODE_DELAY         = (3.0, 8.0)
# Delay between receiving OTP prompt and calling sign_in — mimics human typing
LOGIN_PRE_SIGNIN_DELAY       = (5.0, 12.0)
# Delay before updating profile (bio/name) after account is added
PROFILE_UPDATE_DELAY         = (10.0, 25.0)
# Delay between each account during a force-push bio/name operation
# Long range (3–8 min) mimics a human manually editing accounts one-by-one
# This is the single most important setting to prevent bulk-edit detection
FORCE_PUSH_INTER_ACCOUNT_DELAY = (180.0, 480.0)   # 3 – 8 minutes between accounts
# Extra cooldown after every 3 accounts (lets Telegram's heuristic window reset)
FORCE_PUSH_BATCH_COOLDOWN    = (600.0, 900.0)      # 10 – 15 min after every 3 accounts
FORCE_PUSH_BATCH_SIZE        = 3                   # accounts per batch before long cooldown
# Delay between individual group joins — Telegram flags fast bulk joining
GROUP_JOIN_DELAY             = (25, 55)
# Hard limit on how many groups one account can join per day
MAX_JOINS_PER_DAY            = 8
# Delay between member-scrape batch requests
MEMBER_SCRAPE_DELAY          = (3.0, 7.0)
# Auto-reply: minimum and maximum seconds to wait before sending reply
AUTOREPLY_MIN_DELAY          = 20
AUTOREPLY_MAX_DELAY          = 75
# How many auto-replies one account can send per hour (across all chats)
AUTOREPLY_HOURLY_CAP         = 6
# Minimum seconds between two replies to the same chat
AUTOREPLY_SAME_CHAT_COOLDOWN = 240
# Cooldown (seconds) applied to an account after any send error
ACCOUNT_ERROR_COOLDOWN       = 600   # 10 minutes
# Entity cache TTL (seconds)
ENTITY_CACHE_TTL             = 3600
# Daily send caps per tier
DAILY_CAP_FREE               = 25
DAILY_CAP_PREMIUM            = 80
DAILY_CAP_ELITE              = 200
DAILY_CAP_OWNER              = 9999
# Realistic Android device fingerprint — prevents Telegram detecting "Python script"
DEVICE_MODEL    = "Samsung Galaxy S23"
SYSTEM_VERSION  = "Android 14"
APP_VERSION     = "10.3.2"
LANG_CODE       = "en"
SYSTEM_LANG     = "en-US"

# Tagging
DEFAULT_TAGS_PER_MESSAGE = 1
MAX_TAGS_PER_MESSAGE = 50

# Auto‑reply – fixed global system prompt
GROQ_MODEL = "llama-3.3-70b-versatile"
MAX_REPLY_TOKENS = 100
REPLY_TEMPERATURE = 0.7
MAX_HISTORY_MESSAGES = 5

GLOBAL_AUTOREPLY_PROMPT = (
    "You are a helpful Telegram user. Be casual, friendly, and concise (1-2 sentences). "
    "Use emojis occasionally. Never mention being AI. Act like a normal human."
)

# Default bio / name enforced on free-tier accounts
DEFAULT_BIO = f"For similar advertisement userbot automation, use @{BOT_USERNAME}"
DEFAULT_NAME_SUFFIX = f"@{BOT_USERNAME}"

# Owner‑enforced bio requirement (can be toggled via owner panel)
DEFAULT_BIO_REQUIRED = False

# Cache TTL for target group IDs (seconds)
TARGET_GROUPS_CACHE_TTL = 60

# Logging – filter out noisy "Got difference for channel" logs from telethon
import logging
logging.getLogger('telethon.client.updates').setLevel(logging.WARNING)

# ==================== IMPORTS ====================

import os
import asyncio
import logging
import json
import time
import random
import re
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple, Set, Any
from collections import defaultdict
from cryptography.fernet import Fernet
import sqlite3
import groq
import aiohttp
from telethon import TelegramClient, events, functions, errors
from telethon.errors import (
    PhoneNumberInvalidError, SessionPasswordNeededError,
    FloodWaitError, PhoneCodeInvalidError, PhoneCodeExpiredError,
    UserDeactivatedBanError, UserDeactivatedError,
    AuthKeyUnregisteredError, AuthKeyDuplicatedError,
    PhoneNumberBannedError, UserRestrictedError,
    PeerFloodError, ChatWriteForbiddenError,
    UserBannedInChannelError, SlowModeWaitError,
)
from telethon.tl.functions.channels import GetParticipantsRequest, JoinChannelRequest
from telethon.tl.types import ChannelParticipantsSearch, Channel, Chat
from telethon.sessions import StringSession
from pyrogram import Client as PyroClient, filters, idle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message
from pyrogram.enums import ParseMode
from pyrogram.errors import UserNotParticipant

# ==================== LOGGING SETUP ====================

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('verx_ads.log'), logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

# ==================== EMBEDDED TUTORIAL ====================
# The full interactive tutorial HTML, base64-encoded so the bot
# is a single self-contained file with zero external dependencies.
import base64 as _b64, io as _io
_TUTORIAL_B64 = (
    "PCFET0NUWVBFIGh0bWw+CjxodG1sIGxhbmc9ImVuIj4KPGhlYWQ+CjxtZXRhIGNoYXJzZXQ9IlVURi04"
    "Ij4KPG1ldGEgbmFtZT0idmlld3BvcnQiIGNvbnRlbnQ9IndpZHRoPWRldmljZS13aWR0aCwgaW5pdGlh"
    "bC1zY2FsZT0xLjAiPgo8dGl0bGU+VmVyeCBBZHMgQm90IOKAkyBDb21wbGV0ZSBUdXRvcmlhbDwvdGl0"
    "bGU+CjxsaW5rIHJlbD0icHJlY29ubmVjdCIgaHJlZj0iaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNv"
    "bSI+CjxsaW5rIGhyZWY9Imh0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9T3V0"
    "Zml0OndnaHRAMzAwOzQwMDs1MDA7NjAwOzcwMDs4MDA7OTAwJmZhbWlseT1KZXRCcmFpbnMrTW9ubzp3"
    "Z2h0QDQwMDs1MDA7NzAwJmRpc3BsYXk9c3dhcCIgcmVsPSJzdHlsZXNoZWV0Ij4KPHN0eWxlPgo6cm9v"
    "dCB7CiAgLS1iZzogICAgICAgIzA3MDkwZjsKICAtLXN1cmZhY2U6ICAjMGUxMzIwOwogIC0tY2FyZDog"
    "ICAgICMxMTE4Mjc7CiAgLS1ib3JkZXI6ICAgIzFlMmQ0MjsKICAtLWFjY2VudDogICAjMmVhOGUyOwog"
    "IC0tZ29sZDogICAgICNmNWM1NDI7CiAgLS1wdXJwbGU6ICAgI2E3OGJmYTsKICAtLWdyZWVuOiAgICAj"
    "NGFkZTgwOwogIC0tcmVkOiAgICAgICNmODcxNzE7CiAgLS10ZXh0OiAgICAgI2UyZWFmNTsKICAtLW11"
    "dGVkOiAgICAjNmI3ZmEwOwogIC0tdGctb3V0OiAgICMxYTNkNWM7CiAgLS10Zy1pbjogICAgIzE0MWYz"
    "MDsKfQoqe21hcmdpbjowO3BhZGRpbmc6MDtib3gtc2l6aW5nOmJvcmRlci1ib3h9Cmh0bWx7c2Nyb2xs"
    "LWJlaGF2aW9yOnNtb290aH0KYm9keXsKICBiYWNrZ3JvdW5kOnZhcigtLWJnKTsKICBmb250LWZhbWls"
    "eTonT3V0Zml0JyxzYW5zLXNlcmlmOwogIGNvbG9yOnZhcigtLXRleHQpOwogIG92ZXJmbG93LXg6aGlk"
    "ZGVuOwogIGxpbmUtaGVpZ2h0OjEuNjsKfQoKLyog4pSA4pSAIE5PSVNFIFRFWFRVUkUg4pSA4pSAICov"
    "CmJvZHk6OmJlZm9yZXsKICBjb250ZW50OicnO3Bvc2l0aW9uOmZpeGVkO2luc2V0OjA7CiAgYmFja2dy"
    "b3VuZC1pbWFnZTp1cmwoImRhdGE6aW1hZ2Uvc3ZnK3htbCwlM0Nzdmcgdmlld0JveD0nMCAwIDI1NiAy"
    "NTYnIHhtbG5zPSdodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyclM0UlM0NmaWx0ZXIgaWQ9J24nJTNF"
    "JTNDZmVUdXJidWxlbmNlIHR5cGU9J2ZyYWN0YWxOb2lzZScgYmFzZUZyZXF1ZW5jeT0nMC45JyBudW1P"
    "Y3RhdmVzPSc0JyBzdGl0Y2hUaWxlcz0nc3RpdGNoJy8lM0UlM0MvZmlsdGVyJTNFJTNDcmVjdCB3aWR0"
    "aD0nMTAwJTI1JyBoZWlnaHQ9JzEwMCUyNScgZmlsdGVyPSd1cmwoJTIzbiknIG9wYWNpdHk9JzAuMDQn"
    "LyUzRSUzQy9zdmclM0UiKTsKICBwb2ludGVyLWV2ZW50czpub25lO3otaW5kZXg6MDtvcGFjaXR5Oi41"
    "Owp9CgovKiDilIDilIAgU1RJQ0tZIE5BViDilIDilIAgKi8KbmF2ewogIHBvc2l0aW9uOnN0aWNreTt0"
    "b3A6MDt6LWluZGV4OjEwMDsKICBiYWNrZ3JvdW5kOnJnYmEoNyw5LDE1LC45Mik7CiAgYmFja2Ryb3At"
    "ZmlsdGVyOmJsdXIoMjBweCk7CiAgYm9yZGVyLWJvdHRvbToxcHggc29saWQgdmFyKC0tYm9yZGVyKTsK"
    "ICBwYWRkaW5nOjEycHggMjRweDsKICBkaXNwbGF5OmZsZXg7YWxpZ24taXRlbXM6Y2VudGVyO2dhcDox"
    "MnB4OwogIGZsZXgtd3JhcDp3cmFwOwp9Ci5uYXYtbG9nb3tmb250LXNpemU6MTVweDtmb250LXdlaWdo"
    "dDo4MDA7Y29sb3I6dmFyKC0tYWNjZW50KTtsZXR0ZXItc3BhY2luZzouNXB4O21hcmdpbi1yaWdodDph"
    "dXRvfQoubmF2LWxpbmt7CiAgZm9udC1zaXplOjEycHg7Zm9udC13ZWlnaHQ6NjAwOwogIGNvbG9yOnZh"
    "cigtLW11dGVkKTsKICB0ZXh0LWRlY29yYXRpb246bm9uZTsKICBwYWRkaW5nOjVweCAxMnB4OwogIGJv"
    "cmRlci1yYWRpdXM6OTlweDsKICBib3JkZXI6MXB4IHNvbGlkIHRyYW5zcGFyZW50OwogIHRyYW5zaXRp"
    "b246YWxsIC4yczsKICB3aGl0ZS1zcGFjZTpub3dyYXA7Cn0KLm5hdi1saW5rOmhvdmVye2NvbG9yOnZh"
    "cigtLXRleHQpO2JvcmRlci1jb2xvcjp2YXIoLS1ib3JkZXIpfQoubmF2LWxpbmsuYWN0aXZle2NvbG9y"
    "OiNmZmY7YmFja2dyb3VuZDp2YXIoLS1hY2NlbnQpO2JvcmRlci1jb2xvcjp2YXIoLS1hY2NlbnQpfQoK"
    "Lyog4pSA4pSAIEhFUk8g4pSA4pSAICovCi5oZXJvewogIHBvc2l0aW9uOnJlbGF0aXZlOwogIHRleHQt"
    "YWxpZ246Y2VudGVyOwogIHBhZGRpbmc6ODBweCAyMHB4IDYwcHg7CiAgb3ZlcmZsb3c6aGlkZGVuOwp9"
    "Ci5oZXJvLWdsb3d7CiAgcG9zaXRpb246YWJzb2x1dGU7dG9wOi0xMDBweDtsZWZ0OjUwJTt0cmFuc2Zv"
    "cm06dHJhbnNsYXRlWCgtNTAlKTsKICB3aWR0aDo3MDBweDtoZWlnaHQ6NTAwcHg7CiAgYmFja2dyb3Vu"
    "ZDpyYWRpYWwtZ3JhZGllbnQoZWxsaXBzZSxyZ2JhKDQ2LDE2OCwyMjYsLjEyKSAwJSx0cmFuc3BhcmVu"
    "dCA2NSUpOwogIHBvaW50ZXItZXZlbnRzOm5vbmU7Cn0KLmhlcm8tYmFkZ2V7CiAgZGlzcGxheTppbmxp"
    "bmUtZmxleDthbGlnbi1pdGVtczpjZW50ZXI7Z2FwOjZweDsKICBiYWNrZ3JvdW5kOnJnYmEoNDYsMTY4"
    "LDIyNiwuMSk7CiAgYm9yZGVyOjFweCBzb2xpZCByZ2JhKDQ2LDE2OCwyMjYsLjMpOwogIGJvcmRlci1y"
    "YWRpdXM6OTlweDtwYWRkaW5nOjVweCAxNnB4OwogIGZvbnQtc2l6ZToxMnB4O2ZvbnQtd2VpZ2h0Ojcw"
    "MDsKICBjb2xvcjp2YXIoLS1hY2NlbnQpO2xldHRlci1zcGFjaW5nOjFweDsKICB0ZXh0LXRyYW5zZm9y"
    "bTp1cHBlcmNhc2U7bWFyZ2luLWJvdHRvbToyMHB4OwogIGFuaW1hdGlvbjpmYWRlRG93biAuNnMgZWFz"
    "ZSBib3RoOwp9Ci5oZXJvIGgxewogIGZvbnQtc2l6ZTpjbGFtcCgzMnB4LDZ2dyw2NHB4KTsKICBmb250"
    "LXdlaWdodDo5MDA7bGluZS1oZWlnaHQ6MS4xOwogIGJhY2tncm91bmQ6bGluZWFyLWdyYWRpZW50KDE1"
    "MGRlZywjZmZmIDMwJSx2YXIoLS1hY2NlbnQpKTsKICAtd2Via2l0LWJhY2tncm91bmQtY2xpcDp0ZXh0"
    "Oy13ZWJraXQtdGV4dC1maWxsLWNvbG9yOnRyYW5zcGFyZW50OwogIGJhY2tncm91bmQtY2xpcDp0ZXh0"
    "OwogIGFuaW1hdGlvbjpmYWRlRG93biAuNnMgLjFzIGVhc2UgYm90aDsKfQouaGVybyBwewogIG1hcmdp"
    "bjoxNnB4IGF1dG8gMDttYXgtd2lkdGg6NTIwcHg7CiAgZm9udC1zaXplOjE3cHg7Y29sb3I6dmFyKC0t"
    "bXV0ZWQpO2ZvbnQtd2VpZ2h0OjQwMDsKICBhbmltYXRpb246ZmFkZURvd24gLjZzIC4ycyBlYXNlIGJv"
    "dGg7Cn0KLmhlcm8tYWN0aW9uc3sKICBtYXJnaW4tdG9wOjI4cHg7ZGlzcGxheTpmbGV4O2dhcDoxMnB4"
    "O2p1c3RpZnktY29udGVudDpjZW50ZXI7ZmxleC13cmFwOndyYXA7CiAgYW5pbWF0aW9uOmZhZGVEb3du"
    "IC42cyAuM3MgZWFzZSBib3RoOwp9Ci5idG57CiAgZGlzcGxheTppbmxpbmUtZmxleDthbGlnbi1pdGVt"
    "czpjZW50ZXI7Z2FwOjdweDsKICBwYWRkaW5nOjExcHggMjJweDtib3JkZXItcmFkaXVzOjEwcHg7CiAg"
    "Zm9udC1mYW1pbHk6J091dGZpdCcsc2Fucy1zZXJpZjtmb250LXNpemU6MTRweDtmb250LXdlaWdodDo3"
    "MDA7CiAgY3Vyc29yOnBvaW50ZXI7dGV4dC1kZWNvcmF0aW9uOm5vbmU7dHJhbnNpdGlvbjphbGwgLjJz"
    "O2JvcmRlcjpub25lOwp9Ci5idG4tcHJpbWFyeXtiYWNrZ3JvdW5kOnZhcigtLWFjY2VudCk7Y29sb3I6"
    "I2ZmZn0KLmJ0bi1wcmltYXJ5OmhvdmVye2JhY2tncm91bmQ6IzM4YzBmODt0cmFuc2Zvcm06dHJhbnNs"
    "YXRlWSgtMXB4KX0KLmJ0bi1vdXRsaW5le2JhY2tncm91bmQ6dHJhbnNwYXJlbnQ7Y29sb3I6dmFyKC0t"
    "dGV4dCk7Ym9yZGVyOjFweCBzb2xpZCB2YXIoLS1ib3JkZXIpfQouYnRuLW91dGxpbmU6aG92ZXJ7Ym9y"
    "ZGVyLWNvbG9yOnZhcigtLWFjY2VudCk7Y29sb3I6dmFyKC0tYWNjZW50KX0KCi8qIOKUgOKUgCBTRUNU"
    "SU9OIOKUgOKUgCAqLwouc2VjdGlvbnsKICBtYXgtd2lkdGg6OTYwcHg7bWFyZ2luOjAgYXV0bzsKICBw"
    "YWRkaW5nOjQwcHggMjBweCAyMHB4OwogIHBvc2l0aW9uOnJlbGF0aXZlO3otaW5kZXg6MTsKfQouc2Vj"
    "dGlvbi1oZWFkZXJ7CiAgZGlzcGxheTpmbGV4O2FsaWduLWl0ZW1zOmNlbnRlcjtnYXA6MTJweDsKICBt"
    "YXJnaW4tYm90dG9tOjI4cHg7Cn0KLnNlY3Rpb24tbnVtewogIHdpZHRoOjM2cHg7aGVpZ2h0OjM2cHg7"
    "Ym9yZGVyLXJhZGl1czoxMHB4OwogIGJhY2tncm91bmQ6cmdiYSg0NiwxNjgsMjI2LC4xNSk7CiAgYm9y"
    "ZGVyOjFweCBzb2xpZCByZ2JhKDQ2LDE2OCwyMjYsLjMpOwogIGRpc3BsYXk6ZmxleDthbGlnbi1pdGVt"
    "czpjZW50ZXI7anVzdGlmeS1jb250ZW50OmNlbnRlcjsKICBmb250LXNpemU6MTRweDtmb250LXdlaWdo"
    "dDo4MDA7Y29sb3I6dmFyKC0tYWNjZW50KTsKICBmbGV4LXNocmluazowOwp9Ci5zZWN0aW9uLXRpdGxl"
    "e2ZvbnQtc2l6ZToyMnB4O2ZvbnQtd2VpZ2h0OjgwMH0KLnNlY3Rpb24tc3Vie2NvbG9yOnZhcigtLW11"
    "dGVkKTtmb250LXNpemU6MTRweDttYXJnaW4tdG9wOjJweH0KCi8qIOKUgOKUgCBDQVJEUyDilIDilIAg"
    "Ki8KLmNhcmR7CiAgYmFja2dyb3VuZDp2YXIoLS1jYXJkKTsKICBib3JkZXI6MXB4IHNvbGlkIHZhcigt"
    "LWJvcmRlcik7CiAgYm9yZGVyLXJhZGl1czoxNnB4OwogIHBhZGRpbmc6MjJweCAyNHB4OwogIHRyYW5z"
    "aXRpb246Ym9yZGVyLWNvbG9yIC4yczsKfQouY2FyZDpob3Zlcntib3JkZXItY29sb3I6cmdiYSg0Niwx"
    "NjgsMjI2LC4zKX0KCi5ncmlkLTJ7ZGlzcGxheTpncmlkO2dyaWQtdGVtcGxhdGUtY29sdW1uczpyZXBl"
    "YXQoYXV0by1maXQsbWlubWF4KDI4MHB4LDFmcikpO2dhcDoxNnB4fQouZ3JpZC0ze2Rpc3BsYXk6Z3Jp"
    "ZDtncmlkLXRlbXBsYXRlLWNvbHVtbnM6cmVwZWF0KGF1dG8tZml0LG1pbm1heCgyMjBweCwxZnIpKTtn"
    "YXA6MTRweH0KCi8qIOKUgOKUgCBTVEVQIENBUkRTIOKUgOKUgCAqLwouc3RlcC1jYXJkewogIGJhY2tn"
    "cm91bmQ6dmFyKC0tY2FyZCk7Ym9yZGVyOjFweCBzb2xpZCB2YXIoLS1ib3JkZXIpOwogIGJvcmRlci1y"
    "YWRpdXM6MTZweDtwYWRkaW5nOjIwcHg7CiAgZGlzcGxheTpmbGV4O2dhcDoxNHB4O2FsaWduLWl0ZW1z"
    "OmZsZXgtc3RhcnQ7CiAgdHJhbnNpdGlvbjphbGwgLjJzOwp9Ci5zdGVwLWNhcmQ6aG92ZXJ7Ym9yZGVy"
    "LWNvbG9yOnJnYmEoNDYsMTY4LDIyNiwuMzUpO3RyYW5zZm9ybTp0cmFuc2xhdGVZKC0ycHgpfQouc3Rl"
    "cC1udW17CiAgd2lkdGg6MzJweDtoZWlnaHQ6MzJweDtib3JkZXItcmFkaXVzOjhweDsKICBiYWNrZ3Jv"
    "dW5kOnZhcigtLWFjY2VudCk7Y29sb3I6I2ZmZjsKICBmb250LXNpemU6MTNweDtmb250LXdlaWdodDo4"
    "MDA7CiAgZGlzcGxheTpmbGV4O2FsaWduLWl0ZW1zOmNlbnRlcjtqdXN0aWZ5LWNvbnRlbnQ6Y2VudGVy"
    "OwogIGZsZXgtc2hyaW5rOjA7Cn0KLnN0ZXAtYm9keSBoNHtmb250LXNpemU6MTVweDtmb250LXdlaWdo"
    "dDo3MDA7bWFyZ2luLWJvdHRvbTo0cHh9Ci5zdGVwLWJvZHkgcHtmb250LXNpemU6MTNweDtjb2xvcjp2"
    "YXIoLS1tdXRlZCk7bGluZS1oZWlnaHQ6MS41NX0KCi8qIOKUgOKUgCBQSE9ORSBNT0NLVVAg4pSA4pSA"
    "ICovCi5waG9uZXsKICB3aWR0aDoyNjBweDtmbGV4LXNocmluazowOwogIGJhY2tncm91bmQ6IzBkMTUy"
    "MDsKICBib3JkZXItcmFkaXVzOjM2cHg7CiAgYm9yZGVyOjJweCBzb2xpZCAjMWUyZDQyOwogIGJveC1z"
    "aGFkb3c6MCAwIDAgNXB4ICMwOTExMWQsMCAzMHB4IDYwcHggcmdiYSgwLDAsMCwuNik7CiAgb3ZlcmZs"
    "b3c6aGlkZGVuOwogIHBvc2l0aW9uOnJlbGF0aXZlOwp9Ci5waG9uZS1ub3RjaHsKICBoZWlnaHQ6MjJw"
    "eDtiYWNrZ3JvdW5kOiMwZDE1MjA7CiAgYm9yZGVyLXJhZGl1czowIDAgMTRweCAxNHB4OwogIHdpZHRo"
    "OjgwcHg7bWFyZ2luOjAgYXV0bzsKICBwb3NpdGlvbjpyZWxhdGl2ZTt6LWluZGV4OjI7Cn0KLnBob25l"
    "LWhlYWRlcnsKICBiYWNrZ3JvdW5kOiMxMTFmMzA7CiAgcGFkZGluZzo4cHggMTRweCAxMHB4OwogIGRp"
    "c3BsYXk6ZmxleDthbGlnbi1pdGVtczpjZW50ZXI7Z2FwOjhweDsKICBib3JkZXItYm90dG9tOjFweCBz"
    "b2xpZCB2YXIoLS1ib3JkZXIpOwp9Ci5waG9uZS1hdmF0YXJ7CiAgd2lkdGg6MzBweDtoZWlnaHQ6MzBw"
    "eDtib3JkZXItcmFkaXVzOjUwJTsKICBiYWNrZ3JvdW5kOmxpbmVhci1ncmFkaWVudCgxMzVkZWcsdmFy"
    "KC0tYWNjZW50KSwjMWE1ZjhhKTsKICBkaXNwbGF5OmZsZXg7YWxpZ24taXRlbXM6Y2VudGVyO2p1c3Rp"
    "ZnktY29udGVudDpjZW50ZXI7CiAgZm9udC1zaXplOjEzcHg7ZmxleC1zaHJpbms6MDsKfQoucGhvbmUt"
    "bmFtZXtmb250LXNpemU6MTNweDtmb250LXdlaWdodDo3MDB9Ci5waG9uZS1zdGF0dXN7Zm9udC1zaXpl"
    "OjEwcHg7Y29sb3I6dmFyKC0tZ3JlZW4pfQoucGhvbmUtYm9keXtwYWRkaW5nOjEwcHggOHB4O2Rpc3Bs"
    "YXk6ZmxleDtmbGV4LWRpcmVjdGlvbjpjb2x1bW47Z2FwOjVweDttaW4taGVpZ2h0OjIyMHB4fQoubXNn"
    "LXJvd3tkaXNwbGF5OmZsZXg7ZmxleC1kaXJlY3Rpb246Y29sdW1ufQoubXNnLXJvdy5vdXR7YWxpZ24t"
    "aXRlbXM6ZmxleC1lbmR9Ci5tc2ctcm93Lmlue2FsaWduLWl0ZW1zOmZsZXgtc3RhcnR9Ci5idWJibGV7"
    "CiAgcGFkZGluZzo3cHggMTBweDtib3JkZXItcmFkaXVzOjEycHg7CiAgZm9udC1zaXplOjExLjVweDts"
    "aW5lLWhlaWdodDoxLjU7CiAgbWF4LXdpZHRoOjkwJTsKfQouYnViYmxlLm91dHtiYWNrZ3JvdW5kOiMx"
    "YTNkNWM7Ym9yZGVyLWJvdHRvbS1yaWdodC1yYWRpdXM6M3B4fQouYnViYmxlLmlue2JhY2tncm91bmQ6"
    "IzE0MWYzMDtib3JkZXItYm90dG9tLWxlZnQtcmFkaXVzOjNweH0KLmJ1YmJsZSBie2NvbG9yOiM3ZGQz"
    "ZmN9Ci5rYntkaXNwbGF5OmZsZXg7ZmxleC1kaXJlY3Rpb246Y29sdW1uO2dhcDozcHg7bWFyZ2luLXRv"
    "cDo1cHg7d2lkdGg6MTAwJX0KLmtiLXJvd3tkaXNwbGF5OmZsZXg7Z2FwOjNweH0KLmtidG57CiAgZmxl"
    "eDoxO3BhZGRpbmc6NXB4IDRweDsKICBib3JkZXItcmFkaXVzOjdweDtmb250LXNpemU6MTBweDtmb250"
    "LXdlaWdodDo3MDA7CiAgdGV4dC1hbGlnbjpjZW50ZXI7Y3Vyc29yOnBvaW50ZXI7CiAgYmFja2dyb3Vu"
    "ZDpyZ2JhKDQ2LDE2OCwyMjYsLjEyKTsKICBib3JkZXI6MXB4IHNvbGlkIHJnYmEoNDYsMTY4LDIyNiwu"
    "MjUpOwogIGNvbG9yOiM3ZGQzZmM7d2hpdGUtc3BhY2U6bm93cmFwO292ZXJmbG93OmhpZGRlbjt0ZXh0"
    "LW92ZXJmbG93OmVsbGlwc2lzOwp9Ci5rYnRuLmd7YmFja2dyb3VuZDpyZ2JhKDc0LDIyMiwxMjgsLjEp"
    "O2JvcmRlci1jb2xvcjpyZ2JhKDc0LDIyMiwxMjgsLjI1KTtjb2xvcjojNGFkZTgwfQoua2J0bi55e2Jh"
    "Y2tncm91bmQ6cmdiYSgyNDUsMTk3LDY2LC4xKTtib3JkZXItY29sb3I6cmdiYSgyNDUsMTk3LDY2LC4y"
    "NSk7Y29sb3I6I2Y1YzU0Mn0KLmtidG4ucHtiYWNrZ3JvdW5kOnJnYmEoMTY3LDEzOSwyNTAsLjEpO2Jv"
    "cmRlci1jb2xvcjpyZ2JhKDE2NywxMzksMjUwLC4yNSk7Y29sb3I6I2E3OGJmYX0KLmtidG4ucntiYWNr"
    "Z3JvdW5kOnJnYmEoMjQ4LDExMywxMTMsLjEpO2JvcmRlci1jb2xvcjpyZ2JhKDI0OCwxMTMsMTEzLC4y"
    "NSk7Y29sb3I6I2Y4NzE3MX0KCi8qIOKUgOKUgCBERU1PIEJMT0NLIOKUgOKUgCAqLwouZGVtby1ibG9j"
    "a3sKICBkaXNwbGF5OmZsZXg7Z2FwOjI4cHg7YWxpZ24taXRlbXM6ZmxleC1zdGFydDtmbGV4LXdyYXA6"
    "d3JhcDsKICBtYXJnaW4tdG9wOjhweDsKfQouZGVtby10ZXh0e2ZsZXg6MTttaW4td2lkdGg6MjIwcHh9"
    "Ci5kZW1vLXRleHQgaDN7Zm9udC1zaXplOjE4cHg7Zm9udC13ZWlnaHQ6ODAwO21hcmdpbi1ib3R0b206"
    "OHB4fQouZGVtby10ZXh0IHB7Zm9udC1zaXplOjE0cHg7Y29sb3I6dmFyKC0tbXV0ZWQpO2xpbmUtaGVp"
    "Z2h0OjEuNjU7bWFyZ2luLWJvdHRvbToxMnB4fQoudGlwewogIGRpc3BsYXk6ZmxleDtnYXA6OHB4O2Fs"
    "aWduLWl0ZW1zOmZsZXgtc3RhcnQ7CiAgYmFja2dyb3VuZDpyZ2JhKDQ2LDE2OCwyMjYsLjA3KTsKICBi"
    "b3JkZXI6MXB4IHNvbGlkIHJnYmEoNDYsMTY4LDIyNiwuMik7CiAgYm9yZGVyLXJhZGl1czoxMHB4O3Bh"
    "ZGRpbmc6MTBweCAxMnB4OwogIGZvbnQtc2l6ZToxMi41cHg7Y29sb3I6dmFyKC0tdGV4dCk7bGluZS1o"
    "ZWlnaHQ6MS41O21hcmdpbi10b3A6OHB4Owp9Ci50aXAtaWNvbntmb250LXNpemU6MTRweDtmbGV4LXNo"
    "cmluazowO21hcmdpbi10b3A6MXB4fQoud2FybnsKICBiYWNrZ3JvdW5kOnJnYmEoMjQ1LDE5Nyw2Niwu"
    "MDcpOwogIGJvcmRlci1jb2xvcjpyZ2JhKDI0NSwxOTcsNjYsLjIpOwp9Ci53YXJuIC50aXAtaWNvbntj"
    "b2xvcjp2YXIoLS1nb2xkKX0KCi8qIOKUgOKUgCBUSUVSIENBUkRTIOKUgOKUgCAqLwoudGllci1jYXJk"
    "ewogIGJvcmRlci1yYWRpdXM6MTZweDtwYWRkaW5nOjIycHg7CiAgYm9yZGVyOjFweCBzb2xpZCB2YXIo"
    "LS1ib3JkZXIpOwogIHBvc2l0aW9uOnJlbGF0aXZlO292ZXJmbG93OmhpZGRlbjsKICB0cmFuc2l0aW9u"
    "OnRyYW5zZm9ybSAuMnM7Cn0KLnRpZXItY2FyZDpob3Zlcnt0cmFuc2Zvcm06dHJhbnNsYXRlWSgtM3B4"
    "KX0KLnRpZXItY2FyZC5mcmVle2JhY2tncm91bmQ6bGluZWFyLWdyYWRpZW50KDEzNWRlZywjMGQxYTEy"
    "LCMwZTEzMjApfQoudGllci1jYXJkLnByZW17YmFja2dyb3VuZDpsaW5lYXItZ3JhZGllbnQoMTM1ZGVn"
    "LCMxYTE2MDgsIzBlMTMyMCl9Ci50aWVyLWNhcmQuZWxpdHtiYWNrZ3JvdW5kOmxpbmVhci1ncmFkaWVu"
    "dCgxMzVkZWcsIzE0MGQyNCwjMGUxMzIwKX0KLnRpZXItY2FyZCAuYmFkZ2V7CiAgZGlzcGxheTppbmxp"
    "bmUtYmxvY2s7cGFkZGluZzozcHggMTBweDtib3JkZXItcmFkaXVzOjk5cHg7CiAgZm9udC1zaXplOjEx"
    "cHg7Zm9udC13ZWlnaHQ6ODAwO21hcmdpbi1ib3R0b206MTJweDsKICBsZXR0ZXItc3BhY2luZzouM3B4"
    "Owp9Ci5mcmVlIC5iYWRnZXtiYWNrZ3JvdW5kOnJnYmEoNzQsMjIyLDEyOCwuMTUpO2NvbG9yOnZhcigt"
    "LWdyZWVuKTtib3JkZXI6MXB4IHNvbGlkIHJnYmEoNzQsMjIyLDEyOCwuMyl9Ci5wcmVtIC5iYWRnZXti"
    "YWNrZ3JvdW5kOnJnYmEoMjQ1LDE5Nyw2NiwuMTUpO2NvbG9yOnZhcigtLWdvbGQpO2JvcmRlcjoxcHgg"
    "c29saWQgcmdiYSgyNDUsMTk3LDY2LC4zKX0KLmVsaXQgLmJhZGdle2JhY2tncm91bmQ6cmdiYSgxNjcs"
    "MTM5LDI1MCwuMTUpO2NvbG9yOnZhcigtLXB1cnBsZSk7Ym9yZGVyOjFweCBzb2xpZCByZ2JhKDE2Nywx"
    "MzksMjUwLC4zKX0KLnRpZXItcHJpY2V7Zm9udC1zaXplOjI4cHg7Zm9udC13ZWlnaHQ6OTAwO21hcmdp"
    "bjo2cHggMCAxNHB4fQouZnJlZSAudGllci1wcmljZXtjb2xvcjp2YXIoLS1ncmVlbil9Ci5wcmVtIC50"
    "aWVyLXByaWNle2NvbG9yOnZhcigtLWdvbGQpfQouZWxpdCAudGllci1wcmljZXtjb2xvcjp2YXIoLS1w"
    "dXJwbGUpfQoudGllci1mZWF0e2ZvbnQtc2l6ZToxMi41cHg7Y29sb3I6dmFyKC0tbXV0ZWQpO2Rpc3Bs"
    "YXk6ZmxleDtmbGV4LWRpcmVjdGlvbjpjb2x1bW47Z2FwOjZweH0KLnRpZXItZmVhdCBsaXtkaXNwbGF5"
    "OmZsZXg7YWxpZ24taXRlbXM6Y2VudGVyO2dhcDo3cHg7bGlzdC1zdHlsZTpub25lfQoudGllci1mZWF0"
    "IGxpOjpiZWZvcmV7Y29udGVudDon4pyTJztjb2xvcjp2YXIoLS1ncmVlbik7Zm9udC13ZWlnaHQ6ODAw"
    "O2ZvbnQtc2l6ZToxMXB4O2ZsZXgtc2hyaW5rOjB9Ci50aWVyLWZlYXQgbGkubm86OmJlZm9yZXtjb250"
    "ZW50OifinJcnO2NvbG9yOnZhcigtLXJlZCl9Ci50aWVyLWZlYXQgbGkubm97Y29sb3I6IzQ0NH0KCi8q"
    "IOKUgOKUgCBESVZJREVSIOKUgOKUgCAqLwouZGl2aWRlcnsKICBib3JkZXI6bm9uZTtib3JkZXItdG9w"
    "OjFweCBzb2xpZCB2YXIoLS1ib3JkZXIpOwogIG1hcmdpbjo0MHB4IDA7Cn0KCi8qIOKUgOKUgCBJTkxJ"
    "TkUgQ09ERSDilIDilIAgKi8KY29kZXsKICBmb250LWZhbWlseTonSmV0QnJhaW5zIE1vbm8nLG1vbm9z"
    "cGFjZTsKICBmb250LXNpemU6MTJweDsKICBiYWNrZ3JvdW5kOnJnYmEoNDYsMTY4LDIyNiwuMSk7CiAg"
    "Ym9yZGVyOjFweCBzb2xpZCByZ2JhKDQ2LDE2OCwyMjYsLjIpOwogIHBhZGRpbmc6MXB4IDZweDtib3Jk"
    "ZXItcmFkaXVzOjVweDtjb2xvcjojN2RkM2ZjOwp9CgovKiDilIDilIAgQ09NTUFORCBQSUxMIOKUgOKU"
    "gCAqLwouY21kewogIGRpc3BsYXk6aW5saW5lLWZsZXg7YWxpZ24taXRlbXM6Y2VudGVyO2dhcDo1cHg7"
    "CiAgYmFja2dyb3VuZDojMTExODI3O2JvcmRlcjoxcHggc29saWQgdmFyKC0tYm9yZGVyKTsKICBib3Jk"
    "ZXItcmFkaXVzOjhweDtwYWRkaW5nOjZweCAxMnB4OwogIGZvbnQtZmFtaWx5OidKZXRCcmFpbnMgTW9u"
    "bycsbW9ub3NwYWNlOwogIGZvbnQtc2l6ZToxMi41cHg7Y29sb3I6dmFyKC0tYWNjZW50KTtmb250LXdl"
    "aWdodDo2MDA7CiAgbWFyZ2luOjNweDsKfQoKLyog4pSA4pSAIEZBUSDilIDilIAgKi8KLmZhcS1pdGVt"
    "ewogIGJvcmRlcjoxcHggc29saWQgdmFyKC0tYm9yZGVyKTtib3JkZXItcmFkaXVzOjEycHg7CiAgb3Zl"
    "cmZsb3c6aGlkZGVuO21hcmdpbi1ib3R0b206OHB4Owp9Ci5mYXEtcXsKICBwYWRkaW5nOjE0cHggMThw"
    "eDtmb250LXNpemU6MTRweDtmb250LXdlaWdodDo3MDA7CiAgY3Vyc29yOnBvaW50ZXI7ZGlzcGxheTpm"
    "bGV4O2p1c3RpZnktY29udGVudDpzcGFjZS1iZXR3ZWVuO2FsaWduLWl0ZW1zOmNlbnRlcjsKICB1c2Vy"
    "LXNlbGVjdDpub25lO3RyYW5zaXRpb246YmFja2dyb3VuZCAuMTVzOwp9Ci5mYXEtcTpob3ZlcntiYWNr"
    "Z3JvdW5kOnJnYmEoMjU1LDI1NSwyNTUsLjAzKX0KLmZhcS1hcnJvd3t0cmFuc2l0aW9uOnRyYW5zZm9y"
    "bSAuMjVzO2NvbG9yOnZhcigtLW11dGVkKTtmb250LXNpemU6MTNweH0KLmZhcS1pdGVtLm9wZW4gLmZh"
    "cS1hcnJvd3t0cmFuc2Zvcm06cm90YXRlKDE4MGRlZyl9Ci5mYXEtYXsKICBkaXNwbGF5Om5vbmU7cGFk"
    "ZGluZzowIDE4cHggMTRweDsKICBmb250LXNpemU6MTMuNXB4O2NvbG9yOnZhcigtLW11dGVkKTtsaW5l"
    "LWhlaWdodDoxLjY1Owp9Ci5mYXEtaXRlbS5vcGVuIC5mYXEtYXtkaXNwbGF5OmJsb2NrfQoKLyog4pSA"
    "4pSAIFNBRkVUWSBCQURHRSDilIDilIAgKi8KLnNhZmV0eS1ncmlke2Rpc3BsYXk6Z3JpZDtncmlkLXRl"
    "bXBsYXRlLWNvbHVtbnM6cmVwZWF0KGF1dG8tZml0LG1pbm1heCgyMDBweCwxZnIpKTtnYXA6MTJweH0K"
    "LnNhZmV0eS1pdGVtewogIGJhY2tncm91bmQ6dmFyKC0tY2FyZCk7Ym9yZGVyOjFweCBzb2xpZCB2YXIo"
    "LS1ib3JkZXIpOwogIGJvcmRlci1yYWRpdXM6MTJweDtwYWRkaW5nOjE2cHg7Cn0KLnNhZmV0eS1pY29u"
    "e2ZvbnQtc2l6ZToyMnB4O21hcmdpbi1ib3R0b206OHB4fQouc2FmZXR5LWl0ZW0gaDR7Zm9udC1zaXpl"
    "OjEzcHg7Zm9udC13ZWlnaHQ6NzAwO21hcmdpbi1ib3R0b206NHB4fQouc2FmZXR5LWl0ZW0gcHtmb250"
    "LXNpemU6MTJweDtjb2xvcjp2YXIoLS1tdXRlZCk7bGluZS1oZWlnaHQ6MS41NX0KCi8qIOKUgOKUgCBG"
    "T09URVIg4pSA4pSAICovCmZvb3RlcnsKICB0ZXh0LWFsaWduOmNlbnRlcjtwYWRkaW5nOjQwcHggMjBw"
    "eDsKICBib3JkZXItdG9wOjFweCBzb2xpZCB2YXIoLS1ib3JkZXIpOwogIGNvbG9yOnZhcigtLW11dGVk"
    "KTtmb250LXNpemU6MTNweDsKICBwb3NpdGlvbjpyZWxhdGl2ZTt6LWluZGV4OjE7Cn0KZm9vdGVyIGF7"
    "Y29sb3I6dmFyKC0tYWNjZW50KTt0ZXh0LWRlY29yYXRpb246bm9uZX0KCi8qIOKUgOKUgCBBTklNQVRJ"
    "T05TIOKUgOKUgCAqLwpAa2V5ZnJhbWVzIGZhZGVEb3due2Zyb217b3BhY2l0eTowO3RyYW5zZm9ybTp0"
    "cmFuc2xhdGVZKC0xNnB4KX10b3tvcGFjaXR5OjE7dHJhbnNmb3JtOm5vbmV9fQpAa2V5ZnJhbWVzIGZh"
    "ZGVVcCAge2Zyb217b3BhY2l0eTowO3RyYW5zZm9ybTp0cmFuc2xhdGVZKDE2cHgpIH10b3tvcGFjaXR5"
    "OjE7dHJhbnNmb3JtOm5vbmV9fQoucmV2ZWFse29wYWNpdHk6MDt0cmFuc2Zvcm06dHJhbnNsYXRlWSgy"
    "MHB4KTt0cmFuc2l0aW9uOm9wYWNpdHkgLjU1cyBlYXNlLHRyYW5zZm9ybSAuNTVzIGVhc2V9Ci5yZXZl"
    "YWwuaW57b3BhY2l0eToxO3RyYW5zZm9ybTpub25lfQoKLyog4pSA4pSAIFNDUk9MTEJBUiDilIDilIAg"
    "Ki8KOjotd2Via2l0LXNjcm9sbGJhcnt3aWR0aDo1cHh9Cjo6LXdlYmtpdC1zY3JvbGxiYXItdHJhY2t7"
    "YmFja2dyb3VuZDp0cmFuc3BhcmVudH0KOjotd2Via2l0LXNjcm9sbGJhci10aHVtYntiYWNrZ3JvdW5k"
    "OiMxZTJkNDI7Ym9yZGVyLXJhZGl1czozcHh9CgovKiDilIDilIAgUFJPR1JFU1MgQkFSIOKUgOKUgCAq"
    "LwojcHJvZ3Jlc3N7cG9zaXRpb246Zml4ZWQ7dG9wOjA7bGVmdDowO2hlaWdodDozcHg7YmFja2dyb3Vu"
    "ZDp2YXIoLS1hY2NlbnQpO3otaW5kZXg6OTk5O3RyYW5zaXRpb246d2lkdGggLjFzfQoKLyog4pSA4pSA"
    "IEhJR0hMSUdIVCDilIDilIAgKi8KLmhse2NvbG9yOnZhcigtLWFjY2VudCk7Zm9udC13ZWlnaHQ6NzAw"
    "fQouaGwtZ3tjb2xvcjp2YXIoLS1ncmVlbil9Ci5obC15e2NvbG9yOnZhcigtLWdvbGQpfQouaGwtcHtj"
    "b2xvcjp2YXIoLS1wdXJwbGUpfQoKQG1lZGlhKG1heC13aWR0aDo2MDBweCl7CiAgLmRlbW8tYmxvY2t7"
    "ZmxleC1kaXJlY3Rpb246Y29sdW1uO2FsaWduLWl0ZW1zOmNlbnRlcn0KICAucGhvbmV7d2lkdGg6MTAw"
    "JTttYXgtd2lkdGg6MjgwcHh9Cn0KPC9zdHlsZT4KPC9oZWFkPgo8Ym9keT4KCjxkaXYgaWQ9InByb2dy"
    "ZXNzIj48L2Rpdj4KCjwhLS0gTkFWIC0tPgo8bmF2IGlkPSJtYWluTmF2Ij4KICA8c3BhbiBjbGFzcz0i"
    "bmF2LWxvZ28iPvCfpJYgVmVyeCBBZHMgQm90PC9zcGFuPgogIDxhIGNsYXNzPSJuYXYtbGluayBhY3Rp"
    "dmUiIGhyZWY9IiNzdGFydCI+R2V0IFN0YXJ0ZWQ8L2E+CiAgPGEgY2xhc3M9Im5hdi1saW5rIiBocmVm"
    "PSIjZmVhdHVyZXMiPkZlYXR1cmVzPC9hPgogIDxhIGNsYXNzPSJuYXYtbGluayIgaHJlZj0iI3RpZXJz"
    "Ij5QbGFuczwvYT4KICA8YSBjbGFzcz0ibmF2LWxpbmsiIGhyZWY9IiNzYWZldHkiPlNhZmV0eTwvYT4K"
    "ICA8YSBjbGFzcz0ibmF2LWxpbmsiIGhyZWY9IiNmYXEiPkZBUTwvYT4KPC9uYXY+Cgo8IS0tIEhFUk8g"
    "LS0+CjxkaXYgY2xhc3M9Imhlcm8iPgogIDxkaXYgY2xhc3M9Imhlcm8tZ2xvdyI+PC9kaXY+CiAgPGRp"
    "diBjbGFzcz0iaGVyby1iYWRnZSI+8J+TliBDb21wbGV0ZSBUdXRvcmlhbDwvZGl2PgogIDxoMT5NYXN0"
    "ZXIgVmVyeCBBZHMgQm90PGJyPmluIDUgTWludXRlczwvaDE+CiAgPHA+RXZlcnl0aGluZyB5b3UgbmVl"
    "ZCB0byBhdXRvbWF0ZSB5b3VyIFRlbGVncmFtIGFkdmVydGlzaW5nIOKAlCBzZXR1cCwgZmVhdHVyZXMs"
    "IHRpZXJzLCBhbmQgc2FmZXR5IGV4cGxhaW5lZCBzaW1wbHkuPC9wPgogIDxkaXYgY2xhc3M9Imhlcm8t"
    "YWN0aW9ucyI+CiAgICA8YSBocmVmPSIjc3RhcnQiIGNsYXNzPSJidG4gYnRuLXByaW1hcnkiPvCfmoAg"
    "U3RhcnQgSGVyZTwvYT4KICAgIDxhIGhyZWY9IiN0aWVycyIgY2xhc3M9ImJ0biBidG4tb3V0bGluZSI+"
    "8J+SjiBWaWV3IFBsYW5zPC9hPgogIDwvZGl2Pgo8L2Rpdj4KCjwhLS0g4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ"
    "4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ"
    "4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ"
    "4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQIC0tPgo8IS0tIFNFQ1RJT04gMSDigJQg"
    "V0hBVCBJUyBJVCAtLT4KPCEtLSDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDi"
    "lZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDi"
    "lZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDi"
    "lZDilZDilZDilZDilZAgLS0+CjxkaXYgY2xhc3M9InNlY3Rpb24gcmV2ZWFsIiBpZD0ic3RhcnQiPgog"
    "IDxkaXYgY2xhc3M9InNlY3Rpb24taGVhZGVyIj4KICAgIDxkaXYgY2xhc3M9InNlY3Rpb24tbnVtIj4x"
    "PC9kaXY+CiAgICA8ZGl2PgogICAgICA8ZGl2IGNsYXNzPSJzZWN0aW9uLXRpdGxlIj5XaGF0IGlzIFZl"
    "cnggQWRzIEJvdD88L2Rpdj4KICAgICAgPGRpdiBjbGFzcz0ic2VjdGlvbi1zdWIiPlVuZGVyc3RhbmQg"
    "d2hhdCB0aGUgYm90IGRvZXMgaW4gMzAgc2Vjb25kczwvZGl2PgogICAgPC9kaXY+CiAgPC9kaXY+Cgog"
    "IDxkaXYgY2xhc3M9ImRlbW8tYmxvY2siPgogICAgPGRpdiBjbGFzcz0iZGVtby10ZXh0Ij4KICAgICAg"
    "PGgzPllvdXIgMjQvNyBUZWxlZ3JhbSBBZCBNYWNoaW5lPC9oMz4KICAgICAgPHA+VmVyeCBBZHMgQm90"
    "IHNlbmRzIHlvdXIgYWR2ZXJ0aXNlbWVudCBtZXNzYWdlcyB0byBtdWx0aXBsZSBUZWxlZ3JhbSBncm91"
    "cHMgPHN0cm9uZz5hdXRvbWF0aWNhbGx5PC9zdHJvbmc+LCBvbiBhIHRpbWVyIOKAlCBzbyB5b3UgZG9u"
    "J3QgaGF2ZSB0byBkbyBpdCBtYW51YWxseSBldmVyeSBob3VyLjwvcD4KICAgICAgPHA+WW91IGp1c3Qg"
    "c2V0IGl0IHVwIG9uY2U6IGFkZCB5b3VyIFRlbGVncmFtIGFjY291bnQsIHBpY2sgdGhlIGdyb3VwcyB5"
    "b3Ugd2FudCB0byBhZHZlcnRpc2UgaW4sIHdyaXRlIHlvdXIgbWVzc2FnZSwgY2hvb3NlIGhvdyBvZnRl"
    "biB0byBzZW5kIOKAlCB0aGVuIHByZXNzIFN0YXJ0LiBUaGUgYm90IGRvZXMgZXZlcnl0aGluZyBlbHNl"
    "LjwvcD4KICAgICAgPGRpdiBjbGFzcz0idGlwIj48c3BhbiBjbGFzcz0idGlwLWljb24iPvCfkqE8L3Nw"
    "YW4+IFRoaW5rIG9mIGl0IGxpa2UgYSBzY2hlZHVsZWQgcG9zdCB0b29sLCBidXQgZm9yIFRlbGVncmFt"
    "IGdyb3VwcyDigJQgaGFuZHMtZnJlZSwgcnVubmluZyBpbiB0aGUgYmFja2dyb3VuZCAyNC83LjwvZGl2"
    "PgogICAgPC9kaXY+CiAgICA8ZGl2IGNsYXNzPSJwaG9uZSI+CiAgICAgIDxkaXYgY2xhc3M9InBob25l"
    "LW5vdGNoIj48L2Rpdj4KICAgICAgPGRpdiBjbGFzcz0icGhvbmUtaGVhZGVyIj4KICAgICAgICA8ZGl2"
    "IGNsYXNzPSJwaG9uZS1hdmF0YXIiPvCfpJY8L2Rpdj4KICAgICAgICA8ZGl2PjxkaXYgY2xhc3M9InBo"
    "b25lLW5hbWUiPkBWZXJ4QWRzYm90PC9kaXY+PGRpdiBjbGFzcz0icGhvbmUtc3RhdHVzIj7il48gb25s"
    "aW5lPC9kaXY+PC9kaXY+CiAgICAgIDwvZGl2PgogICAgICA8ZGl2IGNsYXNzPSJwaG9uZS1ib2R5Ij4K"
    "ICAgICAgICA8ZGl2IGNsYXNzPSJtc2ctcm93IG91dCI+PGRpdiBjbGFzcz0iYnViYmxlIG91dCI+L3N0"
    "YXJ0PC9kaXY+PC9kaXY+CiAgICAgICAgPGRpdiBjbGFzcz0ibXNnLXJvdyBpbiI+PGRpdiBjbGFzcz0i"
    "YnViYmxlIGluIj4KICAgICAgICAgIPCfkYsgPGI+V2VsY29tZSB0byBWZXJ4IEFkcyBCb3QhPC9iPjxi"
    "cj48YnI+CiAgICAgICAgICDwn5OkIFNlbmRzIHlvdXIgYWRzIHRvIGdyb3VwcyBhdXRvbWF0aWNhbGx5"
    "PGJyPgogICAgICAgICAg4o+xIFJ1bnMgb24gYSB0aW1lciDigJQgeW91IHNldCBpdCBvbmNlPGJyPgog"
    "ICAgICAgICAg8J+UkiBTYWZlIOKAlCBodW1hbi1saWtlIGRlbGF5cyBidWlsdCBpbjxicj48YnI+CiAg"
    "ICAgICAgICA8ZGl2IGNsYXNzPSJrYiI+CiAgICAgICAgICAgIDxkaXYgY2xhc3M9ImtiLXJvdyI+PGRp"
    "diBjbGFzcz0ia2J0biI+8J+TiiBEYXNoYm9hcmQ8L2Rpdj48L2Rpdj4KICAgICAgICAgICAgPGRpdiBj"
    "bGFzcz0ia2Itcm93Ij48ZGl2IGNsYXNzPSJrYnRuIj7wn5KOIFZpZXcgUGxhbnM8L2Rpdj48ZGl2IGNs"
    "YXNzPSJrYnRuIj7inZMgSGVscDwvZGl2PjwvZGl2PgogICAgICAgICAgPC9kaXY+CiAgICAgICAgPC9k"
    "aXY+PC9kaXY+CiAgICAgIDwvZGl2PgogICAgPC9kaXY+CiAgPC9kaXY+CjwvZGl2PgoKPGhyIGNsYXNz"
    "PSJkaXZpZGVyIj4KCjwhLS0g4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ"
    "4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ"
    "4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ"
    "4pWQ4pWQ4pWQ4pWQIC0tPgo8IS0tIFNFQ1RJT04gMiDigJQgSE9XIFRPIFNFVCBVUCAtLT4KPCEtLSDi"
    "lZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDi"
    "lZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDi"
    "lZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZAgLS0+Cjxk"
    "aXYgY2xhc3M9InNlY3Rpb24gcmV2ZWFsIiBpZD0ic2V0dXAiPgogIDxkaXYgY2xhc3M9InNlY3Rpb24t"
    "aGVhZGVyIj4KICAgIDxkaXYgY2xhc3M9InNlY3Rpb24tbnVtIj4yPC9kaXY+CiAgICA8ZGl2PgogICAg"
    "ICA8ZGl2IGNsYXNzPSJzZWN0aW9uLXRpdGxlIj5Ib3cgdG8gU2V0IFVwIChTdGVwIGJ5IFN0ZXApPC9k"
    "aXY+CiAgICAgIDxkaXYgY2xhc3M9InNlY3Rpb24tc3ViIj5Gcm9tIHplcm8gdG8gcnVubmluZyBhZHMg"
    "aW4gdW5kZXIgMTAgbWludXRlczwvZGl2PgogICAgPC9kaXY+CiAgPC9kaXY+CgogIDxkaXYgc3R5bGU9"
    "ImRpc3BsYXk6ZmxleDtmbGV4LWRpcmVjdGlvbjpjb2x1bW47Z2FwOjEycHgiPgoKICAgIDxkaXYgY2xh"
    "c3M9InN0ZXAtY2FyZCI+CiAgICAgIDxkaXYgY2xhc3M9InN0ZXAtbnVtIj4xPC9kaXY+CiAgICAgIDxk"
    "aXYgY2xhc3M9InN0ZXAtYm9keSI+CiAgICAgICAgPGg0Pk9wZW4gdGhlIGJvdCBhbmQgam9pbiByZXF1"
    "aXJlZCBjaGFubmVsczwvaDQ+CiAgICAgICAgPHA+U2VhcmNoIDxzcGFuIGNsYXNzPSJjbWQiPkBWZXJ4"
    "QWRzYm90PC9zcGFuPiBvbiBUZWxlZ3JhbSBhbmQgcHJlc3MgU3RhcnQuIFRoZSBib3Qgd2lsbCBhc2sg"
    "eW91IHRvIGpvaW4gdHdvIGNoYW5uZWxzIGZpcnN0IOKAlCA8c3Ryb25nPkBHQU1FUlNYMDc8L3N0cm9u"
    "Zz4gYW5kIDxzdHJvbmc+QHZlcnhjaGF0PC9zdHJvbmc+LiBKb2luIGJvdGgsIHRoZW4gcHJlc3MgPHN0"
    "cm9uZz7wn5SEIFZlcmlmeTwvc3Ryb25nPi48L3A+CiAgICAgIDwvZGl2PgogICAgPC9kaXY+CgogICAg"
    "PGRpdiBjbGFzcz0ic3RlcC1jYXJkIj4KICAgICAgPGRpdiBjbGFzcz0ic3RlcC1udW0iPjI8L2Rpdj4K"
    "ICAgICAgPGRpdiBjbGFzcz0ic3RlcC1ib2R5Ij4KICAgICAgICA8aDQ+QWRkIHlvdXIgVGVsZWdyYW0g"
    "YWNjb3VudDwvaDQ+CiAgICAgICAgPHA+R28gdG8gPHN0cm9uZz7wn5GkIEFjY291bnRzIOKGkiDinpUg"
    "QWRkPC9zdHJvbmc+LiBTZW5kIHlvdXIgcGhvbmUgbnVtYmVyIHdpdGggY291bnRyeSBjb2RlIChlLmcu"
    "IDxjb2RlPis5MTk4NzY1NDMyMTA8L2NvZGU+KS4gWW91J2xsIHJlY2VpdmUgYW4gT1RQIG9uIFRlbGVn"
    "cmFtIOKAlCBzZW5kIGl0IGJhY2sgd2l0aCBzcGFjZXMgbGlrZSA8Y29kZT4xIDIgMyA0IDU8L2NvZGU+"
    "LiBJZiB5b3UgaGF2ZSAyRkEgZW5hYmxlZCwgZW50ZXIgeW91ciBwYXNzd29yZCBuZXh0LiBEb25lITwv"
    "cD4KICAgICAgICA8ZGl2IGNsYXNzPSJ0aXAiPjxzcGFuIGNsYXNzPSJ0aXAtaWNvbiI+8J+UjTwvc3Bh"
    "bj4gQWZ0ZXIgYWRkaW5nLCB0aGUgYm90IDxzdHJvbmc+YXV0b21hdGljYWxseSBzY2Fuczwvc3Ryb25n"
    "PiBhbGwgZ3JvdXBzIHlvdSdyZSBhbHJlYWR5IGluIGFuZCBhZGRzIHRoZSBiZXN0IG9uZXMgYXMgeW91"
    "ciB0YXJnZXQgZ3JvdXBzIOKAlCBzYXZpbmcgeW91IHRpbWUuPC9kaXY+CiAgICAgIDwvZGl2PgogICAg"
    "PC9kaXY+CgogICAgPGRpdiBjbGFzcz0ic3RlcC1jYXJkIj4KICAgICAgPGRpdiBjbGFzcz0ic3RlcC1u"
    "dW0iPjM8L2Rpdj4KICAgICAgPGRpdiBjbGFzcz0ic3RlcC1ib2R5Ij4KICAgICAgICA8aDQ+QWRkIHRh"
    "cmdldCBncm91cHM8L2g0PgogICAgICAgIDxwPkdvIHRvIDxzdHJvbmc+8J+RpSBHcm91cHMg4oaSIPCf"
    "lI0gQXV0by1TY2FuPC9zdHJvbmc+IHRvIGRldGVjdCBzdWl0YWJsZSBncm91cHMgYXV0b21hdGljYWxs"
    "eSwgb3IgdXNlIDxzdHJvbmc+4p6VIEFkZCBNYW51YWw8L3N0cm9uZz4gdG8gcGFzdGUgZ3JvdXAgbGlu"
    "a3MgeW91cnNlbGYuIFlvdSBjYW4gYWRkIGxpbmtzIGxpa2UgPGNvZGU+aHR0cHM6Ly90Lm1lL2dyb3Vw"
    "bmFtZTwvY29kZT4gb3IgPGNvZGU+QGdyb3VwbmFtZTwvY29kZT4g4oCUIG9uZSBwZXIgbGluZS4gRXZl"
    "biBmb2xkZXIgbGlua3Mgd29yay48L3A+CiAgICAgICAgPGRpdiBjbGFzcz0idGlwIHdhcm4iPjxzcGFu"
    "IGNsYXNzPSJ0aXAtaWNvbiI+4pqg77iPPC9zcGFuPiBGcmVlIHRpZXIgYWxsb3dzIHVwIHRvIDxzdHJv"
    "bmc+NSBncm91cHM8L3N0cm9uZz4uIFByZW1pdW06IDEwIGdyb3Vwcy4gRWxpdGU6IDMwIGdyb3Vwcy48"
    "L2Rpdj4KICAgICAgPC9kaXY+CiAgICA8L2Rpdj4KCiAgICA8ZGl2IGNsYXNzPSJzdGVwLWNhcmQiPgog"
    "ICAgICA8ZGl2IGNsYXNzPSJzdGVwLW51bSI+NDwvZGl2PgogICAgICA8ZGl2IGNsYXNzPSJzdGVwLWJv"
    "ZHkiPgogICAgICAgIDxoND5Xcml0ZSB5b3VyIGFkIG1lc3NhZ2U8L2g0PgogICAgICAgIDxwPkdvIHRv"
    "IDxzdHJvbmc+4pyJIE1lc3NhZ2VzIOKGkiDinpUgQWRkPC9zdHJvbmc+IGFuZCBzZW5kIHRoZSB0ZXh0"
    "IHlvdSB3YW50IHRvIGJyb2FkY2FzdC4gWW91IGNhbiBhZGQgbXVsdGlwbGUgbWVzc2FnZXMg4oCUIHRo"
    "ZSBib3Qgd2lsbCByb3RhdGUgYmV0d2VlbiB0aGVtIHJhbmRvbWx5IGVhY2ggY3ljbGUsIHNvIGl0IGRv"
    "ZXNuJ3QgbG9vayByZXBldGl0aXZlLjwvcD4KICAgICAgPC9kaXY+CiAgICA8L2Rpdj4KCiAgICA8ZGl2"
    "IGNsYXNzPSJzdGVwLWNhcmQiPgogICAgICA8ZGl2IGNsYXNzPSJzdGVwLW51bSI+NTwvZGl2PgogICAg"
    "ICA8ZGl2IGNsYXNzPSJzdGVwLWJvZHkiPgogICAgICAgIDxoND5TZXQgdGhlIGludGVydmFsIChob3cg"
    "b2Z0ZW4gdG8gc2VuZCk8L2g0PgogICAgICAgIDxwPkdvIHRvIDxzdHJvbmc+4o+xIEludGVydmFsPC9z"
    "dHJvbmc+IGZyb20gdGhlIGRhc2hib2FyZC4gRnJlZSB0aWVyIG1pbmltdW0gaXMgPHN0cm9uZz4xIGhv"
    "dXI8L3N0cm9uZz4uIFByZW1pdW0gbWluaW11bSBpcyA8c3Ryb25nPjUgbWludXRlczwvc3Ryb25nPi4g"
    "RWxpdGUgdXNlcnMgY2FuIHR5cGUgYW55IGN1c3RvbSB2YWx1ZSBpbiBzZWNvbmRzIChlLmcuIDxjb2Rl"
    "PjQ1MDwvY29kZT4gZm9yIDcuNSBtaW51dGVzKS48L3A+CiAgICAgIDwvZGl2PgogICAgPC9kaXY+Cgog"
    "ICAgPGRpdiBjbGFzcz0ic3RlcC1jYXJkIj4KICAgICAgPGRpdiBjbGFzcz0ic3RlcC1udW0iPjY8L2Rp"
    "dj4KICAgICAgPGRpdiBjbGFzcz0ic3RlcC1ib2R5Ij4KICAgICAgICA8aDQ+UHJlc3Mg4pa2IFN0YXJ0"
    "IEFkcyE8L2g0PgogICAgICAgIDxwPkdvIGJhY2sgdG8gdGhlIDxzdHJvbmc+8J+TiiBEYXNoYm9hcmQ8"
    "L3N0cm9uZz4gYW5kIHByZXNzIDxzdHJvbmc+4pa2IFN0YXJ0IEFkczwvc3Ryb25nPi4gVGhlIGJvdCBz"
    "dGFydHMgYnJvYWRjYXN0aW5nIGltbWVkaWF0ZWx5LiBZb3UnbGwgZ2V0IGEgbm90aWZpY2F0aW9uIGZv"
    "ciBlYWNoIGdyb3VwIG1lc3NhZ2Ugc2VudCwgb3IgYSBzdW1tYXJ5IGF0IHRoZSBlbmQgb2YgZWFjaCBj"
    "eWNsZSDigJQgeW91ciBjaG9pY2UuPC9wPgogICAgICA8L2Rpdj4KICAgIDwvZGl2PgoKICA8L2Rpdj4K"
    "PC9kaXY+Cgo8aHIgY2xhc3M9ImRpdmlkZXIiPgoKPCEtLSDilZDilZDilZDilZDilZDilZDilZDilZDi"
    "lZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDi"
    "lZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDi"
    "lZDilZDilZDilZDilZDilZDilZDilZDilZDilZAgLS0+CjwhLS0gU0VDVElPTiAzIOKAlCBGRUFUVVJF"
    "UyAtLT4KPCEtLSDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDi"
    "lZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDi"
    "lZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDi"
    "lZDilZAgLS0+CjxkaXYgY2xhc3M9InNlY3Rpb24gcmV2ZWFsIiBpZD0iZmVhdHVyZXMiPgogIDxkaXYg"
    "Y2xhc3M9InNlY3Rpb24taGVhZGVyIj4KICAgIDxkaXYgY2xhc3M9InNlY3Rpb24tbnVtIj4zPC9kaXY+"
    "CiAgICA8ZGl2PgogICAgICA8ZGl2IGNsYXNzPSJzZWN0aW9uLXRpdGxlIj5BbGwgRmVhdHVyZXMgRXhw"
    "bGFpbmVkPC9kaXY+CiAgICAgIDxkaXYgY2xhc3M9InNlY3Rpb24tc3ViIj5FdmVyeSBidXR0b24gYW5k"
    "IHdoYXQgaXQgZG9lczwvZGl2PgogICAgPC9kaXY+CiAgPC9kaXY+CgogIDwhLS0gQVVUTy1TQ0FOIC0t"
    "PgogIDxkaXYgc3R5bGU9Im1hcmdpbi1ib3R0b206MzJweCI+CiAgICA8ZGl2IGNsYXNzPSJkZW1vLWJs"
    "b2NrIj4KICAgICAgPGRpdiBjbGFzcz0iZGVtby10ZXh0Ij4KICAgICAgICA8aDM+8J+UjSBBdXRvLVNj"
    "YW4gR3JvdXBzPC9oMz4KICAgICAgICA8cD5XaGVuIHlvdSBhZGQgYW4gYWNjb3VudCwgdGhlIGJvdCBh"
    "dXRvbWF0aWNhbGx5IHNjYW5zIGFsbCB0aGUgVGVsZWdyYW0gZ3JvdXBzIHlvdSdyZSBhbHJlYWR5IGEg"
    "bWVtYmVyIG9mLiBJdCBmaWx0ZXJzIG91dCB1bnN1aXRhYmxlIG9uZXMg4oCUIGJyb2FkY2FzdCBjaGFu"
    "bmVscywgZ3JvdXBzIHdoZXJlIHlvdSdyZSBtdXRlZCwgdGlueSBncm91cHMgdW5kZXIgNTAgbWVtYmVy"
    "cyDigJQgYW5kIGFkZHMgb25seSB0aGUgYmVzdCBvbmVzLjwvcD4KICAgICAgICA8cD5Hcm91cHMgYXJl"
    "IHJhbmtlZCBieSA8c3Ryb25nPm1lbWJlciBjb3VudDwvc3Ryb25nPiAobGFyZ2VzdCBmaXJzdCksIHNv"
    "IHlvdXIgbGltaXRlZCBncm91cCBzbG90cyBnbyB0byB0aGUgaGlnaGVzdC1yZWFjaCBncm91cHMgYXV0"
    "b21hdGljYWxseS48L3A+CiAgICAgICAgPGRpdiBjbGFzcz0idGlwIj48c3BhbiBjbGFzcz0idGlwLWlj"
    "b24iPvCfkqE8L3NwYW4+IFlvdSBjYW4gYWxzbyB0cmlnZ2VyIGl0IG1hbnVhbGx5IGFueXRpbWU6IDxz"
    "dHJvbmc+8J+RpSBHcm91cHMg4oaSIPCflI0gQXV0by1TY2FuPC9zdHJvbmc+LiBJdCBjb21wbGV0ZXMg"
    "aW4gc2Vjb25kcy48L2Rpdj4KICAgICAgPC9kaXY+CiAgICAgIDxkaXYgY2xhc3M9InBob25lIj4KICAg"
    "ICAgICA8ZGl2IGNsYXNzPSJwaG9uZS1ub3RjaCI+PC9kaXY+CiAgICAgICAgPGRpdiBjbGFzcz0icGhv"
    "bmUtaGVhZGVyIj4KICAgICAgICAgIDxkaXYgY2xhc3M9InBob25lLWF2YXRhciI+8J+kljwvZGl2Pgog"
    "ICAgICAgICAgPGRpdj48ZGl2IGNsYXNzPSJwaG9uZS1uYW1lIj5AVmVyeEFkc2JvdDwvZGl2PjwvZGl2"
    "PgogICAgICAgIDwvZGl2PgogICAgICAgIDxkaXYgY2xhc3M9InBob25lLWJvZHkiPgogICAgICAgICAg"
    "PGRpdiBjbGFzcz0ibXNnLXJvdyBpbiI+PGRpdiBjbGFzcz0iYnViYmxlIGluIj4KICAgICAgICAgICAg"
    "PGI+8J+UjSBBdXRvLVNjYW4gQ29tcGxldGU8L2I+PGJyPjxicj4KICAgICAgICAgICAg8J+UjiBTY2Fu"
    "bmVkOiA8Yj4zNDwvYj4gZWxpZ2libGUgZ3JvdXBzPGJyPgogICAgICAgICAgICDinIUgQWRkZWQ6IDxi"
    "Pjg8L2I+IG5ldyB0YXJnZXQgZ3JvdXBzPGJyPgogICAgICAgICAgICDwn5qrIFVuc3VpdGFibGU6IDxi"
    "PjIxPC9iPiBza2lwcGVkPGJyPgogICAgICAgICAgICDwn5SBIEFscmVhZHkgYWRkZWQ6IDxiPjU8L2I+"
    "IHNraXBwZWQ8YnI+PGJyPgogICAgICAgICAgICBHcm91cHMgc29ydGVkIGJ5IG1lbWJlciBjb3VudC4K"
    "ICAgICAgICAgICAgPGRpdiBjbGFzcz0ia2IiPgogICAgICAgICAgICAgIDxkaXYgY2xhc3M9ImtiLXJv"
    "dyI+PGRpdiBjbGFzcz0ia2J0biI+8J+TiyBWaWV3IEdyb3VwczwvZGl2PjxkaXYgY2xhc3M9ImtidG4i"
    "PvCflIQgVG9nZ2xlPC9kaXY+PC9kaXY+CiAgICAgICAgICAgICAgPGRpdiBjbGFzcz0ia2Itcm93Ij48"
    "ZGl2IGNsYXNzPSJrYnRuIj7wn5SNIFNjYW4gQWdhaW48L2Rpdj48L2Rpdj4KICAgICAgICAgICAgPC9k"
    "aXY+CiAgICAgICAgICA8L2Rpdj48L2Rpdj4KICAgICAgICA8L2Rpdj4KICAgICAgPC9kaXY+CiAgICA8"
    "L2Rpdj4KICA8L2Rpdj4KCiAgPCEtLSBHUk9VUCBUT0dHTEUgLS0+CiAgPGRpdiBzdHlsZT0ibWFyZ2lu"
    "LWJvdHRvbTozMnB4Ij4KICAgIDxkaXYgY2xhc3M9ImRlbW8tYmxvY2siPgogICAgICA8ZGl2IGNsYXNz"
    "PSJwaG9uZSI+CiAgICAgICAgPGRpdiBjbGFzcz0icGhvbmUtbm90Y2giPjwvZGl2PgogICAgICAgIDxk"
    "aXYgY2xhc3M9InBob25lLWhlYWRlciI+CiAgICAgICAgICA8ZGl2IGNsYXNzPSJwaG9uZS1hdmF0YXIi"
    "PvCfpJY8L2Rpdj4KICAgICAgICAgIDxkaXY+PGRpdiBjbGFzcz0icGhvbmUtbmFtZSI+QFZlcnhBZHNi"
    "b3Q8L2Rpdj48L2Rpdj4KICAgICAgICA8L2Rpdj4KICAgICAgICA8ZGl2IGNsYXNzPSJwaG9uZS1ib2R5"
    "Ij4KICAgICAgICAgIDxkaXYgY2xhc3M9Im1zZy1yb3cgaW4iPjxkaXYgY2xhc3M9ImJ1YmJsZSBpbiI+"
    "CiAgICAgICAgICAgIDxiPvCflIQgVG9nZ2xlIEdyb3VwIFN0YXR1czwvYj48YnI+PGJyPgogICAgICAg"
    "ICAgICBUYXAgdG8gZW5hYmxlIC8gZGlzYWJsZTo8YnI+PGJyPgogICAgICAgICAgICA8ZGl2IGNsYXNz"
    "PSJrYiIgc3R5bGU9ImdhcDo0cHgiPgogICAgICAgICAgICAgIDxkaXYgY2xhc3M9ImtiLXJvdyI+PGRp"
    "diBjbGFzcz0ia2J0biBnIj7il48gQ3J5cHRvQWxlcnRzPC9kaXY+PC9kaXY+CiAgICAgICAgICAgICAg"
    "PGRpdiBjbGFzcz0ia2Itcm93Ij48ZGl2IGNsYXNzPSJrYnRuIGciPuKXjyBTdGFydHVwSW5kaWE8L2Rp"
    "dj48L2Rpdj4KICAgICAgICAgICAgICA8ZGl2IGNsYXNzPSJrYi1yb3ciPjxkaXYgY2xhc3M9ImtidG4g"
    "ciI+4peLIERlYWRHcm91cDk5PC9kaXY+PC9kaXY+CiAgICAgICAgICAgICAgPGRpdiBjbGFzcz0ia2It"
    "cm93Ij48ZGl2IGNsYXNzPSJrYnRuIGciPuKXjyBUZWNoSm9ic0h1YjwvZGl2PjwvZGl2PgogICAgICAg"
    "ICAgICAgIDxkaXYgY2xhc3M9ImtiLXJvdyI+PGRpdiBjbGFzcz0ia2J0biI+4p2MIEJhY2s8L2Rpdj48"
    "L2Rpdj4KICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICA8L2Rpdj48L2Rpdj4KICAgICAgICA8L2Rp"
    "dj4KICAgICAgPC9kaXY+CiAgICAgIDxkaXYgY2xhc3M9ImRlbW8tdGV4dCI+CiAgICAgICAgPGgzPvCf"
    "lIQgVG9nZ2xlIEdyb3VwczwvaDM+CiAgICAgICAgPHA+U2VlIGFsbCB5b3VyIGdyb3VwcyB3aXRoIGdy"
    "ZWVuICjwn5+iIGFjdGl2ZSkgb3IgcmVkICjwn5S0IGluYWN0aXZlKSBpbmRpY2F0b3JzLiBUYXAgYW55"
    "IGdyb3VwIHRvIHR1cm4gaXQgb24gb3Igb2ZmIHdpdGhvdXQgcmVtb3ZpbmcgaXQuIFVzZWZ1bCB3aGVu"
    "IHlvdSB3YW50IHRvIHBhdXNlIHNlbmRpbmcgdG8gb25lIGdyb3VwIHRlbXBvcmFyaWx5LjwvcD4KICAg"
    "ICAgICA8ZGl2IGNsYXNzPSJ0aXAiPjxzcGFuIGNsYXNzPSJ0aXAtaWNvbiI+8J+SoTwvc3Bhbj4gR3Jv"
    "dXBzIGFyZSBhdXRvbWF0aWNhbGx5IHR1cm5lZCBvZmYgaWYgeW91IGdldCBiYW5uZWQgb3IgbXV0ZWQg"
    "aW4gdGhlbSDigJQgdGhlIGJvdCBub3RpZmllcyB5b3UgaW5zdGFudGx5IGFuZCBrZWVwcyBzZW5kaW5n"
    "IHRvIGFsbCBvdGhlciBncm91cHMuPC9kaXY+CiAgICAgIDwvZGl2PgogICAgPC9kaXY+CiAgPC9kaXY+"
    "CgogIDwhLS0gSU5URVJWQUwgLS0+CiAgPGRpdiBzdHlsZT0ibWFyZ2luLWJvdHRvbTozMnB4Ij4KICAg"
    "IDxkaXYgY2xhc3M9ImRlbW8tYmxvY2siPgogICAgICA8ZGl2IGNsYXNzPSJkZW1vLXRleHQiPgogICAg"
    "ICAgIDxoMz7ij7EgQnJvYWRjYXN0IEludGVydmFsPC9oMz4KICAgICAgICA8cD5Db250cm9scyBob3cg"
    "b2Z0ZW4gdGhlIGJvdCBzZW5kcyB5b3VyIGFkcy4gQ2hvb3NlIGZyb20gcHJlc2V0IGJ1dHRvbnMgKDUg"
    "bWluLCAxMCBtaW4sIDMwIG1pbiwgMSBociwgMiBocikgb3Ig4oCUIGlmIHlvdSdyZSBvbiBFbGl0ZSDi"
    "gJQgdGFwIDxzdHJvbmc+4pyP77iPIFR5cGUgQ3VzdG9tPC9zdHJvbmc+IGFuZCBzZW5kIGFueSBudW1i"
    "ZXIgaW4gc2Vjb25kcy48L3A+CiAgICAgICAgPHA+Rm9yIGV4YW1wbGUsIHR5cGUgPGNvZGU+NDUwPC9j"
    "b2RlPiB0byBzZW5kIGV2ZXJ5IDcgbWludXRlcyAzMCBzZWNvbmRzLjwvcD4KICAgICAgICA8ZGl2IGNs"
    "YXNzPSJ0aXAgd2FybiI+PHNwYW4gY2xhc3M9InRpcC1pY29uIj7imqDvuI88L3NwYW4+IDxzdHJvbmc+"
    "RG9uJ3Qgc2V0IGludGVydmFscyB0b28gc2hvcnQuPC9zdHJvbmc+IEZyZWU6IG1pbiAxIGhvdXIuIFBy"
    "ZW1pdW06IG1pbiA1IG1pbi4gRWxpdGU6IG1pbiA1IG1pbiAoZm9yIGFjY291bnQgc2FmZXR5KS4gVGhl"
    "IGJvdCBlbmZvcmNlcyB0aGVzZSBmbG9vcnMgYXV0b21hdGljYWxseS48L2Rpdj4KICAgICAgPC9kaXY+"
    "CiAgICAgIDxkaXYgY2xhc3M9InBob25lIj4KICAgICAgICA8ZGl2IGNsYXNzPSJwaG9uZS1ub3RjaCI+"
    "PC9kaXY+CiAgICAgICAgPGRpdiBjbGFzcz0icGhvbmUtaGVhZGVyIj4KICAgICAgICAgIDxkaXYgY2xh"
    "c3M9InBob25lLWF2YXRhciI+8J+kljwvZGl2PgogICAgICAgICAgPGRpdj48ZGl2IGNsYXNzPSJwaG9u"
    "ZS1uYW1lIj5AVmVyeEFkc2JvdDwvZGl2PjwvZGl2PgogICAgICAgIDwvZGl2PgogICAgICAgIDxkaXYg"
    "Y2xhc3M9InBob25lLWJvZHkiPgogICAgICAgICAgPGRpdiBjbGFzcz0ibXNnLXJvdyBpbiI+PGRpdiBj"
    "bGFzcz0iYnViYmxlIGluIj4KICAgICAgICAgICAgPGI+4o+xIEJyb2FkY2FzdCBJbnRlcnZhbDwvYj48"
    "YnI+CiAgICAgICAgICAgIEN1cnJlbnQ6IDxjb2RlPjQ1MHM8L2NvZGU+ICg3bSAzMHMpPGJyPgogICAg"
    "ICAgICAgICBFbGl0ZTogdHlwZSBhbnkgdmFsdWUgaW4gc2Vjb25kcy48YnI+PGJyPgogICAgICAgICAg"
    "ICA8ZGl2IGNsYXNzPSJrYiI+CiAgICAgICAgICAgICAgPGRpdiBjbGFzcz0ia2Itcm93Ij48ZGl2IGNs"
    "YXNzPSJrYnRuIj41IG1pbjwvZGl2PjxkaXYgY2xhc3M9ImtidG4iPjEwIG1pbjwvZGl2PjxkaXYgY2xh"
    "c3M9ImtidG4iPjIwIG1pbjwvZGl2PjwvZGl2PgogICAgICAgICAgICAgIDxkaXYgY2xhc3M9ImtiLXJv"
    "dyI+PGRpdiBjbGFzcz0ia2J0biI+MzAgbWluPC9kaXY+PGRpdiBjbGFzcz0ia2J0biI+MSBocjwvZGl2"
    "PjxkaXYgY2xhc3M9ImtidG4iPjIgaHI8L2Rpdj48L2Rpdj4KICAgICAgICAgICAgICA8ZGl2IGNsYXNz"
    "PSJrYi1yb3ciPjxkaXYgY2xhc3M9ImtidG4gcCI+4pyP77iPIFR5cGUgQ3VzdG9tIChzZWNvbmRzKTwv"
    "ZGl2PjwvZGl2PgogICAgICAgICAgICAgIDxkaXYgY2xhc3M9ImtiLXJvdyI+PGRpdiBjbGFzcz0ia2J0"
    "biI+4p2MIEJhY2s8L2Rpdj48L2Rpdj4KICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICA8L2Rpdj48"
    "L2Rpdj4KICAgICAgICA8L2Rpdj4KICAgICAgPC9kaXY+CiAgICA8L2Rpdj4KICA8L2Rpdj4KCiAgPCEt"
    "LSBNRU1CRVIgVEFHR0lORyAtLT4KICA8ZGl2IHN0eWxlPSJtYXJnaW4tYm90dG9tOjMycHgiPgogICAg"
    "PGRpdiBjbGFzcz0iZGVtby1ibG9jayI+CiAgICAgIDxkaXYgY2xhc3M9InBob25lIj4KICAgICAgICA8"
    "ZGl2IGNsYXNzPSJwaG9uZS1ub3RjaCI+PC9kaXY+CiAgICAgICAgPGRpdiBjbGFzcz0icGhvbmUtaGVh"
    "ZGVyIj4KICAgICAgICAgIDxkaXYgY2xhc3M9InBob25lLWF2YXRhciI+8J+kljwvZGl2PgogICAgICAg"
    "ICAgPGRpdj48ZGl2IGNsYXNzPSJwaG9uZS1uYW1lIj5AVmVyeEFkc2JvdDwvZGl2PjwvZGl2PgogICAg"
    "ICAgIDwvZGl2PgogICAgICAgIDxkaXYgY2xhc3M9InBob25lLWJvZHkiPgogICAgICAgICAgPGRpdiBj"
    "bGFzcz0ibXNnLXJvdyBpbiI+PGRpdiBjbGFzcz0iYnViYmxlIGluIj4KICAgICAgICAgICAgPGI+8J+P"
    "tyBNZW1iZXIgVGFnZ2luZzwvYj48YnI+PGJyPgogICAgICAgICAgICBTdGF0dXM6IPCfn6IgPGI+RW5h"
    "YmxlZDwvYj4g4oCiIDxjb2RlPjU8L2NvZGU+IHRhZ3MvbXNnPGJyPjxicj4KICAgICAgICAgICAgVGFn"
    "cyByYW5kb20gZ3JvdXAgbWVtYmVycyBpbiBlYWNoIGJyb2FkY2FzdCBtZXNzYWdlIHRvIGluY3JlYXNl"
    "IHJlYWNoLjxicj48YnI+CiAgICAgICAgICAgIDxkaXYgY2xhc3M9ImtiIj4KICAgICAgICAgICAgICA8"
    "ZGl2IGNsYXNzPSJrYi1yb3ciPjxkaXYgY2xhc3M9ImtidG4gciI+8J+UtCBEaXNhYmxlPC9kaXY+PC9k"
    "aXY+CiAgICAgICAgICAgICAgPGRpdiBjbGFzcz0ia2Itcm93Ij48ZGl2IGNsYXNzPSJrYnRuIj7wn5Si"
    "IFRhZ3MgcGVyIG1lc3NhZ2UgKDUpPC9kaXY+PC9kaXY+CiAgICAgICAgICAgICAgPGRpdiBjbGFzcz0i"
    "a2Itcm93Ij48ZGl2IGNsYXNzPSJrYnRuIj7inYwgQmFjazwvZGl2PjwvZGl2PgogICAgICAgICAgICA8"
    "L2Rpdj4KICAgICAgICAgIDwvZGl2PjwvZGl2PgogICAgICAgIDwvZGl2PgogICAgICA8L2Rpdj4KICAg"
    "ICAgPGRpdiBjbGFzcz0iZGVtby10ZXh0Ij4KICAgICAgICA8aDM+8J+PtyBNZW1iZXIgVGFnZ2luZyA8"
    "c3BhbiBzdHlsZT0iZm9udC1zaXplOjEycHg7Y29sb3I6dmFyKC0tZ29sZCk7YmFja2dyb3VuZDpyZ2Jh"
    "KDI0NSwxOTcsNjYsLjEpO2JvcmRlcjoxcHggc29saWQgcmdiYSgyNDUsMTk3LDY2LC4yNSk7Ym9yZGVy"
    "LXJhZGl1czo2cHg7cGFkZGluZzoycHggN3B4O2ZvbnQtd2VpZ2h0OjcwMCI+UHJlbWl1bSs8L3NwYW4+"
    "PC9oMz4KICAgICAgICA8cD5XaGVuIGVuYWJsZWQsIHRoZSBib3QgaW52aXNpYmx5IHRhZ3MgcmVhbCBn"
    "cm91cCBtZW1iZXJzIGluIGVhY2ggbWVzc2FnZSB1c2luZyBoaWRkZW4gSFRNTCBsaW5rcy4gVGFnZ2Vk"
    "IHVzZXJzIGdldCBub3RpZmllZCwgZHJhbWF0aWNhbGx5IGluY3JlYXNpbmcgeW91ciBhZCdzIHJlYWNo"
    "IGJleW9uZCBqdXN0IHdobyBzZWVzIGl0IGluIHRoZSBmZWVkLjwvcD4KICAgICAgICA8cD5QcmVtaXVt"
    "IGFsbG93cyA8c3Ryb25nPjUgdGFncyBwZXIgbWVzc2FnZTwvc3Ryb25nPi4gRWxpdGUgYWxsb3dzIDxz"
    "dHJvbmc+MjAgdGFncyBwZXIgbWVzc2FnZTwvc3Ryb25nPi48L3A+CiAgICAgICAgPGRpdiBjbGFzcz0i"
    "dGlwIj48c3BhbiBjbGFzcz0idGlwLWljb24iPvCfkqE8L3NwYW4+IEdvIHRvIPCfk4ogRGFzaGJvYXJk"
    "IOKGkiDwn4+3IFRhZ2dpbmcgdG8gZW5hYmxlIGl0IGFuZCBjaG9vc2UgaG93IG1hbnkgbWVtYmVycyB0"
    "byB0YWcgcGVyIG1lc3NhZ2UuPC9kaXY+CiAgICAgIDwvZGl2PgogICAgPC9kaXY+CiAgPC9kaXY+Cgog"
    "IDwhLS0gQUkgQVVUTy1SRVBMWSAtLT4KICA8ZGl2IHN0eWxlPSJtYXJnaW4tYm90dG9tOjMycHgiPgog"
    "ICAgPGRpdiBjbGFzcz0iZGVtby1ibG9jayI+CiAgICAgIDxkaXYgY2xhc3M9ImRlbW8tdGV4dCI+CiAg"
    "ICAgICAgPGgzPvCfpJYgQUkgQXV0by1SZXBseSA8c3BhbiBzdHlsZT0iZm9udC1zaXplOjEycHg7Y29s"
    "b3I6dmFyKC0tcHVycGxlKTtiYWNrZ3JvdW5kOnJnYmEoMTY3LDEzOSwyNTAsLjEpO2JvcmRlcjoxcHgg"
    "c29saWQgcmdiYSgxNjcsMTM5LDI1MCwuMjUpO2JvcmRlci1yYWRpdXM6NnB4O3BhZGRpbmc6MnB4IDdw"
    "eDtmb250LXdlaWdodDo3MDAiPkVsaXRlIG9ubHk8L3NwYW4+PC9oMz4KICAgICAgICA8cD5XaGVuIHNv"
    "bWVvbmUgcmVwbGllcyB0byB5b3VyIGFkIG9yIG1lbnRpb25zIHlvdXIgYWNjb3VudCBpbiBhIHRhcmdl"
    "dCBncm91cCwgdGhlIGJvdCBhdXRvbWF0aWNhbGx5IHJlcGxpZXMgd2l0aCBhIG5hdHVyYWwsIGh1bWFu"
    "LXNvdW5kaW5nIHJlc3BvbnNlIHBvd2VyZWQgYnkgYW4gQUkgbW9kZWwuPC9wPgogICAgICAgIDxwPlJl"
    "cGxpZXMgYXJlIGRlbGF5ZWQgYnkgYSByYW5kb20gMjDigJM3NSBzZWNvbmRzIHRvIGxvb2sgbmF0dXJh"
    "bC4gVGhlIGJvdCBoYXMgYSBjYXAgb2YgNiByZXBsaWVzIHBlciBob3VyIHBlciBhY2NvdW50IHRvIGF2"
    "b2lkIHNwYW0gZGV0ZWN0aW9uLjwvcD4KICAgICAgICA8ZGl2IGNsYXNzPSJ0aXAiPjxzcGFuIGNsYXNz"
    "PSJ0aXAtaWNvbiI+8J+SoTwvc3Bhbj4gRW5hYmxlIGl0IGZyb20gRGFzaGJvYXJkIOKGkiDwn6SWIEF1"
    "dG8tUmVwbHkuIE5vIHNldHVwIG5lZWRlZCDigJQgaXQgd29ya3MgYXV0b21hdGljYWxseSBvbmNlIGVu"
    "YWJsZWQuPC9kaXY+CiAgICAgIDwvZGl2PgogICAgICA8ZGl2IGNsYXNzPSJwaG9uZSI+CiAgICAgICAg"
    "PGRpdiBjbGFzcz0icGhvbmUtbm90Y2giPjwvZGl2PgogICAgICAgIDxkaXYgY2xhc3M9InBob25lLWhl"
    "YWRlciI+CiAgICAgICAgICA8ZGl2IGNsYXNzPSJwaG9uZS1hdmF0YXIiPvCfpJY8L2Rpdj4KICAgICAg"
    "ICAgIDxkaXY+PGRpdiBjbGFzcz0icGhvbmUtbmFtZSI+QFZlcnhBZHNib3Q8L2Rpdj48L2Rpdj4KICAg"
    "ICAgICA8L2Rpdj4KICAgICAgICA8ZGl2IGNsYXNzPSJwaG9uZS1ib2R5Ij4KICAgICAgICAgIDxkaXYg"
    "Y2xhc3M9Im1zZy1yb3cgaW4iPjxkaXYgY2xhc3M9ImJ1YmJsZSBpbiI+CiAgICAgICAgICAgIDxiPvCf"
    "pJYgQUkgQXV0by1SZXBseTwvYj48YnI+CiAgICAgICAgICAgIFN0YXR1czog8J+foiA8Yj5FbmFibGVk"
    "PC9iPjxicj48YnI+CiAgICAgICAgICAgIFJlcGxpZXMgdG8gbWVudGlvbnMgYW5kIHJlcGxpZXMgaW4g"
    "dGFyZ2V0IGdyb3VwcyB1c2luZyBHUFQtcG93ZXJlZCBBSS48YnI+PGJyPgogICAgICAgICAgICA8ZGl2"
    "IGNsYXNzPSJrYiI+CiAgICAgICAgICAgICAgPGRpdiBjbGFzcz0ia2Itcm93Ij48ZGl2IGNsYXNzPSJr"
    "YnRuIHIiPvCflLQgRGlzYWJsZTwvZGl2PjwvZGl2PgogICAgICAgICAgICAgIDxkaXYgY2xhc3M9Imti"
    "LXJvdyI+PGRpdiBjbGFzcz0ia2J0biI+8J+TiiBSZXBseSBTdGF0czwvZGl2PjwvZGl2PgogICAgICAg"
    "ICAgICA8L2Rpdj4KICAgICAgICAgIDwvZGl2PjwvZGl2PgogICAgICAgIDwvZGl2PgogICAgICA8L2Rp"
    "dj4KICAgIDwvZGl2PgogIDwvZGl2PgoKICA8IS0tIFNFVCBCSU8gLS0+CiAgPGRpdiBzdHlsZT0ibWFy"
    "Z2luLWJvdHRvbTozMnB4Ij4KICAgIDxkaXYgY2xhc3M9ImRlbW8tYmxvY2siPgogICAgICA8ZGl2IGNs"
    "YXNzPSJwaG9uZSI+CiAgICAgICAgPGRpdiBjbGFzcz0icGhvbmUtbm90Y2giPjwvZGl2PgogICAgICAg"
    "IDxkaXYgY2xhc3M9InBob25lLWhlYWRlciI+CiAgICAgICAgICA8ZGl2IGNsYXNzPSJwaG9uZS1hdmF0"
    "YXIiPvCfpJY8L2Rpdj4KICAgICAgICAgIDxkaXY+PGRpdiBjbGFzcz0icGhvbmUtbmFtZSI+QFZlcnhB"
    "ZHNib3Q8L2Rpdj48L2Rpdj4KICAgICAgICA8L2Rpdj4KICAgICAgICA8ZGl2IGNsYXNzPSJwaG9uZS1i"
    "b2R5Ij4KICAgICAgICAgIDxkaXYgY2xhc3M9Im1zZy1yb3cgaW4iPjxkaXYgY2xhc3M9ImJ1YmJsZSBp"
    "biI+CiAgICAgICAgICAgIDxiPvCfk50gU2V0IEJpbzwvYj48YnI+PGJyPgogICAgICAgICAgICBDdXJy"
    "ZW50IGJpbzogPGk+bm90IHNldDwvaT48YnI+PGJyPgogICAgICAgICAgICBTZW5kIHlvdXIgbmV3IGJp"
    "byB0ZXh0IChtYXggNzAgY2hhcnMpLiBJdCB3aWxsIGJlIGFwcGxpZWQgdG8gPGI+YWxsPC9iPiB5b3Vy"
    "IGxpbmtlZCBhY2NvdW50cy4KICAgICAgICAgICAgPGRpdiBjbGFzcz0ia2IiPgogICAgICAgICAgICAg"
    "IDxkaXYgY2xhc3M9ImtiLXJvdyI+PGRpdiBjbGFzcz0ia2J0biByIj7inJcgQ2FuY2VsPC9kaXY+PC9k"
    "aXY+CiAgICAgICAgICAgIDwvZGl2PgogICAgICAgICAgPC9kaXY+PC9kaXY+CiAgICAgICAgICA8ZGl2"
    "IGNsYXNzPSJtc2ctcm93IG91dCI+PGRpdiBjbGFzcz0iYnViYmxlIG91dCI+QnV5IGFkcyBoZXJlIOKG"
    "kiBAWW91clVzZXJuYW1lPC9kaXY+PC9kaXY+CiAgICAgICAgICA8ZGl2IGNsYXNzPSJtc2ctcm93IGlu"
    "Ij48ZGl2IGNsYXNzPSJidWJibGUgaW4iPuKchSBCaW8gdXBkYXRlZCBvbiBhbGwgYWNjb3VudHMhPC9k"
    "aXY+PC9kaXY+CiAgICAgICAgPC9kaXY+CiAgICAgIDwvZGl2PgogICAgICA8ZGl2IGNsYXNzPSJkZW1v"
    "LXRleHQiPgogICAgICAgIDxoMz7wn5OdIFNldCBCaW8gPHNwYW4gc3R5bGU9ImZvbnQtc2l6ZToxMnB4"
    "O2NvbG9yOnZhcigtLWdvbGQpO2JhY2tncm91bmQ6cmdiYSgyNDUsMTk3LDY2LC4xKTtib3JkZXI6MXB4"
    "IHNvbGlkIHJnYmEoMjQ1LDE5Nyw2NiwuMjUpO2JvcmRlci1yYWRpdXM6NnB4O3BhZGRpbmc6MnB4IDdw"
    "eDtmb250LXdlaWdodDo3MDAiPlByZW1pdW0rPC9zcGFuPjwvaDM+CiAgICAgICAgPHA+U2V0cyB0aGUg"
    "c2FtZSBiaW8gdGV4dCBvbiBhbGwgeW91ciBsaW5rZWQgVGVsZWdyYW0gYWNjb3VudHMgYXQgb25jZS4g"
    "R3JlYXQgZm9yIHByb21vdGluZyB5b3VyIGNvbnRhY3QgdXNlcm5hbWUgb3IgYSBzZXJ2aWNlIGxpbmsg"
    "ZGlyZWN0bHkgaW4geW91ciBwcm9maWxlIGJpby48L3A+CiAgICAgICAgPGRpdiBjbGFzcz0idGlwIHdh"
    "cm4iPjxzcGFuIGNsYXNzPSJ0aXAtaWNvbiI+4pqg77iPPC9zcGFuPiBGcmVlIHRpZXIgYWNjb3VudHMg"
    "Z2V0IHRoZWlyIGJpbyBhdXRvLXNldCB0byB0aGUgb3duZXIncyBkZWZhdWx0IHByb21vdGlvbmFsIHRl"
    "eHQuIFVwZ3JhZGUgdG8gUHJlbWl1bSBvciBFbGl0ZSB0byB1c2UgYSBjdXN0b20gYmlvLjwvZGl2Pgog"
    "ICAgICA8L2Rpdj4KICAgIDwvZGl2PgogIDwvZGl2PgoKICA8IS0tIEFOQUxZVElDUyAtLT4KICA8ZGl2"
    "PgogICAgPGRpdiBjbGFzcz0iY2FyZCI+CiAgICAgIDxoMyBzdHlsZT0iZm9udC1zaXplOjE2cHg7Zm9u"
    "dC13ZWlnaHQ6ODAwO21hcmdpbi1ib3R0b206MTJweCI+8J+TiiBBbmFseXRpY3MgJiBMb2dzPC9oMz4K"
    "ICAgICAgPGRpdiBjbGFzcz0iZ3JpZC0yIiBzdHlsZT0iZ2FwOjEycHgiPgogICAgICAgIDxkaXY+CiAg"
    "ICAgICAgICA8cCBzdHlsZT0iZm9udC1zaXplOjEzcHg7Y29sb3I6dmFyKC0tbXV0ZWQpO21hcmdpbi1i"
    "b3R0b206OHB4Ij5UaGUgPHN0cm9uZz5BbmFseXRpY3M8L3N0cm9uZz4gc2NyZWVuIHNob3dzIHlvdSB0"
    "b3RhbCBtZXNzYWdlcyBzZW50LCBmYWlsZWQsIHRhZ3MgdXNlZCwgYW5kIGFjdGl2ZSBhY2NvdW50cy4g"
    "WW91IGFsc28gc2VlIGhvdyBtYW55IGJyb2FkY2FzdCBjeWNsZXMgaGF2ZSBjb21wbGV0ZWQuPC9wPgog"
    "ICAgICAgICAgPHAgc3R5bGU9ImZvbnQtc2l6ZToxM3B4O2NvbG9yOnZhcigtLW11dGVkKSI+VG9nZ2xl"
    "IDxzdHJvbmc+8J+UlCBNZXNzYWdlIExvZ2dpbmc8L3N0cm9uZz4gdG8gZ2V0IGEgbm90aWZpY2F0aW9u"
    "IGZvciBldmVyeSBzaW5nbGUgbWVzc2FnZSBzZW50IOKAlCBvciB0dXJuIGl0IG9mZiB0byBvbmx5IHJl"
    "Y2VpdmUgYSBzdW1tYXJ5IGF0IHRoZSBlbmQgb2YgZWFjaCBjeWNsZS48L3A+CiAgICAgICAgPC9kaXY+"
    "CiAgICAgICAgPGRpdj4KICAgICAgICAgIDxwIHN0eWxlPSJmb250LXNpemU6MTNweDtjb2xvcjp2YXIo"
    "LS1tdXRlZCk7bWFyZ2luLWJvdHRvbTo4cHgiPldoZW4gYSBncm91cCBiYW5zIG9yIG11dGVzIHlvdXIg"
    "YWNjb3VudCwgeW91IGluc3RhbnRseSByZWNlaXZlOjwvcD4KICAgICAgICAgIDxkaXYgc3R5bGU9ImRp"
    "c3BsYXk6ZmxleDtmbGV4LWRpcmVjdGlvbjpjb2x1bW47Z2FwOjZweCI+CiAgICAgICAgICAgIDxkaXYg"
    "c3R5bGU9ImJhY2tncm91bmQ6IzFhMGUwZTtib3JkZXI6MXB4IHNvbGlkICMzZDE1MTU7Ym9yZGVyLXJh"
    "ZGl1czo4cHg7cGFkZGluZzo4cHggMTBweDtmb250LXNpemU6MTJweCI+8J+aqyA8c3Ryb25nIHN0eWxl"
    "PSJjb2xvcjojZjg3MTcxIj5Hcm91cCBBdXRvLVJlbW92ZWQ8L3N0cm9uZz4g4oCUIGJhbm5lZC9tdXRl"
    "ZCBpbnN0YW50bHkgZGVhY3RpdmF0ZXMgdGhhdCBncm91cDwvZGl2PgogICAgICAgICAgICA8ZGl2IHN0"
    "eWxlPSJiYWNrZ3JvdW5kOiMxYTEwMDg7Ym9yZGVyOjFweCBzb2xpZCAjM2QyYTBhO2JvcmRlci1yYWRp"
    "dXM6OHB4O3BhZGRpbmc6OHB4IDEwcHg7Zm9udC1zaXplOjEycHgiPuKaoO+4jyA8c3Ryb25nIHN0eWxl"
    "PSJjb2xvcjp2YXIoLS1nb2xkKSI+R3JvdXAgQXV0by1EZWFjdGl2YXRlZDwvc3Ryb25nPiDigJQgNSBj"
    "b25zZWN1dGl2ZSBmYWlsdXJlcyB0cmlnZ2VycyBzb2Z0LWJhbiBwcm90ZWN0aW9uPC9kaXY+CiAgICAg"
    "ICAgICA8L2Rpdj4KICAgICAgICA8L2Rpdj4KICAgICAgPC9kaXY+CiAgICA8L2Rpdj4KICA8L2Rpdj4K"
    "CjwvZGl2PgoKPGhyIGNsYXNzPSJkaXZpZGVyIj4KCjwhLS0g4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ"
    "4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ"
    "4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ"
    "4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQIC0tPgo8IS0tIFNFQ1RJT04gNCDigJQgVElFUlMg"
    "LS0+CjwhLS0g4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ"
    "4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ"
    "4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ"
    "4pWQIC0tPgo8ZGl2IGNsYXNzPSJzZWN0aW9uIHJldmVhbCIgaWQ9InRpZXJzIj4KICA8ZGl2IGNsYXNz"
    "PSJzZWN0aW9uLWhlYWRlciI+CiAgICA8ZGl2IGNsYXNzPSJzZWN0aW9uLW51bSI+NDwvZGl2PgogICAg"
    "PGRpdj4KICAgICAgPGRpdiBjbGFzcz0ic2VjdGlvbi10aXRsZSI+UGxhbnMgJiBQcmljaW5nPC9kaXY+"
    "CiAgICAgIDxkaXYgY2xhc3M9InNlY3Rpb24tc3ViIj5DaG9vc2UgdGhlIHJpZ2h0IHRpZXIgZm9yIHlv"
    "dXIgbmVlZHM8L2Rpdj4KICAgIDwvZGl2PgogIDwvZGl2PgoKICA8ZGl2IGNsYXNzPSJncmlkLTMiPgog"
    "ICAgPGRpdiBjbGFzcz0idGllci1jYXJkIGZyZWUiPgogICAgICA8ZGl2IGNsYXNzPSJiYWRnZSI+4pqh"
    "IEZyZWU8L2Rpdj4KICAgICAgPGRpdiBjbGFzcz0idGllci1wcmljZSI+4oK5MDwvZGl2PgogICAgICA8"
    "dWwgY2xhc3M9InRpZXItZmVhdCI+CiAgICAgICAgPGxpPjEgVGVsZWdyYW0gYWNjb3VudDwvbGk+CiAg"
    "ICAgICAgPGxpPjUgdGFyZ2V0IGdyb3VwczwvbGk+CiAgICAgICAgPGxpPjEgYWQgbWVzc2FnZTwvbGk+"
    "CiAgICAgICAgPGxpPjEgaG91ciBtaW5pbXVtIGludGVydmFsPC9saT4KICAgICAgICA8bGkgY2xhc3M9"
    "Im5vIj5DdXN0b20gYmlvIChhdXRvLXNldCBieSBvd25lcik8L2xpPgogICAgICAgIDxsaSBjbGFzcz0i"
    "bm8iPk1lbWJlciB0YWdnaW5nPC9saT4KICAgICAgICA8bGkgY2xhc3M9Im5vIj5BSSBBdXRvLVJlcGx5"
    "PC9saT4KICAgICAgICA8bGkgY2xhc3M9Im5vIj5DdXN0b20gaW50ZXJ2YWw8L2xpPgogICAgICA8L3Vs"
    "PgogICAgPC9kaXY+CiAgICA8ZGl2IGNsYXNzPSJ0aWVyLWNhcmQgcHJlbSI+CiAgICAgIDxkaXYgY2xh"
    "c3M9ImJhZGdlIj7wn5GRIFByZW1pdW08L2Rpdj4KICAgICAgPGRpdiBjbGFzcz0idGllci1wcmljZSI+"
    "4oK5OTk8c3BhbiBzdHlsZT0iZm9udC1zaXplOjE0cHg7Zm9udC13ZWlnaHQ6NTAwO2NvbG9yOnZhcigt"
    "LW11dGVkKSI+L21vbnRoPC9zcGFuPjwvZGl2PgogICAgICA8dWwgY2xhc3M9InRpZXItZmVhdCI+CiAg"
    "ICAgICAgPGxpPjMgVGVsZWdyYW0gYWNjb3VudHM8L2xpPgogICAgICAgIDxsaT4xMCB0YXJnZXQgZ3Jv"
    "dXBzPC9saT4KICAgICAgICA8bGk+NSByb3RhdGluZyBtZXNzYWdlczwvbGk+CiAgICAgICAgPGxpPjUg"
    "bWludXRlIG1pbmltdW0gaW50ZXJ2YWw8L2xpPgogICAgICAgIDxsaT5DdXN0b20gYmlvIGZvciBhbGwg"
    "YWNjb3VudHM8L2xpPgogICAgICAgIDxsaT5NZW1iZXIgdGFnZ2luZyAoNS9tc2cpPC9saT4KICAgICAg"
    "ICA8bGkgY2xhc3M9Im5vIj5BSSBBdXRvLVJlcGx5PC9saT4KICAgICAgICA8bGkgY2xhc3M9Im5vIj5D"
    "dXN0b20gaW50ZXJ2YWwgdHlwaW5nPC9saT4KICAgICAgPC91bD4KICAgIDwvZGl2PgogICAgPGRpdiBj"
    "bGFzcz0idGllci1jYXJkIGVsaXQiPgogICAgICA8ZGl2IGNsYXNzPSJiYWRnZSI+8J+OlyBFbGl0ZTwv"
    "ZGl2PgogICAgICA8ZGl2IGNsYXNzPSJ0aWVyLXByaWNlIj7igrkyNDk8c3BhbiBzdHlsZT0iZm9udC1z"
    "aXplOjE0cHg7Zm9udC13ZWlnaHQ6NTAwO2NvbG9yOnZhcigtLW11dGVkKSI+L21vbnRoPC9zcGFuPjwv"
    "ZGl2PgogICAgICA8dWwgY2xhc3M9InRpZXItZmVhdCI+CiAgICAgICAgPGxpPjEwIFRlbGVncmFtIGFj"
    "Y291bnRzPC9saT4KICAgICAgICA8bGk+MzAgdGFyZ2V0IGdyb3VwczwvbGk+CiAgICAgICAgPGxpPjIw"
    "IHJvdGF0aW5nIG1lc3NhZ2VzPC9saT4KICAgICAgICA8bGk+NSBtaW51dGUgbWluaW11bSBpbnRlcnZh"
    "bDwvbGk+CiAgICAgICAgPGxpPkN1c3RvbSBiaW8gZm9yIGFsbCBhY2NvdW50czwvbGk+CiAgICAgICAg"
    "PGxpPk1lbWJlciB0YWdnaW5nICgyMC9tc2cpPC9saT4KICAgICAgICA8bGk+QUkgQXV0by1SZXBseSAo"
    "R1BUKTwvbGk+CiAgICAgICAgPGxpPlR5cGUgYW55IGN1c3RvbSBpbnRlcnZhbDwvbGk+CiAgICAgIDwv"
    "dWw+CiAgICA8L2Rpdj4KICA8L2Rpdj4KCiAgPGRpdiBjbGFzcz0idGlwIiBzdHlsZT0ibWFyZ2luLXRv"
    "cDoxOHB4Ij4KICAgIDxzcGFuIGNsYXNzPSJ0aXAtaWNvbiI+8J+TqTwvc3Bhbj4KICAgIFRvIHVwZ3Jh"
    "ZGUsIHRhcCA8c3Ryb25nPvCfko4gVmlldyBQbGFuczwvc3Ryb25nPiBpbiB0aGUgYm90IGFuZCBwcmVz"
    "cyA8c3Ryb25nPvCfk6kgQ29udGFjdCBPd25lcjwvc3Ryb25nPiB0byByZWFjaCB0aGUgYWRtaW4uIFRo"
    "ZXknbGwgYWN0aXZhdGUgeW91ciB0aWVyIGFmdGVyIHBheW1lbnQuCiAgPC9kaXY+CjwvZGl2PgoKPGhy"
    "IGNsYXNzPSJkaXZpZGVyIj4KCjwhLS0g4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ"
    "4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ"
    "4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ"
    "4pWQ4pWQ4pWQ4pWQ4pWQ4pWQIC0tPgo8IS0tIFNFQ1RJT04gNSDigJQgU0FGRVRZIC0tPgo8IS0tIOKV"
    "kOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKV"
    "kOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKV"
    "kOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkCAtLT4KPGRp"
    "diBjbGFzcz0ic2VjdGlvbiByZXZlYWwiIGlkPSJzYWZldHkiPgogIDxkaXYgY2xhc3M9InNlY3Rpb24t"
    "aGVhZGVyIj4KICAgIDxkaXYgY2xhc3M9InNlY3Rpb24tbnVtIj41PC9kaXY+CiAgICA8ZGl2PgogICAg"
    "ICA8ZGl2IGNsYXNzPSJzZWN0aW9uLXRpdGxlIj5BY2NvdW50IFNhZmV0eTwvZGl2PgogICAgICA8ZGl2"
    "IGNsYXNzPSJzZWN0aW9uLXN1YiI+SG93IHRoZSBib3QgcHJvdGVjdHMgeW91ciBUZWxlZ3JhbSBhY2Nv"
    "dW50cyBmcm9tIGJhbnM8L2Rpdj4KICAgIDwvZGl2PgogIDwvZGl2PgoKICA8ZGl2IGNsYXNzPSJzYWZl"
    "dHktZ3JpZCI+CiAgICA8ZGl2IGNsYXNzPSJzYWZldHktaXRlbSI+CiAgICAgIDxkaXYgY2xhc3M9InNh"
    "ZmV0eS1pY29uIj7ij7M8L2Rpdj4KICAgICAgPGg0PlJhbmRvbSBEZWxheXMgQmV0d2VlbiBHcm91cHM8"
    "L2g0PgogICAgICA8cD4yMOKAkzUwIHNlY29uZCByYW5kb20gcGF1c2UgYmV0d2VlbiBlYWNoIGdyb3Vw"
    "IHNlbmQg4oCUIG1pbWljcyBob3cgYSBodW1hbiB3b3VsZCBjb3B5LXBhc3RlIG1hbnVhbGx5LjwvcD4K"
    "ICAgIDwvZGl2PgogICAgPGRpdiBjbGFzcz0ic2FmZXR5LWl0ZW0iPgogICAgICA8ZGl2IGNsYXNzPSJz"
    "YWZldHktaWNvbiI+8J+MijwvZGl2PgogICAgICA8aDQ+Rmxvb2RXYWl0IFJlc3BlY3Q8L2g0PgogICAg"
    "ICA8cD5JZiBUZWxlZ3JhbSBzYXlzICJzbG93IGRvd24iLCB0aGUgYm90IHN0b3BzIGltbWVkaWF0ZWx5"
    "LCB3YWl0cyB0aGUgZXhhY3QgcmVxdWlyZWQgdGltZSBwbHVzIGV4dHJhIGJ1ZmZlciwgdGhlbiBjb250"
    "aW51ZXMuPC9wPgogICAgPC9kaXY+CiAgICA8ZGl2IGNsYXNzPSJzYWZldHktaXRlbSI+CiAgICAgIDxk"
    "aXYgY2xhc3M9InNhZmV0eS1pY29uIj7wn5OxPC9kaXY+CiAgICAgIDxoND5SZWFsIERldmljZSBGaW5n"
    "ZXJwcmludDwvaDQ+CiAgICAgIDxwPkxvb2tzIGxpa2UgU2Ftc3VuZyBHYWxheHkgUzIzIG9uIEFuZHJv"
    "aWQgMTQgdG8gVGVsZWdyYW0g4oCUIG5vdCBhIFB5dGhvbiBzY3JpcHQuIFRlbGVncmFtJ3Mgc3BhbSBk"
    "ZXRlY3Rpb24gbG9va3MgZm9yIGJvdCBzaWduYXR1cmVzLjwvcD4KICAgIDwvZGl2PgogICAgPGRpdiBj"
    "bGFzcz0ic2FmZXR5LWl0ZW0iPgogICAgICA8ZGl2IGNsYXNzPSJzYWZldHktaWNvbiI+8J+TijwvZGl2"
    "PgogICAgICA8aDQ+RGFpbHkgU2VuZCBDYXA8L2g0PgogICAgICA8cD5GcmVlOiAyNS9kYXkuIFByZW1p"
    "dW06IDgwL2RheS4gRWxpdGU6IDIwMC9kYXkuIFByZXZlbnRzIHNlbmRpbmcgc28gbXVjaCB0aGF0IFRl"
    "bGVncmFtIGZsYWdzIHRoZSBhY2NvdW50LjwvcD4KICAgIDwvZGl2PgogICAgPGRpdiBjbGFzcz0ic2Fm"
    "ZXR5LWl0ZW0iPgogICAgICA8ZGl2IGNsYXNzPSJzYWZldHktaWNvbiI+8J+aqzwvZGl2PgogICAgICA8"
    "aDQ+QXV0by1SZW1vdmUgQmFubmVkIEdyb3VwczwvaDQ+CiAgICAgIDxwPklmIGJhbm5lZCBvciBtdXRl"
    "ZCBpbiBhIGdyb3VwLCB0aGF0IGdyb3VwIGlzIGltbWVkaWF0ZWx5IGRpc2FibGVkLiBZb3VyIG90aGVy"
    "IGdyb3VwcyBrZWVwIHJ1bm5pbmcgdW5pbnRlcnJ1cHRlZC48L3A+CiAgICA8L2Rpdj4KICAgIDxkaXYg"
    "Y2xhc3M9InNhZmV0eS1pdGVtIj4KICAgICAgPGRpdiBjbGFzcz0ic2FmZXR5LWljb24iPvCflKw8L2Rp"
    "dj4KICAgICAgPGg0PlNvZnQtQmFuIERldGVjdGlvbjwvaDQ+CiAgICAgIDxwPjUgY29uc2VjdXRpdmUg"
    "ZmFpbHVyZXMgdG8gYSBncm91cCB0cmlnZ2VycyBhdXRvLWRlYWN0aXZhdGlvbiDigJQgY2F0Y2hlcyBz"
    "aWxlbnQgbXV0ZXMgYmVmb3JlIHRoZXkgYmVjb21lIGEgYmlnZ2VyIHByb2JsZW0uPC9wPgogICAgPC9k"
    "aXY+CiAgICA8ZGl2IGNsYXNzPSJzYWZldHktaXRlbSI+CiAgICAgIDxkaXYgY2xhc3M9InNhZmV0eS1p"
    "Y29uIj7wn5SRPC9kaXY+CiAgICAgIDxoND5FbmNyeXB0ZWQgU2Vzc2lvbnM8L2g0PgogICAgICA8cD5Z"
    "b3VyIFRlbGVncmFtIHNlc3Npb24gc3RyaW5ncyBhcmUgZW5jcnlwdGVkIGJlZm9yZSBiZWluZyBzdG9y"
    "ZWQuIE5vYm9keSBjYW4gc3RlYWwgeW91ciBhY2NvdW50IGZyb20gdGhlIGRhdGFiYXNlLjwvcD4KICAg"
    "IDwvZGl2PgogICAgPGRpdiBjbGFzcz0ic2FmZXR5LWl0ZW0iPgogICAgICA8ZGl2IGNsYXNzPSJzYWZl"
    "dHktaWNvbiI+8J+kljwvZGl2PgogICAgICA8aDQ+QXV0by1SZXBseSBSYXRlIExpbWl0aW5nPC9oND4K"
    "ICAgICAgPHA+QUkgcmVwbGllcyBhcmUgY2FwcGVkIGF0IDYgcGVyIGhvdXIgcGVyIGFjY291bnQgYW5k"
    "IGhhdmUgYSA0LW1pbnV0ZSBjb29sZG93biBwZXIgY2hhdCDigJQgcHJldmVudHMgc3BhbSBmbGFncy48"
    "L3A+CiAgICA8L2Rpdj4KICAgIDxkaXYgY2xhc3M9InNhZmV0eS1pdGVtIj4KICAgICAgPGRpdiBjbGFz"
    "cz0ic2FmZXR5LWljb24iPuKcj++4jzwvZGl2PgogICAgICA8aDQ+UHJvZmlsZSBVcGRhdGUgRGVsYXlz"
    "PC9oND4KICAgICAgPHA+QmlvL25hbWUgY2hhbmdlcyB1c2UgM+KAkzggbWludXRlIGRlbGF5cyBiZXR3"
    "ZWVuIGFjY291bnRzIHdpdGggYmF0Y2ggY29vbGRvd25zIOKAlCBidWxrIHByb2ZpbGUgZWRpdHMgYXJl"
    "IGEgbWFqb3IgYmFuIHRyaWdnZXIuPC9wPgogICAgPC9kaXY+CiAgPC9kaXY+CgogIDxkaXYgY2xhc3M9"
    "InRpcCB3YXJuIiBzdHlsZT0ibWFyZ2luLXRvcDoyMHB4Ij4KICAgIDxzcGFuIGNsYXNzPSJ0aXAtaWNv"
    "biI+4pqg77iPPC9zcGFuPgogICAgPGRpdj48c3Ryb25nPlVzZSBhY2NvdW50cyB0aGF0IGFyZSBhdCBs"
    "ZWFzdCAyIHdlZWtzIG9sZDwvc3Ryb25nPiB3aXRoIG5vcm1hbCBwcmlvciBhY3Rpdml0eSAocHJvZmls"
    "ZSBwaG90bywgYmlvLCBqb2luZWQgZ3JvdXBzIG1hbnVhbGx5KS4gRnJlc2ggb3Igc3VzcGljaW91cyBh"
    "Y2NvdW50cyBhcmUgYXQgaGlnaGVyIHJpc2sgcmVnYXJkbGVzcyBvZiBkZWxheXMuPC9kaXY+CiAgPC9k"
    "aXY+CjwvZGl2PgoKPGhyIGNsYXNzPSJkaXZpZGVyIj4KCjwhLS0g4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ"
    "4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ"
    "4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ"
    "4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQIC0tPgo8IS0tIFNFQ1RJT04gNiDigJQgQ09N"
    "TUFORFMgLS0+CjwhLS0g4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ"
    "4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ"
    "4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ"
    "4pWQ4pWQ4pWQIC0tPgo8ZGl2IGNsYXNzPSJzZWN0aW9uIHJldmVhbCI+CiAgPGRpdiBjbGFzcz0ic2Vj"
    "dGlvbi1oZWFkZXIiPgogICAgPGRpdiBjbGFzcz0ic2VjdGlvbi1udW0iPjY8L2Rpdj4KICAgIDxkaXY+"
    "CiAgICAgIDxkaXYgY2xhc3M9InNlY3Rpb24tdGl0bGUiPkJvdCBDb21tYW5kczwvZGl2PgogICAgICA8"
    "ZGl2IGNsYXNzPSJzZWN0aW9uLXN1YiI+VHlwZSB0aGVzZSBhbnl0aW1lIGluIHRoZSBjaGF0PC9kaXY+"
    "CiAgICA8L2Rpdj4KICA8L2Rpdj4KICA8ZGl2IGNsYXNzPSJncmlkLTIiPgogICAgPGRpdiBjbGFzcz0i"
    "Y2FyZCIgc3R5bGU9ImRpc3BsYXk6ZmxleDtmbGV4LWRpcmVjdGlvbjpjb2x1bW47Z2FwOjEwcHgiPgog"
    "ICAgICA8ZGl2IHN0eWxlPSJkaXNwbGF5OmZsZXg7YWxpZ24taXRlbXM6Y2VudGVyO2dhcDoxMHB4Ij4K"
    "ICAgICAgICA8c3BhbiBjbGFzcz0iY21kIj4vc3RhcnQ8L3NwYW4+CiAgICAgICAgPHNwYW4gc3R5bGU9"
    "ImZvbnQtc2l6ZToxM3B4O2NvbG9yOnZhcigtLW11dGVkKSI+T3BlbiB0aGUgYm90IC8gd2VsY29tZSBz"
    "Y3JlZW48L3NwYW4+CiAgICAgIDwvZGl2PgogICAgICA8ZGl2IHN0eWxlPSJkaXNwbGF5OmZsZXg7YWxp"
    "Z24taXRlbXM6Y2VudGVyO2dhcDoxMHB4Ij4KICAgICAgICA8c3BhbiBjbGFzcz0iY21kIj4vZGFzaGJv"
    "YXJkPC9zcGFuPgogICAgICAgIDxzcGFuIHN0eWxlPSJmb250LXNpemU6MTNweDtjb2xvcjp2YXIoLS1t"
    "dXRlZCkiPkdvIGRpcmVjdGx5IHRvIHlvdXIgZGFzaGJvYXJkPC9zcGFuPgogICAgICA8L2Rpdj4KICAg"
    "ICAgPGRpdiBzdHlsZT0iZGlzcGxheTpmbGV4O2FsaWduLWl0ZW1zOmNlbnRlcjtnYXA6MTBweCI+CiAg"
    "ICAgICAgPHNwYW4gY2xhc3M9ImNtZCI+L3N0YXR1czwvc3Bhbj4KICAgICAgICA8c3BhbiBzdHlsZT0i"
    "Zm9udC1zaXplOjEzcHg7Y29sb3I6dmFyKC0tbXV0ZWQpIj5DaGVjayBicm9hZGNhc3Qgc3RhdHVzIHF1"
    "aWNrbHk8L3NwYW4+CiAgICAgIDwvZGl2PgogICAgPC9kaXY+CiAgICA8ZGl2IGNsYXNzPSJjYXJkIiBz"
    "dHlsZT0iZGlzcGxheTpmbGV4O2ZsZXgtZGlyZWN0aW9uOmNvbHVtbjtnYXA6MTBweCI+CiAgICAgIDxk"
    "aXYgc3R5bGU9ImRpc3BsYXk6ZmxleDthbGlnbi1pdGVtczpjZW50ZXI7Z2FwOjEwcHgiPgogICAgICAg"
    "IDxzcGFuIGNsYXNzPSJjbWQiPi9teXN0YXRzPC9zcGFuPgogICAgICAgIDxzcGFuIHN0eWxlPSJmb250"
    "LXNpemU6MTNweDtjb2xvcjp2YXIoLS1tdXRlZCkiPlZpZXcgeW91ciB1c2FnZSBzdGF0aXN0aWNzPC9z"
    "cGFuPgogICAgICA8L2Rpdj4KICAgICAgPGRpdiBzdHlsZT0iZGlzcGxheTpmbGV4O2FsaWduLWl0ZW1z"
    "OmNlbnRlcjtnYXA6MTBweCI+CiAgICAgICAgPHNwYW4gY2xhc3M9ImNtZCI+L215cGxhbjwvc3Bhbj4K"
    "ICAgICAgICA8c3BhbiBzdHlsZT0iZm9udC1zaXplOjEzcHg7Y29sb3I6dmFyKC0tbXV0ZWQpIj5TZWUg"
    "eW91ciBjdXJyZW50IHN1YnNjcmlwdGlvbjwvc3Bhbj4KICAgICAgPC9kaXY+CiAgICAgIDxkaXYgc3R5"
    "bGU9ImRpc3BsYXk6ZmxleDthbGlnbi1pdGVtczpjZW50ZXI7Z2FwOjEwcHgiPgogICAgICAgIDxzcGFu"
    "IGNsYXNzPSJjbWQiPi9oZWxwPC9zcGFuPgogICAgICAgIDxzcGFuIHN0eWxlPSJmb250LXNpemU6MTNw"
    "eDtjb2xvcjp2YXIoLS1tdXRlZCkiPkZ1bGwgZmVhdHVyZSBndWlkZSBpbnNpZGUgdGhlIGJvdDwvc3Bh"
    "bj4KICAgICAgPC9kaXY+CiAgICA8L2Rpdj4KICA8L2Rpdj4KPC9kaXY+Cgo8aHIgY2xhc3M9ImRpdmlk"
    "ZXIiPgoKPCEtLSDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDi"
    "lZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDi"
    "lZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDi"
    "lZDilZAgLS0+CjwhLS0gU0VDVElPTiA3IOKAlCBGQVEgLS0+CjwhLS0g4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ"
    "4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ"
    "4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ"
    "4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQIC0tPgo8ZGl2IGNsYXNzPSJzZWN0aW9u"
    "IHJldmVhbCIgaWQ9ImZhcSI+CiAgPGRpdiBjbGFzcz0ic2VjdGlvbi1oZWFkZXIiPgogICAgPGRpdiBj"
    "bGFzcz0ic2VjdGlvbi1udW0iPjc8L2Rpdj4KICAgIDxkaXY+CiAgICAgIDxkaXYgY2xhc3M9InNlY3Rp"
    "b24tdGl0bGUiPkZyZXF1ZW50bHkgQXNrZWQgUXVlc3Rpb25zPC9kaXY+CiAgICAgIDxkaXYgY2xhc3M9"
    "InNlY3Rpb24tc3ViIj5Db21tb24gcXVlc3Rpb25zIGFuc3dlcmVkIHNpbXBseTwvZGl2PgogICAgPC9k"
    "aXY+CiAgPC9kaXY+CgogIDxkaXYgaWQ9ImZhcUxpc3QiPgoKICAgIDxkaXYgY2xhc3M9ImZhcS1pdGVt"
    "Ij4KICAgICAgPGRpdiBjbGFzcz0iZmFxLXEiIG9uY2xpY2s9InRvZ2dsZUZhcSh0aGlzKSI+CiAgICAg"
    "ICAgV2lsbCBteSBUZWxlZ3JhbSBhY2NvdW50IGdldCBiYW5uZWQ/IDxzcGFuIGNsYXNzPSJmYXEtYXJy"
    "b3ciPuKWvDwvc3Bhbj4KICAgICAgPC9kaXY+CiAgICAgIDxkaXYgY2xhc3M9ImZhcS1hIj4KICAgICAg"
    "ICBUaGUgYm90IGhhcyBtYW55IHNhZmV0eSBmZWF0dXJlcyBidWlsdCBpbiDigJQgcmFuZG9tIGRlbGF5"
    "cywgRmxvb2RXYWl0IGhhbmRsaW5nLCBkYWlseSBjYXBzLCBkZXZpY2UgZmluZ2VycHJpbnRpbmcsIGFu"
    "ZCByYXRlIGxpbWl0aW5nLiA8c3Ryb25nPkhvd2V2ZXIsIG5vIHRvb2wgaXMgMTAwJSByaXNrLWZyZWUu"
    "PC9zdHJvbmc+IFRoZSBzYWZlc3QgYWNjb3VudHMgdG8gdXNlIGFyZSBvbmVzIHRoYXQgYXJlIGF0IGxl"
    "YXN0IDIgd2Vla3Mgb2xkLCBoYXZlIGEgcHJvZmlsZSBwaG90bywgYmlvLCBhbmQgd2VyZSB1c2VkIG5v"
    "cm1hbGx5IGJlZm9yZS4gQXZvaWQgZnJlc2ggbnVtYmVycyBvciBhY2NvdW50cyB3aXRoIHByaW9yIHNw"
    "YW0gaGlzdG9yeS4KICAgICAgPC9kaXY+CiAgICA8L2Rpdj4KCiAgICA8ZGl2IGNsYXNzPSJmYXEtaXRl"
    "bSI+CiAgICAgIDxkaXYgY2xhc3M9ImZhcS1xIiBvbmNsaWNrPSJ0b2dnbGVGYXEodGhpcykiPgogICAg"
    "ICAgIENhbiBJIHVzZSBtdWx0aXBsZSBhY2NvdW50cyBhdCB0aGUgc2FtZSB0aW1lPyA8c3BhbiBjbGFz"
    "cz0iZmFxLWFycm93Ij7ilrw8L3NwYW4+CiAgICAgIDwvZGl2PgogICAgICA8ZGl2IGNsYXNzPSJmYXEt"
    "YSI+CiAgICAgICAgWWVzLiBQcmVtaXVtIGFsbG93cyAzIGFjY291bnRzLCBFbGl0ZSBhbGxvd3MgMTAu"
    "IEFsbCBhY2NvdW50cyBicm9hZGNhc3QgaW5kZXBlbmRlbnRseSBhbmQgc2ltdWx0YW5lb3VzbHksIG11"
    "bHRpcGx5aW5nIHlvdXIgcmVhY2guIEVhY2ggYWNjb3VudCBoYXMgaXRzIG93biBicm9hZGNhc3QsIGl0"
    "cyBvd24gdGFyZ2V0IGdyb3VwcywgYW5kIGl0cyBvd24gc2FmZXR5IGNvb2xkb3ducy4KICAgICAgPC9k"
    "aXY+CiAgICA8L2Rpdj4KCiAgICA8ZGl2IGNsYXNzPSJmYXEtaXRlbSI+CiAgICAgIDxkaXYgY2xhc3M9"
    "ImZhcS1xIiBvbmNsaWNrPSJ0b2dnbGVGYXEodGhpcykiPgogICAgICAgIFdoYXQgaGFwcGVucyBpZiBJ"
    "IGdldCBiYW5uZWQgaW4gYSBncm91cD8gPHNwYW4gY2xhc3M9ImZhcS1hcnJvdyI+4pa8PC9zcGFuPgog"
    "ICAgICA8L2Rpdj4KICAgICAgPGRpdiBjbGFzcz0iZmFxLWEiPgogICAgICAgIFRoZSBib3QgZGV0ZWN0"
    "cyBpdCBpbW1lZGlhdGVseSBhbmQgYXV0b21hdGljYWxseSBkaXNhYmxlcyB0aGF0IGdyb3VwLiBZb3Ug"
    "cmVjZWl2ZSBhbiBpbnN0YW50IG5vdGlmaWNhdGlvbjogIvCfmqsgR3JvdXAgQXV0by1SZW1vdmVkIi4g"
    "QWxsIHlvdXIgb3RoZXIgZ3JvdXBzIGNvbnRpbnVlIGJyb2FkY2FzdGluZyBub3JtYWxseSB3aXRob3V0"
    "IGFueSBpbnRlcnJ1cHRpb24uIFlvdSBjYW4gc2VlIGFuZCByZS1tYW5hZ2UgeW91ciBncm91cHMgYW55"
    "dGltZSBmcm9tIPCfkaUgR3JvdXBzIOKGkiDwn5OLIExpc3QuCiAgICAgIDwvZGl2PgogICAgPC9kaXY+"
    "CgogICAgPGRpdiBjbGFzcz0iZmFxLWl0ZW0iPgogICAgICA8ZGl2IGNsYXNzPSJmYXEtcSIgb25jbGlj"
    "az0idG9nZ2xlRmFxKHRoaXMpIj4KICAgICAgICBEb2VzIEF1dG8tU2NhbiBhZGQgZ3JvdXBzIHdpdGhv"
    "dXQgbXkgcGVybWlzc2lvbj8gPHNwYW4gY2xhc3M9ImZhcS1hcnJvdyI+4pa8PC9zcGFuPgogICAgICA8"
    "L2Rpdj4KICAgICAgPGRpdiBjbGFzcz0iZmFxLWEiPgogICAgICAgIEF1dG8tc2NhbiBhZGRzIGdyb3Vw"
    "cyBhdXRvbWF0aWNhbGx5IGFmdGVyIHlvdSBhZGQgYW4gYWNjb3VudCwgYnV0IGl0IG9ubHkgYWRkcyBn"
    "cm91cHMgeW91J3JlIDxzdHJvbmc+YWxyZWFkeSBhIG1lbWJlciBvZjwvc3Ryb25nPi4gSXQgbmV2ZXIg"
    "am9pbnMgbmV3IGdyb3Vwcy4gWW91IGNhbiByZXZpZXcgZXZlcnl0aGluZyB2aWEg8J+RpSBHcm91cHMg"
    "4oaSIPCflIQgVG9nZ2xlIGFuZCBkZWFjdGl2YXRlIGFueSBncm91cCB5b3UgZG9uJ3Qgd2FudC4gWW91"
    "J3JlIGFsd2F5cyBpbiBjb250cm9sLgogICAgICA8L2Rpdj4KICAgIDwvZGl2PgoKICAgIDxkaXYgY2xh"
    "c3M9ImZhcS1pdGVtIj4KICAgICAgPGRpdiBjbGFzcz0iZmFxLXEiIG9uY2xpY2s9InRvZ2dsZUZhcSh0"
    "aGlzKSI+CiAgICAgICAgQ2FuIEkgdXNlIHRoZSBib3Qgb24gYSBwaG9uZSBJJ20gY3VycmVudGx5IHVz"
    "aW5nPyA8c3BhbiBjbGFzcz0iZmFxLWFycm93Ij7ilrw8L3NwYW4+CiAgICAgIDwvZGl2PgogICAgICA8"
    "ZGl2IGNsYXNzPSJmYXEtYSI+CiAgICAgICAgWWVzLCBidXQgYmUgYXdhcmUgdGhhdCBUZWxlZ3JhbSBv"
    "bmx5IGFsbG93cyBvbmUgYWN0aXZlIHNlc3Npb24gcGVyIGFjY291bnQgb24gdGhlIHNhbWUgImRldmlj"
    "ZSIuIFRoZSBib3QgdXNlcyBhIHNlcGFyYXRlIHNlc3Npb24gc3RyaW5nIHN0b3JlZCBzZWN1cmVseS4g"
    "SWYgeW91IGxvZyBvdXQgYWxsIG90aGVyIHNlc3Npb25zIG9uIHlvdXIgcGhvbmUsIHRoZSBib3QncyBz"
    "ZXNzaW9uIGNvbnRpbnVlcyB3b3JraW5nIGluZGVwZW5kZW50bHkuCiAgICAgIDwvZGl2PgogICAgPC9k"
    "aXY+CgogICAgPGRpdiBjbGFzcz0iZmFxLWl0ZW0iPgogICAgICA8ZGl2IGNsYXNzPSJmYXEtcSIgb25j"
    "bGljaz0idG9nZ2xlRmFxKHRoaXMpIj4KICAgICAgICBIb3cgZG9lcyBBSSBBdXRvLVJlcGx5IHdvcms/"
    "IDxzcGFuIGNsYXNzPSJmYXEtYXJyb3ciPuKWvDwvc3Bhbj4KICAgICAgPC9kaXY+CiAgICAgIDxkaXYg"
    "Y2xhc3M9ImZhcS1hIj4KICAgICAgICBXaGVuIHNvbWVvbmUgcmVwbGllcyB0byB5b3VyIGFkIG9yIHRh"
    "Z3MgeW91ciBhY2NvdW50IGluIG9uZSBvZiB5b3VyIHRhcmdldCBncm91cHMsIHRoZSBBSSBnZW5lcmF0"
    "ZXMgYSBjYXN1YWwsIGZyaWVuZGx5IHJlc3BvbnNlICgx4oCTMiBzZW50ZW5jZXMpIGFuZCBzZW5kcyBp"
    "dCBhZnRlciBhIDIw4oCTNzUgc2Vjb25kIGRlbGF5IHRvIGxvb2sgbmF0dXJhbC4gSXQgcmVtZW1iZXJz"
    "IHVwIHRvIDUgcHJldmlvdXMgbWVzc2FnZXMgZm9yIGNvbnRleHQuIEl0J3MgY2FwcGVkIGF0IDYgcmVw"
    "bGllcyBwZXIgaG91ciBwZXIgYWNjb3VudCBzbyBpdCBkb2Vzbid0IHRyaWdnZXIgc3BhbSBkZXRlY3Rp"
    "b24uCiAgICAgIDwvZGl2PgogICAgPC9kaXY+CgogICAgPGRpdiBjbGFzcz0iZmFxLWl0ZW0iPgogICAg"
    "ICA8ZGl2IGNsYXNzPSJmYXEtcSIgb25jbGljaz0idG9nZ2xlRmFxKHRoaXMpIj4KICAgICAgICBNeSBP"
    "VFAgaXMgbm90IHdvcmtpbmcg4oCUIHdoYXQgZG8gSSBkbz8gPHNwYW4gY2xhc3M9ImZhcS1hcnJvdyI+"
    "4pa8PC9zcGFuPgogICAgICA8L2Rpdj4KICAgICAgPGRpdiBjbGFzcz0iZmFxLWEiPgogICAgICAgIE1h"
    "a2Ugc3VyZSB5b3UgdHlwZSB0aGUgY29kZSB3aXRoIHNwYWNlcyBiZXR3ZWVuIGVhY2ggZGlnaXQsIGxp"
    "a2UgPGNvZGU+MSAyIDMgNCA1PC9jb2RlPi4gSWYgdGhlIGNvZGUgZXhwaXJlcywgdGFwIDxzdHJvbmc+"
    "8J+UhCBSZXNlbmQgT1RQPC9zdHJvbmc+IGluIHRoZSBib3QgdG8gcmVxdWVzdCBhIG5ldyBvbmUuIElm"
    "IHlvdSBoYXZlIDJGQSAoVHdvLUZhY3RvciBBdXRoZW50aWNhdGlvbikgZW5hYmxlZCBvbiB5b3VyIGFj"
    "Y291bnQsIHlvdSdsbCBiZSBhc2tlZCBmb3IgeW91ciBwYXNzd29yZCBhZnRlciB0aGUgT1RQIOKAlCBq"
    "dXN0IHNlbmQgaXQgYXMgdGV4dC4KICAgICAgPC9kaXY+CiAgICA8L2Rpdj4KCiAgICA8ZGl2IGNsYXNz"
    "PSJmYXEtaXRlbSI+CiAgICAgIDxkaXYgY2xhc3M9ImZhcS1xIiBvbmNsaWNrPSJ0b2dnbGVGYXEodGhp"
    "cykiPgogICAgICAgIElzIG15IFRlbGVncmFtIHBhc3N3b3JkL3Nlc3Npb24gc3RvcmVkIHNhZmVseT8g"
    "PHNwYW4gY2xhc3M9ImZhcS1hcnJvdyI+4pa8PC9zcGFuPgogICAgICA8L2Rpdj4KICAgICAgPGRpdiBj"
    "bGFzcz0iZmFxLWEiPgogICAgICAgIFlvdXIgc2Vzc2lvbiBzdHJpbmcgKG5vdCB5b3VyIHBhc3N3b3Jk"
    "IOKAlCB0aGF0J3MgbmV2ZXIgc3RvcmVkKSBpcyBlbmNyeXB0ZWQgdXNpbmcgRmVybmV0IGVuY3J5cHRp"
    "b24gYmVmb3JlIGJlaW5nIHdyaXR0ZW4gdG8gdGhlIGRhdGFiYXNlLiBZb3VyIDJGQSBwYXNzd29yZCBp"
    "cyBvbmx5IHVzZWQgbW9tZW50YXJpbHkgZHVyaW5nIGxvZ2luIGFuZCBpcyBuZXZlciBzYXZlZCBhbnl3"
    "aGVyZS4KICAgICAgPC9kaXY+CiAgICA8L2Rpdj4KCiAgPC9kaXY+CjwvZGl2PgoKPGhyIGNsYXNzPSJk"
    "aXZpZGVyIj4KCjwhLS0gRk9PVEVSIC0tPgo8Zm9vdGVyPgogIDxwIHN0eWxlPSJmb250LXNpemU6MjJw"
    "eDttYXJnaW4tYm90dG9tOjhweCI+8J+kljwvcD4KICA8cCBzdHlsZT0iZm9udC1zaXplOjE1cHg7Zm9u"
    "dC13ZWlnaHQ6NzAwO2NvbG9yOnZhcigtLXRleHQpO21hcmdpbi1ib3R0b206NHB4Ij5WZXJ4IEFkcyBC"
    "b3Q8L3A+CiAgPHA+U3VwcG9ydDogPGEgaHJlZj0iaHR0cHM6Ly90Lm1lL3ZlcnhjaGF0Ij50Lm1lL3Zl"
    "cnhjaGF0PC9hPiAmbmJzcDvigKImbmJzcDsgVXBkYXRlczogPGEgaHJlZj0iaHR0cHM6Ly90Lm1lL0dB"
    "TUVSU1gwNyI+dC5tZS9HQU1FUlNYMDc8L2E+ICZuYnNwO+KAoiZuYnNwOyBDb250YWN0OiA8YSBocmVm"
    "PSJodHRwczovL3QubWUvT3duaW5nMDciPkBPd25pbmcwNzwvYT48L3A+CiAgPHAgc3R5bGU9Im1hcmdp"
    "bi10b3A6MTJweDtmb250LXNpemU6MTJweDtjb2xvcjojMmQzZDUwIj5Vc2UgcmVzcG9uc2libHkuIEZv"
    "bGxvdyBUZWxlZ3JhbSdzIFRlcm1zIG9mIFNlcnZpY2UuPC9wPgo8L2Zvb3Rlcj4KCjxzY3JpcHQ+Ci8v"
    "IOKUgOKUgCBQUk9HUkVTUyBCQVIg4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA"
    "4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA"
    "4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA"
    "4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSA4pSACndpbmRvdy5hZGRFdmVudExpc3RlbmVyKCdzY3JvbGwn"
    "LCAoKSA9PiB7CiAgY29uc3QgZWwgPSBkb2N1bWVudC5kb2N1bWVudEVsZW1lbnQ7CiAgY29uc3QgcGN0"
    "ID0gKGVsLnNjcm9sbFRvcCAvIChlbC5zY3JvbGxIZWlnaHQgLSBlbC5jbGllbnRIZWlnaHQpKSAqIDEw"
    "MDsKICBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgncHJvZ3Jlc3MnKS5zdHlsZS53aWR0aCA9IHBjdCAr"
    "ICclJzsKfSk7CgovLyDilIDilIAgU0NST0xMIFJFVkVBTCDilIDilIDilIDilIDilIDilIDilIDilIDi"
    "lIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDi"
    "lIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDi"
    "lIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIDilIAKY29uc3Qgb2JzZXJ2ZXIgPSBuZXcg"
    "SW50ZXJzZWN0aW9uT2JzZXJ2ZXIoZW50cmllcyA9PiB7CiAgZW50cmllcy5mb3JFYWNoKGUgPT4geyBp"
    "ZiAoZS5pc0ludGVyc2VjdGluZykgZS50YXJnZXQuY2xhc3NMaXN0LmFkZCgnaW4nKTsgfSk7Cn0sIHsg"
    "dGhyZXNob2xkOiAwLjA4IH0pOwpkb2N1bWVudC5xdWVyeVNlbGVjdG9yQWxsKCcucmV2ZWFsJykuZm9y"
    "RWFjaChlbCA9PiBvYnNlcnZlci5vYnNlcnZlKGVsKSk7CgovLyDilIDilIAgQUNUSVZFIE5BViBMSU5L"
    "IOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKU"
    "gOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKU"
    "gOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgApj"
    "b25zdCBzZWN0aW9ucyA9IFsnc3RhcnQnLCdzZXR1cCcsJ2ZlYXR1cmVzJywndGllcnMnLCdzYWZldHkn"
    "LCdmYXEnXTsKY29uc3QgbmF2TGlua3MgID0gZG9jdW1lbnQucXVlcnlTZWxlY3RvckFsbCgnLm5hdi1s"
    "aW5rJyk7CndpbmRvdy5hZGRFdmVudExpc3RlbmVyKCdzY3JvbGwnLCAoKSA9PiB7CiAgbGV0IGN1ciA9"
    "ICcnOwogIHNlY3Rpb25zLmZvckVhY2goaWQgPT4gewogICAgY29uc3QgZWwgPSBkb2N1bWVudC5nZXRF"
    "bGVtZW50QnlJZChpZCk7CiAgICBpZiAoZWwgJiYgd2luZG93LnNjcm9sbFkgPj0gZWwub2Zmc2V0VG9w"
    "IC0gMTIwKSBjdXIgPSBpZDsKICB9KTsKICBuYXZMaW5rcy5mb3JFYWNoKGEgPT4gewogICAgYS5jbGFz"
    "c0xpc3QudG9nZ2xlKCdhY3RpdmUnLCBhLmdldEF0dHJpYnV0ZSgnaHJlZicpID09PSAnIycgKyBjdXIp"
    "OwogIH0pOwp9KTsKCi8vIOKUgOKUgCBGQVEgQUNDT1JESU9OIOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKU"
    "gOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKU"
    "gOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKU"
    "gOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgOKUgApmdW5jdGlvbiB0b2dnbGVGYXEo"
    "ZWwpIHsKICBjb25zdCBpdGVtID0gZWwuY2xvc2VzdCgnLmZhcS1pdGVtJyk7CiAgY29uc3Qgd2FzT3Bl"
    "biA9IGl0ZW0uY2xhc3NMaXN0LmNvbnRhaW5zKCdvcGVuJyk7CiAgZG9jdW1lbnQucXVlcnlTZWxlY3Rv"
    "ckFsbCgnLmZhcS1pdGVtJykuZm9yRWFjaChpID0+IGkuY2xhc3NMaXN0LnJlbW92ZSgnb3BlbicpKTsK"
    "ICBpZiAoIXdhc09wZW4pIGl0ZW0uY2xhc3NMaXN0LmFkZCgnb3BlbicpOwp9Cjwvc2NyaXB0Pgo8L2Jv"
    "ZHk+CjwvaHRtbD4K"
)
def _get_tutorial_bytes() -> bytes:
    return _b64.b64decode("".join(_TUTORIAL_B64))

# ==================== HELPERS ====================

def format_duration(total_seconds: int) -> str:
    """Format seconds into Xd Xh Xm."""
    total_seconds = max(0, int(total_seconds))
    d = total_seconds // 86400
    h = (total_seconds % 86400) // 3600
    m = (total_seconds % 3600) // 60
    if d:
        return f"{d}d {h}h {m}m"
    if h:
        return f"{h}h {m}m"
    return f"{m}m"

def time_remaining(iso_str: str) -> str:
    """Return dd hh mm remaining from an ISO date string."""
    try:
        delta = datetime.fromisoformat(iso_str) - datetime.now()
        return format_duration(int(delta.total_seconds()))
    except Exception:
        return "—"

# ==================== TIER HELPER ====================

class Tier:
    FREE = "free"
    PREMIUM = "premium"
    ELITE = "elite"

    OWNER = "owner"

    @staticmethod
    def get_tier(user_id: int, premium_until: Optional[str]) -> str:
        if user_id in OWNER_IDS:
            return Tier.OWNER
        if not premium_until:
            return Tier.FREE
        try:
            if premium_until.startswith("elite:"):
                until = datetime.fromisoformat(premium_until[6:])
                if until > datetime.now():
                    return Tier.ELITE
            else:
                until = datetime.fromisoformat(premium_until)
                if until > datetime.now():
                    return Tier.PREMIUM
        except:
            pass
        return Tier.FREE

    @staticmethod
    def get_limits(tier: str):
        if tier == Tier.FREE:
            return {
                "max_accounts": FREE_MAX_ACCOUNTS,
                "max_groups": FREE_MAX_GROUPS,
                "max_messages": FREE_MAX_MESSAGES,
                "max_tags": FREE_MAX_TAGS,
                "auto_reply": FREE_AUTO_REPLY,
                "set_bio": FREE_SET_BIO,
                "interval_custom": FREE_INTERVAL_CUSTOM,
                "interval_min": FREE_INTERVAL_MIN,
                "tagging_locked": FREE_TAGGING_LOCKED,
            }
        elif tier == Tier.PREMIUM:
            return {
                "max_accounts": PREMIUM_MAX_ACCOUNTS,
                "max_groups": PREMIUM_MAX_GROUPS,
                "max_messages": PREMIUM_MAX_MESSAGES,
                "max_tags": PREMIUM_MAX_TAGS,
                "auto_reply": PREMIUM_AUTO_REPLY,
                "set_bio": PREMIUM_SET_BIO,
                "interval_custom": PREMIUM_INTERVAL_CUSTOM,
                "interval_min": PREMIUM_INTERVAL_MIN,
                "tagging_locked": PREMIUM_TAGGING_LOCKED,
            }
        elif tier == "owner":
            return {
                "max_accounts": 9999, "max_groups": 9999, "max_messages": 9999,
                "max_tags": 9999, "auto_reply": True, "set_bio": True,
                "interval_custom": True, "interval_min": 300,  # Owner: 5 min floor — no exceptions
                "tagging_locked": False,
            }
        else:  # ELITE
            return {
                "max_accounts": ELITE_MAX_ACCOUNTS,
                "max_groups": ELITE_MAX_GROUPS,
                "max_messages": ELITE_MAX_MESSAGES,
                "max_tags": ELITE_MAX_TAGS,
                "auto_reply": ELITE_AUTO_REPLY,
                "set_bio": ELITE_SET_BIO,
                "interval_custom": ELITE_INTERVAL_CUSTOM,
                "interval_min": 300,  # 5 min safe floor for Elite — overrides any old constant
                "tagging_locked": ELITE_TAGGING_LOCKED,
            }

# ==================== DATABASE MANAGER (with connection pooling) ====================

class DatabaseManager:
    def __init__(self):
        self.db_path = DB_PATH
        self._conn = None
        self._init_db()
        self._ensure_columns()
        self._ensure_settings()

    @property
    def conn(self):
        """Return a persistent database connection."""
        if self._conn is None:
            self._conn = sqlite3.connect(self.db_path, check_same_thread=False)
            self._conn.row_factory = sqlite3.Row
        return self._conn

    def close(self):
        if self._conn:
            self._conn.close()
            self._conn = None

    def _init_db(self):
        """Create tables if they don't exist."""
        with self.conn as conn:
            c = conn.cursor()

            c.execute('''CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT, first_name TEXT, last_name TEXT,
                joined_date TIMESTAMP, settings TEXT DEFAULT '{}',
                joined_channels INTEGER DEFAULT 0,
                premium_until TIMESTAMP
            )''')

            c.execute(f'''CREATE TABLE IF NOT EXISTS accounts (
                account_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER, phone_number TEXT, session_string TEXT,
                api_id INTEGER DEFAULT {API_ID}, api_hash TEXT DEFAULT '{API_HASH}',
                is_active INTEGER DEFAULT 1, status TEXT DEFAULT 'idle',
                added_date TIMESTAMP, last_used TIMESTAMP,
                daily_messages INTEGER DEFAULT 0, total_messages INTEGER DEFAULT 0,
                failed_messages INTEGER DEFAULT 0,
                auto_reply_enabled INTEGER DEFAULT 0,
                tagging_enabled INTEGER DEFAULT 0,
                tags_per_message INTEGER DEFAULT {DEFAULT_TAGS_PER_MESSAGE},
                tag_interval INTEGER DEFAULT 30,
                FOREIGN KEY(user_id) REFERENCES users(user_id)
            )''')

            c.execute('''CREATE TABLE IF NOT EXISTS target_groups (
                group_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER, group_username TEXT, group_title TEXT,
                group_link TEXT, added_date TIMESTAMP, is_active INTEGER DEFAULT 1,
                joined INTEGER DEFAULT 0, last_used TIMESTAMP,
                chat_id INTEGER,
                FOREIGN KEY(user_id) REFERENCES users(user_id)
            )''')

            c.execute('''CREATE TABLE IF NOT EXISTS user_messages (
                msg_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER, message_text TEXT, added_date TIMESTAMP,
                is_active INTEGER DEFAULT 1,
                FOREIGN KEY(user_id) REFERENCES users(user_id)
            )''')

            c.execute('''CREATE TABLE IF NOT EXISTS broadcasts (
                broadcast_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER, account_id INTEGER, message_text TEXT,
                interval_seconds INTEGER, is_running INTEGER DEFAULT 0,
                start_time TIMESTAMP, last_run TIMESTAMP,
                messages_sent INTEGER DEFAULT 0, messages_failed INTEGER DEFAULT 0,
                use_tagging INTEGER DEFAULT 0,
                FOREIGN KEY(user_id) REFERENCES users(user_id),
                FOREIGN KEY(account_id) REFERENCES accounts(account_id)
            )''')

            c.execute('''CREATE TABLE IF NOT EXISTS message_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                account_id INTEGER, group_id INTEGER, message_text TEXT,
                sent_time TIMESTAMP, status TEXT, error TEXT, tags_used INTEGER DEFAULT 0,
                FOREIGN KEY(account_id) REFERENCES accounts(account_id),
                FOREIGN KEY(group_id) REFERENCES target_groups(group_id)
            )''')

            c.execute('''CREATE TABLE IF NOT EXISTS tagged_members (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                account_id INTEGER, group_id INTEGER, user_id INTEGER,
                username TEXT, tagged_date TIMESTAMP,
                FOREIGN KEY(account_id) REFERENCES accounts(account_id),
                FOREIGN KEY(group_id) REFERENCES target_groups(group_id)
            )''')

            c.execute('''CREATE TABLE IF NOT EXISTS reply_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                account_id INTEGER, chat_id INTEGER, incoming_message TEXT,
                reply_message TEXT, reply_time TIMESTAMP, tokens_used INTEGER,
                FOREIGN KEY(account_id) REFERENCES accounts(account_id)
            )''')

            c.execute('''CREATE TABLE IF NOT EXISTS settings (
                key TEXT PRIMARY KEY,
                value TEXT
            )''')

            conn.commit()
        logger.info("Database initialized")

    def _ensure_columns(self):
        """Add missing columns to existing tables (for migrations)."""
        with self.conn as conn:
            c = conn.cursor()
            # Add scan_source to target_groups — tracks whether a group was added manually or by auto-scan
            c.execute("PRAGMA table_info(target_groups)")
            tg_cols = [col[1] for col in c.fetchall()]
            if 'scan_source' not in tg_cols:
                c.execute("ALTER TABLE target_groups ADD COLUMN scan_source TEXT DEFAULT 'manual'")
                logger.info("Added scan_source column to target_groups.")
            if 'consecutive_fails' not in tg_cols:
                c.execute("ALTER TABLE target_groups ADD COLUMN consecutive_fails INTEGER DEFAULT 0")
                logger.info("Added consecutive_fails column to target_groups.")
            conn.commit()
            # Add bio column to users (formerly watermark)
            c.execute("PRAGMA table_info(users)")
            columns = [col[1] for col in c.fetchall()]
            if 'bio' not in columns and 'watermark' in columns:
                # rename watermark to bio? Actually we'll keep watermark for compatibility but add bio as alias.
                # For simplicity, we'll just ensure 'bio' column exists.
                c.execute("ALTER TABLE users ADD COLUMN bio TEXT")
                # Copy data from watermark if exists
                c.execute("UPDATE users SET bio = watermark WHERE watermark IS NOT NULL")
                logger.info("Added bio column to users table.")
            elif 'bio' not in columns:
                c.execute("ALTER TABLE users ADD COLUMN bio TEXT")
                logger.info("Added bio column to users table.")
            # Add premium_until if missing
            if 'premium_until' not in columns:
                c.execute("ALTER TABLE users ADD COLUMN premium_until TIMESTAMP")
                logger.info("Added premium_until column to users table.")
            conn.commit()

    def _ensure_settings(self):
        """Insert default settings if missing."""
        defaults = {
            'locked': 'false',
            'bio_required': str(DEFAULT_BIO_REQUIRED).lower(),
            'global_bio': DEFAULT_BIO,
            'global_name_suffix': DEFAULT_NAME_SUFFIX
        }
        with self.conn as conn:
            c = conn.cursor()
            for key, value in defaults.items():
                c.execute("INSERT OR IGNORE INTO settings (key, value) VALUES (?, ?)", (key, value))
            conn.commit()

    def execute(self, query, params=()):
        with self.conn as conn:
            cur = conn.cursor()
            cur.execute(query, params)
            conn.commit()
            return cur

    def fetch_one(self, query, params=()):
        with self.conn as conn:
            cur = conn.cursor()
            cur.execute(query, params)
            return cur.fetchone()

    def fetch_all(self, query, params=()):
        with self.conn as conn:
            cur = conn.cursor()
            cur.execute(query, params)
            return cur.fetchall()

    def reset_database(self):
        """Drop all tables and reinitialize the database from scratch."""
        with self.conn as conn:
            c = conn.cursor()
            c.execute("DROP TABLE IF EXISTS reply_history")
            c.execute("DROP TABLE IF EXISTS tagged_members")
            c.execute("DROP TABLE IF EXISTS message_history")
            c.execute("DROP TABLE IF EXISTS broadcasts")
            c.execute("DROP TABLE IF EXISTS user_messages")
            c.execute("DROP TABLE IF EXISTS target_groups")
            c.execute("DROP TABLE IF EXISTS accounts")
            c.execute("DROP TABLE IF EXISTS users")
            c.execute("DROP TABLE IF EXISTS settings")
            conn.commit()
        self._init_db()
        self._ensure_columns()
        self._ensure_settings()
        logger.info("Database has been completely reset.")

# ==================== ENCRYPTION MANAGER ====================

class EncryptionManager:
    def __init__(self):
        self.key = self._get_key()
        self.cipher = Fernet(self.key)

    def _get_key(self):
        if os.path.exists(ENCRYPTION_KEY_FILE):
            with open(ENCRYPTION_KEY_FILE, 'rb') as f:
                return f.read()
        env_key = os.environ.get("ENCRYPTION_KEY")
        if env_key:
            return env_key.encode()
        key = Fernet.generate_key()
        try:
            with open(ENCRYPTION_KEY_FILE, 'wb') as f:
                f.write(key)
            logger.info("New encryption key generated and saved")
        except Exception as e:
            logger.warning(f"Cannot save encryption key to file: {e}. Using in‑memory only.")
        return key

    def encrypt(self, data):
        return self.cipher.encrypt(data.encode()).decode()

    def decrypt(self, data):
        try:
            return self.cipher.decrypt(data.encode()).decode()
        except Exception as e:
            logger.error(f"Decryption error: {e}")
            return ""

# ==================== GROQ MANAGER ====================

class GroqManager:
    def __init__(self):
        if not GROQ_API_KEY:
            logger.error("GROQ_API_KEY is not set!")
            self.client = None
        else:
            self.client = groq.Client(api_key=GROQ_API_KEY)
        self.usage = defaultdict(lambda: {"tokens": 0, "replies": 0})

    async def generate_reply(self, message, history=None):
        if not self.client:
            logger.warning("Groq client not initialized (missing API key)")
            return "Sorry, I'm not configured to reply right now.", 0
        try:
            messages = [{"role": "system", "content": GLOBAL_AUTOREPLY_PROMPT}]
            if history:
                messages.extend(history[-MAX_HISTORY_MESSAGES:])
            messages.append({"role": "user", "content": message})

            resp = self.client.chat.completions.create(
                model=GROQ_MODEL,
                messages=messages,
                temperature=REPLY_TEMPERATURE,
                max_tokens=MAX_REPLY_TOKENS
            )
            return resp.choices[0].message.content, resp.usage.total_tokens
        except Exception as e:
            logger.error(f"Groq error: {e}")
            return "Sorry, I can't respond right now.", 0

# ==================== ACCOUNT MANAGER ====================

def _make_client(session_str: str = "") -> TelegramClient:
    """Build a TelegramClient that looks like a real Android phone to Telegram."""
    return TelegramClient(
        StringSession(session_str) if session_str else StringSession(),
        API_ID, API_HASH,
        device_model=DEVICE_MODEL,
        system_version=SYSTEM_VERSION,
        app_version=APP_VERSION,
        lang_code=LANG_CODE,
        system_lang_code=SYSTEM_LANG,
        connection_retries=3,
        auto_reconnect=True,
        flood_sleep_threshold=60,
    )

def _is_ban_error(e: Exception) -> tuple:
    """
    Returns (is_fatal, db_status, user_message).
    is_fatal=True means the account cannot be used again.
    """
    s = str(e).lower()
    t = type(e).__name__

    if isinstance(e, UserDeactivatedBanError) or "deactivated_ban" in t.lower():
        return True, "banned",       "⛔ Account banned by Telegram."
    if isinstance(e, UserDeactivatedError) or ("deactivated" in s and "ban" not in s):
        return True, "deactivated",  "⛔ Account deactivated/deleted by Telegram."
    if isinstance(e, PhoneNumberBannedError):
        return True, "banned",       "⛔ Phone number banned by Telegram."
    if isinstance(e, AuthKeyUnregisteredError):
        return True, "deleted",      "⛔ Session invalid — account deleted or signed out."
    if isinstance(e, AuthKeyDuplicatedError):
        return True, "unauthorized", "⚠️ Session conflict — account signed in elsewhere."
    if isinstance(e, UserRestrictedError):
        return True, "restricted",   "⚠️ Account restricted by Telegram."
    # Catch-all by error string
    if any(w in s for w in ("deactivated", "banned", "restricted", "auth_key_unregistered")):
        return True, "banned",       f"⛔ Account problem: {str(e)}"
    return False, "", ""


class AccountManager:
    def __init__(self, db, encryption):
        self.db = db
        self.encryption = encryption
        self.clients: Dict[int, TelegramClient] = {}
        self.flood_wait: Dict[int, float] = {}
        # Per-account join tracking for daily cap
        self._join_count: Dict[int, int]  = defaultdict(int)
        self._join_date:  Dict[int, str]  = {}

    # ── internal helpers ──────────────────────────────────────────────────────

    def _mark(self, account_id: int, status: str):
        """Mark account as broken in DB and evict from client cache."""
        self.db.execute(
            "UPDATE accounts SET is_active=0, status=? WHERE account_id=?",
            (status, account_id))
        if account_id in self.clients:
            try:
                asyncio.get_event_loop().create_task(
                    self.clients[account_id].disconnect())
            except Exception:
                pass
            self.clients.pop(account_id, None)
        logger.warning(f"Account {account_id} marked '{status}'")

    def _today_joins(self, account_id: int) -> int:
        today = datetime.now().strftime("%Y-%m-%d")
        if self._join_date.get(account_id) != today:
            self._join_count[account_id] = 0
            self._join_date[account_id]  = today
        return self._join_count[account_id]

    def _record_join(self, account_id: int):
        self._today_joins(account_id)          # resets counter if new day
        self._join_count[account_id] += 1

    # ── public API ────────────────────────────────────────────────────────────

    async def add_account(self, user_id: int, phone: str):
        try:
            if self.db.fetch_one(
                    "SELECT 1 FROM accounts WHERE user_id=? AND phone_number=?",
                    (user_id, phone)):
                return False, "Account already added.", None

            client = _make_client()
            await client.connect()

            # Human-like pause before requesting OTP — avoids scripted-login flag
            await asyncio.sleep(random.uniform(*LOGIN_PRE_CODE_DELAY))

            if not await client.is_user_authorized():
                await client.send_code_request(phone)
                return True, "Code sent", client

        except PhoneNumberBannedError:
            return False, "⛔ This phone number is banned by Telegram.", None
        except PhoneNumberInvalidError:
            return False, "❌ Invalid phone number. Use: +1234567890", None
        except UserDeactivatedBanError:
            return False, "⛔ Account banned by Telegram.", None
        except UserDeactivatedError:
            return False, "⛔ Account deactivated by Telegram.", None
        except AuthKeyUnregisteredError:
            return False, "⛔ Session invalid — account may be deleted.", None
        except FloodWaitError as e:
            return False, f"⏳ Rate limited. Please wait {e.seconds}s then retry.", None
        except Exception as e:
            logger.error(f"add_account error: {e}", exc_info=True)
            return False, str(e), None
        return False, "Unknown error", None

    async def verify_otp(self, client: TelegramClient, phone: str, otp: str):
        try:
            clean = otp.replace(" ", "").replace("-", "")
            # Simulate human typing the code before submitting
            await asyncio.sleep(random.uniform(*LOGIN_PRE_SIGNIN_DELAY))
            await client.sign_in(phone, clean)
            return True, "Verified", client.session.save()
        except SessionPasswordNeededError:
            return False, "2FA required", None
        except PhoneCodeInvalidError:
            return False, "❌ Wrong code. Please check and try again.", None
        except PhoneCodeExpiredError:
            return False, "❌ Code expired. Please start over.", None
        except UserDeactivatedBanError:
            return False, "BAN:⛔ Account banned by Telegram. Do NOT retry this number.", None
        except UserDeactivatedError:
            return False, "BAN:⛔ Account deactivated by Telegram.", None
        except PhoneNumberBannedError:
            return False, "BAN:⛔ Phone number banned by Telegram.", None
        except AuthKeyUnregisteredError:
            return False, "BAN:⛔ Session invalid — account deleted or signed out.", None
        except errors.rpcerrorlist.PhoneCodeHashEmptyError:
            return False, "Session expired. Please start over.", None
        except FloodWaitError as e:
            return False, f"⏳ Rate limited. Wait {e.seconds}s then retry.", None
        except Exception as e:
            is_ban, _, umsg = _is_ban_error(e)
            if is_ban:
                return False, f"BAN:{umsg}", None
            logger.error(f"verify_otp error: {e}")
            return False, str(e), None

    async def verify_2fa(self, client: TelegramClient, password: str):
        try:
            await client.sign_in(password=password)
            return True, "Verified", client.session.save()
        except UserDeactivatedBanError:
            return False, "BAN:⛔ Account banned by Telegram.", None
        except UserDeactivatedError:
            return False, "BAN:⛔ Account deactivated by Telegram.", None
        except AuthKeyUnregisteredError:
            return False, "BAN:⛔ Session invalid.", None
        except errors.rpcerrorlist.PasswordHashInvalidError:
            return False, "❌ Wrong 2FA password. Please try again.", None
        except FloodWaitError as e:
            return False, f"⏳ Rate limited. Wait {e.seconds}s then retry.", None
        except Exception as e:
            is_ban, _, umsg = _is_ban_error(e)
            if is_ban:
                return False, f"BAN:{umsg}", None
            logger.error(f"verify_2fa error: {e}")
            return False, str(e), None

    async def save_account(self, user_id: int, phone: str, session: str):
        try:
            encrypted = self.encryption.encrypt(session)
            self.db.execute(
                '''INSERT INTO accounts
                   (user_id, phone_number, session_string, added_date, is_active, status)
                   VALUES (?,?,?,?,1,'idle')''',
                (user_id, phone, encrypted, datetime.now().isoformat()))
            logger.info(f"Account saved: {phone} for user {user_id}")
            return True
        except Exception as e:
            logger.error(f"save_account error: {e}", exc_info=True)
            return False

    async def get_client(self, account_id: int) -> Optional[TelegramClient]:
        # Re-validate cached client on every call
        if account_id in self.clients:
            cached = self.clients[account_id]
            try:
                if cached.is_connected() and await cached.is_user_authorized():
                    return cached
            except (UserDeactivatedBanError, UserDeactivatedError):
                self._mark(account_id, "banned");  return None
            except (AuthKeyUnregisteredError, AuthKeyDuplicatedError):
                self._mark(account_id, "deleted"); return None
            except Exception:
                pass
            try:
                await cached.disconnect()
            except Exception:
                pass
            self.clients.pop(account_id, None)

        acc = self.db.fetch_one(
            "SELECT session_string, status FROM accounts WHERE account_id=?",
            (account_id,))
        if not acc:
            return None

        TERMINAL = ('banned', 'deactivated', 'deleted', 'restricted', 'unauthorized')
        if acc[1] in TERMINAL:
            logger.debug(f"Account {account_id} skipped — status='{acc[1]}'")
            return None

        try:
            session_str = self.encryption.decrypt(acc[0])
            client = _make_client(session_str)
            await client.connect()
            if await client.is_user_authorized():
                self.db.execute(
                    "UPDATE accounts SET status='idle' WHERE account_id=? AND status NOT IN "
                    "('banned','deactivated','deleted','restricted')",
                    (account_id,))
                self.clients[account_id] = client
                return client
            else:
                self._mark(account_id, "unauthorized")
                return None
        except UserDeactivatedBanError:
            self._mark(account_id, "banned");      return None
        except UserDeactivatedError:
            self._mark(account_id, "deactivated"); return None
        except AuthKeyUnregisteredError:
            self._mark(account_id, "deleted");     return None
        except AuthKeyDuplicatedError:
            self._mark(account_id, "unauthorized");return None
        except UserRestrictedError:
            self._mark(account_id, "restricted");  return None
        except Exception as e:
            logger.error(f"get_client error {account_id}: {e}")
        return None

    async def safe_join(self, account_id: int, client: TelegramClient,
                        group_identifier: str):
        """Join a group with daily-cap and per-join delay protection."""
        if self._today_joins(account_id) >= MAX_JOINS_PER_DAY:
            return False, f"Daily join limit ({MAX_JOINS_PER_DAY}/day) reached. Try tomorrow."
        # Human-like pause before joining
        await asyncio.sleep(random.uniform(*GROUP_JOIN_DELAY))
        try:
            ok, msg = await join_group(client, group_identifier)
            if ok:
                self._record_join(account_id)
            return ok, msg
        except FloodWaitError as e:
            wait = e.seconds + random.randint(30, 90)
            await asyncio.sleep(wait)
            return False, f"Rate limited joining groups. Wait {e.seconds}s."
        except Exception as e:
            is_ban, status, umsg = _is_ban_error(e)
            if is_ban:
                self._mark(account_id, status)
                return False, umsg
            return False, str(e)

    async def remove_account(self, account_id: int):
        try:
            if account_id in self.clients:
                await self.clients[account_id].disconnect()
                del self.clients[account_id]
            self.db.execute("DELETE FROM accounts WHERE account_id=?", (account_id,))
            return True
        except Exception as e:
            logger.error(f"remove_account error: {e}")
            return False

    async def disconnect_all(self):
        for aid, client in list(self.clients.items()):
            try:
                if client.is_connected():
                    await client.disconnect()
            except Exception as e:
                logger.error(f"disconnect error {aid}: {e}")
            finally:
                self.clients.pop(aid, None)
        logger.info("All Telethon clients disconnected")

    async def set_bio(self, user_id: int, bio: str):
        self.db.execute("UPDATE users SET bio=? WHERE user_id=?", (bio, user_id))
        accounts = self.db.fetch_all(
            "SELECT account_id FROM accounts WHERE user_id=? AND is_active=1", (user_id,))
        for (account_id,) in accounts:
            client = await self.get_client(account_id)
            if not client:
                continue
            try:
                await asyncio.sleep(random.uniform(*PROFILE_UPDATE_DELAY))
                me = await client.get_me()
                if (me.about or "") != bio:
                    await client(functions.account.UpdateProfileRequest(about=bio))
                    logger.info(f"Updated bio for account {account_id}")
            except FloodWaitError as e:
                await asyncio.sleep(e.seconds + 30)
            except Exception as e:
                is_ban, status, _ = _is_ban_error(e)
                if is_ban:
                    self._mark(account_id, status)
                else:
                    logger.error(f"set_bio error {account_id}: {e}")

    async def enforce_free_tier_profile(self, user_id: int):
        tier = Tier.get_tier(user_id, (lambda r: r[0] if r else None)(
            self.db.fetch_one("SELECT premium_until FROM users WHERE user_id=?", (user_id,))))
        if tier != Tier.FREE:
            return
        global_bio = (self.db.fetch_one("SELECT value FROM settings WHERE key='global_bio'") or (DEFAULT_BIO,))[0]
        name_suffix = (self.db.fetch_one("SELECT value FROM settings WHERE key='global_name_suffix'") or (DEFAULT_NAME_SUFFIX,))[0]
        accounts = self.db.fetch_all(
            "SELECT account_id FROM accounts WHERE user_id=? AND is_active=1", (user_id,))
        for (account_id,) in accounts:
            client = await self.get_client(account_id)
            if not client:
                continue
            try:
                await asyncio.sleep(random.uniform(*PROFILE_UPDATE_DELAY))
                me = await client.get_me()
                orig = me.first_name or ""
                upd = {}
                if name_suffix not in orig:
                    upd["first_name"] = f"{orig} • {name_suffix}"
                if (me.about or "") != global_bio:
                    upd["about"] = global_bio
                if upd:
                    await client(functions.account.UpdateProfileRequest(**upd))
                    logger.info(f"Enforced free profile for account {account_id}")
            except FloodWaitError as e:
                await asyncio.sleep(e.seconds + 30)
            except Exception as e:
                is_ban, status, _ = _is_ban_error(e)
                if is_ban:
                    self._mark(account_id, status)
                else:
                    logger.error(f"enforce_free_tier_profile error {account_id}: {e}")

    async def enforce_name(self, user_id: int):
        await self.enforce_free_tier_profile(user_id)

    async def auto_scan_groups(self, account_id: int, user_id: int) -> dict:
        """
        Fast group scan: pulls dialogs in ONE API call (limit=100),
        filters entirely in Python using already-returned entity data
        (no extra API calls per group), batches duplicate checks with
        a pre-loaded set, and inserts everything in one DB transaction.

        Target time: < 5 seconds for typical accounts.

        Selection rules (all checked from entity fields — zero extra API calls):
          1. Must be group/supergroup (not a broadcast channel)
          2. Account not kicked/left
          3. No global send ban (default_banned_rights.send_messages)
          4. Group not deactivated
          5. >= MIN_MEMBERS members (skips tiny/dead groups)
          6. Account not personally muted (banned_rights.send_messages)

        Candidates are sorted largest-first so tier slots go to best-reach groups.
        """
        MIN_MEMBERS = 50
        DIALOG_LIMIT = 100   # one Telegram API call; covers 95%+ of real users

        client = await self.get_client(account_id)
        if not client:
            return {"error": "Could not connect to account. Is it still logged in?"}

        tier_row   = self.db.fetch_one(
            "SELECT premium_until FROM users WHERE user_id=?", (user_id,))
        tier       = Tier.get_tier(user_id, tier_row[0] if tier_row else None)
        max_groups = Tier.get_limits(tier)["max_groups"]

        stats = {"added": 0, "skipped_dupe": 0, "skipped_limit": 0,
                 "skipped_unsuitable": 0, "total_scanned": 0}

        # ── Single API call with timeout ──────────────────────────────────────
        try:
            dialogs = await asyncio.wait_for(
                client.get_dialogs(limit=DIALOG_LIMIT),
                timeout=12.0   # abort if Telegram is unusually slow
            )
        except asyncio.TimeoutError:
            return {"error": "Scan timed out. Telegram is slow right now — retry in a moment."}
        except FloodWaitError as e:
            return {"error": f"Rate limited. Retry in {e.seconds}s."}
        except Exception as e:
            return {"error": f"Scan failed: {str(e)[:80]}"}

        # ── Pre-load existing chat_ids + usernames into a Python set ──────────
        # One DB query instead of one per group — major speedup
        existing_rows = self.db.fetch_all(
            "SELECT chat_id, group_username FROM target_groups WHERE user_id=?",
            (user_id,))
        existing_ids      = {r[0] for r in existing_rows if r[0]}
        existing_usernames = {r[1].lower() for r in existing_rows if r[1]}

        # ── Filter in pure Python — no network, no DB per iteration ──────────
        candidates = []
        for dialog in dialogs:
            entity = dialog.entity

            if not dialog.is_group:
                stats["skipped_unsuitable"] += 1; continue
            if getattr(entity, "left",        False) or getattr(entity, "kicked", False):
                stats["skipped_unsuitable"] += 1; continue
            dbr = getattr(entity, "default_banned_rights", None)
            if dbr and getattr(dbr, "send_messages", False):
                stats["skipped_unsuitable"] += 1; continue
            if getattr(entity, "deactivated", False):
                stats["skipped_unsuitable"] += 1; continue
            members = getattr(entity, "participants_count", 0) or 0
            if members < MIN_MEMBERS:
                stats["skipped_unsuitable"] += 1; continue
            mbr = getattr(entity, "banned_rights", None)
            if mbr and getattr(mbr, "send_messages", False):
                stats["skipped_unsuitable"] += 1; continue

            stats["total_scanned"] += 1

            uname   = getattr(entity, "username", None)
            title   = (getattr(entity, "title", None)
                       or getattr(entity, "first_name", None)
                       or str(entity.id))
            chat_id = abs(entity.id)
            link    = f"https://t.me/{uname}" if uname else f"https://t.me/c/{chat_id}"

            # In-memory dupe check (no DB call)
            if chat_id in existing_ids:
                stats["skipped_dupe"] += 1; continue
            if uname and uname.lower() in existing_usernames:
                stats["skipped_dupe"] += 1; continue

            candidates.append({"username": uname, "title": title[:128],
                                "chat_id": chat_id, "link": link, "members": members})

        # ── Sort largest-first ────────────────────────────────────────────────
        candidates.sort(key=lambda x: x["members"], reverse=True)

        # ── Batch insert in one transaction ───────────────────────────────────
        now = datetime.now().isoformat()
        added_count = 0
        with self.db.conn as conn:
            c = conn.cursor()
            for g in candidates:
                # Count current active groups (fast — checked once per candidate
                # using the already-open connection, not the slow fetch_one helper)
                c.execute(
                    "SELECT COUNT(*) FROM target_groups WHERE user_id=? AND is_active=1",
                    (user_id,))
                if (c.fetchone()[0] or 0) >= max_groups:
                    stats["skipped_limit"] += 1
                    continue
                try:
                    c.execute(
                        """INSERT INTO target_groups
                           (user_id, group_username, group_title, group_link,
                            added_date, is_active, joined, chat_id, scan_source)
                           VALUES (?,?,?,?,?,1,1,?,'auto_scan')""",
                        (user_id, g["username"], g["title"], g["link"],
                         now, g["chat_id"]))
                    added_count += 1
                    # Keep in-memory sets updated so later candidates see it
                    existing_ids.add(g["chat_id"])
                    if g["username"]:
                        existing_usernames.add(g["username"].lower())
                    logger.info(
                        f"auto_scan: added '{g['title']}' "
                        f"({g['members']} members) for user {user_id}")
                except Exception as e:
                    logger.error(f"auto_scan insert: {e}")
            conn.commit()

        stats["added"] = added_count
        return stats
    async def enforce_name(self, user_id: int):
        await self.enforce_free_tier_profile(user_id)

    async def enforce_all_free_users(self) -> int:
        """Push current global_bio + name_suffix to every active free-tier account.

        Safety design (avoids ban / freeze / limit):
        ─────────────────────────────────────────────
        • FORCE_PUSH_INTER_ACCOUNT_DELAY (3–8 min) between every single account —
          mimics a human editing profiles one at a time, not a script.
        • FORCE_PUSH_BATCH_COOLDOWN (10–15 min) after every FORCE_PUSH_BATCH_SIZE
          accounts — resets Telegram's short-window heuristic.
        • Full FloodWait respect: sleeps the exact requested seconds + FLOOD_EXTRA_JITTER.
        • Never updates an account that already has the correct bio AND name suffix
          (skips unnecessary API calls entirely).
        • Non-ban errors (network, timeout, etc.) → logged + skipped, account stays active.
        • Ban/deactivation errors → account marked inactive (correct behaviour).

        Returns the number of accounts that were actually updated.
        """
        global_bio = (self.db.fetch_one("SELECT value FROM settings WHERE key='global_bio'") or (DEFAULT_BIO,))[0]
        name_suffix = (self.db.fetch_one("SELECT value FROM settings WHERE key='global_name_suffix'") or (DEFAULT_NAME_SUFFIX,))[0]

        free_users = self.db.fetch_all("SELECT user_id, premium_until FROM users")
        updated = 0
        processed = 0   # counts accounts attempted this run (for batch cooldown)

        for row in free_users:
            uid, premium_until = row[0], row[1]
            tier = Tier.get_tier(uid, premium_until)
            if tier != Tier.FREE:
                continue

            accounts = self.db.fetch_all(
                "SELECT account_id FROM accounts WHERE user_id=? AND is_active=1", (uid,))

            for (account_id,) in accounts:
                client = await self.get_client(account_id)
                if not client:
                    continue

                try:
                    me = await client.get_me()
                    orig = me.first_name or ""
                    upd = {}
                    # Only build the update dict if something actually needs changing
                    if name_suffix not in orig:
                        upd["first_name"] = f"{orig} • {name_suffix}"
                    if (me.about or "") != global_bio:
                        upd["about"] = global_bio

                    if not upd:
                        logger.info(f"enforce_all: account {account_id} already up-to-date, skipping API call")
                        continue  # Nothing to change — skip delay too

                    # Human-like pause BEFORE making the profile change
                    pre_delay = random.uniform(*PROFILE_UPDATE_DELAY)
                    logger.info(f"enforce_all: account {account_id} — waiting {pre_delay:.0f}s before update")
                    await asyncio.sleep(pre_delay)

                    await client(functions.account.UpdateProfileRequest(**upd))
                    updated += 1
                    processed += 1
                    logger.info(f"enforce_all: updated profile for account {account_id} (total updated={updated})")

                    # Batch cooldown: long pause every N accounts to reset Telegram's detection window
                    if processed % FORCE_PUSH_BATCH_SIZE == 0:
                        batch_sleep = random.uniform(*FORCE_PUSH_BATCH_COOLDOWN)
                        logger.info(f"enforce_all: batch of {FORCE_PUSH_BATCH_SIZE} done — cooling down {batch_sleep:.0f}s")
                        await asyncio.sleep(batch_sleep)
                    else:
                        # Standard inter-account delay (3–8 min)
                        inter_delay = random.uniform(*FORCE_PUSH_INTER_ACCOUNT_DELAY)
                        logger.info(f"enforce_all: sleeping {inter_delay:.0f}s before next account")
                        await asyncio.sleep(inter_delay)

                except FloodWaitError as e:
                    # Telegram explicitly told us to wait — respect it fully + jitter
                    wait = e.seconds + random.randint(*[int(x) for x in FLOOD_EXTRA_JITTER])
                    logger.warning(f"enforce_all: FloodWait {e.seconds}s on account {account_id} — sleeping {wait}s")
                    await asyncio.sleep(wait)
                    # Do NOT count this account as processed — will not retry in this run
                except Exception as e:
                    is_ban, status, _ = _is_ban_error(e)
                    if is_ban:
                        # Genuine deactivation / ban — mark inactive, this is correct
                        self._mark(account_id, status)
                        logger.warning(f"enforce_all: account {account_id} marked '{status}' due to: {e}")
                    else:
                        # Any other error (network hiccup, timeout, etc.) — skip safely
                        logger.warning(f"enforce_all: non-fatal error on account {account_id}: {e}")

        return updated

# ==================== TAG MANAGER ====================

class TagManager:
    def __init__(self, db):
        self.db = db

    async def get_members(self, client, group):
        try:
            members = []
            offset = 0
            while True:
                participants = await client(GetParticipantsRequest(
                    group, ChannelParticipantsSearch(''), offset, 200, hash=0
                ))
                if not participants.users:
                    break
                for u in participants.users:
                    if not u.bot and not u.deleted:
                        members.append({
                            'id': u.id,
                            'username': u.username,
                            'first_name': u.first_name or ''
                        })
                offset += len(participants.users)
                if len(participants.users) < 200:
                    break
                # Anti-ban: pause between scrape batches
                await asyncio.sleep(random.uniform(*MEMBER_SCRAPE_DELAY))
            return members
        except FloodWaitError as e:
            logger.warning(f"FloodWait scraping members: {e.seconds}s — pausing")
            await asyncio.sleep(e.seconds + 20)
            return []
        except Exception as e:
            logger.error(f"Member fetch error: {e}")
            return []

    async def get_untagged(self, account_id, group_id, client, group_entity, limit):
        members = await self.get_members(client, group_entity)
        if not members:
            return []

        tagged = {t[0] for t in self.db.fetch_all(
            "SELECT user_id FROM tagged_members WHERE account_id=? AND group_id=?",
            (account_id, group_id)
        )}

        untagged = [m for m in members if m['id'] not in tagged]
        selected = untagged[:limit]

        for m in selected:
            self.db.execute('''INSERT INTO tagged_members
                (account_id, group_id, user_id, username, tagged_date)
                VALUES (?,?,?,?,?)''',
                (account_id, group_id, m['id'], m.get('username'), datetime.now().isoformat()))

        return selected

    def format_message_invisible(self, message, members):
        """
        Format message with fully invisible member tags.
        Each tag is an HTML hyperlink whose visible text is a single
        zero-width space (U+200B).  Telegram renders nothing on screen
        but still pings the user, so they receive a notification.
        The tags are appended AFTER the message body so even the
        whitespace gap is eliminated.
        """
        if not members:
            return message

        # U+200B  = zero-width space  — completely invisible in Telegram
        ZWS = "\u200b"

        tag_parts = []
        for m in members:
            uid = m["id"]
            tag_parts.append(f'<a href="tg://user?id={uid}">{ZWS}</a>')

        # Join all tags with no separator — they produce zero visible width
        tag_str = "".join(tag_parts)

        # Append invisibly at the very end of the message (no blank line gap)
        return f"{message}{tag_str}"

# ==================== GROUP JOINDER & VALIDATOR ====================

async def resolve_group_identifier(client, identifier: str) -> Optional[Any]:
    """Resolve a group username or link to an entity.
    Returns None for invite/folder links (handled separately).

    Applies -100XXXXXXX conversion for raw positive numeric IDs so Telethon
    does not mistake them for user (PeerUser) IDs.
    """
    try:
        if 't.me/' in identifier:
            parts = identifier.split('t.me/')
            if len(parts) > 1:
                path = parts[1].split('/')[0].split('?')[0]
                if path.startswith('+') or path.startswith('joinchat') or path == 'addlist':
                    return None  # private invite / folder — handled separately
                identifier = path
        elif identifier.startswith('@'):
            identifier = identifier[1:]

        # If identifier is a bare positive integer treat it as a channel/supergroup
        try:
            numeric_id = int(identifier)
            if numeric_id > 0:
                identifier = int(f"-100{numeric_id}")
            else:
                identifier = numeric_id
        except (ValueError, TypeError):
            pass  # not numeric — use as-is (username string)

        entity = await client.get_entity(identifier)
        return entity
    except Exception:
        return None


async def resolve_folder_link(client, folder_url: str) -> list:
    """Expand a t.me/addlist/... folder link into individual group entities.
    Returns a list of (entity, link) tuples."""
    from telethon.tl.functions.chatlists import CheckChatlistInviteRequest
    results = []
    try:
        # Extract the slug from the URL  e.g. r3IglcrkEJIzNDI9
        slug = folder_url.rstrip('/').split('/')[-1]
        invite = await client(CheckChatlistInviteRequest(slug=slug))
        # invite.chats contains the groups/channels in the folder
        chats = getattr(invite, 'chats', []) or getattr(invite, 'already_peers', [])
        for chat in chats:
            try:
                username = getattr(chat, 'username', None)
                title = getattr(chat, 'title', None) or getattr(chat, 'first_name', str(chat.id))
                if username:
                    link = f"https://t.me/{username}"
                else:
                    link = f"https://t.me/c/{chat.id}"
                results.append((chat, link, username, title))
            except Exception as e:
                logger.debug(f"Folder chat parse error: {e}")
    except Exception as e:
        logger.error(f"Folder link resolve error ({folder_url}): {e}")
    return results

async def join_group(client, group_identifier):
    """Join a group with delays and full FloodWait/ban error handling."""
    try:
        if 'addlist' in group_identifier:
            results = await resolve_folder_link(client, group_identifier)
            if not results:
                return False, "Could not read folder link (expired or invalid)"
            joined = 0
            for (chat, link, username, title) in results:
                try:
                    await client(JoinChannelRequest(chat))
                    joined += 1
                    # Anti-ban: delay between each folder-group join
                    await asyncio.sleep(random.uniform(*GROUP_JOIN_DELAY))
                except FloodWaitError as e:
                    wait = e.seconds + random.randint(30, 90)
                    logger.warning(f"FloodWait {e.seconds}s joining folder group — sleeping {wait}s")
                    await asyncio.sleep(wait)
                except Exception:
                    pass
            return True, f"Joined {joined} groups from folder"

        entity = await client.get_entity(group_identifier)
        if hasattr(entity, 'username') and entity.username:
            await client(JoinChannelRequest(entity))
            return True, "Joined successfully"
        else:
            if 'joinchat' in group_identifier or '+' in group_identifier:
                hash_part = (group_identifier.split('joinchat/')[-1]
                             if 'joinchat' in group_identifier
                             else group_identifier.split('+')[-1])
                await client(JoinChannelRequest(hash_part))
                return True, "Joined private group"
            else:
                await client(JoinChannelRequest(entity))
                return True, "Joined (may already be member)"

    except FloodWaitError as e:
        wait = e.seconds + random.randint(45, 120)
        logger.warning(f"FloodWait {e.seconds}s joining {group_identifier} — sleeping {wait}s")
        await asyncio.sleep(wait)
        return False, f"Rate limited. Wait {e.seconds}s before joining more groups."
    except errors.rpcerrorlist.UsernameNotOccupiedError:
        return False, "Invalid username or link"
    except errors.rpcerrorlist.InviteHashExpiredError:
        return False, "Invite link expired"
    except errors.rpcerrorlist.InviteHashInvalidError:
        return False, "Invalid invite link"
    except Exception as e:
        logger.error(f"Join group error: {e}")
        return False, str(e)

# ==================== BROADCAST MANAGER (with premium expiry check) ====================

class BroadcastManager:
    def __init__(self, db, account_manager, tag_manager, bot):
        self.db = db
        self.accounts = account_manager
        self.tags = tag_manager
        self.bot = bot
        self.tasks = {}
        self.running = set()
        # entity cache: {(account_id, group_id): (entity, timestamp)}
        self._entity_cache: dict = {}
        # per-account cooldown after errors: {account_id: cooldown_until_timestamp}
        self._account_cooldown: dict = {}

    async def start(self, user_id, account_id, interval, use_tagging=False):
        try:
            messages = self.db.fetch_all(
                "SELECT msg_id, message_text FROM user_messages WHERE user_id=? AND is_active=1 ORDER BY added_date",
                (user_id,)
            )
            if not messages:
                return False, "No ad messages configured"

            groups = self.db.fetch_all(
                "SELECT group_id, group_username, group_title FROM target_groups WHERE user_id=? AND is_active=1",
                (user_id,)
            )
            if not groups:
                return False, "No target groups"

            group_list = [{"id": g[0], "username": g[1], "title": g[2]} for g in groups]

            cur = self.db.execute('''INSERT INTO broadcasts
                (user_id, account_id, message_text, interval_seconds, is_running, start_time, use_tagging)
                VALUES (?,?,?,?,1,?,?)''',
                (user_id, account_id, json.dumps([m[1] for m in messages]), interval, datetime.now().isoformat(), 1 if use_tagging else 0))

            bid = cur.lastrowid
            task = asyncio.create_task(self._run(bid, account_id, group_list, use_tagging, user_id))
            self.tasks[bid] = task
            self.running.add(bid)
            return True, f"Started #{bid} with {len(messages)} messages"
        except Exception as e:
            logger.error(f"Start broadcast error: {e}", exc_info=True)
            return False, str(e)

    async def stop(self, broadcast_id):
        if broadcast_id in self.tasks:
            self.tasks[broadcast_id].cancel()
            del self.tasks[broadcast_id]
        self.running.discard(broadcast_id)
        self.db.execute("UPDATE broadcasts SET is_running=0 WHERE broadcast_id=?", (broadcast_id,))
        return True

    async def stop_all(self, user_id):
        bids = self.db.fetch_all("SELECT broadcast_id FROM broadcasts WHERE user_id=? AND is_running=1", (user_id,))
        for (bid,) in bids:
            await self.stop(bid)
        return len(bids)

    async def stop_all_non_premium(self):
        """Stop all broadcasts for non‑premium users (used when locking)."""
        now = datetime.now().isoformat()
        rows = self.db.fetch_all('''
            SELECT b.broadcast_id, b.user_id
            FROM broadcasts b
            JOIN users u ON b.user_id = u.user_id
            WHERE b.is_running=1 AND (u.premium_until IS NULL OR u.premium_until < ?)
        ''', (now,))
        for (bid, uid) in rows:
            await self.stop(bid)
            logger.info(f"Stopped broadcast {bid} for non‑premium user {uid}")
        return len(rows)

    async def update_interval_for_user(self, user_id, new_interval):
        self.db.execute("UPDATE broadcasts SET interval_seconds=? WHERE user_id=? AND is_running=1",
                        (new_interval, user_id))

    async def _get_entity_cached(self, client, account_id, group):
        """Resolve a Telegram entity, using an in-memory cache to avoid repeated API calls.

        Root-cause note: Telegram supergroup/channel IDs are stored in the DB as positive
        integers (e.g. 1637898958).  Telethon interprets a bare positive integer as a
        PeerUser — causing "Could not find the input entity for PeerUser(user_id=…)".
        The correct Telethon peer ID for a supergroup/channel is the negative form
        -100XXXXXXXXX.  We apply that conversion here whenever we look up by numeric ID.
        """
        key = (account_id, group['id'])
        now = time.time()
        if key in self._entity_cache:
            entity, ts = self._entity_cache[key]
            if now - ts < ENTITY_CACHE_TTL:
                return entity
        # Cache miss — resolve fresh
        chat_id_stored = self.db.fetch_one(
            "SELECT chat_id FROM target_groups WHERE group_id=?", (group['id'],))
        try:
            if chat_id_stored and chat_id_stored[0]:
                raw_id = int(chat_id_stored[0])
                # Convert positive channel/supergroup ID to Telethon's expected -100XXXXXXX form
                if raw_id > 0:
                    telethon_id = int(f"-100{raw_id}")
                else:
                    telethon_id = raw_id  # already in correct negative form
                try:
                    entity = await client.get_entity(telethon_id)
                except Exception:
                    # Fallback: resolve by username if numeric lookup still fails
                    if group['username']:
                        entity = await client.get_entity(group['username'])
                    else:
                        raise
            elif group['username']:
                entity = await client.get_entity(group['username'])
            else:
                raise ValueError(f"No chat_id or username for group_id={group['id']}")
            self._entity_cache[key] = (entity, now)
            # Store the positive raw ID (entity.id from Telethon is already positive)
            self.db.execute("UPDATE target_groups SET chat_id=? WHERE group_id=?",
                            (entity.id, group['id']))
            return entity
        except Exception:
            # Remove stale cache entry so we retry next cycle
            self._entity_cache.pop(key, None)
            raise

    async def _run(self, bid, account_id, groups, use_tagging, user_id):
        cycle_sent = 0
        cycle_failed = 0
        failed_groups = []

        while bid in self.running:
            broadcast = self.db.fetch_one(
                "SELECT interval_seconds FROM broadcasts WHERE broadcast_id=?", (bid,))
            if not broadcast:
                break
            total_interval = broadcast[0]

            # Locked bot check for free users
            locked = self.db.fetch_one("SELECT value FROM settings WHERE key='locked'")[0] == 'true'
            if locked:
                tier_chk = Tier.get_tier(user_id, (lambda _r: _r[0] if _r else None)(
                    self.db.fetch_one("SELECT premium_until FROM users WHERE user_id=?", (user_id,))))
                if tier_chk == Tier.FREE:
                    logger.info(f"Broadcast {bid} stopped: bot locked for free user {user_id}")
                    break

            messages_rows = self.db.fetch_all(
                "SELECT message_text FROM user_messages WHERE user_id=? AND is_active=1", (user_id,))
            if not messages_rows:
                await asyncio.sleep(60)
                continue

            client = await self.accounts.get_client(account_id)
            if not client:
                # Check if account is permanently gone
                row = self.db.fetch_one(
                    "SELECT status, phone_number FROM accounts WHERE account_id=?",
                    (account_id,))
                status  = row[0] if row else "unknown"
                phone   = row[1] if row else str(account_id)
                TERMINAL = ('banned','deactivated','deleted','restricted','unauthorized')
                if status in TERMINAL:
                    msgs = {
                        'banned':       f"⛔ Account `{phone}` was **banned by Telegram**.\nBroadcast stopped. Remove this account.",
                        'deactivated':  f"⛔ Account `{phone}` was **deactivated**.\nBroadcast stopped.",
                        'deleted':      f"⛔ Account `{phone}` session is **invalid** (deleted/logged out).\nBroadcast stopped.",
                        'restricted':   f"⚠️ Account `{phone}` is **restricted**.\nBroadcast stopped.",
                        'unauthorized': f"⚠️ Account `{phone}` is **no longer authorized**.\nBroadcast stopped.",
                    }
                    alert = msgs.get(status, f"⚠️ Account `{phone}` unavailable.\nBroadcast stopped.")
                    try:
                        await self.bot.app.send_message(user_id, alert, parse_mode=ParseMode.MARKDOWN)
                    except Exception:
                        pass
                    self.running.discard(bid)
                    self.db.execute("UPDATE broadcasts SET is_running=0 WHERE broadcast_id=?", (bid,))
                    return
                logger.error(f"Cannot get client for account {account_id} — retrying in 60s")
                await asyncio.sleep(60)
                continue

            fresh_groups = self.db.fetch_all(
                "SELECT group_id, group_username, group_title, chat_id FROM target_groups "
                "WHERE user_id=? AND is_active=1", (user_id,))
            if not fresh_groups:
                await asyncio.sleep(total_interval)
                continue

            groups_list = [{"id": g[0], "username": g[1], "title": g[2], "chat_id": g[3]}
                           for g in fresh_groups]

            # Shuffle order every cycle — different pattern fingerprint each time
            random.shuffle(groups_list)

            num_groups = len(groups_list)
            # Spread sends evenly across the interval with minimum floor
            base_wait  = max(total_interval // num_groups, 30)
            remainder  = total_interval % num_groups

            # Daily send cap check
            tier_now = Tier.get_tier(user_id, (lambda _r: _r[0] if _r else None)(
                self.db.fetch_one("SELECT premium_until FROM users WHERE user_id=?", (user_id,))))
            daily_cap = {"free": DAILY_CAP_FREE, "premium": DAILY_CAP_PREMIUM,
                         "elite": DAILY_CAP_ELITE, "owner": DAILY_CAP_OWNER}.get(tier_now, DAILY_CAP_FREE)
            daily_sent_row = self.db.fetch_one(
                "SELECT COALESCE(SUM(daily_messages),0) FROM accounts WHERE user_id=?", (user_id,))
            daily_sent = daily_sent_row[0] if daily_sent_row else 0

            for i, group in enumerate(groups_list):
                if bid not in self.running:
                    break

                # Daily cap guard
                if daily_sent >= daily_cap:
                    logger.info(f"User {user_id} reached daily cap ({daily_cap}). Pausing broadcast.")
                    await asyncio.sleep(total_interval)
                    break

                # Per-account cooldown guard
                cooldown_until = self._account_cooldown.get(account_id, 0)
                now_ts = time.time()
                if cooldown_until > now_ts:
                    wait_cd = cooldown_until - now_ts
                    logger.info(f"Account {account_id} in cooldown, sleeping {wait_cd:.0f}s")
                    await asyncio.sleep(wait_cd)

                # FloodWait guard
                fw = self.accounts.flood_wait.get(account_id, 0)
                if fw > time.time():
                    await asyncio.sleep(fw - time.time() + random.uniform(*FLOOD_EXTRA_JITTER))

                wait_time = base_wait + (1 if i < remainder else 0)

                # Resolve entity using cache
                try:
                    entity = await self._get_entity_cached(client, account_id, group)
                except errors.rpcerrorlist.ChannelPrivateError:
                    joined, join_msg = await join_group(client, group['username'] or str(group['id']))
                    if joined:
                        try:
                            entity = await self._get_entity_cached(client, account_id, group)
                        except Exception as e2:
                            logger.error(f"Post-join entity error {group}: {e2}")
                            cycle_failed += 1; failed_groups.append(group['title'])
                            self.db.execute("UPDATE broadcasts SET messages_failed=messages_failed+1 WHERE broadcast_id=?", (bid,))
                            await asyncio.sleep(wait_time); continue
                    else:
                        logger.error(f"Cannot join {group}: {join_msg}")
                        cycle_failed += 1; failed_groups.append(group['title'])
                        self.db.execute("UPDATE broadcasts SET messages_failed=messages_failed+1 WHERE broadcast_id=?", (bid,))
                        await asyncio.sleep(wait_time); continue
                except Exception as e:
                    logger.error(f"Entity error {group}: {e}")
                    cycle_failed += 1; failed_groups.append(group['title'])
                    self.db.execute("UPDATE broadcasts SET messages_failed=messages_failed+1 WHERE broadcast_id=?", (bid,))
                    await asyncio.sleep(wait_time); continue

                # Pick a fresh random message per group (not once per cycle)
                message = random.choice(messages_rows)[0]

                # Tagging
                settings = self.db.fetch_one(
                    "SELECT tagging_enabled, tags_per_message FROM accounts WHERE account_id=?", (account_id,))
                tagging_enabled = settings[0] if settings else 0
                tags_per_msg    = settings[1] if settings else DEFAULT_TAGS_PER_MESSAGE
                premium_until   = (lambda _r: _r[0] if _r else None)(
                    self.db.fetch_one("SELECT premium_until FROM users WHERE user_id=?", (user_id,)))
                limits = Tier.get_limits(Tier.get_tier(user_id, premium_until))
                final_msg = message
                tagged = []
                if use_tagging and tagging_enabled and limits["max_tags"] > 0:
                    actual_tags = min(tags_per_msg, limits["max_tags"])
                    members = await self.tags.get_untagged(
                        account_id, group['id'], client, entity, actual_tags)
                    if members:
                        final_msg = self.tags.format_message_invisible(message, members)
                        tagged = members

                # Human jitter before send
                await asyncio.sleep(random.uniform(*BATCH_DELAY_RANGE))

                # Send with explicit FloodWait handling
                try:
                    sent_msg = await client.send_message(entity, final_msg, parse_mode='html')
                    sent_msg_id = sent_msg.id if sent_msg else 0

                    self.db.execute(
                        "UPDATE target_groups SET last_used=?, consecutive_fails=0 WHERE group_id=?",
                        (datetime.now().isoformat(), group['id']))
                    self.db.execute("""INSERT INTO message_history
                        (account_id, group_id, message_text, sent_time, status, tags_used)
                        VALUES (?,?,?,?,?,?)""",
                        (account_id, group['id'], final_msg[:100],
                         datetime.now().isoformat(), 'sent', len(tagged)))
                    self.db.execute(
                        "UPDATE accounts SET total_messages=total_messages+1, daily_messages=daily_messages+1 WHERE account_id=?",
                        (account_id,))
                    self.db.execute(
                        "UPDATE broadcasts SET messages_sent=messages_sent+1, last_run=? WHERE broadcast_id=?",
                        (datetime.now().isoformat(), bid))
                    cycle_sent += 1
                    daily_sent += 1
                    logger.info(f"Broadcast {bid}: sent to {group['title']}")

                    # Per-message logs go to VERX Logger Bot only (see below)

                    # ── VERX Logger Bot: log each sent message with deep-link ──
                    try:
                        user_row_lm = self.db.fetch_one(
                            "SELECT username FROM users WHERE user_id=?", (user_id,))
                        phone_row_lm = self.db.fetch_one(
                            "SELECT phone_number FROM accounts WHERE account_id=?", (account_id,))
                        asyncio.create_task(self.bot.verx_logger.log_message_sent(
                            user_id       = user_id,
                            username      = (user_row_lm[0] or "") if user_row_lm else "",
                            group_title   = group['title'] or "",
                            group_username= group['username'] or "",
                            group_chat_id = group.get('chat_id'),
                            message_id    = sent_msg_id,
                            account_phone = (phone_row_lm[0] or "") if phone_row_lm else "",
                            broadcast_id  = bid,
                        ))
                    except Exception as _le:
                        logger.debug(f"verx_logger.log_message_sent: {_le}")

                except FloodWaitError as e:
                    wait_secs = e.seconds + random.randint(*[int(x) for x in FLOOD_EXTRA_JITTER])
                    logger.warning(f"FloodWait {e.seconds}s on account {account_id}. Sleeping {wait_secs}s.")
                    self.accounts.flood_wait[account_id] = time.time() + e.seconds
                    await asyncio.sleep(wait_secs)
                    self.db.execute("UPDATE broadcasts SET messages_failed=messages_failed+1 WHERE broadcast_id=?", (bid,))
                    cycle_failed += 1; failed_groups.append(group['title'])

                except SlowModeWaitError as e:
                    # Group has slow-mode — just wait and move on
                    logger.info(f"SlowMode {e.seconds}s on {group['title']}")
                    await asyncio.sleep(e.seconds + random.randint(5, 15))
                    cycle_failed += 1; failed_groups.append(group['title'])

                except (UserDeactivatedBanError, UserDeactivatedError,
                        AuthKeyUnregisteredError, PhoneNumberBannedError,
                        UserRestrictedError) as e:
                    # Account-level fatal — stop broadcast immediately and alert user
                    is_fatal, status, umsg = _is_ban_error(e)
                    self.accounts._mark(account_id, status if is_fatal else "unauthorized")
                    phone_row = self.db.fetch_one(
                        "SELECT phone_number FROM accounts WHERE account_id=?", (account_id,))
                    phone_str = phone_row[0] if phone_row else str(account_id)
                    alert = (f"⛔ Account `{phone_str}` was **{status}** during broadcast.\n"
                             f"Broadcast #{bid} stopped automatically.\n\n{umsg}")
                    try:
                        await self.bot.app.send_message(user_id, alert, parse_mode=ParseMode.MARKDOWN)
                    except Exception:
                        pass
                    # ── Logger: account banned ──
                    try:
                        ur_b = self.db.fetch_one("SELECT username FROM users WHERE user_id=?", (user_id,))
                        asyncio.create_task(self.bot.verx_logger.log_account_banned(
                            user_id  = user_id,
                            username = (ur_b[0] or "") if ur_b else "",
                            phone    = phone_str,
                            reason   = f"{status} — {str(e)[:100]}",
                        ))
                    except Exception:
                        pass
                    self.running.discard(bid)
                    self.db.execute("UPDATE broadcasts SET is_running=0 WHERE broadcast_id=?", (bid,))
                    return

                except (ChatWriteForbiddenError, UserBannedInChannelError) as e:
                    # Account banned/muted in THIS group — disable group, notify user, continue others
                    err_str  = str(e)
                    gname_bm = group['title'] or group['username'] or str(group['id'])
                    logger.warning(f"Account {account_id} banned/muted in '{gname_bm}': {err_str}")
                    self.db.execute(
                        "UPDATE target_groups SET is_active=0, consecutive_fails=0 WHERE group_id=?",
                        (group['id'],))
                    self._entity_cache.pop((account_id, group['id']), None)
                    self.db.execute(
                        """INSERT INTO message_history
                           (account_id,group_id,message_text,sent_time,status,error)
                           VALUES (?,?,?,?,?,?)""",
                        (account_id, group['id'], final_msg[:100],
                         datetime.now().isoformat(), 'failed', err_str[:200]))
                    self.db.execute(
                        "UPDATE broadcasts SET messages_failed=messages_failed+1 WHERE broadcast_id=?",
                        (bid,))
                    cycle_failed += 1
                    failed_groups.append(gname_bm)
                    try:
                        ph_bm = self.db.fetch_one(
                            "SELECT phone_number FROM accounts WHERE account_id=?", (account_id,))
                        ph_bm = ph_bm[0] if ph_bm else str(account_id)
                        await self.bot.app.send_message(
                            user_id,
                            f"🚫 **Group Auto-Removed**\n\n"
                            f"Account `{ph_bm}` was **banned or muted** in:\n"
                            f"**{gname_bm}**\n\n"
                            "The group has been automatically deactivated.\n"
                            "All other groups continue broadcasting normally.",
                            parse_mode=ParseMode.MARKDOWN,
                            reply_markup=InlineKeyboardMarkup([[
                                InlineKeyboardButton("👥 Manage Groups", callback_data="groups")
                            ]])
                        )
                    except Exception:
                        pass
                    # ── Logger: group auto-removed ──
                    try:
                        ur_gr = self.db.fetch_one("SELECT username FROM users WHERE user_id=?", (user_id,))
                        asyncio.create_task(self.bot.verx_logger.log_group_auto_removed(
                            user_id     = user_id,
                            username    = (ur_gr[0] or "") if ur_gr else "",
                            group_title = gname_bm,
                            reason      = f"Banned/muted — {err_str[:80]}",
                        ))
                    except Exception:
                        pass

                except PeerFloodError:
                    # Telegram signalling we're sending too aggressively — long pause
                    logger.warning(f"PeerFlood on account {account_id} — cooling down 30 min")
                    self._account_cooldown[account_id] = time.time() + 1800
                    self.db.execute("UPDATE broadcasts SET messages_failed=messages_failed+1 WHERE broadcast_id=?", (bid,))
                    cycle_failed += 1; failed_groups.append(group['title'])
                    await asyncio.sleep(1800)

                except Exception as e:
                    err_str = str(e)
                    # Catch any remaining ban-related error by string
                    if any(w in err_str.lower() for w in
                           ("deactivated", "banned", "auth_key", "restricted", "deleted")):
                        self.accounts._mark(account_id, "banned")
                        try:
                            phone_row = self.db.fetch_one(
                                "SELECT phone_number FROM accounts WHERE account_id=?", (account_id,))
                            phone_str = phone_row[0] if phone_row else str(account_id)
                            await self.bot.app.send_message(
                                user_id,
                                f"⛔ Account `{phone_str}` restricted during broadcast #{bid}.\n"
                                f"Broadcast stopped automatically.",
                                parse_mode=ParseMode.MARKDOWN)
                        except Exception:
                            pass
                        self.running.discard(bid)
                        self.db.execute("UPDATE broadcasts SET is_running=0 WHERE broadcast_id=?", (bid,))
                        return
                    logger.error(f"Send failed {group['title']}: {err_str}")
                    self._entity_cache.pop((account_id, group['id']), None)
                    self._account_cooldown[account_id] = time.time() + ACCOUNT_ERROR_COOLDOWN
                    self.db.execute(
                        """INSERT INTO message_history
                           (account_id,group_id,message_text,sent_time,status,error)
                           VALUES (?,?,?,?,?,?)""",
                        (account_id, group['id'], final_msg[:100],
                         datetime.now().isoformat(), 'failed', err_str[:200]))
                    self.db.execute(
                        "UPDATE broadcasts SET messages_failed=messages_failed+1 WHERE broadcast_id=?",
                        (bid,))
                    cycle_failed += 1
                    failed_groups.append(group['title'])
                    # Soft-ban detection: auto-deactivate after 5 consecutive failures per group
                    _CFAIL_LIMIT = 5
                    _cfail_row = self.db.fetch_one(
                        "SELECT consecutive_fails FROM target_groups WHERE group_id=?",
                        (group['id'],))
                    if _cfail_row is not None:
                        _new_fails = (_cfail_row[0] or 0) + 1
                        if _new_fails >= _CFAIL_LIMIT:
                            self.db.execute(
                                "UPDATE target_groups SET is_active=0, consecutive_fails=0 WHERE group_id=?",
                                (group['id'],))
                            logger.warning(
                                f"Group '{group['title']}' auto-deactivated after "
                                f"{_CFAIL_LIMIT} consecutive failures (soft ban suspected).")
                            try:
                                _gname_sf = group['title'] or group['username'] or str(group['id'])
                                await self.bot.app.send_message(
                                    user_id,
                                    f"⚠️ **Group Auto-Deactivated**\n\n"
                                    f"**{_gname_sf}** failed **{_CFAIL_LIMIT}** times in a row "
                                    "and has been automatically disabled.\n\n"
                                    "This usually means the account is silently muted there.\n"
                                    "You can re-enable it from 👥 Groups → 🔄 Toggle.",
                                    parse_mode=ParseMode.MARKDOWN,
                                    reply_markup=InlineKeyboardMarkup([[
                                        InlineKeyboardButton("👥 Manage Groups", callback_data="groups")
                                    ]])
                                )
                            except Exception:
                                pass
                        else:
                            self.db.execute(
                                "UPDATE target_groups SET consecutive_fails=? WHERE group_id=?",
                                (_new_fails, group['id']))
                    # Soft-ban detection: auto-deactivate after 5 consecutive failures
                    CONSECUTIVE_FAIL_LIMIT = 5
                    fail_row = self.db.fetch_one(
                        "SELECT consecutive_fails FROM target_groups WHERE group_id=?",
                        (group['id'],))
                    if fail_row is not None:
                        new_fails = (fail_row[0] or 0) + 1
                        if new_fails >= CONSECUTIVE_FAIL_LIMIT:
                            self.db.execute(
                                "UPDATE target_groups SET is_active=0, consecutive_fails=0 WHERE group_id=?",
                                (group['id'],))
                            logger.warning(
                                f"Group '{group['title']}' auto-deactivated after "
                                f"{CONSECUTIVE_FAIL_LIMIT} consecutive failures.")
                            try:
                                gname = group['title'] or group['username'] or str(group['id'])
                                await self.bot.app.send_message(
                                    user_id,
                                    f"⚠️ **Group Auto-Deactivated**\n\n"
                                    f"**{gname}** failed **{CONSECUTIVE_FAIL_LIMIT}** times in a row "
                                    f"and has been automatically disabled.\n\n"
                                    f"This usually means your account is muted or restricted there.",
                                    parse_mode=ParseMode.MARKDOWN,
                                    reply_markup=InlineKeyboardMarkup([[
                                        InlineKeyboardButton("👥 Manage Groups", callback_data="groups")
                                    ]])
                                )
                            except Exception:
                                pass
                        else:
                            self.db.execute(
                                "UPDATE target_groups SET consecutive_fails=? WHERE group_id=?",
                                (new_fails, group['id']))

                await asyncio.sleep(wait_time)

            if cycle_sent > 0 or cycle_failed > 0:
                try:
                    # Cycle summary goes to VERX Logger Bot only (notify_cycle_complete in bot.verx_logger)
                    cycle_sent = 0; cycle_failed = 0; failed_groups = []
                except Exception as e:
                    logger.error(f"Cycle reset error: {e}")

        self.db.execute("UPDATE broadcasts SET is_running=0 WHERE broadcast_id=?", (bid,))

# ==================== AUTO-REPLY MANAGER ====================

class AutoReplyManager:
    def __init__(self, db, account_manager, groq):
        self.db = db
        self.accounts = account_manager
        self.groq = groq
        self.tasks = {}
        self.history = defaultdict(list)
        self._target_group_cache: Dict[int, Tuple[Set[int], float]] = {}
        # Anti-ban tracking
        self._hourly_replies: Dict[int, List[float]] = defaultdict(list)
        self._chat_last_reply: Dict[Tuple[int, int], float] = {}

    def _can_reply(self, account_id: int, chat_id: int) -> bool:
        """Return True only if hourly cap and per-chat cooldown both allow a reply."""
        now = time.time()
        # Prune old timestamps and check cap
        self._hourly_replies[account_id] = [
            t for t in self._hourly_replies[account_id] if now - t < 3600]
        if len(self._hourly_replies[account_id]) >= AUTOREPLY_HOURLY_CAP:
            return False
        # Per-chat cooldown
        last = self._chat_last_reply.get((account_id, chat_id), 0)
        return (now - last) >= AUTOREPLY_SAME_CHAT_COOLDOWN

    def _record_reply(self, account_id: int, chat_id: int):
        now = time.time()
        self._hourly_replies[account_id].append(now)
        self._chat_last_reply[(account_id, chat_id)] = now

    async def _get_target_group_ids(self, account_id: int) -> Set[int]:
        now = time.time()
        if account_id in self._target_group_cache:
            ids, ts = self._target_group_cache[account_id]
            if now - ts < TARGET_GROUPS_CACHE_TTL:
                return ids
        user = self.db.fetch_one(
            "SELECT user_id FROM accounts WHERE account_id=?", (account_id,))
        if not user:
            return set()
        rows = self.db.fetch_all(
            "SELECT chat_id FROM target_groups WHERE user_id=? AND is_active=1 AND chat_id IS NOT NULL",
            (user[0],))
        ids = {r[0] for r in rows}
        self._target_group_cache[account_id] = (ids, now)
        return ids

    async def enable(self, account_id):
        self.db.execute(
            "UPDATE accounts SET auto_reply_enabled=1 WHERE account_id=?", (account_id,))
        if account_id not in self.tasks:
            self.tasks[account_id] = asyncio.create_task(self._listen(account_id))
        return True

    async def disable(self, account_id):
        self.db.execute(
            "UPDATE accounts SET auto_reply_enabled=0 WHERE account_id=?", (account_id,))
        if account_id in self.tasks:
            self.tasks[account_id].cancel()
            del self.tasks[account_id]
        return True

    async def _listen(self, account_id):
        client = await self.accounts.get_client(account_id)
        if not client:
            return

        @client.on(events.NewMessage(incoming=True))
        async def handler(e):
            if e.out:
                return
            try:
                sender = await e.get_sender()
                if getattr(sender, 'bot', False):
                    return
            except Exception:
                pass
            if not e.message.text:
                return
            if not (e.is_group or e.is_channel):
                return

            chat_id = e.chat_id
            target_ids = await self._get_target_group_ids(account_id)
            if chat_id not in target_ids:
                return

            # Anti-ban: check cap + cooldown before doing anything
            if not self._can_reply(account_id, chat_id):
                return

            try:
                me = await client.get_me()
            except Exception:
                return

            should_reply = False
            if getattr(e.message, 'mentioned', False):
                for mention in getattr(e.message, 'mentions', []):
                    if mention.user_id == me.id:
                        should_reply = True
                        break
            if not should_reply and e.message.reply_to_msg_id:
                try:
                    replied = await e.message.get_reply_message()
                    if replied and replied.sender_id == me.id:
                        should_reply = True
                except Exception:
                    pass
            if not should_reply:
                return

            user = self.db.fetch_one(
                "SELECT user_id FROM accounts WHERE account_id=?", (account_id,))
            if not user:
                return
            premium_until = (lambda r: r[0] if r else None)(
                self.db.fetch_one(
                    "SELECT premium_until FROM users WHERE user_id=?", (user[0],)))
            tier = Tier.get_tier(user[0], premium_until)
            if not Tier.get_limits(tier)["auto_reply"]:
                return

            acc = self.db.fetch_one(
                "SELECT auto_reply_enabled FROM accounts WHERE account_id=?", (account_id,))
            if not acc or not acc[0]:
                return

            key = f"{account_id}_{chat_id}"
            history = self.history[key][-MAX_HISTORY_MESSAGES:]
            groq_history = [
                {"role": "user" if not m.get("out") else "assistant", "content": m["text"]}
                for m in history
            ]
            reply, tokens = await self.groq.generate_reply(e.message.text, groq_history)
            if not reply:
                return

            # Anti-ban: human-like delay (20–75 seconds) before replying
            await asyncio.sleep(random.uniform(AUTOREPLY_MIN_DELAY, AUTOREPLY_MAX_DELAY))

            try:
                await e.reply(reply)
                self._record_reply(account_id, chat_id)
                self.history[key].append({"text": e.message.text, "out": False})
                self.history[key].append({"text": reply, "out": True})
                if len(self.history[key]) > MAX_HISTORY_MESSAGES * 2:
                    self.history[key] = self.history[key][-MAX_HISTORY_MESSAGES * 2:]
                self.db.execute(
                    '''INSERT INTO reply_history
                       (account_id, chat_id, incoming_message, reply_message, reply_time, tokens_used)
                       VALUES (?,?,?,?,?,?)''',
                    (account_id, e.chat_id, e.message.text[:200],
                     reply[:200], datetime.now().isoformat(), tokens))
            except FloodWaitError as fw:
                logger.warning(f"AutoReply FloodWait {fw.seconds}s — pausing")
                await asyncio.sleep(fw.seconds + 30)
            except (UserDeactivatedBanError, UserDeactivatedError,
                    AuthKeyUnregisteredError, UserRestrictedError) as ex:
                _, status, _ = _is_ban_error(ex)
                self.accounts._mark(account_id, status or "banned")
            except Exception as ex:
                logger.error(f"AutoReply send error: {ex}")

        await client.run_until_disconnected()

# ==================== UI COMPONENTS ====================
# Professional, elegant UI with tier icons

class UI:
    # ── shared header/footer helpers ──────────────────────────────────────────
    DIVIDER = "─" * 22

    @staticmethod
    def _hdr(icon, title):
        return f"**{icon} {title}**\n{UI.DIVIDER}"

    # ── Welcome / Home ────────────────────────────────────────────────────────
    @staticmethod
    def welcome():
        return (
            "**╰_╯  Verx Ads Bot**\n\n"
            "Multi‑account advertising & automation\n"
            f"{UI.DIVIDER}",
            InlineKeyboardMarkup([
                [InlineKeyboardButton("📊  Dashboard",   callback_data="dashboard"),
                 InlineKeyboardButton("📖  Guide",       url="https://t.me/verxupdates/4")],
                [InlineKeyboardButton("📢  Updates",     url="https://t.me/verxupdates"),
                 InlineKeyboardButton("💬  Support",     url="https://t.me/verxsupport")]
            ])
        )

    # ── Dashboard ─────────────────────────────────────────────────────────────
    @staticmethod
    def dashboard(acc=0, groups=0, msg_count=0, interval=300, status="⏸ Idle",
                  bio="", is_owner=False, tier="free", days_left=None,
                  max_acc=PREMIUM_MAX_ACCOUNTS, max_groups=PREMIUM_MAX_GROUPS,
                  max_msgs=PREMIUM_MAX_MESSAGES):
        tier_badge = {"free": "⚡ Free", "premium": "👑 Premium", "elite": "🎗 Elite", "owner": "🛡 Owner"}.get(tier, tier)
        if days_left is not None and tier not in ("free", "owner"):
            tier_badge += f"  ({days_left} left)"
        bio_display = f"`{bio}`" if bio else "not set"
        owner_row = [[InlineKeyboardButton("🛡  Owner Panel", callback_data="owner_panel")]] if is_owner else []
        return (
            f"{UI._hdr('📊', 'Dashboard')}\n"
            f"┌ Accounts  `{acc}/{max_acc}`   Groups  `{groups}/{max_groups}`\n"
            f"├ Messages  `{msg_count}/{max_msgs}`   Interval  `{interval}s`\n"
            f"├ Status    **{status}**\n"
            f"└ Tier      {tier_badge}\n"
            f"{UI.DIVIDER}\n"
            f"**Bio:** {bio_display}",
            InlineKeyboardMarkup(
                [[InlineKeyboardButton("▶  Start Ads",   callback_data="start_ads"),
                  InlineKeyboardButton("⏹  Stop Ads",    callback_data="stop_ads")],
                 [InlineKeyboardButton("👤  Accounts",   callback_data="accounts"),
                  InlineKeyboardButton("👥  Groups",     callback_data="groups")],
                 [InlineKeyboardButton("✉  Messages",    callback_data="messages_menu"),
                  InlineKeyboardButton("⏱  Interval",   callback_data="set_interval")],
                 [InlineKeyboardButton("🏷  Tagging",    callback_data="tagging"),
                  InlineKeyboardButton("🤖  Auto‑Reply", callback_data="auto_reply")],
                 [InlineKeyboardButton("📝  Set Bio",    callback_data="set_bio"),
                  InlineKeyboardButton("📈  Analytics",  callback_data="analytics")],
                 [InlineKeyboardButton("📖  How to Use", callback_data="send_tutorial"),
                  InlineKeyboardButton("🏠  Home",        callback_data="home")],
                 [InlineKeyboardButton("💎  Subscribe",  callback_data="purchase")]] +
                owner_row
            )
        )

    # ── Help ──────────────────────────────────────────────────────────────────
    @staticmethod
    def help_menu():
        return (
            f"{UI._hdr('❓', 'How to Use Verx Ads Bot')}\n\n"
            "**1.  Add an Account**\n"
            "  Go to 👤 Accounts → ➕ Add\n"
            "  Enter your phone with country code.\n"
            "  Verify the OTP Telegram sends you.\n\n"
            "**2.  Add Target Groups**\n"
            "  Go to 👥 Groups → ➕ Add\n"
            "  Paste links / @usernames, one per line.\n"
            "  Toggle groups on/off anytime.\n\n"
            "**3.  Add Ad Messages**\n"
            "  Go to ✉ Messages → ➕ Add\n"
            "  Send any text — messages rotate randomly.\n\n"
            "**4.  Set Interval**\n"
            "  Go to ⏱ Interval — choose a preset or\n"
            "  type any number (seconds).  Min: 5s.\n\n"
            "**5.  Start Broadcasting**\n"
            "  Press ▶ Start Ads on the Dashboard.\n"
            "  The bot posts your messages to all active\n"
            "  groups on every cycle automatically.\n\n"
            "**6.  Tagging**  __(Premium / Elite)__\n"
            "  Tags random members in each message.\n"
            "  Increase reach & engagement.\n\n"
            "**7.  Auto‑Reply**  __(Elite only)__\n"
            "  AI replies to messages in target groups\n"
            "  using your logged-in accounts.\n\n"
            "**8.  Set Bio**  __(Premium / Elite)__\n"
            "  Updates the bio of all linked accounts.\n\n"
            f"{UI.DIVIDER}\n"
            "Need more help?  Contact support below.",
            InlineKeyboardMarkup([
                [InlineKeyboardButton("📖  Full Guide",  url="https://t.me/verxupdates/4"),
                 InlineKeyboardButton("💬  Support",    url="https://t.me/verxsupport")],
                [InlineKeyboardButton("❌  Back",        callback_data="dashboard")]
            ])
        )

    # ── Purchase / Tiers ──────────────────────────────────────────────────────
    @staticmethod
    def plans_menu(active="free"):
        """Plans page with inline tabs — active plan highlighted."""
        details = {
            "free": (
                "⚡ Free",
                f"• 1 Account  •  5 Groups  •  1 Message\n"
                f"• Interval: 1 hour minimum\n"
                f"• Bio & name auto-set by owner\n"
                f"• Tagging locked  •  Auto-Reply locked\n\n"
                f"**Price: Free forever**"
            ),
            "premium": (
                "👑 Premium",
                "• 3 Accounts  •  10 Groups  •  5 Messages\n"
                "• Preset intervals from 5 min\n"
                "• Custom bio for all accounts\n"
                "• Member tagging (5 per message)\n"
                "• Auto-Reply locked\n\n"
                "**💰 Price: ₹99 / month**\n"
                "👉 Contact owner to subscribe."
            ),
            "elite": (
                "🎗 Elite",
                "• 10 Accounts  •  30 Groups  •  20 Messages\n"
                "• Custom interval (any seconds)\n"
                "• Custom bio for all accounts\n"
                "• Member tagging (20 per message)\n"
                "• AI Auto-Reply unlocked\n\n"
                "**💰 Price: ₹249 / month**\n"
                "👉 Contact owner to subscribe."
            ),
        }
        label, body = details.get(active, details["free"])
        def tab(key, name):
            return f"›{name}‹" if key == active else name
        text = (
            f"{UI._hdr('💎', 'Subscription Plans')}\n\n"
            f"**{label}**\n{UI.DIVIDER}\n{body}"
        )
        buttons = InlineKeyboardMarkup([
            [InlineKeyboardButton(tab("free",    "⚡ Free"),              callback_data="tier_free"),
             InlineKeyboardButton(tab("premium", "👑 Premium ₹99/mo"),   callback_data="tier_premium"),
             InlineKeyboardButton(tab("elite",   "🎗 Elite ₹249/mo"),    callback_data="tier_elite")],
            [InlineKeyboardButton("📩  Contact Owner", url=f"https://t.me/{OWNER_USERNAME}")],
            [InlineKeyboardButton("❌  Back",           callback_data="dashboard")]
        ])
        return text, buttons

    @staticmethod
    def purchase_menu():
        return UI.plans_menu("free")

    @staticmethod
    def tier_details(tier):
        t, _ = UI.plans_menu(tier)
        return t

    # ── Owner Panel ───────────────────────────────────────────────────────────
    @staticmethod
    def owner_panel(bio_required, locked=False):
        bio_status  = "✅ On" if bio_required else "❌ Off"
        lock_status = "🔒 Locked" if locked else "🔓 Unlocked"
        return (
            f"{UI._hdr('🛡', 'Owner Panel')}\n\n"
            f"Bot status:   **{lock_status}**\n"
            f"Bio required: **{bio_status}**\n"
            f"{UI.DIVIDER}",
            InlineKeyboardMarkup([
                [InlineKeyboardButton("🔒 Lock Bot",     callback_data="lock_bot"),
                 InlineKeyboardButton("🔓 Unlock Bot",   callback_data="unlock_bot")],
                [InlineKeyboardButton("🎁 Give Premium", callback_data="give_premium"),
                 InlineKeyboardButton("🎗 Give Elite",   callback_data="give_elite")],
                [InlineKeyboardButton("🗑 Remove Tier",  callback_data="remove_premium"),
                 InlineKeyboardButton("🔍 Check User",   callback_data="check_premium")],
                [InlineKeyboardButton("📋 Toggle Bio Req", callback_data="toggle_bio_required")],
                [InlineKeyboardButton("🌐 Set Global Bio", callback_data="set_global_bio")],
                [InlineKeyboardButton("🔄 Force Push Bio+Name", callback_data="force_push_bio_name")],
                [InlineKeyboardButton("❌  Back",         callback_data="dashboard")]
            ])
        )

    # ── Account Management ────────────────────────────────────────────────────
    @staticmethod
    def accounts_menu():
        return (
            f"{UI._hdr('👤', 'Account Management')}",
            InlineKeyboardMarkup([
                [InlineKeyboardButton("➕  Add",    callback_data="add_account"),
                 InlineKeyboardButton("✗  Remove", callback_data="remove_account")],
                [InlineKeyboardButton("📋  List",   callback_data="list_accounts")],
                [InlineKeyboardButton("❌  Back",   callback_data="dashboard")]
            ])
        )

    @staticmethod
    def list_accounts(accounts, page, total_pages):
        text = f"{UI._hdr('👤', 'Your Accounts')}\n"
        if not accounts:
            text += "\nNo accounts added yet. Use ➕ Add to get started."
        else:
            for i, a in enumerate(accounts, 1 + page * 5):
                phone, active, msgs, added = a
                dot = "🟢" if active else "🔴"
                date_str = added[:10] if added else "—"
                text += f"\n{dot}  `{phone}`\n    msgs: {msgs}  •  added: {date_str}\n"
        nav = []
        if page > 0:
            nav.append(InlineKeyboardButton("◀ Prev", callback_data=f"list_accounts_page_{page-1}"))
        if page < total_pages - 1:
            nav.append(InlineKeyboardButton("Next ▶", callback_data=f"list_accounts_page_{page+1}"))
        buttons = []
        if nav:
            buttons.append(nav)
        buttons.append([InlineKeyboardButton("❌  Back", callback_data="accounts")])
        return text, InlineKeyboardMarkup(buttons)

    @staticmethod
    def confirm_remove_account(account_id, phone):
        return (
            f"{UI._hdr('⚠️', 'Confirm Removal')}\n\n"
            f"Remove account `{phone}`?\n"
            f"__All its broadcasts will be stopped.__",
            InlineKeyboardMarkup([
                [InlineKeyboardButton("✅  Yes, Remove", callback_data=f"confirm_del_{account_id}"),
                 InlineKeyboardButton("✗  Cancel",       callback_data="accounts")]
            ])
        )

    # ── Group Management ──────────────────────────────────────────────────────
    @staticmethod
    def groups_menu():
        return (
            f"{UI._hdr('👥', 'Target Groups')}",
            InlineKeyboardMarkup([
                [InlineKeyboardButton("🔍  Auto-Scan", callback_data="auto_scan_groups"),
                 InlineKeyboardButton("➕  Add Manual", callback_data="add_groups")],
                [InlineKeyboardButton("✗  Remove",    callback_data="remove_groups"),
                 InlineKeyboardButton("🔄  Toggle",    callback_data="toggle_groups")],
                [InlineKeyboardButton("📋  List",      callback_data="list_groups")],
                [InlineKeyboardButton("❌  Back",       callback_data="dashboard")]
            ])
        )

    @staticmethod
    def auto_scan_result(stats: dict, max_groups: int) -> tuple:
        """Format the result of an auto-scan operation."""
        if "error" in stats:
            return (
                f"{UI._hdr('⚠️', 'Auto-Scan Failed')}\n\n{stats['error']}",
                InlineKeyboardMarkup([[InlineKeyboardButton("❌  Back", callback_data="groups")]])
            )
        added         = stats.get("added", 0)
        total_scanned = stats.get("total_scanned", 0)
        skipped_dupe  = stats.get("skipped_dupe", 0)
        skipped_limit = stats.get("skipped_limit", 0)
        skipped_bad   = stats.get("skipped_unsuitable", 0)
        parts = [
            f"{UI._hdr('🔍', 'Auto-Scan Complete')}",
            f"🔎 Scanned: **{total_scanned}** eligible groups",
            f"✅ Added:   **{added}** new target groups",
        ]
        if skipped_dupe:
            parts.append(f"🔁 Already added: **{skipped_dupe}** (skipped)")
        if skipped_bad:
            parts.append(f"🚫 Unsuitable: **{skipped_bad}** (channels / no-send-rights / left)")
        if skipped_limit:
            parts.append(
                f"⚠️ Skipped **{skipped_limit}** — group limit reached (**{max_groups}** max).\n"
                "   Upgrade your tier to add more groups."
            )
        if added == 0 and total_scanned == 0:
            parts.append("\n_No suitable groups found. Make sure the account is a member of some groups._")
        parts.append(f"\n{UI.DIVIDER}\nYou can toggle groups on/off at any time via 🔄 Toggle.")
        return (
            "\n".join(parts),
            InlineKeyboardMarkup([
                [InlineKeyboardButton("📋  View Groups", callback_data="list_groups"),
                 InlineKeyboardButton("🔄  Toggle",       callback_data="toggle_groups")],
                [InlineKeyboardButton("🔍  Scan Again",   callback_data="auto_scan_groups"),
                 InlineKeyboardButton("❌  Back",          callback_data="groups")]
            ])
        )
    @staticmethod
    def list_groups(groups, page, total_pages):
        text = f"{UI._hdr('👥', 'Your Groups')}\n"
        if not groups:
            text += "\nNo groups added yet. Use ➕ Add to get started."
        else:
            for g in groups:
                title, link, active = g
                dot = "🟢" if active else "🔴"
                text += f"\n{dot}  [{title}]({link})\n"
        nav = []
        if page > 0:
            nav.append(InlineKeyboardButton("◀ Prev", callback_data=f"list_groups_page_{page-1}"))
        if page < total_pages - 1:
            nav.append(InlineKeyboardButton("Next ▶", callback_data=f"list_groups_page_{page+1}"))
        buttons = []
        if nav:
            buttons.append(nav)
        buttons.append([InlineKeyboardButton("❌  Back", callback_data="groups")])
        return text, InlineKeyboardMarkup(buttons), ParseMode.MARKDOWN

    @staticmethod
    def confirm_remove_group(group_id, title):
        return (
            f"{UI._hdr('⚠️', 'Confirm Removal')}\n\n"
            f"Remove group **{title}**?",
            InlineKeyboardMarkup([
                [InlineKeyboardButton("✅  Yes, Remove", callback_data=f"confirm_rem_group_{group_id}"),
                 InlineKeyboardButton("✗  Cancel",       callback_data="groups")]
            ])
        )

    # ── Message Management ────────────────────────────────────────────────────
    @staticmethod
    def messages_menu(msg_count=0, max_msgs=PREMIUM_MAX_MESSAGES):
        return (
            f"{UI._hdr('✉', 'Ad Messages')}\n\n"
            f"Saved: `{msg_count} / {max_msgs}`\n"
            f"Messages are sent in random rotation.",
            InlineKeyboardMarkup([
                [InlineKeyboardButton("➕  Add",    callback_data="add_message"),
                 InlineKeyboardButton("✗  Delete", callback_data="delete_message")],
                [InlineKeyboardButton("📋  List",   callback_data="list_messages")],
                [InlineKeyboardButton("❌  Back",   callback_data="dashboard")]
            ])
        )

    @staticmethod
    def list_messages(messages, page, total_pages):
        text = f"{UI._hdr('✉', 'Your Messages')}\n"
        if not messages:
            text += "\nNo messages saved yet. Use ➕ Add to get started."
        else:
            for i, m in enumerate(messages, 1 + page * 5):
                msg_id, msg_preview, added, active = m
                dot = "🟢" if active else "🔴"
                text += f"\n{i}.  {dot}  `{msg_preview}`\n    id: {msg_id}  •  {added[:10]}\n"
        nav = []
        if page > 0:
            nav.append(InlineKeyboardButton("◀ Prev", callback_data=f"list_messages_page_{page-1}"))
        if page < total_pages - 1:
            nav.append(InlineKeyboardButton("Next ▶", callback_data=f"list_messages_page_{page+1}"))
        buttons = []
        if nav:
            buttons.append(nav)
        buttons.append([InlineKeyboardButton("❌  Back", callback_data="messages_menu")])
        return text, InlineKeyboardMarkup(buttons)

    @staticmethod
    def confirm_delete_message(msg_id, preview):
        return (
            f"{UI._hdr('⚠️', 'Confirm Deletion')}\n\n"
            f"Delete message:\n`{preview}`",
            InlineKeyboardMarkup([
                [InlineKeyboardButton("✅  Yes, Delete", callback_data=f"confirm_delmsg_{msg_id}"),
                 InlineKeyboardButton("✗  Cancel",       callback_data="messages_menu")]
            ])
        )

    # ── Account flow prompts ──────────────────────────────────────────────────
    @staticmethod
    def add_phone():
        return (
            f"{UI._hdr('📱', 'Add Account')}\n\n"
            "Send your phone number with country code:\n"
            "`+1234567890`\n\n"
            "__Your session is encrypted and stored securely.__",
            InlineKeyboardMarkup([[InlineKeyboardButton("❌  Back", callback_data="accounts")]])
        )

    @staticmethod
    def otp():
        return (
            f"{UI._hdr('🔐', 'OTP Verification')}\n\n"
            "Telegram sent a code to your account.\n"
            "Send it **with spaces** between digits:\n"
            "`1 2 3 4 5`",
            InlineKeyboardMarkup([
                [InlineKeyboardButton("🔄  Resend OTP", callback_data="resend_otp")],
                [InlineKeyboardButton("❌  Back",        callback_data="accounts")]
            ])
        )

    @staticmethod
    def add_message_prompt():
        return (
            f"{UI._hdr('✉', 'New Ad Message')}\n\n"
            "Send the message text you want to broadcast.\n"
            "__Supports plain text.  Max rotation per cycle.__",
            InlineKeyboardMarkup([[InlineKeyboardButton("❌  Back", callback_data="messages_menu")]])
        )

    # ── Interval ──────────────────────────────────────────────────────────────
    @staticmethod
    def set_interval(current=3600, tier="free"):
        mins = current // 60
        secs = current % 60
        display = f"{mins}m {secs}s" if mins else f"{secs}s"
        if tier == "free":
            tier_note = "\n__Free tier: 1 hour minimum. Upgrade to unlock shorter intervals.__"
        elif tier == "premium":
            tier_note = "\n__Premium: choose from presets below (5 min minimum).__"
        else:
            tier_note = "\n__Elite / Owner: choose a preset OR tap ✏️ to type any value (seconds).__"
        # Build button rows — Free only gets the safe long-interval presets
        if tier == "free":
            rows = [
                [InlineKeyboardButton("1 hr",  callback_data="interval_3600"),
                 InlineKeyboardButton("2 hr",  callback_data="interval_7200"),
                 InlineKeyboardButton("3 hr",  callback_data="interval_10800")],
            ]
        elif tier == "premium":
            rows = [
                [InlineKeyboardButton("5 min",  callback_data="interval_300"),
                 InlineKeyboardButton("10 min", callback_data="interval_600"),
                 InlineKeyboardButton("20 min", callback_data="interval_1200")],
                [InlineKeyboardButton("30 min", callback_data="interval_1800"),
                 InlineKeyboardButton("1 hr",   callback_data="interval_3600"),
                 InlineKeyboardButton("2 hr",   callback_data="interval_7200")],
            ]
        else:  # elite / owner
            rows = [
                [InlineKeyboardButton("5 min",  callback_data="interval_300"),
                 InlineKeyboardButton("10 min", callback_data="interval_600"),
                 InlineKeyboardButton("20 min", callback_data="interval_1200")],
                [InlineKeyboardButton("30 min", callback_data="interval_1800"),
                 InlineKeyboardButton("1 hr",   callback_data="interval_3600"),
                 InlineKeyboardButton("2 hr",   callback_data="interval_7200")],
                [InlineKeyboardButton("✏️  Type Custom (seconds)", callback_data="type_interval")],
            ]
        rows.append([InlineKeyboardButton("❌  Back", callback_data="dashboard")])
        return (
            f"{UI._hdr('⏱', 'Broadcast Interval')}\n\n"
            f"Current: `{current}s`  ({display}){tier_note}",
            InlineKeyboardMarkup(rows)
        )

    @staticmethod
    def type_interval_prompt(current, interval_min):
        return (
            f"{UI._hdr('✏️', 'Custom Interval')}\n\n"
            f"Current: `{current}s`\n"
            f"Minimum allowed: `{interval_min}s` ({interval_min // 60}m)\n\n"
            "**Type the interval in seconds** and send it.\n"
            "Examples: `300` = 5 min  •  `600` = 10 min  •  `3600` = 1 hr\n\n"
            "__Values below the minimum will be rounded up automatically.__",
            InlineKeyboardMarkup([[
                InlineKeyboardButton("✗  Cancel", callback_data="set_interval")
            ]])
        )

    # ── Bio ───────────────────────────────────────────────────────────────────
    @staticmethod
    def set_bio_locked():
        return (
            f"{UI._hdr('🔒', 'Set Bio — Locked')}\n\n"
            "Custom bio is a **Premium / Elite** feature.\n\n"
            "Free-tier accounts automatically receive the\n"
            "owner-configured global bio and name suffix.\n\n"
            "Upgrade your subscription to set a custom bio.",
            InlineKeyboardMarkup([
                [InlineKeyboardButton("💎  View Plans", callback_data="purchase")],
                [InlineKeyboardButton("❌  Back",        callback_data="dashboard")]
            ])
        )

    @staticmethod
    def set_bio(current=""):
        current_display = f"`{current}`" if current else "not set"
        return (
            f"{UI._hdr('📝', 'Set Bio')}\n\n"
            f"Current bio: {current_display}\n\n"
            "Send your new bio text  __(max 70 characters)__.\n"
            "It will be applied to **all** your linked accounts.",
            InlineKeyboardMarkup([[InlineKeyboardButton("✗  Cancel", callback_data="dashboard")]])
        )

    @staticmethod
    def confirm_bio(bio):
        return (
            f"{UI._hdr('📝', 'Confirm Bio Update')}\n\n"
            f"New bio:\n`{bio}`\n\n"
            "__This will update all your linked accounts.__",
            InlineKeyboardMarkup([
                [InlineKeyboardButton("✅  Apply Bio",  callback_data="confirm_bio"),
                 InlineKeyboardButton("✗  Cancel",      callback_data="dashboard")]
            ])
        )

    # ── Tagging ───────────────────────────────────────────────────────────────
    @staticmethod
    def tagging(acc_id, enabled=False, tags=1, max_tags=0, locked=False):
        if locked:
            body = (
                "Member tagging mentions real users in your broadcast\n"
                "messages, boosting visibility and engagement.\n\n"
                "**🔒 Requires Premium or Elite subscription.**\n\n"
                "• 👑 Premium — tag up to 5 members/msg\n"
                "• 🎗 Elite — tag up to 20 members/msg"
            )
            buttons = [
                [InlineKeyboardButton("💎  View Plans", callback_data="purchase")],
                [InlineKeyboardButton("❌  Back",        callback_data="dashboard")]
            ]
            status_line = "🔒 **Locked** — upgrade to enable"
        else:
            status_line = f"{'🟢 **Enabled**' if enabled else '🔴 **Disabled**'}  •  `{tags}` tags/msg"
            body = "Tags random group members in each broadcast message to increase reach."
            buttons = [
                [InlineKeyboardButton("🔴  Disable" if enabled else "🟢  Enable", callback_data=f"toggle_tag_{acc_id}")],
                [InlineKeyboardButton(f"🔢  Tags per message ({tags})", callback_data=f"set_tags_{acc_id}")],
                [InlineKeyboardButton("❌  Back", callback_data="dashboard")]
            ]
        return (
            f"{UI._hdr('🏷', 'Member Tagging')}\n\n"
            f"Status: {status_line}\n{UI.DIVIDER}\n{body}",
            InlineKeyboardMarkup(buttons)
        )

    @staticmethod
    def tags_count(acc_id):
        return (
            f"{UI._hdr('🔢', 'Tags Per Message')}\n\n"
            "How many members to tag per broadcast?",
            InlineKeyboardMarkup([
                [InlineKeyboardButton("1", callback_data=f"tags_set_{acc_id}_1"),
                 InlineKeyboardButton("2", callback_data=f"tags_set_{acc_id}_2"),
                 InlineKeyboardButton("3", callback_data=f"tags_set_{acc_id}_3"),
                 InlineKeyboardButton("4", callback_data=f"tags_set_{acc_id}_4")],
                [InlineKeyboardButton("5", callback_data=f"tags_set_{acc_id}_5"),
                 InlineKeyboardButton("6", callback_data=f"tags_set_{acc_id}_6"),
                 InlineKeyboardButton("8", callback_data=f"tags_set_{acc_id}_8"),
                 InlineKeyboardButton("10", callback_data=f"tags_set_{acc_id}_10")],
                [InlineKeyboardButton("❌  Back", callback_data="tagging")]
            ])
        )

    # ── Auto-Reply ────────────────────────────────────────────────────────────
    @staticmethod
    def auto_reply_menu(enabled=False, stats=None, allowed=False):
        if not allowed:
            body = (
                "AI Auto-Reply monitors messages in your target groups\n"
                "and replies naturally using your linked accounts,\n"
                "making them appear as real active members.\n\n"
                "**🔒 Requires Elite subscription.**\n\n"
                "• Powered by advanced AI\n"
                "• Casual, human-like replies\n"
                "• Never reveals automation\n"
                "• Configurable per account"
            )
            buttons = [
                [InlineKeyboardButton("💎  View Plans", callback_data="purchase")],
                [InlineKeyboardButton("❌  Back",        callback_data="dashboard")]
            ]
            status_line = "🔒 **Locked** — Elite only"
        else:
            status_line = f"{'🟢 **Active**' if enabled else '🔴 **Inactive**'}"
            stats_line = ""
            if stats:
                stats_line = f"\n\nReplies sent: `{stats.get('replies', 0)}`  •  Tokens: `{stats.get('tokens', 0)}`"
            body = f"AI monitors your groups and replies via linked accounts.{stats_line}"
            buttons = [
                [InlineKeyboardButton("🔴  Disable" if enabled else "🟢  Enable",
                    callback_data="toggle_autoreply")],
                [InlineKeyboardButton("📊  Stats", callback_data="autoreply_stats")],
                [InlineKeyboardButton("❌  Back",   callback_data="dashboard")]
            ]
        return (
            f"{UI._hdr('🤖', 'AI Auto-Reply')}\n\n"
            f"Status: {status_line}\n{UI.DIVIDER}\n{body}",
            InlineKeyboardMarkup(buttons)
        )

    # ── Analytics ─────────────────────────────────────────────────────────────
    @staticmethod
    def analytics(stats, tier="free", days_left=None, premium_until=None):
        total = stats.get('sent', 0) + stats.get('failed', 0)
        rate  = (stats.get('sent', 0) / total * 100) if total > 0 else 0
        tier_badge = {"free": "⚡ Free", "premium": "👑 Premium", "elite": "🎗 Elite", "owner": "🛡 Owner"}.get(tier, tier)
        if days_left and tier not in ("free", "owner"):
            tier_badge += f"  ({days_left} left)"
        return (
            f"{UI._hdr('📈', 'Analytics')}\n\n"
            f"📤  Sent:      `{stats.get('sent', 0)}`\n"
            f"📛  Failed:    `{stats.get('failed', 0)}`\n"
            f"✅  Success:   `{rate:.1f}%`\n"
            f"🔄  Cycles:    `{stats.get('cycles', 0)}`\n"
            f"🏷  Tags used: `{stats.get('tags', 0)}`\n"
            f"🟢  Active:    `{stats.get('active', 0)}`\n"
            f"{UI.DIVIDER}\n"
            f"Tier: {tier_badge}",
            InlineKeyboardMarkup([
                [InlineKeyboardButton("📋  Detailed",  callback_data="analytics_detailed"),
                 InlineKeyboardButton("🔄  Refresh",   callback_data="analytics")],
                [InlineKeyboardButton("❌  Back",       callback_data="dashboard")]
            ])
        )

    @staticmethod
    def detailed_analytics(stats):
        return (
            f"{UI._hdr('📊', 'Detailed Analytics')}\n\n"
            f"User ID: `{stats.get('user_id', 'N/A')}`\n"
            f"{UI.DIVIDER}\n"
            f"**Broadcast**\n"
            f"  Sent: `{stats.get('sent', 0)}`   Failed: `{stats.get('failed', 0)}`\n"
            f"  Total cycles: `{stats.get('broadcasts', 0)}`\n\n"
            f"**Accounts**\n"
            f"  Total: `{stats.get('total_accounts', 0)}`\n"
            f"  🟢 Active: `{stats.get('active_accounts', 0)}`   "
            f"🔴 Inactive: `{stats.get('inactive_accounts', 0)}`\n\n"
            f"**Tagging**\n"
            f"  Tags used: `{stats.get('tags_used', 0)}`\n\n"
            f"**Last Error**\n"
            f"  `{stats.get('last_failure', 'None')}`",
            InlineKeyboardMarkup([[InlineKeyboardButton("❌  Back", callback_data="analytics")]])
        )

    # ── Feedback messages ─────────────────────────────────────────────────────
    @staticmethod
    def groups_result(msg):
        return (
            f"{UI._hdr('📋', 'Groups Update')}\n\n{msg}",
            InlineKeyboardMarkup([
                [InlineKeyboardButton("📋  View Groups", callback_data="list_groups"),
                 InlineKeyboardButton("➕  Add More",    callback_data="add_group")],
                [InlineKeyboardButton("❌  Back",         callback_data="groups")]
            ])
        )

    @staticmethod
    def error(msg):
        return (
            f"{UI._hdr('❌', 'Error')}\n\n{msg}",
            InlineKeyboardMarkup([[InlineKeyboardButton("❌  Back", callback_data="dashboard")]])
        )

    @staticmethod
    def success(msg, back="dashboard"):
        return (
            f"{UI._hdr('✅', 'Done')}\n\n{msg}",
            InlineKeyboardMarkup([[InlineKeyboardButton("❌  Back", callback_data=back)]])
        )

    @staticmethod
    def no_accounts_dialog():
        return (
            f"{UI._hdr('⚠️', 'No Accounts')}\n\n"
            "You have no active accounts linked.\n\n"
            "Please add at least one Telegram account\n"
            "before starting a broadcast.",
            InlineKeyboardMarkup([
                [InlineKeyboardButton("➕  Add Account", callback_data="add_account")],
                [InlineKeyboardButton("❌  Back",         callback_data="dashboard")]
            ])
        )

    @staticmethod
    def cycle_notification(bid, sent, failed, interval, failed_groups=None):
        msg = (
            f"{UI._hdr('📡', 'Cycle Complete')}\n\n"
            f"Broadcast ID: `{bid}`\n"
            f"📤 Sent: `{sent}`   ❌ Failed: `{failed}`\n"
            f"⏱ Next cycle in `{interval}s`"
        )
        if failed_groups:
            msg += f"\n\n**Failed groups:**\n" + "\n".join(f"• {g}" for g in failed_groups[:5])
            if len(failed_groups) > 5:
                msg += f"\n_…and {len(failed_groups) - 5} more_"
        return msg

    @staticmethod
    def premium_required():
        return (
            f"{UI._hdr('🔒', 'Feature Locked')}\n\n"
            "This feature requires a higher tier.\n"
            "Upgrade your subscription to unlock it.",
            InlineKeyboardMarkup([
                [InlineKeyboardButton("💎  View Plans", callback_data="purchase")],
                [InlineKeyboardButton("❌  Back",        callback_data="dashboard")]
            ])
        )

    # ── main_menu kept for internal use ──────────────────────────────────────
    @staticmethod
    def main_menu():
        return UI.welcome()

# ==================== VERX LOGGER BOT ====================

class VERXLoggerBot:
    """
    Standalone logger bot (@verxloggerbot).
    Uses direct HTTPS calls to api.telegram.org via aiohttp —
    NO Pyrogram session, NO api_id/api_hash, zero conflict with
    the main @VerxAdsbot client.  Fire-and-forget; errors never
    block the broadcast engine.
    """
    DIVIDER = "─" * 30
    _BASE   = f"https://api.telegram.org/bot{LOGGER_BOT_TOKEN}"

    def __init__(self):
        self._session: Optional[aiohttp.ClientSession] = None

    # ── Lifecycle ────────────────────────────────────────────────────────────
    async def start(self):
        """Create the shared aiohttp session and verify the token with getMe."""
        try:
            self._session = aiohttp.ClientSession()
            async with self._session.get(f"{self._BASE}/getMe", timeout=aiohttp.ClientTimeout(total=10)) as r:
                data = await r.json()
                if data.get("ok"):
                    bot_name = data["result"].get("username", "?")
                    logger.info(f"VERX Logger Bot ready ✅  @{bot_name}")
                else:
                    logger.warning(f"Logger bot token check failed: {data}")
        except Exception as exc:
            logger.warning(f"Logger bot start (non-fatal): {exc}")

    async def stop(self):
        if self._session and not self._session.closed:
            await self._session.close()

    # ── Internal send helper ─────────────────────────────────────────────────
    async def _send(self, text: str, *, disable_preview: bool = True,
                    reply_markup=None):
        """
        POST sendMessage to Telegram Bot API using aiohttp.
        Uses MarkdownV2-safe Markdown (parse_mode=Markdown).
        reply_markup must be a plain dict (JSON-serialisable inline keyboard).
        """
        if not self._session or self._session.closed:
            return
        payload: dict = {
            "chat_id"                  : LOGGER_TARGET_CHAT,
            "text"                     : text,
            "parse_mode"               : "Markdown",
            "disable_web_page_preview" : disable_preview,
        }
        if reply_markup:
            payload["reply_markup"] = reply_markup
        try:
            async with self._session.post(
                f"{self._BASE}/sendMessage",
                json    = payload,
                timeout = aiohttp.ClientTimeout(total=15),
            ) as resp:
                if resp.status != 200:
                    body = await resp.text()
                    logger.debug(f"Logger sendMessage HTTP {resp.status}: {body[:200]}")
        except Exception as exc:
            logger.debug(f"Logger send error: {exc}")

    # ── Utility helpers ──────────────────────────────────────────────────────
    @staticmethod
    def _fmt_interval(seconds: int) -> str:
        """Convert seconds → human-friendly string like '1h 30m 20s'."""
        h = seconds // 3600
        m = (seconds % 3600) // 60
        s = seconds % 60
        parts = []
        if h: parts.append(f"{h}h")
        if m: parts.append(f"{m}m")
        if s or not parts: parts.append(f"{s}s")
        return " ".join(parts)

    @staticmethod
    def _group_deep_link(group_username: str, group_chat_id, message_id: int) -> str:
        """
        Build a clickable Telegram message link.
        • Public group with username  →  t.me/username/msg_id
        • Private supergroup          →  t.me/c/stripped_id/msg_id
          (Telegram expects the positive chat_id WITHOUT the leading -100)
        """
        if group_username:
            uname = group_username.lstrip("@")
            return f"https://t.me/{uname}/{message_id}"
        if group_chat_id:
            raw = str(group_chat_id)
            # Strip leading -100 for the t.me/c/ style link
            stripped = raw.lstrip("-").lstrip("0").lstrip("1").lstrip("0") if raw.startswith("-100") else raw.lstrip("-")
            if raw.startswith("-100"):
                stripped = raw[4:]          # e.g. -1001637898958 → 1637898958
            return f"https://t.me/c/{stripped}/{message_id}"
        return ""

    # ── Public log methods ───────────────────────────────────────────────────

    async def log_new_user(self, user_id: int, username: str, first_name: str,
                           last_name: str, tier: str):
        """Fires when a brand-new user runs /start."""
        now  = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        uname_str = f"@{username}" if username else "_no username_"
        full_name = " ".join(filter(None, [first_name, last_name])) or "Unknown"
        tier_badge = {"free": "⚡ Free", "premium": "👑 Premium",
                      "elite": "🎗 Elite", "owner": "🔱 Owner"}.get(tier, tier)
        await self._send(
            f"🆕 **NEW USER — VERX Logger Bot**\n"
            f"{self.DIVIDER}\n"
            f"👤 **Name:** {full_name}\n"
            f"🔗 **Username:** {uname_str}\n"
            f"🆔 **User ID:** `{user_id}`\n"
            f"🏷 **Tier:** {tier_badge}\n"
            f"🕐 **Time:** `{now}`\n"
            f"{self.DIVIDER}\n"
            f"_User has started the bot for the first time._"
        )

    async def log_returning_user(self, user_id: int, username: str,
                                 first_name: str, tier: str):
        """Fires when an existing user runs /start again."""
        now   = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        uname_str = f"@{username}" if username else "_no username_"
        tier_badge = {"free": "⚡ Free", "premium": "👑 Premium",
                      "elite": "🎗 Elite", "owner": "🔱 Owner"}.get(tier, tier)
        await self._send(
            f"🔄 **RETURNING USER**\n"
            f"{self.DIVIDER}\n"
            f"👤 **Name:** {first_name or 'Unknown'}\n"
            f"🔗 **Username:** {uname_str}\n"
            f"🆔 **User ID:** `{user_id}`\n"
            f"🏷 **Tier:** {tier_badge}\n"
            f"🕐 **Time:** `{now}`\n"
            f"{self.DIVIDER}"
        )

    async def log_ads_started(self, user_id: int, username: str,
                              broadcast_count: int, groups_count: int,
                              interval_seconds: int, tier: str):
        """Fires when a user starts their ad broadcasts."""
        now    = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        uname_str = f"@{username}" if username else f"UID:{user_id}"
        iv_str = self._fmt_interval(interval_seconds)
        tier_badge = {"free": "⚡ Free", "premium": "👑 Premium",
                      "elite": "🎗 Elite", "owner": "🔱 Owner"}.get(tier, tier)
        await self._send(
            f"🚀 **ADS STARTED**\n"
            f"{self.DIVIDER}\n"
            f"👤 **User:** {uname_str}\n"
            f"🆔 **User ID:** `{user_id}`\n"
            f"🏷 **Tier:** {tier_badge}\n"
            f"📡 **Broadcasts:** `{broadcast_count}`\n"
            f"👥 **Target Groups:** `{groups_count}`\n"
            f"⏱ **Interval:** `{iv_str}` (every {iv_str})\n"
            f"🕐 **Started At:** `{now}`\n"
            f"{self.DIVIDER}\n"
            f"_Ads are now broadcasting to {groups_count} group(s) every {iv_str}._"
        )

    async def log_ads_stopped(self, user_id: int, username: str,
                              stopped_count: int):
        """Fires when a user stops their ads."""
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        uname_str = f"@{username}" if username else f"UID:{user_id}"
        await self._send(
            f"🛑 **ADS STOPPED**\n"
            f"{self.DIVIDER}\n"
            f"👤 **User:** {uname_str}\n"
            f"🆔 **User ID:** `{user_id}`\n"
            f"🔢 **Broadcasts stopped:** `{stopped_count}`\n"
            f"🕐 **Time:** `{now}`\n"
            f"{self.DIVIDER}"
        )

    async def log_message_sent(self, user_id: int, username: str,
                               group_title: str, group_username: str,
                               group_chat_id, message_id: int,
                               account_phone: str, broadcast_id: int):
        """
        Fires for every successfully sent ad message.
        Includes a deep-link button that opens the exact message in the group.
        """
        now      = datetime.now().strftime("%H:%M:%S")
        uname_str = f"@{username}" if username else f"UID:{user_id}"
        gname    = group_title or group_username or str(group_chat_id)
        deep_link = self._group_deep_link(group_username, group_chat_id, message_id)

        text = (
            f"📨 **AD SENT**\n"
            f"{self.DIVIDER}\n"
            f"👤 **User:** {uname_str}\n"
            f"📱 **Account:** `{account_phone}`\n"
            f"👥 **Group:** {gname}\n"
            f"📢 **Broadcast #:** `{broadcast_id}`\n"
            f"🕐 **Time:** `{now}`\n"
            f"{self.DIVIDER}"
        )
        markup = None
        if deep_link:
            markup = {
                "inline_keyboard": [[
                    {"text": "🔗 Open Message in Group", "url": deep_link}
                ]]
            }
        await self._send(text, disable_preview=True, reply_markup=markup)

    async def log_account_banned(self, user_id: int, username: str,
                                 phone: str, reason: str):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        uname_str = f"@{username}" if username else f"UID:{user_id}"
        await self._send(
            f"⛔ **ACCOUNT BANNED / RESTRICTED**\n"
            f"{self.DIVIDER}\n"
            f"👤 **Owner:** {uname_str}\n"
            f"📱 **Phone:** `{phone}`\n"
            f"❗ **Reason:** {reason}\n"
            f"🕐 **Time:** `{now}`\n"
            f"{self.DIVIDER}"
        )

    async def log_group_auto_removed(self, user_id: int, username: str,
                                     group_title: str, reason: str):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        uname_str = f"@{username}" if username else f"UID:{user_id}"
        await self._send(
            f"🚫 **GROUP AUTO-REMOVED**\n"
            f"{self.DIVIDER}\n"
            f"👤 **Owner:** {uname_str}\n"
            f"👥 **Group:** {group_title}\n"
            f"❗ **Reason:** {reason}\n"
            f"🕐 **Time:** `{now}`\n"
            f"{self.DIVIDER}"
        )

    async def log_tier_granted(self, target_user_id: int, tier: str, days: int,
                               granted_by: int):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        tier_badge = {"premium": "👑 Premium", "elite": "🎗 Elite"}.get(tier, tier)
        await self._send(
            f"🎁 **TIER GRANTED**\n"
            f"{self.DIVIDER}\n"
            f"🎯 **To User ID:** `{target_user_id}`\n"
            f"🏷 **Tier:** {tier_badge}\n"
            f"📅 **Duration:** `{days}` day(s)\n"
            f"👑 **Granted by:** `{granted_by}`\n"
            f"🕐 **Time:** `{now}`\n"
            f"{self.DIVIDER}"
        )

    async def log_cycle_complete(self, user_id: int, username: str,
                                 broadcast_id: int, sent: int, failed: int,
                                 interval_seconds: int):
        """Summary log after every full broadcast cycle."""
        now    = datetime.now().strftime("%H:%M:%S")
        uname_str = f"@{username}" if username else f"UID:{user_id}"
        iv_str = self._fmt_interval(interval_seconds)
        success_rate = f"{(sent / (sent+failed) * 100):.0f}%" if (sent+failed) > 0 else "N/A"
        await self._send(
            f"✅ **BROADCAST CYCLE DONE**\n"
            f"{self.DIVIDER}\n"
            f"👤 **User:** {uname_str}\n"
            f"📢 **Broadcast #:** `{broadcast_id}`\n"
            f"📤 **Sent:** `{sent}`  •  ❌ **Failed:** `{failed}`\n"
            f"📊 **Success Rate:** `{success_rate}`\n"
            f"⏱ **Next cycle in:** `{iv_str}`\n"
            f"🕐 **Time:** `{now}`\n"
            f"{self.DIVIDER}"
        )


# ==================== MAIN BOT ====================

class VerxAdsBot:
    def __init__(self):
        self.app = PyroClient("verx_ads", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH, in_memory=True)
        self.db = DatabaseManager()
        self.enc = EncryptionManager()
        self.groq = GroqManager()
        self.accounts = AccountManager(self.db, self.enc)
        self.tags = TagManager(self.db)
        self.broadcasts = BroadcastManager(self.db, self.accounts, self.tags, self)
        self.autoreply = AutoReplyManager(self.db, self.accounts, self.groq)
        self.verx_logger = VERXLoggerBot()    # ← VERX Logger Bot instance

        self.states = {}          # user_id -> state dict
        self.temp = {}            # user_id -> {client, phone} for OTP
        self.intervals = {}       # user_id -> current interval
        self._list_pages = {}     # user_id -> page number for lists
        self._pending_bio = {}    # user_id -> pending bio for confirmation

        # ── Speed caches ──────────────────────────────────────────────────────
        # Channel membership: {user_id: (result_bool, timestamp)}
        # TTL = 5 min — avoids 2 live Telegram API calls on every button press
        self._channel_cache: dict = {}
        self._channel_cache_ttl: float = 300.0

        # Tier cache: {user_id: (tier, limits, time_left, timestamp)}
        # TTL = 30 s — avoids repeated DB reads; invalidated on tier change
        self._tier_cache: dict = {}
        self._tier_cache_ttl: float = 30.0

        # Locked-setting cache: (locked_bool, timestamp)  TTL = 10 s
        self._locked_cache = None
        self._locked_cache_ttl: float = 10.0
        # ─────────────────────────────────────────────────────────────────────

        self._register_handlers()

    def _register_handlers(self):
        @self.app.on_message(filters.command("start"))
        async def start_cmd(client, message):
            if not await self._check_required_channels(message.from_user.id):
                buttons = InlineKeyboardMarkup([
                    [InlineKeyboardButton("📢 Join", url=REQUIRED_CHANNELS[0]['link'])],
                    [InlineKeyboardButton("💬 Join", url=REQUIRED_CHANNELS[1]['link'])],
                    [InlineKeyboardButton("🔄 I've Joined – Verify", callback_data="check_joined")]
                ])
                await message.reply_text(
                    "**╰_╯ Verx Ads Bot**\n\n"
                    "━━━━━━━━━━━━━━━━━━━━━\n"
                    "⚠️ **Access Restricted**\n\n"
                    "You must join our channels to use this bot.\n"
                    "After joining both, press **Verify** below.",
                    reply_markup=buttons,
                    disable_web_page_preview=True
                )
                return

            u = message.from_user.id
            # Check if user has already started the bot before
            already_registered = bool(self.db.fetch_one("SELECT 1 FROM users WHERE user_id=?", (u,)))

            if not already_registered:
                # First time — register the user and show full welcome
                self.db.execute(
                    "INSERT INTO users (user_id, username, first_name, last_name, joined_date) VALUES (?,?,?,?,?)",
                    (u, message.from_user.username, message.from_user.first_name,
                     message.from_user.last_name, datetime.now().isoformat())
                )
                self._ensure_user(u)
                row = self.db.fetch_one("SELECT premium_until FROM users WHERE user_id=?", (u,))
                premium_until = row[0] if row else None
                tier = Tier.get_tier(u, premium_until)
                if tier == Tier.FREE:
                    await self.accounts.enforce_free_tier_profile(u)
                # ── Logger: new user ──
                asyncio.create_task(self.verx_logger.log_new_user(
                    user_id    = u,
                    username   = message.from_user.username or "",
                    first_name = message.from_user.first_name or "",
                    last_name  = message.from_user.last_name or "",
                    tier       = tier,
                ))
                t, b = UI.welcome()
                await message.reply_text(t, reply_markup=b, parse_mode=ParseMode.MARKDOWN)
            else:
                # Returning user — skip welcome spam, send a single compact reply with dashboard button
                self._ensure_user(u)
                row = self.db.fetch_one("SELECT premium_until FROM users WHERE user_id=?", (u,))
                premium_until = row[0] if row else None
                tier = Tier.get_tier(u, premium_until)
                if tier == Tier.FREE:
                    await self.accounts.enforce_free_tier_profile(u)
                # ── Logger: returning user ──
                asyncio.create_task(self.verx_logger.log_returning_user(
                    user_id    = u,
                    username   = message.from_user.username or "",
                    first_name = message.from_user.first_name or "",
                    tier       = tier,
                ))
                await message.reply_text(
                    "👋 **Welcome back!**\n\nOpen your dashboard to manage ads.",
                    reply_markup=InlineKeyboardMarkup([[
                        InlineKeyboardButton("📊  Open Dashboard", callback_data="dashboard")
                    ]]),
                    parse_mode=ParseMode.MARKDOWN
                )

        @self.app.on_message(filters.command(["dashboard", "status", "mystats", "myplan", "help"]))
        async def shortcut_cmds(client, message):
            u = message.from_user.id
            if not await self._check_required_channels(u): return
            self._ensure_user(u)
            cmd = message.command[0]
            if cmd == "dashboard":
                tier, limits, days_left = await self._get_tier_and_limits(u)
                running = self.db.fetch_one("SELECT COUNT(*) FROM broadcasts WHERE user_id=? AND is_running=1", (u,))[0] or 0
                groups_cnt = self.db.fetch_one("SELECT COUNT(*) FROM target_groups WHERE user_id=? AND is_active=1", (u,))[0] or 0
                accs_cnt = self.db.fetch_one("SELECT COUNT(*) FROM accounts WHERE user_id=? AND is_active=1", (u,))[0] or 0
                msgs_cnt = self.db.fetch_one("SELECT COUNT(*) FROM user_messages WHERE user_id=? AND is_active=1", (u,))[0] or 0
                t, b = UI.dashboard(tier, limits, running, groups_cnt, accs_cnt, msgs_cnt, days_left)
                await message.reply_text(t, reply_markup=b, parse_mode=ParseMode.MARKDOWN)
            elif cmd == "help":
                t, b = UI.help_menu()
                await message.reply_text(t, reply_markup=b, parse_mode=ParseMode.MARKDOWN)
            elif cmd in ("status", "mystats"):
                row = self.db.fetch_one("SELECT SUM(messages_sent), SUM(messages_failed) FROM broadcasts WHERE user_id=?", (u,))
                sent = row[0] or 0 if row else 0
                failed = row[1] or 0 if row else 0
                running = self.db.fetch_one("SELECT COUNT(*) FROM broadcasts WHERE user_id=? AND is_running=1", (u,))[0] or 0
                await message.reply_text(
                    f"{UI._hdr('📊', 'Your Stats')}\n\n"
                    f"📤 Sent: `{sent}`  •  ❌ Failed: `{failed}`  •  📡 Active: `{running}`",
                    parse_mode=ParseMode.MARKDOWN
                )
            elif cmd == "myplan":
                tier, limits, days_left = await self._get_tier_and_limits(u)
                row = self.db.fetch_one("SELECT premium_until FROM users WHERE user_id=?", (u,))
                premium_until = row[0] if row else None
                badge = {"free": "⚡ Free", "premium": "👑 Premium", "elite": "🎗 Elite"}.get(tier, tier)
                expiry = ""
                if days_left and premium_until:
                    iso = premium_until[6:] if premium_until.startswith("elite:") else premium_until
                    diff = datetime.fromisoformat(iso) - datetime.now()
                    total_mins = int(diff.total_seconds() // 60)
                    hrs = total_mins // 60; mins = total_mins % 60
                    expiry = f"\nExpires: `{iso[:10]}`  ({days_left}d {hrs}h {mins}m)"
                await message.reply_text(
                    f"{UI._hdr('💎', 'My Subscription')}\n\nPlan: **{badge}**{expiry}\n\n"
                    f"Groups: `{limits['max_groups']}`  •  Accounts: `{limits['max_accounts']}`  •  Messages: `{limits['max_messages']}`",
                    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("💎  View Plans", callback_data="purchase")]]),
                    parse_mode=ParseMode.MARKDOWN
                )

        @self.app.on_message(filters.command("restart") & filters.user(OWNER_IDS[0]))
        async def restart_cmd(client, message):
            await message.reply_text("🔄 Resetting all data...")
            for user_id in set(b[0] for b in self.db.fetch_all("SELECT DISTINCT user_id FROM broadcasts WHERE is_running=1")):
                await self.broadcasts.stop_all(user_id)
            await self.accounts.disconnect_all()
            self.states.clear()
            self.temp.clear()
            self.intervals.clear()
            self._list_pages.clear()
            self._pending_bio.clear()
            self.db.reset_database()
            await message.reply_text("✓ Database reset.")

        @self.app.on_message(filters.command("lock") & filters.user(OWNER_IDS))
        async def lock_cmd(client, message):
            self.db.execute("UPDATE settings SET value='true' WHERE key='locked'")
            stopped = await self.broadcasts.stop_all_non_premium()
            await message.reply_text(f"🔒 Locked. Stopped {stopped} broadcasts.")

        @self.app.on_message(filters.command("unlock") & filters.user(OWNER_IDS))
        async def unlock_cmd(client, message):
            self.db.execute("UPDATE settings SET value='false' WHERE key='locked'")
            await message.reply_text("🔓 Unlocked.")

        @self.app.on_message(filters.command("givepremium") & filters.user(OWNER_IDS))
        async def give_premium_cmd(client, message):
            parts = message.text.split()
            if len(parts) != 3:
                await message.reply_text("Usage: /givepremium <user_id> <days>")
                return
            try:
                user_id = int(parts[1])
                days = int(parts[2])
                if days <= 0:
                    raise ValueError
            except:
                await message.reply_text("Invalid user ID or days.")
                return
            until = (datetime.now() + timedelta(days=days)).isoformat()
            self.db.execute("UPDATE users SET premium_until=? WHERE user_id=?", (until, user_id))
            await message.reply_text(f"✓ Given {days} days premium to user {user_id}.")

        @self.app.on_message(filters.command("removepremium") & filters.user(OWNER_IDS))
        async def remove_premium_cmd(client, message):
            parts = message.text.split()
            if len(parts) != 2:
                await message.reply_text("Usage: /removepremium <user_id>")
                return
            try:
                user_id = int(parts[1])
            except:
                await message.reply_text("Invalid user ID.")
                return
            self.db.execute("UPDATE users SET premium_until=NULL WHERE user_id=?", (user_id,))
            await message.reply_text(f"✓ Removed premium from user {user_id}.")

        @self.app.on_message(filters.command("premiumstats") & filters.user(OWNER_IDS))
        async def premium_stats_cmd(client, message):
            parts = message.text.split()
            if len(parts) != 2:
                await message.reply_text("Usage: /premiumstats <user_id>")
                return
            try:
                user_id = int(parts[1])
            except:
                await message.reply_text("Invalid user ID.")
                return
            row = self.db.fetch_one("SELECT premium_until FROM users WHERE user_id=?", (user_id,))
            if not row:
                await message.reply_text("User not found.")
                return
            until = row[0]
            if until:
                try:
                    if until.startswith("elite:"):
                        iso = until[6:]
                        tier_label = "Elite"
                    else:
                        iso = until
                        tier_label = "Premium"
                    days_left = (datetime.fromisoformat(iso) - datetime.now()).days
                    await message.reply_text(
                        f"User {user_id} — **{tier_label}** until {iso[:10]} ({days_left} days left).",
                        parse_mode=ParseMode.MARKDOWN)
                except Exception as e:
                    await message.reply_text(f"User {user_id} — has subscription but parse failed: {e}")
            else:
                await message.reply_text(f"User {user_id} has no premium.")

        @self.app.on_message(filters.text & filters.private & ~filters.command(["start", "dashboard", "status", "mystats", "myplan", "help", "restart", "lock", "unlock", "givepremium", "removepremium", "premiumstats"]))
        async def text_handler(client, message):
            if not await self._check_required_channels(message.from_user.id):
                buttons = InlineKeyboardMarkup([
                    [InlineKeyboardButton("📢 Join", url=REQUIRED_CHANNELS[0]['link'])],
                    [InlineKeyboardButton("📢 Join", url=REQUIRED_CHANNELS[1]['link'])],
                    [InlineKeyboardButton("🔄 Verify", callback_data="check_joined")]
                ])
                await message.reply_text(
                    "**✗ Access Denied**\n\n"
                    "You left a required channel.\n"
                    "Rejoin and press Verify.",
                    reply_markup=buttons,
                    disable_web_page_preview=True
                )
                return
            await self._handle_input(message)

        @self.app.on_callback_query()
        async def callback_handler(client, callback_query):
            if not await self._check_required_channels(callback_query.from_user.id):
                await callback_query.answer("Join our channels first!", show_alert=True)
                return
            await self._handle_callback(callback_query)

    async def _check_required_channels(self, user_id: int) -> bool:
        """Check channel membership with a 5-minute in-memory cache.
        Without caching this fires 2 live Telegram API calls on every button press.
        """
        now = time.time()
        cached = self._channel_cache.get(user_id)
        if cached is not None:
            result, ts = cached
            if now - ts < self._channel_cache_ttl:
                return result   # ← fast path: no network call at all

        # Cache miss or expired — do the real check
        try:
            for channel in REQUIRED_CHANNELS:
                try:
                    await self.app.get_chat_member(channel["username"], user_id)
                except UserNotParticipant:
                    self._channel_cache[user_id] = (False, now)
                    return False
                except Exception as e:
                    logger.error(f"Channel check error: {e}")
                    self._channel_cache[user_id] = (False, now)
                    return False
            self._channel_cache[user_id] = (True, now)
            return True
        except Exception:
            return False

    def _invalidate_channel_cache(self, user_id: int):
        """Call this when user verifies they joined, so the next press re-checks live."""
        self._channel_cache.pop(user_id, None)

    def _ensure_user(self, user_id: int):
        """Insert a bare user row if not present, so subsequent queries never return None."""
        if not self.db.fetch_one("SELECT 1 FROM users WHERE user_id=?", (user_id,)):
            self.db.execute(
                "INSERT OR IGNORE INTO users (user_id, joined_date) VALUES (?,?)",
                (user_id, datetime.now().isoformat())
            )

    async def _get_tier_and_limits(self, user_id: int) -> Tuple[str, dict, Optional[str]]:
        """Cached tier lookup — avoids a DB round-trip on every button press.
        TTL = 30 s; call _invalidate_tier_cache(user_id) whenever tier changes.
        """
        now = time.time()
        cached = self._tier_cache.get(user_id)
        if cached is not None:
            tier, limits, time_left, ts = cached
            if now - ts < self._tier_cache_ttl:
                return tier, limits, time_left   # ← fast path

        # Cache miss — real DB read
        self._ensure_user(user_id)
        row = self.db.fetch_one("SELECT premium_until FROM users WHERE user_id=?", (user_id,))
        premium_until = row[0] if row else None
        tier = Tier.get_tier(user_id, premium_until)
        limits = Tier.get_limits(tier)
        time_left = None
        if premium_until and tier not in (Tier.FREE, "owner"):
            try:
                iso = premium_until[6:] if premium_until.startswith("elite:") else premium_until
                time_left = time_remaining(iso)
            except Exception:
                pass
        self._tier_cache[user_id] = (tier, limits, time_left, now)
        return tier, limits, time_left

    def _invalidate_tier_cache(self, user_id: int):
        """Invalidate tier cache when premium is granted/removed."""
        self._tier_cache.pop(user_id, None)

    def _get_locked(self) -> bool:
        """Cached locked-setting read. TTL = 10 s."""
        now = time.time()
        if self._locked_cache is not None:
            locked, ts = self._locked_cache
            if now - ts < self._locked_cache_ttl:
                return locked
        locked = self.db.fetch_one("SELECT value FROM settings WHERE key='locked'")[0] == 'true'
        self._locked_cache = (locked, now)
        return locked

    def _invalidate_locked_cache(self):
        self._locked_cache = None

    async def _check_access(self, user_id: int) -> bool:
        if user_id in OWNER_IDS:
            return True
        if not self._get_locked():
            return True
        tier, __, __ = await self._get_tier_and_limits(user_id)
        return tier != Tier.FREE

    async def _check_limits(self, user_id: int, action: str, value: int = 1) -> Tuple[bool, str]:
        """Check if user can perform action based on tier limits."""
        tier, limits, _ = await self._get_tier_and_limits(user_id)
        if action == "add_account":
            count = self.db.fetch_one("SELECT COUNT(*) FROM accounts WHERE user_id=?", (user_id,))[0]
            if count + value > limits["max_accounts"]:
                return False, f"Your tier ({tier}) allows max {limits['max_accounts']} accounts."
        elif action == "add_group":
            count = self.db.fetch_one("SELECT COUNT(*) FROM target_groups WHERE user_id=?", (user_id,))[0]
            if count + value > limits["max_groups"]:
                return False, f"Your tier ({tier}) allows max {limits['max_groups']} groups."
        elif action == "add_message":
            count = self.db.fetch_one("SELECT COUNT(*) FROM user_messages WHERE user_id=?", (user_id,))[0]
            if count + value > limits["max_messages"]:
                return False, f"Your tier ({tier}) allows max {limits['max_messages']} messages."
        return True, "OK"

    async def safe_edit(self, message, text, reply_markup=None, parse_mode=ParseMode.MARKDOWN):
        try:
            if message.text == text and message.reply_markup == reply_markup:
                return
            await message.edit_text(text, reply_markup=reply_markup, parse_mode=parse_mode)
        except Exception as e:
            if "MESSAGE_NOT_MODIFIED" not in str(e):
                logger.error(f"Edit error: {e}")

    # ---------- Input Handling ----------
    async def _handle_input(self, m):
        u = m.from_user.id
        if not await self._check_access(u):
            t, b = UI.premium_required()
            await m.reply_text(t, reply_markup=b, parse_mode=ParseMode.MARKDOWN)
            return

        if u not in self.states:
            # If not in a state, ignore random text
            return

        state = self.states[u]

        if state["state"] == "phone":
            await self._handle_phone(m)
        elif state["state"] == "otp":
            await self._handle_otp(m)
        elif state["state"] == "2fa":
            await self._handle_2fa(m)
        elif state["state"] == "new_message":
            # Check message limit
            ok, msg = await self._check_limits(u, "add_message")
            if not ok:
                t, b = UI.error(msg)
                await m.reply_text(t, reply_markup=b, parse_mode=ParseMode.MARKDOWN)
                del self.states[u]
                return
            self.db.execute('''INSERT INTO user_messages
                (user_id, message_text, added_date, is_active)
                VALUES (?,?,?,1)''', (u, m.text.strip(), datetime.now().isoformat()))
            del self.states[u]
            t, b = UI.success("Message added.")
            await m.reply_text(t, reply_markup=b, parse_mode=ParseMode.MARKDOWN)
        elif state["state"] == "interval":
            tier, limits, _ = await self._get_tier_and_limits(u)
            if not limits["interval_custom"]:
                # Should never happen since only Elite can enter this state, but guard it
                t, b = UI.error("Custom interval requires Elite tier. Use the preset buttons.")
                await m.reply_text(t, reply_markup=b, parse_mode=ParseMode.MARKDOWN)
                del self.states[u]
                return
            raw = m.text.strip()
            try:
                i = int(raw)
                if i <= 0:
                    raise ValueError("must be positive")
            except ValueError:
                await m.reply_text(
                    "❌ **Invalid value.** Please send a plain number in seconds.\n"
                    "Example: `600` for 10 minutes.\n\n"
                    "_(Send /start if you want to cancel)_",
                    parse_mode=ParseMode.MARKDOWN
                )
                # Keep state alive so user can retry
                return
            floored = max(i, limits["interval_min"])
            self.intervals[u] = floored
            await self.broadcasts.update_interval_for_user(u, floored)
            del self.states[u]
            label = f"{floored // 3600}h {(floored % 3600) // 60}m" if floored >= 3600 else f"{floored // 60}m {floored % 60}s"
            note = f"\n_(Raised to {floored}s — tier minimum)_" if floored != i else ""
            t, b = UI.success(f"Interval set to `{floored}s` ({label}).{note}")
            await m.reply_text(t, reply_markup=b, parse_mode=ParseMode.MARKDOWN)
        elif state["state"] == "bio":
            # Check if set_bio allowed
            tier, limits, _ = await self._get_tier_and_limits(u)
            if not limits["set_bio"]:
                t, b = UI.error("Bio setting not allowed in your tier.")
                await m.reply_text(t, reply_markup=b, parse_mode=ParseMode.MARKDOWN)
                del self.states[u]
                return
            new_bio = m.text.strip()
            if len(new_bio) > 70:
                t, b = UI.error("Bio too long (max 70 chars).")
                await m.reply_text(t, reply_markup=b, parse_mode=ParseMode.MARKDOWN)
                return
            self._pending_bio[u] = new_bio
            t, b = UI.confirm_bio(new_bio)
            await m.reply_text(t, reply_markup=b, parse_mode=ParseMode.MARKDOWN)
            del self.states[u]
        elif state["state"] == "set_global_bio":
            new_bio = m.text.strip()
            if len(new_bio) > 70:
                await m.reply_text("❌ Bio too long (max 70 chars).", parse_mode=ParseMode.MARKDOWN)
                return
            self.db.execute("UPDATE settings SET value=? WHERE key='global_bio'", (new_bio,))
            del self.states[u]
            t, b = UI.success("Global free-tier bio updated. Pushing to all free accounts in background…")
            await m.reply_text(t, reply_markup=b, parse_mode=ParseMode.MARKDOWN)
            # Push new bio+name to all free-tier accounts safely in the background
            asyncio.create_task(self.accounts.enforce_all_free_users())

        elif state["state"] == "give_premium":
            parts = m.text.strip().split()
            if len(parts) != 2:
                await m.reply_text("❌ Format: `<user_id> <days>`", parse_mode=ParseMode.MARKDOWN)
                return
            try:
                target_id = int(parts[0]); days = int(parts[1])
                if days <= 0: raise ValueError
            except:
                await m.reply_text("❌ Invalid user ID or days.", parse_mode=ParseMode.MARKDOWN)
                return
            until = (datetime.now() + timedelta(days=days)).isoformat()
            self.db.execute("UPDATE users SET premium_until=? WHERE user_id=?", (until, target_id))
            self._invalidate_tier_cache(target_id)
            del self.states[u]
            t, b = UI.success(f"Gave **👑 Premium** to `{target_id}` for **{days} days**.")
            await m.reply_text(t, reply_markup=b, parse_mode=ParseMode.MARKDOWN)
            asyncio.create_task(self.notify_tier_granted(target_id, "premium", days, granted_by=u))

        elif state["state"] == "give_elite":
            parts = m.text.strip().split()
            if len(parts) != 2:
                await m.reply_text("❌ Format: `<user_id> <days>`", parse_mode=ParseMode.MARKDOWN)
                return
            try:
                target_id = int(parts[0]); days = int(parts[1])
                if days <= 0: raise ValueError
            except:
                await m.reply_text("❌ Invalid user ID or days.", parse_mode=ParseMode.MARKDOWN)
                return
            until = "elite:" + (datetime.now() + timedelta(days=days)).isoformat()
            self.db.execute("UPDATE users SET premium_until=? WHERE user_id=?", (until, target_id))
            self._invalidate_tier_cache(target_id)
            del self.states[u]
            t, b = UI.success(f"Gave **🎗 Elite** to `{target_id}` for **{days} days**.")
            await m.reply_text(t, reply_markup=b, parse_mode=ParseMode.MARKDOWN)
            asyncio.create_task(self.notify_tier_granted(target_id, "elite", days, granted_by=u))

        elif state["state"] == "remove_premium":
            try:
                target_id = int(m.text.strip())
            except:
                await m.reply_text("❌ Invalid user ID.", parse_mode=ParseMode.MARKDOWN)
                return
            self.db.execute("UPDATE users SET premium_until=NULL WHERE user_id=?", (target_id,))
            self._invalidate_tier_cache(target_id)
            del self.states[u]
            t, b = UI.success(f"Removed tier from `{target_id}`.")
            await m.reply_text(t, reply_markup=b, parse_mode=ParseMode.MARKDOWN)

        elif state["state"] == "check_premium":
            try:
                target_id = int(m.text.strip())
            except:
                await m.reply_text("❌ Invalid user ID.", parse_mode=ParseMode.MARKDOWN)
                return
            row = self.db.fetch_one("SELECT premium_until FROM users WHERE user_id=?", (target_id,))
            del self.states[u]
            if not row:
                await m.reply_text(f"User `{target_id}` not found.", parse_mode=ParseMode.MARKDOWN)
                return
            until_raw = row[0]
            if not until_raw:
                await m.reply_text(f"User `{target_id}` — **⚡ Free** tier.", parse_mode=ParseMode.MARKDOWN)
            elif until_raw.startswith("elite:"):
                iso = until_raw[6:]
                try:
                    days_left = (datetime.fromisoformat(iso) - datetime.now()).days
                    await m.reply_text(f"User `{target_id}` — **🎗 Elite**\nExpires: `{iso[:10]}` ({days_left}d left)", parse_mode=ParseMode.MARKDOWN)
                except:
                    await m.reply_text(f"User `{target_id}` — **🎗 Elite**", parse_mode=ParseMode.MARKDOWN)
            else:
                try:
                    days_left = (datetime.fromisoformat(until_raw) - datetime.now()).days
                    await m.reply_text(f"User `{target_id}` — **👑 Premium**\nExpires: `{until_raw[:10]}` ({days_left}d left)", parse_mode=ParseMode.MARKDOWN)
                except:
                    await m.reply_text(f"User `{target_id}` — **👑 Premium**", parse_mode=ParseMode.MARKDOWN)

        elif state["state"] == "groups":
            raw_text = m.text.strip()
            added = 0
            skipped = 0
            folder_expanded = 0

            # Get a client for entity resolution (optional, graceful fallback)
            acc = self.db.fetch_one("SELECT account_id FROM accounts WHERE user_id=? LIMIT 1", (u,))
            client = await self.accounts.get_client(acc[0]) if acc else None

            # ── Pre-process: extract all parseable URLs from the blob ────────
            # Split on newlines, handle "prefix:\nurl" patterns
            raw_lines = raw_text.split('\n')
            pending = []
            for line in raw_lines:
                line = line.strip()
                if not line:
                    continue
                # Skip pure-text lines that have no URL and aren't @username/ID
                has_tme  = 't.me/' in line
                has_at   = line.startswith('@')
                has_id   = bool(re.match(r'^-?\d{5,}$', line))
                if not (has_tme or has_at or has_id):
                    continue  # watermark/label/empty line — skip
                parsed = self._parse_group_line(line)
                if parsed[0] is not None:
                    pending.append(parsed)

            if not pending:
                del self.states[u]
                t, b = UI.error("No valid group links found.\nSend t.me/... links or @usernames.")
                await m.reply_text(t, reply_markup=b, parse_mode=ParseMode.MARKDOWN)
                return

            tier_grp, limits_grp, _ = await self._get_tier_and_limits(u)
            skipped_dupe = 0

            for (link, username, title) in pending:
                # ── Folder link ────────────────────────────────────────────
                if link and 'addlist' in link:
                    if client:
                        folder_groups = await resolve_folder_link(client, link)
                        for (chat, g_link, g_username, g_title) in folder_groups:
                            ok, msg_lim = await self._check_limits(u, "add_group", 1)
                            if not ok:
                                break
                            exists = self.db.fetch_one(
                                "SELECT 1 FROM target_groups WHERE user_id=? AND (group_link=? OR (group_username IS NOT NULL AND group_username=?))",
                                (u, g_link, g_username))
                            if exists:
                                skipped_dupe += 1
                                continue
                            try:
                                self.db.execute(
                                    '''INSERT INTO target_groups
                                    (user_id, group_username, group_title, group_link, added_date, is_active, joined)
                                    VALUES (?,?,?,?,?,1,0)''',
                                    (u, g_username, g_title, g_link, datetime.now().isoformat()))
                                added += 1
                                folder_expanded += 1
                            except Exception as e:
                                logger.error(f"Folder group insert error: {e}")
                                skipped += 1
                    else:
                        exists = self.db.fetch_one(
                            "SELECT 1 FROM target_groups WHERE user_id=? AND group_link=?", (u, link))
                        if exists:
                            skipped_dupe += 1
                        else:
                            try:
                                self.db.execute(
                                    '''INSERT INTO target_groups
                                    (user_id, group_username, group_title, group_link, added_date, is_active, joined)
                                    VALUES (?,?,?,?,?,1,0)''',
                                    (u, None, title, link, datetime.now().isoformat()))
                                added += 1
                            except Exception as e:
                                logger.error(f"Folder link insert error: {e}")
                                skipped += 1
                    continue

                # ── Regular group ──────────────────────────────────────────
                ok, msg_lim = await self._check_limits(u, "add_group", 1)
                if not ok:
                    t, b = UI.error(msg_lim)
                    await m.reply_text(t, reply_markup=b, parse_mode=ParseMode.MARKDOWN)
                    del self.states[u]
                    return

                # Duplicate check
                exists = self.db.fetch_one(
                    "SELECT 1 FROM target_groups WHERE user_id=? AND (group_link=? OR (group_username IS NOT NULL AND group_username=?))",
                    (u, link, username))
                if exists:
                    skipped_dupe += 1
                    continue

                if client and username:
                    entity = await resolve_group_identifier(client, username)
                    if entity and hasattr(entity, 'title'):
                        title = entity.title
                        resolved_uname = getattr(entity, 'username', None)
                        if resolved_uname:
                            username = resolved_uname
                            link = f"https://t.me/{username}"
                        # Re-check with resolved username
                        exists2 = self.db.fetch_one(
                            "SELECT 1 FROM target_groups WHERE user_id=? AND group_username=?", (u, username))
                        if exists2:
                            skipped_dupe += 1
                            continue

                try:
                    self.db.execute(
                        '''INSERT INTO target_groups
                        (user_id, group_username, group_title, group_link, added_date, is_active, joined)
                        VALUES (?,?,?,?,?,1,0)''',
                        (u, username, title, link, datetime.now().isoformat()))
                    added += 1
                except Exception as e:
                    logger.error(f"Group add error: {e}")
                    skipped += 1

            del self.states[u]
            total_now = self.db.fetch_one("SELECT COUNT(*) FROM target_groups WHERE user_id=?", (u,))[0] or 0
            max_grp = limits_grp["max_groups"]
            remaining = max_grp - total_now
            parts_msg = [f"**{added}** added  •  **{total_now}/{max_grp}** total"]
            if folder_expanded:
                parts_msg.append(f"📁 **{folder_expanded}** from folder")
            if skipped_dupe:
                parts_msg.append(f"🔁 **{skipped_dupe}** duplicate(s) skipped")
            if skipped:
                parts_msg.append(f"⚠️ **{skipped}** invalid")
            if tier_grp == Tier.FREE and remaining <= 1:
                parts_msg.append(f"\n⚡ Free tier: **{remaining}** slot(s) left of {max_grp}")
            if tier_grp == Tier.FREE and remaining == 0:
                parts_msg.append("Upgrade to **Premium** for up to 10 groups!")
            t, b = UI.groups_result("\n".join(parts_msg))
            await m.reply_text(t, reply_markup=b, parse_mode=ParseMode.MARKDOWN)

    def _parse_group_line(self, line):
        """Parse a single line into (link, username, title).
        Handles:
          - t.me/addlist/... folder links
          - t.me/joinchat/... and t.me/+... private invite links
          - https://t.me/username  public group links
          - @username  bare @-prefixed usernames
          - numeric chat IDs  (-100...)
          Strips ad-forwarded prefixes like "GAMER •via @Bot: https://t.me/..."
        """
        # ── 1. Strip ad-watermark prefixes ────────────────────────────────────
        # ── 1. Strip ad-watermark prefixes ────────────────────────────────────
        # Pattern: any text ending with a colon before a URL
        stripped = re.sub(r'^[^\n]*?(?:via\s+@\w+|•[^\n]*|@\w+\s*:)[^\n]*\n?', '', line, flags=re.IGNORECASE).strip()
        if stripped:
            line = stripped

        # ── 2. Try to find a t.me URL anywhere in the line ───────────────────
        tme_match = re.search(
            r'(?:https?://)?t\.me/(addlist/[A-Za-z0-9_\-]+|joinchat/[A-Za-z0-9_\-+]+|\+[A-Za-z0-9_\-]+|[A-Za-z][A-Za-z0-9_]{3,})',
            line
        )
        if tme_match:
            path = tme_match.group(1)
            full_url = f"https://t.me/{path}"
            if path.startswith('addlist/'):
                return full_url, None, f"Folder: {path.split('/')[-1]}"
            elif path.startswith('joinchat/') or path.startswith('+'):
                return full_url, None, line.strip()
            else:
                username = path.split('/')[0].split('?')[0]
                return f"https://t.me/{username}", username, username
        # ── 3. @username ──────────────────────────────────────────────────────
        elif line.startswith('@'):
            username = re.split(r'[^A-Za-z0-9_]', line[1:])[0]
            return f"https://t.me/{username}", username, username
        # ── 4. Numeric chat ID ────────────────────────────────────────────────
        elif re.match(r'^-?\d{5,}$', line.strip()):
            return line.strip(), None, line.strip()
        else:
            return None, None, None  # unparseable — caller should skip

    async def _handle_phone(self, m):
        u = m.from_user.id
        phone = m.text.strip()
        if not re.match(r'^\+[1-9]\d{1,14}$', phone):
            t, b = UI.error("Invalid format. Use: +1234567890")
            await m.reply_text(t, reply_markup=b, parse_mode=ParseMode.MARKDOWN)
            return

        # Check account limit
        ok, msg = await self._check_limits(u, "add_account")
        if not ok:
            t, b = UI.error(msg)
            await m.reply_text(t, reply_markup=b, parse_mode=ParseMode.MARKDOWN)
            return

        ok, msg, client = await self.accounts.add_account(u, phone)
        if ok and client:
            self.temp[u] = {"client": client, "phone": phone}
            self.states[u] = {"state": "otp"}
            t, b = UI.otp()
            await m.reply_text(t, reply_markup=b, parse_mode=ParseMode.MARKDOWN)
        else:
            t, b = UI.error(msg)
            await m.reply_text(t, reply_markup=b, parse_mode=ParseMode.MARKDOWN)
            if u in self.states:
                del self.states[u]

    async def _handle_otp(self, m):
        u = m.from_user.id
        if u not in self.temp:
            t, b = UI.error("Session expired.")
            await m.reply_text(t, reply_markup=b, parse_mode=ParseMode.MARKDOWN)
            if u in self.states:
                del self.states[u]
            return

        temp_data = self.temp[u]
        client   = temp_data["client"]
        phone    = temp_data["phone"]
        otp      = m.text.strip()

        try:
            ok, msg, session = await self.accounts.verify_otp(client, phone, otp)

            if ok:
                success = await self.accounts.save_account(u, phone, session)
                try:
                    await client.disconnect()
                except Exception:
                    pass
                del self.temp[u]
                del self.states[u]

                if success:
                    bio = self.db.fetch_one("SELECT bio FROM users WHERE user_id=?", (u,))
                    if bio and bio[0]:
                        await self.accounts.set_bio(u, bio[0])
                    tier, __, __ = await self._get_tier_and_limits(u)
                    if tier == Tier.FREE:
                        await self.accounts.enforce_name(u)
                    # Look up newly saved account_id and trigger auto-scan in background
                    new_acc = self.db.fetch_one(
                        "SELECT account_id FROM accounts WHERE user_id=? AND phone_number=?",
                        (u, phone))
                    if new_acc:
                        async def _bg_scan(aid=new_acc[0], uid=u, ph=phone):
                            await asyncio.sleep(3)
                            scan_stats = await self.accounts.auto_scan_groups(aid, uid)
                            added_n = scan_stats.get("added", 0)
                            total_n = scan_stats.get("total_scanned", 0)
                            if "error" not in scan_stats:
                                try:
                                    await self.app.send_message(
                                        uid,
                                        f"🔍 **Auto-Scan Complete** for `{ph}`\n\n"
                                        f"✅ Added **{added_n}** groups from **{total_n}** found.\n"
                                        "Go to 👥 Groups → 🔄 Toggle to review them.",
                                        parse_mode=ParseMode.MARKDOWN,
                                        reply_markup=InlineKeyboardMarkup([[
                                            InlineKeyboardButton("👥 View Groups", callback_data="groups")
                                        ]])
                                    )
                                except Exception:
                                    pass
                        asyncio.create_task(_bg_scan())
                    t, b = UI.success(
                        f"✅ Account `{phone}` added successfully!\n\n"
                        "🔍 Auto-scanning your groups in the background…"
                    )
                    await m.reply_text(t, reply_markup=b, parse_mode=ParseMode.MARKDOWN)
                else:
                    t, b = UI.error("Failed to save account. Please try again.")
                    await m.reply_text(t, reply_markup=b, parse_mode=ParseMode.MARKDOWN)

            elif msg == "2FA required":
                self.states[u] = {"state": "2fa"}
                await m.reply_text(
                    "🔐 **Two-Factor Authentication**\n\nPlease enter your 2FA password:",
                    parse_mode=ParseMode.MARKDOWN)

            else:
                try:
                    await client.disconnect()
                except Exception:
                    pass
                self.temp.pop(u, None)
                self.states.pop(u, None)

                if msg.startswith("BAN:"):
                    real = msg[4:]
                    await m.reply_text(
                        f"⛔ **Account Blocked by Telegram**\n\n"
                        f"{real}\n\n"
                        f"**Why this happens:**\n"
                        f"• This number was already flagged or banned before adding it\n"
                        f"• Fresh/new numbers are at high risk without prior manual activity\n"
                        f"• Accounts with any spam history are immediately rejected\n\n"
                        f"**What to do:**\n"
                        f"• ❌ Do NOT retry this number — it will not work\n"
                        f"• ✅ Use an account that is **2+ weeks old** with normal usage\n"
                        f"• ✅ Make sure it has a profile photo, bio, and display name\n"
                        f"• ✅ The account should have joined groups **manually** before this",
                        parse_mode=ParseMode.MARKDOWN,
                        reply_markup=InlineKeyboardMarkup([[
                            InlineKeyboardButton("◀ Back to Accounts", callback_data="accounts")
                        ]]))
                else:
                    t, b = UI.error(msg)
                    await m.reply_text(t, reply_markup=b, parse_mode=ParseMode.MARKDOWN)

        except Exception as e:
            logger.error(f"OTP handling error: {e}", exc_info=True)
            try:
                await client.disconnect()
            except Exception:
                pass
            self.temp.pop(u, None)
            self.states.pop(u, None)
            t, b = UI.error(f"Error: {str(e)[:80]}")
            await m.reply_text(t, reply_markup=b, parse_mode=ParseMode.MARKDOWN)

    async def _handle_2fa(self, m):
        u = m.from_user.id
        if u not in self.temp:
            t, b = UI.error("Session expired.")
            await m.reply_text(t, reply_markup=b, parse_mode=ParseMode.MARKDOWN)
            if u in self.states:
                del self.states[u]
            return

        temp_data = self.temp[u]
        client   = temp_data["client"]
        phone    = temp_data["phone"]
        password = m.text.strip()

        try:
            ok, msg, session = await self.accounts.verify_2fa(client, password)

            if ok:
                success = await self.accounts.save_account(u, phone, session)
                try:
                    await client.disconnect()
                except Exception:
                    pass
                del self.temp[u]
                del self.states[u]

                if success:
                    bio = self.db.fetch_one("SELECT bio FROM users WHERE user_id=?", (u,))
                    if bio and bio[0]:
                        await self.accounts.set_bio(u, bio[0])
                    tier, __, __ = await self._get_tier_and_limits(u)
                    if tier == Tier.FREE:
                        await self.accounts.enforce_name(u)
                    new_acc_2fa = self.db.fetch_one(
                        "SELECT account_id FROM accounts WHERE user_id=? AND phone_number=?",
                        (u, phone))
                    if new_acc_2fa:
                        async def _bg_scan_2fa(aid=new_acc_2fa[0], uid=u, ph=phone):
                            await asyncio.sleep(3)
                            sc = await self.accounts.auto_scan_groups(aid, uid)
                            added_n = sc.get("added", 0)
                            total_n = sc.get("total_scanned", 0)
                            if "error" not in sc:
                                try:
                                    await self.app.send_message(
                                        uid,
                                        f"🔍 **Auto-Scan Complete** for `{ph}`\n\n"
                                        f"✅ Added **{added_n}** groups from **{total_n}** found.\n"
                                        "Go to 👥 Groups → 🔄 Toggle to review them.",
                                        parse_mode=ParseMode.MARKDOWN,
                                        reply_markup=InlineKeyboardMarkup([[
                                            InlineKeyboardButton("👥 View Groups", callback_data="groups")
                                        ]])
                                    )
                                except Exception:
                                    pass
                        asyncio.create_task(_bg_scan_2fa())
                    t, b = UI.success(
                        f"✅ Account `{phone}` added successfully!\n\n"
                        "🔍 Auto-scanning your groups in the background…"
                    )
                    await m.reply_text(t, reply_markup=b, parse_mode=ParseMode.MARKDOWN)
                else:
                    t, b = UI.error("Failed to save account. Please try again.")
                    await m.reply_text(t, reply_markup=b, parse_mode=ParseMode.MARKDOWN)
            else:
                try:
                    await client.disconnect()
                except Exception:
                    pass
                self.temp.pop(u, None)
                self.states.pop(u, None)

                if msg.startswith("BAN:"):
                    real = msg[4:]
                    await m.reply_text(
                        f"⛔ **Account Blocked by Telegram**\n\n{real}\n\n"
                        f"This number cannot be used. Please add a different account.",
                        parse_mode=ParseMode.MARKDOWN,
                        reply_markup=InlineKeyboardMarkup([[
                            InlineKeyboardButton("◀ Back to Accounts", callback_data="accounts")
                        ]]))
                else:
                    t, b = UI.error(msg)
                    await m.reply_text(t, reply_markup=b, parse_mode=ParseMode.MARKDOWN)

        except Exception as e:
            logger.error(f"2FA handling error: {e}", exc_info=True)
            try:
                await client.disconnect()
            except Exception:
                pass
            self.temp.pop(u, None)
            self.states.pop(u, None)
            t, b = UI.error(f"Error: {str(e)[:80]}")
            await m.reply_text(t, reply_markup=b, parse_mode=ParseMode.MARKDOWN)

    # ---------- Callback Helpers for Pagination ----------
    async def _show_list_accounts(self, q, page=0):
        u = q.from_user.id
        per_page = 5
        accs = self.db.fetch_all(
            "SELECT phone_number, is_active, total_messages, added_date FROM accounts WHERE user_id=? ORDER BY added_date DESC LIMIT ? OFFSET ?",
            (u, per_page, page * per_page)
        )
        total = self.db.fetch_one("SELECT COUNT(*) FROM accounts WHERE user_id=?", (u,))[0] or 0
        total_pages = (total + per_page - 1) // per_page
        t, b = UI.list_accounts(accs, page, total_pages)
        await self.safe_edit(q.message, t, reply_markup=b)

    async def _show_list_groups(self, q, page=0):
        u = q.from_user.id
        per_page = 5
        groups = self.db.fetch_all(
            "SELECT group_title, group_link, is_active FROM target_groups WHERE user_id=? ORDER BY added_date DESC LIMIT ? OFFSET ?",
            (u, per_page, page * per_page)
        )
        total = self.db.fetch_one("SELECT COUNT(*) FROM target_groups WHERE user_id=?", (u,))[0] or 0
        total_pages = (total + per_page - 1) // per_page
        t, b, parse = UI.list_groups(groups, page, total_pages)
        await self.safe_edit(q.message, t, reply_markup=b, parse_mode=parse)

    async def _show_list_messages(self, q, page=0):
        u = q.from_user.id
        per_page = 5
        msgs = self.db.fetch_all(
            "SELECT msg_id, message_text, added_date, is_active FROM user_messages WHERE user_id=? ORDER BY added_date DESC LIMIT ? OFFSET ?",
            (u, per_page, page * per_page)
        )
        msgs_display = []
        for m in msgs:
            preview = m[1][:30] + "..." if len(m[1]) > 30 else m[1]
            msgs_display.append((m[0], preview, m[2], m[3]))
        total = self.db.fetch_one("SELECT COUNT(*) FROM user_messages WHERE user_id=?", (u,))[0] or 0
        total_pages = (total + per_page - 1) // per_page
        t, b = UI.list_messages(msgs_display, page, total_pages)
        await self.safe_edit(q.message, t, reply_markup=b)

    async def _show_toggle_groups_menu(self, q):
        u = q.from_user.id
        groups = self.db.fetch_all("SELECT group_id, group_title, is_active FROM target_groups WHERE user_id=?", (u,))
        if not groups:
            await q.answer("No groups.", show_alert=True)
            return
        kb = []
        for g in groups[:8]:
            status = "●" if g[2] else "○"
            kb.append([InlineKeyboardButton(f"{status} {g[1][:20]}", callback_data=f"toggle_group_{g[0]}")])
        kb.append([InlineKeyboardButton("❌  Back", callback_data="groups")])
        await self.safe_edit(q.message, "**🔄 Toggle Group Status**", reply_markup=InlineKeyboardMarkup(kb))

    async def _show_remove_groups_menu(self, q):
        u = q.from_user.id
        groups = self.db.fetch_all("SELECT group_id, group_title FROM target_groups WHERE user_id=?", (u,))
        if not groups:
            await q.answer("No groups to remove.", show_alert=True)
            t, b = UI.groups_menu()
            try:
                await self.safe_edit(q.message, t, reply_markup=b)
            except Exception:
                await q.message.reply_text(t, reply_markup=b, parse_mode=ParseMode.MARKDOWN)
            return
        kb = []
        for g in groups[:8]:
            label = (g[1] or "Unnamed")[:22]
            kb.append([InlineKeyboardButton(f"✗  {label}", callback_data=f"remove_group_{g[0]}")])
        kb.append([InlineKeyboardButton("❌  Back", callback_data="groups")])
        total = len(groups)
        await self.safe_edit(
            q.message,
            f"{UI._hdr('✗', 'Remove Groups')}\n\n**{total}** group(s). Tap to remove.",
            reply_markup=InlineKeyboardMarkup(kb),
            parse_mode=ParseMode.MARKDOWN
        )

    async def _show_delete_messages_menu(self, q):
        u = q.from_user.id
        msgs = self.db.fetch_all(
            "SELECT msg_id, message_text FROM user_messages WHERE user_id=? AND is_active=1",
            (u,)
        )
        if not msgs:
            await q.answer("No messages.", show_alert=True)
            return
        kb = []
        for m in msgs[:8]:
            preview = m[1][:20] + "..." if len(m[1]) > 20 else m[1]
            kb.append([InlineKeyboardButton(f"✗ {preview}", callback_data=f"delmsg_{m[0]}")])
        kb.append([InlineKeyboardButton("❌  Back", callback_data="messages_menu")])
        await self.safe_edit(q.message, "**✗ Select message to delete**", reply_markup=InlineKeyboardMarkup(kb))

    # ---------- Main Callback Handler ----------
    async def _handle_callback(self, q):
        u = q.from_user.id
        data = q.data

        # Acknowledge the button press immediately — removes the spinner on the client side.
        # This is the single biggest UX win: the button stops "loading" instantly regardless
        # of how long the actual handler takes.
        try:
            await q.answer()
        except Exception:
            pass  # already answered or timed out — not critical

        # First, check access (skip for owner-only actions and purchase menu)
        if not (data.startswith("owner_panel") or data in ["lock_bot", "unlock_bot", "give_premium", "give_elite", "remove_premium", "check_premium", "toggle_bio_required", "set_global_bio", "force_push_bio_name", "type_interval", "send_tutorial", "auto_scan_groups", "purchase", "tier_free", "tier_premium", "tier_elite"]):
            if not await self._check_access(u):
                await q.answer("Locked for free users. Purchase a tier.", show_alert=True)
                return

        # Home (welcome screen)
        if data == "home":
            if u in self.states:
                del self.states[u]
            t, b = UI.welcome()
            await self.safe_edit(q.message, t, b, parse_mode=ParseMode.MARKDOWN)

        # Help screen
        elif data == "help":
            if u in self.states:
                del self.states[u]
            t, b = UI.help_menu()
            await self.safe_edit(q.message, t, reply_markup=b, parse_mode=ParseMode.MARKDOWN)

        elif data == "send_tutorial":
            if u in self.states:
                del self.states[u]
            try:
                html_bytes = _get_tutorial_bytes()
                bio_file = _io.BytesIO(html_bytes)
                bio_file.name = "VerxAdsBot_Tutorial.html"
                await q.message.reply_document(
                    document=bio_file,
                    caption=(
                        "📖 **Verx Ads Bot — Complete Tutorial**\n\n"
                        "Open this file in any browser to read the full interactive guide:\n"
                        "• Step-by-step setup (add account → start ads)\n"
                        "• Every feature explained with live examples\n"
                        "• Free / Premium / Elite plan comparison\n"
                        "• Account safety tips & FAQ"
                    ),
                    parse_mode=ParseMode.MARKDOWN
                )
            except Exception as e:
                logger.error(f"send_tutorial error: {e}")
                await q.answer("Could not send tutorial.", show_alert=True)

        # Dashboard
        elif data == "dashboard":
            if u in self.states:
                del self.states[u]
            await self._show_dashboard(q)

        # Purchase menu
        elif data == "purchase":
            t, b = UI.plans_menu("free")
            await self.safe_edit(q.message, t, reply_markup=b, parse_mode=ParseMode.MARKDOWN)

        elif data == "tier_free":
            t, b = UI.plans_menu("free")
            await self.safe_edit(q.message, t, reply_markup=b, parse_mode=ParseMode.MARKDOWN)

        elif data == "tier_premium":
            t, b = UI.plans_menu("premium")
            await self.safe_edit(q.message, t, reply_markup=b, parse_mode=ParseMode.MARKDOWN)

        elif data == "tier_elite":
            t, b = UI.plans_menu("elite")
            await self.safe_edit(q.message, t, reply_markup=b, parse_mode=ParseMode.MARKDOWN)

        # Navigation
        elif data == "accounts":
            if u in self.states:
                del self.states[u]  # clear any stale state
            t, b = UI.accounts_menu()
            await self.safe_edit(q.message, t, reply_markup=b)
        elif data == "groups":
            if u in self.states:
                del self.states[u]
            t, b = UI.groups_menu()
            await self.safe_edit(q.message, t, reply_markup=b)
        elif data == "messages_menu":
            if u in self.states:
                del self.states[u]
            tier, limits, _ = await self._get_tier_and_limits(u)
            msg_count = self.db.fetch_one("SELECT COUNT(*) FROM user_messages WHERE user_id=?", (u,))[0] or 0
            t, b = UI.messages_menu(msg_count, limits["max_messages"])
            await self.safe_edit(q.message, t, reply_markup=b)

        # Owner panel
        elif data == "owner_panel":
            if u not in OWNER_IDS:
                await q.answer("Unauthorized", show_alert=True)
                return
            bio_required = self.db.fetch_one("SELECT value FROM settings WHERE key='bio_required'")[0] == 'true'
            locked = self.db.fetch_one("SELECT value FROM settings WHERE key='locked'")[0] == 'true'
            t, b = UI.owner_panel(bio_required, locked)
            await self.safe_edit(q.message, t, reply_markup=b)

        elif data == "lock_bot":
            if u not in OWNER_IDS:
                return
            self.db.execute("UPDATE settings SET value='true' WHERE key='locked'")
            self._invalidate_locked_cache()
            stopped = await self.broadcasts.stop_all_non_premium()
            await q.answer(f"Locked. Stopped {stopped} broadcasts.", show_alert=False)
            await self._show_dashboard(q)

        elif data == "unlock_bot":
            if u not in OWNER_IDS:
                return
            self.db.execute("UPDATE settings SET value='false' WHERE key='locked'")
            self._invalidate_locked_cache()
            await q.answer("Unlocked.", show_alert=False)
            await self._show_dashboard(q)

        elif data == "toggle_bio_required":
            if u not in OWNER_IDS:
                return
            current = self.db.fetch_one("SELECT value FROM settings WHERE key='bio_required'")[0] == 'true'
            new = 'false' if current else 'true'
            self.db.execute("UPDATE settings SET value=? WHERE key='bio_required'", (new,))
            await q.answer(f"Bio required set to {'ON' if new=='true' else 'OFF'}.", show_alert=False)
            bio_required = self.db.fetch_one("SELECT value FROM settings WHERE key='bio_required'")[0] == 'true'
            locked = self.db.fetch_one("SELECT value FROM settings WHERE key='locked'")[0] == 'true'
            t, b = UI.owner_panel(bio_required, locked)
            await self.safe_edit(q.message, t, reply_markup=b)

        elif data == "set_global_bio":
            if u not in OWNER_IDS:
                return
            cur_bio_row = self.db.fetch_one("SELECT value FROM settings WHERE key='global_bio'")
            cur_bio = cur_bio_row[0] if cur_bio_row else DEFAULT_BIO
            await q.message.edit_text(
                f"**🌐 Set Global Free-Tier Bio**\n{UI.DIVIDER}\n\n"
                f"Current:\n`{cur_bio}`\n\n"
                "Send the new bio that will be auto-applied to all free-tier accounts.\n"
                "__(max 70 characters)__",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("◄  Back", callback_data="owner_panel")]]),
                parse_mode=ParseMode.MARKDOWN
            )
            self.states[u] = {"state": "set_global_bio"}

        elif data == "force_push_bio_name":
            if u not in OWNER_IDS:
                await q.answer("Unauthorized", show_alert=True)
                return
            await q.answer("Pushing bio+name to all free accounts…", show_alert=False)
            async def _do_force_push():
                count = await self.accounts.enforce_all_free_users()
                try:
                    await self.app.send_message(
                        u,
                        f"✅ **Force Push Complete**\n\nUpdated **{count}** free-tier account(s) with current global bio and name suffix.",
                        parse_mode=ParseMode.MARKDOWN
                    )
                except Exception:
                    pass
            asyncio.create_task(_do_force_push())

        elif data == "give_premium":
            if u not in OWNER_IDS:
                return
            await q.message.edit_text(
                f"**🎁 Give Premium**\n{UI.DIVIDER}\n\n"
                "Send: `<user_id> <days>`\n"
                "Example: `123456789 30`",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌  Back", callback_data="owner_panel")]]),
                parse_mode=ParseMode.MARKDOWN
            )
            self.states[u] = {"state": "give_premium"}

        elif data == "give_elite":
            if u not in OWNER_IDS:
                return
            await q.message.edit_text(
                f"**🎗 Give Elite**\n{UI.DIVIDER}\n\n"
                "Send: `<user_id> <days>`\n"
                "Example: `123456789 30`",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌  Back", callback_data="owner_panel")]]),
                parse_mode=ParseMode.MARKDOWN
            )
            self.states[u] = {"state": "give_elite"}

        elif data == "remove_premium":
            if u not in OWNER_IDS:
                return
            await q.message.edit_text(
                f"**🗑 Remove Tier**\n{UI.DIVIDER}\n\n"
                "Send user ID:\n`<user_id>`",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌  Back", callback_data="owner_panel")]]),
                parse_mode=ParseMode.MARKDOWN
            )
            self.states[u] = {"state": "remove_premium"}

        elif data == "check_premium":
            if u not in OWNER_IDS:
                return
            await q.message.edit_text(
                f"**🔍 Check User Tier**\n{UI.DIVIDER}\n\n"
                "Send user ID:\n`<user_id>`",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌  Back", callback_data="owner_panel")]]),
                parse_mode=ParseMode.MARKDOWN
            )
            self.states[u] = {"state": "check_premium"}

        # Account management
        elif data == "add_account":
            if u in self.states:
                del self.states[u]
            # Check limit before proceeding
            ok, msg = await self._check_limits(u, "add_account")
            if not ok:
                await q.answer(msg, show_alert=True)
                return
            t, b = UI.add_phone()
            await self.safe_edit(q.message, t, reply_markup=b)
            self.states[u] = {"state": "phone"}

        elif data == "list_accounts":
            if u in self.states:
                del self.states[u]
            await self._show_list_accounts(q)

        elif data.startswith("list_accounts_page_"):
            page = int(data.split("_")[3])
            self._list_pages[u] = page
            await self._show_list_accounts(q, page)

        elif data == "remove_account":
            if u in self.states:
                del self.states[u]
            accs = self.db.fetch_all("SELECT account_id, phone_number FROM accounts WHERE user_id=?", (u,))
            if not accs:
                await q.answer("No accounts.", show_alert=True)
                return
            kb = []
            for a in accs[:8]:
                kb.append([InlineKeyboardButton(f"✗ {a[1]}", callback_data=f"remove_acc_{a[0]}")])
            kb.append([InlineKeyboardButton("❌  Back", callback_data="accounts")])
            await self.safe_edit(q.message, "**✗ Select account to remove**", reply_markup=InlineKeyboardMarkup(kb))

        elif data.startswith("remove_acc_"):
            aid = int(data.split("_")[2])
            phone = self.db.fetch_one("SELECT phone_number FROM accounts WHERE account_id=?", (aid,))[0]
            t, b = UI.confirm_remove_account(aid, phone)
            await self.safe_edit(q.message, t, reply_markup=b)

        elif data.startswith("confirm_del_"):
            aid = int(data.split("_")[2])
            running = self.db.fetch_all("SELECT broadcast_id FROM broadcasts WHERE account_id=? AND is_running=1", (aid,))
            for (bid,) in running:
                await self.broadcasts.stop(bid)
            success = await self.accounts.remove_account(aid)
            if success:
                await q.answer("✓ Account removed.", show_alert=False)
            else:
                await q.answer("✗ Failed.", show_alert=True)
            await self._handle_callback_by_data(q, "remove_account")

        # Group management
        elif data in ("add_groups", "add_group"):
            if u in self.states:
                del self.states[u]
            tier_ag, limits_ag, _ = await self._get_tier_and_limits(u)
            current_ag = self.db.fetch_one("SELECT COUNT(*) FROM target_groups WHERE user_id=?", (u,))[0] or 0
            max_ag = limits_ag["max_groups"]
            if current_ag >= max_ag:
                await q.answer(f"Group limit reached ({current_ag}/{max_ag}). Upgrade to add more.", show_alert=True)
                return
            slots = max_ag - current_ag
            tier_label = {"free": "⚡ Free", "premium": "👑 Premium", "elite": "🎗 Elite"}.get(tier_ag, tier_ag)
            t = (
                f"{UI._hdr('➕', 'Add Target Groups')}\n\n"
                f"📊 **{current_ag} / {max_ag}** groups used  •  **{slots}** slot(s) free\n"
                f"🏷 Tier: {tier_label}\n{UI.DIVIDER}\n\n"
                "Send group links — one per line:\n"
                "• `https://t.me/groupname`\n"
                "• `@groupname`\n"
                "• Folder: `https://t.me/addlist/...`\n\n"
                "__Duplicates are detected and skipped automatically.__"
            )
            b = InlineKeyboardMarkup([[InlineKeyboardButton("✗  Cancel", callback_data="groups")]])
            await self.safe_edit(q.message, t, reply_markup=b, parse_mode=ParseMode.MARKDOWN)
            self.states[u] = {"state": "groups"}

        elif data == "auto_scan_groups":
            if u in self.states:
                del self.states[u]
            accs = self.db.fetch_all(
                "SELECT account_id, phone_number FROM accounts WHERE user_id=? AND is_active=1", (u,))
            if not accs:
                await q.answer("Add at least one account before scanning.", show_alert=True)
                return
            tier_s, limits_s, _ = await self._get_tier_and_limits(u)
            await self.safe_edit(
                q.message,
                f"{UI._hdr('🔍', 'Auto-Scanning Groups')}\n\n"
                "Scanning all groups your account is a member of…\n"
                "Filtering for groups where you can actually send messages.\n\n"
                "_This may take a few seconds — please wait._",
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton("✗  Cancel", callback_data="groups")
                ]]),
                parse_mode=ParseMode.MARKDOWN
            )
            account_id = accs[0][0]
            scan_stats = await self.accounts.auto_scan_groups(account_id, u)
            t, b = UI.auto_scan_result(scan_stats, limits_s["max_groups"])
            await self.safe_edit(q.message, t, reply_markup=b, parse_mode=ParseMode.MARKDOWN)
        elif data == "list_groups":
            if u in self.states:
                del self.states[u]
            await self._show_list_groups(q)

        elif data.startswith("list_groups_page_"):
            page = int(data.split("_")[3])
            self._list_pages[u] = page
            await self._show_list_groups(q, page)

        elif data == "toggle_groups":
            if u in self.states:
                del self.states[u]
            await self._show_toggle_groups_menu(q)

        elif data.startswith("toggle_group_"):
            gid = int(data.split("_")[2])
            cur = self.db.fetch_one("SELECT is_active FROM target_groups WHERE group_id=?", (gid,))
            if cur:
                new = 0 if cur[0] else 1
                self.db.execute("UPDATE target_groups SET is_active=? WHERE group_id=?", (new, gid))
                await q.answer(f"Group {'activated' if new else 'deactivated'}.", show_alert=False)
            await self._show_toggle_groups_menu(q)

        elif data == "remove_groups":
            if u in self.states:
                del self.states[u]
            await self._show_remove_groups_menu(q)

        elif data.startswith("remove_group_"):
            gid = int(data.split("_")[2])
            title = self.db.fetch_one("SELECT group_title FROM target_groups WHERE group_id=?", (gid,))[0]
            t, b = UI.confirm_remove_group(gid, title)
            await self.safe_edit(q.message, t, reply_markup=b)

        elif data.startswith("confirm_rem_group_"):
            gid = int(data.split("_")[3])
            self.db.execute("DELETE FROM target_groups WHERE group_id=?", (gid,))
            await q.answer("✓ Group removed.", show_alert=False)
            await self._show_remove_groups_menu(q)

        # Message management
        elif data == "add_message":
            if u in self.states:
                del self.states[u]
            # Check limit
            ok, msg = await self._check_limits(u, "add_message")
            if not ok:
                await q.answer(msg, show_alert=True)
                return
            t, b = UI.add_message_prompt()
            await self.safe_edit(q.message, t, reply_markup=b)
            self.states[u] = {"state": "new_message"}

        elif data == "list_messages":
            if u in self.states:
                del self.states[u]
            await self._show_list_messages(q)

        elif data.startswith("list_messages_page_"):
            page = int(data.split("_")[3])
            self._list_pages[u] = page
            await self._show_list_messages(q, page)

        elif data == "delete_message":
            if u in self.states:
                del self.states[u]
            await self._show_delete_messages_menu(q)

        elif data.startswith("delmsg_"):
            mid = int(data.split("_")[1])
            preview = self.db.fetch_one("SELECT message_text FROM user_messages WHERE msg_id=?", (mid,))[0]
            preview_short = preview[:30] + "..." if len(preview) > 30 else preview
            t, b = UI.confirm_delete_message(mid, preview_short)
            await self.safe_edit(q.message, t, reply_markup=b)

        elif data.startswith("confirm_delmsg_"):
            mid = int(data.split("_")[2])
            self.db.execute("DELETE FROM user_messages WHERE msg_id=?", (mid,))
            await q.answer("✓ Message deleted.", show_alert=False)
            await self._show_delete_messages_menu(q)

        # Ad settings
        elif data == "set_interval":
            if u in self.states:
                del self.states[u]
            tier, limits, _ = await self._get_tier_and_limits(u)
            current = self.intervals.get(u, limits["interval_min"])
            t, b = UI.set_interval(current, tier)
            await self.safe_edit(q.message, t, reply_markup=b)

        elif data == "type_interval":
            # Only Elite/Owner can type custom intervals
            tier, limits, _ = await self._get_tier_and_limits(u)
            if not limits["interval_custom"]:
                await q.answer("Custom interval requires Elite tier.", show_alert=True)
                return
            current = self.intervals.get(u, limits["interval_min"])
            t, b = UI.type_interval_prompt(current, limits["interval_min"])
            self.states[u] = {"state": "interval"}
            await self.safe_edit(q.message, t, reply_markup=b)

        elif data.startswith("interval_"):
            secs = int(data.split("_")[1])
            tier, limits, _ = await self._get_tier_and_limits(u)
            if secs < limits["interval_min"]:
                hrs_min = limits["interval_min"] // 3600
                label = f"{hrs_min}h" if hrs_min else f"{limits['interval_min'] // 60}m"
                await q.answer(
                    f"⚡ {tier.capitalize()} tier minimum is {label}. Upgrade for shorter intervals.",
                    show_alert=True
                )
                if u in self.states: del self.states[u]
                await self._show_dashboard(q)
                return
            self.intervals[u] = secs
            await self.broadcasts.update_interval_for_user(u, secs)
            if u in self.states: del self.states[u]
            hrs = secs // 3600
            mins = (secs % 3600) // 60
            label = f"{hrs}h {mins}m" if hrs else f"{mins}m"
            await q.answer(f"✓ Interval: {label}", show_alert=False)
            await self._show_dashboard(q)

        elif data == "set_bio":
            if u in self.states:
                del self.states[u]
            tier, limits, _ = await self._get_tier_and_limits(u)
            if not limits["set_bio"]:
                t, b = UI.set_bio_locked()
                await self.safe_edit(q.message, t, reply_markup=b, parse_mode=ParseMode.MARKDOWN)
                return
            bio = self.db.fetch_one("SELECT bio FROM users WHERE user_id=?", (u,))
            current = bio[0] if bio and bio[0] else ""
            t, b = UI.set_bio(current)
            self.states[u] = {"state": "bio"}
            await self.safe_edit(q.message, t, reply_markup=b)

        elif data == "confirm_bio":
            if u not in self._pending_bio:
                await q.answer("No pending bio.", show_alert=True)
                return
            bio = self._pending_bio.pop(u)
            await self.accounts.set_bio(u, bio)
            await q.answer("✓ Bio updated.", show_alert=False)
            await self._show_dashboard(q)

        # Broadcast control
        elif data == "start_ads":
            if u in self.states:
                del self.states[u]

            # Lock check — free users cannot start broadcasts when bot is locked
            locked_val = self._get_locked()
            if locked_val and u not in OWNER_IDS:
                tier_chk, _, __ = await self._get_tier_and_limits(u)
                if tier_chk == Tier.FREE:
                    await self.safe_edit(
                        q.message,
                        f"{UI._hdr('🔒', 'Bot Locked')}\n\n"
                        "**Broadcasts are paused for free users.**\n\n"
                        "The owner has temporarily restricted access.\n"
                        "Upgrade to **Premium** or **Elite** to bypass\n"
                        "this restriction and keep broadcasting.",
                        reply_markup=InlineKeyboardMarkup([
                            [InlineKeyboardButton("💬  Contact Owner", url=f"https://t.me/{OWNER_USERNAME}")],
                            [InlineKeyboardButton("❌  Back", callback_data="dashboard")]
                        ]),
                        parse_mode=ParseMode.MARKDOWN
                    )
                    return

            # Already running?
            running_count = self.db.fetch_one(
                "SELECT COUNT(*) FROM broadcasts WHERE user_id=? AND is_running=1", (u,))[0] or 0
            if running_count > 0:
                await q.answer("📡 Broadcast already running!", show_alert=True)
                await self._show_dashboard(q)
                return

            accs = self.db.fetch_all("SELECT account_id FROM accounts WHERE user_id=? AND is_active=1", (u,))
            if not accs:
                await q.answer("No active accounts. Add an account first.", show_alert=True)
                return
            groups = self.db.fetch_one("SELECT COUNT(*) FROM target_groups WHERE user_id=? AND is_active=1", (u,))
            if not groups or groups[0] == 0:
                await q.answer("No target groups. Add groups first.", show_alert=True)
                return
            msgs = self.db.fetch_one("SELECT COUNT(*) FROM user_messages WHERE user_id=? AND is_active=1", (u,))
            if not msgs or msgs[0] == 0:
                await q.answer("No ad messages. Add messages first.", show_alert=True)
                return

            tier, limits, _ = await self._get_tier_and_limits(u)
            tagging = False
            if limits["max_tags"] > 0:
                acc = self.db.fetch_one("SELECT tagging_enabled FROM accounts WHERE account_id=?", (accs[0][0],))
                tagging = acc and acc[0] == 1

            started = 0
            for (aid,) in accs:
                ok, _ = await self.broadcasts.start(u, aid, self.intervals.get(u, limits["interval_min"]), tagging)
                if ok:
                    started += 1

            # ── Professional popup: tell user exactly what is happening ──
            interval_secs = self.intervals.get(u, limits["interval_min"])
            groups_active = self.db.fetch_one(
                "SELECT COUNT(*) FROM target_groups WHERE user_id=? AND is_active=1", (u,))[0] or 0
            iv_h  = interval_secs // 3600
            iv_m  = (interval_secs % 3600) // 60
            iv_s  = interval_secs % 60
            iv_parts = []
            if iv_h: iv_parts.append(f"{iv_h} hour{'s' if iv_h > 1 else ''}")
            if iv_m: iv_parts.append(f"{iv_m} minute{'s' if iv_m > 1 else ''}")
            if iv_s or not iv_parts: iv_parts.append(f"{iv_s} second{'s' if iv_s != 1 else ''}")
            iv_label = " & ".join(iv_parts)

            popup_text = (
                f"✅ Ads are now LIVE!\n\n"
                f"📡 {started} broadcast account(s) active\n"
                f"👥 Targeting {groups_active} group(s)\n"
                f"⏱ Sending every {iv_label}\n\n"
                f"You'll receive a summary after each full cycle."
            )
            await q.answer(popup_text, show_alert=True)

            # ── Logger: ads started ──
            user_row = self.db.fetch_one("SELECT username FROM users WHERE user_id=?", (u,))
            uname_log = (user_row[0] or "") if user_row else ""
            asyncio.create_task(self.verx_logger.log_ads_started(
                user_id         = u,
                username        = uname_log,
                broadcast_count = started,
                groups_count    = groups_active,
                interval_seconds= interval_secs,
                tier            = tier,
            ))

            await self._show_dashboard(q)

        elif data == "stop_ads":
            if u in self.states:
                del self.states[u]
            # Free users can always stop — only starting is locked

            accs = self.db.fetch_all("SELECT account_id FROM accounts WHERE user_id=? AND is_active=1", (u,))
            if not accs:
                t, b = UI.no_accounts_dialog()
                await self.safe_edit(q.message, t, reply_markup=b, parse_mode=ParseMode.MARKDOWN)
                return

            running_count = self.db.fetch_one(
                "SELECT COUNT(*) FROM broadcasts WHERE user_id=? AND is_running=1", (u,))[0] or 0
            if running_count == 0:
                await q.answer("⏹ No active broadcast to stop.", show_alert=True)
                await self._show_dashboard(q)
                return

            stopped = await self.broadcasts.stop_all(u)
            await q.answer(f"⏹ Stopped {stopped} broadcast(s).", show_alert=False)
            # ── Logger: ads stopped ──
            user_row_s = self.db.fetch_one("SELECT username FROM users WHERE user_id=?", (u,))
            asyncio.create_task(self.verx_logger.log_ads_stopped(
                user_id       = u,
                username      = (user_row_s[0] or "") if user_row_s else "",
                stopped_count = stopped,
            ))
            await self._show_dashboard(q)

        # Tagging – all tiers can view; free tier toggle is locked
        elif data == "tagging":
            if u in self.states:
                del self.states[u]
            await self._show_tagging_menu(q)

        elif data.startswith("toggle_tag_"):
            tier, limits, _ = await self._get_tier_and_limits(u)
            if limits.get("tagging_locked", False):
                await q.answer("Tagging toggle requires Premium or Elite.", show_alert=True)
                return
            aid = int(data.split("_")[2])
            cur = self.db.fetch_one("SELECT tagging_enabled FROM accounts WHERE account_id=?", (aid,))
            if cur:
                new = 0 if cur[0] else 1
                self.db.execute("UPDATE accounts SET tagging_enabled=? WHERE account_id=?", (new, aid))
                await q.answer(f"Tagging {'enabled' if new else 'disabled'}.", show_alert=False)
            await self._show_tagging_menu(q)

        elif data.startswith("set_tags_"):
            tier, limits, _ = await self._get_tier_and_limits(u)
            if limits.get("tagging_locked", False):
                await q.answer("Tagging requires Premium or Elite.", show_alert=True)
                return
            aid = int(data.split("_")[2])
            t, b = UI.tags_count(aid)
            await self.safe_edit(q.message, t, reply_markup=b)

        elif data.startswith("tags_set_"):
            tier, limits, _ = await self._get_tier_and_limits(u)
            if limits["max_tags"] == 0:
                await q.answer("Tagging not available.", show_alert=True)
                return
            parts = data.split("_")
            aid = int(parts[2])
            count = int(parts[3])
            if count > limits["max_tags"]:
                await q.answer(f"Your tier allows max {limits['max_tags']} tags.", show_alert=True)
                return
            self.db.execute("UPDATE accounts SET tags_per_message=? WHERE account_id=?", (count, aid))
            await q.answer(f"Tags set to {count}.", show_alert=False)
            await self._show_tagging_menu(q)

        # Auto-reply – only if tier allows
        elif data == "auto_reply":
            if u in self.states:
                del self.states[u]
            tier, limits, _ = await self._get_tier_and_limits(u)
            allowed = limits["auto_reply"]
            await self._show_auto_reply(q, allowed)

        elif data == "toggle_autoreply":
            tier, limits, _ = await self._get_tier_and_limits(u)
            if not limits["auto_reply"]:
                await q.answer("Auto-reply not available in your tier.", show_alert=True)
                return
            accs = self.db.fetch_all("SELECT account_id FROM accounts WHERE user_id=?", (u,))
            if not accs:
                await q.answer("No accounts.", show_alert=True)
                return
            aid = accs[0][0]
            cur = self.db.fetch_one("SELECT auto_reply_enabled FROM accounts WHERE account_id=?", (aid,))
            if cur:
                if cur[0]:
                    await self.autoreply.disable(aid)
                    await q.answer("Auto-reply disabled.", show_alert=False)
                else:
                    await self.autoreply.enable(aid)
                    await q.answer("Auto-reply enabled.", show_alert=False)
            await self._show_auto_reply(q, True)

        elif data == "autoreply_stats":
            tier, limits, _ = await self._get_tier_and_limits(u)
            if not limits["auto_reply"]:
                await q.answer("Auto-reply not available.", show_alert=True)
                return
            if u in self.states:
                del self.states[u]
            total = {"replies": 0, "tokens": 0}
            for acc in self.groq.usage.values():
                total["replies"] += acc["replies"]
                total["tokens"] += acc["tokens"]
            t = (
                f"**📊 Auto-Reply Stats**\n"
                f"━━━━━━━━━━━━━━━━━━━━━\n"
                f"Replies: `{total['replies']}`   Tokens: `{total['tokens']}`\n"
                f"Est. Cost: `${total['tokens']*0.00000059:.6f}`"
            )
            await self.safe_edit(q.message, t, reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("❌  Back", callback_data="auto_reply")
            ]]))

        # Analytics
        elif data == "analytics":
            if u in self.states:
                del self.states[u]
            await self._show_analytics(q)

        elif data == "analytics_detailed":
            if u in self.states:
                del self.states[u]
            await self._show_detailed_analytics(q)

        # Resend OTP
        elif data == "resend_otp":
            if u not in self.temp:
                await q.answer("Session expired.", show_alert=True)
                await self._show_dashboard(q)
                return
            try:
                await self.temp[u]["client"].send_code_request(self.temp[u]["phone"])
                await q.answer("OTP resent.", show_alert=False)
            except Exception as e:
                await q.answer(f"Error: {str(e)[:50]}", show_alert=True)

        # Check joined
        elif data == "check_joined":
            # Invalidate stale cache so we do a live API check right now
            self._invalidate_channel_cache(u)
            if await self._check_required_channels(u):
                await q.answer("✓ Verified! Welcome.", show_alert=False)
                t, b = UI.welcome()
                await self.safe_edit(q.message, t, b, parse_mode=ParseMode.MARKDOWN)
            else:
                await q.answer("✗ Please join both channels first.", show_alert=True)

        else:
            logger.warning(f"Unhandled callback: {data}")

    async def _handle_callback_by_data(self, q, callback_data):
        """Helper to navigate to a menu using callback data.
        Note: _handle_callback only accepts (q) — simulate navigation via show helpers.
        """
        if callback_data == "remove_account":
            await self._show_list_accounts(q)
        elif callback_data == "remove_groups":
            await self._show_remove_groups_menu(q)
        elif callback_data == "delete_message":
            await self._show_delete_messages_menu(q)
        else:
            await self._show_dashboard(q)

    async def _show_auto_reply(self, q, allowed):
        u = q.from_user.id
        accs = self.db.fetch_all("SELECT account_id FROM accounts WHERE user_id=?", (u,))
        if not accs:
            await q.answer("Add accounts first.", show_alert=True)
            return
        aid = accs[0][0]
        acc = self.db.fetch_one("SELECT auto_reply_enabled FROM accounts WHERE account_id=?", (aid,))
        enabled = acc[0] if acc else 0
        stats = self.groq.usage.get(aid, {"replies": 0, "tokens": 0})
        t, b = UI.auto_reply_menu(enabled, stats, allowed)
        await self.safe_edit(q.message, t, reply_markup=b)

    async def _show_tagging_menu(self, q):
        u = q.from_user.id
        accs = self.db.fetch_all("SELECT account_id FROM accounts WHERE user_id=?", (u,))
        if not accs:
            await q.answer("Add accounts first.", show_alert=True)
            await self._show_dashboard(q)
            return
        aid = accs[0][0]
        acc = self.db.fetch_one("SELECT tagging_enabled, tags_per_message FROM accounts WHERE account_id=?", (aid,))
        enabled = acc[0] if acc else 0
        tags = acc[1] if acc else DEFAULT_TAGS_PER_MESSAGE
        tier, limits, _ = await self._get_tier_and_limits(u)
        t, b = UI.tagging(aid, enabled, tags, limits["max_tags"], locked=limits.get("tagging_locked", False))
        await self.safe_edit(q.message, t, reply_markup=b)

    async def _show_dashboard(self, q):
        u = q.from_user.id
        accs = self.db.fetch_all("SELECT account_id FROM accounts WHERE user_id=?", (u,))
        groups = self.db.fetch_all("SELECT group_id FROM target_groups WHERE user_id=? AND is_active=1", (u,))
        msg_count = self.db.fetch_one("SELECT COUNT(*) FROM user_messages WHERE user_id=?", (u,))[0] or 0
        running = self.db.fetch_one("SELECT COUNT(*) FROM broadcasts WHERE user_id=? AND is_running=1", (u,))
        status = "▶️ Running" if running and running[0] > 0 else "⏸️ Paused"
        bio_row = self.db.fetch_one("SELECT bio FROM users WHERE user_id=?", (u,))
        bio = bio_row[0] if bio_row and bio_row[0] else ""
        is_owner = u in OWNER_IDS
        tier, limits, days_left = await self._get_tier_and_limits(u)
        t, b = UI.dashboard(
            acc=len(accs),
            groups=len(groups),
            msg_count=msg_count,
            interval=self.intervals.get(u, DEFAULT_INTERVAL),
            status=status,
            bio=bio,
            is_owner=is_owner,
            tier=tier,
            days_left=days_left,
            max_acc=limits["max_accounts"],
            max_groups=limits["max_groups"],
            max_msgs=limits["max_messages"]
        )
        await self.safe_edit(q.message, t, reply_markup=b)

    async def _show_analytics(self, q):
        u = q.from_user.id
        stats = {
            'sent': 0, 'failed': 0, 'cycles': 0, 'tags': 0, 'active': 0
        }

        totals = self.db.fetch_one('''
            SELECT COALESCE(SUM(total_messages),0), COALESCE(SUM(failed_messages),0)
            FROM accounts WHERE user_id=?
        ''', (u,))
        if totals:
            stats['sent'], stats['failed'] = totals

        cycles = self.db.fetch_one("SELECT COUNT(*) FROM broadcasts WHERE user_id=?", (u,))
        if cycles:
            stats['cycles'] = cycles[0]

        tags = self.db.fetch_one('''
            SELECT COALESCE(SUM(tags_used),0) FROM message_history
            WHERE account_id IN (SELECT account_id FROM accounts WHERE user_id=?)
        ''', (u,))
        if tags:
            stats['tags'] = tags[0]

        active = self.db.fetch_one("SELECT COUNT(*) FROM accounts WHERE user_id=? AND is_active=1", (u,))
        if active:
            stats['active'] = active[0]

        tier, _, days_left = await self._get_tier_and_limits(u)
        t, b = UI.analytics(stats, tier, days_left)
        await self.safe_edit(q.message, t, reply_markup=b)

    async def _show_detailed_analytics(self, q):
        u = q.from_user.id

        total_accs = self.db.fetch_one("SELECT COUNT(*) FROM accounts WHERE user_id=?", (u,))[0] or 0
        active_accs = self.db.fetch_one("SELECT COUNT(*) FROM accounts WHERE user_id=? AND is_active=1", (u,))[0] or 0
        inactive = total_accs - active_accs

        broadcasts = self.db.fetch_one("SELECT COUNT(*) FROM broadcasts WHERE user_id=?", (u,))[0] or 0

        last_fail = self.db.fetch_one('''
            SELECT error FROM message_history
            WHERE account_id IN (SELECT account_id FROM accounts WHERE user_id=?)
            AND status='failed' ORDER BY sent_time DESC LIMIT 1
        ''', (u,))
        last_fail_text = last_fail[0][:50] + "..." if last_fail and last_fail[0] else "None"

        totals = self.db.fetch_one('''
            SELECT COALESCE(SUM(total_messages),0), COALESCE(SUM(failed_messages),0)
            FROM accounts WHERE user_id=?
        ''', (u,))
        sent = totals[0] if totals else 0
        failed = totals[1] if totals else 0

        tags = self.db.fetch_one('''
            SELECT COALESCE(SUM(tags_used),0) FROM message_history
            WHERE account_id IN (SELECT account_id FROM accounts WHERE user_id=?)
        ''', (u,))[0] or 0

        stats = {
            'user_id': u,
            'sent': sent,
            'failed': failed,
            'broadcasts': broadcasts,
            'total_accounts': total_accs,
            'active_accounts': active_accs,
            'inactive_accounts': inactive,
            'tags_used': tags,
            'last_failure': last_fail_text
        }

        t, b = UI.detailed_analytics(stats)
        await self.safe_edit(q.message, t, reply_markup=b)

    async def notify_sent(self, user_id: int, group_name: str, account_phone: str = ""):
        try:
            now = datetime.now().strftime("%H:%M:%S")
            acc_note = f"  •  `{account_phone}`" if account_phone else ""
            await self.app.send_message(
                user_id,
                f"📨 **Sent** → **{group_name}**{acc_note}  `{now}`",
                parse_mode=ParseMode.MARKDOWN
            )
        except Exception as e:
            logger.error(f"notify_sent: {e}")

    async def notify_cycle_complete(self, user_id, broadcast_id, sent, failed, interval, failed_groups=None):
        try:
            text = UI.cycle_notification(broadcast_id, sent, failed, interval, failed_groups)
            await self.app.send_message(user_id, text, parse_mode=ParseMode.MARKDOWN)
        except Exception as e:
            logger.error(f"Failed to send cycle notification: {e}")
        # ── Logger: cycle complete ──
        try:
            user_row_c = self.db.fetch_one("SELECT username FROM users WHERE user_id=?", (user_id,))
            asyncio.create_task(self.verx_logger.log_cycle_complete(
                user_id          = user_id,
                username         = (user_row_c[0] or "") if user_row_c else "",
                broadcast_id     = broadcast_id,
                sent             = sent,
                failed           = failed,
                interval_seconds = interval,
            ))
        except Exception:
            pass

    async def notify_tier_granted(self, user_id: int, tier: str, days: int,
                                  granted_by: int = 0):
        try:
            until = datetime.now() + timedelta(days=days)
            total_mins = days * 24 * 60
            badge = "🎗 Elite" if tier == "elite" else "👑 Premium"
            icon = "🎗" if tier == "elite" else "👑"
            perks = (
                "• 10 accounts  •  30 groups  •  20 messages\n"
                "• Custom interval (any seconds)\n"
                "• AI Auto-Reply  •  Custom bio"
            ) if tier == "elite" else (
                "• 3 accounts  •  10 groups  •  5 messages\n"
                "• Preset intervals from 5 min\n"
                "• Member tagging  •  Custom bio"
            )
            await self.app.send_message(
                user_id,
                f"{UI._hdr(icon, badge + ' Granted!')}\n\n"
                f"You have been upgraded to **{badge}**! 🎉\n\n"
                f"⏳ **Duration:** {days} day(s)\n"
                f"🕐 **Remaining:** {format_duration(days * 86400)}\n"
                f"📅 **Expires:** `{until.strftime('%Y-%m-%d %H:%M')}`\n"
                f"{UI.DIVIDER}\n"
                f"**Unlocked features:**\n{perks}",
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton("📊  Open Dashboard", callback_data="dashboard")
                ]]),
                parse_mode=ParseMode.MARKDOWN
            )
            # ── Logger: tier granted ──
            asyncio.create_task(self.verx_logger.log_tier_granted(
                target_user_id = user_id,
                tier           = tier,
                days           = days,
                granted_by     = granted_by,
            ))
        except Exception as e:
            logger.error(f"notify_tier_granted: {e}")

    async def stop(self):
        logger.info("Stopping bot...")
        for bid in list(self.broadcasts.tasks.keys()):
            await self.broadcasts.stop(bid)
        await self.accounts.disconnect_all()
        self.db.close()
        await self.app.stop()
        await self.verx_logger.stop()
        logger.info("Bot stopped gracefully")

    def run(self):
        print("="*50)
        print("🚀 Verx Ads Bot Starting...")
        print("="*50)
        print(f"Owner: @{OWNER_USERNAME}")
        print(f"Support: t.me/verxsupport")
        print(f"Channel: t.me/verxupdates")
        print("="*50)

        async def _daily_reset():
            while True:
                now = datetime.now()
                midnight = (now + timedelta(days=1)).replace(hour=0, minute=0, second=5, microsecond=0)
                await asyncio.sleep((midnight - now).total_seconds())
                self.db.execute("UPDATE accounts SET daily_messages=0")
                logger.info("Daily message counters reset.")
        asyncio.ensure_future(_daily_reset())

        async def _main():
            await self.app.start()
            await self.verx_logger.start()   # ← start VERX Logger Bot
            from pyrogram.types import BotCommand
            try:
                await self.app.set_bot_commands([
                    BotCommand("start",     "Open the bot"),
                    BotCommand("dashboard", "Your dashboard"),
                    BotCommand("help",      "How to use this bot"),
                    BotCommand("status",    "Broadcast status"),
                    BotCommand("mystats",   "Your usage stats"),
                    BotCommand("myplan",    "Your subscription"),
                ])
                logger.info("Bot commands registered.")
            except Exception as _e:
                logger.warning(f"set_bot_commands: {_e}")
            await idle()
            await self.app.stop()

        try:
            self.app.run(_main())
        except Exception:
            raise
        finally:
            try:
                loop = asyncio.get_event_loop()
                if loop.is_running():
                    loop.create_task(self.stop())
                else:
                    loop.run_until_complete(self.stop())
            except Exception:
                pass

# ==================== ENTRY POINT ====================

if __name__ == "__main__":
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    bot = VerxAdsBot()
    bot.run()