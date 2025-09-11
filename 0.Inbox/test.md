# 💡 Closure em JavaScript
Closure = <mark style="background: #FFF3A3A6;">função + ambiente léxico que a criou.  </mark>
→ Permite acessar variáveis de escopo externo mesmo após execução da função pai.  

## Exemplo
```js
function contador() {
  let count = 0;
  return function() {
    count++;
    return count;
  }
}

const c = contador();
c(); // 1
c(); // 2
```

## Links
- [[Funções]]
- [[Escopo]]
- [[Memória e Garbage Collector]]
- [[Questão: Implementar contador com closure]]
