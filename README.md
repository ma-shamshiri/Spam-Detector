<h1>Artificial Intelligence (Winter 2020)</h1>

<h2>Project Assignment 2: Spam Detector</h2>



<h2 id="overview"><a class="anchor" name="overview" href="#overview"><span class="octicon octicon-link"></span></a>Overview</h2>
<p>I have implemented a spam detector program in Python which classifies given emails as spam or ham based on applying Naive Bayes' theorem.</p>

<p align="center"> 
<img src="gif/spam detector.gif" alt="Animated gif pacman game" height="382px">
</p>

<h2>Project Files Description</h2>

<p>This Project includes 3 executable files, 3 text files as well as 2 directories as follows:</p>
<h4>Executable Files:</h4>
<ul>
  <li><b>spam_detector.py</b> - Includes all functions required for classification operations.</li>
  <li><b>train.py</b> - Uses the functions defined in the spam_detector.py file and generates the model.txt file after execution.</li>
  <li><b>test.py</b> - Uses the functions defined in the spam_detector.py file and, after execution, generates the result.txt as well as evaluation.txt files.</li>
</ul>

<h4>Output Files:</h4>
<ul>
  <li><b>model.txt</b> - Contains information about the vocabularies of the train set, such as the frequency and conditional probability of each word in Spam and Ham classes.</li>
  <li><b>result.txt</b> - Contains information about the classified emails of the test set.</li>
  <li><b>evaluation.txt</b> - Contains evaluation results table as well as Confusion Matrix of Spam and Ham classes.</li>
</ul>

<h4>Source Directories:</h4>
<ul>
  <li><b>train directory</b> - Includes all emails for the training phase of the program.</li>
  <li><b>test directory</b> - Includes all emails for the testing phase of the program.</li>
</ul>

<p>In machine learning, naive Bayes classifiers are a family of simple "probabilistic classifiers" based on applying Bayes' theorem with strong (naive) independence assumptions between the features.
Abstractly, naive Bayes is a conditional probability model: given a problem instance to be classified, represented by a vector
<a target="_blank" rel="noopener noreferrer" href="https://github.com/wruochao19/Hello-world/raw/master/1.png"><img src="https://github.com/wruochao19/Hello-world/raw/master/1.png" alt="Aaron Swartz" style="max-width:100%;"></a></p>

<h2 id="execution-instruction"><a class="anchor" name="execution-instruction" href="#execution-instruction"><span class="octicon octicon-link"></span></a>Execution Instruction</h2>
<p>The order of execution of program files is as follows:</p>
<p><b>1) spam_detector.py</b></p>
<p>First, the spam_detector.py file must be executed to define all the functions and variables required for classification operations.</p>
<p><b>2) train.py</b></p>
<p>Then, the train.py file must be executed, which leads to the production of the model.txt file. 
At the beginning of this file, the spam_detector has been imported so that the functions defined in it can be used.</p>
<p><b>3) test.py</b></p>
<p>Finally, the test.py file must be executed to create the result.txt and evaluation.txt files.
Just like the train.py file, at the beginning of this file, the spam_detector has been imported so that the functions defined in it can be used.</p>

<h2>Credits</h2>
<ul>
  <li>This is the homework project for the course COMP 6721 - Artificial Intelligence (Winter 2020), at Concordia University</li>
  <li>Author: Mohammad Amin Shamshiri</li>
</ul>
