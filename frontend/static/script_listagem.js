async function carregarProjetos() {
  console.log(`chamando na rota: ${window._env_.API_URL}/api/projects`);
  const res = await fetch(`${window._env_.API_URL}/api/projects`);
  const dados = await res.json();

  console.log("Dados recebidos:", dados);

  const tbody = document.querySelector("#tabelaProjetos tbody");
  tbody.innerHTML = "";

  dados.forEach((projeto) => {
    const tr = document.createElement("tr");

    tr.innerHTML = `
      <td>${projeto.id}</td>
      <td>${projeto.title}</td>
      <td>${projeto.description}</td>
      <td>${projeto.category}</td>
      <td>R$ ${projeto.budget.toFixed(2)}</td>
      <td>${projeto.team_size}</td>
      <td>${new Date(projeto.deadline).toLocaleDateString()}</td>
      <td>${new Date(projeto.created_at).toLocaleString()}</td>
    `;

    tbody.appendChild(tr);
  });
}

carregarProjetos();
