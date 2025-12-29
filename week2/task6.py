def all_eq(lst):
    if not lst:
        return []

    max_len = max(len(s) for s in lst)

    result = []
    for s in lst:
        result.append(s + '_' * (max_len - len(s)))

    return result