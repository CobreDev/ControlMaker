name = input("What's the name of this package? ")
package = input("What's the Bundle ID (e.g. com.mac-user669.zenithdark)? ")
version = input("What's the version? ")
maintainer = input("Who made this package? ")
depends = input("What does this depend on? ")
section = input("What section is this in (Themes, Tweaks, etc.)? ")
description = input("Give a short description? ")
depiction = input("Link to the depiction ")
sileodepiction = input("Link to the Sileo depiction json ")
author = maintainer



f = open("control", "w")
f.write(name + "\n")
f.write(package + "\n")
f.write(version + "\n")
f.write(maintainer + "\n")
f.write(section + "\n")
f.write(description + "\n")
f.write(author + "\n")
f.write(depends + "\n")
f.write(depiction + "\n")
f.write(sileodepiction + "\n")
f.close()

#open and read the file after the appending:
f = open("control", "r")
print(f.read())

