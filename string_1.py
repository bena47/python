my_string = "Hello, World!"

# Accessing characters using positive indexing
first_char = my_string[0]
second_char = my_string[1]
last_char = my_string[11]

print("Positive indexing:")
print("First character:", first_char)
print("Second character:", second_char)
print("Last character:", last_char)


# Example: negative indexing
# Accessing characters using negative indexing
last_char_negative = my_string[-1]
second_last_char = my_string[-2]
first_char_negative = my_string[-13]

print("\nNegative indexing:")
print("Last character:", last_char_negative)
print("Second last character:", second_last_char)
print("First character:", first_char_negative)


# immutability
original_string = "Hello, World!"

# The line below gives an error
original_string[0] = 'h'


# Example: Creating a new string by concatenation

original_string = "Hello"
new_string = original_string + ", World!"

# Print the new variable
print(new_string)