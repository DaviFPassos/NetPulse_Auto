# 🖥️ Visualização do Dashboard (Interface de Produção)

O painel foi projetado utilizando a paleta de cores Catppuccin Mocha para garantir um tema escuro confortável para Centros de Operações de Rede (NOC). Os cards reagem dinamicamente à integridade do servidor:

Borda Verde Vibrante: Servidor estável operando com latência nominal.

Borda Vermelha de Alerta: Queda de conectividade detectada, latência zerada automaticamente.

Como visualizar no Windows através do WSL2:
Como o artefato é gerado dentro do Linux virtualizado, você pode abri-lo diretamente no navegador do seu Windows utilizando o explorador de arquivos:

No VS Code, clique com o botão direito sobre o arquivo web/index.html.

Selecione a opção "Reveal in File Explorer" (Revelar no Explorador de Arquivos).

Dê duplo clique no arquivo para abrir no Chrome/Edge. Para atualizar o painel após novos scans, basta pressionar F5.

---

# 🔒 Governança de Código e Boas Práticas (.gitignore)
Este repositório implementa políticas rígidas de versionamento para evitar o Git Noise (poluição visual de commits). Os dados voláteis (metrics.txt) e os artefatos de saída compilados automaticamente pelo código (index.html) estão explicitamente inseridos no arquivo de bloqueio.

# .gitignore
```
logs/
web/index.html
venv/
.venv/
```

Como tratamos de domínios públicos, o expus por didática, mas *ATENÇÃO:* USE O *.gitignore* para proteger seus dados e da sua empresa!