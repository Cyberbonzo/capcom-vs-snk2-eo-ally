# Controles e opções

| ROG Ally | Entrada GameCube |
|---|---|
| Analógico esquerdo | Analógico principal |
| Direcional | D-pad |
| Analógico direito | C-Stick |
| A / B / X / Y | A / B / X / Y |
| RB | Z |
| LT / RT | L / R |
| Menu | Start / pausa original |

O GC-ism usa o C-Stick para comandos simplificados. Os golpes disponíveis e a direção correspondente dependem do personagem. A combinação Z + C-Stick corresponde a RB + analógico direito no Ally. O último código mantém esse estilo ativo para jogadores humanos, com validação em hardware ainda pendente.

Em `jogar.sh`:

- `CVS2_WIDESCREEN=1`: saída 16:9, cenário com recorte proporcional e arena ampliada. Use `0` para regras de largura 4:3.
- `CVS2_EASY_OPERATION=1`: força GC-ism para o jogador humano.
- `CVS2_INFINITE_SUPER=1`: mantém o recurso de super disponível nos seis tipos de barra; oponentes controlados pela CPU conservam as regras normais.

As opções de assistência não eliminam animações, recuperação, restrições aéreas ou regras específicas de cada golpe. O teste completo dos supers em todos os grooves/personagens ainda está pendente. A configuração do launcher é reaplicada a cada inicialização.

O cartão virtual guarda o que o jogo originalmente salva; não é um save state que retoma uma luta no mesmo quadro.
