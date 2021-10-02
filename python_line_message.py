#http通信用ライブラリriquestsをimportする
import  requests

class line_notify:

    def __init__(self):
        self.TOKEN = 'Q48v5mnkZqspV3g1si83JhXzL2CV9Emn4KUEWUYwgRL'
        self.apl_url = 'https://notify-api.line.me/api/notify'

    def line_messeage(self, message):
        #変数send_contentsにLINEに通知したいメッセージを設定
        message = 'データの値は'+ message
        send_contents = message

        #BearerとTOKENの間に半角スペース
        TOKEN_dic = {'Authorization':'Bearer' + ' ' + self.TOKEN}
        send_dic = {'message': send_contents}

        print(TOKEN_dic)
        print(send_contents)

        requests.post(self.apl_url,headers=TOKEN_dic,data=send_dic)
