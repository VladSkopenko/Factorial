def factorial_iterative(n):
    """Ітеративний спосіб розрахунку факторіалу"""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_iterative_list(n):
    """Ітеративний спосіб розрахунку факторіалу але який повертає список послідовностей"""
    result = [1]
    for i in range(2, n + 1):
        result.append(i * result[-1])
    return result


def factorial_iterative_dict(n):
    """Ітеративний спосіб розрахунку факторіалу але який повертає словник послідовностей"""
    result = {1: 1}
    for i in range(2, n + 1):
        result[i] = i * result[i - 1]
    return result


if __name__ == "__main__":
    print(factorial_iterative(5))
    print(factorial_iterative_list(5))
    print(factorial_iterative_dict(5))
