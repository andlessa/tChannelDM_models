# Quark-philic model: DMsimpt_Yscalar_quarks

### Model

The quark-philic scenario introduces two scalar quark mediators, both colour triplets and $SU(2)_L$ singlets: an up-type one, $Y_{Su}$ (hypercharge $2/3$), and a down-type one, $Y_{Sd}$ (hypercharge $-1/3$).
When using the model in a simplified-model framework, one usually assumes only one of them ($Y_{Su}$ or $Y_{Sd}$) is light enough to be relevant.
The dark matter is a Majorana fermion singlet $\chi$.

The BSM Lagrangian is:

```math
\begin{aligned}
\mathcal{L}_{\rm BSM} =&\ \frac{1}{2} \bar{\chi}\, i \gamma^\mu \partial_\mu \chi - \frac{1}{2} M_{X} \bar{\chi} \chi + \sum_{i=u,d} \left[ (D_\mu Y_{Si})^\dagger D^\mu Y_{Si} - M_{Y_i}^2\, Y_{Si}^\dagger Y_{Si} \right]\\
& - \left[ y_{FqR} \left( Y_{Su}^\dagger \bar{\chi} u_R + Y_{Su}^\dagger \bar{\chi} c_R + Y_{Sd}^\dagger \bar{\chi} d_R + Y_{Sd}^\dagger \bar{\chi} s_R \right) + y_{FtR}\, Y_{Su}^\dagger \bar{\chi} t_R + y_{FbR}\, Y_{Sd}^\dagger \bar{\chi} b_R + {\rm h.c.} \right]\\
&- \sum_{i=u,d} \left[ \frac{\lambda_{Y_i}}{4} \left(Y_{Si}^\dagger Y_{Si}\right)^2 + \lambda_{Y_iH}\, Y_{Si}^\dagger Y_{Si} \left(|H|^2 - \frac{v^2}{2}\right) \right]
\end{aligned}
```

The model assumes a universal coupling ($`y_{FqR}`$) to the first/second generation quarks and separate couplings ($`y_{FtR}`$ and $`y_{FbR}`$) to the third generation.

### UFO Model

 * [DMsimpt_Yscalar_quarks_NLO_UFO](./DMsimpt_Yscalar_quarks/DMsimpt_Yscalar_quarks_NLO_UFO): NLO model with QCD NLO corrections (generated with NLOCT). It can be used to generate events or compute cross sections at LO or NLO.

The NLO UFO can be generated with `loadModel_nlo.nb`.

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


