"""
Demo script showing the keyword extraction tool being called by an agent/workflow.

This demonstrates how an AI agent or automated workflow can use the tool
to analyze text and make decisions based on the extracted keywords.
"""

from tool import extract_keywords


class ContentAnalysisAgent:
    """
    An agent that analyzes content and makes decisions based on keyword extraction.
    Simulates an AI agent or workflow system calling the tool.
    """
    
    def __init__(self, name: str):
        self.name = name
        self.analysis_count = 0
    
    def analyze_content(self, text: str, top_n: int = 5, task: str = "general"):
        """
        Agent analyzes content by calling the keyword extraction tool.
        
        Args:
            text: Content to analyze
            top_n: Number of keywords to extract
            task: Type of analysis task
        """
        self.analysis_count += 1
        
        print(f"\n{'='*70}")
        print(f"[AGENT: {self.name}] Task #{self.analysis_count}: {task}")
        print(f"{'='*70}")
        print(f"[AGENT] Calling keyword extraction tool...")
        print(f"[AGENT] Parameters: top_n={top_n}")
        
        # Agent calls the tool
        result = extract_keywords(text, top_n=top_n)
        
        # Agent processes the result
        if "error" in result:
            print(f"[AGENT] Tool returned error: {result['error']}")
            print(f"[AGENT] Decision: Skip this content")
            return None
        
        print(f"[AGENT] Tool execution successful!")
        print(f"[AGENT] Received {len(result['keywords'])} keywords from {result['total_words']} words")
        
        # Display results
        print(f"\n[RESULTS] Top {result['top_n']} Keywords:")
        print("-" * 70)
        for i, kw in enumerate(result['keywords'], 1):
            bar = "#" * min(kw['count'] * 2, 40)
            print(f"  {i}. {kw['word']:<15} | {kw['count']:>3} occurrences | {bar}")
        
        # Agent makes decisions based on keywords
        self._make_decision(result, task)
        
        return result
    
    def _make_decision(self, result: dict, task: str):
        """Agent makes decisions based on extracted keywords."""
        print(f"\n[AGENT] Making decision based on keywords...")
        
        keywords = [kw['word'] for kw in result['keywords']]
        
        if task == "content_categorization":
            if any(word in keywords for word in ['machine', 'learning', 'data', 'algorithm']):
                print(f"[AGENT] Decision: Categorize as 'Technology/AI'")
            elif any(word in keywords for word in ['climate', 'weather', 'energy']):
                print(f"[AGENT] Decision: Categorize as 'Environment'")
            else:
                print(f"[AGENT] Decision: Categorize as 'General'")
        
        elif task == "sentiment_analysis":
            positive_words = ['great', 'excellent', 'amazing', 'good', 'best']
            if any(word in keywords for word in positive_words):
                print(f"[AGENT] Decision: Positive sentiment detected")
            else:
                print(f"[AGENT] Decision: Neutral sentiment")
        
        elif task == "quality_check":
            if result['unique_words'] < 5:
                print(f"[AGENT] Decision: Content too simple, needs enrichment")
            else:
                print(f"[AGENT] Decision: Content quality acceptable")


def workflow_scenario_1():
    """Workflow: Content categorization system"""
    print("\n" + "="*70)
    print(" WORKFLOW SCENARIO 1: Automated Content Categorization")
    print("="*70)
    
    agent = ContentAnalysisAgent("ContentCategorizer")
    
    # Document 1: Technical article
    doc1 = """
    Machine learning is transforming the technology industry. Deep learning
    uses neural networks to process data. Artificial intelligence and machine
    learning are revolutionizing healthcare, finance, and transportation.
    """
    agent.analyze_content(doc1, top_n=5, task="content_categorization")
    
    # Document 2: Environmental article
    doc2 = """
    Climate change continues to impact global weather patterns. Scientists
    warn that rising temperatures are causing extreme weather events.
    Renewable energy sources like solar and wind power are becoming important.
    """
    agent.analyze_content(doc2, top_n=5, task="content_categorization")


def workflow_scenario_2():
    """Workflow: Product review analysis"""
    print("\n" + "="*70)
    print(" WORKFLOW SCENARIO 2: Product Review Sentiment Analysis")
    print("="*70)
    
    agent = ContentAnalysisAgent("ReviewAnalyzer")
    
    review = """
    This smartphone has an amazing camera. The battery life is excellent,
    lasting all day. The display is bright and vibrant. Performance is smooth
    and fast. The camera quality exceeds expectations. Great value for money.
    """
    agent.analyze_content(review, top_n=8, task="sentiment_analysis")


def workflow_scenario_3():
    """Workflow: Content quality checker"""
    print("\n" + "="*70)
    print(" WORKFLOW SCENARIO 3: Content Quality Validation")
    print("="*70)
    
    agent = ContentAnalysisAgent("QualityChecker")
    
    # Good content
    content1 = "Python programming is fun. Python is powerful and versatile for development."
    agent.analyze_content(content1, top_n=3, task="quality_check")
    
    # Poor content (only stop words)
    content2 = "the a an and or but in on at to for"
    agent.analyze_content(content2, top_n=3, task="quality_check")


def workflow_scenario_4():
    """Workflow: Error handling in automated pipeline"""
    print("\n" + "="*70)
    print(" WORKFLOW SCENARIO 4: Error Handling in Pipeline")
    print("="*70)
    
    agent = ContentAnalysisAgent("PipelineProcessor")
    
    # Test various error cases
    print("\n[WORKFLOW] Processing batch of documents...")
    
    documents = [
        ("", "Empty document"),
        (12345, "Invalid type document"),
        ("Python is great for programming", "Valid document")
    ]
    
    for i, (doc, desc) in enumerate(documents, 1):
        print(f"\n[WORKFLOW] Processing document {i}: {desc}")
        result = agent.analyze_content(doc, top_n=3, task="general")
        if result:
            print(f"[WORKFLOW] Document {i} processed successfully")
        else:
            print(f"[WORKFLOW] Document {i} skipped due to error")


def main():
    """Run all workflow scenarios demonstrating agent/tool interaction."""
    print("\n" + "="*70)
    print("  KEYWORD EXTRACTION TOOL - AGENT/WORKFLOW DEMONSTRATION")
    print("="*70)
    print("\nThis demo shows how an AI agent or automated workflow")
    print("calls the keyword extraction tool to analyze content.")
    
    # Run workflow scenarios
    workflow_scenario_1()
    workflow_scenario_2()
    workflow_scenario_3()
    workflow_scenario_4()
    
    # Summary
    print("\n" + "="*70)
    print(" DEMONSTRATION COMPLETE")
    print("="*70)
    print("\n[SUMMARY] The tool was successfully called by agents in 4 workflows:")
    print("  1. Content categorization (2 documents)")
    print("  2. Sentiment analysis (1 review)")
    print("  3. Quality validation (2 contents)")
    print("  4. Error handling pipeline (3 documents)")
    print("\nThe tool integrates seamlessly into agent-based systems!")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
