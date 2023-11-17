Class Example Usage
===================

``waterdynamics`` operates around class based analyses.
Find examples of their use below.

WaterOrientationalRelaxation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Analyzing water orientational relaxation (WOR)
:class:`~waterdynamics.WaterOrientationalRelaxation`. In this case we are analyzing "how fast"
water molecules are rotating/changing direction. If WOR is very stable we can
assume that water molecules are rotating/changing direction very slow, on the
other hand, if WOR decay very fast, we can assume that water molecules are
rotating/changing direction very fast::

  import MDAnalysis
  from waterdynamics import WaterOrientationalRelaxation as WOR

  u = MDAnalysis.Universe(pdb, trajectory)
  select = "byres name OH2 and sphzone 6.0 protein and resid 42"
  WOR_analysis = WOR(universe, select, 0, 1000, 20)
  WOR_analysis.run()
  time = 0
  #now we print the data ready to plot. The first two columns are WOR_OH vs t plot,
  #the second two columns are WOR_HH vs t graph and the third two columns are WOR_dip vs t graph
  for WOR_OH, WOR_HH, WOR_dip in WOR_analysis.timeseries:
        print("{time} {WOR_OH} {time} {WOR_HH} {time} {WOR_dip}".format(time=time, WOR_OH=WOR_OH, WOR_HH=WOR_HH,WOR_dip=WOR_dip))
        time += 1

  #now, if we want, we can plot our data
  plt.figure(1,figsize=(18, 6))

  #WOR OH
  plt.subplot(131)
  plt.xlabel('time')
  plt.ylabel('WOR')
  plt.title('WOR OH')
  plt.plot(range(0,time),[column[0] for column in WOR_analysis.timeseries])

  #WOR HH
  plt.subplot(132)
  plt.xlabel('time')
  plt.ylabel('WOR')
  plt.title('WOR HH')
  plt.plot(range(0,time),[column[1] for column in WOR_analysis.timeseries])

  #WOR dip
  plt.subplot(133)
  plt.xlabel('time')
  plt.ylabel('WOR')
  plt.title('WOR dip')
  plt.plot(range(0,time),[column[2] for column in WOR_analysis.timeseries])

  plt.show()

where t0 = 0, tf = 1000 and dtmax = 20. In this way we create 20 windows
timesteps (20 values in the x axis), the first window is created with 1000
timestep average (1000/1), the second window is created with 500 timestep
average(1000/2), the third window is created with 333 timestep average (1000/3)
and so on.

Water orientational relaxation (WOR) data is returned per window timestep,
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

Analyzing angular distribution (AD) :class:`AngularDistribution` for OH vector,
HH vector and dipole vector. It returns a line histogram with vector
orientation preference. A straight line in the output plot means no
preferential orientation in water molecules. In this case we are analyzing if
water molecules have some orientational preference, in this way we can see if
water molecules are under an electric field or if they are interacting with
something (residue, protein, etc)::

  import MDAnalysis
  from waterdynamics import AngularDistribution as AD

  u = MDAnalysis.Universe(pdb, trajectory)
  selection = "byres name OH2 and sphzone 6.0 (protein and (resid 42 or resid 26) )"
  bins = 30
  AD_analysis = AD(universe,selection,bins)
  AD_analysis.run()
  #now we print data ready to graph. The first two columns are P(cos(theta)) vs cos(theta) for OH vector ,
  #the seconds two columns are P(cos(theta)) vs cos(theta) for HH vector and thirds two columns
  #are P(cos(theta)) vs cos(theta) for dipole vector
  for bin in range(bins):
        print("{AD_analysisOH} {AD_analysisHH} {AD_analysisDip}".format(AD_analysis.graph0=AD_analysis.graph[0][bin], AD_analysis.graph1=AD_analysis.graph[1][bin],AD_analysis.graph2=AD_analysis.graph[2][bin]))

  #and if we want to graph our results
  plt.figure(1,figsize=(18, 6))

  #AD OH
  plt.subplot(131)
  plt.xlabel('cos theta')
  plt.ylabel('P(cos theta)')
  plt.title('PDF cos theta for OH')
  plt.plot([float(column.split()[0]) for column in AD_analysis.graph[0][:-1]],[float(column.split()[1]) for column in AD_analysis.graph[0][:-1]])

  #AD HH
  plt.subplot(132)
  plt.xlabel('cos theta')
  plt.ylabel('P(cos theta)')
  plt.title('PDF cos theta for HH')
  plt.plot([float(column.split()[0]) for column in AD_analysis.graph[1][:-1]],[float(column.split()[1]) for column in AD_analysis.graph[1][:-1]])

  #AD dip
  plt.subplot(133)
  plt.xlabel('cos theta')
  plt.ylabel('P(cos theta)')
  plt.title('PDF cos theta for dipole')
  plt.plot([float(column.split()[0]) for column in AD_analysis.graph[2][:-1]],[float(column.split()[1]) for column in AD_analysis.graph[2][:-1]])

  plt.show()


where `P(cos(theta))` is the angular distribution or angular probabilities.

Angular distribution (AD) data is returned per vector, which is stored in
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

Analyzing mean square displacement (MSD) :class:`MeanSquareDisplacement` for
water molecules. In this case we are analyzing the average distance that water
molecules travels inside protein in XYZ direction (cylindric zone of radius
11[nm], Zmax 4.0[nm] and Zmin -8.0[nm]). A strong rise mean a fast movement of
water molecules, a weak rise mean slow movement of particles::

  import MDAnalysis
  from waterdynamics import MeanSquareDisplacement as MSD

  u = MDAnalysis.Universe(pdb, trajectory)
  select = "byres name OH2 and cyzone 11.0 4.0 -8.0 protein"
  MSD_analysis = MSD(universe, select, 0, 1000, 20)
  MSD_analysis.run()
  #now we print data ready to graph. The graph
  #represents MSD vs t
  time = 0
  for msd in MSD_analysis.timeseries:
        print("{time} {msd}".format(time=time, msd=msd))
        time += 1

  #Plot
  plt.xlabel('time')
  plt.ylabel('MSD')
  plt.title('MSD')
  plt.plot(range(0,time),MSD_analysis.timeseries)
  plt.show()

Mean Square Displacement (MSD) data is returned in a list, which each element
represents a MSD value in its respective window timestep. Data is stored in
:attr:`MeanSquareDisplacement.timeseries`::

    results = [
         #MSD values orders by window timestep
            <MSD_t0>, <MSD_t1>, ...
     ]

.. _SP-examples:

SurvivalProbability
~~~~~~~~~~~~~~~~~~~

Analyzing survival probability (SP) :class:`SurvivalProbability` of molecules.
In this case we are analyzing how long water molecules remain in a
sphere of radius 12.3 centered in the geometrical center of resid 42 and 26.
A slow decay of SP means a long permanence time of water molecules in
the zone, on the other hand, a fast decay means a short permanence time::

  import MDAnalysis
  from waterdynamics import SurvivalProbability as SP
  import matplotlib.pyplot as plt

  universe = MDAnalysis.Universe(pdb, trajectory)
  select = "byres name OH2 and sphzone 12.3 (resid 42 or resid 26) "
  sp = SP(universe, select, verbose=True)
  sp.run(start=0, stop=101, tau_max=20)
  tau_timeseries = sp.tau_timeseries
  sp_timeseries = sp.sp_timeseries

  # print in console
  for tau, sp in zip(tau_timeseries, sp_timeseries):
        print("{time} {sp}".format(time=tau, sp=sp))

  # plot
  plt.xlabel('Time')
  plt.ylabel('SP')
  plt.title('Survival Probability')
  plt.plot(tau_timeseries, sp_timeseries)
  plt.show()

One should note that the `stop` keyword as used in the above example has an
`exclusive` behaviour, i.e. here the final frame used will be 100 not 101.
This behaviour is aligned with :class:`AnalysisBase` but currently differs from
other :mod:`waterdynamics` classes, which all exhibit
`inclusive` behaviour for their final frame selections.

Another example applies to the situation where you work with many different "residues".
Here we calculate the SP of a potassium ion around each lipid in a membrane and
average the results. In this example, if the SP analysis were run without treating each lipid
separately, potassium ions may hop from one lipid to another and still be counted as remaining
in the specified region. That is, the survival probability of the potassium ion around the
entire membrane will be calculated.

Note, for this example, it is advisable to use `Universe(in_memory=True)` to ensure that the
simulation is not being reloaded into memory for each lipid::

  import MDAnalysis as mda
  from waterdynamics import SurvivalProbability as SP
  import numpy as np

  u = mda.Universe("md.gro", "md100ns.xtc", in_memory=True)
  lipids = u.select_atoms('resname LIPIDS')
  joined_sp_timeseries = [[] for _ in range(20)]
  for lipid in lipids.residues:
      print("Lipid ID: %d" % lipid.resid)

      select = "resname POTASSIUM and around 3.5 (resid %d and name O13 O14) " % lipid.resid
      sp = SP(u, select, verbose=True)
      sp.run(tau_max=20)

      # Raw SP points for each tau:
      for sps, new_sps in zip(joined_sp_timeseries, sp.sp_timeseries_data):
          sps.extend(new_sps)

  # average all SP datapoints
  sp_data = [np.mean(sp) for sp in joined_sp_timeseries]

  for tau, sp in zip(range(1, tau_max + 1), sp_data):
      print("{time} {sp}".format(time=tau, sp=sp))

Survival Probability (SP) computes two lists: a list of taus (:attr:`SurvivalProbability.tau_timeseries`) and a list of
the corresponding survival probabilities (:attr:`SurvivalProbability.sp_timeseries`).

    results = [ tau1, tau2, ..., tau_n ], [ sp_tau1, sp_tau2, ..., sp_tau_n]

Additionally, a list :attr:`SurvivalProbability.sp_timeseries_data`, is provided which contains
a list of all SPs calculated for each tau. This can be used to compute the distribution or time dependence of SP, etc.

