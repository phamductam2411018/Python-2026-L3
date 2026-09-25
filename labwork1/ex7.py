def remove_dollar_sign(s):
    new_string = s.replace("$", "")
    return new_string

s = input()
result = remove_dollar_sign(s)

print("Initial String :", s)
print("String after remove $:", result)