const altura = Number(prompt("Digite a altura em centímetros:"));
const sexo = (prompt("Digite o sexo (m/f):") ?? "").toLowerCase();

let k: number;

if (sexo === "m") {
  k = 4;
} else if (sexo === "f") {
  k = 2;
} else {
  console.log("Sexo inválido");
  throw new Error("Sexo inválido");
}

const pesoIdeal = altura - 100 - (altura - 150) / k;

console.log(`Peso ideal: ${pesoIdeal.toFixed(2)} kg`);