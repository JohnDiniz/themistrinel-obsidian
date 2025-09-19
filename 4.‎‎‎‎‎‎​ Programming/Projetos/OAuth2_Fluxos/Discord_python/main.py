from flask import Flask, redirect, request, jsonify
import requests

app = Flask(__name__)

CLIENT_ID = "1233086097760845868"
CLIENT_SECRET = "M4K3kh3QHn-mK_jxivBIIf_IEgyaNecc"
REDIRECT_URI = "http://localhost:5000/callback"

TOKEN_URL = "https://discord.com/api/oauth2/token"
USER_URL = "https://discord.com/api/users/@me"

@app.route("/")
def home():
    return '''
    <h1>Login com Discord</h1>
    <a href="https://discord.com/api/oauth2/authorize?client_id=1233086097760845868&redirect_uri=http%3A%2F%2Flocalhost%3A5000%2Fcallback&response_type=code&scope=identify%20email">
        Entrar com Discord
    </a>
    '''

@app.route("/callback")
def callback():
    code = request.args.get("code")
    if not code:
        return "Nenhum código recebido!"

    # Trocar code por access token
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    r = requests.post(TOKEN_URL, data=data, headers=headers)
    token_info = r.json()
    
    access_token = token_info.get("access_token")
    if not access_token:
        return f"Erro ao obter token: {token_info}"

    # Pegar informações do usuário
    headers = {"Authorization": f"Bearer {access_token}"}
    user_resp = requests.get(USER_URL, headers=headers)
    user_data = user_resp.json()
    
    return jsonify(user_data)

if __name__ == "__main__":
    app.run(debug=True)
