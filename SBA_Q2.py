class Kardus:
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def volumeKardus(self):
        return self.panjang*self.lebar*self.tinggi

    def luasPermKardus(self):
        return 2*((self.panjang*self.lebar)+(self.panjang*self.tinggi)+(self.tinggi*self.lebar))
    
    def massaJenis(self, massa):
        return massa / self.volumeKardus()

    def output(self,massa):
        return 'volume : '+str(self.volumeKardus())+' \nluas_permukaan : '+str(self.luasPermKardus())+' \nmassa_jenis : '+str(self.massaJenis(massa))

if __name__ == "__main__":

    massa_kotakBiru = 10
    KotakBiru = Kardus(10,8,4)
    KotakBiru = KotakBiru.output(massa_kotakBiru)
    print('---Kotak Biru---')
    print(KotakBiru)

    print('\n')
    massa_kotakMerah = 12
    KotakMerah = Kardus(15,5,1)
    KotakMerah = KotakMerah.output(massa_kotakMerah)
    print('---Kotak Merah---')
    print(KotakMerah)

