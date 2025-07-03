# Write a function merge_dicts(dict1, dict2) that merges two dictionaries. If a key
# exists in both dictionaries, sum their values. For example,
# merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}) returns {"a": 1, "b": 5, "c": 4}.
# Use dictionary methods like keys() or items() and conditionals.


def merge_dicts(dict1, dict2):
    merge = {}
    for k in set(dict1.keys()).union(dict2.keys()):
        value1 = dict1.get(k, 0)
        value2 = dict2.get(k, 0)
        merge[k] = value1 + value2
    return merge


d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
print(merge_dicts(d1, d2))
