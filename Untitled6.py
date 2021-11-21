#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Boolean Indexing in Pandas
import pandas as pd
import numpy as np
data = pd.read_csv("train.csv", index_col="Loan_ID")

data.loc[(data["Gender"]=="Female") & (data["Education"]=="Not Graduate") & (data["Loan_Status"]=="Y"), ["Gender","Education","Loan_Status"]]


# In[ ]:


#Determine pivot table
impute_grps = data.pivot_table(values=["LoanAmount"], index=["Gender","Married","Self_Employed"], aggfunc=np.mean)


# In[ ]:


#Pandas Crosstab
pd.crosstab(data["Credit_History"],data["Loan_Status"],margins=True)
def percConvert(ser):
  return ser/float(ser[-1])
  pd.crosstab(data["Credit_History"],data["Loan_Status"],margins=True).apply(percConvert, axis=1)


# In[ ]:


#Cut function for binning

#Binning:
def binning(col, cut_points, labels=None):
#Define min and max values:
    minval = col.min()
    maxval = col.max()

  #create list by adding min and max to cut_points
break_points = [minval] + cut_points + [maxval]

#if no labels provided, use default labels 0 ... (n-1)
  if not labels:
    labels = range(len(cut_points)+1)
#Binning using cut function of pandas
  colBin = pd.cut(col,bins=break_points,labels=labels,include_lowest=True)
    return colBin

#Binning age:
cut_points = [90,140,190]
labels = ["low","medium","high","very high"]
data["LoanAmount_Bin"] = binning(data["LoanAmount"], cut_points, labels)
print pd.value_counts(data["LoanAmount_Bin"], sort=False)


# In[ ]:


#Coding nominal data using Pandas

#Define a generic function using Pandas replace function
def coding(col, codeDict):
    colCoded = pd.Series(col, copy=True)
    for key, value in codeDict.items():
    colCoded.replace(key, value, inplace=True)
    return colCoded
 
#Coding LoanStatus as Y=1, N=0:
print 'Before Coding:'
print pd.value_counts(data["Loan_Status"])
data["Loan_Status_Coded"] = coding(data["Loan_Status"], {'N':0,'Y':1})
print '\nAfter Coding:'
print pd.value_counts(data["Loan_Status_Coded"])


# In[ ]:




