from pymongo import MongoClient
import config
from lib.queries.query import *
from time import localtime, strftime




dbClient = MongoClient(config.db_client)
collection = dbClient[config.db_name][config.db_collection_name]



"""
    Dates to query
"""
queryString = config.topicQuery
dateUntil = config.untilDateTopic
dateSince = config.sinceDateTopic



print(dbClient, collection, queryString, dateSince, dateUntil)
print(strftime("%Y-%m-%d %H:%M:%S", localtime()))

# Querying and storing data in mongo
# queryString, sinceDate, untilDate, mongoCollection, language='en'
#queryTopic(queryString, dateSince, dateUntil, collection)
