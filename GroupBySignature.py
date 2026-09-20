def group_by_signature(words: list) -> list:
    pass
    
groups = {}
    for w in words:
        if not w:
            continue
        signature = "".join(sorted(w))
        if signature not in groups:
            groups[signature] = []
        groups[signature].append(w)
    return list(groups.values())

if __name__ == "__main__":
    # Example 1
    words = ["abc", "bca", "cab", "bac", "xyz", "yxz", "zxy", "dog"]
    print(group_by_signature(words))
    # Output: [["abc", "bca", "cab", "bac"], ["xyz", "yxz", "zxy"], ["dog"]]

    # Example 2
    words = ["apple", "pale", "leap", "plea", "papel", "hello"]
    print(group_by_signature(words))
    # Output: [["apple", "papel"], ["pale", "leap", "plea"], ["hello"]]
