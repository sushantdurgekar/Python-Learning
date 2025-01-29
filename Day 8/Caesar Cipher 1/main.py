# def greet():
#     print("Hello, ")
#     print("How do you do?")
#     print("Isn't the weather nice?")
#
# # greet()
#
# # ### Function with Inputs
# def greet_with_name(name):
#     print(f"Hello, {name}")
#     print(f"How do you do {name}?")
#     print(f"{name}, Isn't the weather nice?")
#
# greet_with_name("abcd")


# # ### Functions with 2 or more input
#
# def greet_with(name,location):
#     print(f"Hello {name}")
#     print(f"How are you doing {name} in {location}?")
#
#
# greet_with("Jack Bauer","US")
# greet_with("US","Jack Bauer")
# greet_with(location="US",name="Jack Bauer")



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text'
#  and 'shift_amount' as 2 inputs.

def encrypt(original_text,shift_amount):
    # TODO-2: Inside the 'encrypt()' function, shift each letter of the
    #  'original_text' forwards in the alphabet
    #  by the shift amount and print the encrypted text.
    encrypted_text=""
    for letter in original_text:
        letter_index=alphabet.index(letter)
        shifted_index=letter_index+shift_amount
        # TODO-4: What happens if you try to shift z forwards by 9?
        #  Can you fix the code?
        # if shifted_index>25:
        #     shifted_index=shifted_index-25-1
        shifted_index%=len(alphabet)
        encrypted_text+=alphabet[shifted_index]
    print(f"Here is the encoded result: {encrypted_text}")

# TODO-3: Call the 'encrypt()' function and pass in the user inputs.
#  You should be able to test the code and encrypt a message.
encrypt(text,shift)











