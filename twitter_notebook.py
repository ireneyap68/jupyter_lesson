#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver


# In[2]:


import json, re, datetime, time, requests


# In[8]:


# Start the driver
driver = webdriver.Chrome(executable_path='/Users/airine/Downloads/chromedriver')
print(driver)

# driver.quit()


# In[10]:


# Goto Twitter
driver.get('https://twitter.com/login')
print('*', 'going to twitter')


# In[23]:


# get username, input username
username = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
username.send_keys('airine02823604')


# In[24]:


from keys import password


# In[30]:


password_input = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
print(password_input)
password_input.send_keys('password1234')
print('*','This is working...')


# In[31]:


# Make login button, and click login
login_button = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div')
login_button.click()


# In[34]:


tweet = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[4]/div/div/section/div/div/div[13]/div/div/article/div/div').text
print(tweet)


# In[36]:


tweet_list = tweet.split('\n')
print(tweet_list)


# In[45]:


name = tweet_list[0]
username = tweet_list[1]
actual_tweet = tweet_list[5:-3]

final_tweet = " ".join(actual_tweet)
likes = tweet_list[-1]

print(final_tweet)


# In[40]:


import pymongo


# In[43]:


myclient = pymongo.MongoClient('mongodb://localhost:27017/')
print(myclient)
print(myclient.list_database_names())


# In[44]:


mydb = myclient['database']
tweetCollection = mydb['tweets']


# In[46]:


data = {
    "name": name,
    "username": username,
    "tweet": final_tweet,
    "likes": likes
}


# In[47]:


tweetCollection.insert_one(data)


# In[48]:


print(tweetCollection.find_one())


# In[ ]:




