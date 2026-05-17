# Game Character Battle

class Character: #parent class
    def __init__(self, nama, hp, attack):
        self.nama = nama
        self.hp = hp
        self.attack = attack

    def tampil_status(self):
        print("=== STATUS CHARACHTER ===")
        print(f"Nama    : {self.nama}")
        print(f"HP      : {self.hp}")           
        print(f"Attack  : {self.attack}")

    def serang(self, musuh):
        musuh.hp -= self.attack
        print(f"{self.nama} menyerang {musuh.nama}")
        print(f"HP {musuh.nama} berkurang {self.attack}")
    
class Warrior(Character):
    def __init__(self, nama, hp, attack, armor):
        super().__init__(nama, hp, attack)
        self.armor = armor
    
    def skill_tebas(self):
        print(f"{self.nama} menggunakan skill Tebasan Pedang")

    def tampil_status(self):
        super().tampil_status()
        print(f"Armor   : {self.armor}")
        print()

class Mage(Character):
    def __init__(self, nama, hp, attack, mana):
        super().__init__(nama, hp, attack)
        self.mana = mana
        
    def skill_api(self):
        print(f"{self.nama} menggunakan skill Bola Api")

    def tampil_status(self):
        super().tampil_status()
        print(f"Mana    : {self.mana}")
        print()

class Archer(Character):
    def __init__(self, nama, hp, attack, panah):
        super().__init__(nama, hp, attack)
        self.panah = panah

    def skill_panah(self):
        print(f"{self.nama} menggunakan skill Hujan Panah")

    def tampil_status(self):
        super().tampil_status()
        print(f"Panah   : {self.panah}")
        print()

# Program Utama
warrior1 = Warrior ("Arthur", 120, 25, 15) #nama, hp, attack, armor
mage1 = Mage("Luna", 80, 30, 100) #nama, hp, attack, mana
archer1 = Archer("Robin", 90, 20, 40) #nama, hp, attack,  panah

# Menampilkan status character
warrior1.tampil_status()
mage1.tampil_status()
archer1.tampil_status()

#menggunakan skill
warrior1.skill_tebas()
mage1.skill_api()
archer1.skill_panah()

print()

#battle sederhana
warrior1.serang(mage1)

print(f"Sisa HP {mage1.nama} : {mage1.hp}")