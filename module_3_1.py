calls = 0

def count_calls():
    global calls
    calls +=1
    return calls
calls = count_calls()-1


def string_info(string):
    string = (len(string), string.upper(), string.lower())
    count_calls()
    return string


def is_contains(string, list_to_search):
    string = string.lower()
    list_to_search = str(list_to_search)
    list_to_search = list_to_search.lower()
    if string in list_to_search:
        result = string in list_to_search
    else:
        result = string in list_to_search
    count_calls()
    return result 

       
print(string_info("Привет, мир!"))
print(string_info("Учу Python"))
print(string_info("Capybara"))
print(string_info("Armageddon"))
print(is_contains("cHeRyY", ["ChErYy", "Apple", "Orange"]))
print(is_contains("Goodbye", ["Hello", "world"]))
print(calls)
    


 
        

