def flipstring_rec(string, result, i):
    if i < len(string):
        result = string[i] + result
        i += 1
        return flipstring_rec(string, result, i)
    else:
        return result

string = "Hello"
print(flipstring_rec(string, "", 0))
