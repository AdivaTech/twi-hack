import time
import os

class SDReader:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        """
        Reads data from the SD card file specified during initialization.
        Returns the contents of the file.
        Raises FileNotFoundError if the file does not exist.
        Raises IOError for other input/output errors.
        """
        try:
            if not os.path.exists(self.filename):
                raise FileNotFoundError(f"File '{self.filename}' not found.")
            with open(self.filename, 'r') as file:
                data = file.read()
                return data
        except FileNotFoundError as fnf_error:
            print(fnf_error)
            return None
        except IOError as io_error:
            print(f"Error reading from '{self.filename}': {io_error}")
            return None

if __name__ == '__main__':
    reader = SDReader('sample_data.txt')
    data = reader.read()
    if data:
        print(data)
    else:
        print("No data read from the file.")
