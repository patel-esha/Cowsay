from cow import Cow


class FileCow(Cow):

    def __init__(self, name, filename):  # takes on from the parent class Cow
        super().__init__(name)  # super() retrieves Cow initializers
        self.name = name
        self.filename = filename
        try:
            file = open(filename)  # tries to open the file
            file = file.read()  # tries to read the file
            self.image = file  # if the try statement worksm the image is the file's contents
        except RuntimeError:  # except statement allows gracefulness if the try statement does not work
            print('MOOOOOO!!!!!!')

    # constructor; creates a new FileCow object with the given name and image
    # loaded from filename
    # if the file cannot be loaded, it should raise a new RuntimeError with the message,
    # "MOOOOOO!!!!!!"
    # This should be the only constructor for the FileCow class

    def set_image(self, image):
        raise RuntimeError and print('Cannot reset FileCow Image')  # runtime error as specified in lab 9 instructions
# should immediately raise a new RuntimeError with the message
# "Cannot reset FileCow Image"
