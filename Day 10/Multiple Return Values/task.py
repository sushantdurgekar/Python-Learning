def format_name(f_name, l_name):
    if f_name=="" and l_name=="":
        return "You have provided an invalid input."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name(input("What is you first name: "), input("What "
                                                           "is "
                                                           "your "
                                                           "last "
                                                           "name: ")))
