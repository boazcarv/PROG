/**
 * Recebe um número inteiro maior que 1 e informa se ele é primo.
 * Um número primo só é divisível por 1 e por ele mesmo.
 */
function verificarPrimo(numero: number): boolean {
	if (numero < 2) {
		return false;
	}

	let primo = true;
	let divisor = numero - 1;

	while (primo && divisor >= 2) {
		if (numero % divisor === 0) {
			primo = false;
		}
		divisor--;
	}

	return primo
}