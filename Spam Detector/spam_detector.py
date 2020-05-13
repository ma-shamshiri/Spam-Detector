# Importing the libraries
import os
import re
import numpy as np


# Setting the path of the train files
train_path = "./train"


# Setting the path of the test files
test_path = "./test"


"*** Returns the number of all emails (train files) ***"


def number_of_allEmails():
    counter = 0
    for directories, subdirectories, files in os.walk(train_path):
        for filename in files:
            counter += 1

    return counter


"*** Returns the number of spam emails (train files) ***"


def number_of_spamEmails():
    counter = 0
    for directories, subdirectories, files in os.walk(train_path):
        for filename in files:
            if "spam" in filename:
                counter += 1

    return counter

"*** Returns the number of ham emails (train files) ***"


def number_of_hamEmails():
    counter = 0
    for directories, subdirectories, files in os.walk(train_path):
        for filename in files:
            if "ham" in filename:
                counter += 1

    return counter


"*** Parses the given text - (split format: [^a-zA-Z]) ***"


def text_parser(text):
    words = re.split("[^a-zA-Z]", text)
    lower_words = [word.lower() for word in words if len(word) > 0]

    return lower_words


"*** Returns the words of train data: (all_trainWords, spam_trainWords, ham_trainWords) ***"


def trainWord_generator():
    all_words = []
    spam_words = []
    ham_words = []

    for directories, subdirectories, files in os.walk(train_path):
        for filename in files:
            full_path = os.path.join(directories, filename)
            with open(full_path) as target_file:
                data = target_file.read()
                words = text_parser(data)
                for word in words:
                    all_words.append(word)
                    if "ham" in filename:
                        ham_words.append(word)
                    elif "spam" in filename:
                        spam_words.append(word)

    all_words = sorted(all_words)
    spam_words = sorted(spam_words)
    ham_words = sorted(ham_words)

    return all_words, spam_words, ham_words


"*** Returns all unique words ***"


def unique_words(all_trainWords):
    return sorted(list(set(all_trainWords)))


"*** Calculates the frequency of given words ***"


def frequency_calculator(words):
    wf = {}
    for word in words:
        if word in wf:
            wf[word] += 1
        else:
            wf[word] = 1

    return wf


"*** Returns the frequency of each word in spam and ham classes: (spam_bagOfWords, ham_bagOfWords) ***"


def bagOfWords_genarator(all_uniqueWords, spam_trainWords, ham_trainWords):
    spam_bagOfWords = frequency_calculator(spam_trainWords)
    ham_bagOfWords = frequency_calculator(ham_trainWords)

    for word in all_uniqueWords:
        if word not in spam_bagOfWords.keys():
            spam_bagOfWords[word] = 0
        if word not in ham_bagOfWords.keys():
            ham_bagOfWords[word] = 0

    spam_bagOfWords = dict(
        sorted(spam_bagOfWords.items(), key=lambda item: item[0]))
    ham_bagOfWords = dict(
        sorted(ham_bagOfWords.items(), key=lambda item: item[0]))

    return spam_bagOfWords, ham_bagOfWords


"*** Returns the smooothed Bag of Words: (smoothed_spamBOW, smoothed_hamBOW) ***"


def smoothed_bagOfWords(all_uniqueWords, spam_bagOfWords, ham_bagOfWords, delta):
    smoothed_spamBOW = {}
    smoothed_hamBOW = {}

    for word in spam_bagOfWords.keys():
        smoothed_spamBOW[word] = spam_bagOfWords[word] + delta
    for word in ham_bagOfWords.keys():
        smoothed_hamBOW[word] = ham_bagOfWords[word] + delta

    smoothed_spamBOW = dict(
        sorted(smoothed_spamBOW.items(), key=lambda item: item[0]))
    smoothed_hamBOW = dict(
        sorted(smoothed_hamBOW.items(), key=lambda item: item[0]))

    return smoothed_spamBOW, smoothed_hamBOW


"*** Calculates the probability of spam class: P(spam) ***"


def spam_probability(nb_of_allEmails, nb_of_spamEmails):
    return nb_of_spamEmails/nb_of_allEmails


""" Calculates the probability of ham class: P(ham) """


def ham_probability(nb_of_allEmails, nb_of_hamEmails):
    return nb_of_hamEmails/nb_of_allEmails


"*** Calculates P(Wi|spam) for each word ***"


def spam_condProbability(all_uniqueWords, spam_bagOfWords, smoothed_spamBOW, delta):
    spam_condProb = {}
    for word in smoothed_spamBOW.keys():
        wf = smoothed_spamBOW[word]
        total_wf = (sum(spam_bagOfWords.values()) +
                    (delta * len(all_uniqueWords)))
        spam_condProb[word] = (wf / total_wf)

    return spam_condProb


""" Calculates P(Wi|ham) for each word """


def ham_condProbability(all_uniqueWords, ham_bagOfWords, smoothed_hamBOW, delta):
    ham_condProb = {}
    for word in smoothed_hamBOW.keys():
        wf = smoothed_hamBOW[word]
        total_wf = (sum(ham_bagOfWords.values()) +
                    (delta * len(all_uniqueWords)))
        ham_condProb[word] = (wf / total_wf)

    return ham_condProb


"*** Generates the content of model.txt """


def model_output_generator(word_numbers, words, ham_wf, ham_cp, spam_wf, spam_cp):
    output = ""
    for index in range(0, word_numbers):
        output += f"{index + 1}  {words[index]}  {ham_wf[words[index]]}  {ham_cp[words[index]]}  {spam_wf[words[index]]}  {spam_cp[words[index]]}\n"

    return output


"*** Builds model.txt file ***"


def modelFileBuilder(model_output):
    model_file = open("model.txt", 'w')
    model_file.write(model_output)


"*** Returns the name of all emails (test files) ***"


def get_testFileNames():
    file_names = []
    for directories, subdirectories, files in os.walk(test_path):
        for filename in files:
            file_names += [filename]

    return file_names


"*** Returns the actual label (ham or spam) of each email ***"


def get_actualLabels():
    actual_label = []
    for directories, subdirectories, files in os.walk(test_path):
        for filename in files:
            if "ham" in filename:
                actual_label += ["ham"]
            else:
                actual_label += ["spam"]

    return actual_label


"*** Calculates the score of ham and spam for each email ***"


def score_calculator(all_uniqueWords, spam_prob, ham_prob, spam_condProb, ham_condProb, delta):
    actual_label = ""
    predicted_label = ""
    decision_label = ""

    ham_score_list = []
    spam_score_list = []

    predicted_label_list = []
    decision_label_list = []

    for directories, subdirectories, files in os.walk(test_path):
        for filename in files:
            actual_label = "ham" if "ham" in filename else "spam"
            full_path = os.path.join(directories, filename)
            with open(full_path, encoding="latin-1") as target_file:
                email_content = target_file.read()
                email_words = text_parser(email_content)

                sigma_spamScore = 0
                sigma_hamScore = 0

                for word in email_words:
                    if word in all_uniqueWords:
                        sigma_spamScore += np.log(spam_condProb[word])
                        sigma_hamScore += np.log(ham_condProb[word])

                spam_score = (np.log(spam_prob) + sigma_spamScore)
                spam_score_list.append(spam_score)

                ham_score = (np.log(ham_prob) + sigma_hamScore)
                ham_score_list.append(ham_score)

                predicted_label = "spam" if spam_score > ham_score else "ham"
                predicted_label_list += [predicted_label]

                decision_label = "right" if predicted_label == actual_label else "wrong"
                decision_label_list += [decision_label]

    return ham_score_list, spam_score_list, predicted_label_list, decision_label_list


"*** Generates the content of result.txt ***"


def result_output_generator(fileNumbers, fileNames, predictedLabels, hamScores, spamScores, actualLabels, decisionLabels):
    output = ""
    for index in range(0, fileNumbers):
        output += f"{index + 1}  {fileNames[index]}  {predictedLabels[index]}  {hamScores[index]}  {spamScores[index]}  {actualLabels[index]}  {decisionLabels[index]} \n"
    return output


"*** Builds result.txt file ***"


def resultFileBuilder(result_output):
    model_file = open("result.txt", 'w')
    model_file.write(result_output)


"*** Calculates Precision (spam class) - Formula: (True Positive / (True Positive + False Positive)) ***"


def get_spamPrecision(fileNumbers, actualLabels, predictedLabels):
    tp = 0
    fp = 0
    precision = 0

    for index in range(0, fileNumbers):
        if(actualLabels[index] == "spam" and actualLabels[index] == predictedLabels[index]):
            tp += 1
        if(actualLabels[index] == "ham" and predictedLabels[index] == "spam"):
            fp += 1

    precision = (tp / (tp + fp))

    return precision


"*** Calculates Recall (spam class) - Formula: (True Positive / (True Positive + False Negative)) ***"


def get_spamRecall(fileNumbers, actualLabels, predictedLabels):
    tp = 0
    fn = 0
    recall = 0

    for index in range(0, fileNumbers):
        if(actualLabels[index] == "spam" and actualLabels[index] == predictedLabels[index]):
            tp += 1
        if(actualLabels[index] == "spam" and predictedLabels[index] == "ham"):
            fn += 1

    recall = (tp / (tp + fn))

    return recall


"*** Calculates Accuracy (spam class) - Formula: (TP + TN) / (TP + FP + TN + FN) ***"


def get_spamAccuracy(fileNumbers, actualLabels, predictedLabels):
    tp = 0
    fp = 0
    tn = 0
    fn = 0
    accuracy = 0

    for index in range(0, fileNumbers):
        if(actualLabels[index] == "spam" and actualLabels[index] == predictedLabels[index]):
            tp += 1
        if(actualLabels[index] == "ham" and actualLabels[index] == predictedLabels[index]):
            tn += 1
        if(actualLabels[index] == "ham" and predictedLabels[index] == "spam"):
            fp += 1
        if(actualLabels[index] == "spam" and predictedLabels[index] == "ham"):
            fn += 1

    accuracy = ((tp + tn) / (tp + tn + fp + fn))

    return accuracy


""" Calculates F1-measure (spam class) - Formula: 2 * ((precision * recall) / (precision + recall)) """


def get_spamFmeasure(spam_precision, spam_recall):
    return (2 * ((spam_precision * spam_recall) / (spam_precision + spam_recall)))


"*** Returns confusion parameters for spam class: (TP, TN, FP, FN) ***"


def spamConfusionParams(fileNumbers, actualLabels, predictedLabels):
    tp = 0
    fp = 0
    tn = 0
    fn = 0
    accuracy = 0

    for index in range(0, fileNumbers):
        if(actualLabels[index] == "spam" and actualLabels[index] == predictedLabels[index]):
            tp += 1
        if(actualLabels[index] == "ham" and actualLabels[index] == predictedLabels[index]):
            tn += 1
        if(actualLabels[index] == "ham" and predictedLabels[index] == "spam"):
            fp += 1
        if(actualLabels[index] == "spam" and predictedLabels[index] == "ham"):
            fn += 1

    return tp, tn, fp, fn


"*** Calculates Precision (ham class) - Formula: (True Positive / (True Positive + False Positive)) ***"


def get_hamPrecision(fileNumbers, actualLabels, predictedLabels):
    tp = 0
    fp = 0
    precision = 0

    for index in range(0, fileNumbers):
        if(actualLabels[index] == "ham" and actualLabels[index] == predictedLabels[index]):
            tp += 1
        if(actualLabels[index] == "spam" and predictedLabels[index] == "ham"):
            fp += 1

    precision = (tp / (tp + fp))

    return precision


"*** Calculates Recall (ham class) - Formula: (True Positive / (True Positive + False Negative)) ***"


def get_hamRecall(fileNumbers, actualLabels, predictedLabels):
    tp = 0
    fn = 0
    recall = 0

    for index in range(0, fileNumbers):
        if(actualLabels[index] == "ham" and actualLabels[index] == predictedLabels[index]):
            tp += 1
        if(actualLabels[index] == "ham" and predictedLabels[index] == "spam"):
            fn += 1

    recall = (tp / (tp + fn))

    return recall


"*** Calculates Accuracy (ham class) - Formula: (TP + TN) / (TP + FP + TN + FN) ***"


def get_hamAccuracy(fileNumbers, actualLabels, predictedLabels):
    tp = 0
    fp = 0
    tn = 0
    fn = 0
    accuracy = 0

    for index in range(0, fileNumbers):
        if(actualLabels[index] == "ham" and actualLabels[index] == predictedLabels[index]):
            tp += 1
        if(actualLabels[index] == "spam" and actualLabels[index] == predictedLabels[index]):
            tn += 1
        if(actualLabels[index] == "spam" and predictedLabels[index] == "ham"):
            fp += 1
        if(actualLabels[index] == "ham" and predictedLabels[index] == "spam"):
            fn += 1

    accuracy = ((tp + tn) / (tp + tn + fp + fn))

    return accuracy


"*** Calculates F1-measure (ham class) - Formula: 2 * ((precision * recall) / (precision + recall)) ***"


def get_hamFmeasure(ham_precision, ham_recall):
    return (2 * ((ham_precision * ham_recall) / (ham_precision + ham_recall)))


"*** Returns confusion parameters for ham class: (TP, TN, FP, FN) ***"


def hamConfusionParams(fileNumbers, actualLabels, predictedLabels):
    tp = 0
    fp = 0
    tn = 0
    fn = 0
    accuracy = 0

    for index in range(0, fileNumbers):
        if(actualLabels[index] == "ham" and actualLabels[index] == predictedLabels[index]):
            tp += 1
        if(actualLabels[index] == "spam" and actualLabels[index] == predictedLabels[index]):
            tn += 1
        if(actualLabels[index] == "spam" and predictedLabels[index] == "ham"):
            fp += 1
        if(actualLabels[index] == "ham" and predictedLabels[index] == "spam"):
            fn += 1

    return tp, tn, fp, fn


"*** Creates a table of the Evaluation Results ***"


def evaluation_result(spam_accuracy, spam_precision, spam_recall, spam_fmeasure, ham_accuracy, ham_precision, ham_recall, ham_fmeasure):
    output = ""

    output += "################################################################################## \n"
    output += "#                           *** Evaluation Results ***                           # \n"
    output += "#                                                                                # \n"
    output += "#                  Accuracy |     Precission    | Recall |     F1-measure        # \n"
    output += "# ==========================|===================|========|====================== # \n"
    output += f"#  Spam Class :    {spam_accuracy}   |{spam_precision} | {spam_recall}   | {spam_fmeasure}    # \n"
    output += "# --------------------------|-------------------|--------|---------------------- # \n"
    output += f"#  Ham  Class :    {ham_accuracy}   |{ham_precision} | {ham_recall}  | {ham_fmeasure}    # \n"
    output += "#                           |                   |        |                       # \n"
    output += "################################################################################## \n"

    return output


"*** Creates the Confusion Matrix for spam class ***"


def spam_confusionMatrix(tp, tn, fp, fn):
    output = ""

    output += "             ########################################################### \n"
    output += "             #          *** Confusion Matrix (Spam Class) ***          # \n"
    output += "             #                                                         # \n"
    output += "             #                |    Spam     |     Ham     |            # \n"
    output += "             #      ==========|=============|=============|======      # \n"
    output += f"             #        Spam    |  TP = {tp}   |  FN = {fn}    |            # \n"
    output += "             #      ==========|=============|=============|======      # \n"
    output += f"             #        Ham     |  FP = {fp}     |  TN = {tn}   |            # \n"
    output += "             #                |             |             |            # \n"
    output += "             ########################################################### \n"

    return output


"*** Creates the Confusion Matrix for ham class ***"


def ham_confusionMatrix(tp, tn, fp, fn):
    output = ""

    output += "             ########################################################### \n"
    output += "             #          *** Confusion Matrix (Ham Class) ***           # \n"
    output += "             #                                                         # \n"
    output += "             #                |    Spam     |     Ham     |            # \n"
    output += "             #      ==========|=============|=============|======      # \n"
    output += f"             #        Spam    |  TP = {tp}   |  FN = {fn}     |            # \n"
    output += "             #      ==========|=============|=============|======      # \n"
    output += f"             #        Ham     |  FP = {fp}    |  TN = {tn}   |            # \n"
    output += "             #                |             |             |            # \n"
    output += "             ########################################################### \n"

    return output


"*** Generates the content of evaluation.txt ***"


def evaluation_output_generator(evaluation_result_output, spam_confusionMatrix_output, ham_confusionMatrix_output):
    output = ""

    output += evaluation_result_output

    output += "\n"
    output += "\n"
    output += "\n"

    output += spam_confusionMatrix_output

    output += "\n"
    output += "\n"
    output += "\n"

    output += ham_confusionMatrix_output

    return output


"*** Builds evaluation.txt file ***"


def evaluationFileBuilder(evaluation_output):
    model_file = open("evaluation.txt", 'w')
    model_file.write(evaluation_output)
