-- Adapter for telescope pickers under generic 'dotfiles' namespace
local M = require('techdufus.telescope.pickers')

-- Ensure both namespaces resolve to the same module
package.loaded['dotfiles.telescope.pickers'] = M

return M
