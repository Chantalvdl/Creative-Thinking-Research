import copy
import queue
import pandas as pd

# Authors:
# Chantal van de Luijtgaarden


def data():
    data = pd.read_csv('adjusted dataset.csv', delimiter=';')
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


# Correlation Interest and Match Count
def CIMCtest(data):
    extneg_match = 0
    extneg_no_mat = 0
    neg_match = 0
    neg_no_mat = 0
    extpos_match = 0
    extpos_no_mat = 0
    pos_match = 0
    pos_no_mat = 0
    result_match = []
    result_no_match = []

    for i in range(1, len(data["int_corr"])):
        if (data["int_corr"][i] >= 0.5) and (data["match"][i] == 1):
            extpos_match += 1
        elif (data["int_corr"][i] >= 0.5) and (data["match"][i] == 0):
            extpos_no_mat += 1
        elif (data["int_corr"][i] <= -0.5) and (data["match"][i] == 1):
            extneg_match += 1
        elif (data["int_corr"][i] <= -0.5) and (data["match"][i] == 0):
            extneg_no_mat += 1
        elif (data["int_corr"][i] < 0.5) and (data["int_corr"][i] > 0) and (data["match"][i] == 1):
            pos_match += 1
        elif (data["int_corr"][i] < 0.5) and (data["int_corr"][i] > 0) and (data["match"][i] == 0):
            pos_no_mat += 1
        elif (data["int_corr"][i] > -0.5) and (data["int_corr"][i] <= 0) and (data["match"][i] == 1):
            neg_match += 1
        elif (data["int_corr"][i] > -0.5) and (data["int_corr"][i] <= 0) and (data["match"][i] == 0):
            neg_no_mat += 1

    result_match.append(extneg_match)
    result_match.append(neg_match)
    result_match.append(pos_match)
    result_match.append(extpos_match)
    result_no_match.append(extneg_no_mat)
    result_no_match.append(neg_no_mat)
    result_no_match.append(pos_no_mat)
    result_no_match.append(extpos_no_mat)

    print(result_match)
    print(result_no_match)
    return result_match, result_no_match


# Perceiving Yourself and Others Match
def PYOMtest(data):
    # attractive attr3_1 and 5_1 and attr
    high_simattr_match = 0
    high_simattr_nomatch = 0
    for i in range(1, len(data["attr3_1"])):

    # sincere sinc3_1 and 5_1 and sinc
    high_simsin_match = 0
    high_simsin_nomatch = 0

    # intelligent int3_1 and 5_1 and intel
    high_simint_match = 0
    high_simint_nomatch = 0

    # fun fun3_1 and 5_1 fun
    high_simfun_match = 0
    high_simfun_nomatch = 0

    # ambitious amb3_1 and 5_1 and amb
    high_simamb_match = 0
    high_simamb_nomatch = 0

    return result


def main():
    dataset = data()
    rrresult = RRtest(dataset)
    pyomresult = PYOMtest(dataset)
    cimcresult, cimcresult2 = CIMCtest(dataset)
    print("Race and Religion Results", file=open("merged.txt", "a"))
    print(rrresult, file=open("merged.txt", "a"))

    print("Correlation Interest and Match Results", file=open("merged.txt", "a"))
    print("Match: Extreme Negative, Negative, Positive, Extreme Positive", file=open("merged.txt", "a"))
    print(cimcresult, file=open("merged.txt", "a"))
    print("No Match: Extreme Negative, Negative, Positive, Extreme Positive", file=open("merged.txt", "a"))
    print(cimcresult2, file=open("merged.txt", "a"))

    print("Personal Interest Results", file=open("merged.txt", "a"))
    print(pyomresult, file=open("merged.txt", "a"))

main()