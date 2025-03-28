install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv pip install --no-deps dist/*.whl

lint:
    uv run ruff check brain_games
	