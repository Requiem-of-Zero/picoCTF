file_path_read = "pico.txt"
file_path_write = "outputpico.txt"
i = 1

with open(file_path_read, "r") as file_read:
  with open(file_path_write, "w") as file_write:
    for line in file_read:
      file_write.write(str(i) + "\n")
      file_write.write(line + "\n")
      i += 1

print("look inside your folder...")