function diasDesdeInicioDoAno(dataDDMMAAAA) {
  const partes = dataDDMMAAAA.split("/");
  const dia = Number(partes[0]);
  const mes = Number(partes[1]);
  const ano = Number(partes[2]);

  const data = new Date(ano, mes - 1, dia);
  const inicioDoAno = new Date(ano, 0, 1);

  const MS_POR_DIA = 1000 * 60 * 60 * 24;
  return Math.round((data - inicioDoAno) / MS_POR_DIA);
}

const dataInformada = "18/08/2026";

console.log(
  `Do início do ano até ${dataInformada} se passaram ` +
  `${diasDesdeInicioDoAno(dataInformada)} dias.`
);

