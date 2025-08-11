local M = {}

-- Return true if there are words before the cursor position
function M.has_words_before()
  local unpack = unpack or table.unpack
  local line, col = unpack(vim.api.nvim_win_get_cursor(0))
  if col == 0 then return false end
  local text = vim.api.nvim_buf_get_lines(0, line - 1, line, true)[1]
  return text:sub(col, col):match("%s") == nil
end

-- Shim to mirror luasnip's jumpable convenience used in mappings
function M.jumpable(dir)
  local ok, luasnip = pcall(require, 'luasnip')
  if not ok then return false end
  return luasnip.jumpable(dir)
end

return M
