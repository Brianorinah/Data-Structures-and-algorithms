def inverting_a_string(str1):
    last_index = len(str1)-1
    if len(str1) == 1:
        return str1[0]
    else:
        return str1[last_index] + inverting_a_string(str1[:last_index])

print(inverting_a_string("jackson"))