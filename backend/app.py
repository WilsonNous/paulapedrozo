from flask import Flask, render_template, request, redirect, url_for, jsonify
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

    return redirect(url_for("home"))


# =========================
# ASSISTENTE VIRTUAL (MVP)
# =========================
@app.route("/assistente", methods=["POST"])
def assistente():
    data = request.get_json(silent=True) or {}
    etapa = data.get("etapa")
    resposta = (data.get("resposta") or "").strip()

    # Log simples (evolui depois para DB)
    print("🤖 Assistente | Etapa:", etapa, "| Resposta:", resposta)

    if etapa == "inicio":
        return jsonify({
            "mensagem": (
                "Olá! Sou o assistente virtual da Paula Pedrozo 😊\n\n"
                "Posso te ajudar com:\n"
                "1️⃣ Atendimento individual\n"
                "2️⃣ Mentoria para mães\n"
                "3️⃣ Devocional / Livro\n"
                "4️⃣ Agendamento\n\n"
                "Digite o número da opção desejada."
            ),
            "proxima_etapa": "menu"
        })

    if etapa == "menu":
        if resposta == "1":
            return jsonify({
                "mensagem": (
                    "O atendimento é realizado de forma online, "
                    "com ética, sigilo e cuidado.\n\n"
                    "Posso te direcionar para falar com a Paula pelo WhatsApp."
                ),
                "link": "https://wa.me/554899449961",
                "proxima_etapa": "fim"
            })

        if resposta == "2":
            return jsonify({
                "mensagem": (
                    "A mentoria para mães está em fase de desenvolvimento 🌱\n\n"
                    "Você pode falar com a Paula agora ou pedir para ser avisada quando abrir."
                ),
                "link": "https://wa.me/554899449961",
                "proxima_etapa": "fim"
            })

        if resposta == "3":
            return jsonify({
                "mensagem": (
                    "O devocional/livro está em preparação 📖\n\n"
                    "Você pode receber novidades diretamente com a Paula."
                ),
                "link": "https://wa.me/554899449961",
                "proxima_etapa": "fim"
            })

        if resposta == "4":
            return jsonify({
                "mensagem": (
                    "O agendamento é feito de forma personalizada.\n\n"
                    "Vamos alinhar horários pelo WhatsApp?"
                ),
                "link": "https://wa.me/554899449961",
                "proxima_etapa": "fim"
            })

        return jsonify({
            "mensagem": "Não entendi 😕 Por favor, responda com 1, 2, 3 ou 4.",
            "proxima_etapa": "menu"
        })


# =========================
# START (LOCAL / RENDER)
# =========================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
