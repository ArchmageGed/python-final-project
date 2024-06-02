#funqcia imisatvis, rom davabrunot swori input

def get_input(text, type):
    while True:
        try:
            user_input = input(text)
            if type == "int":
                user_input = int(user_input)
                return user_input
            elif type == "float":
                user_input = float(user_input)
                return user_input
            else:
                return user_input
        except ValueError:
            print("Invalid input :( Please try entering a valid value!")
