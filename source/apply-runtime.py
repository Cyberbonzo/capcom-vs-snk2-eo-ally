"""Apply the tested frontend, ordered scanout and optional widescreen changes."""
from pathlib import Path
import subprocess
import hashlib
import tempfile
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
elif check("--reverse", "--check", "--exclude=runtime/hw/vi.cpp").returncode == 0:
    # Update an existing installation of the ordered-scanout patch.
    vi = upstream / "runtime/hw/vi.cpp"
    if hashlib.sha256(vi.read_text(encoding="utf-8").encode()).hexdigest() != "04e289ff850ef0f2fcf1c559b2e9d71d9a8ac68c38c340f581ac854356de1cf1":
        raise SystemExit("Unrecognized vi.cpp. Existing source preserved.")
    with tempfile.TemporaryDirectory() as tmp:
        relative = "runtime/hw/vi.cpp"
        updated = Path(tmp) / relative
        updated.parent.mkdir(parents=True)
        updated.write_bytes(subprocess.check_output(["git", "-C", str(upstream), "show", "HEAD:" + relative]))
        subprocess.run(["git", "apply", "--include=" + relative, str(patch)], cwd=tmp, check=True)
        vi.write_bytes(updated.read_bytes())
    print("Autosave update applied")
else:
    raise SystemExit("Runtime source does not match the pinned revision or the tested patch")
