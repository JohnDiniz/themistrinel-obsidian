[[Método 360]]
[[Ritmo Circadiano e Cronobiologia]]

## 🚦 Sistema de Revisão Farol Para questoes

```dataviewjs
// Config
const pages = dv.pages('"0 TJ Concurso/2 Questões"')
  .where(p => p.materia && p.nivel && p.ultima_revisao && p.proxima_revisao)
  .map(p => {
    const proxima = moment(p.proxima_revisao, "DD/MM/YYYY");
    return {
      ...p,
      proxima_moment: proxima,
      diff: proxima.startOf("day").diff(moment().startOf("day"), "days")
    };
  })
  .sort(p => p.diff, "asc"); // Ordena pela diferença de dias (asc = menores primeiro)

// Constante
const hoje = moment().startOf("day");

const rows = pages.map(p => {
  if (!p.proxima_moment.isValid()) {
    return [
      dv.fileLink(p.file.path),
      p.nivel ?? "",
      p.ultima_revisao ?? "",
      p.proxima_revisao ?? "",
      "—",
      "⚠️ Data inválida"
    ];
  }

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
    dv.fileLink(p.file.path),
    nivelLabel,
    p.ultima_revisao ?? "",
    p.proxima_moment.format("DD/MM/YYYY"),
    Math.abs(diffDays) + (diffDays < 0 ? " dias atrás" : " dias"),
    status
  ];
});

dv.table(
  ["📘 Matéria", "⚡ Nível", "📅 Última Revisão", "⏭ Próxima Revisão", "⏳ Status Temporal", "🚦 Status"],
  rows
);
```


