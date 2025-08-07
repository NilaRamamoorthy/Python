import os
import difflib

class PlagiarismChecker:
    def __init__(self, directory):
        self.directory = directory
        self.documents = []  # list of (filename, content)

    def load_documents(self):
        """Load all text files in the directory."""
        if not os.path.isdir(self.directory):
            raise FileNotFoundError(f"Directory not found: {self.directory}")
        for fname in os.listdir(self.directory):
            if fname.lower().endswith('.txt'):
                path = os.path.join(self.directory, fname)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        text = f.read()
                        if not text.strip():
                            raise ValueError("Empty document")
                        self.documents.append((fname, text))
                except Exception as e:
                    print(f"[Warning] Skipped '{fname}': {e}")

    def compare_pair(self, doc1, doc2):
        """Return similarity ratio between two document strings."""
        name1, text1 = doc1
        name2, text2 = doc2
        ratio = difflib.SequenceMatcher(None, text1, text2).ratio()
        return name1, name2, ratio

    def find_similar(self, threshold=0.75):
        """
        Generator yielding pairs of documents with similarity above threshold.
        """
        docs = self.documents
        for i in range(len(docs)):
            for j in range(i + 1, len(docs)):
                name1, name2, ratio = self.compare_pair(docs[i], docs[j])
                if ratio >= threshold:
                    yield name1, name2, ratio

if __name__ == "__main__":
    directory = input("Enter directory containing .txt files: ").strip()
    checker = PlagiarismChecker(directory)
    try:
        checker.load_documents()
    except FileNotFoundError as fnf:
        print(fnf)
        exit(1)

    print("\nPotential plagiarism matches (ratio ≥ 75%):\n")
    for doc1, doc2, sim in checker.find_similar(threshold=0.75):
        print(f" • {doc1} ↔ {doc2}: {sim:.2%}")
