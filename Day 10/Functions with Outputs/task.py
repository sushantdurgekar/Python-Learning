f_name = input("First Name: ")
l_name = input("Last Name: ")

def format_name(first_name,last_name):
    return f"{first_name.title()} {last_name.title()}"

print(format_name(first_name=f_name,last_name=l_name))


def concatenate(text):
    return text+text
def titleize(text):
    return text.title()

print(titleize(concatenate((f_name))))




