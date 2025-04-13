Quick Start
===========

这一页主要对我想分享的内容做一个简要的介绍。

Tmux
----

详细了解 :ref:`Tmux <about tmux>`

* 关于Tmux的文档： `Tmux Wiki <https://github.com/tmux/tmux/wiki>`_ ;
* 了解Tmux中 `session`, `window` 和 `pane` 的概念;
* 把 `<prefix>` 从默认的 `<Ctrl+b>` 改成 `<Ctrl+a>` 会更方便;
* `<prefix> + hjkl` 实现不同 `pane` 之间的移动;
* `<prefix> + |` / `<prefix> + _` 实现垂直/水平分割 `pane` ;
* `<prefix> + x` 关闭当前 `pane` ;
* `<prefix> + [` / `<prefix> + ]` 实现 `window` 之间的切换;
* `<prefix> + Ctrl-s` 保存当前的 `session` ;
* `<prefix> + Ctrl-r` 加载之前保存的 `session` ;
* `<prefix> + r` 重命名当前的 `window` ;
* `<prefix> + R` 重命名当前的 `session` ;

Shell
-----

1. 安装 `subframe7536/maple-font <https://github.com/subframe7536/Maple-font>`_ 字体;
2. 安装 `zsh` 和 `oh-my-zsh` ，`安装步骤 <https://github.com/ohmyzsh/ohmyzsh/wiki/Installing-ZSH>`_ ;
3. 安装 `zsh-users/zsh-autosuggestions <https://github.com/zsh-users/zsh-autosuggestions>`_ 插件;
4. 安装 `zsh-users/zsh-syntax-highlighting <https://github.com/zsh-users/zsh-syntax-highlighting>`_ 插件;
5. 安装 `romkatv/powerlevel10k <https://github.com/romkatv/powerlevel10k>`_ zsh 主题;

Neovim
------

* 了解 Neovim 中的 `session`, `tab`, `window`, `buffer` 的概念;
* 从 `nvim-lua/kickstart.nvim <https://github.com/nvim-lua/kickstart.nvim>`_ 开始，学习使用 `lazy.nvim <https://github.com/folke/lazy.nvim>`_ 管理插件;
* 利用 `smoka7/hop.nvim <https://github.com/smoka7/hop.nvim>`_ 在 `buffer` 中移动;
* 利用 `akinsho/bufferline.nvim <https://github.com/akinsho/bufferline.nvim>`_ 快速切换 `buffer`;
* 利用 `nvim-neo-tree/neo-tree.nvim <https://github.com/nvim-neo-tree/neo-tree.nvim>`_ 实现文件管理;
* 利用 `nvim-telescope/telescope.nvim <https://github.com/nvim-telescope/telescope.nvim>`_ 实现各种搜索;
* 利用 `numToStr/Comment.nvim <https://github.com/numToStr/Comment.nvim>`_ 快速注释;
* 利用 `neovim/nvim-lspconfig <https://github.com/neovim/nvim-lspconfig>`_ 管理LSP服务;
* 利用 `williamboman/mason.nvim <https://github.com/williamboman/mason.nvim>`_ 管理常用的package;
* 利用 `olimorris/persisted.nvim <https://github.com/olimorris/persisted.nvim>`_ 保存和加载 Neovim 的 `session` ;
* 利用 `nvimdev/dashboard <https://github.com/glepnir/dashboard-nvim>`_ 自定义 dashbooard
* 利用 `gitsigns.nvim <https://github.com/lewis6991/gitsigns.nvim>`_, `diffview.nvim <https://github.com/sindrets/diffview.nvim>`_, `lazygit.nvim <https://github.com/kdheepak/lazygit.nvim>`_ 等插件实现git版本管理;
* 利用 `mfussenegger/nvim-dap <https://github.com/mfussenegger/nvim-dap>`_ 实现C/C++, Python, Nvim插件调试;
* TODO AI编程助手

.. list-table:: Neovim v.s. VS Code
   :widths: 10 25 10
   :header-rows: 1

   * - VS Code
     - Neovim
     - 参考

   * - Workspace
     - `persisted.nvim <https://github.com/olimorris/persisted.nvim>`_
     - :ref:`工作区 <workspace>`
