from time import sleep
import sys


print('This is my file to demonstrate best practices.')

def process_data(data):
    print('Beginning data processing...')
    modified_data = data + ' that has been moodified'
    sleep(3)
    print('Data processing finished.')
    return modified_data


def main():
    data = 'My data read from the Web'
    print(data)
    modified_data = process_data(data)
    print(modified_data)
 
# if __name__ == '__main__':
#     main()

# for i in sys.path:
#     print(i)


from sys import getrecursionlimit

print(getrecursionlimit())