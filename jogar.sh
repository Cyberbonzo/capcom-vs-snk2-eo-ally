#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
cd "$ROOT"
mkdir -p logs saves
exec 9>logs/session.lock
flock -n 9 || exit 0
export SDL_JOYSTICK_HIDAPI=0
export SDL_JOYSTICK_ALLOW_BACKGROUND_EVENTS=1
export GCN_VI_PRESENT=1
export CVS2_AUTOSAVE=1
export CVS2_WIDESCREEN=1
export CVS2_EASY_OPERATION=1
export CVS2_INFINITE_SUPER=1
export GCN_TEXHASH_ALWAYS=1
export GCN_GX_SYNC=1
export GCN_XF_SYNC=1
unset LD_PRELOAD
exec "$ROOT/build-linux/cvs2eo" "$ROOT/game/disc.nkit.iso" --scale=3 --no-input-log --log=os "$@" >>logs/session.log 2>&1
