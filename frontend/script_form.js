async function enviar() {
  const msg = document.getElementById("mensagem").value;
  await fetch(`${window._env_.API_URL}/post`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({mensagem: msg})
  });
  alert("Mensagem enviada!");
}
