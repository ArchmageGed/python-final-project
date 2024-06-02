class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    #produqtis monacemebis stringis formatshi gadayvana 
    #gvchirdeba davabrunot stringuli monacemi, rom chavwerot txt failshi
    def to_string(self):
        return f"{self.name}, {self.quantity}, {self.price}\n"
