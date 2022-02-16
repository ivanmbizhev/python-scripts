import webbrowser
#
#webbrowser.open("https://www.python.org/", new=1)

# help(webbrowser)

chrome = webbrowser.get(using='google-chrome').open_new("https://www.python.org/")