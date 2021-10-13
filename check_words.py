def longest_words():
    max_len=0
    with open(r"C:\Users\epy12\miniProject1\file.txt") as f:
        words = f.read().split()
    max_len = len(max(words, key=len))
    #return [word for word in words if len(word) == max_len]
    return max_len


def word_count():
    Count = 0

    with open(r"C:\Users\epy12\miniProject1\file.txt") as f:
        data= f.readlines()
        for line in data:
            words = line.split()
            for word in words:
                if word == "Epy":
                    Count+=1
    return Count
print(longest_words())
