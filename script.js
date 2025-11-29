async function analyze() {
    const commentsInput = document.getElementById("comments").value;
    const loadingDiv = document.getElementById("loading");
    const button = document.querySelector("button");

    // Show loading
    loadingDiv.classList.remove("hidden");
    button.disabled = true;
    button.innerText = "Analyzing...";

    const comments = commentsInput
        .split("\n")
        .map(c => c.trim())
        .filter(c => c.length > 0);

    const response = await fetch("http://127.0.0.1:8000/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ comments }),
    });

    const data = await response.json();

    const container = document.getElementById("results");
    container.innerHTML = ""; // Clear old results

    // Per-comment cards
    data.sentiments.forEach((sentiment, i) => {
        container.innerHTML += `
            <div class="p-3 mb-3 border rounded-lg bg-gray-50">
                <p><strong>Comment ${i + 1}</strong></p>
                <p><strong>Sentiment:</strong> ${sentiment}</p>
                <p><strong>Emotion:</strong> ${data.emotions[i]}</p>
            </div>
        `;
    });

    // Combined summary
    container.innerHTML += `
        <div class="mt-6 p-4 bg-blue-50 border border-blue-200 rounded-lg">
            <h3 class="font-semibold text-blue-800 mb-1">Summary of All Comments</h3>
            <p class="text-sm text-blue-700">${data.combined_summary}</p>
        </div>
    `;

    // Hide loading & restore button
    loadingDiv.classList.add("hidden");
    button.disabled = false;
    button.innerText = "Analyze";
}
