import os
import random

import pytest

from tests.pages.taiga_login_page import TaigaLoginPage
from tests.pages.taiga_project_page import TaigaProjectPage
from tests.pages.taiga_session import TaigaSession

TAIGA_BASE_URL: str | None = None  # e.g. "https://tree.taiga.io" or "https://taiga.mycompany.com"
TAIGA_TOKEN: str | None = None  # Personal auth token (same one used for API)
TAIGA_PROJECT_SLUG: str | None = None  # e.g. "myproject" (optional, needed for project flow)


def _get_env(name: str) -> str | None:
    val = os.getenv(name)
    if val is None:
        return None
    val = val.strip()
    return val or None


def _require_taiga_env():
    base_url = _get_env("TAIGA_BASE_URL") or TAIGA_BASE_URL
    token = _get_env("TAIGA_TOKEN") or TAIGA_TOKEN

    if not (base_url and token):
        pytest.skip(
            "Taiga config is not set. Fill TAIGA_BASE_URL/TAIGA_TOKEN in this file, "
            "or provide TAIGA_BASE_URL/TAIGA_TOKEN via env vars."
        )

    return base_url, token


class TestTaigaFlows:
    def test_taiga_login(self, browser):
        base_url, token = _require_taiga_env()

        TaigaSession.login_with_token(browser, base_url, token)
        TaigaLoginPage(browser, base_url).wait_logged_in()

        assert True

    def test_taiga_create_user_story_in_project(self, browser):
        base_url, token = _require_taiga_env()
        project_slug = _get_env("TAIGA_PROJECT_SLUG") or TAIGA_PROJECT_SLUG
        if not project_slug:
            pytest.skip(
                "Taiga project slug is not set. Fill TAIGA_PROJECT_SLUG in this file, "
                "or provide TAIGA_PROJECT_SLUG via env var."
            )

        TaigaSession.login_with_token(browser, base_url, token)
        TaigaLoginPage(browser, base_url).wait_logged_in()

        project = TaigaProjectPage(browser, base_url, project_slug)
        project.open()
        project.open_backlog()

        title = f"autotest-us-{random.randint(1, 1_000_000)}"
        project.create_user_story(title)

        assert project.has_title(title)

