import sys
from Router import Router

if __name__ == '__main__':
    file_path = sys.argv[1]
    input_test = ''
    print(file_path)
    with open(file_path, 'r') as file:
        input_test = file.read()

    print(Router(input_test).get_route_information())
