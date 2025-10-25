"""
Storage module for tracking sent AI concepts.
Handles reading and writing concept history to JSON file.
"""

import json
import os
from typing import List


class ConceptStorage:
    """Class to manage storage of sent concepts"""
    
    def __init__(self, storage_file: str):
        """
        Initialize storage with file path
        
        Args:
            storage_file: Path to JSON file storing sent concepts
        """
        self.storage_file = storage_file
        self._ensure_storage_exists()
    
    def _ensure_storage_exists(self):
        """Create storage directory and file if they don't exist"""
        # Create directory if it doesn't exist
        directory = os.path.dirname(self.storage_file)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        
        # Create empty file if it doesn't exist
        if not os.path.exists(self.storage_file):
            self.save_concepts([])
    
    def load_concepts(self) -> List[str]:
        """
        Load previously sent concepts from storage
        
        Returns:
            List of previously sent concept titles
        """
        try:
            with open(self.storage_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data if isinstance(data, list) else []
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def save_concepts(self, concepts: List[str]):
        """
        Save concepts list to storage
        
        Args:
            concepts: List of concept titles to save
        """
        with open(self.storage_file, 'w', encoding='utf-8') as f:
            json.dump(concepts, f, indent=2, ensure_ascii=False)
    
    def add_concepts(self, new_concepts: List[str], max_stored: int = 100):
        """
        Add new concepts to storage, maintaining maximum storage limit
        
        Args:
            new_concepts: List of new concept titles to add
            max_stored: Maximum number of concepts to keep in storage
        """
        existing_concepts = self.load_concepts()
        updated_concepts = existing_concepts + new_concepts
        
        # Keep only the most recent concepts
        if len(updated_concepts) > max_stored:
            updated_concepts = updated_concepts[-max_stored:]
        
        self.save_concepts(updated_concepts)
    
    def get_recent_concepts(self, count: int = 50) -> List[str]:
        """
        Get the most recent concepts for duplicate avoidance
        
        Args:
            count: Number of recent concepts to retrieve
            
        Returns:
            List of recent concept titles
        """
        concepts = self.load_concepts()
        return concepts[-count:] if concepts else []
