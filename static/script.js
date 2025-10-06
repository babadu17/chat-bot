async function sendMessage() {
    const input = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");

    const message = input.value.trim();
    if (!message) return;

    // Ajout du message utilisateur
    chatBox.innerHTML += `<div class="user">${message}</div>`;
    input.value = "";

    // Scroll automatique
    chatBox.scrollTop = chatBox.scrollHeight;

    // Envoi au serveur
    const response = await fetch("/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: message })
    });

    const data = await response.json();

    // Réponse du bot
    chatBox.innerHTML += `<div class="bot">${data.reply}</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;
}
