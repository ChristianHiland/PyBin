text = input("Text To Add to out.bin:\n\n").encode('ascii')
map(bin,bytearray(text))
textn = b"Type the following command to edit /etc/hostname using nano or vi text editor: sudo nano /etc/hostname.\n Delete the old name and setup new name.\n Next Edit the /etc/hosts file: sudo nano /etc/hosts. ... \nReboot the system to changes take effect: sudo reboot."

with open("out.bin", "wb") as out_file:
  out_file.write(text)