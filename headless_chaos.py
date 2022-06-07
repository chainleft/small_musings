import pandas as pd
import requests
import json

resplist = list()
for i in range(20000):
	if i%5 == 0:
		print("Song #",str(i)," is running")
	url = "https://ipfs.io/ipfs/bafybeic3pw5dd6tsu67mpgcm3mj5x335nfmq7xpesomv3uyuqluv2srsg4/"+str(i)+".json"
	response = requests.request("GET", url)
	response_json = response.json()
	resplist.append(response_json)

df_resp = pd.DataFrame(resplist)
df_resp.to_csv("Headless_Chaos.csv")
