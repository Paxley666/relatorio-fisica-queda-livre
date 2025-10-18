# Análise Experimental da Queda Livre (Script Python)

Este repositório contém o script Python (`Meto_Graf_Ajus_Ret_Ince.py`) utilizado para a análise dos dados de um experimento de queda livre.

[cite_start]O script realiza uma regressão linear nos dados de tempo ($t$) vs. velocidade vertical ($v_y$) coletados com o software Tracker, conforme o método de análise de incertezas descrito no Apêndice D do tutorial [cite: 143-169].

**Todos os outros arquivos do projeto (o relatório em PDF, o vídeo `.mp4` original e o gráfico gerado) foram enviados ao professor por e-mail.**

---

## Análise e Resultado Final

Os dados foram coletados no Tracker e a taxa de quadros (FPS) do vídeo foi ajustada corretamente para 60 FPS, refletindo a gravação original da câmera.

O script Python analisou esses dados corrigidos e o resultado final encontrado para a aceleração da gravidade foi:

**$g = 10.41 \pm 0.13 \, m/s²$**

Este valor experimental é consistente com o valor teórico da gravidade ($g \approx 9.8 \, m/s²$), estando dentro da margem de erro esperada para o método.

## Como Executar este Script

1.  Instale as dependências:
    ```bash
    pip install numpy scipy matplotlib
    ```
2.  Execute o script:
    ```bash
    python Meto_Graf_Ajus_Ret_Ince.py
    ```
