cmake_minimum_required(VERSION 3.20)
project(cvs2eo C CXX)
add_subdirectory(upstream/gcn-recomp)
gcn_add_game(
 NAME cvs2eo
 TITLE "Capcom vs. SNK 2 EO"
 LABEL "CVS2 EO Recomp"
 DISC_ID GEOE08
 DOL_SHA1 0772a7cabc270b32949f43279a16b0aec81811f9
 SYMBOLS ${CMAKE_SOURCE_DIR}/analysis/symbols.txt
 TABLES ${CMAKE_SOURCE_DIR}/recomp
 IMAGE_DIR ${CMAKE_SOURCE_DIR}/game
 FPS 60
 REL_SYMBOLS ${CMAKE_SOURCE_DIR}/analysis/rel-symbols
 RELS
 module/demo.rel
 module/game.rel
 module/menu.rel
 module/pl00.rel
 module/pl01.rel
 module/pl02.rel
 module/pl03.rel
 module/pl04.rel
 module/pl05.rel
 module/pl06.rel
 module/pl07.rel
 module/pl08.rel
 module/pl09.rel
 module/pl0a.rel
 module/pl0b.rel
 module/pl0c.rel
 module/pl0d.rel
 module/pl0e.rel
 module/pl0f.rel
 module/pl10.rel
 module/pl11.rel
 module/pl12.rel
 module/pl13.rel
 module/pl14.rel
 module/pl15.rel
 module/pl16.rel
 module/pl17.rel
 module/pl18.rel
 module/pl19.rel
 module/pl1a.rel
 module/pl1b.rel
 module/pl1c.rel
 module/pl1d.rel
 module/pl1e.rel
 module/pl1f.rel
 module/pl20.rel
 module/pl21.rel
 module/pl22.rel
 module/pl23.rel
 module/pl24.rel
 module/pl25.rel
 module/pl26.rel
 module/pl27.rel
 module/pl28.rel
 module/pl29.rel
 module/pl2a.rel
 module/pl2b.rel
 module/pl2c.rel
 module/pl2d.rel
 module/pl2e.rel
 module/pl2f.rel
)
target_sources(gcn_core PRIVATE ${CMAKE_SOURCE_DIR}/source/game-config.cpp)
