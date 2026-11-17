"""Apply the tested frontend, ordered scanout and optional widescreen changes."""
from pathlib import Path
import subprocess
root = Path(__file__).resolve().parents[1]
upstream = root / "upstream/gcn-recomp"
patch = root / "source/runtime.patch"
def check(*args):
    return subprocess.run(["git", "-C", str(upstream), "apply", *args, str(patch)],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if check("--reverse", "--check").returncode == 0:
    print("Runtime changes already applied")
elif check("--check").returncode == 0:
    subprocess.run(["git", "-C", str(upstream), "apply", str(patch)], check=True)
    print("Runtime changes applied")
else:
    raise SystemExit("Runtime source does not match the pinned revision or the tested patch")
