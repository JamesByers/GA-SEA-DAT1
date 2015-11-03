'''
CLASS: Pandas for Exploratory Data Analysis

MovieLens 100k movie rating data:
    main page: http://grouplens.org/datasets/movielens/
    data dictionary: http://files.grouplens.org/datasets/movielens/ml-100k-README.txt
    files: u.user, u.user_original (no header row)

WHO alcohol consumption data:
    article: http://fivethirtyeight.com/datalab/dear-mona-followup-where-do-people-drink-the-most-beer-wine-and-spirits/    
    original data: https://github.com/fivethirtyeight/data/tree/master/alcohol-consumption
    file: drinks.csv (with additional 'continent' column)

National UFO Reporting Center data:
    main page: http://www.nuforc.org/webreports.html
    file: ufo.csv
'''

import pandas as pd

'''
Reading Files, Selecting Columns, and Summarizing
'''

# can read a file from local computer or directly from a URL


# read 'u.user' into 'users'


# examine the users data


# select a column


# summarize (describe) the DataFrame


# summarize a Series


# count the number of occurrences of each value


'''
EXERCISE ONE
'''

# read drinks.csv into a DataFrame called 'drinks'

# [your code here]


# print the head and the tail

# [your code here]



# examine the default index, data types, and shape

# [your code here]



# print the 'beer_servings' Series

# [your code here]



# calculate the mean 'beer_servings' for the entire dataset

# [your code here]



# count the number of occurrences of each 'continent' value and see if it looks correct

# [your code here]



# BONUS: display only the number of rows of the 'users' DataFrame

# [your code here]



# BONUS: display the 3 most frequent occupations in 'users'

# [your code here]



# BONUS: create the 'users' DataFrame from the u.user_original file (which lacks a header row)
# Hint: read the pandas.read_table documentation

# [your code here]



'''
Filtering and Sorting
'''

# boolean filtering: only show users with age < 20


# boolean filtering with multiple conditions


# sorting


'''
EXERCISE TWO
'''

# filter 'drinks' to only include European countries

# [your code here]



# filter 'drinks' to only include European countries with wine_servings > 300

# [your code here]



# calculate the mean 'beer_servings' for all of Europe

# [your code here]



# determine which 10 countries have the highest total_litres_of_pure_alcohol

# [your code here]



# BONUS: sort 'users' by 'occupation' and then by 'age' (in a single command)

# [your code here]



# BONUS: filter 'users' to only include doctors and lawyers without using a |
# Hint: read the pandas.Series.isin documentation

# [your code here]



'''
Renaming, Adding, and Removing Columns
'''

# rename one or more columns


# replace all column names


# replace all column names when reading the file


# add a new column as a function of existing columns


# removing columns


'''
Handling Missing Values
'''

# missing values are usually excluded by default


# find missing values in a Series


# use a boolean Series to filter DataFrame rows


# side note: understanding axes


# side note: adding booleans


# find missing values in a DataFrame


# drop missing values


# fill in missing values


# turn off the missing value filter


'''
EXERCISE THREE
'''

# read ufo.csv into a DataFrame called 'ufo'

# [your code here]



# check the shape of the DataFrame

# [your code here]



# calculate the most frequent value for each of the columns (in a single command)

# [your code here]



# what are the four most frequent colors reported?

# [your code here]



# for reports in VA, what's the most frequent city?

# [your code here]



# show only the UFO reports from Arlington, VA

# [your code here]



# count the number of missing values in each column

# [your code here]



# show only the UFO reports in which the City is missing

# [your code here]



# how many rows remain if you drop all rows with any missing values?

# [your code here]



# replace any spaces in the column names with an underscore

# [your code here]



# BONUS: redo the task above, writing generic code to replace spaces with underscores
# In other words, your code should not reference the specific column names

# [your code here]



# BONUS: create a new column called 'Location' that includes both City and State
# For example, the 'Location' for the first row would be 'Ithaca, NY'

# [your code here]



'''
Split-Apply-Combine
Diagram: http://i.imgur.com/yjNkiwL.png
'''

# for each continent, calculate the mean beer servings


# for each continent, count the number of occurrences


# for each continent, describe beer servings


# similar, but outputs a DataFrame and can be customized


# if you don't specify a column to which the aggregation function should be applied,
# it will be applied to all numeric columns


'''
EXERCISE FOUR
'''

# for each occupation in 'users', count the number of occurrences

# [your code here]



# for each occupation, calculate the mean age

# [your code here]



# BONUS: for each occupation, calculate the minimum and maximum ages

# [your code here]



# BONUS: for each combination of occupation and gender, calculate the mean age

# [your code here]



'''
Selecting Multiple Columns and Filtering Rows
'''

# select multiple columns


# use loc to select columns by name


# loc can also filter rows by "name" (the index)


# use iloc to filter rows and select columns by integer position


'''
Other Frequently Used Features
'''

# map existing values to a different set of values


# encode strings as integer values (automatically starts at 0)


# determine unique values in a column


# replace all instances of a value in a column (must match entire value)


# string methods are accessed via 'str'
    # converts to uppercase
    # checks for a substring

# convert a string to the datetime format

	# datetime format exposes convenient attributes
	# also allows you to do datetime "math"
	# boolean filtering with datetime format

# setting and then removing an index


# sort a column by its index


# change the data type of a column


# change the data type of a column when reading in a file


# create dummy variables for 'continent' and exclude first dummy column


# concatenate two DataFrames (axis=0 for rows, axis=1 for columns)


'''
Less Frequently Used Features
'''

# create a DataFrame from a dictionary


# create a DataFrame from a list of lists


# detecting duplicate rows
	# True if a row is identical to a previous row
	# count of duplicates
	# only show duplicates
	# check a single column for duplicates
	# specify columns for finding duplicates

# display a cross-tabulation of two Series


# alternative syntax for boolean filtering (noted as "experimental" in the documentation)
	# users[users.age < 20]
	# users[(users.age < 20) & (users.gender=='M')]
	# users[(users.age < 20) | (users.age > 60)]

# display the memory usage of a DataFrame
	# total usage
	# usage by column

# change a Series to the 'category' data type (reduces memory usage and increases performance)


# temporarily define a new column as a function of existing columns


# limit which rows are read when reading in a file
	# only read first 10 rows
	# skip the first two rows of data

# write a DataFrame out to a CSV
	# index is used as first column
	# ignore index

# save a DataFrame to disk (aka 'pickle') and read it from disk (aka 'unpickle')


# randomly sample a DataFrame
	# will contain 75% of the rows
	# will contain the other 25%

# change the maximum number of rows and columns printed ('None' means unlimited)


# reset options to defaults


# change the options temporarily (settings are restored when you exit the 'with' block)

