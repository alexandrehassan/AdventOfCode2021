
str_a = "abc"
str_b = "ac"
new_str = ""
if len(str_a) > len(str_b):
    for ch in str_b:
        print(ch)
        str_a = str_a.replace(ch, "")
    print(str_a)
