import matplotlib.pyplot as plt

def text2dict(file, min = 1, max = 1000000, blacklist = [], spChar = ""):
    """"Convertir archivo de textor a diccionario para facilitar el historgrama.
        Se define frecuencia mínima y máxima"""
    if max > min:
        # Dictionary
        histo = dict()
        # Reading data
        with open(file, "r") as data:
            text = data.read()
        # Remove special characters
        for char in spChar:
            text = text.replace(char, "")
        # string to list lowercase
        for word in text.lower().split():
            if word in histo.keys() and word not in blacklist:
                histo[word] += 1
            else:
                histo[word] = 1
        # histo needs to be filtered before return
        return dict((k, v) for k, v in histo.items() if v >= min and v <= max)
    else:
        print("min > max !")
        return {"no words":0}

if __name__ == "__main__":
    # Parameters
    min2show = 2
    max2show = 20
    bl = ["or", "to", "the", "with", "is", "a", "in", "but", "not", "any", "eg",
          "plus", "have", "on", "plus", "end", "into", "related", "etc",
          "good", "advanced", "and", "of", "knowledge", "strong", "working", "user"]
    specialChars = "()!@#$%^&*.,"
    # Obtain histrogram
    histo = text2dict("data.txt", min2show, max2show, bl, specialChars)
    plt.figure(1, figsize=(8, 12))
    plt.bar(histo.keys(), histo.values(), 1.0, color='g')
    plt.xlabel('Words')
    plt.xticks(rotation=90)
    plt.ylabel('Frecuency')
    plt.title('Histogram of Words')
    plt.grid(True)
    plt.show()
