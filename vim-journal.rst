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
* vim-unimpaired: shortcut pairs like [l and ]l for :lprev and :lnext
* folding: set foldmethod=indent zM zR ...
* fzf
* CTRL-W o ; Only this window
* CTRL-W f ; Open window with file under cursor.
* fugitive
* Reverse lines.  See :help 12.4
* Insert at beginning or end of line with I and A

Future
------

* (more) g-movements
* apply a macro to all lines: :%norm! @a
* tab groupings / tab switching
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

See drill_01.rst

Drill 02 - Comments
"""""""""""""""""""

Use nerdcommenter to comment and uncomment sections.

See drill_02.py

Drill 03 - Code linting and formatting
""""""""""""""""""""""""""""""""""""""

Use neomake to check code for stylistic and syntactic issues.
Use neoformat to correct style issues.

See drill_03.py

Drill 04 - Code navigation
""""""""""""""""""""""""""

Navigate to code definitions using jedi-vim.  Replace names and examine docs.

* <leader>g : goto assignment
* <leader>d : goto definition
* <leader>n : show usage in quickfix window
* <leader>r : rename
* [[ ]] [m ]m for function and method navigation.

See drill_04.py

Drill 05 - Reverse a list
"""""""""""""""""""""""""

See drill_05.rst

Drill 06 - window (aka split) management
""""""""""""""""""""""""""""""""""""""""

* set winfixheight
* Create new splits
* Close split with <C-w> c
* Close all splits except current with :only
* Move current window to top, bottom, left, right with CTRL-W J K H L
* Close all splits except this one: CTRL-w o (only this one).
* Maximize windows horizontally and vertically: CTRL-W _ and CTRL-W |

Drill 07 - macros
"""""""""""""""""

* Create a macro and apply it to all lines `:%norm! @a`

Drill 08 - folding
""""""""""""""""""

* Practice folding and unfolding.
* set foldmethod=indent
* set foldnestmax=1
* zj, zk navigation
* zo, ZO, zc, ZC, zr, zR, zm, zM



Old Practices
-------------

* Leader mappings for switching buffers
* "z" - positioning (center, top, bottom)
* :colorscheme CTRL-D for color scheme list.

