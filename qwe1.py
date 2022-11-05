class Statistics_txt:

    def __init__(self, path):
        self.path = path

    def characters(self):
        file = open(self.path, "r")
        data = file.read()
        characters_count = len(data)
        return characters_count

    def words(self):
        file = open(self.path, "r")
        data = file.read()
        words_count = data.split()
        return len(words_count)

    def sentences(self):
        file = open(self.path, "r")
        data = file.read()
        sentences_count = (len([i for i in data.split('.')]))
        return sentences_count



xcv = Statistics_txt("sss.txt") #type here path to your file
print(xcv.characters())
print(xcv.words())
print(xcv.sentences())