"""
AI Insight Daily - A daily AI concepts learning email system.

This package provides automated daily emails with 5 new AI concepts,
avoiding duplicates and presenting information in beautiful HTML format.
"""

__version__ = "1.0.0"
__author__ = "Moussaab Boutelis"

from .config import config
from .storage import ConceptStorage
from .ai_generator import AIConceptGenerator
from .email_template import EmailTemplate
from .email_sender import EmailSender

__all__ = [
    'config',
    'ConceptStorage',
    'AIConceptGenerator',
    'EmailTemplate',
    'EmailSender'
]
