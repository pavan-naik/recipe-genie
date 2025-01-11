import pytest
from unittest.mock import Mock, patch
from src.app import generate_recipe, setup_pipeline


@pytest.fixture
def mock_pipeline():
    with patch("src.app.pipeline") as mock:
        mock_generator = Mock()
        mock_generator.return_value = [{"generated_text": "Test recipe output"}]
        mock.return_value = mock_generator
        yield mock


def test_empty_input():
    result = generate_recipe("")
    assert "Please enter a dish name" in result


def test_generate_recipe_success(mock_pipeline):
    result = generate_recipe("Pasta")
    assert isinstance(result, str)
    assert "Pasta" in result


def test_generate_recipe_exception():
    with patch("src.app.generator", side_effect=Exception("Test error")):
        result = generate_recipe("Pasta")
        assert "Error:" in result


def test_pipeline_creation():
    with patch("src.app.pipeline") as mock_pipeline:
        setup_pipeline()
        mock_pipeline.assert_called_once_with(
            "text-generation", model="meta-llama/Llama-3.2-1B-instruct", device=-1
        )
