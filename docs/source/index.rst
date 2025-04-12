Why Neovim
==========

大家好，我是一名普通的软件开发工程师，我平时的工作偏嵌入式开发，
主要的开发语言是C/C++/python。
在接触 `Neovim <https://neovim.io>`_ 之前我一直使用 `VS Code <https://code.visualstudio.com>`_，
VS Code非常直观易用，又有丰富的插件，已经能够满足我所有的工作需求了。

但在使用鼠标的过程中，我总会不自觉地耸肩，长期下来导致我的右侧肩膀异常酸痛😣。
我想如果能减少使用鼠标的频率，那么肩膀酸痛的问题应该也能得到缓解。
这也是我开始考虑使用Neovim的最直接原因。
VS Code里虽然也有很多键盘快捷键可以设置，
但是我感觉基于Neovim的键盘操作更纯粹，体验更好。

在刚开始使用Neovim的这段时间里，Neovim/Vim的某些特性有种令人“眼前一亮”的感觉，
这种新奇的体验能让人深切地体会到Vim灵活而又强大的设计哲学。
因此我希望能通过这篇文档来分享一些Neovim的使用体会，以及解释“ **Why Neovim** ”。

我觉得Neovim相较于其它一众现代的编辑器虽然没有绝对碾压的优势，但它还是能够占有一席之地的。
准备开始写这片文档的时候，正值 `Neovim 0.11 <https://github.com/neovim/neovim/releases/tag/v0.11.0>`_ 版本发布。
我顺便看了一下0.12版本的 `更新计划 <https://neovim.io/roadmap>`_ ，0.12+版本会变得更加开箱即用。
相信Neovim在不久的将来会受到更多开发者的欢迎和推荐。

About
-----

如果你对这个文档感兴趣，请查阅：:ref:`概述 <overview>` 和 :ref:`快速入门 <quick start>`。

我会先从 :ref:`Tmux <about tmux>` 开始介绍，
强烈建议在使用 Neovim 前先了解 Tmux。

接着，一个好用的shell可以显著提高工作效率，我推荐使用 :ref:`Zsh <about shell>`。

最后，结合使用VS Code与Neovim的使用体验来介绍 :ref:`Neovim <kickstart>`。

Contents
--------

.. toctree::
   :maxdepth: 2
   :caption: 速览

   overview
   quickstart

.. toctree::
   :maxdepth: 1
   :caption: Tmux

   tmux/about
   tmux/move_around
   tmux/save_context
   tmux/practice

.. toctree::
   :maxdepth: 1
   :caption: Shell

   shell/about
   shell/font
   shell/zsh

.. toctree::
   :maxdepth: 1
   :caption: Neovim

   nvim/kickstart
   nvim/move_around
   nvim/registers
   nvim/surround
   nvim/debug
   nvim/auto_im
   nvim/practice

