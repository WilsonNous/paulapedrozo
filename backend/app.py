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

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

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
# FORMULÁRIO
# =========================
@app.route("/contato", methods=["POST"])
def contato_submit():
    print("📩 Novo contato recebido em", datetime.now())
    return redirect(url_for("home"))

# =========================
# ASSISTENTE YARDEN
# =========================
@app.route("/assistente", methods=["POST"])
def assistente():
    data = request.get_json() or {}
    etapa = data.get("etapa")
    resposta = (data.get("resposta") or "").strip().lower()

    if etapa == "inicio":
        return jsonify({
            "mensagem": (
                "Olá, eu sou a Yarden 🌿\n\n"
                "Meu nome carrega o significado de rio e jardim — "
                "um lugar de renovo.\n\n"
                "Como posso te ajudar hoje?\n\n"
                "1️⃣ Atendimento terapêutico\n"
                "2️⃣ Mentoria para mães\n"
                "3️⃣ Devocional / Livro\n"
                "4️⃣ Agendamento\n"
                "5️⃣ Sobre a Paula"
            ),
            "proxima_etapa": "menu"
        })

    if etapa == "menu":
        if resposta == "5":
            return jsonify({
                "mensagem": (
                    "A Paula Pedrozo é terapeuta clínica, mãe de dois filhos e "
                    "chamada para cuidar de vidas com amor, fé e propósito 🤍\n\n"
                    "Deseja conhecer mais sobre a história dela?"
                    "\n\nResponda: Sim ou Não."
                ),
                "proxima_etapa": "confirmar_sobre"
            })

        if resposta in ["1", "2", "3", "4"]:
            return jsonify({
                "mensagem": (
                    "Posso te ajudar melhor conversando diretamente com a Paula 😊\n\n"
                    "Você gostaria de ir para o WhatsApp agora?"
                    "\n\nResponda: Sim ou Não."
                ),
                "proxima_etapa": "confirmar_whatsapp"
            })

        return jsonify({
            "mensagem": "Responda com 1, 2, 3, 4 ou 5 😊",
            "proxima_etapa": "menu"
        })

    if etapa == "confirmar_whatsapp":
        if resposta in ["sim", "s", "ok", "claro"]:
            return jsonify({
                "mensagem": "Perfeito 🤍",
                "link": "https://wa.me/554899449961",
                "proxima_etapa": "fim"
            })
        return jsonify({
            "mensagem": "Tudo bem, estarei aqui se precisar 🌷",
            "proxima_etapa": "fim"
        })

    if etapa == "confirmar_sobre":
        if resposta in ["sim", "s", "ok"]:
            return jsonify({
                "mensagem": "Te levo agora 😊",
                "link": "/sobre",
                "proxima_etapa": "fim"
            })
        return jsonify({
            "mensagem": "Sem problema 🤍",
            "proxima_etapa": "menu"
        })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
