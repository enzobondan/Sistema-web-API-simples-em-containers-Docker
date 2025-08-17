async function carregar() {
  const res = await fetch(`${window._env_.API_URL}/get`);
  const dados = await res.json();
  const lista = document.getElementById("lista");
  lista.innerHTML = "";
  dados.forEach(([id, conteudo]) => {
    const li = document.createElement("li");
    li.textContent = `${id}: ${conteudo}`;
    lista.appendChild(li);
  });
}
carregar();
