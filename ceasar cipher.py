# ord = string to ascii
# chr = ascii to string

def research_mutator(user_input, shift):
    input_list = []
    input_list[:0] = user_input
    mutated_list = []
    il_size = len(input_list)
    while il_size != 0:
        il_size -= 1
        new_int = ord(input_list[il_size]) + int(shift)
        new_char = chr(new_int)
        mutated_list.insert(0, new_char)
    changed_string = "".join(str(e) for e in mutated_list)
    return changed_string


def main():
    user_input = input("Enter a string: ")
    shift = input("Enter the cipher number (negative for decoding): ")
    mutated_input = research_mutator(user_input, shift)
    print(mutated_input)


if __name__ == '__main__':
    main()
