<h1>Artificial Intelligence (Winter 2020)</h1>

<h2>Project Assignment 2: Spam Detector</h2>



<h2 id="overview"><a class="anchor" name="overview" href="#overview"><span class="octicon octicon-link"></span></a>Overview</h2>
<p>I have implemented a spam detector program in Python which classifies given emails as spam or ham based on applying Naive Bayes' theorem.</p>

<p align="center"> 
<img src="gif/spam detector.gif" alt="Animated gif pacman game" height="382px">
</p>

<h2>Project Files Description</h2>

<p>This Project includes 3 executable files, 3 text files as well as 2 directories as follows:</p>
<h3>Executable Files:</h3>
<ul>
  <li><b>spam_detector.py</b> - Includes all functions required for classification operations.</li>
  <li><b>train.py</b> - Uses the functions defined in the spam_detector.py file and generates the model.txt file after execution.</li>
  <li><b>test.py</b> - Uses the functions defined in the spam_detector.py file and, after execution, generates the result.txt as well as evaluation.txt files.</li>
</ul>

<h3>Output Files:</h3>
<ul>
  <li><b>model.txt</b> - Contains information about the vocabularies of the train set, such as the frequency and conditional probability of each word in Spam and Ham classes.</li>
  <li><b>result.txt</b> - Contains information about the classified emails of the test set.</li>
  <li><b>evaluation.txt</b> - Contains evaluation results table as well as Confusion Matrix of Spam and Ham classes.</li>
</ul>

<h3>Source Directories:</h3>
<ul>
  <li><b>train directory</b> - Includes all emails for the training phase of the program.</li>
  <li><b>test directory</b> - Includes all emails for the testing phase of the program.</li>
</ul>

<h3 id="execution-instruction"><a class="anchor" name="execution-instruction" href="#execution-instruction"><span class="octicon octicon-link"></span></a>Execution Instruction</h3>
<p>The order of execution of program files is as follows:</p>
<p>1) spam_detector.py</p>
<p>First, the spam_detector.py file must be executed to define all the functions and variables required for classification operations.</p>
<p>2) train.py</p>
<p>Then, the train.py file must be executed, which leads to the production of the model.txt file. 
At the beginning of this file, the spam_detector has been imported so that the functions defined in it can be used.</p>
<p>3) test.py</p>
<p>Finally, the test.py file must be executed to create the result.txt and evaluation.txt files.
Just like the train.py file, at the beginning of this file, the spam_detector has been imported so that the functions defined in it can be used.</p>

<h2>Credits</h2>
<ul>
  <li>This is the homework project for the course COMP 6721 - Artificial Intelligence (Winter 2020), at Concordia University</li>
  <li>Author: Mohammad Amin Shamshiri</li>
</ul>
