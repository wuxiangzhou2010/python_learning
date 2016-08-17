## List comprehensions
```
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
	if word != "the":
		word_lengths.append(len(word))
```
```
sentence = "the quick brown fox jumps overy the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]
```
