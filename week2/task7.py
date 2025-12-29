purchases = input().split()
from collections import Counter
freq = Counter(purchases)
most_popular = max(freq, key=freq.get)
once = [item for item in freq if freq[item] == 1]
sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
print("Purchase frequency:")
for item in sorted(freq.keys()):
    print(f"{item}: {freq[item]}")

print(f"Most popular item: {most_popular}")

print("Purchased once:", ' '.join(sorted(once)))

print("Sorted by frequency:")
for item, count in sorted_items:
    print(item, count)