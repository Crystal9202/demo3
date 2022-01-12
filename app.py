from flask import Flask, request ,jsonify
from linebot import LineBotApi
from linebot.models import TextSendMessage
import time
app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"message":"Crystal!"})


@app.route("/myapi", methods = ['POST'])
def myapi():
    data = request.get_json()
    if data['password'] == 123:
        from linebot import LineBotApi
        from linebot.models import TextSendMessage

        line_bot_api = LineBotApi('AyR5HX3JZp44DRfcTWoIy5H7Lr0tgxvk52Bu0fc3epviMspQu64b0BNYNEyH9W3HV3eW3/2+rtiFtX3Tel/81DXsPXxRecJFl1ZZgSNQfloXdAQ+IXF+xhEjZBpNDSvw0ou/1BsrrV/OTGxFGQ0JIwdB04t89/1O/w1cDnyilFU=')
        yourID = 'U16fa4929599e4ae13eddc7e3f71c9083'
        # member_ids_res = line_bot_api.get_group_member_ids()
        # line_bot_api.push_message(yourID, 
        #                   TextSendMessage(text=data['message']))
        
        line_bot_api.broadcast(TextSendMessage(text=data['message']))     
        return {"message": "success"}
    return {"message": "fail"}


# import os
# if __name__ == "__main__":
#     port = int(os.environ.get('PORT', 5000))
#     app.run(host='0.0.0.0', port=port)
