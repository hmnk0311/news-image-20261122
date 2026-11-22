#!/usr/bin/env python3
"""Entry program for the make.fun contest "Sum up 22 November's world
news in one image" (news-image-20261122).

The repository holds the finished front-page image as ``entry.png``
beside this file. The grader runs this program twice in a sandbox with
no network; each run copies the image to ``/output/entry.png`` (or to
``$MAKEFUN_OUTPUT_DIR/entry.png`` when that variable is set, which is
how it is run locally). Copying a fixed file makes the two runs write
exactly the same bytes.

Python 3.13, standard library only.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    # Use a predictable umask so the written file ends up readable by
    # everyone (mode 0644) however the sandbox started this process.
    os.umask(0o022)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    source = Path(__file__).resolve().parent / "entry.png"
    target = out_dir / "entry.png"
    shutil.copyfile(source, target)
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
