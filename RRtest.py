import copy
import queue
import pandas as pd

# Authors:
# Chantal van de Luijtgaarden


def data():
    data = pd.read_csv('adjusted dataset.csv', delimiter=';')
    # for i in range(1, len(data["gender"]) - 1):
    #     if (data["gender"][i]) == 1:
    #         print(data["gender"][i])
    return data


# Race and Religion
def RRtest(data):
    pos_race_pos_mat = 0
    neg_race_neg_mat = 0
    neg_race_pos_mat = 0
    pos_race_neg_mat = 0
    result = []

    for i in range(1,len(data["samerace"])):
        if (data["samerace"][i] == 1) and (data["match"][i]== 1):
            pos_race_pos_mat += 1
        elif (data["samerace"][i] == 0) and (data["match"][i] == 0):
            neg_race_neg_mat += 1
        elif (data["samerace"][i] == 0) and (data["match"][i] == 1):
            neg_race_pos_mat += 1
        elif (data["samerace"][i] == 1) and (data["match"][i] == 0):
            pos_race_neg_mat += 1

    result.append("PRPM  Result:")
    result.append(pos_race_pos_mat)
    result.append("NRNM  Result:")
    result.append(neg_race_neg_mat)
    result.append("NRPM  Result:")
    result.append(neg_race_pos_mat)
    result.append("PRNM  Result:")
    result.append(pos_race_neg_mat)

    print(result)
    return result


# Perceiving Yourself and Others Match
def PYOMtest(data):
    result = True
    return result


# Correlation Interest and Match Count
def CIMCtest(data):
    result = True
    return result


def main():
    dataset = data()
    rrresult = RRtest(dataset)
    pyomresult = PYOMtest(dataset)
    cimcresult = CIMCtest(dataset)
    print("Race and Religion Results", file=open("merged.txt", "a"))
    print(rrresult, file=open("merged.txt", "a"))
    print("Personal Interest Results", file=open("merged.txt", "a"))
    print(pyomresult, file=open("merged.txt", "a"))
    print("Correlation Interest and Match Results", file=open("merged.txt", "a"))
    print(cimcresult, file=open("merged.txt", "a"))


main()