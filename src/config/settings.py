from dotenv import load_dotenv
import os

load_dotenv()

# App
APP_NAME = os.getenv("APP_NAME", "Business AI Assistant")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# Groq
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Google
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Redis
REDIS_URL = os.getenv("REDIS_URL")
REDIS_TOKEN = os.getenv("REDIS_TOKEN")

# WhatsApp
WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
WHATSAPP_VERIFY_TOKEN = os.getenv("WHATSAPP_VERIFY_TOKEN")
WHATSAPP_PHONE_NUMBER_ID = os.getenv("WHATSAPP_PHONE_NUMBER_ID")
WHATSAPP_BUSINESS_NUMBER_ID = os.getenv("WHATSAPP_BUSINESS_NUMBER_ID")