const b1 = Number(prompt("Digite a nota do primeiro bimestre:"));
const b2 = Number(prompt("Digite a nota do segundo bimestre:"));

const mediaParcial = (b1 * 2 + b2 * 3) / 5;

if (mediaParcial < 10) {
  console.log("reprovado");
} else if (mediaParcial >= 60) {
  console.log("aprovado");
} else {
  console.log("prova final");
}