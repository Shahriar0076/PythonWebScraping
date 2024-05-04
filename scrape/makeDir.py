import os

def create_directory_and_file(directory):
    dir_name, file_name = os.path.split(directory)    
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        print(f"Directory '{dir_name}' created.")
            
    file_path = os.path.join(dir_name, file_name)
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.write("This is a new file.")
        print(f"File '{file_path}' created.")
    else:
        print(f"File '{file_path}' already exists.")

if __name__ == "__main__":
    directory = './test/asd/app1.txt'
    create_directory_and_file(directory)
