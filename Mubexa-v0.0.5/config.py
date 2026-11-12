import os

# ==========================
# Mubexa AI Configuration
# ==========================

# Gemini Models
MODELS = [
    "gemini-flash-lite-latest",
    "gemini-flash-latest"
]

# API Key
API_KEY = os.environ.get("GEMINI_API_KEY", "")

# Memory File
MEMORY_FILE = "data/memory.json"

# Conversation
MAX_HISTORY = 20

# Voice
VOICE_LANG = "bn"

# Wake Word (ভবিষ্যতের জন্য)
WAKE_WORDS = [
    "hey mubexa",
    "hey",
    "হেই মুবেক্সা",
    "মুবেক্সা"
]
