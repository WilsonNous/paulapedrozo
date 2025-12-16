from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# =========================
# HOME
# =========================
@app.route("/")
def home():
    return render_template("index.html")

# =========================
# FORMULÁRIO (LEAD)
# =========================
@app.route("/contato", methods=["POST"])
def contato():
    nome = request.form.get("nome")
    email = request.form.get("email")
    telefone = request.form.get("telefone")
    mensagem = request.form.get("mensagem")

    # MVP: apenas log (DB entra depois)
    print("📩 Novo contato recebido:")
    print(nome, email, telefone, mensagem)

    return redirect(url_for("home"))

# =========================
# START
# =========================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
