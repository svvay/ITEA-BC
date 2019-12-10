# 6. Return list of domains from list of emails.
#

emails = ['vgitun@i.ua', 'vgytun@gmail.com', 'v.hytun@sbrf.com.ua']


def email_domain(my_emails):
    import re
    my_email_str = ','.join(emails)
    print(my_email_str)
    my_domain = re.findall(r'@\w+\.\w+|@\w+\.\w+\.\w+', my_email_str)
    print(my_domain)


email_domain(emails)
