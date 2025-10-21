import webbrowser as wb



def workauto ():
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    URLS =('gmail.com',
           'indeed.com',
           'linkedin.com',
           'facebook.com',
           'www.onlinejobs.ph')
    
    for url in URLS:
        wb.get(chrome_path).open(url)


workauto()