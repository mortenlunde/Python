import json
import typesense

def client_connection():
    client = typesense.Client({
      'nodes': [{
        'host': 'localhost',
        'port': '8108',
        'protocol': 'http'
      }],
      'api_key': 'xyz',
      'connection_timeout_seconds': 2
    })
    return client

def add_book_collection(client):
    books_schema = {
      'name': 'books',
      'fields': [
        {'name': 'title', 'type': 'string' },
        {'name': 'authors', 'type': 'string[]', 'facet': True },
        {'name': 'publication_year', 'type': 'int32', 'facet': True },
        {'name': 'ratings_count', 'type': 'int32' },
        {'name': 'average_rating', 'type': 'float' }
      ],
      'default_sorting_field': 'ratings_count'
    }

    try:
        client.collections.create(books_schema)
        print("Collection created successfully.")
    except Exception as e:
        print(f"Error creating collection: {e}")

# Check if collection exists and delete it
def check_collection(client):
    try:
        client.collections['books'].retrieve()
        print("Collection already exists. Deleting it...")
        client.collections['books'].delete()
        print("Collection deleted.")
    except Exception as e:
        print(f"Collection does not exist or another error occurred: {e}")

# Import documents from JSONL file and handle errors
def import_books(client):
    try:
        with open('books.jsonl') as jsonl_file:
            client.collections['books'].documents.import_(jsonl_file.read().encode('utf-8'))
            print("Documents imported successfully.")
    except Exception as e:
        print(f"Error importing documents: {e}")

# Search the collection
def search_books(client):
    try:
        search_parameters = {
            'q'         : 'harry potter',
            'query_by'  : 'title',
            'sort_by'   : 'ratings_count:desc'
        }

        search_results = client.collections['books'].documents.search(search_parameters)

        # Write the search results to a file
        with open('search_results.json', 'w') as json_file:
          json.dump(search_results, json_file, indent=4)  # indent=4 for pretty printing

        print("Search results saved to 'search_results.json'.")

        print("")
        print("Search Results:")
        for hit in search_results['hits']:
          document = hit['document']
          print(f"Title: {document['title']}")
          print(f"Authors: {', '.join(document['authors'])}")
          print(f"Publication Year: {document['publication_year']}")
          print(f"Ratings Count: {document['ratings_count']}")
          print(f"Average Rating: {document['average_rating']}")
          print(f"Highlighted Title: {hit['highlight']['title']['snippet']}")
          print("-" * 40)
    except Exception as e:
        print(f"Error during search: {e}")

def main():
    client = client_connection()
    check_collection(client)
    add_book_collection(client)
    import_books(client)
    search_books(client)

if __name__ == '__main__':
    main()