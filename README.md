# tellus-traveler-python

Unofficial Python client for [Tellus Traveler API](https://www.tellusxdp.com/docs/travelers/).

## Getting Started

https://tellus-traveler.readthedocs.io/

## Development

This project uses [Rye](https://rye-up.com/) for package management.

### Install dependencies

    $ rye sync

### Run the test suite

    $ rye run test

### Publish a new version

1. Bump the version in `pyproject.toml` and update `CHANGELOG.md`.
2. Create a git commit, push it, and ensure that the CI passes.
3. Create a git tag for the new version and push it, then the `PyPI / publish` job starts.
