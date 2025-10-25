"""
Configuration module for AI Insight Daily project.
Handles environment variables and project settings.
"""

import os


class Config:
    """Configuration class to store all project settings"""
    
    def __init__(self):
        """Initialize configuration from environment variables"""
        self.perplexity_api_key = os.getenv('PERPLEXITY_API_KEY')
        self.from_email = os.getenv('FROM_EMAIL')
        self.to_email = os.getenv('TO_EMAIL')
        self.app_password = os.getenv('APP_PASSWORD')
        
        # API Configuration
        self.api_base_url = "https://api.perplexity.ai/chat/completions"
        self.model_name = "sonar"
        self.max_tokens = 2000
        self.temperature = 0.7
        
        # Email Configuration
        self.smtp_server = 'smtp.gmail.com'
        self.smtp_port = 465
        self.email_subject = "🤖 AI Insight Daily: 5 Concepts, 5 Minutes"
        
        # Storage Configuration
        self.storage_file = 'data/sent_concepts.json'
        self.max_stored_concepts = 100  # Keep last 100 concepts
    
    def validate(self):
        """Validate that all required environment variables are set"""
        required_vars = {
            'PERPLEXITY_API_KEY': self.perplexity_api_key,
            'FROM_EMAIL': self.from_email,
            'TO_EMAIL': self.to_email,
            'APP_PASSWORD': self.app_password
        }
        
        missing_vars = [var for var, value in required_vars.items() if not value]
        
        if missing_vars:
            raise ValueError(
                f"Missing required environment variables: {', '.join(missing_vars)}"
            )
        
        return True


# Create a global config instance
config = Config()
