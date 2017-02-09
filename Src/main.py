import sys
from Src.RailroadService import RailroadService

if __name__ == '__main__':
    file_path = sys.argv[1]
    input_test = ''

    with open(file_path, 'r') as file:
        input_test = file.read()

    print(RailroadService(input_test).get_route_information())
