# tChannelDM Models - Vector-like Fermion Mediator

FeynRules implementations of t-channel dark matter simplified models in which the mediator is a **vector-like fermion** ($Y_F$, spin 1/2) and the dark matter is a **real scalar** ($X_s$, spin 0).
Both the mediator and the dark matter are odd under an assumed $`\mathcal{Z}_2`$ symmetry, while all Standard Model fields are even.
The mediator is an $SU(2)_L$ singlet and couples only to right-handed SM fermions.

Two models are available:

| Model | Mediator(s) | Couples to | Folder |
|---|---|---|---|
| Lepto-philic | $Y_F$ (charge $-1$, colour singlet) | $e_R,\ \mu_R,\ \tau_R$ | [DMsimpt_Yfermion_leptons](./DMsimpt_Yfermion_leptons) |
| Quark-philic | $Y_{Fu}$ (charge $+2/3$), $Y_{Fd}$ (charge $-1/3$), colour triplets | $u_R,c_R,t_R$ / $d_R,s_R,b_R$ | [DMsimpt_Yfermion_quarks](./DMsimpt_Yfermion_quarks) |

Each model folder contains:

 * `DMsimpt_Yfermion_*.fr`: the FeynRules model file (loaded together with the `SM.fr`, `Massless.rst` and `DiagonalCKM.rst` files in the same folder);
 * `loadModel_lo.nb` / `loadModel_nlo.nb`: Mathematica notebooks that generate the LO and NLO (with NLOCT) UFO models;
 * `Cards`: example MadGraph5 cards.


--------------------------------------------
## Lepto-philic model: DMsimpt_Yfermion_leptons

### Model

The model adds a vector-like charged lepton $Y_F$ (hypercharge $-1$, lepton number $+1$) and a real scalar singlet $X_s$ to the SM.
The BSM Lagrangian is:

```math
\begin{aligned}
\mathcal{L}_{\rm BSM} =&\ \frac{1}{2} (\partial_\mu X_s)^2 -\frac{1}{2} M_{X}^2 X_s^2  + i \bar{Y}_F \gamma^\mu D_\mu Y_F - M_{Y} \bar{Y}_F Y_F\\
& - X_s \left( y_{FeR}\, \bar{Y}_F e_R + y_{F\mu R}\, \bar{Y}_F \mu_R + y_{F\tau R}\, \bar{Y}_F \tau_R + {\rm h.c.}  \right)\\
 &- \frac{\lambda_{Xs}}{4} X_s^4 - \lambda_{XsH} X_s^2 \left(|H|^2 - \frac{v^2}{2}\right)
\end{aligned}
```

where the Lagrangian mass parameter of $X_s$ has been traded for its physical mass $M_X$ ($\mu_{Xs}^2 = M_X^2 - \lambda_{XsH} v^2$).

### UFO Model

 * [DMsimpt_Yfermion_leptons_NLO_UFO](./DMsimpt_Yfermion_leptons/DMsimpt_Yfermion_leptons_NLO_UFO): NLO model with QCD NLO corrections (generated with NLOCT). It can be used to generate events or compute cross sections at LO or NLO.

A LO-only UFO can be generated with `loadModel_lo.nb`.

The BSM particles are:

| Particle | MG5 name | PDG | Spin |
|---|---|---|---|
| $X_s$ | `xs` | 51 | 0 |
| $Y_F$ | `yf` / `yf~` | 5920011 | 1/2 |

The BSM parameters are:

  * `MY` : vector-like mediator mass (`MASS` block, PDG 5920011)
  * `MX` : scalar dark matter mass (`MASS` block, PDG 51)
  * `WY` : mediator total width
  * `yFeR`: $Y_F-X_s-e$ coupling, controls $BR(Y_F \to e + X_s)$
  * `yFmuR`: $Y_F-X_s-\mu$ coupling, controls $BR(Y_F \to \mu + X_s)$
  * `yFtaR`: $Y_F-X_s-\tau$ coupling, controls $BR(Y_F \to \tau + X_s)$
  * `lamXsH`: Higgs-portal coupling $\lambda_{XsH}$
  * `lamXs`: dark scalar quartic coupling $\lambda_{Xs}$

`lamXsH` and `lamXs` are not relevant for mediator pair production at the LHC, but can have an impact on DM production through the Higgs portal.

The mediator total width is given by:

```math
\Gamma_{Y} = \sum_{\alpha=e,\mu,\tau} y_{F\alpha R}^2\, \frac{(M_Y^2  + m_\alpha^2 - M_X^2)\sqrt{\lambda(M_Y^2, m_\alpha^2, M_X^2)}}{32 \pi M_Y^3} \simeq \left(\sum_{\alpha=e,\mu,\tau} y_{F\alpha R}^2\right) \frac{(M_{Y}^2 -M_{X}^2)^2}{32 \pi M_Y^3}
```

where the approximation holds for negligible lepton masses ($m_{\alpha} \ll M_X,M_Y$).
The UFO includes these partial widths (`decays.py`), so the width can also be computed automatically by setting `WY` to `Auto` in MadGraph5.

### Event Generation

Example cards can be found in [Cards](./DMsimpt_Yfermion_leptons/Cards).
The mediator pair production can be computed at LO (NLO) using the MadGraph5 syntax:

```
import model DMsimpt_Yfermion_leptons_NLO_UFO
generate p p > yf yf~            # LO
generate p p > yf yf~ [QCD]      # NLO
```


--------------------------------------------
## Quark-philic model: DMsimpt_Yfermion_quarks

### Model

This is the hadronic version of the model above.
It introduces two vector-like quark mediators, both colour triplets and $SU(2)_L$ singlets: an up-type one, $Y_{Fu}$ (hypercharge $2/3$), and a down-type one, $Y_{Fd}$ (hypercharge $-1/3$).
When using the model in a simplified-model framework, one usually assumes only one of them ($Y_{Fu}$ or $Y_{Fd}$) is light enough to be relevant.
The dark matter is again a real scalar singlet $X_s$.

The BSM Lagrangian is:

```math
\begin{aligned}
\mathcal{L}_{\rm BSM} =&\ \frac{1}{2} (\partial_\mu X_s)^2 -\frac{1}{2} M_{X}^2 X_s^2  + i \bar{Y}_{Fu} \gamma^\mu D_\mu Y_{Fu} - M_{Y_u} \bar{Y}_{Fu} Y_{Fu}   + i \bar{Y}_{Fd} \gamma^\mu D_\mu Y_{Fd} - M_{Y_d} \bar{Y}_{Fd} Y_{Fd}\\
& - X_s \left[ y_{FqR} \left( \bar{Y}_{Fu} u_R + \bar{Y}_{Fu} c_R + \bar{Y}_{Fd} d_R + \bar{Y}_{Fd} s_R \right) + y_{FtR}\, \bar{Y}_{Fu} t_R + y_{FbR}\, \bar{Y}_{Fd} b_R + {\rm h.c.} \right]\\
&- \frac{\lambda_{Xs}}{4} X_s^4 - \lambda_{XsH} X_s^2 \left(|H|^2 - \frac{v^2}{2}\right)
\end{aligned}
```

with colour indices contracted between the mediator and the SM quark.
The model assumes a universal coupling ($`y_{FqR}`$) to the first/second generation quarks and separate couplings ($`y_{FtR}`$ and $`y_{FbR}`$) to the third generation.

### UFO Model

No UFO is included in the repository for this model yet.
LO and NLO UFO models can be generated from [DMsimpt_Yfermion_quarks.fr](./DMsimpt_Yfermion_quarks/DMsimpt_Yfermion_quarks.fr) with `loadModel_lo.nb` and `loadModel_nlo.nb`.

The BSM particles are:

| Particle | MG5 name | PDG | Spin |
|---|---|---|---|
| $X_s$ | `xs` | 51 | 0 |
| $Y_{Fu}$ | `yfu` / `yfu~` | 5910002 | 1/2 |
| $Y_{Fd}$ | `yfd` / `yfd~` | 5910001 | 1/2 |

The BSM parameters are:

  * `MYu` : up-type mediator mass
  * `MYd` : down-type mediator mass
  * `MX` : scalar dark matter mass
  * `WYu`, `WYd` : mediator total widths
  * `yFqR`: coupling between the mediators and the first/second generation quarks
  * `yFtR`: $Y_{Fu}-X_s-t$ coupling, controls $BR(Y_{Fu} \to t + X_s)$
  * `yFbR`: $Y_{Fd}-X_s-b$ coupling, controls $BR(Y_{Fd} \to b + X_s)$
  * `lamXsH`: Higgs-portal coupling $\lambda_{XsH}$
  * `lamXs`: dark scalar quartic coupling $\lambda_{Xs}$

`lamXsH` and `lamXs` are not relevant for mediator pair production at the LHC, but can have an impact on DM production through the Higgs portal.

The partial width for $Y_{Fu} \to q + X_s$ ($q = u,c,t$) is:

```math
\Gamma(Y_{Fu} \to q X_s) = y_{q}^2\, \frac{(M_{Y_u}^2  + m_q^2 - M_X^2)\sqrt{\lambda(M_{Y_u}^2, m_q^2, M_X^2)}}{32 \pi M_{Y_u}^3}
```

with $y_{u} = y_{c} = y_{FqR}$ and $y_{t} = y_{FtR}$, and analogously for $Y_{Fd}$ (with $y_{d} = y_{s} = y_{FqR}$ and $y_{b} = y_{FbR}$).

### Event Generation

Example cards can be found in [Cards](./DMsimpt_Yfermion_quarks/Cards).
For instance, the up-type mediator pair production can be computed at LO (NLO) using the MadGraph5 syntax:
`p p > yfu yfu~` (`p p > yfu yfu~ [QCD]`).


--------------------------------------
## References

### Papers:

* [LHC-friendly freeze-in model paper](https://arxiv.org/abs/1811.05478)

* [t-channel dark matter models – a whitepaper](https://arxiv.org/abs/2504.10597)

### FeynRules Model Database:

* [Simplified Freeze-in model](http://feynrules.irmp.ucl.ac.be/wiki/FICPLHC)

* [t-Channel DM Models database](http://feynrules.irmp.ucl.ac.be/wiki/DMsimpt)
