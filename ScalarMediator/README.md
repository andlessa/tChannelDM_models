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


--------------------------------------------
## Lepto-philic model: DMsimpt_Yscalar_leptons

### Model

The model adds a charged scalar lepton $Y_{Se}$ (hypercharge $-1$, lepton number $+1$) and a Majorana fermion singlet $\chi$ ($X_m$ in the model files) to the SM.
The BSM Lagrangian is:

```math
\begin{aligned}
\mathcal{L}_{\rm BSM} =&\ \frac{1}{2} \bar{\chi}\, i \gamma^\mu \partial_\mu \chi - \frac{1}{2} M_{X} \bar{\chi} \chi  + (D_\mu Y_{Se})^\dagger D^\mu Y_{Se} - M_{Y}^2\, Y_{Se}^\dagger Y_{Se}\\
& - Y_{Se}^\dagger \left( y_{FeR}\, \bar{\chi} e_R + y_{F\mu R}\, \bar{\chi} \mu_R + y_{F\tau R}\, \bar{\chi} \tau_R \right) + {\rm h.c.}\\
 &- \frac{\lambda_{Y}}{4} \left(Y_{Se}^\dagger Y_{Se}\right)^2 - \lambda_{YH}\, Y_{Se}^\dagger Y_{Se} \left(|H|^2 - \frac{v^2}{2}\right)
\end{aligned}
```

where the Lagrangian mass parameter of $Y_{Se}$ has been traded for its physical mass $M_Y$ ($\mu_{YS}^2 = M_Y^2 - \lambda_{YH} v^2/2$).

### UFO Model

 * [DMsimpt_Yscalar_leptons_NLO_UFO](./DMsimpt_Yscalar_leptons/DMsimpt_Yscalar_leptons_NLO_UFO): NLO model with QCD NLO corrections (generated with NLOCT). It can be used to generate events or compute cross sections at LO or NLO.

A LO-only UFO can be generated with `loadModel_lo.nb`.

The BSM particles are:

| Particle | MG5 name | PDG | Spin |
|---|---|---|---|
| $\chi$ | `xm` | 52 | 1/2 (Majorana) |
| $Y_{Se}$ | `yse` / `yse~` | 5920011 | 0 |

The BSM parameters are:

  * `MY` : scalar mediator mass (`MASS` block, PDG 5920011)
  * `MX` : Majorana dark matter mass (`MASS` block, PDG 52)
  * `WY` : mediator total width
  * `yFeR`: $Y_{Se}-\chi-e$ coupling, controls $BR(Y_{Se} \to e + \chi)$
  * `yFmuR`: $Y_{Se}-\chi-\mu$ coupling, controls $BR(Y_{Se} \to \mu + \chi)$
  * `yFtaR`: $Y_{Se}-\chi-\tau$ coupling, controls $BR(Y_{Se} \to \tau + \chi)$
  * `lamYH`: mediator–Higgs portal coupling $\lambda_{YH}$
  * `lamY`: mediator quartic coupling $\lambda_{Y}$

`lamYH` and `lamY` do not enter mediator pair production at LO, but `lamYH` modifies the mediator coupling to the Higgs boson.

The mediator total width is given by:

```math
\Gamma_{Y} = \sum_{\alpha=e,\mu,\tau} y_{F\alpha R}^2\, \frac{(M_Y^2  - m_\alpha^2 - M_X^2)\sqrt{\lambda(M_Y^2, m_\alpha^2, M_X^2)}}{16 \pi M_Y^3} \simeq \left(\sum_{\alpha=e,\mu,\tau} y_{F\alpha R}^2\right) \frac{(M_{Y}^2 -M_{X}^2)^2}{16 \pi M_Y^3}
```

where the approximation holds for negligible lepton masses ($m_{\alpha} \ll M_X,M_Y$).
The UFO includes these partial widths (`decays.py`), so the width can also be computed automatically by setting `WY` to `Auto` in MadGraph5.

### Event Generation

Example cards can be found in [Cards](./DMsimpt_Yscalar_leptons/Cards).
The mediator pair production can be computed at LO (NLO) using the MadGraph5 syntax:

```
import model DMsimpt_Yscalar_leptons_NLO_UFO
generate p p > yse yse~            # LO
generate p p > yse yse~ [QCD]      # NLO
```


--------------------------------------------
## Quark-philic model: DMsimpt_Yscalar_quarks

### Model

This is the hadronic version of the model above.
It introduces two scalar quark mediators, both colour triplets and $SU(2)_L$ singlets: an up-type one, $Y_{Su}$ (hypercharge $2/3$), and a down-type one, $Y_{Sd}$ (hypercharge $-1/3$).
When using the model in a simplified-model framework, one usually assumes only one of them ($Y_{Su}$ or $Y_{Sd}$) is light enough to be relevant.
The dark matter is again a Majorana fermion singlet $\chi$.

The BSM Lagrangian is:

```math
\begin{aligned}
\mathcal{L}_{\rm BSM} =&\ \frac{1}{2} \bar{\chi}\, i \gamma^\mu \partial_\mu \chi - \frac{1}{2} M_{X} \bar{\chi} \chi + \sum_{i=u,d} \left[ (D_\mu Y_{Si})^\dagger D^\mu Y_{Si} - M_{Y_i}^2\, Y_{Si}^\dagger Y_{Si} \right]\\
& - \left[ y_{FqR} \left( Y_{Su}^\dagger \bar{\chi} u_R + Y_{Su}^\dagger \bar{\chi} c_R + Y_{Sd}^\dagger \bar{\chi} d_R + Y_{Sd}^\dagger \bar{\chi} s_R \right) + y_{FtR}\, Y_{Su}^\dagger \bar{\chi} t_R + y_{FbR}\, Y_{Sd}^\dagger \bar{\chi} b_R + {\rm h.c.} \right]\\
&- \sum_{i=u,d} \left[ \frac{\lambda_{Y_i}}{4} \left(Y_{Si}^\dagger Y_{Si}\right)^2 + \lambda_{Y_iH}\, Y_{Si}^\dagger Y_{Si} \left(|H|^2 - \frac{v^2}{2}\right) \right]
\end{aligned}
```

with colour indices contracted between the mediator and the SM quark (and within each $Y_{Si}^\dagger Y_{Si}$ pair).
The model assumes a universal coupling ($`y_{FqR}`$) to the first/second generation quarks and separate couplings ($`y_{FtR}`$ and $`y_{FbR}`$) to the third generation.

### UFO Model

 * [DMsimpt_Yscalar_quarks_NLO_UFO](./DMsimpt_Yscalar_quarks/DMsimpt_Yscalar_quarks_NLO_UFO): NLO model with QCD NLO corrections (generated with NLOCT). It can be used to generate events or compute cross sections at LO or NLO.

A LO-only UFO can be generated with `loadModel_lo.nb`.

The BSM particles are:

| Particle | MG5 name | PDG | Spin |
|---|---|---|---|
| $\chi$ | `xm` | 52 | 1/2 (Majorana) |
| $Y_{Su}$ | `ysu` / `ysu~` | 5910002 | 0 |
| $Y_{Sd}$ | `ysd` / `ysd~` | 5910001 | 0 |

The BSM parameters are:

  * `MYu` : up-type mediator mass
  * `MYd` : down-type mediator mass
  * `MX` : Majorana dark matter mass
  * `WYu`, `WYd` : mediator total widths
  * `yFqR`: coupling between the mediators and the first/second generation quarks
  * `yFtR`: $Y_{Su}-\chi-t$ coupling, controls $BR(Y_{Su} \to t + \chi)$
  * `yFbR`: $Y_{Sd}-\chi-b$ coupling, controls $BR(Y_{Sd} \to b + \chi)$
  * `lamYuH`, `lamYdH`: mediator–Higgs portal couplings $\lambda_{Y_uH}$, $\lambda_{Y_dH}$
  * `lamYu`, `lamYd`: mediator quartic couplings $\lambda_{Y_u}$, $\lambda_{Y_d}$

`lamYuH`, `lamYdH`, `lamYu` and `lamYd` do not enter mediator pair production at LO, but the Higgs-portal couplings modify the mediator coupling to the Higgs boson.

The partial width for $Y_{Su} \to q + \chi$ ($q = u,c,t$) is:

```math
\Gamma(Y_{Su} \to q \chi) = y_{q}^2\, \frac{(M_{Y_u}^2  - m_q^2 - M_X^2)\sqrt{\lambda(M_{Y_u}^2, m_q^2, M_X^2)}}{16 \pi M_{Y_u}^3}
```

with $y_{u} = y_{c} = y_{FqR}$ and $y_{t} = y_{FtR}$, and analogously for $Y_{Sd}$ (with $y_{d} = y_{s} = y_{FqR}$ and $y_{b} = y_{FbR}$).
These partial widths are included in the UFO (`decays.py`), so the widths can be set to `Auto` in MadGraph5.

### Event Generation

Example cards can be found in [Cards](./DMsimpt_Yscalar_quarks/Cards).
For instance, the up-type mediator pair production can be computed at LO (NLO) using the MadGraph5 syntax:

```
import model DMsimpt_Yscalar_quarks_NLO_UFO
generate p p > ysu ysu~            # LO
generate p p > ysu ysu~ [QCD]      # NLO
```


--------------------------------------
## References

### Papers:

* [LHC-friendly freeze-in model paper](https://arxiv.org/abs/1811.05478)

* [t-channel dark matter models – a whitepaper](https://arxiv.org/abs/2504.10597)

### FeynRules Model Database:

* [Simplified Freeze-in model](http://feynrules.irmp.ucl.ac.be/wiki/FICPLHC)

* [t-Channel DM Models database](http://feynrules.irmp.ucl.ac.be/wiki/DMsimpt)
