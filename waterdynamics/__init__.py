"""
waterdynamics
Analysis of water dynamics in molecular dynamics trajectories and water interactions with other molecules.
"""

# Add imports here
from ._version import get_versions
from .waterdynamics import (
    WaterOrientationalRelaxation,
    AngularDistribution,
    MeanSquareDisplacement,
    SurvivalProbability,
)

# Handle versioneer
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
