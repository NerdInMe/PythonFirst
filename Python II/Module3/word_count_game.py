# This simple program counts duplicate words in a sentence using dictinary
text = (
    "Peter Piper picked a peck of pickled peppers "
    "A peck of pickled peppers Peter Piper picked "
    "if Peter Piper picked a peck of pickled peppers "
    "Where is the peck of pickled peppers Peter Piper picked"
)

# Convert everything to lowercase and split into words: list of strings.
words = text.lower().split()

# Create an empty dictionary to hold counts and use for loop to count the words.
counts = {}
for w in words:
    if w in counts:
        counts[w] += 1
    else:
        counts[w] = 1
print(counts)
# find words that appeared more than once.
duplicates = {}
for w, c in counts.items():
    if c > 1:
        duplicates[w] = c

# Print the result
print(f"Words \t Count \n")
for w, c in duplicates.items():
    print(f"{w} \t {c}")

