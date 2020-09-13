def fibo(n):
    """
    Return the Fibonacci number with index n. n starts from 1. 
    For example: 
    
    fibo(1) -> 1
    fibo(2) -> 1
    fibo(3) -> 2
    fibo(4) -> 3
    fibo(5) -> 5
    
    Parameters
    ---------
    n : int 
        The index of Fibonacci number (starts from 1). 
    
    Returns
    -------
    int 
        The Fibonacci number of index n.
    """
    if n in [1, 2]:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

def fibo_list(n):
    """
    Return a list of ordered Fibonacci numbers with length n.
    
    fibo_list(1) -> [1]
    fibo_list(2) -> [1, 1]
    fibo_list(3) -> [1, 1, 2]
    fibo_list(4) -> [1, 1, 2, 3]
    fibo_list(5) -> [1, 1, 2, 3, 5]
    
    Parameters
    ---------
    n : int 
        The length of Fibonacci list.
    
    Returns
    -------
    list 
        List of Fibonacci numbers with length n.
    """
    return [fibonacci(i) for i in range(1, n + 1)]

    
if __name__ == "__main__":
    print("The 10th Fibonacci number: ")
    print(fibo(10))
    print('\n')
    print("The first 10 Fibonacci numbers:")
    print(fibo_list(10))
