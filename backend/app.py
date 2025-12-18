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
    resposta = (data.get("resposta") or "").strip().lower()

    print("🤖 Assistente | Etapa:", etapa, "| Resposta:", resposta)

    # ===== INÍCIO =====
    if etapa == "inicio":
        return jsonify({
            "mensagem": (
                "Olá! 😊\n\n"
                "Sou o assistente virtual da Paula Pedrozo.\n"
                "Estou aqui para te orientar com carinho.\n\n"
                "Como posso te ajudar hoje?\n\n"
                "1️⃣ Atendimento terapêutico\n"
                "2️⃣ Mentoria para mães\n"
                "3️⃣ Devocional / Livro\n"
                "4️⃣ Agendamento\n\n"
                "Digite o número da opção desejada."
            ),
            "proxima_etapa": "menu"
        })

    # ===== MENU =====
    if etapa == "menu":

        if resposta == "1":
            return jsonify({
                "mensagem": (
                    "O atendimento terapêutico é realizado de forma online, "
                    "por chamada de vídeo, em dia e horário previamente agendados.\n\n"
                    "Cada sessão dura em média 50 minutos e acontece em um espaço de "
                    "escuta, acolhimento e sigilo 🤍\n\n"
                    "Você gostaria de falar com a Paula pelo WhatsApp agora?"
                    "\n\nResponda: Sim ou Não."
                ),
                "proxima_etapa": "confirmar_whatsapp"
            })

        if resposta == "2":
            return jsonify({
                "mensagem": (
                    "A mentoria para mães é um projeto prioritário 🌷\n\n"
                    "Ela foi pensada para apoiar mulheres em sua jornada emocional, "
                    "familiar e espiritual, com encontros e conteúdos especiais.\n\n"
                    "Você gostaria de falar com a Paula pelo WhatsApp para saber mais?"
                    "\n\nResponda: Sim ou Não."
                ),
                "proxima_etapa": "confirmar_whatsapp"
            })

        if resposta == "3":
            return jsonify({
                "mensagem": (
                    "O devocional / livro está em fase de preparação 📖\n\n"
                    "Será um conteúdo de reflexão, fortalecimento emocional e espiritual.\n\n"
                    "Você gostaria de falar com a Paula pelo WhatsApp para receber novidades?"
                    "\n\nResponda: Sim ou Não."
                ),
                "proxima_etapa": "confirmar_whatsapp"
            })

        if resposta == "4":
            return jsonify({
                "mensagem": (
                    "O agendamento é feito de forma personalizada 🗓️\n\n"
                    "Assim conseguimos respeitar o seu tempo e a disponibilidade da Paula.\n\n"
                    "Você gostaria de alinhar isso pelo WhatsApp?"
                    "\n\nResponda: Sim ou Não."
                ),
                "proxima_etapa": "confirmar_whatsapp"
            })

        return jsonify({
            "mensagem": (
                "Não consegui entender 😕\n\n"
                "Por favor, responda com:\n"
                "1, 2, 3 ou 4."
            ),
            "proxima_etapa": "menu"
        })

    # ===== CONFIRMAÇÃO WHATSAPP =====
    if etapa == "confirmar_whatsapp":

        if resposta in ["sim", "s", "ok", "claro"]:
            return jsonify({
                "mensagem": (
                    "Perfeito 😊\n\n"
                    "Vou te direcionar agora."
                ),
                "link": "https://wa.me/554899449961",
                "proxima_etapa": "fim"
            })

        if resposta in ["não", "nao", "n"]:
            return jsonify({
                "mensagem": (
                    "Tudo bem 🤍\n\n"
                    "Se precisar, estarei por aqui para te ajudar."
                ),
                "proxima_etapa": "fim"
            })

        return jsonify({
            "mensagem": (
                "Pode me responder com **Sim** ou **Não**, por favor 😊"
            ),
            "proxima_etapa": "confirmar_whatsapp"
        })


# =========================
# START (LOCAL / RENDER)
# =========================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
