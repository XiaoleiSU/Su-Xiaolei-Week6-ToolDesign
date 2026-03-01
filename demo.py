"""
Demo script for the keyword extraction tool.

This script demonstrates various usage scenarios including normal cases
and error handling.
"""

from tool import extract_keywords


def print_separator(title: str = "") -> None:
    """Print a formatted separator line."""
    print("\n" + "=" * 70)
    if title:
        print(f" {title}")
        print("=" * 70)


def print_result(result: dict) -> None:
    """Print the extraction result in a formatted way."""
    if "error" in result:
        print(f"[ERROR] {result['error']}")
    else:
        print(f"[OK] Total words processed: {result['total_words']}")
        print(f"[OK] Unique words found: {result['unique_words']}")
        print(f"\nTop {result['top_n']} Keywords:")
        print("-" * 40)
        for i, kw in enumerate(result['keywords'], 1):
            bar = "#" * (kw['count'] * 2)
            print(f"  {i}. {kw['word']:<15} | {kw['count']:>3} times | {bar}")
    print()


def demo_1_technical_article():
    """Demo 1: Extract keywords from a technical article."""
    print_separator("Demo 1: Technical Article Analysis")
    
    text = """
    Machine learning is transforming the technology industry. Deep learning,
    a subset of machine learning, uses neural networks to process data.
    Artificial intelligence and machine learning are revolutionizing healthcare,
    finance, and transportation. Data scientists use machine learning algorithms
    to build predictive models and extract insights from large datasets.
    """
    
    print("Input text:")
    print(text.strip())
    print("\nExtracting top 8 keywords...")
    
    result = extract_keywords(text, top_n=8)
    print_result(result)


def demo_2_news_article():
    """Demo 2: Extract keywords from a news article."""
    print_separator("Demo 2: News Article Analysis")
    
    text = """
    Climate change continues to impact global weather patterns. Scientists
    warn that rising temperatures are causing more extreme weather events.
    Governments worldwide are implementing policies to reduce carbon emissions
    and combat climate change. Renewable energy sources like solar and wind
    power are becoming increasingly important in the fight against climate change.
    """
    
    print("Input text:")
    print(text.strip())
    print("\nExtracting top 5 keywords...")
    
    result = extract_keywords(text, top_n=5)
    print_result(result)


def demo_3_short_text():
    """Demo 3: Extract keywords from a short text."""
    print_separator("Demo 3: Short Text Analysis")
    
    text = "Python programming is fun. Python is powerful and versatile."
    
    print(f"Input text: {text}")
    print("\nExtracting top 3 keywords...")
    
    result = extract_keywords(text, top_n=3)
    print_result(result)


def demo_4_error_cases():
    """Demo 4: Demonstrate error handling."""
    print_separator("Demo 4: Error Handling Demonstrations")
    
    # Test case 1: Empty string
    print("Test 1: Empty string input")
    print("Input: ''")
    result = extract_keywords("", top_n=5)
    print_result(result)
    
    # Test case 2: Non-string input
    print("\nTest 2: Non-string input (integer)")
    print("Input: 12345")
    result = extract_keywords(12345, top_n=5)
    print_result(result)
    
    # Test case 3: Text with only stop words
    print("\nTest 3: Text with only stop words")
    text = "the a an and or but in on at to for of with"
    print(f"Input: '{text}'")
    result = extract_keywords(text, top_n=5)
    print_result(result)
    
    # Test case 4: Invalid top_n parameter
    print("\nTest 4: Invalid top_n parameter (negative number)")
    text = "Python is great for programming"
    print(f"Input: '{text}' with top_n=-5")
    result = extract_keywords(text, top_n=-5)
    print_result(result)


def demo_5_custom_scenario():
    """Demo 5: Custom scenario - Product review analysis."""
    print_separator("Demo 5: Product Review Analysis")
    
    text = """
    This smartphone has an amazing camera. The battery life is excellent,
    lasting all day with heavy usage. The display is bright and vibrant.
    Performance is smooth and fast. The camera quality exceeds expectations.
    Overall, this phone offers great value for money. Highly recommend this
    smartphone for anyone looking for a reliable device with excellent camera
    and battery performance.
    """
    
    print("Input text (Product Review):")
    print(text.strip())
    print("\nExtracting top 10 keywords...")
    
    result = extract_keywords(text, top_n=10)
    print_result(result)


def main():
    """Run all demo scenarios."""
    print("\n" + "█" * 70)
    print("  KEYWORD EXTRACTION TOOL - DEMONSTRATION")
    print("█" * 70)
    
    # Run all demos
    demo_1_technical_article()
    demo_2_news_article()
    demo_3_short_text()
    demo_4_error_cases()
    demo_5_custom_scenario()
    
    # Summary
    print_separator("Demo Complete")
    print("All demonstration scenarios have been executed successfully!")
    print("The tool handles both normal inputs and error cases gracefully.")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
