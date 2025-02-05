"""Github stars count for the reflex repository."""

import asyncio
import httpx

import reflex as rx
import contextlib

GITHUB_API_URL = "https://api.github.com/repos/reflex-dev/reflex"


def get_stars_on_build():
    """Fetch the stars when app is built as default"""
    resp = httpx.get(GITHUB_API_URL)
    resp.raise_for_status()
    data = resp.json()
    return int(data.get("stargazers_count", 21000))


REFLEX_STAR_COUNT = get_stars_on_build()


async def fetch_count():
    """Fetch the stars count of the reflex repository."""
    try:
        while True:
            with contextlib.suppress(Exception):
                global REFLEX_STAR_COUNT
                data = httpx.get(GITHUB_API_URL).json()
                REFLEX_STAR_COUNT = int(data["stargazers_count"])
            await asyncio.sleep(3600)
    except asyncio.CancelledError:
        pass


class GithubStarState(rx.State):
    @rx.var(cache=True, interval=60)
    def stars(self) -> str:
        return f"{REFLEX_STAR_COUNT}"

    @rx.var(cache=True, interval=60)
    def stars_short(self) -> str:
        return f"{round(REFLEX_STAR_COUNT/1000)}K"
