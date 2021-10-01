#import packages
from vtclear import clear_screen
# array 2 dimensi & data sesuai grafik
kelompok_umur = [[25, 35, 45, 55, 65],
                 [
                     'MUDA', 
                     'MUDA 0.5 & SETENGAH BAYA 0.5', 
                     'SETENGAH BAYA',
                     'SETENGAH BAYA 0.5 & TUA 0.5',
                     'TUA '
                 ]]

#fungsi
def mulai():
    print("\n====================================")
    print("Pengelompokan Usia pada System Fuzzy")
    print("====================================")
    print("Created By Arizki Putra Rahman\n")
    print("Alert ! umur hanya terdiri 25,35,45,55,65")
    #input
    umur = int(input("Masukkan umur anda : "))
    #kondisional
    if (umur in kelompok_umur[0]):
        #looping
        for i in range(len(kelompok_umur[0])):
            if (umur == kelompok_umur[0][i]):
                print(
                    f"\nAnda berusia {kelompok_umur[0][i]} tahun termasuk {kelompok_umur[1][i]}"
                )
    else:
        print("\nUmur yang anda masukan tidak ada dalam data")
    ulang = input("\nApakah anda ingin mengulang (ya/tidak)? ")
    if (ulang == "ya" or ulang == "Ya"):
        clear_screen()
        mulai()
    else:
        print("\nSampai Jumpa ! Salam hangat dari Mimin")

#PerintahAwal
mulai()
