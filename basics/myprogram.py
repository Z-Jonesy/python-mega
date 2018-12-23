print("Hello")

def string_length(mystring):
    if type(mystring) == int:
        return "this is a number"

    elif type(mystring) ==float:
        return "this is float"
        
    else:
        return len(mystring) 

print(string_length(0.4))