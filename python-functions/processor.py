def process_numbers(input):
    output = []

    if input == None:
        return output
    elif not isinstance(input, list):
        return output

    for i in input:
        if str(i).isnumeric() == True:
            output.append(int(i))

    output.sort()

    return output

def process_names(input):
    output = []

    if input == None:
        return output
    elif not isinstance(input, list):
        return output

    for i in input:
        if str(i).isnumeric() == False:
            output.append(str(i))

    output.sort()

    return output