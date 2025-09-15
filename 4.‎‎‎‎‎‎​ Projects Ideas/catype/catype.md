# ✅ Catype – SaaS MVP To-Do List

## 📌 Estrutura Principal

* [ ] **Sidebar de Navegação**
  * [ ] Ícones principais (Trilha, Perfil, Configurações)
  * [ ] Indicador de progresso e premium
* [ ] **Tela Inicial estilo Duolingo**
  * [ ] Layout de trilha linear (missões em sequência)
  * [ ] Animações de entrada (Framer Motion)
* [ ] **Tema Visual**
  * [ ] Definir paleta de cores
  * [ ] Escolher tipografia padrão
  * [ ] Biblioteca de ícones

---

## 🎯 Componentes Essenciais

* [ ] **Componente Typing** (digitação interativa)

  * [ ] Entrada de texto com tempo real
  * [ ] Validação de caracteres
  * [ ] Feedback (correto/erro)
* [ ] **Componente Input Chat** (caixa estilo chat)

  * [ ] Entrada com envio por Enter
  * [ ] Histórico de mensagens
* [ ] **Componente Quiz**

  * [ ] Modo múltipla escolha
  * [ ] Modo digitação livre
* [ ] **Sistema de Validação**

  * [ ] Checar respostas corretas/erradas
  * [ ] Feedback visual imediato (verde/vermelho)
  * [ ] Contabilizar progresso da missão

---

## 💳 Integração de Pagamentos

* [ ] Escolher API (Polar vs Stripe)
* [ ] Configurar autenticação segura
* [ ] Criar **Plano MVP** (mensal / anual)
* [ ] Implementar **checkout funcional**
* [ ] Testar fluxo de cancelamento
* [ ] Testar renovação automática

---

## 🔧 Infra e Backend

* [ ] Definir stack inicial (Node.js + Express/NestJS ou Python FastAPI)
* [ ] Criar **API base**

  * [ ] Usuário (auth, perfil)
  * [ ] Sessão (login/logout)
  * [ ] Progresso (trilha, missões)
* [ ] Configurar banco de dados

  * [ ] Tabelas: usuários, trilha, missões, exercícios, planos
* [ ] Criar ambiente de testes (unitário + integração)

---

## 🚀 Roadmap MVP

* [ ] **v0.1** → Sidebar + Tela inicial + Quiz básico
* [ ] **v0.2** → Input Chat + Typing Component
* [ ] **v0.3** → Pagamentos (Stripe/Polar) + Usuários
* [ ] **v0.4** → Ajustes finais de UI/UX + Feedback

---


Logica

* [ ] recebe texto da ai
* [ ] validar repostas + progresso da barra
* [ ] gerar e armazenar proxima questao com base no usuario