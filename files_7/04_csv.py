import csv
import os

# # write
# with open('files_7/file.csv', 'w') as file:
#     writer = csv.writer(file)
#     writer.writerow(['tweet_id', 'user_id', 'text'])
#     writer.writerow(['1000', '1', 'This is a tweet'])
#     writer.writerow(['1001', '2', 'Another tweet'])


# # read
# with open('files_7/file.csv', 'r') as file:
#     reader = csv.reader(file)
#     # print(list(reader))
#     for line in reader:
#         print(line)


# "update" .csv
with open('files_7/file.csv', 'r') as r, open('files_7/temp_file.csv', 'w') as w:
    reader = csv.reader(r)
    writer = csv.writer(w)
    for line in reader:
        if line[0] == '1000':
            writer.writerow([1000, 1, 'Modified text'])
        else:
            writer.writerow(line)

    os.remove('files_7/file.csv')
    os.rename('files_7/temp_file.csv', 'files_7/file.csv')
