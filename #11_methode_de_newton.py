def newton_et_ces_methodes_petes_couilles(x):
    while True:
        y = (x + 2/x) / 2
        print(y)

        if (x >= y):
            difference = x - y
        else:
            difference = y - x 

        if difference < 10 ** -6:
           break
        
        x = y

newton_et_ces_methodes_petes_couilles(2)