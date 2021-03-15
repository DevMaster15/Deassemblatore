
import handle_lists

# dict that represents functions
function_dict = {
    0: "zero",
    1: "incr",
    2: "proj",
    3: "jump"
}

def list_to_string(element_list):
    string = ""

    string += element_list + " "

    return string


# return string function contained in dictionary
def check_function(element_sub_list, sub_list):

    for el, fun in function_dict.items():
        if element_sub_list == el:
            return fun


# parse list and sub list
def parse(list_of_instruction):
    
    pc = 1

    for sub_list in list_of_instruction:

        for element_sub_list in sub_list:

            if element_sub_list == sub_list[0]:  # means that it's the first element and so the 'function code id'
                sub_list[0] = check_function(element_sub_list, sub_list)

            else:

                sub_list[pc] = str(element_sub_list)

                pc += 1

                if pc > 2 and sub_list[0] == "proj":
                    pc = 1

                elif pc > 1 and (sub_list[0] == "zero" or sub_list[0] == "incr"):
                    pc = 1

                elif pc > 3:
                    pc = 1


    return list_of_instruction


# method that divide the input list in sublists of 4 elements
# and then compute operations
def start_deassembler():
    list_of_instruction = handle_lists.read_list_from_file()

    print("list of instruction = " + str(list_of_instruction))

    final_list = parse(list_of_instruction)
    return final_list


def main():


    final_list = start_deassembler()

    with open("myfile.txt", "w") as fp:
        for sublist in final_list:
            for sub_list_element in sublist:
                string_to_write = list_to_string(sub_list_element)
                fp.write(string_to_write)

            fp.write("\n")

    print("lista in uscita = " + str(final_list))


if __name__ == '__main__':
    main()