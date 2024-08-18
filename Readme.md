

# DATA ANALYTICS USING PYTHON 

## OVERVIEW

Welcome to my project DATA ANALYTICS USING PYTHON , In this project we used Data of Job postings to get insights into the Job Market for the Data sector. This project was created out of a desire to navigate and understand the job market more effectively. It delves into the top-paying and in-demand skills to help find optimal job opportunities for data analysts.

Thanks Luke Barrouse ([Luke Barousse \- YouTube](https://www.youtube.com/@LukeBarousse)) this wonderful Data analytics course and also including a project and explaining this hands on. 

# Tools and Libraries used 

Python \- All of the project is coded in Python and using its Libraries.

Pandas , Numpy- Python tool for managing and accessing dataset  
Matplotlib , Seaborn \- for making visualisation from pandas to get the insights  
Visual Studio Code \-  My go-to for executing my Python scripts  
Jupyter Notebooks \-  The tool I used to run my Python scripts which let me easily include my notes and analysis  
Git & GitHub \-  Essential for version control and sharing my Python code and analysis, ensuring collaboration and project tracking.

# Below are the questions I want to answer in my project:

1\. What are the skills most in demand for the top 3 most popular data roles?  
2\. How are in-demand skills trending for Data Analysts?  
3\. How well do jobs and skills pay for Data Analysts?  
4\. What are the optimal skills for data analysts to learn? (High Demand AND High Paying) 

## 

# Data Importing 

Imported from \[Luke Barousse's Python Course\]([https://lukebarousse.com/python](https://lukebarousse.com/python))\]  
Python command   
   
import pandas as pd  
from datasets import load\_dataset

dataset \= load\_dataset("lukebarousse/data\_jobs")

# Data Preparation and Cleanup 

After Importing Data is cleaned and Prepared , making it ready to analyse and get insights 

### Data Cleaning code file \- 

# Analysis

Each Jupyter notebook for this project aimed at investigating specific aspects of the data job market. Here’s how I approached each question \- 

## 0\. What are the best jobs according to salary and demand ?

To find the best jobs , we grouped data by Jobs and found their median salary and demand in job postings.

[File for Analysis of Q1(Python Code)](https://github.com/anmol112/Python\_data\_project/blob/main/best\_job.ipynb)

### Visualisation \- ![Python\_data\_project/plots/new plots/Best jobs in software and data.png at main · anmol112/Python\_data\_project (github.com)](https://github.com/anmol112/Python\_data\_project/blob/main/plots/new%20plots/Best%20jobs%20in%20software%20and%20data.png)

### Insights \- 

Highest paying jobs were Senior Data Scientist , Senior Data Engineer and Most demanded jobs were Data Analts and Data Engineer   
Most demanded jobs were Data Analyst , Data Engineer and Data Scientist .  
But The best Jobs were Data Scientist , Data Engineer with their high salary and Great demand. 

## 1\. What are the most demanded skills for the top 3 most popular data roles?

To find the most demanded skills for the top 3 most popular data roles. I filtered out those positions by which ones were the most popular, and got the top 5 skills for these top 3 roles. 

### [File for Analysis of Q1(Python Code)](https://github.com/anmol112/Python\_data\_project/blob/main/data\_3\_jobs\_skills\_DA\_DS\_DE.ipynb) \- 

### Visualisation \- ![Python\_data\_project/plots/new plots/A\_DS\_DE\_skills\_occurance\_likelyhood.png at main · anmol112/Python\_data\_project (github.com)](https://github.com/anmol112/Python\_data\_project/blob/main/plots/new%20plots/A\_DS\_DE\_skills\_occurance\_likelyhood.png)

### Insights \- 

SQL and Python turned out to be the most demanded skills , also from Q0 we know that Data Scientist and Data Engineer offer good salary so that means these skills also are high paying  
Data Scientist and Data Engineer are more into advanced Data Technologies and Programing but Data Analyst require basic data skills and Visualisation tools.  
It looks Data Analyst  work is like collaboration between Non Data and Data Team and Data Engineer and Data Scientist are more into Advanced Data Data Skills.  
   

## 2\. How are in-demand skills trending for Data Analysts?

To find how skills are trending in 2023 for Data Analysts, I filtered data analyst positions and grouped the skills by the month of the job postings. This got me the top 5 skills of data analysts by month, showing how popular skills were throughout 2023 .

### [File for Analysis of Q2(Python Code)](https://github.com/anmol112/Python\_data\_project/blob/main/DA\_skills\_trending.ipynb) 

### 

### Visualisation \- ![Python\_data\_project/plots/new plots/skills\_trending\_da.png at main · anmol112/Python\_data\_project (github.com)](https://github.com/anmol112/Python\_data\_project/blob/main/plots/new%20plots/skills\_trending\_da.png)

### Insights \-

SQL remains the most consistently demanded skill throughout the year, although it shows a gradual decrease in demand.  
Excel experienced a significant increase in demand starting around September, surpassing both Python and Tableau by the end of the year.  
Both Python and Tableau show relatively stable demand throughout the year with some fluctuations but remain essential skills for data analysts. Power BI, while less demanded compared to the others, shows a slight upward trend towards the year's end.

##  3\. How well do jobs pay for Data Analyst , Data Scientist , Data Engineer and their senior roles?

To identify the highest-paying roles and skills, I only got jobs in the United States and looked at their median salary. But first I looked at the salary distributions of common data jobs like Data Scientist, Data Engineer, and Data Analyst, to get an idea of which jobs are paid the most. 

[File for Analysis of Q3(Python Code)](https://github.com/anmol112/Python\_data\_project/blob/main/Data\_best\_jobs.ipynb) 

### Visualisation \- ![Python\_data\_project/plots/new plots/Salary Distribution of data jobs.png at main · anmol112/Python\_data\_project (github.com)](https://github.com/anmol112/Python\_data\_project/blob/main/plots/new%20plots/Salary%20Distribution%20of%20data%20jobs.png)

### Insights \-

There's a significant variation in salary ranges across different job titles. Senior Data Scientist positions tend to have the highest salary potential, with up to $600K, indicating the high value placed on advanced data skills and experience in the industry.

Senior Data Engineer and Senior Data Scientist roles show a considerable number of outliers on the higher end of the salary spectrum, suggesting that exceptional skills or circumstances can lead to high pay in these roles. In contrast, Data Analyst roles demonstrate more consistency in salary, with fewer outliers.

The median salaries increase with the seniority and specialisation of the roles. Senior roles (Senior Data Scientist, Senior Data Engineer) not only have higher median salaries but also larger differences in typical salaries, reflecting greater variance in compensation as responsibilities increase.

##  4.Highest Paid & Most Demanded Skills for Data Analysts 

Next, I narrowed my analysis and focused only on data analyst roles. I looked at the highest-paid skills and the most in-demand skills. I used two bar charts to showcase these.

[File for Analysis of Q4(Python Code)](https://github.com/anmol112/Python\_data\_project/blob/main/best\_skills\_DA.ipynb) 

### Visualisation \- ![Python\_data\_project/plots/new plots/Data Analyst best skills.png at main · anmol112/Python\_data\_project (github.com)](https://github.com/anmol112/Python\_data\_project/blob/main/plots/new%20plots/Data%20Analyst%20best%20skills.png)

### 

### Insights:

The top graph shows specialised technical skills like  ‘svn ’ , \`dplyr\`, \`Bitbucket\`, and \`Gitlab\` are associated with higher salaries, some reaching up to $200K, suggesting that advanced technical proficiency can increase earning potential.

The bottom graph highlights that foundational skills like \`Excel\`, \`Python\`, and \`SQL\` are the most in-demand, even though they may not offer the highest salaries. This demonstrates the importance of these core skills for employability in data analysis roles.

There's a clear distinction between the skills that are highest paid and those that are most in-demand. Data analysts aiming to maximise their career potential should consider developing a diverse skill set that includes both high-paying specialised skills and widely demanded foundational skills.

## 5\. What are the most optimal skills to learn for Data Analysts?

To identify the most optimal skills to learn ( the ones that are the highest paid and highest in demand) I calculated the percent of skill demand and the median salary of these skills. To easily identify which are the most optimal skills to learn. 

[File for Analysis of Q3(Python Code)](https://github.com/anmol112/Python\_data\_project/blob/main/Optimal\_skills.ipynb) 

### Visualisation \- ![Python\_data\_project/plots/new plots/optimal Skills.png at main · anmol112/Python\_data\_project (github.com)](https://github.com/anmol112/Python\_data\_project/blob/main/plots/new%20plots/optimal%20Skills.png)

### Insights \- 

Kafka , scala , and spark have the highest salary  due to the specialised and high-demand nature of their skills in big data and real-time processing, which are critical for large-scale, high-impact systems.

Python and SQL are most demanded and form the basis of Data Technologies.

## What I Learned 

I learned python advanced  Frameworks such as \- Pandas , Matplotlib ,seaborn, these frameworks are very efficient in handling the data , manipulating data and advanced visualisations.

#### Pandas \-

* Data Cleaning and Data Manipulation   
* Useful Pandas command such (dropna , drop\_duplicates , groupby , Pivot\_table , explode , merge  )

#### Matplotlib , Seaborn \- 

* Advanced Data Visualisations  
* Multiple types of plots (barchart , scatterplot , line , advanced statistic plots )

 Also learned basics about Git and Github for uploading code on the internet ,getting suggestions and for coding with teams.  
While learning about these libraries i also strengthened and deepened my knowledge of python.

## Insights

This project provided several general insights into the data job market for analysts:

Skill Demand and Salary Correlation: There is a clear correlation between the demand for specific skills and the salaries these skills command. Advanced and specialised skills like Python and Oracle often lead to higher salaries.  
Market Trends: There are changing trends in skill demand, highlighting the dynamic nature of the data job market. Keeping up with these trends is essential for career growth in data analytics.  
Economic Value of Skills : Understanding which skills are both in-demand and well-compensated can guide data analysts in prioritising learning to maximise their economic returns.

## Challenges I Faced 

* Faced challenges while getting used to the syntax.  
* Very minor details like the difference between series and dataframe causes a lot of errors.  
* Getting working at it because it took a lot of time 

## Conclusion

Learned a lot about Python \-  pandas , matplotlib , seaborn.  
As compared to SQL I found SQL easier than pandas , Matplotlib for general manipulations , Cleaning and plotting but I felt like Python is better for its statistical and advanced operations. I also felt like python is more flexible than SQL.

