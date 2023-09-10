# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.3.0] - 2023-09-11

### Added

- Add `dataset_terms_url()` and `dataset_manual_url()` functions.
- Add `File.url()`, `File.download()`, and `Scene.download_all_files()` functions.
- Add `api.scene_file_url()` and `api.scene_thumbnail_url()` functions
- Add `api.scene_files()` and `api.scene_thumbnails()` functions.
- Add `scene()` function.
- Add "Getting Started" page to documentation.

### Fixed

- Fix HTTP status 422 error of `search()`.

### Changed

- Improve the module structure.

## [0.2.0] - 2023-09-10

### Added

- Add `search()` function.
- Add `datasets()` and `dataset(id)` functions.
- Add the documentation pages built by `mkdocs`.

## [0.1.0] - 2023-09-09

- Initial release

[unreleased]: https://github.com/sankichi92/tellus-traveler-python/compare/v0.3.0...HEAD
[0.3.0]: https://github.com/olivierlacan/keep-a-changelog/compare/v0.1.0...v0.3.0
[0.2.0]: https://github.com/olivierlacan/keep-a-changelog/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/sankichi92/tellus-traveler-python/releases/tag/v0.1.0
