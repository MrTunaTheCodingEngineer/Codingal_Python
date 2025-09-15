def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)

    print("List of words with the first and last letter same:\n", lst)
    return ctr
          
count = match_words(['abc', 'cfc', 'xyz', 'aba', '12221', '213', '6432112346', '1912'])
print("number of words having the first and last letter same:", count)
         
