from main_functional.file_operations import File, get_contact_list
from main_functional.operate_contact import create_contact


def main():
    # while True:
    file_name = "contacts"
    contact_list = get_contact_list(file_name, file_extension="csv")
    contact_list.sort(key=lambda contact: (contact["first_name"], contact["second_name"]))
    # contact_list = sorted(contact_list, key=lambda contact: contact["first_name"], reverse=True)
    new_contact = create_contact(first_name="Jonny", second_name="Depp")
    # file_manager.write(contact_list=[new_contact.to_dict() for x in range(3)])



main()
