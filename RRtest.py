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

    for i in range(0,len(data["samerace"])):
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

    for i in range(0, len(data["int_corr"])):
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
    result_attr = []
    result_sinc = []
    result_intel = []
    result_fun = []
    result_amb = []

    # attractive attr3_1 and 5_1 and attr
    high_simattr3_match = 0
    high_simattr3_nomatch = 0
    high_simattr5_match = 0
    high_simattr5_nomatch = 0
    print(abs(data["fun3_1"][0] - data["fun"][0]))
    for i in range(0, len(data["attr3_1"])):
        if (abs(data["attr3_1"] - data["attr"]) <= 1) and (data["match"] == 1):
            high_simattr3_match += 1
        elif (abs(data["attr3_1"] - data["attr"]) <= 1) and (data["match"] == 0):
            high_simattr3_nomatch += 1
        elif (abs(data["attr5_1"] - data["attr"]) <= 1) and (data["match"] == 1):
            high_simattr5_match += 1
        elif (abs(data["attr5_1"] - data["attr"]) <= 1) and (data["match"] == 0):
            high_simattr5_nomatch += 1

    # sincere sinc3_1 and 5_1 and sinc
    high_simsin3_match = 0
    high_simsin3_nomatch = 0
    high_simsin5_match = 0
    high_simsin5_nomatch = 0
    for i in range(0, len(data["sinc3_1"])):
        if (abs(data["sinc3_1"] - data["sinc"]) <= 1) and (data["match"] == 1):
            high_simsin3_match +=1
        elif (abs(data["sinc3_1"] - data["sinc"]) <= 1) and (data["match"] == 0):
            high_simsin3_nomatch += 1
        elif (abs(data["sinc5_1"] - data["sinc"]) == 1) and (data["match"] == 1):
            high_simsin5_match += 1
        elif (abs(data["sinc5_1"] - data["sinc"]) == 1) and (data["match"] == 0):
            high_simsin5_nomatch += 1

    # intelligent int3_1 and 5_1 and intel
    high_simint3_match = 0
    high_simint3_nomatch = 0
    high_simint5_match = 0
    high_simint5_nomatch = 0
    for i in range(0, len(data["int3_1"])):
        if (abs(data["int3_1"] - data["intel"]) == 1) and (data["match"] == 1):
            high_simint3_match +=1
        elif (abs(data["int3_1"] - data["intel"]) == 1) and (data["match"] == 0):
            high_simint3_nomatch += 1
        elif (abs(data["int5_1"] - data["intel"]) == 1) and (data["match"] == 1):
            high_simint5_match += 1
        elif (abs(data["int5_1"] - data["intel"]) == 1) and (data["match"] == 0):
            high_simint5_nomatch += 1

    # fun fun3_1 and 5_1 fun
    high_simfun3_match = 0
    high_simfun3_nomatch = 0
    high_simfun5_match = 0
    high_simfun5_nomatch = 0
    for i in range(0, len(data["fun3_1"])):
        if (abs(data["fun3_1"][i] - data["fun"][i]) == 1) and (data["match"] == 1):
            high_simfun3_match += 1
        elif (abs(data["fun3_1"][i] - data["fun"][i]) == 1) and (data["match"] == 0):
            high_simfun3_nomatch += 1
        elif (abs(data["fun5_1"] - data["fun"]) == 1) and (data["match"] == 1):
            high_simfun5_match += 1
        elif (abs(data["fun5_1"] - data["fun"]) == 1) and (data["match"] == 0):
            high_simfun5_nomatch += 1

    # ambitious amb3_1 and 5_1 and amb
    high_simamb3_match = 0
    high_simamb3_nomatch = 0
    high_simamb5_match = 0
    high_simamb5_nomatch = 0
    for i in range(0, len(data["amb3_1"])):
        if (abs(data["amb3_1"] - data["amb"]) == 1) and (data["match"] == 1):
            high_simamb3_match += 1
        elif (abs(data["amb3_1"] - data["amb"]) == 1) and (data["match"] == 0):
            high_simamb3_nomatch += 1
        elif (abs(data["amb5_1"] - data["amb"]) == 1) and (data["match"] == 1):
            high_simamb5_match += 1
        elif (abs(data["amb5_1"] - data["amb"]) == 1) and (data["match"] == 0):
            high_simamb5_nomatch += 1

    # Appending result to lists
    result_attr.append(high_simattr3_match)
    result_attr.append(high_simattr3_nomatch)
    result_attr.append(high_simattr5_match)
    result_attr.append(high_simattr5_nomatch)
    result_sinc.append(high_simsin3_match)
    result_sinc.append(high_simsin3_nomatch)
    result_sinc.append(high_simsin5_match)
    result_sinc.append(high_simsin5_nomatch)
    result_intel.append(high_simint3_match)
    result_intel.append(high_simint3_nomatch)
    result_intel.append(high_simint5_match)
    result_intel.append(high_simint5_nomatch)
    result_fun.append(high_simfun3_match)
    result_fun.append(high_simfun3_nomatch)
    result_fun.append(high_simfun5_match)
    result_fun.append(high_simfun5_nomatch)
    result_amb.append(high_simamb3_match)
    result_amb.append(high_simamb3_nomatch)
    result_amb.append(high_simamb5_match)
    result_amb.append(high_simamb5_nomatch)

    return result_attr, result_sinc, result_intel, result_fun, result_amb


def main():
    dataset = data()
    rrresult = RRtest(dataset)
    cimcresult, cimcresult_no = CIMCtest(dataset)
    pyomres_attr, pyomres_sinc, pyomres_intel, pyomres_fun, pyomres_amb = PYOMtest(dataset)

    print("Race and Religion Results", file=open("merged.txt", "a"))
    print(rrresult, file=open("merged.txt", "a"))

    print("Correlation Interest and Match Results", file=open("merged.txt", "a"))
    print("Match: Extreme Negative, Negative, Positive, Extreme Positive", file=open("merged.txt", "a"))
    print(cimcresult, file=open("merged.txt", "a"))
    print("No Match: Extreme Negative, Negative, Positive, Extreme Positive", file=open("merged.txt", "a"))
    print(cimcresult_no, file=open("merged.txt", "a"))

    print("Personal Interest Results", file=open("merged.txt", "a"))
    print(pyomres_attr, file=open("merged.txt", "a"))
    print(pyomres_sinc, file=open("merged.txt", "a"))
    print(pyomres_intel, file=open("merged.txt", "a"))
    print(pyomres_fun, file=open("merged.txt", "a"))
    print(pyomres_amb, file=open("merged.txt", "a"))


main()