## Add code below with answer clearly stated

def factorial(N: int) -> int:
    fac = 1
    for n in range(1, N + 1):
        fac *= n
    return fac

def sum_fact_digit(fact: int) -> int:
    """sum digits in factorial"""
    sum_ = 0
    while fact !=0:
        sum_ += fact%10
        fact = int(fact/10)
    return sum_


if __name__ == "__main__":
    print(sum_fact_digit(factorial(99))) # Sum of digits in 99! is same as 100! (only saves some computations)