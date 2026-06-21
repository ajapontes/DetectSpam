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

    const accuracyValue = document.getElementById("accuracyValue");
    const precisionValue = document.getElementById("precisionValue");
    const recallValue = document.getElementById("recallValue");
    const f1Value = document.getElementById("f1Value");
    const modelName = document.getElementById("modelName");
    const metricsGeneratedAt = document.getElementById("metricsGeneratedAt");

    function formatPercentage(value) {
        return `${(value * 100).toFixed(2)}%`;
    }

    async function loadMetrics() {
        try {
            const response = await fetch("/metrics");

            if (!response.ok) {
                throw new Error("Could not load model metrics.");
            }

            const data = await response.json();

            if (data.status === "not_available") {
                modelName.textContent = data.message;
                return;
            }

            accuracyValue.textContent = formatPercentage(data.metrics.accuracy);
            precisionValue.textContent = formatPercentage(data.metrics.precision);
            recallValue.textContent = formatPercentage(data.metrics.recall);
            f1Value.textContent = formatPercentage(data.metrics.f1_score);

            modelName.textContent = `Model: ${data.model}`;
            metricsGeneratedAt.textContent = `Generated at: ${data.generated_at}`;
        } catch (error) {
            modelName.textContent = error.message;
        }
    }

    analyzeButton.addEventListener("click", async () => {
        const text = messageInput.value.trim();

        if (!text) {
            errorMessage.textContent = "Please enter a message to analyze.";
            errorMessage.classList.remove("hidden");
            return;
        }

        errorMessage.classList.add("hidden");
        errorMessage.textContent = "";

        analyzeButton.disabled = true;
        analyzeButton.textContent = "Analyzing...";

        try {
            const response = await fetch("/predict", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ text }),
            });

            if (!response.ok) {
                throw new Error("Error analyzing the message.");
            }

            const data = await response.json();
            const confidencePercentage = formatPercentage(data.confidence);

            resultCard.classList.remove("hidden", "spam", "ham");

            if (data.prediction === "spam") {
                resultCard.classList.add("spam");
                predictionText.textContent = "Result: SPAM";
            } else {
                resultCard.classList.add("ham");
                predictionText.textContent = "Result: HAM";
            }

            confidenceText.textContent = `Confidence: ${confidencePercentage}`;
            messageText.textContent = `Analyzed message: ${data.message}`;
            explanationText.textContent = `Explanation: ${data.explanation}`;
        } catch (error) {
            errorMessage.textContent = error.message;
            errorMessage.classList.remove("hidden");
        } finally {
            analyzeButton.disabled = false;
            analyzeButton.textContent = "Analyze message";
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

    loadMetrics();
});