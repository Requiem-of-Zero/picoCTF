def caesar_encrypt(text):
  result = ""

  # go through each char of the text in this for loop
  for i in range(len(text)):
    char_position = ord(text[i])

    # subtract 97 to have a character from 1 to 26
    char_position = char_position - 97

    # add 3 to the position, as casesar does
    new_char_position = char_position + 3

    # make sure that the position does not surpass 26 (we wrap around)
    new_char_position = new_char_position % 26

    # convert back to ASCII values
    new_char_position = new_char_position + 97

    # convert ASCII value to character and concatenate it to final result
    result = result + chr(new_char_position)

    print(result)
  return result

def caesar_decrypt(cipher_text):
  result = ""

  # go through each character of the text in this for loop
  for i in range(len(cipher_text)):

    # obtain the ascii value using ord
    char_position = ord(cipher_text[i])

    # subtract 97 to have a character from 1 to 26
    char_position = char_position - 97

    # subtract 3 to the position, to get back original position
    new_char_position = char_position - 3

    # make sure that the position doesn't surpass 26 (we wrap around)
    new_char_position = new_char_position % 26

    # convert back to ascii values
    new_char_position = new_char_position + 97

    # convert ascii value to character and concat
    result = result + chr(new_char_position)
    print(result)
  return result

text = "picoctf"
print(f"Plain Text: {text}")
cipher_text = caesar_encrypt(text)
print(f"Encrypted: {cipher_text}")
print(f"Decrypted: {caesar_decrypt(cipher_text)}")