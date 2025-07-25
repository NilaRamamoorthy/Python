class NewsPaginator:
    def __init__(self, headlines, per_page=3):
        self.headlines = headlines
        self.per_page = per_page
        self.total_pages = (len(headlines) - 1) // per_page + 1
        self.page = 0  # zero-based page index

    def __iter__(self):
        return self

    def __next__(self):
        if self.page >= self.total_pages:
            raise StopIteration
        start = self.page * self.per_page
        end = start + self.per_page
        page_data = self.headlines[start:end]
        self.page += 1
        return page_data

    def prev(self):
        if self.page <= 1:
            return []
        # step back two pages, so that __next__ returns the current previous page
        self.page -= 2
        return self.__next__()
headlines = [f"Headline {i}" for i in range(1, 11)]
p = NewsPaginator(headlines, per_page=3)

print("Page 1:", next(p))
# Page 1: ['Headline 1', 'Headline 2', 'Headline 3']

print("Page 2:", next(p))
# Page 2: ['Headline 4', 'Headline 5', 'Headline 6']

print("Back to Page 1:", p.prev())
# Back to Page 1: ['Headline 1', 'Headline 2', 'Headline 3']

print("Next Page (should be Page 2):", next(p))
# Next Page: ['Headline 4', 'Headline 5', 'Headline 6']

print("Remaining pages:")
for pg in p:
    print(pg)
# ['Headline 7', 'Headline 8', 'Headline 9']
# ['Headline 10']

