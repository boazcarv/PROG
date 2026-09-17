function lerInteiroMaiorQueUm(): number {
  let numero: number;

  do {
    numero = Number(prompt("Digite um inteiro maior que 1:"));
  } while (numero <= 1 || !Number.isInteger(numero));

  return numero;
}

function ehPrimo(numero: number): boolean {
  for (let divisor = 2; divisor < numero; divisor++) {
    if (numero % divisor === 0) {
      return false;
    }
  }

  return true;
}

const numero = lerInteiroMaiorQueUm();
const resultado = ehPrimo(numero) ? "é" : "não é";

console.log(`${numero} ${resultado} primo.`);