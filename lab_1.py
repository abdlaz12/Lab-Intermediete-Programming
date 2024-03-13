kata_rahasia= "Opungku"
tabakanmu = []
kesempatanmu = 6
while chances > 0:
    tebak = input("Tabaklah kata rahasiaku kawan: ")
    if len(tebak) != 1:
        print("Masukkan minimal satu huruf")
    elif not tebak.isalpha():
        print("Kasih aku huruf sobat")
    elif tebak.lower() in tebakanmu:
        print("kau dah tebak ituu")
    else:
        tebakanmu.append(tebak.lower())
    if tebak.lower() in kata_rahasia.lower():
        print("Salamat kamu benar sobat")
    else:
        kesempatanmu -= 1
        print("Semoga kamu beruntung. Kamu ada {} kesempatan lagi.".format(kesempatanmu))
    display = ""
    for kata in kata_rahasia:
            if kata.lower() in tebakanmu:
                display += kata
            else:
                display += "_"
                print(display)
                if "_" not in display:
                    print("Salamat kamu benar: ", kata_rahasia)
                if kesempatanmu == 0:
                    print("Sorry kesempatan kamu dah abis, anjing mu mati: Depo dulu", kata_rahasia)

    
# kata_rahasia='taik'
# tebakan=[]
# kesempatan=6
# while kesempatan>0:
#     tebak=input('Masukkan tebakanmu')
#     if tebak!=kata_rahasia:
#         kesempatan-=1
#         print('kamu salah coba lagi')
#     else:
#         print('kamu benar yeee')
