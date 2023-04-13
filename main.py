import file
import system
import os
import platform

osPlatform = platform.system()
print("Platform: " + osPlatform)

if osPlatform == str("Linux"):
  file.WriteFile("out.bin")
  os.system("clear")
  file.ReadFile("out.bin")
elif osPlatform == str("Windows"):
  file.WriteFile("out.bin")
  os.system("CLS")
  file.ReadFile("out.bin")
elif osPlatform == str("Darwin"):
  file.WriteFile("out.bin")
  os.system("Clear screen")
  file.ReadFile("out.bin")
else:
  print("We don't know what platform you're on.")