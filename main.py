def StringScramble(str1, str2):
    outer_string = str1
    inner_string = str2
    for char in inner_string:
        if char not in outer_string:
            return False
        updated_outer = outer_string.replace(char, "", 1)
        outer_string = updated_outer
    return True
