#!/usr/bin/env python3
"""Imprime los campos de resource pack de server.properties.

Usa el zip de servidor de la release mas reciente. Ignora
Dreamers-Resourcepack.zip, que es el pack simple de sonidos.
"""

import hashlib
import json
import sys
import uuid
import urllib.error
import urllib.request

REPO = "JosFlix7/Dreamers-Resourcepack"
IGNORED_ASSET = "Dreamers-Resourcepack.zip"
LATEST_RELEASE = f"https://api.github.com/repos/{REPO}/releases/latest"


def fetch(url: str) -> bytes:
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "dreamers-resourcepack",
        },
    )
    with urllib.request.urlopen(request) as response:
        return response.read()


def server_zip(assets: list[dict]) -> dict:
    chosen = [
        asset
        for asset in assets
        if asset["name"].lower().endswith(".zip")
        and asset["name"].lower() != IGNORED_ASSET.lower()
    ]
    if len(chosen) == 1:
        return chosen[0]

    names = ", ".join(asset["name"] for asset in assets) or "(ninguno)"
    raise SystemExit(
        f"La release debe traer un zip ademas de {IGNORED_ASSET}. Assets: {names}"
    )


def main() -> None:
    try:
        release = json.loads(fetch(LATEST_RELEASE))
    except urllib.error.HTTPError as error:
        raise SystemExit(f"No se pudo leer la release: {error.code}") from error

    asset = server_zip(release.get("assets", []))
    url = asset["browser_download_url"]
    name = asset["name"]
    data = fetch(url)
    sha1 = hashlib.sha1(data).hexdigest()
    pack_id = uuid.uuid5(uuid.NAMESPACE_URL, name)

    print(f"Release {release['tag_name']}: {name}", file=sys.stderr)
    print(f"resource-pack={url}")
    print(f"resource-pack-sha1={sha1}")
    print(f"resource-pack-id={pack_id}")


def pause() -> None:
    if sys.stdin is None or not sys.stdin.isatty():
        return
    try:
        input("\nPresiona Enter para cerrar.")
    except EOFError:
        pass


if __name__ == "__main__":
    try:
        main()
    finally:
        pause()
