def makePPM(filename, w, h,):
    f = open(filename + ".ppm", "w+")
    f.write("P3" + "\n" + w + " " + h + "\n" + "255" + "\n")
    G = 0
    B = 0

    for i in range(2000):
        f.write("0 " + str(G) + " " + str(B) + " ")
        G += 1
        B += 1
        if (i % 50 == 0 and i > 0):
            f.write("\n")
        if (G > 255):
            G = 0
        if (B > 255):
            B = 0

makePPM("pic", "50", "40")
