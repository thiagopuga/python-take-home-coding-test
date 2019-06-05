# consumir stream de mudanças recentes do wikipedia
from sseclient import SSEClient as EventSource
# manipular estruturas JSON
import json
# utilizar banco de dados mongodb
import pymongo
# formatar data e hora
import datetime
# criar gráfico
import matplotlib
import matplotlib.pyplot as plt

# url do stream
streamURL = 'https://stream.wikimedia.org/v2/stream/recentchange'
# url do banco de dados
databaseURL = 'mongodb://localhost:27017/'
# nome do banco de dados
databaseName = 'task3'
# nome da coleção
collectionName = 'recent_change_stream_wikipedia'
# nome arquivo json
jsonName = 'recent_change_stream_wikipedia.json'
# nome arquivo html
htmlName = 'Recent Change Stream.html'
# definir fonte do gráfico
font = {'family': 'monospace',
        'weight': 'normal',
        'size'  : 6}
# utilizar fonte definida
matplotlib.rc('font', **font)

# função utilizada para se conectar ao cliente do mongodb
def connectToClient(databaseURL):
        # conectar cliente mongodb
        client = pymongo.MongoClient(databaseURL)
        return client

# função utilizada para criar ou usar um banco de dados já existente
def openDatabase(databaseName):
        # criar/usar banco de dados
        database = client[databaseName]
        return database

# função utilizada para criar ou usar uma coleção já existente
def openCollection(collectionName):
        # criar/usar coleção
        collection = database[collectionName]
        return collection

# função utilizada para excluir a coleção caso ela já existente (debug)
def deleteCollection(collection, collectionName):
        # caso coleção esteja com dados
        if collection.count_documents({}) > 0:
                # apagar coleção
                collection.drop()
                # recriar coleção
                collection = database[collectionName]
                # imprimir coleção apagada
                print('DEBUG - collection deleted')
                print('\n')

# função utilizada para criar o gráfico utilizado na página html
def buildGraph(aggregation):
        # inicializar eixos
        axisX = list()
        axisY = list()
        # obter campos do agrupamento
        for aggregationElement in aggregation:
                # obter valores
                idTime = aggregationElement['_id']
                countChanges = aggregationElement['count_changes']
                # formatar data e hora
                dateTime = datetime.datetime.fromtimestamp(idTime).strftime('%H:%M:%S')                
                # adicionar valores
                axisX.append(dateTime)
                axisY.append(countChanges)
        # definir tamanho do gráfico
        plt.figure(figsize = (12, 6))
        # adicionar título
        plt.suptitle('Task 4 - Recent Change Stream Graph (REFS 5s)', fontsize = 16)
        # adicionar valores
        plt.plot(axisX, axisY)
        # adicionar legendas
        plt.ylabel('Recent Changes', fontsize = 10)
        plt.xlabel('Timestamp', fontsize = 10)
        # rotacionar valores do eixo X
        plt.xticks(rotation = 45)
        # salvar gráfico
        plt.savefig('Recent Change Stream Graph.png')
        # fechar gráfico
        plt.close()

# código principal

# criar/usar arquivo json
fileJSON = open(jsonName, 'w')

# conectar cliente mongodb
client = connectToClient(databaseURL)
# criar/usar banco de dados
database = openDatabase(databaseName)
# criar/usar coleção
collection = openCollection(collectionName)

# apagar coleção caso exista (debug)
deleteCollection(collection, collectionName)

# repetir para cada elemento dentro do eventsource
for eventSourceElement in EventSource(streamURL):
        # filtrar eventos do tipo mensagem
        if eventSourceElement.event == 'message':
                try:
                        # ler recent change
                        recentChange = json.loads(eventSourceElement.data)
                        # filtrar alterções non-bot (task 1)
                        if not recentChange['bot']:
                                # escrever change formatada no arquivo json (task 1)
                                json.dump(recentChange, fileJSON, indent=4)
                                fileJSON.write('\n')
                                # inserir change no database mongodb (task 2)
                                insertOneResult = collection.insert_one(recentChange)
                                # agrupar inserções por timestamp
                                # limitado a x exibições
                                # ordenado do menor para o maior timestamp
                                cursor = collection.aggregate([{'$group': {'_id': '$timestamp', 'count_changes': {'$sum': 1}}}, {'$limit': 20}, {'$sort': {'_id': 1}}])
                                # listar agrupamento
                                aggregation = list(cursor)
                                # construir gráfico
                                buildGraph(aggregation)
                                # imprimir change (task 1)
                                print('Task 2 - {user} edited {title}'.format(**recentChange))
                                # imprimir o id da inserção (task 2)
                                print('Task 3 - inserted id:', insertOneResult.inserted_id)
                                print('\n')
                except ValueError:
                        continue

# fechar arquivo json
fileJSON.close()
