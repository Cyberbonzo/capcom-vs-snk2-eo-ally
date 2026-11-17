# Compilação privada

Use uma cópia própria de GEOE08. SHA-1 de `main.dol`: `0772a7cabc270b32949f43279a16b0aec81811f9`. A imagem testada foi extraída de um arquivo do usuário; suporte a outras formas de NKit comprimido não foi estabelecido.

`source/prepare.py` copia a imagem para `game/disc.nkit.iso`, verifica o executável, extrai 51 módulos ativos e usa decomp-toolkit para produzir análise local. O executável dtk usado no desenvolvimento foi 1.9.1. O preparador busca a revisão fixa do gcn-recomp. Não inclui os módulos alternativos de teste que duplicam IDs.

`source/build-linux.sh` aplica `source/runtime.patch` de forma idempotente e usa CMake/Ninja/Clang em Release. O patch precisa ser aplicado ao upstream fixado. `recomp/patches.txt` substitui instruções específicas apenas na tradução; a imagem original permanece intacta.

Saída: `build-linux/cvs2eo`. Execute `bash jogar.sh` a partir de uma sessão gráfica Linux. Adicione esse launcher como jogo externo ao Steam, sem Proton. Feche jogos anteriores antes de iniciar outro teste.

Dados privados: `game/`, `rom-original/`, `analysis/`, `build*/`, `saves/`, `logs/` e arquivos gerados. Nunca publique esses diretórios. A pasta pública de distribuição é montada por uma lista explícita de arquivos permitidos.

## Verificação sem ROM

O workflow `source-check.yml` baixa apenas o runtime MIT fixado, aplica o patch duas vezes, compila os hooks de configuração e verifica limites, assistências habilitadas/desabilitadas, isolamento da CPU e acessos à RAM. Isso não substitui testes de gameplay.
