# Models
DEFAULT_MODEL = "claude-haiku-4-5"
FAST_MODEL = "claude-haiku-4-5"
SMART_MODEL = "claude-sonnet-4-6"
POWERFUL_MODEL = "claude-opus-4-6"

# Gemini
GEMINI_DEFAULT = "gemini-1.5-flash"
GEMINI_PRO = "gemini-1.5-pro"

# Groq
GROQ_DEFAULT = "llama-3.3-70b-versatile"
GROQ_FAST = "gemma2-9b-it"

# Chat
MAX_HISTORY = 10
MAX_TOKENS_CHEAP = 500
MAX_TOKENS_SMART = 1024
MAX_TOKENS_POWERFUL = 4096

# Routing
SHORT_CONVERSATION = 5
LONG_CONVERSATION = 15

# App
APP_VERSION = "1.0.0"
TEMPERATURE = 0.7

# AI Provider
AI_PROVIDER = "groq"  # only "gemini" for now

# Gemini Model (FREE)
GEMINI_MODEL = "gemini-1.5-flash"

# System Prompt
SYSTEM_PROMPT = """
You are a helpful business assistant.
You are friendly, professional and concise.
If you know the customer's name, use it naturally in conversation.
Help customers with enquiries, orders and payments.
"""