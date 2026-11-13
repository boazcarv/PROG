import { Component, inject, output } from '@angular/core';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';

type TipoContato = 'Amigo(a)' | 'Família' | 'Trabalho' | 'Outro';

interface DadosContato {
  nome: string;
  telefone: string;
  email: string;
  aniversario: string;
  tipo: TipoContato;
  endereco: string;
}

@Component({
  imports: [ReactiveFormsModule],
  selector: 'app-adiciona-contato',
  styleUrl: './adiciona-contato.css',
  templateUrl: './adiciona-contato.html',
})
export class AdicionaContato {
  private readonly fb = inject(FormBuilder);

  protected readonly formularioContato = this.fb.nonNullable.group({
    nome: ['', [Validators.required, Validators.minLength(3)]],
    telefone: ['', Validators.required],
    email: ['', [Validators.required, Validators.email]],
    aniversario: ['', Validators.required],
    tipo: ['Outro' as TipoContato, Validators.required],
    endereco: ['', Validators.required],
  });

  readonly contatoAdicionado = output<DadosContato>();

  protected adicionarContato(): void {
    if (this.formularioContato.invalid) {
      this.formularioContato.markAllAsTouched();
      return;
    }

    this.contatoAdicionado.emit(this.formularioContato.getRawValue());
    this.formularioContato.reset();
  }
}
