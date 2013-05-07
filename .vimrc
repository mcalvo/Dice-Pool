
"Syntax highlighting
syntax enable
syntax on

"Tab settings
set smarttab
filetype plugin indent on
set tabstop=4 softtabstop=4 shiftwidth=4 noexpandtab

"Macro Commands
" ca <Command I Type> <Command that Runs>
ca CT ConqueTerm
ca CTS ConqueTermSplit

" Key bindings

" Title settings (used by Screen)
let &titlestring = "" . expand("%:t") . ""
if &term == "screen"
   set t_ts=^[k
   set t_fs=^[\
endif
if &term == "screen" || &term == "xterm"
   set title
endif
let &titleold=" "
