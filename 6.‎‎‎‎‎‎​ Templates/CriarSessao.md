<%*
/**
 * Template de Sessão de Estudo (Circuito Loop)
 */

try {
    // Arquivo central
    const circuitoFile = app.vault.getAbstractFileByPath("Estudo/CircuitoLoop/CircuitoLoop.md");
    if (!circuitoFile) throw "Arquivo CircuitoLoop.md não encontrado!";

    let content = await app.vault.read(circuitoFile);

    // Lista de matérias
    let materias = content.match(/- (.*)/g)?.map(m => m.replace("- ", "")) || [];
    if (materias.length === 0) throw "Nenhuma matéria encontrada no CircuitoLoop.md";

    // Índice atual
    const idxMatch = content.match(/índiceAtual:: (\d+)/i);
    let idx = idxMatch ? parseInt(idxMatch[1]) : 0;

    // Matéria atual e próxima
    let atual = materias[idx % materias.length];
    let proxima = materias[(idx+1) % materias.length];

    // Atualiza índice
    let novoIdx = (idx + 1) % materias.length;
    let novoContent = content.replace(/índiceAtual:: \d+/i, "índiceAtual:: " + novoIdx);
    await app.vault.modify(circuitoFile, novoContent);

    // Horário aleatório 50-90min
    let duracao = Math.floor(Math.random() * (90-50+1)) + 50;
    let now = new Date();
    let inicio = now.toTimeString().slice(0,5);
    let fim = ""; 
    let pausa = "15min";

    // Pasta da matéria
    let folderPath = "Estudo/CircuitoLoop/Sessões/" + atual;
    let folders = folderPath.split("/");
    let pathAcc = "";
    for (let f of folders) {
        pathAcc += f + "/";
        if (!app.vault.getAbstractFileByPath(pathAcc)) {
            await app.vault.createFolder(pathAcc).catch(()=>{});
        }
    }

    // Nome do arquivo
    let sessionName = "Sessao - " + now.toISOString().slice(0,19).replace("T"," ").replace(/:/g,"-");
    let outputPath = folderPath + "/" + sessionName + ".md";

    // Última aula (preencher manualmente ou automatizar)
    let ultimaAula = "";

    // Conteúdo da sessão
    let registro = `
materia:: ${atual}
inicio:: ${inicio}
fim:: ${fim}
pausa:: ${pausa}

observacoes::
revisaoD1:: false
revisaoD2:: false
revisaoD3:: false

questoes:: 0
`;

    // Criar arquivo
    await app.vault.create(outputPath, registro);
    tR += "✅ Sessão criada: `" + outputPath + "`";

} catch (err) {
    tR += "❌ Erro ao criar sessão: " + err;
}
%>
