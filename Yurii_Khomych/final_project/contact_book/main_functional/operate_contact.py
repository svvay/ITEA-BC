from main_functional.contact import Contact


def create_contact(first_name, second_name):
    try:
        new_contact = Contact(
            first_name=first_name,
            second_name=second_name,
        )
    except ValueError:
        new_contact = None
        pass

    return new_contact
