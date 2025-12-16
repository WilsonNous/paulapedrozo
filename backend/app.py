from flask import Flask, render_template, request, redirect, url_for
import os
from datetime import datetime

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
    #
