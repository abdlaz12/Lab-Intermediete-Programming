kata_rahasia= "loveu"
tebakanmu = []
kesempatanmu = 6
while kesempatanmu > 0:
    display = ""
    for kata in kata_rahasia:
        if kata.lower() in tebakanmu:
            display += kata
        else:
            display += "_"
    print(display)
    if "_" not in display:
        print("Salamat kamu benar: ", kata_rahasia)
        print('Horeee, we did it mas bro')
        break
    tebak = input("Tebaklah kata rahasiaku kawan: ")
    if len(tebak) != 1:
        print("Masukkan minimal satu huruf")
    elif not tebak.isalpha():
        print("Kasih aku huruf sobat")
    if tebak.lower() in tebakanmu:
        print("kau dah tebak ituu")
    else:
        tebakanmu.append(tebak.lower())
        if tebak.lower() in kata_rahasia.lower():
            print("Salamat kamu benar sobat")   
        else:
            kesempatanmu -= 1
            print("Semoga kamu beruntung. Kamu ada {} kesempatan lagi.".format(kesempatanmu))
if kesempatanmu == 0:
        print(f"Sorry kesempatan kamu dah abis, ini jawabannya {kata_rahasia}")
       
