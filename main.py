#!/usr/bin/env python3
"""Entry program for "Sum up 22 November's world news in one image".

The finished front page ships in this repository as ``entry.png``.
Running this program validates that file and then installs it as
``entry.png`` inside the output directory:

* the output directory is ``$MAKEFUN_OUTPUT_DIR`` when that variable
  is set (handy for local runs) and ``/output`` otherwise;
* the write goes through a temporary sibling file and an atomic
  rename, so a grader that inspects the directory never sees a
  half-copied image;
* before and after copying, the image is checked against the
  competition's limits (PNG format, at most 1024x1024 pixels, at
  most 1 MiB), and any problem aborts the run with a clear message
  instead of silently shipping a broken entry.

The grader runs the program twice with no network access; copying a
fixed, validated file makes both runs produce exactly the same
bytes. Python 3.13, standard library only.
"""

import hashlib
import os
import shutil
import struct
import sys
from pathlib import Path

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
MAX_IMAGE_BYTES = 1024 * 1024
MAX_IMAGE_SIDE = 1024
OUTPUT_NAME = "entry.png"


def png_dimensions(path: Path) -> tuple[int, int]:
    """Return the (width, height) stored in a PNG file's IHDR chunk.

    Only the first 24 bytes are needed: the 8-byte signature, the
    IHDR chunk length and type, then width and height as big-endian
    unsigned 32-bit integers. Anything else means the file is not
    the PNG it claims to be, which is reported as a ValueError.
    """
    with path.open("rb") as handle:
        header = handle.read(24)
    if len(header) < 24 or not header.startswith(PNG_SIGNATURE):
        raise ValueError(f"{path} does not start with a PNG signature")
    if header[12:16] != b"IHDR":
        raise ValueError(f"{path} has no IHDR chunk where one belongs")
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def check_image(path: Path) -> None:
    """Raise ValueError if *path* breaks any of the entry limits."""
    size = path.stat().st_size
    if size > MAX_IMAGE_BYTES:
        raise ValueError(f"{path} is {size} bytes, over the 1 MiB cap")
    width, height = png_dimensions(path)
    if width == 0 or height == 0:
        raise ValueError(f"{path} reports a zero-sized dimension")
    if width > MAX_IMAGE_SIDE or height > MAX_IMAGE_SIDE:
        raise ValueError(
            f"{path} is {width}x{height}, over the 1024x1024 cap"
        )


def digest(path: Path) -> str:
    """SHA-256 of a file, read in chunks so big files stay cheap."""
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def install(source: Path, out_dir: Path) -> Path:
    """Copy *source* into *out_dir* atomically and return the target.

    The temporary file lives in the same directory as the target so
    that ``os.replace`` is a rename within one filesystem. The final
    file is made readable by everyone (mode 0644) and its digest is
    compared with the source, so a truncated copy cannot slip past.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / OUTPUT_NAME
    temporary = out_dir / (OUTPUT_NAME + ".tmp")
    shutil.copyfile(source, temporary)
    os.replace(temporary, target)
    os.chmod(target, 0o644)
    if digest(target) != digest(source):
        raise ValueError("the copied image does not match the original")
    return target


def main() -> int:
    # A predictable umask keeps the output readable however the
    # sandbox happened to start this process.
    os.umask(0o022)
    source = Path(__file__).resolve().parent / OUTPUT_NAME
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    try:
        check_image(source)
        target = install(source, out_dir)
        check_image(target)
    except (OSError, ValueError) as error:
        print(f"entry failed: {error}", file=sys.stderr)
        return 1
    print(f"wrote {target} ({target.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
