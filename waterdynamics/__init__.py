"""
waterdynamics
Analysis of water dynamics in molecular dynamics trajectories and water interactions with other molecules.
"""

# Add imports here
from .waterdynamics import (
    WaterOrientationalRelaxation,
    AngularDistribution,
    MeanSquareDisplacement,
    SurvivalProbability,
)

# Handle version
from importlib.metadata import version
__version__ = version("waterdynamics")
