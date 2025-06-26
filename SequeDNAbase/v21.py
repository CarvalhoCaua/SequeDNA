import pandas as pd


def sequedna_v2(genearq_txt):
    getsequence = open(genearq_txt)
    sequence = getsequence.read()
    print("Sequência do Gene: {}".format(sequence))
    print("Tamanho do Gene: {}".format(len(sequence)))
    print("Primeiras Três Bases: {}".format(sequence[:3]))
    print("Últimas Três Bases: {}".format(sequence[-3:]))
    print("Quantidades de Adenina (A): {}".format(sequence.count("A")))
    print("Quantidades de Timina (T): {}".format(sequence.count("T")))
    print("Quantidades de Guanina (G): {}".format(sequence.count("G")))
    print("Quantidades de Citosina (C): {}".format(sequence.count("C")))
    sequencecomp = ''
    for i in sequence:
        if i == "A":
            sequencecomp += "T"
        elif i == "T":
            sequencecomp += "A"
        elif i == "C":
            sequencecomp += "G"
        elif i == "G":
            sequencecomp += "C"
    print(f"Sequência Complementar: {sequencecomp}")
    print(f"Quantidade de Ligações GCs: {sequence.count('G')}")
    rnaseq = ''
    for i in sequence:
        if i == "A":
            rnaseq += "A"
        elif i == "T":
            rnaseq += "U"
        elif i == "C":
            rnaseq += "G"
        elif i == "G":
            rnaseq += "C"
    print(f"Sequência Transcrita (RNA): {rnaseq}")
    data = {
        'A': ["DNA", "Tamanho", " Três Bases Iniciais",
              "Últimas Três Bases", "A", "T", "G", "C",
              "Sequência Complementar", "GCs", "RNA"],
        'B': [sequence, len(sequence), sequence[:3], sequence[-3:],
              sequence.count("A"), sequence.count("T"), sequence.count("G"), sequence.count("C"),
              sequence, sequence.count('G'), rnaseq]
    }

    dataframe = pd.DataFrame(data)
    print(dataframe)
    dataframe.to_csv('dataframe.csv')


sequedna_v2("SRY.txt")
