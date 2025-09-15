[[0.‎‎‎‎‎‎​ Método 360]]
[[0.‎‎‎‎‎‎​ Ritmo Circadiano e Cronobiologia]]

### Rastreador de hábitos
```dataviewjs
const META = 10;
const PASTA = "1.‎‎‎‎‎‎ ​Daily Notes";
const MES = 9; // Setembro (1 = Janeiro, 12 = Dezembro)

const pages = dv.pages(`"${PASTA}"`)
    .where(p => p.file && p.file.name && p.date && dv.date(p.date).month === MES)
    .sort(p => p.date, 'desc');

dv.table(
    ["Data", "Arquivo", "Aulas", "Status"],
    pages.map(p => {
        const data = p.date ? dv.date(p.date).toFormat("dd-MM-yyyy") : "Sem data";
        const aulas = p.aulas || 0;
        let status;

        if (aulas > META) {
            status = `🔥 ${aulas - META} a mais`;
        } else if (aulas < META) {
            status = `⚠️ ${META - aulas} faltando`;
        } else {
            status = "✅ Meta atingida";
        }

        return [
            data,
            dv.fileLink(p.file.path), // <-- link interno do Obsidian
            aulas,
            status
        ];
    })
);


```

## 🚦 Sistema de Revisão Farol Para questões

```dataviewjs
// Config
const pages = dv.pages('"2.‎‎‎‎‎‎​ TJ Concurso/4.‎‎‎‎‎‎​ Questões"')
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
