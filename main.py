import tkinter, webbrowser
from CodeHTTP import CodeHTTP
from AmazonURLGenerator import AmazonURLGenerator
from AmazonAdsLocation import AmazonAdsLocation
from http.server import HTTPServer, ThreadingHTTPServer
import threading, requests
from AuthCodeResponse import AuthCodeResponse

httpServer: HTTPServer = None
def startServer():
    global httpServer 
    httpServer = ThreadingHTTPServer(("127.0.0.1", 9999), CodeHTTP)
    httpServer.serve_forever()

    

serverThread = threading.Thread(target=startServer)
serverThread.start()

def loginButtonCallback():
    webbrowser.open(AmazonURLGenerator().createURL(AmazonAdsLocation.Europe, "amzn1.application-oa2-client.9bec6d95acb24c8d9966fe497dc68ee9", "advertising::campaign_management"))

def checkButtonCallback():
    codeLabel.config(text=AuthCodeResponse.code)

    threading.Thread(target=sendGetRefreshTokenRequest).start()

def sendGetRefreshTokenRequest():
    url = "https://api.amazon.co.uk/auth/o2/token"

    payload = f"grant_type=authorization_code&code={AuthCodeResponse.code}&client_id=amzn1.application-oa2-client.9bec6d95acb24c8d9966fe497dc68ee9&redirect_uri=http://127.0.0.1:9999&client_secret=amzn1.oa2-cs.v1.2a9d5c2438a383d6996b34ff8667a4c34d9c81f8d01f48cb7e30e169b71deaea"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)



root = tkinter.Tk()
root.geometry("400x400")
root.title("Report Downloader")

loginButton = tkinter.Button(root, text="Login to Amazon Ads API", command=loginButtonCallback)
loginButton.pack()

checkButton = tkinter.Button(root, text="Check Code", command=checkButtonCallback)
checkButton.pack()

codeLabel = tkinter.Label(root, text="No code")
codeLabel.pack()
root.mainloop()

httpServer.shutdown()
