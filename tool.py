"""
Keyword Extraction Tool

This module provides functionality to extract keywords from text using
frequency-based heuristic methods.
"""

import re
from typing import Dict, List, Union
from collections import Counter


# Common English stop words to filter out
STOP_WORDS = {
    'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
    'of', 'with', 'by', 'from', 'as', 'is', 'was', 'are', 'were', 'been',
    'be', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would',
    'could', 'should', 'may', 'might', 'can', 'this', 'that', 'these',
    'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'what', 'which',
    'who', 'when', 'where', 'why', 'how', 'all', 'each', 'every', 'both',
    'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not',
    'only', 'own', 'same', 'so', 'than', 'too', 'very', 'just', 'about',
    'into', 'through', 'during', 'before', 'after', 'above', 'below',
    'between', 'under', 'again', 'further', 'then', 'once'
}


def extract_keywords(text: str, top_n: int = 5) -> Dict[str, Union[List[Dict[str, Union[str, int]]], int]]:
    """
    Extract keywords from text using frequency-based analysis.
    
    This function analyzes the input text and extracts the most frequently
    occurring words (keywords) after filtering out stop words and applying
    basic text preprocessing.
    
    Args:
        text (str): The input text to extract keywords from.
        top_n (int, optional): The number of top keywords to return. 
                               Defaults to 5.
    
    Returns:
        dict: A dictionary containing:
            - keywords (list): List of dictionaries with 'word' and 'count' keys,
                              sorted by frequency in descending order.
            - total_words (int): Total number of words in the text after preprocessing.
            - unique_words (int): Number of unique words after preprocessing.
            - top_n (int): The requested number of keywords.
            
            If an error occurs, returns:
            - error (str): Error message describing what went wrong.
            - keywords (list): Empty list.
            - total_words (int): 0
            - unique_words (int): 0
            - top_n (int): The requested number of keywords.
    
    Examples:
        >>> result = extract_keywords("Python is a great programming language. Python is easy to learn.")
        >>> print(result['keywords'])
        [{'word': 'python', 'count': 2}, {'word': 'programming', 'count': 1}, ...]
        
        >>> result = extract_keywords("", top_n=10)
        >>> print(result['error'])
        'Input text is empty'
    
    Raises:
        No exceptions are raised. All errors are caught and returned in the result dictionary.
    """
    try:
        # Input validation: Check if text is a string
        if not isinstance(text, str):
            return {
                "error": f"Input must be a string, got {type(text).__name__}",
                "keywords": [],
                "total_words": 0,
                "unique_words": 0,
                "top_n": top_n
            }
        
        # Input validation: Check if text is empty
        if not text or text.strip() == "":
            return {
                "error": "Input text is empty",
                "keywords": [],
                "total_words": 0,
                "unique_words": 0,
                "top_n": top_n
            }
        
        # Validate top_n parameter
        if not isinstance(top_n, int) or top_n < 1:
            return {
                "error": "top_n must be a positive integer",
                "keywords": [],
                "total_words": 0,
                "unique_words": 0,
                "top_n": top_n
            }
        
        # Extract words using regex (alphanumeric characters only)
        words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
        
        # Filter words: remove stop words and words with length < 2
        filtered_words = [
            word for word in words 
            if word not in STOP_WORDS and len(word) >= 2
        ]
        
        # Handle case where no valid words remain after filtering
        if not filtered_words:
            return {
                "keywords": [],
                "total_words": 0,
                "unique_words": 0,
                "top_n": top_n
            }
        
        # Count word frequencies
        word_counts = Counter(filtered_words)
        
        # Get top N keywords sorted by frequency (descending order)
        top_keywords = word_counts.most_common(top_n)
        
        # Format the result
        keywords_list = [
            {"word": word, "count": count} 
            for word, count in top_keywords
        ]
        
        return {
            "keywords": keywords_list,
            "total_words": len(filtered_words),
            "unique_words": len(word_counts),
            "top_n": top_n
        }
    
    except Exception as e:
        # Catch any unexpected errors and return structured error information
        return {
            "error": f"Unexpected error occurred: {str(e)}",
            "keywords": [],
            "total_words": 0,
            "unique_words": 0,
            "top_n": top_n
        }


if __name__ == "__main__":
    # Example usage and testing
    sample_text = """
    Python is a high-level programming language. Python is widely used for 
    web development, data analysis, artificial intelligence, and scientific 
    computing. Python's syntax is clean and easy to learn. Many developers 
    love Python because of its simplicity and powerful libraries.
    """
    
    result = extract_keywords(sample_text, top_n=5)
    
    print("Keyword Extraction Results:")
    print("=" * 50)
    
    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print(f"Total words: {result['total_words']}")
        print(f"Unique words: {result['unique_words']}")
        print(f"\nTop {result['top_n']} keywords:")
        for i, kw in enumerate(result['keywords'], 1):
            print(f"  {i}. {kw['word']}: {kw['count']} occurrences")
