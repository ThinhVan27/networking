# Changelog
## 2025-10-14
### Added
- `daemon/backend.py`: Add multi-thread handling client request
- Implement `build_content(self, path, base_dir)`, Build basic header for response `build_response_header(self, request)` at `daemon/response.py` (fetch the object to file in raw byte then return)
- 
- Add some comment for clear docs at `daemon/proxy.py` `daemon/request.py`
### Changed
- Updated `daemon/httpadapter.py` to use the head and body from `req` not the dummy `bksysnet` and `get in touch`
- Improved error handling in `daemon/proxy.py`.

### Fixed
- The for loop in `parse_virtual_hosts` is wrong, the `proxy_map = {}` init should be outside the loop
