# Ineffective way
result = ""
for s in string_list:
    result += s

# Effective way
result = "".join(string_list)
