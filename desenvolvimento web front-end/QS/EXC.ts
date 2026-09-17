

/// QUESTÃO 1
const combustivel: string = "Gasolina";
const preco: number = 5.80;
const litros: number = 30;

function calcularTotal(preco: number, litros: number): number {
	return preco * litros;
}

const total: number = calcularTotal(preco, litros);

console.log(`Combustivel: ${combustivel} | Total: R$ ${total.toFixed(2)}`);


/// QUESTÃO 2 ex1
function calcularMulta(diasAtraso: number, tipoLeitor: string): number {
  let multaTotal: number;

  // calcula a multa base usando let
  if (tipoLeitor === "Estudante") {
    multaTotal = diasAtraso * 1.00;
  } else {
    multaTotal = diasAtraso * 2.00;
  }

  // aplica a taxa extra se o atraso for maior que 15 dias
  if (diasAtraso > 15) {
    multaTotal += 10.00;
  }

  return multaTotal;
}

// testando a função:
console.log(calcularMulta(10, "Estudante")); // Saída: 10
console.log(calcularMulta(20, "Comum"));     // Saída: 50


/// QUESTÃO 2 ex2
function calcularFrete(peso: number, regiao: string): number {
  const precoPorQuilo: number = regiao === "Sudeste" ? 5.00 : 10.00;
  const taxaManuseioPesado: number = peso > 20 ? 15.00 : 0;

  return peso * precoPorQuilo + taxaManuseioPesado;
}


/// QUESTÃO 3
function calcularPontos(qtdIngressos: number, tipoCliente: string): number {
  const pontosPorIngresso: number = tipoCliente === "VIP" ? 15 : 10;
  const bonus: number = qtdIngressos >= 4 ? 20 : 0;

  return qtdIngressos * pontosPorIngresso + bonus;
}


  /// QUESTÃO 4
  function calcularMediaPositivas(temperaturas: number[]): number {
    let soma: number = 0;
    let quantidade: number = 0;

    for (const temperatura of temperaturas) {
      if (temperatura > 0) {
        soma += temperatura;
        quantidade++;
      }
    }

    return quantidade > 0 ? soma / quantidade : 0;
  }



  /// QUESTÃO 5
  function contarPares(numeros: number[]): number {
    let contador: number = 0;

    for (const numero of numeros) {
      if (numero % 2 === 0) {
        contador++;
      }
    }

    return contador;
  }
  /// QUESTÃO 6

function processarVendas(vendas: number[]): number {
  let total: number = 0;

  for (const venda of vendas) {
    total += venda;
  }

  return total >= 500 ? total + 50 : total;
}
  
