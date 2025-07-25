class WordSplitterIterator:
    def __init__(self, sentence):
        self.words = sentence.split()
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        w = self.words[self.index]
        self.index += 1
        return w

# Demo:
sentence = "This is a sample sentence"
print("19 words:", list(WordSplitterIterator(sentence)))
# Output: ['This', 'is', 'a', 'sample', 'sentence']
