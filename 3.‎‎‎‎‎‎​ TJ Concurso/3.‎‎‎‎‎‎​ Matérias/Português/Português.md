### **básico**
- [[aula 1 Morfologia - classes gramaticas]]


```dataviewjs
// Config
const materiaFiltro = "Português"; // <<< coloque aqui a matéria desejada

const pages = dv.pages('"3.‎‎‎‎‎‎​ TJ Concurso/4.‎‎‎‎‎‎​ Questões"')
  .where(p => p.materia == materiaFiltro && p.nivel && p.ultima_revisao && p.proxima_revisao)
  .map(p => {
    const proxima = moment(p.proxima_revisao, "DD/MM/YYYY");
    return {
      ...p,
      proxima_moment: proxima,
      diff: proxima.startOf("day").diff(moment().startOf("day"), "days")
    };
  })
  .sort(p => p.diff, "asc"); // Ordena pela diferença de dias

const rows = pages.map(p => {
  const diffDays = p.diff;
  let status;
  if (diffDays < 0) status = "❌ Atrasado";
  else if (diffDays === 0) status = "⚠️ Hoje";
  else status = "✅ Em dia";

  const nivelLabel =
    p.nivel === "verde" ? "🟢 Verde" :
    p.nivel === "amarelo" ? "🟡 Amarelo" :
    p.nivel === "vermelho" ? "🔴 Vermelho" :
    (p.nivel ?? "");

  return [
    p.materia ?? "—",                  
    dv.fileLink(p.file.path),          
    nivelLabel,                        
    p.ultima_revisao ?? "",            
    p.proxima_moment.format("DD/MM/YYYY"),
    Math.abs(diffDays) + (diffDays < 0 ? " dias atrás" : " dias"),
    status                             
  ];
});

dv.table(
  ["📘 Matéria", "🗂 Nota", "⚡ Nível", "📅 Última Revisão", "⏭ Próxima Revisão", "⏳ Status Temporal", "🚦 Status"],
  rows
);

```