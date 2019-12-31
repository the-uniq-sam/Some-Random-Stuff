import requests
url = 'https://docs.google.com/forms/d/e/1FAIpQLSeMWPlkDtiqAexTV9mzrjIFStgAuJ4RR6H1zjohW_nZJpUhNw/formResponse'
f_data = {'entry.1332256353':'why not'}

user_agent = {'Referer':'https://docs.google.com/forms/d/e/1FAIpQLSeMWPlkDtiqAexTV9mzrjIFStgAuJ4RR6H1zjohW_nZJpUhNw/formResponse', 'User-Agent':"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}

r = requests.post(url, data = f_data, headers = user_agent)
print(r)
