def snake_to_lower_camel(src):
    words=src.split(' ');
    full_word=''
    for i in words:
        left_trimmed_word=trim_left(i)
        left_count=len(i)-len(left_trimmed_word)
        right_trimmed_word=trim_right(i)
        right_count=len(i)-len(right_trimmed_word)
        trimmed_word=trim_right(left_trimmed_word)

        # for word of words
        w=trimmed_word.split('_')
        combinedWords= w[0]+''.join(word.capitalize() for word in w[1:])

        #final string 
        full_word=full_word+''.join('_'*left_count)+combinedWords+''.join('_'*right_count)+' '
    return full_word.strip(' ')

def trim_left(text):
    return text.lstrip('_')

def trim_right(text):
    return text.rstrip('_')

print(snake_to_lower_camel('akhila'))
print(snake_to_lower_camel('_the_uSA'))
print(snake_to_lower_camel('__the_uSA'))
print(snake_to_lower_camel('the_usa__'))
print(snake_to_lower_camel('This __is__ the doc_string for __secret_fun'))