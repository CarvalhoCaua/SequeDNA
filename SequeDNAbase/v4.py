amostra = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
amostracomplementar = ''
for i in amostra:
    if i == "A":
        amostracomplementar += "T"
    elif i == "T":
        amostracomplementar += "A"
    elif i == "C":
        amostracomplementar += "G"
    elif i == "G":
        amostracomplementar += "C"
print(amostracomplementar)
