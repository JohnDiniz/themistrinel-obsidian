```dataviewjs
// Matéria atual
const file = app.vault.getAbstractFileByPath("1.‎‎‎‎‎‎​ Estudo/CircuitoLoop/CircuitoLoop.md");
let materiaAtual = "Não definido";

if (file) {
    const content = await app.vault.read(file);
    const materias = content.match(/- (.*)/g)?.map(m => m.replace("- ","")) || [];
    const idxMatch = content.match(/índiceAtual:: (\d+)/i);
    const idxAtual = idxMatch ? parseInt(idxMatch[1]) : 0;
    materiaAtual = materias[idxAtual] || "Não definido";
}

// Função para converter título "Sessao-YYYY-MM-DD" em Date
function parseTitleDate(title) {
    const match = title.match(/(\d{4})-(\d{2})-(\d{2})/);
    if (match) {
        const [_, year, month, day] = match.map(Number);
        return new Date(year, month - 1, day);
    }
    return new Date(0);
}

// Ler sessões
const sessions = dv.pages('"1.‎‎‎‎‎‎​ Estudo/CircuitoLoop/Sessões"').where(p => p.file.path.endsWith(".md"));
let grouped = {};

// Agrupar por matéria
sessions.forEach(s => {
    const materia = s.materia?.path 
        ? s.materia.path.replace(".md","").split("/").pop() 
        : (s.materia?.toString() ?? "Sem matéria");

    if (!grouped[materia]) grouped[materia] = [];

    const status = s.fim && s.fim.trim() !== "" ? "✅ Concluída" : "⏳ Em andamento";
    const d1 = s.revisaoD1 ? "✅" : "❌";
    const d2 = s.revisaoD2 ? "✅" : "❌";
    const d3 = s.revisaoD3 ? "✅" : "❌";

    // Extrair data do título do arquivo
    const inicioDate = parseTitleDate(s.file.name);

    grouped[materia].push({
        sessao: s.file.link,
        status,
        inicio: s.inicio ?? "-",
        inicioDate: inicioDate, // Guardar objeto Date para ordenação
        fim: s.fim ?? "-",
        observacoes: Array.isArray(s.observacoes) ? s.observacoes.join("\n") : (s.observacoes ?? "-"),
        D1: d1,
        D2: d2,
        D3: d3,
        questoes: s.questoes ?? 0
    });
});

// Ordenar sessões por data do título (mais recente primeiro)
for (let materia in grouped) {
    grouped[materia].sort((a, b) => b.inicioDate - a.inicioDate);
}

// Verificar se há alguma sessão em andamento → essa vira a matéria atual
for (let materia in grouped) {
    if (grouped[materia].some(x => x.status === "⏳ Em andamento")) {
        materiaAtual = materia;
        break;
    }
}

dv.header(2, `🟢 Matéria atual: **${materiaAtual}**`);

// Ordenar matérias → atual sempre no topo
const materiasOrdenadas = Object.keys(grouped).sort((a, b) => {
    if (a === materiaAtual) return -1;
    if (b === materiaAtual) return 1;
    return a.localeCompare(b);
});

// Mostrar tabela
for (let materia of materiasOrdenadas) {
    dv.header(3, materia === materiaAtual ? `${materia} (ATUAL)` : materia);

    dv.table(
        ["Sessão", "Status", "Início", "Fim", "Obs", "D1", "D2", "D3", "Questões"],
        grouped[materia].map(x => [
            x.sessao, 
            x.status, 
            x.inicio, 
            x.fim, 
            x.observacoes, 
            x.D1, 
            x.D2, 
            x.D3, 
            x.questoes
        ])
    );
}

```

