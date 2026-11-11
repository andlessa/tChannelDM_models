# tChannelDM Models - Scalar Mediator

FeynRules implementations of t-channel dark matter simplified models in which the mediator is a **complex scalar** ($Y_S$, spin 0) and the dark matter is a **Majorana fermion** ($\chi$, spin 1/2).
Both the mediator and the dark matter are odd under an assumed $`\mathcal{Z}_2`$ symmetry, while all Standard Model fields are even.
The mediator is an $SU(2)_L$ singlet and couples only to right-handed SM fermions.

Two models are available:

| Model | Mediator(s) | Couples to | Folder |
|---|---|---|---|
| Lepto-philic | $Y_{Se}$ (charge $-1$, colour singlet) | $e_R,\ \mu_R,\ \tau_R$ | [DMsimpt_Yscalar_leptons](./DMsimpt_Yscalar_leptons) |
| Quark-philic | $Y_{Su}$ (charge $+2/3$), $Y_{Sd}$ (charge $-1/3$), colour triplets | $u_R,c_R,t_R$ / $d_R,s_R,b_R$ | [DMsimpt_Yscalar_quarks](./DMsimpt_Yscalar_quarks) |

Each model folder contains:

 * `DMsimpt_Yscalar_*.fr`: the FeynRules model file (loaded together with the `SM.fr`, `Massless.rst` and `DiagonalCKM.rst` files in the same folder);
 * `loadModel_lo.nb` / `loadModel_nlo.nb`: Mathematica notebooks that generate the LO and NLO (with NLOCT) UFO models;
 * `DMsimpt_Yscalar_*_NLO_UFO`: the NLO UFO model;
 * `Cards`: example MadGraph5 cards.

**More details about the lepto-philic model can be found [here](./DMsimpt_Yscalar_leptons/), while about the quark-philic model can be found [here](./DMsimpt_Yscalar_quarks).**

--------------------------------------
## References

### Papers:

* [LHC-friendly freeze-in model paper](https://arxiv.org/abs/1811.05478)

* [t-channel dark matter models – a whitepaper](https://arxiv.org/abs/2504.10597)

### FeynRules Model Database:

* [Simplified Freeze-in model](http://feynrules.irmp.ucl.ac.be/wiki/FICPLHC)

* [t-Channel DM Models database](http://feynrules.irmp.ucl.ac.be/wiki/DMsimpt)
