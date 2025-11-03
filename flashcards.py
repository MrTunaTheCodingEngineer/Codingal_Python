class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):

        return self.word + '('+self.meaning+')'
        

flash = []
print("welcome to flashcard application")

while(True):

    word = input("Enter a word to your flashcard: ")
    meaning = input("what is the meaining of the word: ")

    flash.append(flashcard(word, meaning))
    option = int(input("enter 0 in you want to add another flashcard, otherwise type in 1: "))

    if(option):
            break
    
    print("\nYour Flashcards: ")
    for i in flash:
         print(">", i)

