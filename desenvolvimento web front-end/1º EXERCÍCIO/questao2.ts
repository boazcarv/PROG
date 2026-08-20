const mediaParcial: number = 45;

const notaNecessaria: number = 120 - mediaParcial;

if (notaNecessaria > 100) {
    console.log(
        `Com a média parcial de ${mediaParcial}, é necessário obter ${notaNecessaria} para atingir a média final de 100. Portanto, é impossível atingir essa média.`
    );
} else {
    console.log(
        `Com a média parcial de ${mediaParcial}, é necessário obter ${notaNecessaria} para atingir a média final de 100. Portanto, é possível atingir essa média.`
    );
}