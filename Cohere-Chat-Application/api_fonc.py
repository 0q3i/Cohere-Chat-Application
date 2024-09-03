import cohere

#DO NOT MODIFIE UNLESS YOU KNOW WHAT YOU ARE DOING 
cohere_chat = None #used to hold cohere response
history=[

        ]
    # A dynamique history to provide context to a conversation 

def chatLLM(chat):
    #Returns cohere_chat by taking in history and chat  
    global cohere_chat
    global history
    
    co = cohere.Client(
        api_key="<Your-API-key>"
    )
    
    cohere_chat = co.chat(
        chat_history = history,
        message=chat,
        model="command"

    ) 
    
    return cohere_chat.text
    
def context(cohere_chat, chat):
    # adds to history what COHERE and USER said 
    global history
    
    dic_USER = {"role": "USER", "message": str(chat)}
    history.append(dic_USER)

    dic_COHERE = {"role": "CHATBOT", "message": str(cohere_chat)}
    history.append(dic_COHERE)
        
    return history
    
