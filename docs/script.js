document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("review-form");
  const codeInput = document.getElementById("code-input");
  const output = document.getElementById("output");

  form.addEventListener("submit", async function (e) {
    e.preventDefault();
    output.innerHTML = "<p>⏳ Generating feedback...</p>";

    const code = codeInput.value;

    try {
      const response = await fetch("https://devmate-ai.onrender.com", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ code: code })
      });

      const feedback = await response.json();

      output.innerHTML = `
        <h3>📝 Summary</h3><p>${feedback.summary || "No summary available."}</p>
        <h3>🐛 Issues</h3><ul>
          ${feedback.issues?.length ? feedback.issues.map(i => `<li>${i}</li>`).join("") : "<li>No issues found.</li>"}
        </ul>
        <h3>💡 Suggestions</h3><ul>
          ${feedback.suggestions?.length ? feedback.suggestions.map(s => `<li>${s}</li>`).join("") : "<li>No suggestions at this time.</li>"}
        </ul>
      `;
    } catch (error) {
      output.innerHTML = `<p>❌ Error fetching feedback. Try again later.</p>`;
      console.error("Review error:", error);
    }
  });
});
