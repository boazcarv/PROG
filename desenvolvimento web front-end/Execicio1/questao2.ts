export {};
const mediaParcial: number = 45;

const notaNecessaria: number = 120 - mediaParcial;

if (notaNecessaria > 100) {
  console.log(
    `Com média parcial ${mediaParcial}, seriam necessários ${notaNecessaria} ` +
    `pontos na avaliação final — como a nota máxima é 100, não é mais possível aprovar.`
  );
} else {
  console.log(
    `Com média parcial ${mediaParcial}, o(a) estudante precisa tirar ` +
    `${notaNecessaria} na avaliação final para ser aprovado(a).`
  );
}
