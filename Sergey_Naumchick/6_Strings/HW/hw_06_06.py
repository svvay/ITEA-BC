# 6. Return list of domains from list of emails.

li = ["Sky_fall@gmail.com", "def_get@i.ua", "Andriy_Zhopin@yahoo.com"]
li = ['1221', 'sergey@gmail.com', 'koko@i.ua']


def mail_return_domain(list_email):
    domain_list = []

    for word in list_email:
        temp = False
        temp_string = ""

        for letter in word:

            if temp == True:
                temp_string += letter

            if letter == "@":
                temp = True

        domain_list.append(temp_string)
    print(domain_list)
    return domain_list


