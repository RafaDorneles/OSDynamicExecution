# Ambiente

O programa foi desenvolvido utilizando **Python 3.12.5** e **Windows**.

---

# Parâmetros

Para iniciar a execução do trabalho, siga os passos abaixo:

1. Insira todos os arquivos que deseja testar dentro da pasta `inputFiles`.
2. Acesse o arquivo `simulator.py` e, no array **input_files**, insira os caminhos corretos dos arquivos, além das outras informações que deseja simular.
3. **Atenção para o valor passado para `computation_time`!**

---

# Sobre o `computation_time`

O `computation_time` é baseado no número de instruções executadas, considerando que **cada instrução demora 1 unidade de tempo (1u)**.

### Exemplos:

#### **`prog1.txt`**

- Não possui loop.
- Número de instruções: **4**.
- **`computation_time = 4`**

#### **`prog2.txt`**

- Possui loop.
- O tempo de computação para a tarefa ser executada é calculado como:

Onde:

- `ifa`: Número de instruções fixas **antes do loop**.
- `il`: Número de instruções **dentro do loop**.
- `nl`: Número de vezes que o programa entra no loop.
- `ifp`: Número de instruções fixas **após o loop**.

**Exemplo com 6 iterações (`nl = 6`):**

- `ifa = 3` (instruções antes do loop).
- `il = 5` (instruções dentro do loop).
- `ifp = 3` (instruções após o loop).

Se o valor de `computation_time` for menor que o necessário para completar a execução, o programa **não conseguirá executar completamente**.
`computation_time = ifa + il * nl + ifp`

---

---

# Sobre o `simulation_time`

O `simulation_time` define o tempo total de execução da simulação no escalonador. Ele é usado para limitar o tempo que o escalonador ficará ativo.

### Como funciona:

- O `simulation_time` é configurado diretamente no método `_run` da classe `EDFScheduler`.
- Durante a execução, o escalonador verifica se o tempo atual (`self.time`) atingiu o valor de `simulation_time`. Se isso ocorrer, a simulação é encerrada, mesmo que existam processos ainda não concluídos.

### Exemplo:

No arquivo `scheduler.py`, o `simulation_time` está configurado como `500`:

### Processos não concluídos:

Se o simulation_time for menor que o necessário para concluir todos os processos, alguns processos podem não ser finalizados.

### Ajuste do valor:

Certifique-se de que o simulation_time seja suficiente para permitir que todos os processos sejam executados, considerando seus computation_time e period.

### Uso em testes:

Durante testes, você pode configurar um valor menor para o simulation_time para verificar o comportamento do escalonador em cenários de interrupção.

---

# Como Rodar o Programa

1. Certifique-se de que o arquivo `main.py` está configurado corretamente.
2. Execute o comando abaixo no terminal para iniciar a aplicação:

```bash
python -u main.py
```

O computation_time deve ser configurado corretamente para cada programa, com base no número de instruções executadas.
Caso o valor de computation_time ou simulation_time seja insuficiente , o programa não será concluído corretamente.
Certifique-se de que os arquivos de entrada estão no formato correto e localizados na pasta inputFiles.
O arquivo possui 3 novos programas criados para fim de teste, além dos disponibilizados, prog3, prog4 e prog5, caso não os queira, basta comentar na área de input_files
