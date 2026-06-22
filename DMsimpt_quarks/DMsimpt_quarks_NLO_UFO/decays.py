# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.3.1 for Linux x86 (64-bit) (July 24, 2023)
# Date: Mon 22 Jun 2026 18:48:24


from object_library import all_decays, Decay
import particles as P


Decay_b = Decay(name = 'Decay_b',
                particle = P.b,
                partial_widths = {(P.W__minus__,P.t):'(((3*ee**2*MB**2)/(2.*sw**2) + (3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MB**4)/(2.*MW**2*sw**2) - (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MB)**3)',
                                  (P.Xs,P.YFd):'((12*MB**2*yFbR**2 - 12*MX**2*yFbR**2 + 12*MYd**2*yFbR**2)*cmath.sqrt(MB**4 - 2*MB**2*MX**2 + MX**4 - 2*MB**2*MYd**2 - 2*MX**2*MYd**2 + MYd**4))/(96.*cmath.pi*abs(MB)**3)'})

Decay_H = Decay(name = 'Decay_H',
                particle = P.H,
                partial_widths = {(P.b,P.b__tilde__):'((-12*MB**2*yb**2 + 3*MH**2*yb**2)*cmath.sqrt(-4*MB**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.t,P.t__tilde__):'((3*MH**2*yt**2 - 12*MT**2*yt**2)*cmath.sqrt(MH**4 - 4*MH**2*MT**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((MH**2*ytau**2 - 4*MTA**2*ytau**2)*cmath.sqrt(MH**4 - 4*MH**2*MTA**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.W__minus__,P.W__plus__):'(((3*ee**4*vev**2)/(4.*sw**4) + (ee**4*MH**4*vev**2)/(16.*MW**4*sw**4) - (ee**4*MH**2*vev**2)/(4.*MW**2*sw**4))*cmath.sqrt(MH**4 - 4*MH**2*MW**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.Xs,P.Xs):'(lamXsH**2*vev**2*cmath.sqrt(MH**4 - 4*MH**2*MX**2))/(8.*cmath.pi*abs(MH)**3)',
                                  (P.Z,P.Z):'(((9*ee**4*vev**2)/2. + (3*ee**4*MH**4*vev**2)/(8.*MZ**4) - (3*ee**4*MH**2*vev**2)/(2.*MZ**2) + (3*cw**4*ee**4*vev**2)/(4.*sw**4) + (cw**4*ee**4*MH**4*vev**2)/(16.*MZ**4*sw**4) - (cw**4*ee**4*MH**2*vev**2)/(4.*MZ**2*sw**4) + (3*cw**2*ee**4*vev**2)/sw**2 + (cw**2*ee**4*MH**4*vev**2)/(4.*MZ**4*sw**2) - (cw**2*ee**4*MH**2*vev**2)/(MZ**2*sw**2) + (3*ee**4*sw**2*vev**2)/cw**2 + (ee**4*MH**4*sw**2*vev**2)/(4.*cw**2*MZ**4) - (ee**4*MH**2*sw**2*vev**2)/(cw**2*MZ**2) + (3*ee**4*sw**4*vev**2)/(4.*cw**4) + (ee**4*MH**4*sw**4*vev**2)/(16.*cw**4*MZ**4) - (ee**4*MH**2*sw**4*vev**2)/(4.*cw**4*MZ**2))*cmath.sqrt(MH**4 - 4*MH**2*MZ**2))/(32.*cmath.pi*abs(MH)**3)'})

Decay_t = Decay(name = 'Decay_t',
                particle = P.t,
                partial_widths = {(P.W__plus__,P.b):'(((3*ee**2*MB**2)/(2.*sw**2) + (3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MB**4)/(2.*MW**2*sw**2) - (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.Xs,P.YFu):'((12*MT**2*yFtR**2 - 12*MX**2*yFtR**2 + 12*MYu**2*yFtR**2)*cmath.sqrt(MT**4 - 2*MT**2*MX**2 + MX**4 - 2*MT**2*MYu**2 - 2*MX**2*MYu**2 + MYu**4))/(96.*cmath.pi*abs(MT)**3)'})

Decay_ta__minus__ = Decay(name = 'Decay_ta__minus__',
                          particle = P.ta__minus__,
                          partial_widths = {(P.W__minus__,P.vt):'((MTA**2 - MW**2)*((ee**2*MTA**2)/(2.*sw**2) + (ee**2*MTA**4)/(2.*MW**2*sw**2) - (ee**2*MW**2)/sw**2))/(32.*cmath.pi*abs(MTA)**3)'})

Decay_W__plus__ = Decay(name = 'Decay_W__plus__',
                        particle = P.W__plus__,
                        partial_widths = {(P.c,P.s__tilde__):'(ee**2*MW**4)/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.t,P.b__tilde__):'(((-3*ee**2*MB**2)/(2.*sw**2) - (3*ee**2*MT**2)/(2.*sw**2) - (3*ee**2*MB**4)/(2.*MW**2*sw**2) + (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) - (3*ee**2*MT**4)/(2.*MW**2*sw**2) + (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.u,P.d__tilde__):'(ee**2*MW**4)/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.ve,P.e__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vm,P.mu__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vt,P.ta__plus__):'((-MTA**2 + MW**2)*(-0.5*(ee**2*MTA**2)/sw**2 - (ee**2*MTA**4)/(2.*MW**2*sw**2) + (ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)'})

Decay_Xs = Decay(name = 'Decay_Xs',
                 particle = P.Xs,
                 partial_widths = {(P.b,P.YFd__tilde__):'((-12*MB**2*yFbR**2 + 12*MX**2*yFbR**2 - 12*MYd**2*yFbR**2)*cmath.sqrt(MB**4 - 2*MB**2*MX**2 + MX**4 - 2*MB**2*MYd**2 - 2*MX**2*MYd**2 + MYd**4))/(16.*cmath.pi*abs(MX)**3)',
                                   (P.c,P.YFu__tilde__):'((MX**2 - MYu**2)*(3*MX**2*yFqR**2 - 3*MYu**2*yFqR**2))/(16.*cmath.pi*abs(MX)**3)',
                                   (P.d,P.YFd__tilde__):'((MX**2 - MYd**2)*(3*MX**2*yFqR**2 - 3*MYd**2*yFqR**2))/(16.*cmath.pi*abs(MX)**3)',
                                   (P.s,P.YFd__tilde__):'((MX**2 - MYd**2)*(3*MX**2*yFqR**2 - 3*MYd**2*yFqR**2))/(16.*cmath.pi*abs(MX)**3)',
                                   (P.t,P.YFu__tilde__):'((-12*MT**2*yFtR**2 + 12*MX**2*yFtR**2 - 12*MYu**2*yFtR**2)*cmath.sqrt(MT**4 - 2*MT**2*MX**2 + MX**4 - 2*MT**2*MYu**2 - 2*MX**2*MYu**2 + MYu**4))/(16.*cmath.pi*abs(MX)**3)',
                                   (P.u,P.YFu__tilde__):'((MX**2 - MYu**2)*(3*MX**2*yFqR**2 - 3*MYu**2*yFqR**2))/(16.*cmath.pi*abs(MX)**3)',
                                   (P.YFd,P.b__tilde__):'((-12*MB**2*yFbR**2 + 12*MX**2*yFbR**2 - 12*MYd**2*yFbR**2)*cmath.sqrt(MB**4 - 2*MB**2*MX**2 + MX**4 - 2*MB**2*MYd**2 - 2*MX**2*MYd**2 + MYd**4))/(16.*cmath.pi*abs(MX)**3)',
                                   (P.YFd,P.d__tilde__):'((MX**2 - MYd**2)*(3*MX**2*yFqR**2 - 3*MYd**2*yFqR**2))/(16.*cmath.pi*abs(MX)**3)',
                                   (P.YFd,P.s__tilde__):'((MX**2 - MYd**2)*(3*MX**2*yFqR**2 - 3*MYd**2*yFqR**2))/(16.*cmath.pi*abs(MX)**3)',
                                   (P.YFu,P.c__tilde__):'((MX**2 - MYu**2)*(3*MX**2*yFqR**2 - 3*MYu**2*yFqR**2))/(16.*cmath.pi*abs(MX)**3)',
                                   (P.YFu,P.t__tilde__):'((-12*MT**2*yFtR**2 + 12*MX**2*yFtR**2 - 12*MYu**2*yFtR**2)*cmath.sqrt(MT**4 - 2*MT**2*MX**2 + MX**4 - 2*MT**2*MYu**2 - 2*MX**2*MYu**2 + MYu**4))/(16.*cmath.pi*abs(MX)**3)',
                                   (P.YFu,P.u__tilde__):'((MX**2 - MYu**2)*(3*MX**2*yFqR**2 - 3*MYu**2*yFqR**2))/(16.*cmath.pi*abs(MX)**3)'})

Decay_YFd = Decay(name = 'Decay_YFd',
                  particle = P.YFd,
                  partial_widths = {(P.Xs,P.b):'((12*MB**2*yFbR**2 - 12*MX**2*yFbR**2 + 12*MYd**2*yFbR**2)*cmath.sqrt(MB**4 - 2*MB**2*MX**2 + MX**4 - 2*MB**2*MYd**2 - 2*MX**2*MYd**2 + MYd**4))/(96.*cmath.pi*abs(MYd)**3)',
                                    (P.Xs,P.d):'((-MX**2 + MYd**2)*(-3*MX**2*yFqR**2 + 3*MYd**2*yFqR**2))/(96.*cmath.pi*abs(MYd)**3)',
                                    (P.Xs,P.s):'((-MX**2 + MYd**2)*(-3*MX**2*yFqR**2 + 3*MYd**2*yFqR**2))/(96.*cmath.pi*abs(MYd)**3)'})

Decay_YFu = Decay(name = 'Decay_YFu',
                  particle = P.YFu,
                  partial_widths = {(P.Xs,P.c):'((-MX**2 + MYu**2)*(-3*MX**2*yFqR**2 + 3*MYu**2*yFqR**2))/(96.*cmath.pi*abs(MYu)**3)',
                                    (P.Xs,P.t):'((12*MT**2*yFtR**2 - 12*MX**2*yFtR**2 + 12*MYu**2*yFtR**2)*cmath.sqrt(MT**4 - 2*MT**2*MX**2 + MX**4 - 2*MT**2*MYu**2 - 2*MX**2*MYu**2 + MYu**4))/(96.*cmath.pi*abs(MYu)**3)',
                                    (P.Xs,P.u):'((-MX**2 + MYu**2)*(-3*MX**2*yFqR**2 + 3*MYu**2*yFqR**2))/(96.*cmath.pi*abs(MYu)**3)'})

Decay_Z = Decay(name = 'Decay_Z',
                particle = P.Z,
                partial_widths = {(P.b,P.b__tilde__):'((-7*ee**2*MB**2 + ee**2*MZ**2 - (3*cw**2*ee**2*MB**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) - (17*ee**2*MB**2*sw**2)/(6.*cw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MB**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.c,P.c__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.d,P.d__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.e__minus__,P.e__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.mu__minus__,P.mu__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.s,P.s__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.t,P.t__tilde__):'((-11*ee**2*MT**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MT**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MT**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MT**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((-5*ee**2*MTA**2 - ee**2*MZ**2 - (cw**2*ee**2*MTA**2)/(2.*sw**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MTA**2*sw**2)/(2.*cw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2))*cmath.sqrt(-4*MTA**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.u,P.u__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ve,P.ve__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vm,P.vm__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vt,P.vt__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.W__minus__,P.W__plus__):'(((-12*cw**2*ee**2*MW**2)/sw**2 - (17*cw**2*ee**2*MZ**2)/sw**2 + (4*cw**2*ee**2*MZ**4)/(MW**2*sw**2) + (cw**2*ee**2*MZ**6)/(4.*MW**4*sw**2))*cmath.sqrt(-4*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.YFd,P.YFd__tilde__):'(((8*ee**2*MYd**2*sw**2)/(9.*cw**2) + (4*ee**2*MZ**2*sw**2)/(9.*cw**2))*cmath.sqrt(-4*MYd**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.YFu,P.YFu__tilde__):'(((32*ee**2*MYu**2*sw**2)/(9.*cw**2) + (16*ee**2*MZ**2*sw**2)/(9.*cw**2))*cmath.sqrt(-4*MYu**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)'})

