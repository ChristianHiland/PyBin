import platform

def Info():
    print("Platform: " + platform.system())
    print("Release" + platform.release())
    print("Cersion" + platform.version())
    print("Platform" + platform.platform())