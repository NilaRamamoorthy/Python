import os

class TxtFileScanner:
    def __init__(self, root_path, limit=None):
        self.root_path = root_path
        self.limit = limit
        self.count = 0
        self.it = self._scanner()

    def __iter__(self):
        return self

    def __next__(self):
        if self.limit and self.count >= self.limit:
            raise StopIteration
        file_path = next(self.it)  # may raise StopIteration
        self.count += 1
        return file_path

    def _scanner(self):
        for root, dirs, files in os.walk(self.root_path):
            for fname in files:
                if fname.endswith('.txt'):  # filter text files
                    yield os.path.join(root, fname)

scanner = TxtFileScanner('/path/to/dir', limit=5)
print("First up to 5 .txt files:")
for fp in scanner:
    print(fp)
