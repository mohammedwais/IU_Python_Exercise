def add_articel(x=str):
    '''
    It adds article 'a' or 'an' to the name based on
    the starting alpapet of he word.
    (Warning! it is assumed that the user is rational and shall
    use nouns only)
    '''
    if x[0] in ['a','o','e','i']:
        x= 'an '+ x
    else:
        x= 'a '+ x
    return x
