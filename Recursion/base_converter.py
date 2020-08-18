def base_conveter(number , base):
    convert_str = "0123456789ABCDEF"
    
    if number < base:
        return convert_str[number]
    else:
        return base_conveter(number // base , base) + convert_str[number % base]


print(base_conveter(10, 2))