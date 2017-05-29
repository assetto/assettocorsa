# FetchParge-code originated by Stereo (stereo_minoprint.py)
# personally I have no clue what I'm doing, so please call in if you see improvements
import ac
import json
import threading

try:
  import urllib.request
  import urllib.parse
except Exception as ex:
  ac.log("helicorsa::urllib not imported: {}".format(str(ex)))

# We'll store any result we get from the MR backend here, it's assumed that
# some other piece of code just uses this AND SETs TO NONE THEN
lastResult = None
requestPending = False

# The result contains some Ids that will speed up the query massively,
# so we'll just store them on the fly
lastMRSessionId = -1
driverSteamId = -1

# driver name, car model and track are unique per Helicorsa session, they only need to be setup once
driverName = ""
carModel = ""
track = ""

# this is the template for the web request
urlstrtemplate = 'http://app.minorating.com:805/minodata/getMRServerInfo/?id={}&session={}&name={}&model={}&track={}&anotherDriver=&sessionType=&serverIp={}&serverPort={}'
urlstr = ""

def initConstants():
    global driverName, carModel, track

    driverName = ac.getDriverName(0)
    carModel =ac.getCarName(0)
    track = ac.getTrackName(0)
    if(str(ac.getTrackConfiguration(0)) == "-1"):
        track = track + "[]"
    else:
        track = track + "[" + ac.getTrackConfiguration(0) + "]"

def requestMinoratingData():
    global requestPending, urlstr

    if requestPending == False:
        urlstr = urlstrtemplate.format(driverSteamId, lastMRSessionId, driverName, carModel, track, ac.getServerIP(), ac.getServerHttpPort())
        ac.log("helicorsa::FetchPage.Start(): " + urlstr)
        requestPending = True
        FetchPage().start()

class FetchPage(threading.Thread):
    def run(self):
        global requestPending, lastResult, lastMRSessionId, driverSteamId

        try:
            # this replaces spaces with %20 and so forth
            url = urllib.parse.quote(urlstr, safe="%/:=&?~#+!$,;'@()*[]")
            with urllib.request.urlopen(url, timeout=5) as mresponse:
                request_resp = mresponse.read().decode('utf-8')
                json_data = json.loads(request_resp)
                lastResult = json_data
                lastMRSessionId = json_data["sessionId"]
                if driverSteamId == -1:
                    driverSteamId = json_data["driverSteamId"]
        except Exception as e:
            lastResult = {}
            lastResult["errorMsg"] = "web request error {}".format(e)
        requestPending = False