


def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    s=sentence
    w=s.swapcase()
    words = w.split(' ')     
    reverse_sentence = ' '.join(reversed(words)) 
    return reverse_sentence 
