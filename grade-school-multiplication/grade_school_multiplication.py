def grade_school_multiplication(a, b):
    multiplicator = str(b)
    multiplicator = multiplicator[::-1] # Reverse the order

    out = 0
    for idx, j in enumerate(multiplicator):
        out += (a * int(j) * (10 ** idx))
    return out 


if __name__ == "__main__":
    # Test 
    for i in range(100):
        for j in range(100):
            assert grade_school_multiplication(i, j) == i * j

