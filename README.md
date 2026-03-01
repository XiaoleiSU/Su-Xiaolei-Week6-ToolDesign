# Keyword Extraction Tool

## What It Does

Extracts the most frequent keywords from English text using simple frequency analysis.

**Input:** Text string + number of keywords to extract  
**Output:** Top keywords with occurrence counts, plus word statistics

```python
from tool import extract_keywords

result = extract_keywords("Python is great. Python is easy.", top_n=3)
# Returns: {'keywords': [{'word': 'python', 'count': 2}, ...], 
#           'total_words': 4, 'unique_words': 3, 'top_n': 3}
```

## How to Run the Demo

```bash
python demo.py
```

Shows 5 scenarios: technical articles, news, short text, error cases, and product reviews.

## Design Decisions

**Why frequency-based approach?**
- No external dependencies (uses only Python standard library)
- Fast processing without ML overhead
- Simple and transparent logic
- Effective for articles, reviews, and short documents

**Stop word selection:**
- 60+ common English function words based on standard NLP practice
- Removes high-frequency, low-meaning words (the, and, is, etc.)

**Error handling:**
- Returns structured error messages instead of raising exceptions
- Validates input types and empty text
- Handles edge cases gracefully

## Limitations

1. **English only** - Stop words optimized for English text
2. **No semantic understanding** - Can't distinguish word meanings by context
3. **Single words only** - Doesn't extract multi-word phrases
4. **Simple frequency** - Doesn't use TF-IDF or document-level weighting