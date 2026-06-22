# tChannelDM Models

Repository to collect model definitions and files for event generation using t-channel DM simplified models.


--------------------------------------------
## Lepto-philic model: DMsimpt_leptons

### Model

The model corresponds to the addition of a lepton-like mediator ($Y_F$) and and a single scalar ($X_s$), both odd under an assumed $`\mathcal{Z}_2`$ symmetry.
Since the mediator is a singlet under $SU(2)_L$, the BSM Lagrangian is given by:

```math
\begin{aligned}
\mathcal{L}_{\rm BSM} =&  \frac{1}{2} |\partial_\mu X_s|^2 -\frac{1}{2} M_{X}^2 |X_s|^2  + i \bar{\psi}_Y \gamma^\mu D_\mu \psi_Y - M_{Y} \bar{\psi}_Y \psi_Y\\
& - X_s \left( y_{FeR} \bar{\psi}_Y e_R + y_{FmuR} \bar{\psi}_Y \mu_R + y_{FtaR} \bar{\psi}_Y \tau_R + h.c.  \right)\\
 &- \frac{1}{4} \lambda_{Xs} X_s^4 - \lambda_{XsH} X_s^2 \left(|H|^2 - \frac{v^2}{2}\right)
\end{aligned}
```


#### UFO Model

Two versions of the UFO model are available:

 * [DMsimpt_leptons_UFO](./DMsimpt_leptons/DMsimpt_leptons_UFO): LO model corresponding to the Lagrangian above.
* [DMsimpt_leptons_NLO_UFO](./DMsimpt_leptons/DMsimpt_leptons_NLO_UFO): NLO model corresponding to the Lagrangian above. In this model QCD NLO corrections are implemented and can be used to generate NLO events or compute cross-sections at NLO.

The relevant parameters (see [param_card.dat](./DMsimpt_leptons/Cards/param_card.dat)) are:

  * `MY` : vector-like mediator mass
  * `MX` : scalar Dark Matter mass
  * `yFer`: $Y-X_s-e$ coupling, controls $BR(Y \to e + X_s)$
  * `yFmur`: $Y-X_s-\mu$ coupling, controls $BR(Y \to \mu + X_s)$
  * `yFtar`: $Y-X_s-\mu$ coupling, controls $BR(Y \to \tau + X_s)$

The remaining parameters (`lamXsH` and `lamXs`) are not relevant for the mediator pair production at the LHC, but can have an impact on the DM production through the Higgs-portal.

In addition, the mediator total width is given by:

```math
\Gamma_Y = \sum_{\alpha=e,\mu,\tau} (y_{F\alpha R})^2 \frac{(M_Y^2  + m_\alpha^2 - M_X^2)\sqrt{\lambda(M_Y^2, m_\alpha^2, M_X^2)}}{32 \pi M_Y^3} \simeq \left(\sum_{\alpha=e,\mu,\tau} (y_{F\alpha R})^2)\right) \frac{(M_{Y}^2 -m_{X}^2)^2}{32 \pi M_Y^3}
```
for negligible lepton masses ($m_{\alpha} \ll M_X,M_Y$).

### Event Generation

Cards for event generation can be found in [Cards](./DMsimpt_leptons/Cards) and can be used to generate
parton-level events with MadGraph5.
The mediator production can be computed at LO (NLO) using the MadGraph5 syntax: `p p > yf yf~` (`p p > yf yf~ [QCD]`).



--------------------------------------------
## Quark-philic model: DMsimpt_quarks

### Model

This model is the hadronic version of the model described above.
The main difference, however, is that in the quark-philic model it is possible to introduce two mediators: one coupling to down-type quarks ($Y_{Fd}$) and another to up-type quarks ($Y_{Fu}$).
When using the model in a simplified model framework, one should assume only one mediator 
($Y_{Fd}$ or $Y_{Fu}$) is present.

The quark-philic model corresponds to the addition of two quark-like mediators ($Y_{Fd}$ and $Y_{Fu}$) and a single scalar ($X_s$), all odd under an assumed $`\mathcal{Z}_2`$ symmetry.
Since the mediators are assumed to be a singlet under $SU(2)_L$, the BSM Lagrangian is given by:

```math
\begin{aligned}
\mathcal{L}_{\rm BSM} =&  \frac{1}{2} |\partial_\mu X_s|^2 -\frac{1}{2} M_{X}^2 |X_s|^2  + i \bar{\psi}_{Y_u} \gamma^\mu D_\mu \psi_{Y_u} - M_{Y_u} \bar{\psi}_{Y_u} \psi_{Y_u}   + i \bar{\psi}_{Y_d} \gamma^\mu D_\mu \psi_{Y_d} - M_{Y_d} \bar{\psi}_{Y_d} \psi_{Y_d}\\
& - X_s \left[ y_{FqR} \left( \bar{\psi}_{Y_u} u_R + \bar{\psi}_{Y_u} c_R + \bar{\psi}_{Y_d} d_R + \bar{\psi}_{Y_s} s_R \right) + y_{FtR} \bar{\psi}_{Y_u} t_R + y_{FbR} \bar{\psi}_{Y_b} b_R + h.c. \right]\\
&- \frac{1}{4} \lambda_{Xs} X_s^4 - \lambda_{XsH} X_s^2 \left(|H|^2 - \frac{v^2}{2}\right)
\end{aligned}
```
Note that the model assumes a universal coupling ($`y_{FqR} `$) to the first/second generation quarks and separate couplings ($`y_{FtR} `$ and $`y_{FbR} `$) for the third generation.



#### UFO Model

Two versions of the UFO model are available:

 * [DMsimpt_quarks_UFO](./DMsimpt_quarks/DMsimpt_quarks_UFO): LO model corresponding to the Lagrangian above.
* [DMsimpt_quarks_NLO_UFO](./DMsimpt_quarks/DMsimpt_quarks_NLO_UFO): NLO model corresponding to the Lagrangian above. In this model QCD NLO corrections are implemented and can be used to generate NLO events or compute cross-sections at NLO.

The relevant parameters (see [param_card.dat](./DMsimpt_quarks/Cards/param_card.dat)) are:

  * `MYu` : up-type mediator mass
  * `MYd` : down-type mediator mass
  * `MX` : scalar Dark Matter mass
  * `yFqr`: coupling between the mediators and the first/second quarks
  * `yFtr`: $Y_u-X_s-t$ coupling, controls $BR(Y_u \to t + X_s)$
  * `yFbr`: $Y_d-X_s-b$ coupling, controls $BR(Y_d \to b + X_s)$

The remaining parameters (`lamXsH` and `lamXs`) are not relevant for the mediator pair production at the LHC, but can have an impact on the DM production through the Higgs-portal.


### Event Generation

Cards for event generation can be found in [Cards](./DMsimpt_quarks/Cards) and can be used to generate
parton-level events with MadGraph5.
For instance, the up-type mediator production can be computed at LO (NLO) using the MadGraph5 syntax: `p p > yf yf~` (`p p > yf yf~ [QCD]`).


--------------------------------------
## References

### Papers:

* [LHC-friendly freeze-in model paper](https://arxiv.org/abs/1811.05478)

* [t-channel dark matter models – a whitepaper](https://arxiv.org/abs/2504.10597)

### FeynRules Model Database:

* [Simplified Freeze-in model](http://feynrules.irmp.ucl.ac.be/wiki/FICPLHC)

* [t-Channel DM Models database](http://feynrules.irmp.ucl.ac.be/wiki/DMsimpt)
