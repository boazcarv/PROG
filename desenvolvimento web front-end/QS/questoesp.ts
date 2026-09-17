///questao 1
const x1 = 0;
const y1 = 0;
const x2 = 3;
const y2 = 4;

const distancia = Math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2);
console.log(`A distância entre os pontos é ${distancia}.`);


///questao 2

const mediasFinais = [95, 78, 63, 42, 18, 101, -1, Number.NaN];

for (const mediaFinal of mediasFinais) {
if (Number.isNaN(mediaFinal) || mediaFinal < 0 || mediaFinal > 100) {
	console.log(`Média ${mediaFinal}: inválida. Digite um valor entre 0.0 e 100.0.`);
	} else if (mediaFinal >= 85) {
	console.log(`Média ${mediaFinal}: Conceito A`);
    } else if (mediaFinal >= 70) {
	console.log(`Média ${mediaFinal}: Conceito B`);
	} else if (mediaFinal >= 50) {
	console.log(`Média ${mediaFinal}: Conceito C`);
	} else if (mediaFinal >= 30) {
	console.log(`Média ${mediaFinal}: Conceito D`);
	} else {
	console.log(`Média ${mediaFinal}: Conceito E`);
	}
}
///questao 3
function jogarDado(): number {
  return Math.floor(Math.random() * 6) + 1;
}
let contadorFaceseis = 0;
for (let i = 0; i < 1000; i++) {
  if (jogarDado() === 6) {
    contadorFaceseis++;
}
}
console.log(`O resultado é esse: ${contadorFaceseis}`);
