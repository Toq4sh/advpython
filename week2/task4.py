n, m = map(int, input().split())
s = input().strip()
assert len(s) == n
unique_words = set()
for i in range(n - m + 1):
    substring = s[i:i + m]
    unique_words.add(substring)

print(len(unique_words))