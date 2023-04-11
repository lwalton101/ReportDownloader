import tkinter

def loginButtonCallback():
    print("hello world")

root = tkinter.Tk()
root.geometry("400x400")
root.title("Report Downloader")

loginButton = tkinter.Button(root, text="Login to Amazon Ads API", command=loginButtonCallback)
loginButton.pack()
root.mainloop()


