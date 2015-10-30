### SEA-DAT1 course repository

Materials for [General Assembly's Data Science course](https://generalassemb.ly/education/data-science/seattle/) in Seattle, WA
(10/27/15 - 1/21/16)

**Instructor:** [Jim Byers](https://www.linkedin.com/profile/view?id=ADEAAAEai9UBI1CGmAPFMYpURJeL9zvxWX6xBqI)

**Classes:** 6:30pm - 9:30pm

Tuesday | Thursday
--- | ---
**2015** | 
| 10/27: L01 Introduction to Data Science | 10/29: L02 Command Line and Version Control
11/3: L03 Data Reading and Cleaning | 11/5: L04 Exploratory Data Analysis
11/10: L05 Visualization<br>**Project Discussion Deadline** | 11/12: L06 Machine Learning<br>**Project Question and Dataset Due**
11/17: L07 Getting Data | 11/19: L08 K-Nearest Neighbors
11/24: L09 Basic Model Evaluation | 11/26 (Holiday/ No class) |
12/1: L10 Linear Regression | 12/3:  L11 **First Project Presentation** 
12/8: L12 Logistic Regression | 12/10: L13 Advanced Model Evaluation
12/15: L14 Naive Bayes and Text Data | 12/17: L15  Language Processing
12/22: L16 TBD, **Draft Paper Due** | 12/24: (Holiday/ No class)
12/29: (Holiday/ No class) | 12/31: (Holiday/ No class)
**2016** |
1/5: L17 Decision Trees | 1/7: L18 Ensembling
1/12: L19 Regularization and<br>Clustering, **Peer Review Due** | 1/22: L20 Course Review and Bonus Topics
1/19: L21 Bonus Topics and<br>**Final Project Presentation** | 1/21: L22 **Final Project Presentation**
&nbsp;
## Submission Forms
### [      Exit ticket form] (https://docs.google.com/a/generalassemb.ly/forms/d/10L0tgB2X70bIHAzb1d0_4guWmCEqxavhQAHM1t1I4-Y/viewform)
### [      Homework and project submissions form] (https://docs.google.com/forms/d/1S82LIibhiG2olZQb2C7iboqN5rb8wB6mQLFBg992eh4/viewform?usp=send_form)
 &nbsp;
-----

### Before the Course Begins
* Install [Git](http://git-scm.com/downloads).
* Create an account on the [GitHub](https://github.com/) website.
    * It is not necessary to download "GitHub for Windows" or "GitHub for Mac"
* Install the [Anaconda distribution](http://continuum.io/downloads) of Python 2.7x.
    * If you choose not to use Anaconda, here is a list of the [Python packages](other/python_packages.md) you will need to install during the course.
* We would like to check the setup of your laptop before the course begins:
    * You can have your laptop checked prior to class on 10/27 from 5:00-5:45PM.
    * Alternatively, you can walk through the [setup checklist](other/setup_checklist.md) yourself.
* Once you receive an email invitation from Slack, join our "SEA-DAT1" Slack group and add your photo.
* Practice Python using the resources below.

### Additional Python Resources
* [Codecademy's Python course](http://www.codecademy.com/en/tracks/python): Good beginner material, including tons of in-browser exercises.
* [Google's Python Class](https://developers.google.com/edu/python/): Slightly more advanced, including hours of useful lecture videos and downloadable exercises (with solutions).
* [Introduction to Python](http://introtopython.org/): A series of IPython notebooks that do a great job explaining core Python concepts and data structures.
* [Python for Informatics](http://www.pythonlearn.com/book.php): A very beginner-oriented book, with associated [slides](https://drive.google.com/folderview?id=0B7X1ycQalUnyal9yeUx3VW81VDg&usp=sharing) and [videos](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj4JXIwMwN1_ss1Tk8wZShEJ).
* [A Crash Course in Python for Scientists](http://nbviewer.ipython.org/gist/rpmuller/5920182): Read through the Overview section for a very quick introduction to Python.
* [Python Quick Reference Guide](other/python_reference): Kevin Markham's beginner-oriented guide that demonstrates Python concepts through short, well-commented examples.
* [Beginner](code/00_python_beginner_workshop.py) and [intermediate](code/00_python_intermediate_workshop.py) workshop code: Useful for review and reference.
* [Python Tutor](http://pythontutor.com/): Allows you to visualize the execution of Python code.




<!--
### [Comparison of machine learning models](other/model_comparison.md)
-->

<!--
### [Comparison of model evaluation procedures and metrics](other/model_evaluation_comparison.md)
-->

-----

### Class 1: Introduction to Data Science

**By the end of this lesson you will be able to:**

* Describe what data science is and the types of problems it can solve
* Name at least three types of data
* Describe at least two of the elements of the Final project requirements

**Topics/Highlights**
* Welcome from General Assembly staff
* Course overview ([slides](slides/01_course_overview.pdf))
* Data Science Intro ([slides](slides/01_data_science_intro.pdf))
* Types of data ([slides](slides/01_types_of_data.pdf)) and [public data sources](project/public_data.md)
* Discuss the course project: [requirements](project/README.md) and [example projects](/project/project_examples/README.md)

**Homework:**
* Complete GA's friendly [command line tutorial](http://generalassembly.github.io/prework/command-line/#/) using Terminal (Linux/Mac) or Git Bash (Windows).
* Read through this [command line reference](code/02_command_line_basics.md), and complete the pre-class exercise at the bottom. (There's nothing you need to submit once you're done.)
* Watch videos 1 through 8 (21 minutes) of [Introduction to Git and GitHub](https://www.youtube.com/playlist?list=PL5-da3qGB5IBLMp7LtN8Nc3Efd4hJq0kD), or read sections 1.1 through 2.2 of [Pro Git](http://git-scm.com/book/en/v2).
* If your laptop has any setup issues, please work with us to resolve them by Thursday. If your laptop has not yet been checked, you should come early on Thursday, or just walk through the [setup checklist](other/setup_checklist.md) yourself (and let us know you have done so).

**Resources:**
* For a useful look at the different types of data scientists, read [Analyzing the Analyzers](http://cdn.oreillystatic.com/oreilly/radarreport/0636920029014/Analyzing_the_Analyzers.pdf) (32 pages).
* For some thoughts on what it's like to be a data scientist, read these short posts from [Win-Vector](http://www.win-vector.com/blog/2012/09/on-being-a-data-scientist/) and [Datascope Analytics](http://datascopeanalytics.com/what-we-think/2014/07/31/six-qualities-of-a-great-data-scientist).
* Quora has a [data science topic FAQ](https://www.quora.com/Data-Science) with lots of interesting Q&A.

-----

### Class 2: Command Line and Version Control

**By the end of this lesson you will be able to:**
* clone a Githib repository to your laptop
* synch your local files with your GitHub repository using git add, commit, push and pull
* use more advanced command line commands such as Grep and |

**Topics/Highlights**
* Slack tour
* Review the command line pre-class exercise ([code](code/02_command_line_basics.md))
* Git and GitHub ([slides](slides/02_git_github.pdf))
* Intermediate command line

**Homework:**
* Complete the [command line homework assignment](homework/02_command_line_chipotle.md) with the Chipotle data.
* Review the code from a [beginner](code/00_python_beginner_workshop.py) and an [intermediate](code/00_python_intermediate_workshop.py) Python workshop. If you don't feel comfortable with any of the content (excluding the "requests" and "APIs" sections), you should spend some time this weekend practicing Python:
    * [Introduction to Python](http://introtopython.org/) does a great job explaining Python essentials and includes tons of example code.
    * If you like learning from a book, [Python for Informatics](http://www.pythonlearn.com/html-270/) has useful chapters on strings, lists, and dictionaries.
    * If you prefer interactive exercises, try these lessons from [Codecademy](http://www.codecademy.com/en/tracks/python): "Python Lists and Dictionaries" and "A Day at the Supermarket".
    * If you have more time, try missions 2 and 3 from [DataQuest's Learning Python](https://www.dataquest.io/course/learning-python) course.
    * If you've already mastered these topics and want more of a challenge, try solving [Python Challenge](http://www.pythonchallenge.com/) number 1 (decoding a message) and send me your code in Slack.
* To give you a framework for thinking about your project, watch [What is machine learning, and how does it work?](https://www.youtube.com/watch?v=elojMnjn4kk) (10 minutes). (This is the [IPython notebook](other/scikit-learn_videos/01_machine_learning_intro.ipynb) shown in the video.) Alternatively, read [A Visual Introduction to Machine Learning](http://www.r2d3.us/visual-intro-to-machine-learning-part-1/), which focuses on a specific machine learning model called decision trees.
* **Optional:** Browse through some more [example student projects](/project/project_examples/README.md), which may help to inspire your own project!

**Git and Markdown Resources:**
* [Pro Git](http://git-scm.com/book/en/v2) is an excellent book for learning Git. Read the first two chapters to gain a deeper understanding of version control and basic commands.
* If you want to practice a lot of Git (and learn many more commands), [Git Immersion](http://gitimmersion.com/) looks promising.
* If you want to understand how to contribute on GitHub, you first have to understand [forks and pull requests](http://www.dataschool.io/simple-guide-to-forks-in-github-and-git/).
* [GitRef](http://gitref.org/) is my favorite reference guide for Git commands, and [Git quick reference for beginners](http://www.dataschool.io/git-quick-reference-for-beginners/) is a shorter guide with commands grouped by workflow.
* [Cracking the Code to GitHub's Growth](https://growthhackers.com/growth-studies/github) explains why GitHub is so popular among developers.
* [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) provides a thorough set of Markdown examples with concise explanations. GitHub's [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) is a simpler and more attractive guide, but is less comprehensive.

**Command Line Resources:**
* If you want to go much deeper into the command line, [Data Science at the Command Line](http://shop.oreilly.com/product/0636920032823.do) is a great book. The [companion website](http://datascienceatthecommandline.com/) provides installation instructions for a "data science toolbox" (a virtual machine with many more command line tools), as well as a long reference guide to popular command line tools.
* If you want to do more at the command line with CSV files, try out [csvkit](http://csvkit.readthedocs.org/), which can be installed via `pip`.

-----

### Class 3: Data Reading and Cleaning
* Git and GitHub assorted tips ([slides](slides/02_git_github.pdf))
* Review command line homework ([solution](homework/02_command_line_chipotle.md))
* Python:
    * Spyder interface
    * Looping exercise
    * Lesson on file reading with airline safety data ([code](code/03_file_reading.py), [data](data/airlines.csv), [article](http://fivethirtyeight.com/features/should-travelers-avoid-flying-airlines-that-have-had-crashes-in-the-past/))
    * Data cleaning exercise
    * Walkthrough of Python homework with Chipotle data ([code](homework/03_python_homework_chipotle.py), [data](data/chipotle.tsv), [article](http://www.nytimes.com/interactive/2015/02/17/upshot/what-do-people-actually-order-at-chipotle.html))

**Homework:**
* Complete the [Python homework assignment](homework/03_python_homework_chipotle.py) with the Chipotle data, add a commented Python script to your GitHub repo, and submit a link using the homework submission form. You have until Tuesday (9/1) to complete this assignment. (**Note:** Pandas, which is covered in class 4, should not be used for this assignment.)

**Resources:**
* [Want to understand Python's comprehensions? Think in Excel or SQL](http://blog.lerner.co.il/want-to-understand-pythons-comprehensions-think-like-an-accountant/) may be helpful if you are still confused by list comprehensions.
* [My code isn't working](http://www.tecoed.co.uk/uploads/1/4/2/4/14249012/624506_orig.png) is a great flowchart explaining how to debug Python errors.
* [PEP 8](https://www.python.org/dev/peps/pep-0008/) is Python's "classic" style guide, and is worth a read if you want to write readable code that is consistent with the rest of the Python community.
* If you want to understand Python at a deeper level, Ned Batchelder's [Loop Like A Native](http://nedbatchelder.com/text/iter.html) and [Python Names and Values](http://nedbatchelder.com/text/names1.html) are excellent presentations.

-----

### Class 4: Exploratory Data Analysis
* Pandas ([code](code/04_pandas.py)):
    * MovieLens 100k movie ratings ([data](data/u.user), [data dictionary](http://files.grouplens.org/datasets/movielens/ml-100k-README.txt), [website](http://grouplens.org/datasets/movielens/))
    * Alcohol consumption by country ([data](data/drinks.csv), [article](http://fivethirtyeight.com/datalab/dear-mona-followup-where-do-people-drink-the-most-beer-wine-and-spirits/))
    * Reports of UFO sightings ([data](data/ufo.csv), [website](http://www.nuforc.org/webreports.html))
* Project question exercise

**Homework:**
* The deadline for discussing your project ideas with an instructor is Tuesday (9/1), and your project question write-up is due Thursday (9/3).
* Read [How Software in Half of NYC Cabs Generates $5.2 Million a Year in Extra Tips](http://iquantny.tumblr.com/post/107245431809/how-software-in-half-of-nyc-cabs-generates-5-2) for an excellent example of exploratory data analysis.
* Read [Anscombe's Quartet, and Why Summary Statistics Don't Tell the Whole Story](http://data.heapanalytics.com/anscombes-quartet-and-why-summary-statistics-dont-tell-the-whole-story/) for a classic example of why visualization is useful.

**Resources:**
* Browsing or searching the Pandas [API Reference](http://pandas.pydata.org/pandas-docs/stable/api.html) is an excellent way to locate a function even if you don't know its exact name.
* [What I do when I get a new data set as told through tweets](http://simplystatistics.org/2014/06/13/what-i-do-when-i-get-a-new-data-set-as-told-through-tweets/) is a fun (yet enlightening) look at the process of exploratory data analysis.

-----

