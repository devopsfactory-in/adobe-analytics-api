# adobe-analytics-api
Adobe provides APIs for the Adobe Experience Cloud, here we are using Adobe Analytics API 1.4 to automate reportsuite creation and settings updation. 

## Prerequisites

Before you set up your OAuth client, make sure you

    - Have valid Adobe ID credentials.

    - Have access to the Marketing Cloud.

 For this example we are using Client Credentials Grant method, you can find more details here https://github.com/AdobeDocs/analytics-1.4-apis/blob/master/docs/authentication/auth_client_credentials.md

* client_id - The client ID is defined when you register your app.
* client_secret - The client secret is defined when you register your app.


## To run locally

* Configure client_id and client_secret in 'resourcer/configureparams.ini'

```
client_id=<clientid>
client_secret=<clientsecre
```

*  To create a new report suite, just change the duplicate_rsid of'resource/CreateRS.json' with valid reportsuiteid (The neewly created reportsuite is based on the duplicate_rsid, all evars, events, props of duplicate_rsid shoudl be copied to the new reportsuite). Then execute the following script,

```
 python AnalyticsAPI.py --create --rs=<newreportsuitename>

```

* To update existing reportsuite please use the following script,
```
 python AnalyticsAPI.py --update --rs=<reportsuitename>

```