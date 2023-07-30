"""This module helps us translate the strings from one language to another."""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """This function translates English strings into French."""
    french_text = MyMemoryTranslator(source = "en-GB", target = "fr-FR").translate(english_text)
    return french_text

def french_to_english(french_text):
    """This function translates French strings into English."""
    english_text = MyMemoryTranslator(source = "fr-FR", target = "en-GB").translate(french_text)
    return english_text
