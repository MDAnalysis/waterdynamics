Outputs
=======

Here we outline the output data structures for each of the packages classes.

WaterOrientationalRelaxation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:class:`~waterdynamics.WaterOrientationalRelaxation` (WOR) data is returned per window timestep,
which is stored in :attr:`WaterOrientationalRelaxation.timeseries`::

    results = [
        [ # time t0
            <WOR_OH>, <WOR_HH>, <WOR_dip>
        ],
        [ # time t1
            <WOR_OH>, <WOR_HH>, <WOR_dip>
        ],
        ...
     ]

AngularDistribution
~~~~~~~~~~~~~~~~~~~

:class:`~waterdynamics.AngularDistribution` (AD) data is returned per vector, which is stored in
:attr:`AngularDistribution.graph`. In fact, AngularDistribution returns a
histogram::

    results = [
        [ # OH vector values
          # the values are order in this way: <x_axis  y_axis>
            <cos_theta0 ang_distr0>, <cos_theta1 ang_distr1>, ...
        ],
        [ # HH vector values
            <cos_theta0 ang_distr0>, <cos_theta1 ang_distr1>, ...
        ],
        [ # dip vector values
           <cos_theta0 ang_distr0>, <cos_theta1 ang_distr1>, ...
        ],
     ]

MeanSquareDisplacement
~~~~~~~~~~~~~~~~~~~~~~

:class:`~waterdynamics.MeanSquareDisplacement` (MSD) data is returned in a list, which each element
represents a MSD value in its respective window timestep. Data is stored in
:attr:`MeanSquareDisplacement.timeseries`::

    results = [
         #MSD values orders by window timestep
            <MSD_t0>, <MSD_t1>, ...
     ]

SurvivalProbability
~~~~~~~~~~~~~~~~~~~

:class:`~waterdynamics.SurvivalProbability` (SP) computes two lists: a list of taus (:attr:`SurvivalProbability.tau_timeseries`) and a list of
the corresponding survival probabilities (:attr:`SurvivalProbability.sp_timeseries`).

    results = [ tau1, tau2, ..., tau_n ], [ sp_tau1, sp_tau2, ..., sp_tau_n]

Additionally, a list :attr:`SurvivalProbability.sp_timeseries_data`, is provided which contains
a list of all SPs calculated for each tau. This can be used to compute the distribution or time dependence of SP, etc.
