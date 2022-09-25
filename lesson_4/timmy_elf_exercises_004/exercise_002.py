#VIP

vip = ("pelle", "lisa", "olle", "evert", "frida")
name = input("Write your name: ")

if name in vip:
    print(f"Welcome{name} you're on the list")
else:
    print("Sorry, you're not on the list")