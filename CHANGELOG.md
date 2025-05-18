## [v1.2.0] - 2025-05-18

### Added
- Support for module usage: import functions like `validate_path`, `get_url_ctn`, `extract_emails`.
- New `print_emails()` function for better CLI output display.
- Display emails in numbered, clean format.
- Added `-v` / `--version` CLI option to display the current version.
- Added `__all__` in `__init__.py` to support module import: `from mailgrab import ...`.
- `--version` flag to show current version.

### Changed
- CLI argument parser now mutually exclusive for `--url` and `--file`.
- Internal error handling improved using mailgrab exception (MailgrabError).
- Bumped version to 1.2.0 in `__version__.py`.

