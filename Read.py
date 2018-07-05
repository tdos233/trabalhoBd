# -*- coding: utf-8 -*-
import csv
import urllib
import urllib2
import json


class indexs:
    date = 0
    time = 1
    borough = 2
    zipCode = 3
    latitude = 4
    longitude = 5
    location = 6
    onStreetName = 7
    crossStreetName = 8
    offStreetName = 9
    numberOfPersonsInjured = 10
    numberOfPersonsKilled = 11
    numberOfPedestriansInjured = 12
    numberOfPedestriansKilled = 13
    numberOfCyclistInjured = 14
    numberOfCyclistKilled = 15
    numberOfMotoristInjured = 16
    numberOfMotoristKilled = 17
    contributingFactorVehicle1 = 18
    contributingFactorVehicle2 = 19
    contributingFactorVehicle3 = 20
    contributingFactorVehicle4 = 21
    contributingFactorVehicle5 = 22
    uniqueKey = 23
    vehicleTypeCode1 = 24
    vehicleTypeCode2 = 25
    vehicleTypeCode3 = 26
    vehicleTypeCode4 = 27
    vehicleTypeCode5 = 28
                                               
    Column_Count = 29                                                                      

def read_data(path):
    with open(path, 'rb') as csvfile:
        csvReader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(csvReader)
        for row in csvReader:
            yield row
def InsertIntoAcidente(d,t,u):
    url = 'http://localhost:8080/api/1.0/'
    voltparams = json.dumps([d,t,u])
    httpparams = urllib.urlencode({
        'Procedure': 'InsertIntoAcidente',
        'Parameters' : voltparams
        })
    data = urllib2.urlopen(url, httpparams).read()
    result = json.loads(data)

def InsertIntoLocalidade(Id_local ,Bairro, ZipCode, Latitude, Longitude):
    url = 'http://localhost:8080/api/1.0/'
    voltparams = json.dumps([Id_local ,Bairro, ZipCode, Latitude, Longitude])
    httpparams = urllib.urlencode({
        'Procedure': 'InsertIntoLocalidade',
        'Parameters' : voltparams
        })
    data = urllib2.urlopen(url, httpparams).read()
    result = json.loads(data)

def InsertTipoPessoa(TipoPessoa_ID,Descricao):
    url = 'http://localhost:8080/api/1.0/'
    voltparams = json.dumps([TipoPessoa_ID,Descricao])
    httpparams = urllib.urlencode({
        'Procedure': 'InsertTipoPessoa',
        'Parameters' : voltparams
        })
    data = urllib2.urlopen(url, httpparams).read()
    result = json.loads(data)

def InsertTipoVeiculo(TipoVeiculo_ID,Descricao):
    url = 'http://localhost:8080/api/1.0/'
    voltparams = json.dumps([TipoVeiculo_ID,Descricao])
    httpparams = urllib.urlencode({
        'Procedure': 'InsertTipoVeiculo',
        'Parameters' : voltparams
        })
    data = urllib2.urlopen(url, httpparams).read()
    result = json.loads(data)

def InsertFator(Fator_ID,Descricao):
    url = 'http://localhost:8080/api/1.0/'
    voltparams = json.dumps([Fator_ID,Descricao])
    httpparams = urllib.urlencode({
        'Procedure': 'InsertFator',
        'Parameters' : voltparams
        })
    data = urllib2.urlopen(url, httpparams).read()
    result = json.loads(data)

def InsertAcidenteVeiculo(TipoVeiculo_ID, Fator_ID, UniqueKey):
    url = 'http://localhost:8080/api/1.0/'
    voltparams = json.dumps([TipoVeiculo_ID, Fator_ID, UniqueKey])
    httpparams = urllib.urlencode({
        'Procedure': 'InsertAcidenteVeiculo',
        'Parameters' : voltparams
        })
    data = urllib2.urlopen(url, httpparams).read()
    result = json.loads(data)

def InsertAcidentePessoa(TipoPessoa_ID, quantidadeFeridos, quantidadeMortos, UniqueKey):
    url = 'http://localhost:8080/api/1.0/'
    voltparams = json.dumps([TipoPessoa_ID, quantidadeFeridos, quantidadeMortos, UniqueKey])
    httpparams = urllib.urlencode({
        'Procedure': 'InsertAcidentePessoa',
        'Parameters' : voltparams
        })
    data = urllib2.urlopen(url, httpparams).read()
    result = json.loads(data)

def InsertAcidenteLocal(Id_local, UniqueKey, OnStreet, OffStreet, CrossStreet):
    url = 'http://localhost:8080/api/1.0/'
    voltparams = json.dumps([Id_local, UniqueKey, OnStreet, OffStreet, CrossStreet])
    httpparams = urllib.urlencode({
        'Procedure': 'InsertAcidenteLocal',
        'Parameters' : voltparams
        })
    data = urllib2.urlopen(url, httpparams).read()
    result = json.loads(data)


def select_acidente(u):
    url = 'http://localhost:8080/api/1.0/'
    voltparams = json.dumps([u])
    httpparams = urllib.urlencode({
        'Procedure': 'Select',
        'Parameters' : voltparams
        })
    data = urllib2.urlopen(url, httpparams).read()
    result = json.loads(data)
def carregar_csv():
    idx = indexs()
    Id_local=1
    InsertTipoPessoa(1,"Pessoa")
    InsertTipoPessoa(2,"Pedestre")
    InsertTipoPessoa(3,"Ciclista")
    InsertTipoPessoa(4,"Motorista")
    InsertTipoVeiculo()
    for rowIndex, row in enumerate(read_data('/home/thiago/Documentos/bd/NYPD_Motor_Vehicle_Collisions.csv')):
        InsertIntoAcidente(row[idx.date], row[idx.time], row[idx.uniqueKey])
        InsertIntoLocalidade(Id_local,row[borough],row[ZipCode],row[latitude],row[longitude])
        Id_local+=1
        InsertTipoVeiculo()
        InsertFator()
        InsertAcidenteLocal()
        InsertAcidentePessoa()
        InsertAcidenteVeiculo()
        
# -------------------------------------------------------

if __name__ == "__main__":
           
