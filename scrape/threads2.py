import threading
import os

# Array of URLs
urls = [
    'https://softexpo.com.bd/exhibitor/details/10119/adn-group',
    'https://softexpo.com.bd/exhibitor/details/10058/bank-asia-limited',
    'https://softexpo.com.bd/exhibitor/details/10137/bikroycom-limited',
    'https://softexpo.com.bd/exhibitor/details/10009/bjit-limited',
    'https://softexpo.com.bd/exhibitor/details/10056/dohatec-new-media',
    'https://softexpo.com.bd/exhibitor/details/10161/flora-systems-limited',
    'https://softexpo.com.bd/exhibitor/details/10024/genuity-systems-limited',
    'https://softexpo.com.bd/exhibitor/details/10187/giga-tech-ltd',
    'https://softexpo.com.bd/exhibitor/details/10116/ibos-limited',
    'https://softexpo.com.bd/exhibitor/details/10016/intelligent-machines-limited',
    'https://softexpo.com.bd/exhibitor/details/10163/kaicom-solutions',
    'https://softexpo.com.bd/exhibitor/details/10097/mango-teleservices-limited',
    'https://softexpo.com.bd/exhibitor/details/10042/panache-solutions-pvt-ltd',
    'https://softexpo.com.bd/exhibitor/details/10121/pridesys-it-ltd',
    'https://softexpo.com.bd/exhibitor/details/10114/reve-systems-limited',
    'https://softexpo.com.bd/exhibitor/details/10061/soft-tech-innovation-ltd',
    'https://softexpo.com.bd/exhibitor/details/10140/the-decode-ltd',
    'https://softexpo.com.bd/exhibitor/details/10022/vivasoft-limited',
    'https://softexpo.com.bd/exhibitor/details/10143/access-telecom-bd-ltd',
    'https://softexpo.com.bd/exhibitor/details/10157/adorsho-pranisheba-limited',
]

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

# Function to print URLs in a given range and write them to a file
def print_urls(start, end, file_name):
    file_name = './textFiles/'+file_name
    create_directory_and_file(file_name)
    with open(file_name, 'w') as file:
        for url in urls[start:end]:
            file.write(url + '\n')
            print(url)

# Function to divide the array into n threads and print URLs
def print_urls_in_threads(n):
    thread_list = []
    urls_per_thread = len(urls) // n  # dividing number of URLs among n threads

    for i in range(n):
        start = i * urls_per_thread
        end = (i + 1) * urls_per_thread if i < n - 1 else len(urls)
        file_name = f'urls_thread_{i}.txt'  # Generating file name
        thread = threading.Thread(target=print_urls, args=(start, end, file_name))
        thread_list.append(thread)
        thread.start()

    for thread in thread_list:
        thread.join()

# Example usage with 5 threads
print_urls_in_threads(3)
