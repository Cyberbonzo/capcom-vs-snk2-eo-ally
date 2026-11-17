# Capcom vs. SNK 2 EO — Ally Recomp

Projeto experimental de recompilação estática para Linux x86-64, desenvolvido e testado em um ROG Ally com Bazzite. **Traga sua própria cópia do jogo.** Este repositório contém adaptações e instruções; não contém imagem de disco, código gerado do jogo, executáveis, saves ou artes da Capcom/SNK.

Versão do projeto: **0.1.0**. Revisão suportada: GameCube USA **GEOE08**.

Repositório: https://github.com/Cyberbonzo/capcom-vs-snk2-eo-ally

## Estado

- CPU PowerPC traduzida previamente em C e compilada para x86-64, usando o [gcn-recomp](https://github.com/ethannicholas/gcn-recomp), revisão fixa `9e93f1bb7cc4a370af53c895e971fdcab55ed3fc`.
- Runtime de compatibilidade para GX, áudio e dispositivos. O executável deste projeto não usa um interpretador PowerPC ou JIT para executar o código do jogo.
- Tela cheia 1920×1080 e proporção 16:9, com personagens preservados em suas proporções. Os fundos recebem ampliação uniforme e recorte vertical; não há esticamento horizontal. Isso não é expansão inédita da geometria dos cenários.
- Limites de movimento alterados de ±160 para ±213 unidades em relação à câmera, incluindo a restrição de movimento de pares de lutadores.
- Apresentação da imagem sincronizada com os comandos gráficos, corrigindo o desaparecimento intermitente dos personagens. Gameplay e 16:9 confirmados pelo usuário no Ally.
- Controles físicos do Ally, pausa original do jogo e cartão de memória virtual.
- GC-ism permanente e barra de super continuamente abastecida para jogadores humanos. A versão com essas assistências foi compilada no Ally e iniciou pelo Steam. Falta confirmar os comandos durante uma luta.

Consulte [compilação](docs/BUILD.md), [controles](docs/CONTROLS.md) e [validação](docs/VALIDATION.md).

## Preparar sua cópia

Requer Python, Git, decomp-toolkit, CMake, Ninja, Clang e as dependências Linux do runtime. Os scripts não instalam pacotes do sistema. No ambiente de desenvolvimento foi reutilizado um contêiner de compilação existente.

```sh
python3 source/prepare.py /caminho/para/sua-imagem.iso --dtk /caminho/para/dtk
bash source/build-linux.sh
bash jogar.sh
```

O preparador valida a identidade e o SHA-1 do executável principal. Não existe download de dados do jogo. Não execute o preparador dentro de um clone público que você pretende publicar inteiro: mantenha imagem, análise e build privados, conforme o `.gitignore` e a lista de publicação.

## Limites conhecidos

As texturas e os sprites continuam com o detalhe dos originais; saída 1080p não cria arte HD. O recorte de fundos pode remover detalhes superiores/inferiores. Nem todos os cenários, personagens e modos foram testados exaustivamente. Replays produzidos com arena ampliada ou assistências podem divergir das regras originais.

Este projeto não é afiliado à Capcom, SNK ou Nintendo. Nomes identificam o jogo compatível. Licença MIT apenas para o código disponibilizado, respeitando os avisos do runtime.
