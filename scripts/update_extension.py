#!/usr/bin/env python3
"""Fetch and archive a Chrome Web Store extension package."""

from __future__ import annotations

import hashlib
import io
import os
import shutil
import sys
import urllib.request
import zipfile
from pathlib import Path
from xml.etree import ElementTree


EXTENSION_ID = "hehggadaopoacecdllhhajmbjkdcmajg"
PROD_VERSION = "131.0"
ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
STATE = ROOT / "state" / "version.txt"
UPDATE_URL = (
    "https://clients2.google.com/service/update2/crx?"
    f"response=updatecheck&prodversion={PROD_VERSION}&acceptformat=crx2,crx3&"
    f"x=id%3D{EXTENSION_ID}%26uc"
)


def fetch_update() -> tuple[str, str]:
    request = urllib.request.Request(UPDATE_URL, headers={"User-Agent": "Chrome"})
    with urllib.request.urlopen(request, timeout=60) as response:
        xml = response.read()
    root = ElementTree.fromstring(xml)
    # The response uses a default XML namespace, so match by local name.
    check = next((element for element in root.iter() if element.tag.rsplit("}", 1)[-1] == "updatecheck"), None)
    if check is None or check.get("status") != "ok":
        raise RuntimeError(f"Chrome update service returned no package: {xml[:500]!r}")
    version = check.get("version")
    codebase = check.get("codebase")
    if not version or not codebase:
        raise RuntimeError("Update response did not contain version/codebase")
    return version, codebase


def extract_crx(data: bytes, destination: Path) -> None:
    # CRX2/CRX3 contain a ZIP archive after a small binary header.
    offset = data.find(b"PK\x03\x04")
    if offset < 0:
        raise RuntimeError("Downloaded file does not contain a ZIP payload")
    destination.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(io.BytesIO(data[offset:])) as archive:
        for member in archive.infolist():
            target = (destination / member.filename).resolve()
            if destination.resolve() not in target.parents and target != destination.resolve():
                raise RuntimeError(f"Unsafe ZIP member path: {member.filename!r}")
            archive.extract(member, destination)


def main() -> int:
    version, codebase = fetch_update()
    previous = STATE.read_text().strip() if STATE.exists() else "0.0.0"
    changed = version != previous
    print(f"Latest version: {version} (previous: {previous})")

    if changed or not (DIST / "chatgpt-extension.crx").exists():
        if DIST.exists():
            shutil.rmtree(DIST)
        DIST.mkdir(parents=True)
        request = urllib.request.Request(codebase, headers={"User-Agent": "Chrome"})
        with urllib.request.urlopen(request, timeout=120) as response:
            package = response.read()
        (DIST / "chatgpt-extension.crx").write_bytes(package)
        extract_crx(package, DIST / "unpacked")
        with zipfile.ZipFile(DIST / "chatgpt-extension.zip", "w", zipfile.ZIP_DEFLATED) as archive:
            for path in (DIST / "unpacked").rglob("*"):
                if path.is_file():
                    archive.write(path, path.relative_to(DIST / "unpacked"))
        digest = hashlib.sha256(package).hexdigest()
        (DIST / "SHA256SUMS").write_text(f"{digest}  chatgpt-extension.crx\n")
        STATE.parent.mkdir(parents=True, exist_ok=True)
        STATE.write_text(version + "\n")

    output = os.environ.get("GITHUB_OUTPUT")
    if output:
        with open(output, "a", encoding="utf-8") as handle:
            handle.write(f"version={version}\nchanged={'true' if changed else 'false'}\n")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(1)
