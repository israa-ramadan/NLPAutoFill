import nltk as nltk
import re
import os


def ReadDataSet(path, path2):
    f2 = open(path2, "w")
    j = 0
    for i in os.listdir(path):
        print(i)
        f = open(path + "//" + i, "r")
        read = f.read()
        read += "\n"
        f2.write(read)
        f.close()
        if j == 1000:
            break
        j += 1
    f2.close()


# ReadDataSet(
#     "D://Iseul//Education//College//(4)_2nd_Semester//Artificial Intelligence_Selected2//Assignment2//archive1//Sports",
#     "D://Iseul//Education/College//(4)_2nd_Semester//Artificial Intelligence_Selected2//Assignment2//SportsDatabase.txt")


prob_dict = {}


def Ngram():
    file = open(
        "SportsDatabase.txt",
        "r", encoding="UTF-8")
    paragraphs = file.read()
    file.close()

    paragraphs = re.sub('[^\s0-9.ء-ي]', '', paragraphs)

    List_paragraphs = paragraphs.split(".")

    unigram_dict = {}
    bigram_dict = {}
    prob_dict = {}

    for paragraph in List_paragraphs:
        words = paragraph.split()

        for each_word in words:
            if each_word in unigram_dict:
                unigram_dict[each_word] += 1
            else:
                unigram_dict[each_word] = 1
    # print(unigram_dict)
    for paragraph in List_paragraphs:
        words = paragraph.split()
        bigram_list = list(nltk.bigrams(words))

        for term in bigram_list:
            if term in bigram_dict:
                bigram_dict[term] += 1
            else:
                bigram_dict[term] = 1
    # print(bigram_list)
    for double in bigram_dict:
        bi = bigram_dict[double]
        uni = unigram_dict[double[0]]
        prob = bi / uni
        prob_dict[double] = prob
    return prob_dict


def Autofill(query):
    ngramProb_dict = Ngram()
    print(ngramProb_dict)

    temp = query.split()
    unii = temp[-1]

    # print(NgramProb_dict)
    result = {}
    for t in ngramProb_dict:
        if t[0] == unii:
            result[t] = ngramProb_dict[t]

    result = sorted(result.items(), key=lambda x: x[1], reverse=True)

    suggestions = []
    if len(result) == 0:
        print("There is no result for this query")
    else:
        lenght = 10
        if len(result) < 10:
            lenght = len(result)
        for z in range(lenght):
            x, y = result[z]
            finalResult = query + " " + x[1]
            suggestions.append(query + " " + x[1])
    # print(suggestions)
    return suggestions

# input_query = input("\n\nEnter your query: ")
# Autofill(input_query)
