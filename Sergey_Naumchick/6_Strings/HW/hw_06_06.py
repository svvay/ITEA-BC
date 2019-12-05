# 6. Return list of domains from list of emails.

li = ["Sky_fall@gmail.com", "def_get@i.ua", "Andriy_Zhopin@yahoo.com"]
lii = ['1221', 'sergey@gmail.com', 'koko@i.ua']


def mail_return_domain(list_email):
    domail_list = []
    for word in list_email:
        if "@" in word:
            domail_list.append(word.split("@")[1])
    return domail_list
