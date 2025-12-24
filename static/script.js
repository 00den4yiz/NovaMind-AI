document.addEventListener("DOMContentLoaded", () => {
    const sendBtn = document.getElementById('send-btn');
    const userInput = document.getElementById('user-input');
    const messages = document.getElementById('messages');

    sendBtn.addEventListener('click', async () => {
        const text = userInput.value.trim();
        if(!text) {
            alert("Lütfen bir mesaj yazın!");
            return;
        }

        // Kullanıcı mesajı
        const userMsg = document.createElement('p');
        userMsg.classList.add("user");
        userMsg.innerHTML = `<strong>Sen:</strong> ${text}`;
        messages.appendChild(userMsg);
        userInput.value = "";

        // AI mesajı (bekleme)
        const aiMsg = document.createElement('p');
        aiMsg.classList.add("ai");
        aiMsg.innerHTML = `<strong>NovaMind AI:</strong> Cevap alınıyor...`;
        messages.appendChild(aiMsg);

        messages.scrollTop = messages.scrollHeight;

        try {
            const response = await fetch("http://localhost:3000/chat", {
                method:"POST",
                headers:{"Content-Type":"application/json"},
                body:JSON.stringify({message:text})
            });
            const data = await response.json();
            aiMsg.innerHTML = `<strong>NovaMind AI:</strong> ${data.response}`;
        } catch(err) {
            aiMsg.innerHTML = `<strong>NovaMind AI:</strong> Hata oluştu.`;
            console.error(err);
        }
    });

    userInput.addEventListener("keypress", e => {
        if(e.key === "Enter") sendBtn.click();
    });
});
