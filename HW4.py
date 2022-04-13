#!/usr/bin/env python
# coding: utf-8

# In[208]:


#Michael Cohen 316372499
import json
import requests
api_key = "AIzaSyD7uaK6EnGeuXaGBwm_bD-WB-A5yrWjT_Q"


# In[209]:


data=open("C:\\Users\\mcohen\\Downloads\\dests.txt")
arr=[]
for i in data:
    arr.append(i.strip())
print(arr)    


# In[210]:


url=[]
urlgeo=[]
for i in arr:
    urlgeo.append("https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s"%(i,api_key))
    url.append("https://maps.googleapis.com/maps/api/distancematrix/json?origins=Jerusalem&destinations=%s&key=%s"%(i,api_key))
print(urlgeo)        


# In[230]:


distances=[]
for i in url:
    distances.append(requests.get(i).json())  

addresses=[]
for i in urlgeo:
    addresses.append(requests.get(i).json())
    
dic = {}
for i in range(5):
    dic[i] = (distances[i]['rows'][0]['elements'][0]['distance']['text'],
    distances[i]['rows'][0]['elements'][0]['duration']['text'],addresses[i]['results'][0]['geometry']['location']['lng'],
    addresses[i]['results'][0]['geometry']['location']['lat']  )   
    dic[arr[i]] = dic.pop(i)
print(dic)


# In[268]:


for i in arr:
    print(i ,'\ndistance : ', dic[i][0] , '\nduration : ', dic[i][1], '\nLongitude : ', dic[i][2], '\nLatitude : ', dic[i][3], '\n')
    


# In[337]:


array = []
for i in arr:
    dis = dic[i][0].split()
    array.append(int(dis[0].replace(',','')))

dic_far = []
for i in range(3):
    dic_far.append(max(array)) 
    array.remove(max(array))

array = []
for i in arr:
    dis = dic[i][0].split()
    array.append(int(dis[0].replace(',','')))

far_city = []
for i in range(3):
    for j in range(len(array)):
        if dic_far[i] == array[j]:
            far_city.append(arr[j])
print('The three farthest cities are : ', far_city)


# In[ ]:




