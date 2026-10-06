import { Component } from '@angular/core';
import { DecimalPipe } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  imports: [DecimalPipe, FormsModule],
  selector: 'app-calcular',
  styleUrl: './calcular.scss',
  templateUrl: './calcular.html',
})
export class Calcular {
  notaPrimeiroBimestre = 0;
  notaSegundoBimestre = 0;
  mediaParcial: number | null = null;

  calcularMedia(): void {
    this.mediaParcial =
      (2 * this.notaPrimeiroBimestre + 3 * this.notaSegundoBimestre) / 5;
  }

  get situacao(): string {
    if (this.mediaParcial === null) {
      return '';
    }

    if (this.mediaParcial >= 60) {
      return 'Aprovado(a)';
    }

    if (this.mediaParcial >= 10) {
      return 'Avaliação final';
    }

    return 'Reprovado(a)';
  }
}
