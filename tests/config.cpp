#include "recomp.h"
#include <cassert>
#include <cstdlib>
#include <cstdio>
#include <vector>
extern "C" {
uint8_t* g_mem;
uint8_t g_gp_buf[64];
uint32_t g_gp_len;
uint32_t vm_translate(uint32_t, int) { std::abort(); }
uint8_t mmio_read8(uint32_t) { std::abort(); }
uint16_t mmio_read16(uint32_t) { std::abort(); }
void mmio_write8(uint32_t, uint8_t) { std::abort(); }
void mmio_write16(uint32_t, uint16_t) { std::abort(); }
void gp_flush_line() { std::abort(); }
}
int main(int argc, char**) {
    const bool on = argc == 1;
    setenv("CVS2_WIDESCREEN", on ? "1" : "0", 1);
    setenv("CVS2_EASY_OPERATION", on ? "1" : "0", 1);
    setenv("CVS2_INFINITE_SUPER", on ? "1" : "0", 1);
    std::vector<uint8_t> ram(32 * 1024 * 1024);
    g_mem = ram.data();
    const uint32_t human = 0x80190190, cpu = human + 0x5b4;
    ST8(human, 1); ST8(cpu, 1); ST8(cpu + 0x52d, 1);
    ST8(0x802b588c, 1); ST8(0x802b588d, 1);
    assert(cvs2_arena_half_width() == (on ? 213u : 160u));
    const uint16_t expected[] = {168, 144, 192, 100, 216, 72};
    for (uint32_t groove = 0; groove < 6; ++groove) {
        ST8(human + 0x1e9, groove);
        ST16(human + 0x1e2, 0); ST16(human + 0x208, 0);
        const auto before = ram;
        cvs2_apply_assists();
        if (!on) { assert(ram == before); continue; }
        assert(LD8(human + 0x4ff) == 1 && LD8(0x802b588c) == 0);
        assert(LD16(human + 0x1e2) == expected[groove]);
        assert(LD16(human + 0x208) == (groove == 3 ? 1u : groove == 5 ? 1080u : 0u));
        assert(LD8(cpu + 0x4ff) == 0 && LD8(0x802b588d) == 1);
        assert(LD16(cpu + 0x1e2) == 0 && LD16(cpu + 0x208) == 0);
        // No adjacent or unrelated memory may be changed by the assist.
        for (size_t i = 0; i < ram.size(); ++i) {
            const uint32_t a = uint32_t(i) + 0x80000000u;
            if (a == human + 0x4ff || a == 0x802b588c ||
                (a >= human + 0x1e2 && a < human + 0x1e4) ||
                (a >= human + 0x208 && a < human + 0x20a)) continue;
            assert(ram[i] == before[i]);
        }
    }
    ST8(human + 0x1e9, 255); ST16(human + 0x1e2, 17);
    cvs2_apply_assists(); assert(LD16(human + 0x1e2) == 17);
    ST8(human + 0x1e9, 0); ST8(human, 0);
    cvs2_apply_assists(); assert(LD16(human + 0x1e2) == 17);
    std::puts(on ? "enabled: bounds, six gauges, CPU isolation and write boundaries passed" : "disabled: no RAM changes passed");
}
