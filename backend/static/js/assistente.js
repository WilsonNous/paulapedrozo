let etapaAtual = "inicio";

const botao = document.getElementById("assistente-botao");
const janela = document.getElementById("assistente-janela");
const fechar = document.getElementById("assistente-fechar");
const mensagens = document.getElementById("assistente-mensagens");
const input = document.getElementById("assistente-input");

botao.onclick = () => {
    janela.classList.remove("assistente-fechado");
    iniciarAssistente();
};

fechar.onclick = () => {
    janela.classList.add("assistente-fechado");
};

function adicionarMensagem(texto) {
    const div = document.createElement("div");
    div.style.marginBottom = "8px";
    div.innerText = texto;
    mensagens.appendChild(div);
    mensagens.scrollTop = mensagens.scrollHeight;
}

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
        adicionarMensagem(data.mensagem);
        etapaAtual = data.proxima_etapa;
    });
}

input.addEventListener("keypress", function(e) {
    if (e.key === "Enter") {
        const texto = input.value.trim();
        if (!texto) return;

        input.value = "";
        adicionarMensagem(texto);

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
            adicionarMensagem(data.mensagem);

            if (data.link) {
                window.open(data.link, "_blank");
            }

            etapaAtual = data.proxima_etapa;
        });
    }
});
