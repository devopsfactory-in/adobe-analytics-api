import requests
import json
import sys

class ReportSuite:
    def __init__(self):
        self.resturl = 'https://api.omniture.com/admin/1.4/rest/?method='
        self.accesstokenurl='&access_token='

        self.createurl='ReportSuite.Create'
        self.getsettingsurl='ReportSuite.GetSettings'
        #discover enabled is same as adhoc enable
        self.savediscoverenabledurl='ReportSuite.SaveDiscoverEnabled'
       

    def create(self,access_token,data):
        session = requests.post(self.resturl+self.createurl+self.accesstokenurl+access_token,data=data)
        return session.text;



    def getSettings(self,access_token,rsid):
        data = {
          'rsid_list': [rsid]
        }
        
        session = requests.post(self.resturl+self.getsettingsurl+self.accesstokenurl+access_token,data=json.dumps(data))
        try:
            print('>>>Settings returned for {}',rsid)
            return session.json
        except:
            return session.text;       
        

    def saveDiscoverEnabled(self,access_token,rsid):
        try:
            data = {
             'discover_enabled': True,
             'rsid_list': [rsid]
            }
            session = requests.post(self.resturl+self.savediscoverenabledurl+self.accesstokenurl+access_token,data=json.dumps(data))

            try:
                print('>>>Adhoc report enabled for {}',rsid)
                return session.json
            except:
                return session.text;
        except:
            type,value,traceback=sys.exc_info()
            print("Exception in saveDiscoverEnabled() -  ",type,value,traceback.tb_frame.f_code.co_filename,traceback.tb_lineno)  

    
