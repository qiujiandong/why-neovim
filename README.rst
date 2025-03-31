
=================================
Why Neovim - Documentation
=================================

.. image:: https://img.shields.io/badge/status-active-brightgreen
   :alt: Project Status
   :target: https://why-neovim.readthedocs.io/en/latest/

Welcome to the documentation repository for **Why Neovim**.  
This repository contains insights, experiences, and guides on using Neovim effectively.

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
    │   └── source/
    │       ├── conf.py         # Sphinx configuration
    │       ├── index.rst       # Documentation homepage
    │       ├── locale/         # Translation files
    │       ├── nvim/           # Neovim-related docs
    │       ├── overview.rst
    │       ├── quickstart.rst
    │       ├── shell/          # Shell-related docs
    │       └── tmux/           # Tmux-related docs
    ├── LICENSE.txt
    └── README.rst              # This file

🚀 **Build & Run Locally**
---------------------------------
If you want to preview the documentation locally, follow these steps:

1. Install dependencies:

   .. code-block:: sh

      cd /path/to/docs
      pip install -r requirements.txt

2. Build the documentation:

   .. code-block:: sh

      make html

   Then open ``build/index.html`` in your browser.

3. (Optional) Use live preview with `sphinx-autobuild`:

   .. code-block:: sh

      pip install sphinx-autobuild
      sphinx-autobuild source build/html

   Open `http://127.0.0.1:8000/` in your browser for live updates.

📜 **License**
---------------------------------
This documentation is released under the **Apache-2.0 License**.  
See `LICENSE <LICENSE.txt>`_ for details.
