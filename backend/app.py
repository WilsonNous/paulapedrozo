from flask import Flask, render_template, request, redirect, url_for
import os
from datetime import datetime

app = Flask(__name__)

# =========================
# PÁGINAS
# =========================

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/atendimento")
def atendimento():
    return render_template("atendimento.html")


@app.route("/mentoria")
def mentoria():
    return render_template("mentoria.html")


@app.route("/devocional")
def devocional():
    return render_template("devocional.html")


@app.route("/agendamento")
def agendamento():
    return render_template("agendamento.html")


@app.route("/contato", methods=["GET"])
def contato_page():
    return render_template("contato.html")


# =========================
# FORMULÁRIO (LEAD)
# =========================
@app.route("/contato", methods=["POST"])
def contato_submit():
    nome = request.form.get("nome")
    email = request.form.get("email")
    telefone = request.form.get("telefone")
    interesse = request.form.get("interesse")
    mensagem = request.form.get("mensagem")

    # MVP: apenas log (DB entra depois)
    print("===================================")
    print("📩 Novo contato recebido")
    print(f"🕒 Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"👤 Nome: {nome}")
    print(f"📧 Email: {email}")
    print(f"📱 Telefone: {telefone}")
    print(f"🎯 Interesse: {interesse}")
    print(f"💬 Mensagem: {mensagem}")
    print("===================================")

    # Futuro:
    # - salvar no MySQL
    # - disparar WhatsApp / e-mail
    # - classificar lead por interesse

    return redirect(url_for("home"))


# =========================
# START (LOCAL / RENDER)
# =========================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
