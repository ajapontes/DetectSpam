document.addEventListener("DOMContentLoaded", () => {
    const messageInput = document.getElementById("messageInput");
    const analyzeButton = document.getElementById("analyzeButton");
    const clearButton = document.getElementById("clearButton");
    const resultCard = document.getElementById("resultCard");
    const predictionText = document.getElementById("predictionText");
    const confidenceText = document.getElementById("confidenceText");
    const messageText = document.getElementById("messageText");
    const explanationText = document.getElementById("explanationText");
    const errorMessage = document.getElementById("errorMessage");

    analyzeButton.addEventListener("click", async () => {
        const text = messageInput.value.trim();

        if (!text) {
            alert("Por favor escribe un mensaje para analizar.");
            return;
        }

        analyzeButton.disabled = true;
        analyzeButton.textContent = "Analizando...";
        errorMessage.classList.add("hidden");
        errorMessage.textContent = "";

        try {
            const response = await fetch("/predict", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ text }),
            });

            if (!response.ok) {
                throw new Error("Error al analizar el mensaje.");
            }

            const data = await response.json();
            const confidencePercentage = (data.confidence * 100).toFixed(2);

            resultCard.classList.remove("hidden", "spam", "ham");

            if (data.prediction === "spam") {
                resultCard.classList.add("spam");
                predictionText.textContent = "Resultado: SPAM";
            } else {
                resultCard.classList.add("ham");
                predictionText.textContent = "Resultado: NO SPAM";
            }

            confidenceText.textContent = `Confianza: ${confidencePercentage}%`;
            messageText.textContent = `Mensaje analizado: ${data.message}`;
            explanationText.textContent = `Explicación: ${data.explanation}`;

        } catch (error) {
            errorMessage.textContent = error.message;
            errorMessage.classList.remove("hidden");
        } finally {
            analyzeButton.disabled = false;
            analyzeButton.textContent = "Analizar mensaje";
        }
    });

clearButton.addEventListener("click", () => {
    messageInput.value = "";
    resultCard.classList.add("hidden");
    resultCard.classList.remove("spam", "ham");
    predictionText.textContent = "";
    confidenceText.textContent = "";
    messageText.textContent = "";
    explanationText.textContent = "";
    errorMessage.classList.add("hidden");
    errorMessage.textContent = "";
});
});