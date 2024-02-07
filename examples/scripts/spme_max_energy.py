import pybop

## NOTE: This is a brittle example, the classes and methods below will be
## integrated into pybop in a future release.

# A design optimisation example loosely based on work by L.D. Couto
# available at https://doi.org/10.1016/j.energy.2022.125966.

# The target is to maximise the gravimetric energy density over a
# range of possible design parameter values, including for example:
# cross-sectional area = height x width (only need change one)
# electrode widths, particle radii, volume fractions and
# separator width.

# Define parameter set and model
parameter_set = pybop.ParameterSet.pybamm("Chen2020")
model = pybop.lithium_ion.SPMe(parameter_set=parameter_set)

# Fitting parameters
parameters = [
    pybop.Parameter(
        "Positive electrode thickness [m]",
        prior=pybop.Gaussian(7.56e-05, 0.05e-05),
        bounds=[65e-06, 10e-05],
    ),
    pybop.Parameter(
        "Positive particle radius [m]",
        prior=pybop.Gaussian(5.22e-06, 0.05e-06),
        bounds=[2e-06, 9e-06],
    ),
]

# Define test protocol
experiment = pybop.Experiment(
    ["Discharge at 1C until 2.5 V (5 seconds period)"],
)
init_soc = 1  # start from full charge
signal = ["Voltage [V]", "Current [A]"]

# Generate problem
problem = pybop.DesignProblem(
    model, parameters, experiment, signal=signal, init_soc=init_soc
)

# Generate cost function and optimisation class
cost = pybop.GravimetricEnergyDensity(problem)
optim = pybop.Optimisation(
    cost, optimiser=pybop.PSO, verbose=True, allow_infeasible_solutions=False
)
optim.set_max_iterations(15)

# Run optimisation
x, final_cost = optim.run()
print("Estimated parameters:", x)
print(f"Initial gravimetric energy density: {-cost(cost.x0):.2f} Wh.kg-1")
print(f"Optimised gravimetric energy density: {-final_cost:.2f} Wh.kg-1")

# Plot the timeseries output
# cost.nominal_capacity(x, cost.problem._model)
pybop.quick_plot(x, cost, title="Optimised Comparison")

# Plot the cost landscape with optimisation path
if len(x) == 2:
    pybop.plot_cost2d(cost, optim=optim, steps=3)
