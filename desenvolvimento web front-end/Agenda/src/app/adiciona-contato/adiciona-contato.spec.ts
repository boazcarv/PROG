import { ComponentFixture, TestBed } from '@angular/core/testing';
import { AdicionaContato } from './adiciona-contato';

describe('AdicionaContato', () => {
  let component: AdicionaContato;
  let fixture: ComponentFixture<AdicionaContato>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AdicionaContato],
    }).compileComponents();

    fixture = TestBed.createComponent(AdicionaContato);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('deve criar o componente', () => {
    expect(component).toBeTruthy();
  });
});
