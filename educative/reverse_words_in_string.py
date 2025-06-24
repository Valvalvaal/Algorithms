# T: O(N), S: O(N)
def reverse_words(sentence):
    sentence = sentence.strip()
    word_list = sentence.split()
    
    # With my approach I'll find each individual word and then place 
    # it in its corresponding indices backwards
    
    l, r = 0, len(word_list) - 1 
    
    while l < r:
        word_list[r], word_list[l] = word_list[l], word_list[r]
        
        l += 1
        r -= 1
    sentence = ' '.join(word_list)    
    return sentence

# Test cases

assert reverse_words("  Hello World  ") == "World Hello"
assert reverse_words("  I love    running  ") == "running love I"
assert reverse_words("  Reverse  this string  ") == "string this Reverse"
