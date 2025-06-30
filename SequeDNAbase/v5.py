
amostra = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
amostrarna = ''
for i in amostra:
    if i == "A":
        amostrarna += "A"
    elif i == "T":
        amostrarna += "U"
    elif i == "C":
        amostrarna += "G"
    elif i == "G":
        amostrarna += "C"
print(amostrarna)
