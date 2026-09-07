function main(): void {
	let inicio: number;
	let fim: number;

	// Leitura e validação do início
	do {
		inicio = Number(prompt("Digite o início do intervalo (inteiro positivo): ") ?? "");
	} while (!Number.isInteger(inicio) || inicio <= 0);

	// Leitura e validação do fim
	do {
		fim = Number(prompt(`Digite o fim do intervalo (inteiro >= ${inicio}): `) ?? "");
	} while (!Number.isInteger(fim) || fim < inicio);

	let quantidadePrimos = 0;

	// Percorre cada número do intervalo
	for (let num = inicio; num <= fim; num++) {
		if (num <= 1) {
			continue; // 0 e 1 não são primos
		}

		// Lógica idêntica à Questão 2 para cada número
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
			quantidadePrimos++;
		}
	}

	console.log(`No intervalo de ${inicio} até ${fim}, existem ${quantidadePrimos} números primos.`);
}

main();