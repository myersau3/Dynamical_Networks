test:
	pytest -v .\dynamical_networks\test\test_statistics.py
	pytest -v .\dynamical_networks\test\test_evolutionary_homology.py
lint:
	pylint -rn dynamical_networks\simulate
	pylint -rn dynamical_networks\analysis
	pylint -rn dynamical_networks\test