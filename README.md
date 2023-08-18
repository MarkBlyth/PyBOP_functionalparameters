# PyBOP - A *Py*thon package for *B*attery *O*ptimisation and *P*arameterisation

<div align="center">

[![Build Status](https://github.com/pybop-team/PyBOP/actions/workflows/test_on_push.yaml/badge.svg?branch=develop)](https://github.com/pybop-team/PyBOP/actions/workflows/test_on_push.yaml)

</div>

PyBOP aims to be a modular library for the parameterisation and optimisation of battery models, with a particular focus on classes built around [PyBaMM](https://github.com/pybamm-team/PyBaMM) models. The figure below gives the current conceptual idea of PyBOP's structure. This will likely evolve as development progresses.

<p align="center">
    <img src="assets/PyBOP_Arch.svg" alt="Data flows from battery cycling machines to Galv Harvesters, then to the     Galv server and REST API. Metadata can be updated and data read using the web client, and data can be downloaded by the Python client." width="600" />
</p>

The living software specification of PyBOP can be found [here](https://github.com/pybop-team/software-spec); however, an overview is introduced below.

- Provide design optimisation plus both frequentist and Bayesian parameterisation methods to battery modellers
- Provide workflows and examples for parameter fitting and grouping
- Create diagnostics for end-users to understand parameter identifiability and optimisation fidelity

**Community and values**

PyBOP aims to foster a broad consortium of developers and users, building on and
learning from the success of the PyBaMM community. Our values are:

-   Open-source (code and ideas should be shared)

-   Inclusivity and fairness (those who want to contribute may do so,
    and their input is appropriately recognised)

-   Inter-operability (aiming for modularity to enable maximum impact
    and inclusivity)

-   User-friendliness (putting user requirements first, thinking about user- assistance & workflows)
