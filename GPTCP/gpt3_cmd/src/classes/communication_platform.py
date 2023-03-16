from typing import List, Dict
from src.Language import Language

class Language:
    def __init__(self, name: str, syntax_mapping: Dict[str, List[str]]):
        self.name = name
        self.syntax_mapping = syntax_mapping

class CommunicationPlatform:
    def __init__(self, languages: List[Language]):
        self.languages = languages

    def translate_message(self, message: str, from_language: Language, to_language: Language) -> str:
        for key, values in from_language.syntax_mapping.items():
            for value in values:
                message = message.replace(value, key)
        for key, values in to_language.syntax_mapping.items():
            for value in values:
                message = message.replace(key, value)
        return message
