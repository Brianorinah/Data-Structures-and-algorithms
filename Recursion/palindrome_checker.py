import string

def data_cleaner(data):
    
    without_spaces = data.replace(" ","").lower()
    cleaned = without_spaces.translate(without_spaces.maketrans("","",string.punctuation))

    return cleaned

def inverting_a_string(str1):
    last_index = len(str1)-1
    if len(str1) == 1:
        return str1[0]
    else:
        return str1[last_index] + inverting_a_string(str1[:last_index])

my_str = "Able was I ere I saw Elba"
cleaned_data = data_cleaner(my_str)
inverted_str =inverting_a_string(cleaned_data)

print("cleaned_data",cleaned_data)
print("inverted_data",inverted_str)
print(cleaned_data == inverted_str)