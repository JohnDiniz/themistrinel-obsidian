```dataviewjs
// Matéria atual
const file = app.vault.getAbstractFileByPath("Estudo/CircuitoLoop/CircuitoLoop.md");
let materiaAtual = "Não definido";

if (file) {
    const content = await app.vault.read(file);
    const materias = content.match(/- (.*)/g)?.map(m => m.replace("- ","")) || [];
    const idxMatch = content.match(/índiceAtual:: (\d+)/i);
    const idxAtual = idxMatch ? parseInt(idxMatch[1]) : 0;
    materiaAtual = materias[idxAtual] || "Não definido";
}
dv.header(2, `🟢 Matéria atual a ser iniciada: **${materiaAtual}**`);

// Ler sessões
const sessions = dv.pages('"Estudo/CircuitoLoop/Sessões"').where(p => p.file.path.endsWith(".md"));
let grouped = {};

// Agrupar por matéria
sessions.forEach(s => {
    const materia = s.materia || "Sem matéria";

    if (!grouped[materia]) grouped[materia] = [];

    // Status e revisões
    const status = s.fim && s.fim.trim() !== "" ? "✅ Concluída" : "⏳ Em andamento";
    const d1 = s.revisaoD1 ? "✅" : "❌";
    const d2 = s.revisaoD2 ? "✅" : "❌";
    const d3 = s.revisaoD3 ? "✅" : "❌";
    

    grouped[materia].push({
    sessao: s.file.link,
    status,
    inicio: s.inicio ?? "-",
    fim: s.fim ?? "-",
    observacoes: Array.isArray(s.observacoes) ? s.observacoes.join("\n") : (s.observacoes ?? "-"),
    D1: d1,
    D2: d2,
    D3: d3,
    questoes: s.questoes ?? 0
});

});

// Mostrar tabela
for (let materia in grouped) {
    dv.header(3, materia === materiaAtual ? `${materia} (ATUAL)` : materia);

    dv.table(
        ["Sessão", "Status", "Início", "Fim", "Obs", "D1", "D2", "D3", "Questões"],
        grouped[materia].map(x => [
            x.sessao, x.status, x.inicio, x.fim, x.observacoes, x.D1, x.D2, x.D3, x.questoes
        ])
    );
}

