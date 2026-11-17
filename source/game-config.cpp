// Original GEOE08 configuration hooks. Runs on the translated game's thread.
#include "recomp.h"
#include <cstdlib>
#include <cstring>

static bool enabled(const char* key) {
    const char* value = std::getenv(key);
    return value && *value && std::strcmp(value, "0") != 0;
}

extern "C" uint32_t cvs2_arena_half_width(void) {
    static const uint32_t width = enabled("CVS2_WIDESCREEN") ? 213u : 160u;
    return width;
}

extern "C" void cvs2_apply_assists(void) {
    static const bool easy = enabled("CVS2_EASY_OPERATION");
    static const bool supers = enabled("CVS2_INFINITE_SUPER");
    // C, A, P, S, N and K gauge capacities from the game's gauge routines.
    static const uint16_t maximum[] = {168, 144, 192, 100, 216, 72};
    for (uint32_t side = 0; side < 2; ++side) {
        const uint32_t p = 0x80190190u + side * 0x5b4u;
        // CPU fighters retain their original control and gauge rules.
        if (LD8(p + 0x52d) != 0) continue;
        if (easy) {
            ST8(0x802b588cu + side, 0); // Selection value: GC-ism.
            ST8(p + 0x4ff, 1);         // Active fighter: GC-ism enabled.
        }
        if (!supers || LD8(p) != 1) continue;
        const uint32_t groove = LD8(p + 0x1e9);
        if (groove >= 6) continue;
        ST16(p + 0x1e2, maximum[groove]);
        // S/MAX and K/Rage use an additional active-state/timer field.
        if (groove == 3) ST16(p + 0x208, 1);
        if (groove == 5) ST16(p + 0x208, 1080);
    }
}
