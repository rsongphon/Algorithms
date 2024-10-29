def read_txt_return_arraynum(filepath):
    """
    Input : Filepath of txt file of number. Each number seperates by newline
    Output : Array of numbers
    """
    
    file_path = filepath

    # Initialize an empty list to store the numbers
    numbers_list = []

    # Open the file and read the contents
    with open(file_path, 'r') as file:
        for line in file:
            # Strip any extra whitespace and convert the line to an integer
            number = int(line.strip())
            # Append the number to the list
            numbers_list.append(number)
            
    return numbers_list
