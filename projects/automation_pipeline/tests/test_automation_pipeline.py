import pytest
import requests

import automation_pipeline as pipeline


def test_get_github_data_extracts_expected_fields(monkeypatch):
    class FakeResponse:
        def raise_for_status(self):
            return None

        def json(self):
            return {
                "current_user_url": "https://api.github.com/user",
                "repository_search_url": "https://api.github.com/search/repositories{?q}",
            }

    monkeypatch.setattr(pipeline.requests, "get", lambda *args, **kwargs: FakeResponse())

    data = pipeline.get_github_data()

    assert data["user_url"] == "https://api.github.com/user"
    assert "repository_search" in data


def test_get_github_data_propagates_request_errors(monkeypatch):
    def raise_error(*args, **kwargs):
        raise requests.RequestException("Network failure")

    monkeypatch.setattr(pipeline.requests, "get", raise_error)

    with pytest.raises(requests.RequestException):
        pipeline.get_github_data()


class FakeResponse:
    text = "Short summary"


class FakeModels:
    def generate_content(self, **kwargs):
        return FakeResponse()


class FakeClient:
    models = FakeModels()


def test_summarize_data_returns_ai_text():
    result = pipeline.summarize_data(FakeClient(), {"user_url": "example"})

    assert result == "Short summary"
