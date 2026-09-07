let inicio = Number(prompt("Início do intervalo:"));
let fim = Number(prompt("Fim do intervalo:"));

if (
  Number.isInteger(inicio) &&
  Number.isInteger(fim) &&
  inicio >= 1 &&
  fim >= inicio
) {
  let contadorPrimos = 0;

  for (let num = Math.max(inicio, 2); num <= fim; num++) {
    let primo = true;
    let divisor = num - 1;

    while (primo && divisor > 1) {
      if (num % divisor === 0) {
        primo = false;
      } else {
        divisor--;
      }
    }

    if (primo) {
      contadorPrimos++;
    }
  }

  console.log(`Quantidade de primos: ${contadorPrimos}`);
} else {
  console.log("Intervalo inválido.");
}