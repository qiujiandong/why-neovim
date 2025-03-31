=================================
Documentation about Why Neovim
=================================

.. image:: https://img.shields.io/badge/status-active-brightgreen
   :alt: Project Status
   :target: https://why-neovim.readthedocs.io/en/latest/

Welcome to the documentation repository for **Why Neovim**. This repository contains some of my experience about Neovim.

📖 **Read Online**: `Why Neovim <https://why-neovim.readthedocs.io/en/latest/>`_

📂 **Repository Structure**
---------------------------------
The documentation is organized as follows:

.. code-block:: text

    root/
    ├── docs/
    │   ├── make.bat
    │   ├── Makefile
    │   ├── requirements.txt
    │   └── source
    │       ├── conf.py         # Sphinx configuration
    │       ├── index.rst       # Documentation homepage
    │       ├── locale/         # translation
    │       ├── nvim/           # documentation about nvim
    │       ├── overview.rst
    │       ├── quickstart.rst
    │       ├── shell/          # documentation about shell
    │       └── tmux/           # documentation about tmux
    ├── LICENSE.txt
    └── README.rst              # this file

🚀 **Build & Run Locally**
---------------------------------
If you want to preview the documentation locally, you can use `Sphinx`:

.. code-block:: sh

    cd /path/to/docs
    pip install -r requirements.txt
    make html

Then open ``build/index.html`` in your browser.

📜 **License**
---------------------------------
This documentation is released under the Apache-2.0 License. See `LICENSE <LICENSE.txt>`_ for details.
