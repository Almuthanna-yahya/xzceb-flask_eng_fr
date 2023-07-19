"""
#Module: translator
This module provides a function for translating English text 
to French using and French to English the MyMemoryTranslator API.
"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text: str) -> str:
    """Translates English text to French 
    using the MyMemoryTranslator API."""
    try:
        return MyMemoryTranslator(source="en", target="fr").translate(english_text)
    except Exception as snake_case:
        return f"Translation Error: {str(snake_case)}"

def french_to_english(french_text: str) -> str:
    """Translates French text to English 
    using the MyMemoryTranslator API."""
    try:
        return MyMemoryTranslator(source="fr", target="en").translate(french_text)
    except Exception as snake_case:
        return f"Translation Error: {str(snake_case)}"