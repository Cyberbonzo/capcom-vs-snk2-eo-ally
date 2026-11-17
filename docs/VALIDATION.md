# Validação — 2026-11-17

## Confirmado

- Build Linux Release com o patch de apresentação e 16:9 concluído no contêiner já disponível no Ally.
- Personagens voltaram a permanecer visíveis; confirmação explícita do usuário.
- Capturas 1920×1080 e jogo próximo de 60 FPS no cenário testado.
- Leitura dos limites em execução: borda esquerda em X=-405 com câmera=-192 (diferença de -213), ultrapassando o limite anterior de -160. Também observada a marca de colisão da borda direita após ampliação.
- Cenário de Xangai preencheu ambos os lados nas capturas após a correção. O usuário confirmou que o ajuste de tela e movimento funcionou.
- O patch completo foi reaplicado a arquivos originais da revisão fixada; conteúdo comparado após normalizar finais de linha Windows/Linux. Aplicação repetida reconheceu que o patch já estava instalado.
- [Verificação de código no GitHub aprovada](https://github.com/Cyberbonzo/capcom-vs-snk2-eo-ally/actions/runs/44153366432): compilação Clang dos hooks, aplicação idempotente do patch, validação Python/shell e testes das seis barras, configurações desativadas, isolamento da CPU e limites de escrita na RAM.

- A compilação Linux com as assistências terminou no Ally. O atalho Steam iniciou o executável e o jogo carregou o módulo game.rel. A cópia privada do executável e a do cartão de memória foram conferidas por SHA-256.

## Pendente

O teste físico dos especiais pelo analógico direito e dos supers com RB + analógico direito segue pendente nesta compilação, inclusive em Arcade e Training.

Não se afirma cobertura exaustiva de todos os cenários, finais, combinações de personagens ou modos. O cenário de gelo não foi recapturado nesta última sessão de teste após a correção; a confirmação geral do usuário complementa as capturas de Xangai.

REA foi usado na inspeção inicial. O formato DOL não era suportado diretamente nessa etapa; a análise do jogo usou decomp-toolkit/disassembly e a tradução estática do gcn-recomp. O relatório ELF inicial não certifica o executável final.
