import os

# AI Models
MODELS = [
    "gemini-flash-lite-latest",
    "gemini-flash-latest",
]

# Gemini API Key
API_KEY = os.environ.get("GEMINI_API_KEY", "")

# Memory
MEMORY_FILE = "data/memory.json"

# Conversation History
MAX_HISTORY = 20

# Voice
VOICE_LANG = "bn"

# Wake Words (ভবিষ্যতের জন্য)
WAKE_WORDS = [
    "hey mubexa",
    "হেই মুবেক্সা",
    "মুবেক্সা",
]

