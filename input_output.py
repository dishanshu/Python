# Python Input Output


with open("text_file_input_output.txt", 'a') as file:
    txt = file.write("qwerty!!!")
    file.close()
 
file_read = open("text_file_input_output.txt", 'r')
print(file_read.read())