def Update_letter(kata_rahasia, tebakanmu):
    display = ""
    for kata in kata_rahasia:
     if kata.isalpha():
        if kata.lower() in tebakanmu:
            display += kata
        else:
            display += "_"
     else:
            display+=kata
    return display

kata_rahasia= "nyala"
tebakanmu = []
kesempatanmu = 6


while kesempatanmu > 0:
    tebak = input("Tabaklah kata rahasianya kawan: ")
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
    display=Update_letter(kata_rahasia, tebakanmu)
    print(display)
    if tebak == kata_rahasia:
        print("Selamat kamu benar. kamu berhasil nyawa kamu ada {}".format(kesempatanmu))
if kesempatanmu==0:
    print(f"Maaf kamu telah kalah. Jawabannya{kata_rahasia}")

