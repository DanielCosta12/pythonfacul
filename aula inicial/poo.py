

class Tv:
    def __init__(self):
        self.volume = 0

    def aumentar_volume(self):
        self.volume += 1

    def diminuir_volume(self):
        self.volume -= 1


tv = Tv()
print("Volume ao ligar a TV = ", tv.volume)
tv.aumentar_volume()
print("Volume atual = ", tv.volume)
