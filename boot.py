import requests, base64, os, threading, time
print("⚡ TESLA 369 BOT")
print("="*30)
print("🔑 Token...")
TK = requests.get("https://gist.githubusercontent.com/gynbetfc/7af02df43a6b967eea94a35f375b7c10/raw/token.txt", timeout=10).text.strip()
print("📥 Baixando...")
url = "https://api.github.com/repos/gynbetfc/v-sensitivo-bot/contents/main.py"
h = {"Authorization": "token " + TK, "Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=h)
if r.status_code == 200:
    data = r.json()
    codigo = base64.b64decode(data["content"]).decode("utf-8")
    def start(): exec(codigo)
    threading.Thread(target=start, daemon=True).start()
    time.sleep(5)
    print("📱 Chrome...")
    os.system("am start -a android.intent.action.VIEW -d http://localhost:5000")
    print("✅ Pronto!")
else:
    print(f"❌ Erro: {r.status_code}")
