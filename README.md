# ML Zoomcamp homework

Workspace for ML Zoomcamp homework. The recommended way to work on the course is the **DevContainer**: a ready-made development environment so you do not need to install Python or course dependencies on the host.

## DevContainer (course-wide)

Configuration lives in [`.devcontainer/`](.devcontainer/):

- [`devcontainer.json`](.devcontainer/devcontainer.json) — VS Code / Cursor settings, extensions, and post-create setup
- [`Dockerfile`](.devcontainer/Dockerfile) — Python 3.12 base image with [`uv`](https://docs.astral.sh/uv/) installed

### Open the workspace

1. Open this repository in Cursor or VS Code with the Dev Containers extension.
2. Choose **Reopen in Container** (or **Open in Container** when prompted).
3. On first create, the container runs `uv sync` against the root [`pyproject.toml`](pyproject.toml). That installs Jupyter, NumPy, pandas, scikit-learn, and the other course dependencies into `.venv/`.

The editor is configured to use `${workspaceFolder}/.venv/bin/python`. Port **8888** is forwarded for Jupyter.

### Day-to-day use

- Edit notebooks and scripts inside the container.
- Run tools with `uv run …` or activate / select the root `.venv`.
- You can work on any homework folder from this same environment.

### Homework-specific packaging

Some homework folders ship their own dependencies and Docker setup. That is separate from the DevContainer:

| | DevContainer | Homework service image (e.g. deployment) |
|--|--------------|------------------------------------------|
| Purpose | Develop the whole course | Run one packaged API / service |
| Who uses it | You in the IDE | You, graders, or production via `docker run` |
| Lifetime | Long-lived workspace | Process that serves HTTP |

See [05-deployment/README.md](05-deployment/README.md) for how that homework uses a slim service Dockerfile alongside local `uv` runs.

### Python versions

The course DevContainer uses **Python 3.12**. The deployment homework pins **Python 3.11**. When working under `05-deployment/`, use that folder’s own `uv sync` / `.venv` (and its lockfile) so you match the service image rather than relying only on the root course environment.
