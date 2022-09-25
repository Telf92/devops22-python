# Until stop

while True:
    text = input("Enter text, or Enter stop to quit: ")
    if text == "stop":
        break
    print(f'{text} has length {len(text)}')