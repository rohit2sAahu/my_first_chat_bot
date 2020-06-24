import requests as requests
url="https://api.telegram.org/bot1220208257:AAHXaiKfmRmEcXSlu--7ipx-f_oALkQP97Y/"
def chat_id(update):
    chat_id=update["message"]["chat"]["id"]
    return chat_id
def get_message(update):
    text_message=update["message"]["text"]
    return get_message
def last_update(req):
    response=requests.get(req+"getUpdates")
    response=response.json()
    result=response["result"]
    total_update=len(response)-1
    return result[total_update]
def send_message(chat_id,message_text):
    params={"chat_id":chat_id,"text":message_text}
    result=requests.post(url+"sendMessage",data=params)
    return result
def main():
    update_id=last_update(url)["update_id"]
    while True:
        update=last_update(url)
        if update_id==update["update_id"]:
            if get_message(update)=="hii"or get_message(update)=="hello":
                send_message(chat_id(update),"hey hii i am alexa  how can i help you type help for help")
            elif get_message(update)=="help":
                send_message(chat_id(update),"we are happy to help you press 1 to Continue")
            else:
                send_message(chat_id(update),"sorry wrong input type again ")
            update_id+=1
main()
                
            