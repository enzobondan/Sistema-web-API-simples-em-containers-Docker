document
  .getElementById("formProjeto")
  .addEventListener("submit", async function (e) {
    e.preventDefault();

    try {
      const projeto = {
        title: document.getElementById("title").value,
        description: document.getElementById("description").value,
        category: document.getElementById("category").value,
        budget: parseFloat(
          document
            .getElementById("budget")
            .value.replace(".", "")
            .replace(",", ".")
        ),
        team_size: parseInt(document.getElementById("team_size").value),
        deadline: document.getElementById("deadline").value,
      };

      const response = await fetch(`${window._env_.API_URL}/post`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(projeto),
      });

      if (!response.ok) {
        throw new Error("Erro ao cadastrar projeto");
      }

      const statusDiv = document.getElementById("statusMessage");
      statusDiv.textContent = "Projeto cadastrado com sucesso!";
      statusDiv.className = "status-message success";

      document.getElementById("formProjeto").reset();

      setTimeout(() => {
        statusDiv.className = "status-message";
      }, 5000);
    } catch (error) {
      const statusDiv = document.getElementById("statusMessage");
      statusDiv.textContent = "Erro ao cadastrar projeto: " + error.message;
      statusDiv.className = "status-message error";

      console.error("Erro:", error);
    }
  });
