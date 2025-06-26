import pandas as pd


def sequedna(genearq_txt):
    getsequence = open(genearq_txt)
    sequence = getsequence.read()
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
    data = {
        'A': ["DNA", "Tamanho", "Três Bases Iniciais",
              "Últimas Três Bases", "A", "T", "G", "C",
              "Sequência Complementar", "GCs", "RNA"],
        'B': [sequence, len(sequence), sequence[:3], sequence[-3:],
              sequence.count("A"), sequence.count("T"), sequence.count("G"), sequence.count("C"),
              sequence, sequence.count('G'), rnaseq]
    }

    dataframe = pd.DataFrame(data)
    dataframe.to_csv('dataframe.csv')
    dataframe.to_csv('dataframe.txt', sep='\t', index=False)


sequedna("SRY.txt")
