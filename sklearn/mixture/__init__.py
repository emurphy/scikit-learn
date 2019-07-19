"""
The :mod:`sklearn.mixture` module implements mixture modeling algorithms.
"""

from .gaussian_mixture import GaussianMixture
from .bayesian_mixture import BayesianGaussianMixture


__all__ = ['bmatrix', 'GaussianMixture',
           'BayesianGaussianMixture']
