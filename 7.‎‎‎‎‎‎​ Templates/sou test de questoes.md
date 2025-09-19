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

# 📝 Questões - <% tp.date.now("DD/MM/YYYY") %>

## 1️⃣ Pergunta
> Escreva aqui a pergunta de forma clara e objetiva.

**Alternativas (marque apenas uma):**  
- [ ] Alternativa A  
- [ ] Alternativa B  
- [ ] Alternativa C  
- [ ] Alternativa D  

**Resposta correta::**  
<!-- Use o formato Spaced Repetition: "Resposta:: Texto" -->

**Explicação:**  
<!-- Pequena explicação do porquê da resposta correta -->

**Dicas / Observações:**  
<!-- Qualquer lembrete importante ou detalhe que ajude a memorizar -->

---

## 2️⃣ Pergunta
> Escreva a próxima pergunta aqui

- [ ] Alternativa A  
- [ ] Alternativa B  
- [ ] Alternativa C  
- [ ] Alternativa D  

**Resposta correta::**  

**Explicação:**  

**Dicas / Observações:**  

---

## 🔖 Tags e revisão
- #questoes  
- #revisao  
- #<% tp.user.materia %>
``