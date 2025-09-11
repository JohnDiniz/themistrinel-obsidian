---
materia: <% tp.system.suggester(["Português","Matemática","Direito Constitucional","Direito Penal","Raciocínio Lógico"], ["Português","Matemática","Direito Constitucional","Direito Penal","Raciocínio Lógico"]) %>
nivel: <% tp.system.suggester(["🟢 Verde","🟡 Amarelo","🔴 Vermelho"], ["verde","amarelo","vermelho"]) %>
ultima_revisao: <% tp.date.now("YYYY-MM-DD") %>
proxima_revisao: <%* 
  let nivel = await tp.system.suggester(["Verde","Amarelo","Vermelho"], ["verde","amarelo","vermelho"]);
  let today = moment();
  if (nivel == "verde") { tR += today.add(30, 'days').format("YYYY-MM-DD") }
  if (nivel == "amarelo") { tR += today.add(12, 'days').format("YYYY-MM-DD") } // média 10-15
  if (nivel == "vermelho") { tR += today.add(7, 'days').format("YYYY-MM-DD") }
%>
---

# 🚦 Revisão Farol

- **Tópico:**  
- **Questão/Resumo:**  

## 🔁 Revisão
- Última revisão: `=this.ultima_revisao`
- Próxima revisão: `=this.proxima_revisao`

> ✍️ Observações:  
>
