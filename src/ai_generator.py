"""
AI Generator module for creating daily AI concepts.
Handles communication with Perplexity API.
"""

import re
import time
import requests
from typing import List
from requests.exceptions import RequestException, Timeout


class AIConceptGenerator:
    """Class to generate AI concepts using Perplexity API"""
    
    def __init__(self, api_key: str, api_url: str, model: str,
                 max_tokens: int = 2000, temperature: float = 0.7,
                 max_retries: int = 3, retry_delay: float = 5.0):
        """
        Initialize AI generator
        
        Args:
            api_key: Perplexity API key
            api_url: API endpoint URL
            model: Model name to use
            max_tokens: Maximum tokens for response
            temperature: Temperature for generation
        """
        self.api_key = api_key
        self.api_url = api_url
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.max_retries = max(1, max_retries)
        self.retry_delay = max(0.0, retry_delay)
    
    def _create_prompt(self, previous_concepts: List[str]) -> str:
        """
        Create prompt for generating new concepts
        
        Args:
            previous_concepts: List of previously covered topics
            
        Returns:
            Formatted prompt string
        """
        previous_topics_text = ", ".join(previous_concepts) if previous_concepts else "none"
        
        prompt = f"""Generate 5 new and important concepts in artificial intelligence that have NOT been covered before.

Previously covered topics to AVOID: {previous_topics_text}

For each of the 5 NEW concepts, provide:
1. Concept name (as a clear heading)
2. Clear definition
3. Key points (2-3 bullet points)
4. Practical applications
5. A relevant example

Format each concept clearly with proper headings and structure.
Make the content educational, engaging, and suitable for daily learning.
Ensure all 5 concepts are DIFFERENT from the previously covered topics."""
        
        return prompt
    
    def generate_concepts(self, previous_concepts: List[str]) -> str:
        """
        Generate 5 new AI concepts avoiding duplicates
        
        Args:
            previous_concepts: List of previously covered topics
            
        Returns:
            Generated concepts text
            
        Raises:
            Exception: If API call fails
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        prompt = self._create_prompt(previous_concepts)
        
        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "max_tokens": self.max_tokens,
            "temperature": self.temperature
        }
        
        last_error = None
        for attempt in range(1, self.max_retries + 1):
            try:
                response = requests.post(
                    self.api_url,
                    headers=headers,
                    json=payload,
                    timeout=60
                )

                if response.status_code == 200:
                    result = response.json()
                    content = result.get("choices", [{}])[0].get("message", {}).get("content", "")

                    if not content:
                        raise Exception("No content generated from API")

                    return content
                else:
                    raise Exception(f"API Error ({response.status_code}): {response.text}")

            except (Timeout, RequestException) as error:
                last_error = error
                if attempt < self.max_retries:
                    wait_time = self.retry_delay * attempt
                    print(f"⚠️ API request failed (attempt {attempt}/{self.max_retries}): {error}. Retrying in {wait_time} seconds...")
                    time.sleep(wait_time)
                else:
                    break

        raise Exception(f"Perplexity API request failed after {self.max_retries} attempts: {last_error}")
    
    @staticmethod
    def extract_concept_titles(content: str) -> List[str]:
        """
        Extract concept titles from generated content
        
        Args:
            content: Generated content text
            
        Returns:
            List of extracted concept titles
        """
        lines = content.split('\n')
        concepts = []
        
        banned_titles = {
            "definition",
            "definitions",
            "key points",
            "key point",
            "key takeaways",
            "practical applications",
            "practical application",
            "applications",
            "example",
            "examples",
            "use cases",
            "overview",
            "summary",
            "conclusion",
            "insights",
        }

        for line in lines:
            line = line.strip()
            # Look for headings (lines starting with # or ** or numbered)
            if line and (line.startswith('#') or line.startswith('**') or 
                        (len(line.split()) <= 8 and line[0].isdigit())):
                # Clean the title
                clean_title = (line.replace('#', '')
                                  .replace('*', '')
                                  .replace(':', '')
                                  .strip())
                clean_title = re.sub(r'^\d+[\).\s-]*', '', clean_title).strip()
                
                # Filter reasonable titles
                if 5 < len(clean_title) < 100 and not clean_title.startswith('-'):
                    if clean_title.lower() in banned_titles:
                        continue
                    concepts.append(clean_title)
        
        # Return first 5 unique concepts
        unique_concepts = []
        for concept in concepts:
            if concept not in unique_concepts:
                unique_concepts.append(concept)
            if len(unique_concepts) == 5:
                break
        
        return unique_concepts
