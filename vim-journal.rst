
VIM Practice Journal
====================

Working On
----------

* buffer switching
* hjkl (no arrows)
* HTML formatting
* sorting
* paragraph navigation: { }
* w-e-b movements
* f t F T , ; movements
* ZZ - saves
* relative number
* spell checking
* g-movements
* 80 cols formatting - gq
* nerdcommenter: number <leader> cl | c<space> | cu
* nerdtree: IDE like file explorer
* neomake: run code linters; :lnext :lprev for navigating errors
* neoformat: automatically format code
* vim-unimpared: shortcut pairs like [l and ]l for :lprev and :lnext

Future
------

* (more) g-movements
* apply a macro to all lines: :%norm! @a
* tab groupings / tab switching
* vim slides ???
* Highlight groups: `so $VIMRUNTIME/syntax/hitest.vim`
* Plugins:
  * Plug 'jiangmiao/auto-pairs' : auto-finish quotes, parentheses


Drills
------

Drill 01 - Basics
"""""""""""""""""

Focuses on movements and other built-in vim staples.

* hjkl movement
* word movements / navigation (w, e, b, W, E, B)
* line movements - ^ $ 0
* screen line movements - g0 g$ gm
* paragraph movements - { }
* match movements - * #

Drill 02 - Comments
"""""""""""""""""""

Use nerdcommenter to comment and uncomment sections.

Drill 03 - Code linting and formatting
""""""""""""""""""""""""""""""""""""""

Use neomake to check code for stylistic and syntactic issues.
Use neoformat to correct style issues.

Drill 04 - Code navigation
""""""""""""""""""""""""""

Navigate to code definitions using jedi-vim.  Replace names and examine docs.

* <leader>g : goto assignment
* <leader>d : goto definition
* <leader>n : show usage in quickfix window
* <leader>r : rename

Drill 05 - window (aka split) management
""""""""""""""""""""""""""""""""""""""""

* set winfixheight
* Create new splits
* Close split with <C-w> c
*

Drill 06 - macros
"""""""""""""""""

* Create a macro and apply it to all lines `:%norm! @a`



Old Practices
-------------

* Leader mappings for switching buffers
* "z" - positioning (center, top, bottom)
* :colorscheme CTRL-D for color scheme list.
