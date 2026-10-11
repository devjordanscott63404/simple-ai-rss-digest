import datetime
import re
from dataclasses import dataclass

# Sample RSS-like data (replace with real feed fetching)
SAMPLE_FEEDS = [
    {'title': 'New AI model achieves SOTA on benchmark', 'source': 'AI News'},
    {'title': 'Open-source finance tracker gains popularity', 'source': 'Tech Weekly'},
    {'title': 'Type-safe LLM libraries trending on GitHub', 'source': 'Dev Digest'},
    {'title': 'Daily standup best practices for remote teams', 'source': 'Management Blog'},
    {'title': 'AI interview prep guide released', 'source': 'Career Insights'},
]

# Keyword-based scoring for "hot" items (simulated AI curation)
HOT_KEYWORDS = ['ai', 'llm', 'open-source', 'github', 'trend', 'new', 'sota', 'fintech']

def score_article(article: dict) -> int:
    title = article['title'].lower()
    score = sum(1 for kw in HOT_KEYWORDS if kw in title)
    return score

@dataclass
class Digest:
    date: str
    items: list

def generate_daily_digest(feeds: list) -> Digest:
    # Filter & rank by score, then take top 3
    ranked = sorted(feeds, key=score_article, reverse=True)
    hot_items = [a for a in ranked if score_article(a) > 0][:3]
    return Digest(date=datetime.date.today().isoformat(), items=hot_items)

def format_digest(digest: Digest) -> str:
    lines = [f"Daily AI Hot Digest - {digest.date}", "---"]
    for i, item in enumerate(digest.items, 1):
        lines.append(f"{i}. [{item['source']}] {item['title']}")
    return "\n".join(lines)

if __name__ == '__main__':
    digest = generate_daily_digest(SAMPLE_FEEDS)
    print(format_digest(digest))
    print("\n(Simple demo: replace SAMPLE_FEEDS with real RSS/API data)")