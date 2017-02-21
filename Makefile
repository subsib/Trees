#########################
# Makefile              #
#                       #
# Arabella Brayer       #
# 22 feb 2017           #
#                       #
#########################

all: export tests

export:
		export PYTHONPATH=/home/arabella/Documents/progra_perso/Trees/tests/

tests: tests/Test__BinaryTree.py
		python3 tests/Test__BinaryTree.py

# TODO fix this awful makefile.