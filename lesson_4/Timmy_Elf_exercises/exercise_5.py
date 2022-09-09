# Until stop

while True:

    text_input = input("Enter stop to quit: ")

    if(text_input == "stop"):
        break
    print(f'{text_input} has length {len(text_input)}')
    