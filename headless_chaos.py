import pandas as pd
import requests
import json

resplist = list()

runit = True
trial = 0
i = 0
while runit == True and i < 20000:
	try:
		if trial == 5:
			break
		if i%5 == 0:
			print("Song #",str(i)," is running")
		url = "https://ipfs.io/ipfs/bafybeic3pw5dd6tsu67mpgcm3mj5x335nfmq7xpesomv3uyuqluv2srsg4/"+str(i)+".json"
		response = requests.request("GET", url)
		response_json = response.json()
		resplist.append(response_json)
		i = i+1
		trial = 0
	except:
		trial=trial+1
		pass

df_resp = pd.DataFrame(resplist)
df_resp.to_csv("Headless_Chaos.csv")
