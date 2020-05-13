################################################
"*************** TRAINING PHASE ***************"
################################################



# Importing the spam_detector file to use the required functions
import spam_detector as sd



"************** MAIN FUNCTION **************"
"*** Defines main function for train.py ***"

def mainFunction():
    
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
    spam_bagOfWords, ham_bagOfWords = sd.bagOfWords_genarator(all_uniqueWords, spam_trainWords, ham_trainWords)
    

    
#     smooothed Bag of Words: (smoothed_spamBOW, smoothed_hamBOW)
    smoothed_spamBOW, smoothed_hamBOW = sd.smoothed_bagOfWords(all_uniqueWords, spam_bagOfWords, ham_bagOfWords, 0.5)
    

    
#     probability of spam class: P(spam)
    spam_prob = sd.spam_probability(nb_of_allEmails, nb_of_spamEmails)

    
    
#     probability of ham class: P(ham)
    ham_prob = sd.ham_probability(nb_of_allEmails, nb_of_hamEmails)
    

    
#     P(Wi|spam) for each word
    spam_condProb = sd.spam_condProbability(all_uniqueWords, spam_bagOfWords, smoothed_spamBOW, 0.5)
    

    
#     P(Wi|ham) for each word
    ham_condProb = sd.ham_condProbability(all_uniqueWords, ham_bagOfWords, smoothed_hamBOW, 0.5)
    

    
#     Output variables (for model.txt)
    word_numbers = len(all_uniqueWords)
    words = all_uniqueWords
    ham_wf = ham_bagOfWords
    ham_cp = ham_condProb
    spam_wf = spam_bagOfWords
    spam_cp = spam_condProb



#     Stores the content of model.txt
    model_output = sd.model_output_generator(word_numbers, words, ham_wf, ham_cp, spam_wf, spam_cp)
    

    
#     Builds model.txt file
    sd.modelFileBuilder(model_output)





"*** The starting point of the program ***"
# Calls the main function to create model.txt

mainFunction()