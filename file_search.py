import os


path = "F:/test/"
# for file in os.listdir(path):
#     print(file)

# print('-----------------')
# print(os.path)
# print('-----------------')

for root, dir, files in os.walk(path):
    print(f'{root} --> {dir} --> {files}')
    for file in files:
        if file.endswith('.png'):
            print(os.path.join(root, file))
