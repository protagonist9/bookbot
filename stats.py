def count_words(text):
    counter = 0
    list = text.split()
    for i in list:
        counter+=1
    print(f"Found {counter} total words")    
    return counter

def count_char(text):
    answer = {}

    for char in text.lower():
        if char in answer:
            answer[char]+=1
        else:
            answer[char]=1
    return answer

def sort_by_num(dictionary):
    return dictionary["num"]


def sort_final(dictionary):
    new_list = []
    for char, count in dictionary.items():
        new_list.append({"char":char , "num": count})
    new_list.sort(key=sort_by_num, reverse=True)
    return new_list

