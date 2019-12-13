# Create function has_permission that get name of page.
# Inside has_permission function write inner function that
# check access to this page by username of user. Print result to console.

# Done

# my_nick = 'svvay'
# my_pass = '1122'


def has_permission(my_nick, my_pass):
    file = open('has_permission.txt')
    text = file.read().split()
    file.close()

    def check(text):
        if my_pass in text and my_nick in text:
            print(f'All good. \nYour nick - {my_nick}, \nYor password - {my_pass}')
        else:
            print('Sorry, something wrong ')
    check(text)
    # return True

# has_permission(my_nick, my_pass)

# print(f'All good. \nYour nick - {my_nick}, \nYor password - {my_pass}')
# print('Sorry, something wrong ')