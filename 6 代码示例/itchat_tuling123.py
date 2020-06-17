import requests
import itchat

KEY = 'b16283170bb64b94ac494ffa85c8cce9'


def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': KEY,
        'info': msg,  # ??????????
        'userid': 'wechat-rebot',
    }
    try:

        r = requests.post(apiUrl, data=data).json()

        return r.get('text')
    except:
        pass


@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    # defaultReply = 'I received: ' + msg['Text']
    reply = '[tuling123API answer]' + get_response(msg)

    # return reply or defaultReply
    return reply

while True:
    text = input(">>> ")
    print(tuling_reply(text))
"""
itchat.auto_login(hotReload=True)
itchat.run()
"""