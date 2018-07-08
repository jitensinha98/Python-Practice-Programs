def break_words(sentence):
    words=sentence.split()
    return words
    
def print_first_word(sentence):
    word=break_words(sentence)
    x=word.pop(0)
    print x
  
def print_last_word(sentence):
    word=break_words(sentence)
    y=word.pop(-1)
    print y
    
def sort_sentence(sentence):
    word=break_words(sentence)
    z=sorted(word)
    print z
    
string=str(raw_input("Enter Sentence")

print_first_word(string)


print_last_word(string)


sort_sentence(string)
    
