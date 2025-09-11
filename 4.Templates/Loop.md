---
materia: <% tp.system.suggester(
  ["Português","Matemática","Direito Constitucional","Direito Penal","Raciocínio Lógico"],
  ["Português","Matemática","Direito Constitucional","Direito Penal","Raciocínio Lógico"]) %>
<%* 
  let nivel = await tp.system.suggester(
    ["🟢 Verde (Fácil)", "🟡 Amarelo (Médio)", "🔴 Vermelho (Difícil)"],
    ["verde","amarelo","vermelho"]
  );
  tR += "nivel: " + nivel + "\n";

  // Última revisão hoje
  tR += "ultima_revisao: " + tp.date.now("DD/MM/YYYY") + "\n";

  // Próxima revisão de acordo com nível
  let today = moment();
  if (nivel == "verde") { tR += "proxima_revisao: " + today.add(30, 'days').format("DD/MM/YYYY") + "\n"; }
  if (nivel == "amarelo") { tR += "proxima_revisao: " + today.add(12, 'days').format("DD/MM/YYYY") + "\n"; }
  if (nivel == "vermelho") { tR += "proxima_revisao: " + today.add(7, 'days').format("DD/MM/YYYY") + "\n"; }
%>
---

# 🚦 Revisão Farol

- **Tópico:**  
- **Questão/Resumo:**  

## 📝 Histórico Manual
- **Data:** `=this.ultima_revisao`  
  **Nível:** 🟢/🟡/🔴  
  **Observação:** Mantido/Alterado para X  

- **Data:** DD/MM/YYYY  
  **Nível:** 🟢/🟡/🔴  
  **Observação:** Mantido/Alterado para X  

> ✍️ Observações:  
>
