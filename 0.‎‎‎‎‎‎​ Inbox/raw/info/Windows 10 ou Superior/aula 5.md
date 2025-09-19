# 🗑️ **Lixeira do Windows**

#questões 

## **Definição**

* Pasta especial do sistema que armazena **arquivos e pastas excluídos**.
* Permite:

  * ✅ Restaurar arquivos para o local original ou outro local
  * ❌ Excluir definitivamente

---

Perfeito! Vou detalhar melhor o ponto da **capacidade da Lixeira** e o que acontece quando um arquivo é maior ou exatamente do tamanho disponível:

---

## **❌ O que não vai para a Lixeira**

1. Arquivos/pastas em unidades **removíveis** (pen drives, cartões de memória)
2. Arquivos/pastas **em rede**
3. Arquivos **maiores que a capacidade disponível da Lixeira**

   * A Lixeira tem um **espaço limitado** por unidade (normalmente definido nas propriedades da Lixeira).
   * Se o arquivo for **maior que o espaço livre** da Lixeira:

     * Ele **não será movido para a Lixeira**, será **apagado definitivamente**.
   * Se o arquivo for **exatamente do tamanho da Lixeira**:

     * O Windows **libera espaço automaticamente** apagando permanentemente os arquivos mais antigos da Lixeira para acomodar o novo arquivo.
4. Arquivos/pastas excluídos usando **SHIFT + DEL**

> ⚠️ Observação: Arquivos excluídos de **HD externo** podem ser movidos para a Lixeira, pois ele **não é considerado um disco removível**.

---

## **📂 Como excluir arquivos ou pastas**

* Selecionando o arquivo/pasta:

  * Tecla **Delete (DEL)**
  * Botão direito → **Excluir**
  * Arrastando o objeto para a Lixeira (Área de Trabalho ou Explorador de Arquivos)

* Conteúdo da Lixeira pode ser:

  * Restaurado para o **local de origem**
  * Movido para **outro local**

---

## **❓ Questões de Exemplo**

### **03. CESPE / CEBRASPE**

> O termo lixeira é usado para denominar o conteúdo de um computador que se torna defasado em função de lançamentos de programas novos ou complementares que não são incorporados ao sistema operacional já existente.

* ( ) Certo
* (✅) Errado

> **Explicação:** Lixeira é o local de armazenamento temporário de arquivos apagados, não tem relação com programas defasados.

---

### **04. CESPE**

> No ambiente Windows, um arquivo, ao ser deletado, é enviado para a Lixeira, de onde poderá ser recuperado por meio da opção Restaurar.

* (✅) Certo
* ( ) Errado

> **Explicação:** Arquivos deletados vão para a Lixeira, podendo ser restaurados, **exceto os casos listados acima**.

---

### **05. FCC**

> Marcelo trabalha com o Windows 10. Apagou por engano um documento importante do pen drive utilizando a tecla Delete. O que acontece ao abrir a Lixeira?

**Alternativas:**

* **A)** Clicou com o botão direito no arquivo e selecionou **Restaurar**
* **B)** Observou que o arquivo não estava na Lixeira ✅
* C) Selecionou **Restaurar Arquivos**
* D) Selecionou o arquivo e clicou em **Desfazer**

> **Explicação:** Como o arquivo estava em pen drive (unidade removível), ele **não vai para a Lixeira**.

---