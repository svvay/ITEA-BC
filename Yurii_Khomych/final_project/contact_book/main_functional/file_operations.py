import csv

from main_functional.decorators import get_file_size


class File:
    def __init__(self, file_name, file_extension="csv"):
        self.file_name = file_name
        self.file_extension = file_extension

    def read(self):
        with open(f"../data/{self.file_name}.{self.file_extension}") as f:
            return list(csv.DictReader(f))

    def write(self, contact_list):
        with open(f"../data/{self.file_name}.{self.file_extension}", "w") as f:
            fieldnames = list(contact_list[0].keys())
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(contact_list)

@get_file_size
def get_contact_list(file_name, file_extension="csv"):
    file_manager = File(file_name=file_name, file_extension=file_extension)
    contact_list = file_manager.read()
    return contact_list
