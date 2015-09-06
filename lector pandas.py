
# Referencia: ayudantía de Pandas

import pandas as pd
import json
import random
import numpy as np
import csv
import pprint


data = pd.read_csv('foursquare_checkins.csv')
checkins = data.shape
print("número de checkins: "+ str(checkins[0]))
n_users = data.user.unique().size
print("numero de usuarios: "+ str(n_users))
n_locations = data.location.unique().size
print("numero de ubicaciones: "+ str(n_locations))
checkins_prom_us = data.groupby('user').count().mean()[0]
print("numero de checkins por usuario: "+ str(checkins_prom_us))
 
 
checkins_prom_loc = data.groupby('location').count().mean()[0]
print("numero de checkins por ubicación: "+ str(checkins_prom_loc))

#sacar los datos de los amigos
friendship = pd.read_csv('foursquare_friendship.csv')
friendship.groupby('user1').count()


friends_per_user = friendship.groupby('user1').count().mean()
print("numero de amigos por usuario: "+ str(friends_per_user))

#friendship.shape()
#friendship.user1.unique().size

dict = {}

dict['n_user'] = n_users
dict['n_locations'] = n_locations
dict['checkins'] = checkins
dict['checkins_prom_us'] = checkins_prom_us
dict['friends_per_user'] = friends_per_user
dict['checkins_prom_loc'] = checkins_prom_loc

print(dict)

size = int(500) 
num_lines = 2290997

#skip = sorted(random.sample(xrange(num_lines), num_lines - size))
skip = np.random.choice(np.arange(1, num_lines+1), (num_lines - size), replace = False)

data_loc1 = pd.read_csv('foursquare_checkins.csv', skiprows = skip)

dat1 = data_loc1.transpose().to_dict().values()


print(dat1)



##print(data_loc1)

#data_loc2 = pd.DataFrame(index = data_loc1, )

#for row in data_loc:
#    loc = {}
#    loc['lat'] = data_loc1[1]
#    loc['long'] = data_loc1[2]
#        

with open('datos.json', 'w') as outfile: # con esto meto los datos al json
 	json.dump(dat1, outfile)
#	
#	
#jsonfile = open('datos.json', 'w')
#fieldnames = ("latitude", "longitude", "time")
#reader = csv.DictReader(data_loc1, fieldnames)
#for row in reader:
#        json.dump(row, jsonfile)
#        jsonfile.write("\n")
        
#with open('datos.json') as data_file:
#    data1 = json.load(data_file)
#    
#    
#pprint(data)

        
        
        