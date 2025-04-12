Overview
========

Pros and Cons
-------------

Neovim的优点和缺点和Vim是类似的。

.. rubric:: 优点

* 轻量
* 全键盘工作流
* 高度可配置

.. rubric:: 缺点

* 学习曲线陡峭

可能对大部分人来说，平时的开发工作本身就已经很辛苦了，
实在没有额外的精力用来学习Neovim。能够开箱即用的VS Code难道不好吗？

确实如此，万事开头难。但我希望能够通过这个文档帮助更多人降低学习的门槛，更快地感受到Neovim/Vim的魅力所在。


Why Tmux
--------

Tmux是一个终端复用器（Terminal Multiplexer）。
Neovim是一个终端内的编辑器，学习使用Tmux有几个考虑：

1. 编辑文件的时候，常常需要切换到不同的目录。
2. 编辑文件后，常常需要运行一些终端命令。
3. Tmux和Neovim的快捷键设置需要一起考虑，避免冲突。

Tmux与Neovim配合使用可以让你的工作流变得更加灵活，更加高效。

Tmux的配置一般来说也是比较繁琐的，但好在有很多开源的配置可以参考。
我参考了 samoshkin 的 `tmux-config <https://github.com/samoshkin/tmux-config>`_ 配置，
基本上也能做到让Tmux开箱即用。

我的Tmux配置：`qiujiandong/tmux-config <https://github.com/qiujiandong/tmux-config>`_

Neovim Kickstart
----------------

入门Neovim最简单的方法是参考网上已有的配置。
Github上有很多人分享自己的Neovim配置，一般用的人越多，配置越经得起考验。
我是通过 `kikstart.nvim <https://github.com/nvim-lua/kickstart.nvim>`_ 入门的。

`TJ DeVries <https://github.com/tjdevries>`_ 甚至在Youtube上有一个视频介绍这个配置，
对于刚入门的我来说是相当友好了！

我的Neovim配置：`qiujiandong/kickstart.nvim <https://github.com/qiujiandong/kickstart.nvim/tree/dev>`_

.. youtube:: m8C0Cq9Uv9o
   :width: 560
   :height: 315
   :align: center

