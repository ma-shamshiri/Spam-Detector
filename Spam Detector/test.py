################################################
"*************** TESTING PHASE ***************"
################################################


# Importing the spam_detector and train file to use the required functions
import spam_detector as sd


"************** MAIN FUNCTION **************"
"*** Defines main function for test.py ***"


def mainFunction():

    #     name of all emails
    test_fileNames = sd.get_testFileNames()


#     number of all emails
    nb_of_allEmails = sd.number_of_allEmails()


#     number of spam emails
    nb_of_spamEmails = sd.number_of_spamEmails()


#     number of ham emails
    nb_of_hamEmails = sd.number_of_hamEmails()


#     words of train data: (all_trainWords, spam_trainWords, ham_trainWords)
    all_trainWords, spam_trainWords, ham_trainWords = sd.trainWord_generator()


#     all unique words
    all_uniqueWords = sd.unique_words(all_trainWords)


#     frequency of each word in spam and ham classes: (spam_bagOfWords, ham_bagOfWords)
    spam_bagOfWords, ham_bagOfWords = sd.bagOfWords_genarator(
        all_uniqueWords, spam_trainWords, ham_trainWords)


#     smooothed Bag of Words: (smoothed_spamBOW, smoothed_hamBOW)
    smoothed_spamBOW, smoothed_hamBOW = sd.smoothed_bagOfWords(
        all_uniqueWords, spam_bagOfWords, ham_bagOfWords, 0.5)


#     probability of spam class: P(spam)
    spam_prob = sd.spam_probability(nb_of_allEmails, nb_of_spamEmails)


#     probability of ham class: P(ham)
    ham_prob = sd.ham_probability(nb_of_allEmails, nb_of_hamEmails)


#     P(Wi|spam) for each word
    spam_condProb = sd.spam_condProbability(
        all_uniqueWords, spam_bagOfWords, smoothed_spamBOW, 0.5)


#     P(Wi|ham) for each word
    ham_condProb = sd.ham_condProbability(
        all_uniqueWords, ham_bagOfWords, smoothed_hamBOW, 0.5)


#     actual label (ham or spam) of each email
    actual_labels = sd.get_actualLabels()


#     score of ham and spam as well as predicted label and decision label for each email
    ham_scores, spam_scores, predicted_labels, decision_labels = sd.score_calculator(
        all_uniqueWords, spam_prob, ham_prob, spam_condProb, ham_condProb, 0.5)


#     Output variables (for result.txt)
    fileNumbers = len(test_fileNames)
    fileNames = test_fileNames
    actualLabels = actual_labels
    predictedLabels = predicted_labels
    hamScores = ham_scores
    spamScores = spam_scores
    decisionLabels = decision_labels


#     Stores the content of result.txt
    result_output = sd.result_output_generator(
        fileNumbers, fileNames, predictedLabels, hamScores, spamScores, actualLabels, decisionLabels)


#     Builds result.txt file
    sd.resultFileBuilder(result_output)

    ################################################
    "*************** ANALYSIS PHASE ***************"
    ################################################

    "*** Spam Analysis ***"

#     Precision (spam class)
    spam_precision = sd.get_spamPrecision(
        fileNumbers, actualLabels, predictedLabels)


#     Recall (spam class)
    spam_recall = sd.get_spamRecall(fileNumbers, actualLabels, predictedLabels)


#     Accuracy (spam class)
    spam_accuracy = sd.get_spamAccuracy(
        fileNumbers, actualLabels, predictedLabels)


#     F1-measure (spam class)
    spam_fmeasure = sd.get_spamFmeasure(spam_precision, spam_recall)

    "*** Ham Analysis ***"

#     Precision (spam class)
    ham_precision = sd.get_hamPrecision(
        fileNumbers, actualLabels, predictedLabels)


#     Recall (spam class)
    ham_recall = sd.get_hamRecall(fileNumbers, actualLabels, predictedLabels)


#     Accuracy (spam class)
    ham_accuracy = sd.get_hamAccuracy(
        fileNumbers, actualLabels, predictedLabels)


#     F1-measure (spam class)
    ham_fmeasure = sd.get_hamFmeasure(ham_precision, ham_recall)

    ################################################
    "************* EVALUATION RESULTS *************"
    ################################################


#     Stores the output of the Evaluation Results
    evaluation_result_output = sd.evaluation_result(
        spam_accuracy, spam_precision, spam_recall, spam_fmeasure, ham_accuracy, ham_precision, ham_recall, ham_fmeasure)


#     Stores the parameters of the Confusion Matrix (spam class): (spam_TP, spam_TN, spam_FP, spam_FN)
    spam_tp, spam_tn, spam_fp, spam_fn = sd.spamConfusionParams(
        fileNumbers, actualLabels, predictedLabels)


#     Stores the output of the Confusion Matrix (spam class)
    spam_confusionMatrix_output = sd.spam_confusionMatrix(
        spam_tp, spam_tn, spam_fp, spam_fn)


#     Stores the parameters of the Confusion Matrix (spam class): (ham_TP, ham_TN, ham_FP, ham_FN)
    ham_tp, ham_tn, ham_fp, ham_fn = sd.hamConfusionParams(
        fileNumbers, actualLabels, predictedLabels)


#     Stores the output of the Confusion Matrix (ham class)
    ham_confusionMatrix_output = sd.ham_confusionMatrix(
        ham_tp, ham_tn, ham_fp, ham_fn)


#     Stores the content of evaluation.txt
    evaluation_output = sd.evaluation_output_generator(
        evaluation_result_output, spam_confusionMatrix_output, ham_confusionMatrix_output)


#     Builds evaluation.txt file
    sd.evaluationFileBuilder(evaluation_output)


# Calls the main function to create result.txt as well as evaluate.txt
mainFunction()
