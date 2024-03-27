kata_rahasia= "brody"
tebakanmu = []
kesempatanmu = 6
while True:
    
    tebak = input("Tabaklah kata rahasiaku kawan: ")
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
        elif kata_rahasia == tebakanmu:
            break
