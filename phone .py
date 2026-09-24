
class Phone:
    def __init__(self,brand,model,color):
        self.brand=brand
        self.model=model
        self.color=color

    def deviceinfo(self):
        print(f"BRAND : {self.brand}")
        print(f"MODEL: {self.model}")
        print(f"COLOR : {self.color}")

class android(Phone):
    def __init__(self,brand,model,color,ram,rom):
        super(). __init__(brand,model,color)
        self.ram=ram
        self.rom=rom

    def aboutdevice(self):
        super().deviceinfo()
        print(f"RAM : {self.ram}")    
        print(f"ROM : {self.rom}")

a1=android("NOTHING "," phone 3a","black","8gb","256gb")
a1.aboutdevice()              

