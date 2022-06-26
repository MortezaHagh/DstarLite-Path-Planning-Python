def compare_keys(key1, key2):
    result = True
    if key1[0] > key2[0]:
        result = False
    elif key1[0] == key2[0]:
        if key1[1] >= key2[1]:
            result = False

    return result
