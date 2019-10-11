mata_pel = {
    '001':'Bahasa Indonesia',
    '002':'Bahasa Inggris',
    '003':'Matematika',
    '004':'Biologi',
    '005':'Fisika'
}

def cetak_matapel(data):

    result = '\nKode Mata Kuliah   Mata Kuliah\n'
    for key,val in data.items():
        result+=key+' ==> '+val+'\n'
    
    return result

print('Sekarang Terdapat '+str(len(mata_pel))+' mata pelajaran')
print('Sebelum kode 003 dan 005 diganti \n')

print(cetak_matapel(mata_pel))
mata_pel['003'] = 'Kimia' #mengganti kode 003 menjadi Kimia
mata_pel['005'] = 'Olahraga' #mengganti kode 005 menjadi Olahraga
print('\nSetelah kode 003 dan 005 diganti \n')
print(cetak_matapel(mata_pel))

print('masukkan jumlah data baru :')
n = int(input())

print('masukkan data Kode Mata Pelajaran dan Nama Mata Pelajaran dipisahkan dengan spasi :')

for i in range(n):
    
    item  = list(map(str,input().split(' ')))
    mata_pel[item[0]] = item[1]

print(cetak_matapel(mata_pel))
