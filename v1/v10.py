import pandas as pd

#Análise simples de uma sequência de DNA

gene = "GATGGAACTTGACTACGTAAATT"

print("Sequência do Gene: {}".format(gene))
print("Tamanho do Gene: {}".format(len(gene)))
print("Primeiras Três Bases: {}".format(gene[:3]))
print("Últimas Três Bases: {}".format(gene[-3:]))
print("Quantidades de Adenina (A): {}".format(gene.count("A")))
print("Quantidades de Timina (T): {}".format(gene.count("T")))
print("Quantidades de Guanina (G): {}".format(gene.count("G")))
print("Quantidades de Citosina (C): {}".format(gene.count("C")))
genec = ''
for i in gene:
    if i == "A":
        genec += "T"
    elif i == "T":
        genec += "A"
    elif i == "C":
        genec += "G"
    elif i == "G":
        genec += "C"
print(f"Sequência Complementar: {genec}")
print(f"Quantidade de Ligações GCs: {gene.count('G')}")
rnaseq = ''
for i in gene:
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
    'B': [gene, len(gene), gene[:3], gene[-3:],
          gene.count("A"), gene.count("T"), gene.count("G"), gene.count("C"),
          genec, gene.count('G'), rnaseq]
}

dataframe = pd.DataFrame(data)
print(dataframe)
dataframe.to_csv('dataframe.csv')
