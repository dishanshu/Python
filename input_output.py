# Python Input Output


# Append to a file
with open("text_file_input_output.txt", 'a') as file:
    txt = file.write("qwerty!!!")
    file.close()
 
# Read file
file_read = open("text_file_input_output.txt", 'r')
print(file_read.read())