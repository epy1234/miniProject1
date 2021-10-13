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
print(word_count())
