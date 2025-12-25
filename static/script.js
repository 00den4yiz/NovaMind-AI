const userInput = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");
const messagesDiv = document.getElementById("messages");

async function sendMessage() {
    const message = userInput.value.trim();
    if (!message) return alert("Lütfen bir mesaj yazın!");
    messagesDiv.innerHTML += `<p class="user"><strong>Sen:</strong> ${message}</p>`;
    userInput.value = "";

    const botMsg = document.createElement("p");
    botMsg.classList.add("ai");
    botMsg.innerHTML = "<strong>NovaMind AI:</strong> Cevap alınıyor...";
    messagesDiv.appendChild(botMsg);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message })
        });
        const data = await response.json();
        botMsg.innerHTML = `<strong>NovaMind AI:</strong> ${data.response}`;
    } catch (err) {
        botMsg.innerHTML = `<strong>NovaMind AI:</strong> Cevap alınamadı`;
        console.error(err);
    }
}

sendBtn.addEventListener("click", sendMessage);
userInput.addEventListener("keypress", e => { if(e.key === "Enter") sendMessage(); });
