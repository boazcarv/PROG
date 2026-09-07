let num: number;

do {
  num = Number(prompt("Digite um inteiro maior que 1:"));
} while (num <= 1 || !Number.isInteger(num));

let primo = true;
let divisor = num - 1;

while (primo && divisor > 1) {
  if (num % divisor === 0) {
    primo = false;
  } else {
    divisor--;
  }
}

console.log(`${num} ${primo ? "é" : "não é"} primo.`);