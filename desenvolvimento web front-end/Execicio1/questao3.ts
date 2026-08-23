export {};

function diasDesdeInicioDoAno(dataDDMMAAAA: string): number {
  const partes: string[] = dataDDMMAAAA.split("/");
  const dia: number = Number(partes[0]);
  const mes: number = Number(partes[1]);
  const ano: number = Number(partes[2]);

  const data: Date = new Date(ano, mes - 1, dia);
  const inicioDoAno: Date = new Date(ano, 0, 1);

  const MS_POR_DIA: number = 1000 * 60 * 60 * 24;
  return Math.round((data.getTime() - inicioDoAno.getTime()) / MS_POR_DIA);
}

const dataInformada: string = "18/08/2026";

console.log(
  `Do início do ano até ${dataInformada} se passaram ` +
  `${diasDesdeInicioDoAno(dataInformada)} dias.`
);

