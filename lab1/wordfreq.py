def tokenize(lines):
    words = []
    for line in lines:
        start = 0
        # Kontrollerar att start < längden på line
        while start < len(line):
            # Hoppar öven mellanrum
            while start < len(line) and line[start].isspace():
                start = start + 1
            if start < len(line) and line[start].isalpha():
                # Sätter start till ordets första bokstav
                end = start
                # Flyttar 'end' till slutet av ordet
                while end < len(line) and line[end].isalpha():
                    end = end + 1
                # Lägger til ordet fast med små bokstäver till listan 'words'
                words.append(line[start:end].lower())
                start = end
            # Samma fast med siffror
            elif start < len(line) and line[start].isdigit():
                end = start
                while end < len(line) and line[end].isdigit():
                    end = end + 1
                words.append(line[start:end])
                start = end
            # Skyddar mot index  out of range error
            elif start >= len(line):
                break
            # Lägger till specialtecken i listan words
            else:
                words.append(line[start])
                start = start + 1
    return words


def countWords(words, stopWords):
    # Öppnar en tom dictionary
    dictionary = {}
    for word in words:
        # Om ordet ligger i stopWords hoppar vi över det
        if word in stopWords:
            pass
        elif word not in dictionary:
            # Lägger till en key med ordet och value 1 om ordet inte finns i tidigare
            dictionary[word] = 1
        else:
            # Ökar value på ordet om det redan finns som en key
            dictionary[word] += 1
    return dictionary


def printTopMost(frequencies, n):
    # Sorterar våran dictionary
    frequencies = dict(sorted(frequencies.items(), key=lambda item: -item[1]))
    # Skapar en lista av de 'n' första keys och values
    top_n = list(frequencies.items())[:n]
    for word, freq in top_n:
        # Printar ut listan enligt de angivna avstånden
        print(word.ljust(20) + str(freq).rjust(5))
