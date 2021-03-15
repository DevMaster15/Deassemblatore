import sys

def convertToInt(byte):

    int_value = int.from_bytes(byte, byteorder='big')
    return int_value

def read_list_from_file():
    # start program
    list_instruction = []
    final_list = []

    file_name = sys.argv[1]

    # initialize file descriptor f
    with open(file_name, "rb") as f:
        byte = f.read(1)  # read 1 bytes at a time
        counter = 0

        while byte:  # while byte is not null
            byte = convertToInt(byte)

            # create list of instruction -> [[byte1, byte2, byte3, byte4], [...], ...]
            list_instruction.insert(counter, byte)

            counter += 1

            if counter > 3:
                list_instruction = exclude_usless(list_instruction)
                final_list.append(list_instruction)
                list_instruction = []
                counter = 0

            byte = f.read(1)

    return final_list

# method that excludes useless elements if there are 'zero' or 'incr' or 'proj' function
def exclude_usless(byte_list):

    if byte_list[0] == 0 or byte_list[0] == 1:
        byte_list = byte_list[:2]
    elif byte_list[0] == 2:
        byte_list = byte_list[:3]

    return byte_list


