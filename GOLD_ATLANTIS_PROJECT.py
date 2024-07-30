#!/usr/bin/env python
# coding: utf-8

# # Gold Atlantis : Repaying the Credit 

# # Task
# As an analyst, you need to analyze the credit data of Gold Atlantis, figure out various patterns in the data, and make interpretations, The aim of this analysis is to help firm identify those customers who have a lower probability of becoming a defaulter.

# In[4]:


# importing the important libraries  

import matplotlib.pyplot as plt             # to visualize       
from tabulate import tabulate               # to print the table 
import matplotlib as mat                    # to visualize 
import seaborn as sns                       # to visualize
import pandas as pd                         # for data reading   
import numpy as np                          # for numerical computation     


# In[5]:


df = pd.read_csv("DS1_C5_S4_Credit_Data_Hackathon.csv")
df.head()


# In[6]:


df.sample(10)


# # Understanding and cleaning the data

# To perform the analysis, we need to first understand the variables in the dataset. The variables in the given dataset are:
# 
# * SK_ID_CURR: The ID of the customer
# * TARGET: A binary variable indicating whether the customer has defaulted on the loan (1) or not (0)
# * NAME_CONTRACT_TYPE: Type of loan - cash loans or revolving loans
# * GENDER: Gender of the customer
# * Car: Whether the customer owns a car or not
# * House: Whether the customer owns a house or not
# * CNT_CHILDREN: Number of children the customer has
# * AMT_INCOME_TOTAL: Total income of the customer
# * AMT_CREDIT: Total amount of credit taken by the customer
# * AMT_GOODS_PRICE: Price of the goods for which the loan is taken
# * DAYS_EMPLOYED: Number of days the customer has been employed
# * MOBILE: Whether the customer has provided a mobile phone number
# * WORK_PHONE: Whether the customer has provided a work phone number
# * HOME_PHONE: Whether the customer has provided a home phone number
# * MOBILE_REACHABLE: Whether the mobile phone number provided is reachable
# * FLAG_EMAIL: Whether the customer has provided an email address
# * OCCUPATION_TYPE: Type of occupation of the customer
# * CNT_FAM_MEMBERS: Number of family members of the customer
# * APPLICATION_DAY: The day of the week on which the loan application was made
# * TOTAL_DOC_SUBMITTED: Total number of documents submitted by the customer

# In[7]:


df.isnull().sum()            # to check the null values


# In[8]:


a = df.select_dtypes(exclude = 'object')
b = df.select_dtypes(include = 'object')
alist = list(a.columns)
blist = list(b.columns)
print(tabulate({"Categorical":blist,
                "continuous": alist}, headers = ["categorical", "continuous"]))


# In[9]:


def info_of_cat(col):                  
    print(f"Number of missing values in {col} is {df[col].isnull().sum()}")         # mode: returns the mode of the column


# In[10]:


info_of_cat("NAME_TYPE_SUITE")      


# In[11]:


# filing the missing values of categorical columns with mode
df["NAME_TYPE_SUITE"].fillna('Unaccompanied', inplace = True)  


# In[12]:


info_of_cat("OCCUPATION_TYPE")


# In[13]:


# filing the missing values of categorical columns with mode
df["OCCUPATION_TYPE"].fillna('Laborers', inplace = True)


# In[14]:


# filling the continuous columns' missing values with mean
df['AMT_GOODS_PRICE'].fillna(df['AMT_GOODS_PRICE'].mean(), inplace=True)


# In[15]:


# filling the continuous columns' missing values with mean
df['CNT_FAM_MEMBERS'].fillna(df['CNT_FAM_MEMBERS'].mean(), inplace=True)


# In[16]:


df.isnull().sum()         # after imputting, rechecking for the missing values


# There are not any null values in the dataframe now. So, we can start our analysis.

# # Univariate Analysis:

# In[17]:


# distribution of the target variable
sns.countplot(x="TARGET", data=df)
plt.title("Distribution of Defaulters vs Non-Defaulters")

# annotate the counts on the bars
for i in range(len(df["TARGET"].value_counts())):
    count = df["TARGET"].value_counts()[i]
    plt.annotate(str(count), xy=(i, count), ha='center', va='bottom')
    
plt.show()


# # Interpretation : 
# This plot shows the distribution of the target variable (i.e., whether the loan was repaid or not). We can see that the number of non-defaulters is much higher than the number of defaulters, indicating that the majority of applicants have repaid their loans.

# In[18]:


# Distribution of the loan amount
sns.histplot(df["AMT_CREDIT"], kde=True)
plt.title("Distribution of Loan Amount")
plt.show()


# # Interpretation 
# 
# * The distribution of the loan amount is right-skewed, meaning that the majority of the loans are smaller and fewer loans are larger.​
# 
# * There are some extreme loan amounts, which can be seen from the long tail on the right side of the plot. These are likely to be the larger loans, which are few in number but  higher in amount than the majority of the loans.

# In[19]:


# Distribution of the number of children
sns.countplot(x="CNT_CHILDREN", data=df)
plt.title("Distribution of Number of Children")
plt.show()


# # Interpretation :
# This plot shows the distribution of the number of children. We can see that the majority of the applicants do not have any children, with a few applicants having one or two children.

# In[20]:


sns.set_style('whitegrid')
sns.countplot(y='NAME_EDUCATION_TYPE', data=df, order=df['NAME_EDUCATION_TYPE'].value_counts().index)
plt.title('Count of Loan Applications by Education Level')
plt.xlabel('Count')
plt.ylabel('Education Level')
plt.show()


# *** Interpretation : The above graph represents the count of loan applications by education level of the applicants. It shows that most of the loan applications are from applicants who have completed Secondary / secondary special education. The next largest group of loan applications is from applicants with Higher education. This suggests that applicants with higher education are more likely to apply for loans.

# In[21]:


sns.set_style('whitegrid')
sns.countplot(y='NAME_INCOME_TYPE', data=df, order=df['NAME_INCOME_TYPE'].value_counts().index)
plt.title('Count of Loan Applications by Income Level')
plt.xlabel('Count')
plt.ylabel('Income Level')
plt.show()


# # Interpretation 
# * The majority of loan applicants fall under the working class category.
# * There are a significant number of loan applicants in the commercial associate and pensioner categories as well.
# * Businessmen and women are the least likely to apply for loans.

# In[22]:


fig, ax = plt.subplots(figsize = (10,7))
sns.countplot(y=df["OCCUPATION_TYPE"])
plt.show()


# # Interpretation
# * The highest number of loan applicants have an occupation type of Laborers or Sales staff.
# * IT staff and HR staff have the lowest number of loan applications.
# * There are significant numbers of loan applicants across most of the occupation types.

# # Bivariate Analysis:

# In[23]:


# Relationship between number of children and loan amount
sns.boxplot(x="AMT_CREDIT", y="NAME_EDUCATION_TYPE", hue="TARGET", data=df)
plt.title("Amount credit vs Education type")
plt.show()


# # Interpretation 
# * The median loan amount for those with an academic degree is the highest among all education levels.
# * For non-defaulters, the median loan amount increases as the education level increases. 
# * Overall, there are more non-defaulters than defaulters across all education levels.
# * The outliers in the graph suggest that there are some applicants with high amounts of credit and high education levels who defaulted on their loans, while there are also applicants with lower education levels and lower credit amounts who did not default.

# In[24]:


fig, ax = plt.subplots(figsize = (15, 7))
sns.countplot(x="NAME_INCOME_TYPE", hue="TARGET", data=df )
plt.show()


# * Interpretation : Majority of the applicants belong to Working category and it has the highest number of defaulters as well.

# In[25]:


fig, ax = plt.subplots(figsize = (15, 7))
sns.countplot(x="GENDER", hue="TARGET", data=df )
plt.show()


# # Interpretation 
# 
# * The count of females is higher than males for loan applications.
# * For both genders, the count of non-defaulters is higher than the count of defaulters.
# * The count of male non-defaulters is almost the same as female non-defaulters.
# * This indicates that the gender of the applicant does not have a significant impact on loan repayment.

# In[26]:


df.columns


# # Multivariate Analysis:

# In[27]:


fig, ax=plt.subplots(figsize=(20,7))
sns.heatmap(df.corr(), annot=True, cbar=0.5, linewidth=0.5, cmap="coolwarm")
plt.show()


# # Interpretation :
# * The heatmap shows a positive correlation between the amount of credit and the amount of goods price which is quite obvious as the amount of credit will be dependent on the amount of goods to be purchased.

# In[28]:


sns.scatterplot(x="AMT_GOODS_PRICE", y="AMT_CREDIT", hue="NAME_EDUCATION_TYPE", style="TARGET", data=df)
plt.title("Loan Amount vs Amount goods price by Education Level")
plt.show()


# # Interpretation : 
# * Majority of the loan applications are from people with Secondary/secondary special education, followed by those with higher education.
# * Applications from people with incomplete higher education are the lowest.

# In[29]:


sns.scatterplot(x="AMT_GOODS_PRICE", y="AMT_CREDIT", hue="OCCUPATION_TYPE", style="TARGET", data=df)
plt.title("Loan Amount vs Amount goods price by Occupation")
plt.show()


# # Interpretation 
# * The majority of loan applications are from applicants with occupation types of "Laborers" and "Sales staff".

# # Based on our analysis, we can draw the following conclusions regarding the likelihood of customers becoming defaulters:
# 
# # Defaulters:
# 
# * The count of the defaulters 8093.
# * Defaulters have lower income compared to non-defaulters, with the median income around 120K.
# * There is a positive correlation between loan amount and income for defaulters, with the median loan amount around 270K.
# * Defaulters tend to have more children compared to non-defaulters.
# 
# 
# # Non-defaulters:
# 
# * The count of the non-defaulters is 91907.
# * Non-defaulters have higher income compared to defaulters, with the median income around 170K.
# * There is a positive correlation between loan amount and income for non-defaulters, with the median loan amount around 530K.
# * Non-defaulters tend to have fewer children compared to defaulters.
# 
# # 50-50 chances:
# 
# * Applicants with 50-50 chances are evenly distributed across all age groups.
# * Applicants with 50-50 chances have income levels between those of defaulters and non-defaulters, with the median income around 145K.
# * There is a positive correlation between loan amount and income for applicants with 50-50 chances, with the median loan amount around 400K.
# * Applicants with 50-50 chances tend to have fewer children compared to defaulters and more children compared to non-defaulters.
