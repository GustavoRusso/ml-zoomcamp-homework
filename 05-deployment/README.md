# ML Zoomcamp 2026 deployment release

This directory contains the frozen lead-scoring artifact used by Homework 5
and Homework 10. It is trained from
`cohorts/2026/data/course_lead_scoring_2026.csv`, not from a prior cohort's
dataset.

The API accepts the eight observable fields in the release. Missing numeric
values are replaced with medians calculated from the training CSV and recorded
in `feature_defaults.json`; missing categories use `NA`.

## DevContainer vs this homework’s Docker image

The [repo DevContainer](../README.md) is for developing the whole course (IDE,
Jupyter, root dependencies). It is **not** the image you ship for this
homework.

This folder’s [`Dockerfile`](Dockerfile) is a **service image**: a slim,
digest-pinned Python 3.11 runtime that installs from the checked-in lockfile,
copies only the API and model files, and starts `uvicorn` on port 9696. Use
that image when you want a self-contained prediction service (Homework 10
style). Use the DevContainer (or any host with `uv`) when you are editing and
testing the code.

This project pins **Python 3.11**. Prefer this folder’s own `uv sync --locked`
and `.venv` over the course root `.venv` (Python 3.12) so local runs match the
service image.

## Local run

From this directory (inside the course DevContainer or any environment with
`uv`):

```bash
uv sync --locked
uv run python smoke_test.py
uv run uvicorn predict:app --host 0.0.0.0 --port 9696
```

In another terminal:

```bash
python q6_test.py
```

## Container run

Build and run the deployment service image (not the DevContainer):

```bash
docker build -t zoomcamp-model:2026-hw10 .
docker run --rm -p 9696:9696 zoomcamp-model:2026-hw10
```

The API exposes `GET /health` and `POST /predict`. The model artifact is
addressed by its checksum in `model_metadata.json`; the API health response
also reports the feature-default checksum. The Dockerfile pins the Python and
uv image digests and installs from the checked-in lockfile.
