from console_gfx import ConsoleGfx
def to_hex_string(data):
    for values in data:                 # each value in list
        if values == 10:
            data[data.index(10)] = "a"
        if values == 11:
            data[data.index(11)] = "b"     # change value to string equivalent
        if values == 12:
            data[data.index(12)] = "c"
        if values == 13:
            data[data.index(13)] = "d"
        if values == 14:
            data[(data.index(14))] = "e"
        if values == 15:
            data[(data.index(15))] = "f"

    hex_str = ""
    for values in data:
        hex = str(values)
        hex_str = hex_str + hex   # place values in a string
    return hex_str

def count_runs(flat_data):
    current = flat_data[0]
    count = 1
    count_repeat = 1
    for item in flat_data[1:]:
        if current != item:
            count += 1
            current = item
        else:
            count_repeat += 1

        if count_repeat >= 15:
            count_repeat = 0
            count += 1
            current = flat_data[item + 1]

    return count

def encode_rle(flat_data):

    current = flat_data[0]
    count = 1
    count_repeat = 1
    for item in flat_data[1:]:
        if current != item:
            count += 1
            current = item
    num_variables = count

    rle_complete = []  # goes through each value in flat_data
    for item in flat_data:
        if item not in rle_complete:  # if item is not in blank list then it is added
            rle_complete.append(item)

    rle_final = []
    run_length = 1
    current_char = flat_data[0]   # First item in flat_data
    for item in rle_complete:   # for each item in rle_complete
        for i in range (1, len(flat_data)):
            if current_char == flat_data[i]:
                run_length += 1                 # if current char is the same as any character in the list run_length is extended
            else:
                rle_final.extend([run_length, current_char])
                run_length = 1                      # When current char is not the same, list is extended
                current_char = flat_data[i]         # run_length is reset
                num_variables -= 1
            if run_length >= 15:                    # if run_length goes over 15, list is extended
                rle_final.extend([run_length, current_char])
                run_length = 0                          # run_length is set to 0
                current_char = flat_data[i + 1]

            if num_variables == 0:          # break out of for loop when num_variables is 0
                break

    return rle_final

def get_decoded_length(rle_data):
    sum_even = 0
    for index, item in enumerate(rle_data):      # only count the items with an even index
        if index % 2 == 0:
            sum_even += item

    return sum_even

def decode_rle(rle_data):
    decode_string = [] # blank list
    for index, item in enumerate(rle_data):
        if index % 2 != 0: # Identifies which values need to be duplicated
            decode_length = rle_data[index - 1] # assigns the length of each value
            for i in range(decode_length):
                decode_string.append(item) # appends each value the specified number of times

    return decode_string

def string_to_data(data_string):

    data = []
    for item in data_string:       # for each item in the string
        if item.isdigit():
            item = int(item)
            data.append(item)       # if its a digit turn it to an int
        if item == "f":
            item = 15
            data.append(item)       # convert letters to ints
        if item == "e":
            item = 14
            data.append(item)
        if item == "d":
            item = 13
            data.append(item)
        if item == "c":
            item = 12
            data.append(item)
        if item == "b":
            item = 11
            data.append(item)
        if item == "a":
            item = 10
            data.append(item)       # add to list and return the data

    return data

def to_rle_string(rle_data):

    for index, item in enumerate(rle_data):
        if index % 2 != 0:
            if item <= 9:
                rle_data[rle_data.index(item)] = str(item)
            if item == 10:
                rle_data[rle_data.index(item)] = "a"
            if item == 11:
                rle_data[rle_data.index(item)] = "b"
            if item == 12:
                rle_data[rle_data.index(item)] = "c"
            if item == 13:
                rle_data[rle_data.index(item)] = "d"
            if item == 14:
                rle_data[rle_data.index(item)] = "e"
            if item == 15:
                rle_data[rle_data.index(item)] = "f"
        else:
            rle_data[rle_data.index(item)] = str(item)

    delim = ":"
    delim_list = []
    count = 0
    for i in range(0, len(rle_data), 1):
        if count == 2:
            delim_list.extend([delim, rle_data[i]])
            count = 1
        else:
            delim_list.append(rle_data[i])
            count += 1

    final_str = ""
    for values in delim_list:
        final_str += values


    return final_str

def string_to_rle(rle_string):
    results_list = []

    rle_list = [rle_string.split(":")]
    for item in rle_list:
        for character in item:
            first_char = int(character[0:-1])
            last_char = character[-1]
            if last_char == "f":
                last_char = 15
            if last_char == "e":
                last_char = 14
            if last_char == "d":
                last_char = 13
            if last_char == "c":
                last_char = 12
            if last_char == "b":
                last_char = 11
            if last_char == "a":
                last_char = 10
            else:
                last_char = int(last_char)

            results_list.extend([first_char, last_char])

    return results_list

def main():

    print("Welcome to the RLE image encoder!\n")
    print("Displaying Spectrum Image:")
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)
    program_continue = True
    image_data = None
    test_image = ConsoleGfx. test_image
    while program_continue: # 1 iteration option 1 read the image file, 2nd iteration option 6 display the image

        #print("Displaying Spectrum Image:")
        #ConsoleGfx.display_image(ConsoleGfx.test_rainbow)
        print(" ")
        print("RLE Menu")
        print("--------")
        print("0. Exit")
        print("1. Load File")
        print("2. Load Test Image")
        print("3. Read RLE String")
        print("4. Read RLE Hex String")
        print("5. Read Data Hex String")
        print("6. Display Image")
        print("7. Display RLE String")
        print("8. Display Hex RLE Data")
        print("9. Display Hex Flat Data\n")


        # set up option 1, 2, 6 in project 2A
        # prompt for the user input
        option = int(input("Select a Menu Option: "))

        if option == 0:
            program_continue = False

        elif option == 1:
            # read the image data from file
            file_load = input("Enter name of file to load: ")
            image_data = ConsoleGfx. load_file(file_load)

            # filename is going to be inputted by the user
            # assign ConsoleGfx. load_file(filename) to image_data
            # store the image data in the image_data variable

        elif option == 2:
            # assign ConsoleGfx. test_image to image_data
            image_data = ConsoleGfx. test_image
            print("Test image data loaded.")

        elif option == 3:
            rle_str_input = input("Enter an RLE string to be decoded: ")
            total_data = decode_rle(string_to_rle(rle_str_input))
        elif option == 4:
            rle_hex_input = input("Enter the hex string holding RLE data: ")
            total_data = decode_rle(string_to_data(rle_hex_input))
        elif option == 5:
            # collect hex string
            flat_hex_str_input = input("Enter the hex string holding flat data: ")
            total_data = string_to_data((flat_hex_str_input))

        elif option == 6:
            # display the image
            print(" Displaying image...")
            ConsoleGfx. display_image(image_data)

        elif option == 7:
           final_display = to_rle_string(encode_rle(total_data))
           print(f"RLE representation: {final_display}")

        elif option == 8:
            final_display = to_hex_string(encode_rle(total_data))
            print(f"RLE hex values: {final_display}")

        elif option == 9:
            final_display = to_hex_string(total_data)
            print(f"Flat hex values: {final_display}")



if __name__ == "__main__":
    main()

