def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        lowered_contents = convert_string_to_lowercase(file_contents)
        letter_dict = create_letter_dict(lowered_contents)
        only_alpha_contents = remove_non_alphas(lowered_contents)
        letter_dict = create_letter_dict(only_alpha_contents)
        letter_list = convert_dict_to_list(letter_dict)
        sorted_list = sort_list(letter_list)
        create_report_output(file_contents, sorted_list)

def count_words(string):
    words = string.split()
    return len(words)

def convert_string_to_lowercase(string):
    lowered_string = string.lower()
    return lowered_string

def remove_non_alphas(string):
    new_string = ""
    for char in string:
        if not char.isalpha():
            continue
        else:
            new_string += char
    return new_string

def create_letter_dict(string):
    letter_dict = {}
    for char in string:
        if char in letter_dict:
            letter_dict[char] += 1
        else:
            letter_dict[char] = 1
    return letter_dict

def convert_dict_to_list(dict):
    letter_list = []
    for k in dict:
        single_dict = {"letter": k, "count": dict[k]}
        letter_list.append(single_dict)
    return letter_list

def sort_on(dict):
    return dict["count"]

def sort_list(list):
    list.sort(reverse=True, key=sort_on)
    return list

def create_report_output(string, list_of_dicts):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(string)} words found in the document\n")
    for dict in list_of_dicts:
        print(f"The '{dict["letter"]}' character was found {dict["count"]} times")
    print("--- End report ---")


if __name__ == '__main__':
    main()