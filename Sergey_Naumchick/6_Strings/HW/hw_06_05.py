# li = ["+380971236789", "+380809123232", "99999x9999"]
# 5. Check that mobile phone number is valid.

def check_numb(tel_numb_list):
    valid_numb_list = []

    for tel_numb in tel_numb_list:
        if len(tel_numb) == 13:
            if tel_numb.startswith("+380"):
                print(f"number {tel_numb} is valid!")
                valid_numb_list.append(tel_numb)

            else:
                print(f"number {tel_numb} is not valid!")
        elif len(tel_numb) == 10:
            if tel_numb.startswith("0"):
                print(f"number {tel_numb} is valid!")
                valid_numb_list.append(tel_numb)

            else:
                print(f"number {tel_numb} is not valid!")
        else:
            print(f"number {tel_numb} is not valid!")
    print(f"list of valid tel numb: {valid_numb_list}")
    return valid_numb_list
