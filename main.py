from astrapy.collections import create_client, AstraCollection
import os

ASTRA_DB_ID = os.environ['id']
ASTRA_DB_REGION = os.environ['region']
ASTRA_DB_APPLICATION_TOKEN = os.environ['token']
ASTRA_DB_KEYSPACE = os.environ['keyspace']
TEST_COLLECTION_NAME = "test"

astra_client = create_client(astra_database_id=ASTRA_DB_ID,
                                astra_database_region=ASTRA_DB_REGION,
                                astra_application_token=ASTRA_DB_APPLICATION_TOKEN)
db_namespace = astra_client.namespace(ASTRA_DB_KEYSPACE)
q_collection = db_namespace.collection(TEST_COLLECTION_NAME)

def get_items():
    documents = q_collection.find(query={})

print('query...')
get_items()
print('done.')