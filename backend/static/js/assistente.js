let etapaAtual = null;
let assistenteIniciado = false;

const botao = document.getElementById("assistente-botao");
const janela = document.getElementById("assistente-janela");
const fechar = document.getElementById("assistente-fechar");
const mensagens = document.getElementById("assistente-mensagens");
const input = document.getElementById("assistente-input");

// =========================
// ABRIR ASSISTENTE
// =========================
botao.onclick = () => {
    janela.classList.remove("assistente-fechado");

    if (!assistenteIniciado) {
        iniciarAssistente();
        assistenteIniciado = true;
    }
};

// =========================
// FECHAR ASSISTENTE
// =========================
fechar.onclick = () => {
    janela.classList.add("assistente-fechado");
};

// =========================
// ADICIONAR MENSAGEM
// =========================
function adicionarMensagem(texto, tipo = "bot") {
    const div = document.createElement("div");
    div.className = tipo === "user" ? "mensagem-user" : "mensagem-bot";
    div.innerText = texto;
    mensagens.appendChild(div);
    mensagens.scrollTop = mensagens.scrollHeight;
}

// =========================
// DIGITANDO...
// =========================
function mostrarDigitando() {
    const div = document.createElement("div");
    div.id = "digitando";
    div.className = "mensagem-bot mensagem-digitando";
    div.innerText = "Digitando...";
    mensagens.appendChild(div);
    mensagens.scrollTop = mensagens.scrollHeight;
}

function removerDigitando() {
    const el = document.getElementById("digitando");
    if (el) el.remove();
}

// =========================
// INICIAR ASSISTENTE
// =========================
function iniciarAssistente() {
    mensagens.innerHTML = "";
    etapaAtual = "inicio";

    fetch("/assistente", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ etapa: "inicio" })
    })
    .then(res => res.json())
    .then(data => {
        adicionarMensagem(data.mensagem, "bot");
        etapaAtual = data.proxima_etapa;
    });
}

// =========================
// INPUT DO USUÁRIO
// =========================
input.addEventListener("keypress", function(e) {
    if (e.key === "Enter") {
        const texto = input.value.trim();
        if (!texto) return;

        input.value = "";
        adicionarMensagem(texto, "user");

        mostrarDigitando();

        setTimeout(() => {
            fetch("/assistente", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    etapa: etapaAtual,
                    resposta: texto
                })
            })
            .then(res => res.json())
            .then(data => {
                removerDigitando();
                adicionarMensagem(data.mensagem, "bot");

                if (data.link) {
                    window.open(data.link, "_blank");
                }

                etapaAtual = data.proxima_etapa;
            });
        }, 600);
    }
});
