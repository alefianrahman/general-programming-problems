def is_palindrome(s):
    """
    Check whether a string is a palindrome or not. 
    For example:
    
    is_palindrome('aba') -> True
    is_palindrome('bacia') -> False
    is_palindrome('hutuh') -> True
    
    Parameters
    ----------
    s : str
        String to check. 
    
    Returns
    -------
    bool 
        Is the string input a palindrome. 
    """
    if len(s) == 1:
        return True
    else:
        return s[0] == s[-1] and is_palindrome(s[1:-1])
    
    
if __name__ == "__main__":
    print("Is 'aba' a palindrome?")
    print(is_palindrome('aba'))
    print('\n')
    print("Is 'bacia' a palindrome?")
    print(is_palindrome('bacia'))
    print('\n')
    print("Is 'hutuh' a palindrome?")
    print(is_palindrome('hutuh'))
