# Lepto-philic model: DMsimpt_Yscalar_leptons

### Model

The model adds a charged scalar lepton $Y_{Se}$ (hypercharge $-1$) and a Majorana fermion singlet $\chi$ ($X_m$ in the model files) to the SM.
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

The NLO UFO can be generated with `loadModel_nlo.nb`.

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
