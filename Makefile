.PHONY: \*

PYTHON_EXEC := python3.9

PROJECT_NAME := project_template


setup_env:
	poetry env use $(PYTHON_EXEC)
	poetry install --with notebooks
	poetry run pre-commit install
	@echo
	@echo "Virtual environment has been created."
	@echo "Path to Python executable:"
	@echo `poetry env info -p`/bin/python


jupyterlab_start:
	# These lines ensure that CTRL+B can be used to jump to definitions in
	# code of installed modules.
	# Explained here: https://github.com/jupyter-lsp/jupyterlab-lsp/blob/39ee7d93f98d22e866bf65a80f1050d67d7cb504/README.md?plain=1#L175
	ln -s / .lsp_symlink || true  # Create if does not exist.
	jupyter nbextension enable --py --sys-prefix widgetsnbextension
	jupyter lab --ContentsManager.allow_hidden=True


run_training:
	poetry run $(PYTHON_EXEC) -m src.train
