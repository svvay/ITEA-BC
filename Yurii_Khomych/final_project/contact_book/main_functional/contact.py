class Contact:
    def __init__(
            self,
            first_name,
            second_name,
            address=None,
            phone=None,
            mobile_phone=None,
            email=None,
            second_mail=None,
    ):
        # self.check_name(first_name)
        self.first_name = self.check_name(name=first_name)
        self.second_name = self.check_name(name=second_name)

    def check_name(self, name):
        if len(name) < 3:
            raise ValueError(f"Your {name} less that 3 symbols")
        return name

    def search(self, first_name, second_name,):
        pass

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "second_name": self.second_name,
            # "address": self.address,
            # "phone": self.phone,
            # "mobile_phone": self.mobile_phone,
            # "email": self.email,
            # "second_mail": self.second_mail,
        }
