# -*- coding: utf-8 -*-
import urllib
import urllib2
import json

# Construct the procedure name, parameter list, and URL.
# url = 'http://localhost:8080/api/1.0/'
# voltparams = json.dumps(["02/08/2018","00:00","34555"])
# httpparams = urllib.urlencode({
#     'Procedure': 'InsertIntoAcidente',
#     'Parameters' : voltparams
# })
def select_acidente(u):
    url = 'http://localhost:8080/api/1.0/'
    voltparams = json.dumps([u])
    httpparams = urllib.urlencode({
        'Procedure': 'Select',
        'Parameters' : voltparams
        })
    data = urllib2.urlopen(url, httpparams).read()
    result = json.loads(data)
    teste=result[u'results'][0]
    print(teste.keys())
    print (teste[u'data'])


# Execute the request


# Decode the results
select_acidente(3687941)
