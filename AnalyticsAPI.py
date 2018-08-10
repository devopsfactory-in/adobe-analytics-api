import requests
import datetime
import time
import ReportSuite as reportsuite
import configparser
import argparse
import json
import sys

tokenurl = 'https://api.omniture.com/token'

parser = argparse.ArgumentParser()
parser.add_argument("--rsid", nargs='?', help='reportsuite id',default="",required=True)
parser.add_argument("--create",  help='create newreport suite',action='store_true')
parser.add_argument("--update",  help='update settings of reportsuite report suite',action='store_true')

args=parser.parse_args()

rsid=args.rsid
create=args.create
update=args.update

config = configparser.ConfigParser()
config.read('resources/configparams.ini')

clientid=config['DEFAULT']['client_id']
clientsecret=config['DEFAULT']['client_secret']

  
def createnewreportsuite():
    try:
        print('>>>Creating new reportsuite')
        rs=reportsuite.ReportSuite()
        rs.create(access_token,data); 
        updatereportsuite()
    except:
        type,value,traceback=sys.exc_info()
        print("Exception -  ",type,value,traceback.tb_frame.f_code.co_filename,traceback.tb_lineno)


def updatereportsuite():
    try:
        print('>>>Updating new reportsuite')
        rs=reportsuite.ReportSuite()
        #to enable adhoc result
        rs.saveDiscoverEnabled(access_token,rsid)
        rs.getSettings(access_token,rsid) 
    except:
        type,value,traceback=sys.exc_info()
        print("Exception -  ",type,value,traceback.tb_frame.f_code.co_filename,traceback.tb_lineno)  

def getaccesstoken():
        data = {'grant_type': 'client_credentials'}
        session = requests.post(tokenurl,data=data,auth=(clientid, clientsecret))
        json_obj=json.loads(session.text);
        access_token = json_obj.get('access_token')
        return access_token;



#getting auth2 access token
access_token=getaccesstoken()

with open('resources/CreateRS.json') as json_file:
    data=json.load(json_file)

    today=datetime.date.today().strftime("%m/%d/%y")
    data['go_live_date']=today;
    data['rsid']=rsid;


#invoke crreate new reportsuite method
if create:
    createnewreportsuite()

#invoke crreate new reportsuite method
if update:
    updatereportsuite()
