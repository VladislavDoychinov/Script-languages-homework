def flipstring(string):
    result = ""   
    for i in string:
        result = i + result
   
    return result

string = "Hello"
print(flipstring(string))

