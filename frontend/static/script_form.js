document
  .getElementById("formProjeto")
  .addEventListener("submit", async function (e) {
    e.preventDefault();

    const projeto = {
      title: document.getElementById("title").value,
      description: document.getElementById("description").value,
      category: document.getElementById("category").value,
      budget: parseFloat(document.getElementById("budget").value),
      team_size: parseInt(document.getElementById("team_size").value),
      deadline: document.getElementById("deadline").value,
    };

    await fetch(`${window._env_.API_URL}/post`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(projeto),
    });

    alert("Projeto cadastrado com sucesso!");
    document.getElementById("formProjeto").reset();
  });
