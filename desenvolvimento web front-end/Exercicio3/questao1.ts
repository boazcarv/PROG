let somaRendas: number = 0;
let somaFilhos: number = 0;
let quantidadeFamilias: number = 0;


const entradaRenda = prompt("Digite a renda familiar (valor negativo para encerrar):");
let renda: number = entradaRenda !== null ? Number(entradaRenda) : -1;

let filhos: number = -1;
if (renda >= 0) {
  const entradaFilhos = prompt("Digite a quantidade de filhos da família (valor negativo para encerrar):");
  filhos = entradaFilhos !== null ? Number(entradaFilhos) : -1;
}


while (renda >= 0 && filhos >= 0) {
  somaRendas += renda;
  somaFilhos += filhos;
  quantidadeFamilias++;

  const proxRenda = prompt("Digite a renda familiar (valor negativo para encerrar):");
  renda = proxRenda !== null ? Number(proxRenda) : -1;

  if (renda >= 0) {
    const proxFilhos = prompt("Digite a quantidade de filhos da família (valor negativo para encerrar):");
    filhos = proxFilhos !== null ? Number(proxFilhos) : -1;
  }
}

const mediaRenda: number =
  quantidadeFamilias > 0 ? somaRendas / quantidadeFamilias : 0;

const mediaFilhos: number =
  quantidadeFamilias > 0 ? somaFilhos / quantidadeFamilias : 0;

console.log(`Total de famílias: ${quantidadeFamilias}`);
console.log(`Renda familiar média: R$ ${mediaRenda.toFixed(2)}`);
console.log(`Média de filhos por família: ${mediaFilhos.toFixed(2)}`);