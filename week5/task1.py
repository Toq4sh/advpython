import string

def analyze_text():
    with open("text.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    line_count = len(lines)
    word_count = 0
    freq = {}

    for line in lines:
        line = line.lower().translate(str.maketrans("", "", string.punctuation))
        words = line.split()
        word_count += len(words)
        for w in words:
            freq[w] = freq.get(w, 0) + 1

    with open("analysis.txt", "w", encoding="utf-8") as f:
        f.write(f"Lines: {line_count}\n")
        f.write(f"Words: {word_count}\n")
        f.write("Word frequency:\n")
        for k, v in freq.items():
            f.write(f"{k}: {v}\n")

analyze_text()
