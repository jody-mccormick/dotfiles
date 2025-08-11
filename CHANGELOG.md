# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog, and this project adheres to Semantic Versioning when appropriate.

## [Unreleased]
- Polish visuals and repository metadata (description, topics, social preview).
- Optional: remove legacy `techdufus/` shim files after verification.
- Add pre-commit hooks and CI as needed.
- Run full validation on a fresh environment.

## [2025-08-11]
### Added
- New `docs/` content: QUICKSTART, TROUBLESHOOTING, EXAMPLES.
- Credits & Inspiration section in `README.md`.
- Neovim core modules under `roles/neovim/files/lua/dotfiles/core/`:
  - `init.lua`, `disable.lua`, `globals.lua`, `options.lua`, `keymaps.lua`, `autocommands.lua`, `utils.lua`.
- Telescope pickers under `roles/neovim/files/lua/dotfiles/telescope/pickers.lua`.

### Changed
- Rebranded repo to personal identity across README and scripts.
- Neovim Lua namespace migrated from `techdufus` to `dotfiles`.
- Updated plugin and entrypoints to `dotfiles` namespace.
- Parameterized Obsidian repo URL in Ansible role.
- Ansible SSH var naming generalized to `op.ssh.github.personal`.
- Dockerfile defaults set to user `jody`.

### Deprecated
- Legacy `roles/neovim/files/lua/techdufus/` modules now act as shims forwarding to `dotfiles`.

### Security
- Documentation and configuration centered on 1Password vault usage to avoid committing secrets.

