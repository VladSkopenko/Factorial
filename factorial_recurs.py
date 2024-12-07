def fact_mem_list(n, memory_list=None):
    """Оптимізація через список"""
    if not memory_list:
        memory_list = [1]
    if n == 1:
        return memory_list
    else:
        fact_mem_list(n - 1, memory_list)
        memory_list.append(n * memory_list[-1])
        return memory_list


def fact_mem_dict(n, memory_dict=None):
    """Оптимізація через словник"""
    if not memory_dict:
        memory_dict = {1: 1}
    if n == 1:
        return memory_dict
    else:
        fact_mem_dict(n - 1, memory_dict)
        memory_dict[n] = n * memory_dict[n - 1]
        return memory_dict


if __name__ == "__main__":
    print(fact_mem_list(5))
    print(fact_mem_dict(5))
