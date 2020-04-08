#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 00:13:39 2020

@author: renan
"""
import matplotlib.ticker as tck
import numpy as np
import matplotlib.pyplot as plt
import requests

api_url = 'https://api.nasa.gov/neo/rest/v1/neo/browse?api_key=4Octvw3qaCnUjUQdBd5LClsKNRaBYGjq566lWi6F'

req_url = requests.get(api_url)

tres_partes =[]
'''-------------------------------------------------------------------------'''
geral =[]
size =[]
links =[]

'''-------------------------------------------------------------------------'''
geraldata =[]
asteroid =[]
orbital_data =[]
'''-------------------------------------------------------------------------'''
names=[]
inclination=[]
if req_url.status_code == 200:

    dados = req_url.json()

    for elemento in dados:

        tres_partes.append(dados[elemento]) 
        
geral = tres_partes[0]
size = tres_partes[1]
links = tres_partes[2]



for i in range (0,len(geral),1):
    geraldata.append(geral[i].items())
   
for i in range (len(geraldata)):
    asteroid.append(geraldata[i])    


'''
name                 interval        type                        information

geral                 (0,19)         list        contais each asteroid's dictionary.  
geral[i]              (0,11)         dict        contains each asteroid information.
geral[i].items()      (0,11)         list        contains each asteroid information but as a list.
geraldata             (0,11)         list        
asteroid[i]           (0,11)         list        contais information of each asteroid.
asteroid[i][0]                                   all orbital data list
asteroid[i][3][1]                                absolute_magnitude_h
asteroid[i][5][1]                                asteroid's diameter 
asteroid[i][6][1]                                asteroid's close approach data
asteroid[i][8][1]                    bool        asteroid potentially hazardous (false or true)
asteroid[i][9][1]                    bool        asteroid is sentry object (false or true)
asteroid[i][10][1]                               asteroid's id                               
asteroid[i][11][1]    (0,1)          tuple       asteroid's name (i escolhe o asteroid)

asteroid[i][i][i]     
'''


''' 
orbital_data list:
    
orbital_data[i][0][1]                              last observation date
orbital_data[i][1][1]                              equinox
orbital_data[i][2][1]                              first observation date
orbital_data[i][3][1]
orbital_data[i][4][1]                             aphelion distance
orbital_data[i][5][1]                             data arc in days
orbital_data[i][6][1]
orbital_data[i][10][1]                             orbit id
orbital_data[i][11][1]                            inclination
orbital_data[i][15][1]                           jupiter tisserand invariant (JTI)
orbital_data[i][21][1]                           semi major axis
orbital_data[i][1][1]

'''



'''trocar o numero 11'''
for i in range(11):
    orbital_data.append(asteroid[i][0][1].items())
    





print'-----------------------------------------------------------------------------'
for i in range (0,len(asteroid),1):
    if asteroid[i][8][1] == False:
        print'The asteroid',asteroid[i][11][1],'\033[32m'+'is not HAZARDOUS'+'\033[32m'+'\033[0;0m'
    elif asteroid[i][8][1] == True:    
        print'The asteroid',asteroid[i][11][1],'\033[31m'+'is HAZARDOUS'+'\033[31m'+'\033[0;0m'

print'-----------------------------------------------------------------------------'      
for i in range (0,len(asteroid),1):
    if asteroid[i][9][1] == False:
        print'The asteroid',asteroid[i][11][1],'\033[32m'+'is not a sentry object'+'\033[32m'+'\033[0;0m'
    elif asteroid[i][9][1] == True:    
        print'The asteroid',asteroid[i][11][1],'\033[31m'+'is a sentry object'+'\033[31m'+'\033[0;0m'
        
'''trocar o numero 11'''

for i in range(0,11,1):
    names.append(asteroid[i][11][1])
    inclination.append(orbital_data[i][11][1]) 
    
    
'''
fig1, ax = plt.subplots() #anexa os subplots na figura

ax.yaxis.set_minor_locator(tck.AutoMinorLocator())
plt.rcParams['figure.figsize'] = (70,20)    
plt.bar(names,inclination)     
#plt.show()
fig1.savefig('asteroid inclination comparison')
'''
print '---------------------------------------------------'
last_observation_date=[] 

for i in range(0,11,1):
    
    last_observation_date.append(asteroid[i][0][1].items()[0][1])#last_observation
    
first_observation_date=[]

for i in range(0,11,1):
    first_observation_date.append(asteroid[i][0][1].items()[2][1])
    
for i in range(0,11,1):
    print 'The first observation of this asteroid was', first_observation_date[i],'\n' ,'The last observation of this asteroid was', last_observation_date[i]   
    print '---------------------------------------------------'
    
