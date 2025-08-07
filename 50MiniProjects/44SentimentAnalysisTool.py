from textblob import TextBlob
import os
import functools
import json
import time

def cache_results(func):
    """
    Decorator that caches sentiment results to a file,
    avoiding repeated API use or heavy recomputation.
    """
    @functools.wraps(func)
    def wrapper(self, texts):
        cache_path = self.cache_file
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        try:
            with open(cache_path, 'r', encoding='utf-8') as f:
                cache = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            cache = {}

        results = {}
        new_texts = []
        for text in texts:
            key = text.strip()
            if key in cache:
                results[key] = cache[key]
            else:
                new_texts.append(key)

        if new_texts:
            try:
                computed = func(self, new_texts)
                cache.update(computed)
                with open(cache_path, 'w', encoding='utf-8') as f:
                    json.dump(cache, f, ensure_ascii=False, indent=2)
            except Exception as e:
                print(f"[cache_results] Error: {e}")
                computed = {}
            results.update(computed)

        # return results in same order as input
        return [(text, results[text.strip()]) for text in texts]
    return wrapper

class Analyzer:
    def __init__(self, cache_file='cache/sentiment_cache.json'):
        self.cache_file = cache_file

    @cache_results
    def analyze_batch(self, texts):
        """
        Process a batch of texts and return a dict mapping text to sentiment dicts.
        """
        results = {}
        for text in texts:
            try:
                blob = TextBlob(text)
                polarity = blob.sentiment.polarity
                subjectivity = blob.sentiment.subjectivity
                results[text] = {
                    'polarity': polarity,
                    'subjectivity': subjectivity,
                    'label': self._label(polarity),
                }
            except Exception as e:
                print(f"[Error] analyzing text '{text}': {e}")
                results[text] = {'polarity': None, 'subjectivity': None, 'label': 'error'}
        return results

    def _label(self, polarity: float) -> str:
        if polarity is None:
            return 'error'
        if polarity > 0:
            return 'positive'
        elif polarity < 0:
            return 'negative'
        else:
            return 'neutral'

    def analyze(self, texts):
        """
        Public method: yields (text, sentiment_info) tuples.
        """
        batch = self.analyze_batch(texts)
        for original, info in batch:
            yield original, info

if __name__ == "__main__":
    texts = [
        "I love this product!",
        "This was the worst experience ever.",
        "It was okay, nothing special.",
        "I love this product!"  # duplicate to test cache
    ]
    analyzer = Analyzer()

    print("Sentiment Analysis Results:\n")
    for txt, info in analyzer.analyze(texts):
        print(f"• \"{txt}\" → {info['label']}, polarity={info['polarity']:.3f}, subj={info['subjectivity']:.3f}")
