import json

import typesense

client = typesense.Client({
  'nodes': [{
    'host': 'localhost',
    'port': '8108',
    'protocol': 'http'
  }],
  'api_key': 'xyz',
  'connection_timeout_seconds': 2
})

#collections = client.collections.retrieve()
#for collection in collections:
#    print(collection)

#client.collections['books_5'].delete()
#client.collections['books_4'].delete()
#client.collections['books_3'].delete()
#client.collections['books_2'].delete()
#client.collections['books'].delete()

documents = client.collections['books'].documents.search({'q': '*', 'query_by': 'title'})
print(documents)

schema = client.collections['books'].retrieve()
print(json.dumps(schema, indent=4))
