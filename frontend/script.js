const backendUrl = "http://127.0.0.1:8000";

async function validateIdea() {
    const idea = document.getElementById("ideaInput").value;
    if (!idea) {
        alert("Please enter an idea.");
        return;
    }

    const response = await fetch(`${backendUrl}/validate-idea/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ idea: idea })
    });

    const data = await response.json();
    document.getElementById("validationResult").textContent = data.validation;
}

async function getAdvice() {
    const response = await fetch(`${backendUrl}/get-startup-advice/`);
    const data = await response.json();

    const adviceList = document.getElementById("adviceList");
    adviceList.innerHTML = "";

    data.advice.forEach(advice => {
        const li = document.createElement("li");
        li.textContent = advice;
        adviceList.appendChild(li);
    });
}

async function fetchIdeas() {
    const response = await fetch(`${backendUrl}/get-ideas/`);
    const data = await response.json();

    const ideasList = document.getElementById("ideasList");
    ideasList.innerHTML = "";

    data.ideas.forEach(idea => {
        const li = document.createElement("li");
        li.textContent = `${idea.id}: ${idea.idea} - ${idea.validation}`;
        ideasList.appendChild(li);
    });
}
