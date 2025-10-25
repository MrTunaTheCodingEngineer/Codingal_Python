class StringReverse:

    def __init__(self, string_input):


      self.original_string = string_input

    def reverse_words(self):
       
       words = self.original_string.split()

       reversed_words = reversed(words)

       return"".join(reversed_words)
    
if __name__ == "__main__":
   
    sentence = " this sentence is in reverse"

    reverser = StringReverse(sentence)

    reversed_sentence = reverser.reverse_words()

    print(f"The Original string: '{sentence}'")
    print(f"The Reversed string: '{reversed_sentence}'")

    another_sentence = "This is Codingal"
    another_reverser = StringReverse(another_sentence)
    another_reversed_sentence = another_reverser.reverse_words()
    
    print(f"\nOriginal string: '{another_sentence}'")
    print(f"Reversed string: '{another_reversed_sentence}'")