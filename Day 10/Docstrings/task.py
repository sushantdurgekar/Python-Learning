def format_name(f_name, l_name):
    """ This Function takes first and last name as input and return it back in title case."""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name(input("What is your First name: "),
                             input("What is your Last name: "))

length = len(formatted_name)



