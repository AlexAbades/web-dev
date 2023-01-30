class Device:
    def __init__(self, name, connected_by):
        self.name = name 
        self.connected_by = connected_by
        self.connected = True 

    def __str__(self):
        return f"Device {self.name!r} ({self.connected})"  # !r basically just puts quotation marks between

    def disconect(self):
        self.connected = False 
        print("Disconected.")

class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, capacity)  # super method it specifies that we want to obtain the __init__ method from the inherit class 
        self.capacity = capacity
        self.remaning_pages = capacity
    
    def __str__(self):
        return f"{super().__str__()} ({self.remaning_pages} pages remaining)"
    
    def print(self, pages):
        if not self.connected:
            print("Your device is not connected!")
            return
        print(f"Printing {pages} pages.")
        self.remaning_pages -= pages
    
if __name__ == "__main__":
    printer = Printer("Printer", "USB", 500)
    printer.print(40)
    print(printer)
    printer.disconect()
    printer.print(20)
