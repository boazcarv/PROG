export {};

interface Aluno {
  nome: string;
  matricula: string;
  curso: string;
  ira: number;
}

const aluno: Aluno = {
  "nome": "Maria da Silva",
  "matricula": "202092923222",
  "curso": "Informática",
  "ira": 83.2
};

console.log(`${aluno.nome} é aluna de ${aluno.curso} com matrícula ${aluno.matricula} e possui IRA ${aluno.ira}.`);
