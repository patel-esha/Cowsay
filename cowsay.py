import sys
from cow import Cow
from dragon import Dragon
from ice_dragon import IceDragon
from file_cow import FileCow
from heifer_generator import HeiferGenerator as Hgx


def list_cows():
    cows = Hgx.get_cows()  # retrieves cows from Python's list of objects
    return cows


def list_file_cows():  # retrieves from the cows folder
    file_cows = Hgx.get_file_cows()
    return file_cows


def find_cow(name):  # given a name and a python list of objects
    for cow in list_cows():  # looks for the cow in Python's list
        if cow.name == name:
            return cow  # returns the cow object
    return None  # no such object found in list_cows()


def find_file_cow(name):  # replica of find_cow() but for the cow files
    for cow in list_file_cows():
        if cow.name == name:
            return cow
    return None


# Main program
def main():
    cows = Hgx.get_cows()
    file_cows = Hgx.get_file_cows()
# List the available cows: Cows available: heifer kitteh dragon ice-dragon
    if sys.argv[1] == '-l':
        list = [cow.name for cow in cows]  # heifer and kitteh
        list = str(list).replace(',', '')[1:-1]  # removes brackets and commas
        list = str(list).replace("'", '')  # removes quotation marks
        file_list = [cow.name for cow in file_cows]
        file_list = str(file_list).replace(',', '')[1:-1]  # removes brackets and commas
        file_list = str(file_list).replace("'", '')  # removes quotation marks
        print(f'Cows available: {list}')
        print(f'File cows available: {file_list}')

# Prints out the MESSAGE using the specified COW: I am pritteh! (Kitteh or Heifer)
    elif sys.argv[1] == '-n':
        specific_cow = find_cow(sys.argv[2])  # the cow index
        if specific_cow:  # looks for indexxed cow in the list_cows() --> Python's list
            message = ' '.join(sys.argv[3:])
            print(message)
            print(specific_cow.image)  # prints image
            if sys.argv[2] == 'dragon':
                print('This dragon can breathe fire.')
            elif sys.argv[2] == 'ice-dragon':
                print('This dragon cannot breathe fire.')
        else:
            print(f'Could not find {sys.argv[2]} cow!')  # ex: ninja

    elif sys.argv[1] == '-f':  # added on for the file cow
        specific_file = find_file_cow(sys.argv[2])  # uses the file cow version of function find_cow
        if specific_file:  # if it returns
            message = ' '.join(sys.argv[3:])  # sys.argv[3:] == everything after index 2
            print(message)
            print(specific_file.image)

# if a user calls for a cow that does not exist:"Could not find [cowname] cow!"
        else:
            print(f'Could not find {sys.argv[2]} cow!')  # ex: ninja

# Prints out the MESSAGE using the default COW: I am a potato! (Heifer)
    else:
        message = ' '.join(sys.argv[1:]) # message starts as "-n" or "l" was not typed
        print(message)
        print(Hgx.get_cows()[0].image)  # set to image of heifer from HeiferGenerator


main()  # calls main to run

