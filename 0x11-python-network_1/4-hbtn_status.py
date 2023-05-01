#!/usr/bin/python3
"""Script that fetches https://alx-intranet.hbtn.io/status."""	
import requests
		
if __name__ == "__main__": 
    r = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type:", type(str(r)))
    print("\t- content:", r.content.decode("utf-8"))
