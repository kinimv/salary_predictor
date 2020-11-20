# -*- coding: utf-8 -*-
"""

"""

import pandas as pd 

df = pd.read_csv('glassdoor_jobs.csv')

#salary parsing 

df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

df = df[df['Salary Estimate'] != '-1']
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_Kd = salary.apply(lambda x: x.replace('K','').replace('$',''))

min_hr = minus_Kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))

df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary+df.max_salary)/2

#Company name text only
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis = 1)

#state field 
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1] if ',' in x else 0)


df.job_state.value_counts()


#df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)

#age of company 
df['age'] = df.Founded.apply(lambda x: x if x <1 else 2020 - x)


from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
wordcloud2 = WordCloud().generate(' '.join(df['Job Description']))
plt.imshow(wordcloud2)
plt.axis("off")
plt.show()
#parsing of job description (python, etc.)

#javascript
df['javascript_yn'] = df['Job Description'].apply(lambda x: 1 if 'javascript' in x.lower() else 0)
df.javascript_yn.value_counts()

#rest
df['rest_yn'] = df['Job Description'].apply(lambda x: 1 if 'rest' in x.lower() else 0)
df.rest_yn.value_counts()

#spark 
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.spark.value_counts()

#angular 
df['angular'] = df['Job Description'].apply(lambda x: 1 if 'angular' in x.lower() else 0)
df.angular.value_counts()

#react
df['react'] = df['Job Description'].apply(lambda x: 1 if 'react' in x.lower() else 0)
df.react.value_counts()

#scala
df['scala'] = df['Job Description'].apply(lambda x: 1 if 'scala' in x.lower() else 0)
df.scala.value_counts()

#python 
df['python'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df.python.value_counts()

#linux
df['linux'] = df['Job Description'].apply(lambda x: 1 if 'linux' in x.lower() else 0)
df.linux.value_counts()

#.NET
df['dotnet'] = df['Job Description'].apply(lambda x: 1 if '.net' in x.lower() else 0)
df.dotnet.value_counts()

#security clearance
df['tssci'] = df['Job Description'].apply(lambda x: 1 if 'ts/sci' in x.lower() else 0)
df.tssci.value_counts()

#cpp
df['cpp'] = df['Job Description'].apply(lambda x: 1 if 'c/c++' in x.lower() else 0)
df.cpp.value_counts()

df.columns

#df_out = df.drop(['Unnamed: 0'], axis =1)

df.to_csv('salary_data_cleaned.csv',index = False)

