class TV:
    def __init__(self, canal = 1, volume = 10):
        self.canal = canal
        self.volume = volume
        self.lista_canais = {'1':"TV Cultura",'2':"SBT",'3':"Globo",'4':"Band",'5':"Record",'6':"MTV",'7':"Loading TV"}

    def mudar_canal(self,canal):
        if canal in "1234567":
            print(f"OK, vamos assistir agora ao canal: {self.lista_canais[canal]}")
        else:
            print("Canal não encontrado, digite um número de 1 a 7")
    
    def aumentar_volume(self,volume):
        self.volume += volume
        print(f"Pronto, agora o volume está em {self.volume}")
    
    def diminuir_volume(self,volume):
        volume = int(input("Digite o quanto terá de ser diminuido no volume: "))
        self.volume -= volume
        print(f"Pronto, agora o volume está em {self.volume}")

tv = TV()
volume = int(input("Digite o quanto terá de ser aumentado no volume: "))
tv.aumentar_volume(volume)
canal = input("Digite o canal que quer assistir: ")
tv.mudar_canal(canal)