from io import open

# # write mode
# text = 'Hello world!\n'
# file = open('files_7/test_file.txt', 'w')
# file.write(text)
# file.close()


# # read mode
# file = open('files_7/test_file.txt', 'r')
# text = file.read()
# file.close()
# print(text)


# # read mode as list
# file = open('files_7/test_file.txt', 'r')
# text = file.readlines()
# file.close()
# print(text)


# # with & seek
# with open('files_7/test_file.txt', 'r') as file:
#     print(file.readlines())
#     file.seek(0)
#     for line in file:
#         print(line)


# # with & add
# with open('files_7/test_file.txt', 'a+') as file:
#     file.write('\nChao mundo!')


# read & write
with open('files_7/test_file.txt', 'r+') as file:
    text = file.readlines()
    file.seek(0)
    text[0] = 'Chanchito feliz'
    file.writelines(text)
