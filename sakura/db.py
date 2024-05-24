from pymongo import MongoClient

# Function to insert a new chat
def insertChat(chat_id, user_id, char_id, mongoURI):
    client = MongoClient(mongoURI)
    db = client['SAKURA']

    # Define the chat collection
    chat_collection = db['Chat']
    # Insert the chat data into the collection
    chat_collection.insert_one({'chat_id': chat_id, 'user_id': user_id, 'char_id': char_id})
    return True

# Function to get a chat id by user id
def getChatId(user_id, mongoURI):
    client = MongoClient(mongoURI)
    db = client['SAKURA']

    # Define the chat collection
    chat_collection = db['Chat']

    # Find the chat data by user id
    chat = chat_collection.find_one({'user_id': user_id})
    if chat:
        print(chat['chat_id'])
        return chat['chat_id']
    else:
        print("NOT Found")
        return None

def delete_sakura_database(mongoURI):
    client = MongoClient(mongoURI)
    client.drop_database('SAKURA')
    print("SAKURA database deleted successfully.")
    return True