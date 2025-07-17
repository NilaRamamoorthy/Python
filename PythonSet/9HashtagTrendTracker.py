# Daily hashtag sets
monday_tags = {"#AI", "#Python", "#ML", "#Tech"}
tuesday_tags = {"#Python", "#DevOps", "#Cloud", "#Tech"}
wednesday_tags = {"#AI", "#Cloud", "#CyberSecurity", "#Python"}

# Weekly trending set: Combine all tags using update()
weekly_trending = set()
weekly_trending.update(monday_tags, tuesday_tags, wednesday_tags)
print("Weekly Trending Hashtags:", weekly_trending)

# Unique hashtags used only on Monday (not on other days)
unique_monday = monday_tags.difference(tuesday_tags.union(wednesday_tags))
print("Hashtags Unique to Monday:", unique_monday)

# Hashtags used on only one of the three days (symmetric difference)
# Combine pairwise symmetric differences for complete uniqueness
unique_one_day = monday_tags ^ tuesday_tags ^ wednesday_tags
print("Hashtags Used on Only One Day:", unique_one_day)
