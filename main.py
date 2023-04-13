code = bytearray()

text = input("Text To Add to out.bin:\n\n").encode('ascii')
map(bin,bytearray(text))
with open("out.bin", "wb") as out_file:
  out_file.write(text)