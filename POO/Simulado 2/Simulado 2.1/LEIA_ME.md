### **PARTE 1: PROVA OFICIAL DA AP2 (QUESTÃO ÚNICA INTEGRADA)**

---

**INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA (IFRN)** **Disciplina:** Programação Orientada a Objetos **Professor:** Higor Morais **Avaliação:** AP2 — Avaliação Prática em Laboratório (Em dupla, com consulta à documentação oficial do Python)[1] **Entrega:** Submissão do código-fonte em arquivos `.py` ao término do encontro[1].

---

#### **ENUNCIADO DA QUESTÃO ÚNICA INTEGRADA: SISTEMA DE DELIVERY E LOGÍSTICA**

Uma empresa de tecnologia contratou sua dupla para desenvolver o núcleo do sistema de processamento de pedidos e logística de entregas de um restaurante[2][3]. O sistema deve integrar **todos os conceitos do bloco**: **classes abstratas**, **herança simples e múltipla (mixin)**, **polimorfismo puro**, **relacionamentos (associação, agregação e composição)**, **injeção de dependência** e **tratamento de exceções personalizadas**[1][4].

Siga rigorosamente os requisitos de modelagem arquitetural abaixo:

---

#### **Requisitos da Questão**

1. **Exceção Personalizada (** **EntregaForaDeAreaError** **):**
  * Crie uma classe de exceção herdando de `Exception`[2][4].
  * Ela deve ser disparada (`raise`) caso a distância de entrega informada seja superior ao limite máximo operacional suportado pelo entregador[2].
2. **Herança Múltipla e Mixin de Habilidade (** **RastreavelMixin** **):**
  * Crie a classe `RastreavelMixin` contendo o método `emitir_sinal_gps() -&gt; str`, demonstrando o uso de herança múltipla para adicionar habilidades reutilizáveis sem poluir a classe base principal[4].
3. **Hierarquia Abstrata e Subclasses (** **Entregador** **,** **DeBike** **,** **DeMoto** **):**
  * **Entregador(ABC)**: Classe abstrata base herdando de `ABC`[2][4].
    * Atributos no construtor: `nome` (str) e `limite_distancia` (float)[2].
    * Método abstrato `@abstractmethod`: `taxa_entrega(distancia: float) -&gt; float`[2][4].
    * Contrato de validação: Se `distancia &gt; self.limite_distancia`, deve lançar a exceção `EntregaForaDeAreaError`[2].
  * **DeBike**: Subclasse de `Entregador` e `RastreavelMixin` (Herança Múltipla)[2][4].
    * Seu construtor recebe apenas o `nome` e repassa ao construtor pai via `super().__init__()` fixando o `limite_distancia = 5.0` km[4].
    * O cálculo da taxa de entrega é fixo em **R$ 5,00** (após validar a distância via `super().taxa_entrega(distancia)`)[2].
  * **DeMoto**: Subclasse de `Entregador` e `RastreavelMixin`[2][4].
    * Seu construtor recebe `nome` e repassa ao pai via `super().__init__()` fixando `limite_distancia = 20.0` km[4].
    * O cálculo da taxa é **R$ 7,00 + (R$ 1,50 × distancia)** (após validar o limite via `super()`)[2].
4. **Relacionamentos de Objetos (** **Cliente** **,** **ItemPedido** **,** **Pedido** **,** **Restaurante** **):**
  * **Cliente**: Possui `nome` (str) e `endereco` (str).
  * **ItemPedido**: Possui `descricao` (str) e `preco` (float).
  * **Pedido**:
    * **Associação:** Recebe e armazena um objeto `Cliente` recebido de fora[2][4].
    * **Injeção de Dependência:** Recebe um objeto `Entregador` injetado pelo construtor (qualquer subclasse de `Entregador`)[2][4].
    * **Composição:** Gerencia internamente uma lista de `ItemPedido`. Contém o método `adicionar_item(descricao, preco)` que **instancia o** **ItemPedido** **internamente**[2][4].
    * Método `calcular_total(distancia: float) -&gt; float`: Calcula a soma dos preços dos itens composta com a taxa de entrega polimórfica obtida do `entregador`. **É proibido utilizar qualquer estrutura** **if isinstance(...)**[4][5].
  * **Restaurante**:
    * **Agregação:** Armazena uma lista de pedidos cadastrados via `registrar_pedido(pedido)`[2][4].
    * Método `faturamento_total(distancias: list[float]) -&gt; float`: Iterar polimorficamente sobre a lista de pedidos agregados para somar o faturamento[2][6].
5. **Programa Principal (** **main.py** **):**
  * Instancie clientes, entregadores (`DeBike` e `DeMoto`) e crie pedidos[2].
  * Demonstre o cálculo bem-sucedido de entregas dentro do limite[2].
  * Demonstre a captura do erro `EntregaForaDeAreaError` em um bloco `try/except` ao tentar realizar uma entrega de `DeBike` a 8.0 km[2].
  * Prove que a classe abstrata `Entregador` não pode ser instanciada diretamente (disparando `TypeError`)[2][6].