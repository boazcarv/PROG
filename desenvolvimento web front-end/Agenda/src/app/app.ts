import { Component, signal } from '@angular/core';
import { FormsModule } from '@angular/forms';

type TipoContato = 'Amigo(a)' | 'Família' | 'Trabalho' | 'Outro';

interface Contato {
  id: number;
  nome: string;
  telefone: string;
  email: string;
  endereco: string;
  aniversario: string;
  tipo: TipoContato;
  cor: string;
}

@Component({
  imports: [FormsModule],
  selector: 'app-root',
  styleUrl: './app.css',
  templateUrl: './app.html',
})
export class App {
  protected readonly contatos = signal<Contato[]>([]);
  protected novoContato = this.contatoVazio();

  private readonly coresDosAvatares = ['#e5b7ad', '#b9c9b2', '#b7c8df', '#d7c0d8', '#e4cf9f'];

  protected adicionarContato(): void {
    if (!this.novoContato.nome.trim() || !this.novoContato.telefone.trim()) {
      return;
    }

    const contato: Contato = {
      ...this.novoContato,
      id: Date.now(),
      nome: this.novoContato.nome.trim(),
      telefone: this.novoContato.telefone.trim(),
      email: this.novoContato.email.trim(),
      endereco: this.novoContato.endereco.trim(),
      cor: this.coresDosAvatares[this.contatos().length % this.coresDosAvatares.length],
    };

    this.contatos.update((contatos) => [...contatos, contato]);
    this.novoContato = this.contatoVazio();
  }

  protected removerContato(id: number): void {
    this.contatos.update((contatos) => contatos.filter((contato) => contato.id !== id));
  }

  protected obterIniciais(nome: string): string {
    return nome
      .split(' ')
      .filter(Boolean)
      .slice(0, 2)
      .map((part) => part[0].toUpperCase())
      .join('');
  }

  private contatoVazio(): Omit<Contato, 'id' | 'cor'> {
    return {
      nome: '',
      telefone: '',
      email: '',
      endereco: '',
      aniversario: '',
      tipo: 'Outro',
    };
  }
}
