"""
#Module: translator
This module provides a function for translating English text 
to French using the MyMemoryTranslator API.
"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text: str) -> str:
    """Translates English text to French 
    using the MyMemoryTranslator API."""
    try:
        return MyMemoryTranslator(source="en", target="fr").translate(english_text)
    except Exception as snake_case:
        return f"Translation Error: {str(snake_case)}"
