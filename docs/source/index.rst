Why Neovim
===================================

Hi, everyone! I mainly work with C/C++/Python development, and I have been using `VS Code <https://code.visualstudio.com>`_ for a long time. I find VS Code very intuitive and convenient—it has a low entry barrier, is easy to get started with, and is powerful enough to meet most work requirements.

However, recently, I started using `Neovim <https://neovim.io>`_ and discovered that some of its features are extremely useful—some of which VS Code doesn't even natively support. Here, I’d like to share some of my experiences and explain "\ **Why Neovim**\ ".

As I was preparing to write these thoughts, `Neovim 0.11 <https://github.com/neovim/neovim/releases/tag/v0.11.0>`_ had just been released. I also took a look at the `roadmap <https://neovim.io/roadmap>`_ for the upcoming 0.12 version, which is being referred to as "\ **The year of Nvim OOTB**\ " (Out of the Box). Future versions of Neovim will become even more user-friendly and ready to use from the start. I believe that in the near future, Neovim will gain even more recognition and recommendations from developers.

About
-----

If you're interested in this document, please refer to :ref:`Overview <overview>` and :ref:`Quick Start <quick start>`

I'll begin by introducing Tmux. In my opinion, before diving into Neovim, it's essential to first familiarize with :ref:`Tmux <about tmux>`.

.. Note::

    Using Neovim without Tmux is like using VS Code without a Workspace.

Next, having a powerful shell can greatly enhance your workflow. I recommend using :ref:`Zsh <about shell>`.

Finally, I'll discuss :ref:`Neovim <kickstart>`, primarily in comparison with VS Code.

Contents
--------

.. toctree::
   :maxdepth: 2
   :caption: At a Glance

   overview
   quickstart

.. toctree::
   :maxdepth: 2
   :caption: Tmux

   tmux/about
   tmux/move_around
   tmux/save_context
   tmux/practice

.. toctree::
   :maxdepth: 2
   :caption: Shell

   shell/about
   shell/font
   shell/zsh

.. toctree::
   :maxdepth: 2
   :caption: Neovim

   nvim/kickstart
   nvim/move_around
   nvim/registers
   nvim/surround
   nvim/debug
   nvim/auto_im
   nvim/practice

