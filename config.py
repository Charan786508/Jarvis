# Configuration settings for Jarvis Voice Assistant

API_KEYS = {
    'google': 'YOUR_GOOGLE_API_KEY',
    'weather': 'YOUR_WEATHER_API_KEY',
    'music': 'YOUR_MUSIC_API_KEY'
}

TIMEOUTS = {
    'default': 5,  # Default timeout in seconds
    'long': 15     # Long timeout for certain commands
}

COMMAND_MAPPINGS = {
    'greet': 'Hello, how can I help you?',
    'weather': 'Get weather information',
    'music': 'Play some music',
    'info': 'Provide information'
}