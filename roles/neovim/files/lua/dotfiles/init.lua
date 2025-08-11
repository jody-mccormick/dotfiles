-- Generic namespace adapter to existing modules
-- This module provides a stable 'dotfiles' namespace while reusing the
-- existing implementation under 'techdufus'.

local M = require('techdufus')

-- Preload common submodules so `require('dotfiles.*')` resolves correctly.
package.loaded['dotfiles'] = M
package.loaded['dotfiles.core'] = require('techdufus.core')
package.loaded['dotfiles.core.icons'] = require('techdufus.core.icons')
package.loaded['dotfiles.core.utils'] = require('techdufus.core.utils')

return M
