
# coding: utf-8

# Machine learning with Decision Tree
# 
# In this section we will predict whether a bank note is authentic or fake depending upon the four different attributes of the image of the note. The attributes are Variance of wavelet transformed image, curtosis of the image, entropy, and skewness of the image.

# In[43]:


#importing libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report,confusion_matrix


# In[6]:


#importing dataset
data=pd.read_csv('C:\\Users\\Rohit\\Desktop\\Kaggle\\bill_authentication.csv',sep=',')


# In[7]:


#preview of data
data.head()


# In[8]:


#shape of data (row,column)
data.shape


# In[9]:


data.describe()


# In[12]:


#unique value in class
data['Class'].unique()


# Data exploration|

# In[15]:


#when class=0
data[data['Class']==0].describe()


# In[16]:


#when class=1
data[data['Class']==1].describe()


# In[19]:


#distribution of class
data['Class'].value_counts()


# In[24]:


#Missing value
data.isnull().any()


# In[25]:


#creating x and y dataset
x=data.drop('Class',axis=1)
y=data['Class']


# In[27]:


x.head()


# In[29]:


y.head()


# In[35]:


#spliting data into  train and test dataset
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)


# In[37]:


x_train.shape


# In[39]:


x_test.shape


# Training decision tree model

# In[41]:


decision_classifier=DecisionTreeClassifier()
decision_classifier.fit(x_train,y_train)


# Prediction and evalution of decision tree

# In[42]:


y_pred=decision_classifier.predict(x_test)


# In[45]:


#accuracy
print (confusion_matrix(y_test,y_pred))


# In[46]:


print(classification_report(y_test,y_pred))


# Visualize the decision tree 

# In[53]:


from sklearn.tree import export_graphviz
with open("decision_classifier.txt", "w") as f:
    f = export_graphviz(decision_classifier, out_file=f)
    


# 
# To visualize the decision tree, you just need to open the decision_classifier.txt file and copy the contents of the file to paste in the graphviz web portal. Below is the address for the web portal.
# 
# http://webgraphviz.com
# 
