import pandas as pd
dict = {'Nourah': 1,
		'leen': 2,
		'Mofadlh': 3}
ser = pd.Series(dict)
print(ser)

import pandas as pd
dict = {11: 'Nourah',
		12: 'leen',
		13: 'Mofadlh'}
ser = pd.Series(dict)
print(ser)

import pandas as pd
dict = {11: 'Nourah',
		12: 'leen',
		13: 'Mofadlh'}
ser = pd.Series(dict)
print(ser)
print(ser[0:2])

import pandas as pd
data = {'ID': [111111,222222,333333],
'Name': ['mofadlh','nourah','leen'],}
Students = pd.DataFrame(data,columns=['ID','Name',])
print(Students)

import pandas as pd
dict = {11: 'Nourah',
		12: 'leen',
		13: 'Mofadlh'}
ser = pd.Series(dict)
print(ser)
ser = pd.Series({50: 'mofadlh', 60: 'leen'})
ser.drop(50)
ser.drop_duplicates()
print(ser)



import pandas as pd
read = pd.read_csv('https://raw.githubusercontent.com/Data-Science-July31/Lectures/main/Day%237/educ_figdp_1_Data.csv')
print(read)


Q\7
First of all, .loc is a label based method whereas .iloc is an integer-based method. This means that iloc will consider the names or
 labels of the index when we are slicing the dataframe.
For example, if “case” would be in the index of a dataframe (e.g., df), df.loc['case'] will result in that the third row is 
being selected. Note, in the loc and iloc examples below we will work with the first column, in the dataset, as index
 (see first code chunk).
On the other hand, Pandas .iloc takes slices based on index’s position. Unlike .loc, .iloc behaves like regular Python slicing. That is,
 we just indicate the positional index number, and we get the slice we want.
For example, df.iloc[2] will give us the third row of the dataframe. This is because, just like in Python, 
.iloc is zero positional based. That is it starts at 0. We will learn how we use loc and iloc, in the following sections of this post.