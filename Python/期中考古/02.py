def main():
    while True:
        inp = input()
        if inp == "-1":
            break
        else:
            h, w = inp.split()
            h = int(h)
            w = int(w)
            w *= 0.454
            if not 50 <= h <= 250:
                print("Input Height Error")
                continue
            elif not 20 <= w <= 300:
                print("Input Weight Error")
                continue
            bmi = round(w / (h / 100) ** 2, 3)
            if bmi > 24:
                print("BMI too high")
            elif bmi < 18.5:
                print("BMI too low")
            else:
                print("%.2f" % bmi)


main()

# 15 min
