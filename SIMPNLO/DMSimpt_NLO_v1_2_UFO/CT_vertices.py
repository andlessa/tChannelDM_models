# This file was automatically created by FeynRules 2.4.91
# Mathematica version: 13.3.1 for Linux x86 (64-bit) (July 24, 2023)
# Date: Tue 23 Jun 2026 14:44:53


from object_library import all_vertices, all_CTvertices, Vertex, CTVertex
import particles as P
import CT_couplings as C
import lorentz as L


V_1 = CTVertex(name = 'V_1',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV2, L.VVV3, L.VVV4, L.VVV5, L.VVV6, L.VVV7 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u], [P.YF3d1], [P.YF3d2], [P.YF3d3], [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3], [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3], [P.YF3u1], [P.YF3u2], [P.YF3u3] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_231_93,(0,0,1):C.R2GC_231_94,(0,1,0):C.R2GC_230_91,(0,1,1):C.R2GC_230_92,(0,2,0):C.R2GC_230_91,(0,2,1):C.R2GC_230_92,(0,3,0):C.R2GC_231_93,(0,3,1):C.R2GC_231_94,(0,4,0):C.R2GC_231_93,(0,4,1):C.R2GC_231_94,(0,5,0):C.R2GC_230_91,(0,5,1):C.R2GC_230_92})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u], [P.YF3d1], [P.YF3d2], [P.YF3d3], [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3], [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3], [P.YF3u1], [P.YF3u2], [P.YF3u3] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_226_86,(0,0,1):C.R2GC_226_87,(2,0,0):C.R2GC_226_86,(2,0,1):C.R2GC_226_87,(5,0,0):C.R2GC_224_82,(5,0,1):C.R2GC_224_83,(1,0,0):C.R2GC_224_82,(1,0,1):C.R2GC_224_83,(7,0,0):C.R2GC_234_99,(7,0,1):C.R2GC_234_100,(6,0,0):C.R2GC_233_97,(6,0,1):C.R2GC_233_98,(4,0,0):C.R2GC_224_82,(4,0,1):C.R2GC_224_83,(3,0,0):C.R2GC_224_82,(3,0,1):C.R2GC_224_83,(8,0,0):C.R2GC_225_84,(8,0,1):C.R2GC_225_85,(11,0,0):C.R2GC_228_89,(11,0,1):C.R2GC_228_90,(10,0,0):C.R2GC_228_89,(10,0,1):C.R2GC_228_90,(9,0,1):C.R2GC_227_88,(0,1,0):C.R2GC_226_86,(0,1,1):C.R2GC_226_87,(2,1,0):C.R2GC_226_86,(2,1,1):C.R2GC_226_87,(7,1,0):C.R2GC_234_99,(7,1,1):C.R2GC_225_85,(5,1,0):C.R2GC_224_82,(5,1,1):C.R2GC_224_83,(1,1,0):C.R2GC_224_82,(1,1,1):C.R2GC_224_83,(4,1,0):C.R2GC_224_82,(4,1,1):C.R2GC_224_83,(3,1,0):C.R2GC_224_82,(3,1,1):C.R2GC_224_83,(8,1,0):C.R2GC_225_84,(8,1,1):C.R2GC_234_100,(6,1,0):C.R2GC_239_101,(6,1,1):C.R2GC_239_102,(11,1,0):C.R2GC_228_89,(11,1,1):C.R2GC_228_90,(10,1,0):C.R2GC_228_89,(10,1,1):C.R2GC_228_90,(9,1,1):C.R2GC_227_88,(0,2,0):C.R2GC_226_86,(0,2,1):C.R2GC_226_87,(2,2,0):C.R2GC_226_86,(2,2,1):C.R2GC_226_87,(7,2,0):C.R2GC_232_95,(7,2,1):C.R2GC_232_96,(5,2,0):C.R2GC_224_82,(5,2,1):C.R2GC_224_83,(1,2,0):C.R2GC_224_82,(1,2,1):C.R2GC_224_83,(4,2,0):C.R2GC_224_82,(4,2,1):C.R2GC_224_83,(3,2,0):C.R2GC_224_82,(3,2,1):C.R2GC_224_83,(8,2,0):C.R2GC_225_84,(8,2,1):C.R2GC_232_96,(6,2,0):C.R2GC_233_97,(11,2,0):C.R2GC_228_89,(11,2,1):C.R2GC_228_90,(10,2,0):C.R2GC_228_89,(10,2,1):C.R2GC_228_90,(9,2,1):C.R2GC_227_88})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.YF3d1__tilde__, P.YF3d1, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.YF3d1] ] ],
               couplings = {(0,0,0):C.R2GC_243_104})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.YF3d2__tilde__, P.YF3d2, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.YF3d2] ] ],
               couplings = {(0,0,0):C.R2GC_243_104})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.YF3d3__tilde__, P.YF3d3, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.YF3d3] ] ],
               couplings = {(0,0,0):C.R2GC_243_104})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.YF3Qd1__tilde__, P.YF3Qd1, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.YF3Qd1] ] ],
               couplings = {(0,0,0):C.R2GC_243_104})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.YF3Qd2__tilde__, P.YF3Qd2, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.YF3Qd2] ] ],
               couplings = {(0,0,0):C.R2GC_243_104})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.YF3Qd3__tilde__, P.YF3Qd3, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.YF3Qd3] ] ],
               couplings = {(0,0,0):C.R2GC_243_104})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.YF3Qu1__tilde__, P.YF3Qu1, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.YF3Qu1] ] ],
               couplings = {(0,0,0):C.R2GC_250_108})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.YF3Qu2__tilde__, P.YF3Qu2, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_250_108})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.YF3Qu3__tilde__, P.YF3Qu3, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_250_108})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.YF3u1__tilde__, P.YF3u1, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3u1] ] ],
                couplings = {(0,0,0):C.R2GC_250_108})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.YF3u2__tilde__, P.YF3u2, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3u2] ] ],
                couplings = {(0,0,0):C.R2GC_250_108})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.YF3u3__tilde__, P.YF3u3, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3u3] ] ],
                couplings = {(0,0,0):C.R2GC_250_108})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.u__tilde__, P.YF3Qu1, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                couplings = {(0,0,0):C.R2GC_597_192})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.u__tilde__, P.YF3Qu1, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                couplings = {(0,0,0):C.R2GC_597_192})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.d__tilde__, P.YF3Qd1, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                couplings = {(0,0,0):C.R2GC_597_192})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.d__tilde__, P.YF3Qd1, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                couplings = {(0,0,0):C.R2GC_597_192})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.c__tilde__, P.YF3Qu2, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_589_184})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.c__tilde__, P.YF3Qu2, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_589_184})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.s__tilde__, P.YF3Qd2, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                couplings = {(0,0,0):C.R2GC_589_184})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.s__tilde__, P.YF3Qd2, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                couplings = {(0,0,0):C.R2GC_589_184})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.t__tilde__, P.YF3Qu3, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_584_179})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.t__tilde__, P.YF3Qu3, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_584_179})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.b__tilde__, P.YF3Qd3, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                couplings = {(0,0,0):C.R2GC_584_179})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.b__tilde__, P.YF3Qd3, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                couplings = {(0,0,0):C.R2GC_584_179})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.YF3d1__tilde__, P.d, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                couplings = {(0,0,0):C.R2GC_595_190})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.YF3d2__tilde__, P.s, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                couplings = {(0,0,0):C.R2GC_760_209})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.YF3d3__tilde__, P.b, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                couplings = {(0,0,0):C.R2GC_582_177})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.YF3d1__tilde__, P.d, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                couplings = {(0,0,0):C.R2GC_595_190})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.YF3d2__tilde__, P.s, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                couplings = {(0,0,0):C.R2GC_760_209})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.YF3d3__tilde__, P.b, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                couplings = {(0,0,0):C.R2GC_582_177})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.YF3u1__tilde__, P.u, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                couplings = {(0,0,0):C.R2GC_778_217})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.YF3u2__tilde__, P.c, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                couplings = {(0,0,0):C.R2GC_591_186})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.YF3u3__tilde__, P.t, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                couplings = {(0,0,0):C.R2GC_771_214})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.YF3u1__tilde__, P.u, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                couplings = {(0,0,0):C.R2GC_778_217})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.YF3u2__tilde__, P.c, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                couplings = {(0,0,0):C.R2GC_591_186})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.YF3u3__tilde__, P.t, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                couplings = {(0,0,0):C.R2GC_771_214})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_764_210})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_469_161})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_468_160})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.d__tilde__, P.YF3d1, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                couplings = {(0,0,0):C.R2GC_595_190})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.s__tilde__, P.YF3d2, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                couplings = {(0,0,0):C.R2GC_760_209})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.b__tilde__, P.YF3d3, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                couplings = {(0,0,0):C.R2GC_582_177})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.d__tilde__, P.YF3d1, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                couplings = {(0,0,0):C.R2GC_595_190})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.s__tilde__, P.YF3d2, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                couplings = {(0,0,0):C.R2GC_760_209})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.b__tilde__, P.YF3d3, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                couplings = {(0,0,0):C.R2GC_582_177})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.u__tilde__, P.YF3u1, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                couplings = {(0,0,0):C.R2GC_778_217})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.c__tilde__, P.YF3u2, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                couplings = {(0,0,0):C.R2GC_591_186})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.t__tilde__, P.YF3u3, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                couplings = {(0,0,0):C.R2GC_771_214})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.u__tilde__, P.YF3u1, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                couplings = {(0,0,0):C.R2GC_778_217})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.c__tilde__, P.YF3u2, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                couplings = {(0,0,0):C.R2GC_591_186})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.t__tilde__, P.YF3u3, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                couplings = {(0,0,0):C.R2GC_771_214})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.YF3Qu1__tilde__, P.u, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                couplings = {(0,0,0):C.R2GC_597_192})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.YF3Qu1__tilde__, P.u, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                couplings = {(0,0,0):C.R2GC_597_192})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.YF3Qd1__tilde__, P.d, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                couplings = {(0,0,0):C.R2GC_597_192})

V_57 = CTVertex(name = 'V_57',
                type = 'R2',
                particles = [ P.YF3Qd1__tilde__, P.d, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                couplings = {(0,0,0):C.R2GC_597_192})

V_58 = CTVertex(name = 'V_58',
                type = 'R2',
                particles = [ P.YF3Qu2__tilde__, P.c, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_589_184})

V_59 = CTVertex(name = 'V_59',
                type = 'R2',
                particles = [ P.YF3Qu2__tilde__, P.c, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_589_184})

V_60 = CTVertex(name = 'V_60',
                type = 'R2',
                particles = [ P.YF3Qd2__tilde__, P.s, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                couplings = {(0,0,0):C.R2GC_589_184})

V_61 = CTVertex(name = 'V_61',
                type = 'R2',
                particles = [ P.YF3Qd2__tilde__, P.s, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                couplings = {(0,0,0):C.R2GC_589_184})

V_62 = CTVertex(name = 'V_62',
                type = 'R2',
                particles = [ P.YF3Qu3__tilde__, P.t, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_584_179})

V_63 = CTVertex(name = 'V_63',
                type = 'R2',
                particles = [ P.YF3Qu3__tilde__, P.t, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_584_179})

V_64 = CTVertex(name = 'V_64',
                type = 'R2',
                particles = [ P.YF3Qd3__tilde__, P.b, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                couplings = {(0,0,0):C.R2GC_584_179})

V_65 = CTVertex(name = 'V_65',
                type = 'R2',
                particles = [ P.YF3Qd3__tilde__, P.b, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                couplings = {(0,0,0):C.R2GC_584_179})

V_66 = CTVertex(name = 'V_66',
                type = 'R2',
                particles = [ P.YF3Qd1__tilde__, P.YF3Qd1, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd1] ] ],
                couplings = {(0,0,0):C.R2GC_244_105})

V_67 = CTVertex(name = 'V_67',
                type = 'R2',
                particles = [ P.YF3Qd2__tilde__, P.YF3Qd2, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd2] ] ],
                couplings = {(0,0,0):C.R2GC_244_105})

V_68 = CTVertex(name = 'V_68',
                type = 'R2',
                particles = [ P.YF3Qd3__tilde__, P.YF3Qd3, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd3] ] ],
                couplings = {(0,0,0):C.R2GC_244_105})

V_69 = CTVertex(name = 'V_69',
                type = 'R2',
                particles = [ P.YF3Qu1__tilde__, P.YF3Qu1, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qu1] ] ],
                couplings = {(0,0,0):C.R2GC_244_105})

V_70 = CTVertex(name = 'V_70',
                type = 'R2',
                particles = [ P.YF3Qu2__tilde__, P.YF3Qu2, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_244_105})

V_71 = CTVertex(name = 'V_71',
                type = 'R2',
                particles = [ P.YF3Qu3__tilde__, P.YF3Qu3, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_244_105})

V_72 = CTVertex(name = 'V_72',
                type = 'R2',
                particles = [ P.YF3u1__tilde__, P.YF3u1, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3u1] ] ],
                couplings = {(0,0,0):C.R2GC_244_105})

V_73 = CTVertex(name = 'V_73',
                type = 'R2',
                particles = [ P.YF3u2__tilde__, P.YF3u2, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3u2] ] ],
                couplings = {(0,0,0):C.R2GC_244_105})

V_74 = CTVertex(name = 'V_74',
                type = 'R2',
                particles = [ P.YF3u3__tilde__, P.YF3u3, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3u3] ] ],
                couplings = {(0,0,0):C.R2GC_244_105})

V_75 = CTVertex(name = 'V_75',
                type = 'R2',
                particles = [ P.YF3d1__tilde__, P.YF3d1, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3d1] ] ],
                couplings = {(0,0,0):C.R2GC_244_105})

V_76 = CTVertex(name = 'V_76',
                type = 'R2',
                particles = [ P.YF3d2__tilde__, P.YF3d2, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3d2] ] ],
                couplings = {(0,0,0):C.R2GC_244_105})

V_77 = CTVertex(name = 'V_77',
                type = 'R2',
                particles = [ P.YF3d3__tilde__, P.YF3d3, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3d3] ] ],
                couplings = {(0,0,0):C.R2GC_244_105})

V_78 = CTVertex(name = 'V_78',
                type = 'R2',
                particles = [ P.YF3Qd1__tilde__, P.YF3Qu1, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd1, P.YF3Qu1] ] ],
                couplings = {(0,0,0):C.R2GC_587_182})

V_79 = CTVertex(name = 'V_79',
                type = 'R2',
                particles = [ P.YF3Qd2__tilde__, P.YF3Qu2, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd2, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_587_182})

V_80 = CTVertex(name = 'V_80',
                type = 'R2',
                particles = [ P.YF3Qd3__tilde__, P.YF3Qu3, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd3, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_587_182})

V_81 = CTVertex(name = 'V_81',
                type = 'R2',
                particles = [ P.YF3Qu1__tilde__, P.YF3Qd1, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd1, P.YF3Qu1] ] ],
                couplings = {(0,0,0):C.R2GC_587_182})

V_82 = CTVertex(name = 'V_82',
                type = 'R2',
                particles = [ P.YF3Qu2__tilde__, P.YF3Qd2, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd2, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_587_182})

V_83 = CTVertex(name = 'V_83',
                type = 'R2',
                particles = [ P.YF3Qu3__tilde__, P.YF3Qd3, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd3, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_587_182})

V_84 = CTVertex(name = 'V_84',
                type = 'R2',
                particles = [ P.a, P.YS3d1__tilde__, P.YS3d1 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1, L.VSS2 ],
                loop_particles = [ [ [P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_263_113,(0,1,0):C.R2GC_262_112})

V_85 = CTVertex(name = 'V_85',
                type = 'R2',
                particles = [ P.Xd__tilde__, P.d, P.YS3d1__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_592_187})

V_86 = CTVertex(name = 'V_86',
                type = 'R2',
                particles = [ P.Xm, P.d, P.YS3d1__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_592_187})

V_87 = CTVertex(name = 'V_87',
                type = 'R2',
                particles = [ P.g, P.YS3d1__tilde__, P.YS3d1 ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS1, L.VSS2 ],
                loop_particles = [ [ [P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_266_116,(0,1,0):C.R2GC_265_115})

V_88 = CTVertex(name = 'V_88',
                type = 'R2',
                particles = [ P.d__tilde__, P.Xd, P.YS3d1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_592_187})

V_89 = CTVertex(name = 'V_89',
                type = 'R2',
                particles = [ P.d__tilde__, P.Xm, P.YS3d1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_592_187})

V_90 = CTVertex(name = 'V_90',
                type = 'R2',
                particles = [ P.a, P.a, P.YS3d1__tilde__, P.YS3d1 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_264_114})

V_91 = CTVertex(name = 'V_91',
                type = 'R2',
                particles = [ P.a, P.g, P.YS3d1__tilde__, P.YS3d1 ],
                color = [ 'T(2,4,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_267_117})

V_92 = CTVertex(name = 'V_92',
                type = 'R2',
                particles = [ P.g, P.g, P.YS3d1__tilde__, P.YS3d1 ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g] ], [ [P.g, P.YS3d1] ] ],
                couplings = {(2,0,0):C.R2GC_270_121,(2,0,1):C.R2GC_270_122,(1,0,0):C.R2GC_270_121,(1,0,1):C.R2GC_270_122,(0,0,0):C.R2GC_228_90,(0,0,1):C.R2GC_269_120})

V_93 = CTVertex(name = 'V_93',
                type = 'R2',
                particles = [ P.a, P.YS3d2__tilde__, P.YS3d2 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1, L.VSS2 ],
                loop_particles = [ [ [P.g, P.YS3d2] ] ],
                couplings = {(0,0,0):C.R2GC_263_113,(0,1,0):C.R2GC_262_112})

V_94 = CTVertex(name = 'V_94',
                type = 'R2',
                particles = [ P.Xd__tilde__, P.s, P.YS3d2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.YS3d2] ] ],
                couplings = {(0,0,0):C.R2GC_757_207})

V_95 = CTVertex(name = 'V_95',
                type = 'R2',
                particles = [ P.Xm, P.s, P.YS3d2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.YS3d2] ] ],
                couplings = {(0,0,0):C.R2GC_757_207})

V_96 = CTVertex(name = 'V_96',
                type = 'R2',
                particles = [ P.g, P.YS3d2__tilde__, P.YS3d2 ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS1, L.VSS2 ],
                loop_particles = [ [ [P.g, P.YS3d2] ] ],
                couplings = {(0,0,0):C.R2GC_266_116,(0,1,0):C.R2GC_265_115})

V_97 = CTVertex(name = 'V_97',
                type = 'R2',
                particles = [ P.s__tilde__, P.Xd, P.YS3d2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.s, P.YS3d2] ] ],
                couplings = {(0,0,0):C.R2GC_757_207})

V_98 = CTVertex(name = 'V_98',
                type = 'R2',
                particles = [ P.s__tilde__, P.Xm, P.YS3d2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.s, P.YS3d2] ] ],
                couplings = {(0,0,0):C.R2GC_757_207})

V_99 = CTVertex(name = 'V_99',
                type = 'R2',
                particles = [ P.a, P.a, P.YS3d2__tilde__, P.YS3d2 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.YS3d2] ] ],
                couplings = {(0,0,0):C.R2GC_264_114})

V_100 = CTVertex(name = 'V_100',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_267_117})

V_101 = CTVertex(name = 'V_101',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3d2] ] ],
                 couplings = {(2,0,0):C.R2GC_270_121,(2,0,1):C.R2GC_270_122,(1,0,0):C.R2GC_270_121,(1,0,1):C.R2GC_270_122,(0,0,0):C.R2GC_228_90,(0,0,1):C.R2GC_269_120})

V_102 = CTVertex(name = 'V_102',
                 type = 'R2',
                 particles = [ P.a, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_263_113,(0,1,0):C.R2GC_262_112})

V_103 = CTVertex(name = 'V_103',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.b, P.YS3d3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_579_174})

V_104 = CTVertex(name = 'V_104',
                 type = 'R2',
                 particles = [ P.Xm, P.b, P.YS3d3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_579_174})

V_105 = CTVertex(name = 'V_105',
                 type = 'R2',
                 particles = [ P.g, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_266_116,(0,1,0):C.R2GC_265_115})

V_106 = CTVertex(name = 'V_106',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.Xd, P.YS3d3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_579_174})

V_107 = CTVertex(name = 'V_107',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.Xm, P.YS3d3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_579_174})

V_108 = CTVertex(name = 'V_108',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_264_114})

V_109 = CTVertex(name = 'V_109',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_267_117})

V_110 = CTVertex(name = 'V_110',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3d3] ] ],
                 couplings = {(2,0,0):C.R2GC_270_121,(2,0,1):C.R2GC_270_122,(1,0,0):C.R2GC_270_121,(1,0,1):C.R2GC_270_122,(0,0,0):C.R2GC_228_90,(0,0,1):C.R2GC_269_120})

V_111 = CTVertex(name = 'V_111',
                 type = 'R2',
                 particles = [ P.a, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_263_113,(0,1,0):C.R2GC_262_112})

V_112 = CTVertex(name = 'V_112',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.d, P.YS3Qd1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_593_188})

V_113 = CTVertex(name = 'V_113',
                 type = 'R2',
                 particles = [ P.Xm, P.d, P.YS3Qd1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_593_188})

V_114 = CTVertex(name = 'V_114',
                 type = 'R2',
                 particles = [ P.W__minus__, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_659_203,(0,1,0):C.R2GC_657_202})

V_115 = CTVertex(name = 'V_115',
                 type = 'R2',
                 particles = [ P.g, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_266_116,(0,1,0):C.R2GC_265_115})

V_116 = CTVertex(name = 'V_116',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.Xd, P.YS3Qd1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_593_188})

V_117 = CTVertex(name = 'V_117',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.Xm, P.YS3Qd1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_593_188})

V_118 = CTVertex(name = 'V_118',
                 type = 'R2',
                 particles = [ P.W__plus__, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_657_202,(0,1,0):C.R2GC_659_203})

V_119 = CTVertex(name = 'V_119',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_264_114})

V_120 = CTVertex(name = 'V_120',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_655_200,(0,0,1):C.R2GC_655_201})

V_121 = CTVertex(name = 'V_121',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_267_117})

V_122 = CTVertex(name = 'V_122',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(2,0,0):C.R2GC_270_121,(2,0,1):C.R2GC_270_122,(1,0,0):C.R2GC_270_121,(1,0,1):C.R2GC_270_122,(0,0,0):C.R2GC_228_90,(0,0,1):C.R2GC_269_120})

V_123 = CTVertex(name = 'V_123',
                 type = 'R2',
                 particles = [ P.a, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_263_113,(0,1,0):C.R2GC_262_112})

V_124 = CTVertex(name = 'V_124',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.s, P.YS3Qd2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_585_180})

V_125 = CTVertex(name = 'V_125',
                 type = 'R2',
                 particles = [ P.Xm, P.s, P.YS3Qd2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_585_180})

V_126 = CTVertex(name = 'V_126',
                 type = 'R2',
                 particles = [ P.W__minus__, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_659_203,(0,1,0):C.R2GC_657_202})

V_127 = CTVertex(name = 'V_127',
                 type = 'R2',
                 particles = [ P.g, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_266_116,(0,1,0):C.R2GC_265_115})

V_128 = CTVertex(name = 'V_128',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.Xd, P.YS3Qd2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_585_180})

V_129 = CTVertex(name = 'V_129',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.Xm, P.YS3Qd2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_585_180})

V_130 = CTVertex(name = 'V_130',
                 type = 'R2',
                 particles = [ P.W__plus__, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_657_202,(0,1,0):C.R2GC_659_203})

V_131 = CTVertex(name = 'V_131',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_264_114})

V_132 = CTVertex(name = 'V_132',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_655_200,(0,0,1):C.R2GC_655_201})

V_133 = CTVertex(name = 'V_133',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_267_117})

V_134 = CTVertex(name = 'V_134',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(2,0,0):C.R2GC_270_121,(2,0,1):C.R2GC_270_122,(1,0,0):C.R2GC_270_121,(1,0,1):C.R2GC_270_122,(0,0,0):C.R2GC_228_90,(0,0,1):C.R2GC_269_120})

V_135 = CTVertex(name = 'V_135',
                 type = 'R2',
                 particles = [ P.a, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_263_113,(0,1,0):C.R2GC_262_112})

V_136 = CTVertex(name = 'V_136',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.b, P.YS3Qd3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_580_175})

V_137 = CTVertex(name = 'V_137',
                 type = 'R2',
                 particles = [ P.Xm, P.b, P.YS3Qd3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_580_175})

V_138 = CTVertex(name = 'V_138',
                 type = 'R2',
                 particles = [ P.W__minus__, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_659_203,(0,1,0):C.R2GC_657_202})

V_139 = CTVertex(name = 'V_139',
                 type = 'R2',
                 particles = [ P.g, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_266_116,(0,1,0):C.R2GC_265_115})

V_140 = CTVertex(name = 'V_140',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.Xd, P.YS3Qd3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_580_175})

V_141 = CTVertex(name = 'V_141',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.Xm, P.YS3Qd3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_580_175})

V_142 = CTVertex(name = 'V_142',
                 type = 'R2',
                 particles = [ P.W__plus__, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_657_202,(0,1,0):C.R2GC_659_203})

V_143 = CTVertex(name = 'V_143',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_264_114})

V_144 = CTVertex(name = 'V_144',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_655_200,(0,0,1):C.R2GC_655_201})

V_145 = CTVertex(name = 'V_145',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_267_117})

V_146 = CTVertex(name = 'V_146',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(2,0,0):C.R2GC_270_121,(2,0,1):C.R2GC_270_122,(1,0,0):C.R2GC_270_121,(1,0,1):C.R2GC_270_122,(0,0,0):C.R2GC_228_90,(0,0,1):C.R2GC_269_120})

V_147 = CTVertex(name = 'V_147',
                 type = 'R2',
                 particles = [ P.a, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_358_139,(0,1,0):C.R2GC_359_140})

V_148 = CTVertex(name = 'V_148',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.u, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_593_188})

V_149 = CTVertex(name = 'V_149',
                 type = 'R2',
                 particles = [ P.Xm, P.u, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_593_188})

V_150 = CTVertex(name = 'V_150',
                 type = 'R2',
                 particles = [ P.a, P.W__plus__, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_661_204})

V_151 = CTVertex(name = 'V_151',
                 type = 'R2',
                 particles = [ P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_662_205,(0,0,1):C.R2GC_662_206})

V_152 = CTVertex(name = 'V_152',
                 type = 'R2',
                 particles = [ P.g, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_266_116,(0,1,0):C.R2GC_265_115})

V_153 = CTVertex(name = 'V_153',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.Xd, P.YS3Qu1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_593_188})

V_154 = CTVertex(name = 'V_154',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.Xm, P.YS3Qu1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_593_188})

V_155 = CTVertex(name = 'V_155',
                 type = 'R2',
                 particles = [ P.a, P.W__minus__, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_661_204})

V_156 = CTVertex(name = 'V_156',
                 type = 'R2',
                 particles = [ P.g, P.W__minus__, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_662_205,(0,0,1):C.R2GC_662_206})

V_157 = CTVertex(name = 'V_157',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_360_141})

V_158 = CTVertex(name = 'V_158',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,1):C.R2GC_655_200,(0,0,0):C.R2GC_655_201})

V_159 = CTVertex(name = 'V_159',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_363_142})

V_160 = CTVertex(name = 'V_160',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(2,0,0):C.R2GC_270_121,(2,0,1):C.R2GC_270_122,(1,0,0):C.R2GC_270_121,(1,0,1):C.R2GC_270_122,(0,0,0):C.R2GC_228_90,(0,0,1):C.R2GC_269_120})

V_161 = CTVertex(name = 'V_161',
                 type = 'R2',
                 particles = [ P.a, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_358_139,(0,1,0):C.R2GC_359_140})

V_162 = CTVertex(name = 'V_162',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.c, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_585_180})

V_163 = CTVertex(name = 'V_163',
                 type = 'R2',
                 particles = [ P.Xm, P.c, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_585_180})

V_164 = CTVertex(name = 'V_164',
                 type = 'R2',
                 particles = [ P.a, P.W__plus__, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_661_204})

V_165 = CTVertex(name = 'V_165',
                 type = 'R2',
                 particles = [ P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_662_205,(0,0,1):C.R2GC_662_206})

V_166 = CTVertex(name = 'V_166',
                 type = 'R2',
                 particles = [ P.g, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_266_116,(0,1,0):C.R2GC_265_115})

V_167 = CTVertex(name = 'V_167',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.Xd, P.YS3Qu2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_585_180})

V_168 = CTVertex(name = 'V_168',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.Xm, P.YS3Qu2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_585_180})

V_169 = CTVertex(name = 'V_169',
                 type = 'R2',
                 particles = [ P.a, P.W__minus__, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_661_204})

V_170 = CTVertex(name = 'V_170',
                 type = 'R2',
                 particles = [ P.g, P.W__minus__, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_662_205,(0,0,1):C.R2GC_662_206})

V_171 = CTVertex(name = 'V_171',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_360_141})

V_172 = CTVertex(name = 'V_172',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,1):C.R2GC_655_200,(0,0,0):C.R2GC_655_201})

V_173 = CTVertex(name = 'V_173',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_363_142})

V_174 = CTVertex(name = 'V_174',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(2,0,0):C.R2GC_270_121,(2,0,1):C.R2GC_270_122,(1,0,0):C.R2GC_270_121,(1,0,1):C.R2GC_270_122,(0,0,0):C.R2GC_228_90,(0,0,1):C.R2GC_269_120})

V_175 = CTVertex(name = 'V_175',
                 type = 'R2',
                 particles = [ P.a, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_358_139,(0,1,0):C.R2GC_359_140})

V_176 = CTVertex(name = 'V_176',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.t, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_580_175})

V_177 = CTVertex(name = 'V_177',
                 type = 'R2',
                 particles = [ P.Xm, P.t, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_580_175})

V_178 = CTVertex(name = 'V_178',
                 type = 'R2',
                 particles = [ P.a, P.W__plus__, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_661_204})

V_179 = CTVertex(name = 'V_179',
                 type = 'R2',
                 particles = [ P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_662_205,(0,0,1):C.R2GC_662_206})

V_180 = CTVertex(name = 'V_180',
                 type = 'R2',
                 particles = [ P.g, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_266_116,(0,1,0):C.R2GC_265_115})

V_181 = CTVertex(name = 'V_181',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.Xd, P.YS3Qu3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_580_175})

V_182 = CTVertex(name = 'V_182',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.Xm, P.YS3Qu3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_580_175})

V_183 = CTVertex(name = 'V_183',
                 type = 'R2',
                 particles = [ P.a, P.W__minus__, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_661_204})

V_184 = CTVertex(name = 'V_184',
                 type = 'R2',
                 particles = [ P.g, P.W__minus__, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_662_205,(0,0,1):C.R2GC_662_206})

V_185 = CTVertex(name = 'V_185',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_360_141})

V_186 = CTVertex(name = 'V_186',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,1):C.R2GC_655_200,(0,0,0):C.R2GC_655_201})

V_187 = CTVertex(name = 'V_187',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_363_142})

V_188 = CTVertex(name = 'V_188',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(2,0,0):C.R2GC_270_121,(2,0,1):C.R2GC_270_122,(1,0,0):C.R2GC_270_121,(1,0,1):C.R2GC_270_122,(0,0,0):C.R2GC_228_90,(0,0,1):C.R2GC_269_120})

V_189 = CTVertex(name = 'V_189',
                 type = 'R2',
                 particles = [ P.a, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_358_139,(0,1,0):C.R2GC_359_140})

V_190 = CTVertex(name = 'V_190',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.u, P.YS3u1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_774_215})

V_191 = CTVertex(name = 'V_191',
                 type = 'R2',
                 particles = [ P.Xm, P.u, P.YS3u1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_774_215})

V_192 = CTVertex(name = 'V_192',
                 type = 'R2',
                 particles = [ P.g, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_266_116,(0,1,0):C.R2GC_265_115})

V_193 = CTVertex(name = 'V_193',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.Xd, P.YS3u1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_774_215})

V_194 = CTVertex(name = 'V_194',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.Xm, P.YS3u1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_774_215})

V_195 = CTVertex(name = 'V_195',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_360_141})

V_196 = CTVertex(name = 'V_196',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_363_142})

V_197 = CTVertex(name = 'V_197',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3u1] ] ],
                 couplings = {(2,0,0):C.R2GC_270_121,(2,0,1):C.R2GC_270_122,(1,0,0):C.R2GC_270_121,(1,0,1):C.R2GC_270_122,(0,0,0):C.R2GC_228_90,(0,0,1):C.R2GC_269_120})

V_198 = CTVertex(name = 'V_198',
                 type = 'R2',
                 particles = [ P.a, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_358_139,(0,1,0):C.R2GC_359_140})

V_199 = CTVertex(name = 'V_199',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.c, P.YS3u2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_586_181})

V_200 = CTVertex(name = 'V_200',
                 type = 'R2',
                 particles = [ P.Xm, P.c, P.YS3u2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_586_181})

V_201 = CTVertex(name = 'V_201',
                 type = 'R2',
                 particles = [ P.g, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_266_116,(0,1,0):C.R2GC_265_115})

V_202 = CTVertex(name = 'V_202',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.Xd, P.YS3u2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_586_181})

V_203 = CTVertex(name = 'V_203',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.Xm, P.YS3u2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_586_181})

V_204 = CTVertex(name = 'V_204',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_360_141})

V_205 = CTVertex(name = 'V_205',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_363_142})

V_206 = CTVertex(name = 'V_206',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3u2] ] ],
                 couplings = {(2,0,0):C.R2GC_270_121,(2,0,1):C.R2GC_270_122,(1,0,0):C.R2GC_270_121,(1,0,1):C.R2GC_270_122,(0,0,0):C.R2GC_228_90,(0,0,1):C.R2GC_269_120})

V_207 = CTVertex(name = 'V_207',
                 type = 'R2',
                 particles = [ P.a, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_358_139,(0,1,0):C.R2GC_359_140})

V_208 = CTVertex(name = 'V_208',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.t, P.YS3u3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_767_212})

V_209 = CTVertex(name = 'V_209',
                 type = 'R2',
                 particles = [ P.Xm, P.t, P.YS3u3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_767_212})

V_210 = CTVertex(name = 'V_210',
                 type = 'R2',
                 particles = [ P.g, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_266_116,(0,1,0):C.R2GC_265_115})

V_211 = CTVertex(name = 'V_211',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.Xd, P.YS3u3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_767_212})

V_212 = CTVertex(name = 'V_212',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.Xm, P.YS3u3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_767_212})

V_213 = CTVertex(name = 'V_213',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_360_141})

V_214 = CTVertex(name = 'V_214',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_363_142})

V_215 = CTVertex(name = 'V_215',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3u3] ] ],
                 couplings = {(2,0,0):C.R2GC_270_121,(2,0,1):C.R2GC_270_122,(1,0,0):C.R2GC_270_121,(1,0,1):C.R2GC_270_122,(0,0,0):C.R2GC_228_90,(0,0,1):C.R2GC_269_120})

V_216 = CTVertex(name = 'V_216',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_765_211})

V_217 = CTVertex(name = 'V_217',
                 type = 'R2',
                 particles = [ P.YF3Qd1__tilde__, P.YF3Qd1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_245_106})

V_218 = CTVertex(name = 'V_218',
                 type = 'R2',
                 particles = [ P.YF3Qd2__tilde__, P.YF3Qd2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_245_106})

V_219 = CTVertex(name = 'V_219',
                 type = 'R2',
                 particles = [ P.YF3Qd3__tilde__, P.YF3Qd3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_245_106})

V_220 = CTVertex(name = 'V_220',
                 type = 'R2',
                 particles = [ P.YF3Qu1__tilde__, P.YF3Qu1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_252_109})

V_221 = CTVertex(name = 'V_221',
                 type = 'R2',
                 particles = [ P.YF3Qu2__tilde__, P.YF3Qu2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_252_109})

V_222 = CTVertex(name = 'V_222',
                 type = 'R2',
                 particles = [ P.YF3Qu3__tilde__, P.YF3Qu3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_252_109})

V_223 = CTVertex(name = 'V_223',
                 type = 'R2',
                 particles = [ P.YF3d1__tilde__, P.YF3d1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_246_107})

V_224 = CTVertex(name = 'V_224',
                 type = 'R2',
                 particles = [ P.YF3d2__tilde__, P.YF3d2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_246_107})

V_225 = CTVertex(name = 'V_225',
                 type = 'R2',
                 particles = [ P.YF3d3__tilde__, P.YF3d3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_246_107})

V_226 = CTVertex(name = 'V_226',
                 type = 'R2',
                 particles = [ P.YF3u1__tilde__, P.YF3u1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_253_110})

V_227 = CTVertex(name = 'V_227',
                 type = 'R2',
                 particles = [ P.YF3u2__tilde__, P.YF3u2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_253_110})

V_228 = CTVertex(name = 'V_228',
                 type = 'R2',
                 particles = [ P.YF3u3__tilde__, P.YF3u3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_253_110})

V_229 = CTVertex(name = 'V_229',
                 type = 'R2',
                 particles = [ P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_272_124,(0,1,0):C.R2GC_273_125})

V_230 = CTVertex(name = 'V_230',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_274_126})

V_231 = CTVertex(name = 'V_231',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_275_127})

V_232 = CTVertex(name = 'V_232',
                 type = 'R2',
                 particles = [ P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_272_124,(0,1,0):C.R2GC_273_125})

V_233 = CTVertex(name = 'V_233',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_274_126})

V_234 = CTVertex(name = 'V_234',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_275_127})

V_235 = CTVertex(name = 'V_235',
                 type = 'R2',
                 particles = [ P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_272_124,(0,1,0):C.R2GC_273_125})

V_236 = CTVertex(name = 'V_236',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_274_126})

V_237 = CTVertex(name = 'V_237',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_275_127})

V_238 = CTVertex(name = 'V_238',
                 type = 'R2',
                 particles = [ P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_321_133,(0,1,0):C.R2GC_320_132})

V_239 = CTVertex(name = 'V_239',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_322_134})

V_240 = CTVertex(name = 'V_240',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_323_135})

V_241 = CTVertex(name = 'V_241',
                 type = 'R2',
                 particles = [ P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_321_133,(0,1,0):C.R2GC_320_132})

V_242 = CTVertex(name = 'V_242',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_322_134})

V_243 = CTVertex(name = 'V_243',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_323_135})

V_244 = CTVertex(name = 'V_244',
                 type = 'R2',
                 particles = [ P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_321_133,(0,1,0):C.R2GC_320_132})

V_245 = CTVertex(name = 'V_245',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_322_134})

V_246 = CTVertex(name = 'V_246',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_323_135})

V_247 = CTVertex(name = 'V_247',
                 type = 'R2',
                 particles = [ P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_369_145,(0,1,0):C.R2GC_368_144})

V_248 = CTVertex(name = 'V_248',
                 type = 'R2',
                 particles = [ P.W__plus__, P.Z, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_652_199})

V_249 = CTVertex(name = 'V_249',
                 type = 'R2',
                 particles = [ P.W__minus__, P.Z, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_652_199})

V_250 = CTVertex(name = 'V_250',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_370_146})

V_251 = CTVertex(name = 'V_251',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_371_147})

V_252 = CTVertex(name = 'V_252',
                 type = 'R2',
                 particles = [ P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_369_145,(0,1,0):C.R2GC_368_144})

V_253 = CTVertex(name = 'V_253',
                 type = 'R2',
                 particles = [ P.W__plus__, P.Z, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_652_199})

V_254 = CTVertex(name = 'V_254',
                 type = 'R2',
                 particles = [ P.W__minus__, P.Z, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_652_199})

V_255 = CTVertex(name = 'V_255',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_370_146})

V_256 = CTVertex(name = 'V_256',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_371_147})

V_257 = CTVertex(name = 'V_257',
                 type = 'R2',
                 particles = [ P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_369_145,(0,1,0):C.R2GC_368_144})

V_258 = CTVertex(name = 'V_258',
                 type = 'R2',
                 particles = [ P.W__plus__, P.Z, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_652_199})

V_259 = CTVertex(name = 'V_259',
                 type = 'R2',
                 particles = [ P.W__minus__, P.Z, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_652_199})

V_260 = CTVertex(name = 'V_260',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_370_146})

V_261 = CTVertex(name = 'V_261',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_371_147})

V_262 = CTVertex(name = 'V_262',
                 type = 'R2',
                 particles = [ P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_417_153,(0,1,0):C.R2GC_416_152})

V_263 = CTVertex(name = 'V_263',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_418_154})

V_264 = CTVertex(name = 'V_264',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_419_155})

V_265 = CTVertex(name = 'V_265',
                 type = 'R2',
                 particles = [ P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_417_153,(0,1,0):C.R2GC_416_152})

V_266 = CTVertex(name = 'V_266',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_418_154})

V_267 = CTVertex(name = 'V_267',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_419_155})

V_268 = CTVertex(name = 'V_268',
                 type = 'R2',
                 particles = [ P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_417_153,(0,1,0):C.R2GC_416_152})

V_269 = CTVertex(name = 'V_269',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_418_154})

V_270 = CTVertex(name = 'V_270',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_419_155})

V_271 = CTVertex(name = 'V_271',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_276_128})

V_272 = CTVertex(name = 'V_272',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_276_128})

V_273 = CTVertex(name = 'V_273',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_276_128})

V_274 = CTVertex(name = 'V_274',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_324_136})

V_275 = CTVertex(name = 'V_275',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_324_136})

V_276 = CTVertex(name = 'V_276',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_324_136})

V_277 = CTVertex(name = 'V_277',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_372_148})

V_278 = CTVertex(name = 'V_278',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_372_148})

V_279 = CTVertex(name = 'V_279',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_372_148})

V_280 = CTVertex(name = 'V_280',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_420_156})

V_281 = CTVertex(name = 'V_281',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_420_156})

V_282 = CTVertex(name = 'V_282',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_420_156})

V_283 = CTVertex(name = 'V_283',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.YF3Qu1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_596_191})

V_284 = CTVertex(name = 'V_284',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.YF3Qd1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_596_191})

V_285 = CTVertex(name = 'V_285',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.YF3Qu2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_588_183})

V_286 = CTVertex(name = 'V_286',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.YF3Qd2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_588_183})

V_287 = CTVertex(name = 'V_287',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.YF3Qu3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_583_178})

V_288 = CTVertex(name = 'V_288',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.YF3Qd3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_583_178})

V_289 = CTVertex(name = 'V_289',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.YF3Qu1, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_596_191})

V_290 = CTVertex(name = 'V_290',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.YF3Qd1, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_596_191})

V_291 = CTVertex(name = 'V_291',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.YF3Qu2, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_588_183})

V_292 = CTVertex(name = 'V_292',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.YF3Qd2, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_588_183})

V_293 = CTVertex(name = 'V_293',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.YF3Qu3, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_583_178})

V_294 = CTVertex(name = 'V_294',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.YF3Qd3, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_583_178})

V_295 = CTVertex(name = 'V_295',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_250_108})

V_296 = CTVertex(name = 'V_296',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_250_108})

V_297 = CTVertex(name = 'V_297',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_250_108})

V_298 = CTVertex(name = 'V_298',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_243_104})

V_299 = CTVertex(name = 'V_299',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_243_104})

V_300 = CTVertex(name = 'V_300',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_243_104})

V_301 = CTVertex(name = 'V_301',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_244_105})

V_302 = CTVertex(name = 'V_302',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_244_105})

V_303 = CTVertex(name = 'V_303',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_244_105})

V_304 = CTVertex(name = 'V_304',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_244_105})

V_305 = CTVertex(name = 'V_305',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_244_105})

V_306 = CTVertex(name = 'V_306',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_244_105})

V_307 = CTVertex(name = 'V_307',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_587_182})

V_308 = CTVertex(name = 'V_308',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_587_182})

V_309 = CTVertex(name = 'V_309',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_587_182})

V_310 = CTVertex(name = 'V_310',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_587_182})

V_311 = CTVertex(name = 'V_311',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_587_182})

V_312 = CTVertex(name = 'V_312',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_587_182})

V_313 = CTVertex(name = 'V_313',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_252_109,(0,1,0):C.R2GC_253_110})

V_314 = CTVertex(name = 'V_314',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_252_109,(0,1,0):C.R2GC_253_110})

V_315 = CTVertex(name = 'V_315',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_252_109,(0,1,0):C.R2GC_253_110})

V_316 = CTVertex(name = 'V_316',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_245_106,(0,1,0):C.R2GC_246_107})

V_317 = CTVertex(name = 'V_317',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_245_106,(0,1,0):C.R2GC_246_107})

V_318 = CTVertex(name = 'V_318',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_245_106,(0,1,0):C.R2GC_246_107})

V_319 = CTVertex(name = 'V_319',
                 type = 'R2',
                 particles = [ P.YF3Qu1__tilde__, P.u, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_596_191})

V_320 = CTVertex(name = 'V_320',
                 type = 'R2',
                 particles = [ P.YF3Qd1__tilde__, P.d, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_596_191})

V_321 = CTVertex(name = 'V_321',
                 type = 'R2',
                 particles = [ P.YF3Qu2__tilde__, P.c, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_588_183})

V_322 = CTVertex(name = 'V_322',
                 type = 'R2',
                 particles = [ P.YF3Qd2__tilde__, P.s, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_588_183})

V_323 = CTVertex(name = 'V_323',
                 type = 'R2',
                 particles = [ P.YF3Qu3__tilde__, P.t, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_583_178})

V_324 = CTVertex(name = 'V_324',
                 type = 'R2',
                 particles = [ P.YF3Qd3__tilde__, P.b, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_583_178})

V_325 = CTVertex(name = 'V_325',
                 type = 'R2',
                 particles = [ P.YF3Qu1__tilde__, P.u, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_596_191})

V_326 = CTVertex(name = 'V_326',
                 type = 'R2',
                 particles = [ P.YF3Qd1__tilde__, P.d, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_596_191})

V_327 = CTVertex(name = 'V_327',
                 type = 'R2',
                 particles = [ P.YF3Qu2__tilde__, P.c, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_588_183})

V_328 = CTVertex(name = 'V_328',
                 type = 'R2',
                 particles = [ P.YF3Qd2__tilde__, P.s, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_588_183})

V_329 = CTVertex(name = 'V_329',
                 type = 'R2',
                 particles = [ P.YF3Qu3__tilde__, P.t, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_583_178})

V_330 = CTVertex(name = 'V_330',
                 type = 'R2',
                 particles = [ P.YF3Qd3__tilde__, P.b, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_583_178})

V_331 = CTVertex(name = 'V_331',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.YF3d1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_594_189})

V_332 = CTVertex(name = 'V_332',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.YF3d2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_759_208})

V_333 = CTVertex(name = 'V_333',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.YF3d3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_581_176})

V_334 = CTVertex(name = 'V_334',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.YF3u1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_777_216})

V_335 = CTVertex(name = 'V_335',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.YF3u2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_590_185})

V_336 = CTVertex(name = 'V_336',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.YF3u3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_770_213})

V_337 = CTVertex(name = 'V_337',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.YF3d1, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_594_189})

V_338 = CTVertex(name = 'V_338',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.YF3d2, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_759_208})

V_339 = CTVertex(name = 'V_339',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.YF3d3, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_581_176})

V_340 = CTVertex(name = 'V_340',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.YF3u1, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_777_216})

V_341 = CTVertex(name = 'V_341',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.YF3u2, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_590_185})

V_342 = CTVertex(name = 'V_342',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.YF3u3, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_770_213})

V_343 = CTVertex(name = 'V_343',
                 type = 'R2',
                 particles = [ P.YF3d1__tilde__, P.d, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_594_189})

V_344 = CTVertex(name = 'V_344',
                 type = 'R2',
                 particles = [ P.YF3d2__tilde__, P.s, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_759_208})

V_345 = CTVertex(name = 'V_345',
                 type = 'R2',
                 particles = [ P.YF3d3__tilde__, P.b, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_581_176})

V_346 = CTVertex(name = 'V_346',
                 type = 'R2',
                 particles = [ P.YF3u1__tilde__, P.u, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_777_216})

V_347 = CTVertex(name = 'V_347',
                 type = 'R2',
                 particles = [ P.YF3u2__tilde__, P.c, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_590_185})

V_348 = CTVertex(name = 'V_348',
                 type = 'R2',
                 particles = [ P.YF3u3__tilde__, P.t, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_770_213})

V_349 = CTVertex(name = 'V_349',
                 type = 'R2',
                 particles = [ P.YF3d1__tilde__, P.d, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_594_189})

V_350 = CTVertex(name = 'V_350',
                 type = 'R2',
                 particles = [ P.YF3d2__tilde__, P.s, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_759_208})

V_351 = CTVertex(name = 'V_351',
                 type = 'R2',
                 particles = [ P.YF3d3__tilde__, P.b, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_581_176})

V_352 = CTVertex(name = 'V_352',
                 type = 'R2',
                 particles = [ P.YF3u1__tilde__, P.u, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_777_216})

V_353 = CTVertex(name = 'V_353',
                 type = 'R2',
                 particles = [ P.YF3u2__tilde__, P.c, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_590_185})

V_354 = CTVertex(name = 'V_354',
                 type = 'R2',
                 particles = [ P.YF3u3__tilde__, P.t, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_770_213})

V_355 = CTVertex(name = 'V_355',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_242_103})

V_356 = CTVertex(name = 'V_356',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_242_103})

V_357 = CTVertex(name = 'V_357',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_465_159,(0,1,0):C.R2GC_242_103})

V_358 = CTVertex(name = 'V_358',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_242_103})

V_359 = CTVertex(name = 'V_359',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_242_103})

V_360 = CTVertex(name = 'V_360',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_242_103})

V_361 = CTVertex(name = 'V_361',
                 type = 'R2',
                 particles = [ P.YF3Qu1__tilde__, P.YF3Qu1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_530_168,(0,1,0):C.R2GC_242_103})

V_362 = CTVertex(name = 'V_362',
                 type = 'R2',
                 particles = [ P.YF3Qu2__tilde__, P.YF3Qu2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_541_169,(0,1,0):C.R2GC_242_103})

V_363 = CTVertex(name = 'V_363',
                 type = 'R2',
                 particles = [ P.YF3Qu3__tilde__, P.YF3Qu3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_552_170,(0,1,0):C.R2GC_242_103})

V_364 = CTVertex(name = 'V_364',
                 type = 'R2',
                 particles = [ P.YF3Qd1__tilde__, P.YF3Qd1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_503_165,(0,1,0):C.R2GC_242_103})

V_365 = CTVertex(name = 'V_365',
                 type = 'R2',
                 particles = [ P.YF3Qd2__tilde__, P.YF3Qd2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_512_166,(0,1,0):C.R2GC_242_103})

V_366 = CTVertex(name = 'V_366',
                 type = 'R2',
                 particles = [ P.YF3Qd3__tilde__, P.YF3Qd3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_521_167,(0,1,0):C.R2GC_242_103})

V_367 = CTVertex(name = 'V_367',
                 type = 'R2',
                 particles = [ P.YF3u1__tilde__, P.YF3u1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_563_171,(0,1,0):C.R2GC_242_103})

V_368 = CTVertex(name = 'V_368',
                 type = 'R2',
                 particles = [ P.YF3u2__tilde__, P.YF3u2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_570_172,(0,1,0):C.R2GC_242_103})

V_369 = CTVertex(name = 'V_369',
                 type = 'R2',
                 particles = [ P.YF3u3__tilde__, P.YF3u3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_577_173,(0,1,0):C.R2GC_242_103})

V_370 = CTVertex(name = 'V_370',
                 type = 'R2',
                 particles = [ P.YF3d1__tilde__, P.YF3d1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_482_162,(0,1,0):C.R2GC_242_103})

V_371 = CTVertex(name = 'V_371',
                 type = 'R2',
                 particles = [ P.YF3d2__tilde__, P.YF3d2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_489_163,(0,1,0):C.R2GC_242_103})

V_372 = CTVertex(name = 'V_372',
                 type = 'R2',
                 particles = [ P.YF3d3__tilde__, P.YF3d3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_496_164,(0,1,0):C.R2GC_242_103})

V_373 = CTVertex(name = 'V_373',
                 type = 'R2',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV2, L.VV3 ],
                 loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u], [P.YF3d1], [P.YF3d2], [P.YF3d3], [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3], [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3], [P.YF3u1], [P.YF3u2], [P.YF3u3] ], [ [P.g] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ] ],
                 couplings = {(0,2,1):C.R2GC_120_1,(0,0,2):C.R2GC_129_13,(0,0,3):C.R2GC_129_14,(0,0,4):C.R2GC_129_15,(0,0,5):C.R2GC_129_16,(0,0,6):C.R2GC_129_17,(0,0,7):C.R2GC_129_18,(0,0,8):C.R2GC_129_19,(0,0,9):C.R2GC_129_20,(0,0,10):C.R2GC_129_21,(0,0,11):C.R2GC_129_22,(0,0,12):C.R2GC_129_23,(0,0,13):C.R2GC_129_24,(0,0,14):C.R2GC_129_25,(0,1,0):C.R2GC_126_8})

V_374 = CTVertex(name = 'V_374',
                 type = 'R2',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_367_143,(0,1,0):C.R2GC_261_111})

V_375 = CTVertex(name = 'V_375',
                 type = 'R2',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_383_149,(0,1,0):C.R2GC_261_111})

V_376 = CTVertex(name = 'V_376',
                 type = 'R2',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_399_150,(0,1,0):C.R2GC_261_111})

V_377 = CTVertex(name = 'V_377',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_319_131,(0,1,0):C.R2GC_261_111})

V_378 = CTVertex(name = 'V_378',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_335_137,(0,1,0):C.R2GC_261_111})

V_379 = CTVertex(name = 'V_379',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_351_138,(0,1,0):C.R2GC_261_111})

V_380 = CTVertex(name = 'V_380',
                 type = 'R2',
                 particles = [ P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_415_151,(0,1,0):C.R2GC_261_111})

V_381 = CTVertex(name = 'V_381',
                 type = 'R2',
                 particles = [ P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_431_157,(0,1,0):C.R2GC_261_111})

V_382 = CTVertex(name = 'V_382',
                 type = 'R2',
                 particles = [ P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_447_158,(0,1,0):C.R2GC_261_111})

V_383 = CTVertex(name = 'V_383',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_271_123,(0,1,0):C.R2GC_261_111})

V_384 = CTVertex(name = 'V_384',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_287_129,(0,1,0):C.R2GC_261_111})

V_385 = CTVertex(name = 'V_385',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_303_130,(0,1,0):C.R2GC_261_111})

V_386 = CTVertex(name = 'V_386',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVV1 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_124_4,(0,0,1):C.R2GC_124_5})

V_387 = CTVertex(name = 'V_387',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVS1 ],
                 loop_particles = [ [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_121_2})

V_388 = CTVertex(name = 'V_388',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Xv, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV5 ],
                 loop_particles = [ [ [P.b, P.YF3d3] ], [ [P.b, P.YF3Qd3], [P.t, P.YF3Qu3] ], [ [P.c, P.YF3Qu2], [P.s, P.YF3Qd2] ], [ [P.c, P.YF3u2] ], [ [P.d, P.YF3d1] ], [ [P.d, P.YF3Qd1], [P.u, P.YF3Qu1] ], [ [P.s, P.YF3d2] ], [ [P.t, P.YF3u3] ], [ [P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_134_53,(0,0,1):C.R2GC_134_54,(0,0,2):C.R2GC_134_55,(0,0,3):C.R2GC_134_56,(0,0,4):C.R2GC_134_57,(0,0,5):C.R2GC_134_58,(0,0,6):C.R2GC_134_59,(0,0,7):C.R2GC_134_60,(0,0,8):C.R2GC_134_61})

V_389 = CTVertex(name = 'V_389',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Xv, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV5 ],
                 loop_particles = [ [ [P.b, P.YF3d3] ], [ [P.b, P.YF3Qd3], [P.t, P.YF3Qu3] ], [ [P.c, P.YF3Qu2], [P.s, P.YF3Qd2] ], [ [P.c, P.YF3u2] ], [ [P.d, P.YF3d1] ], [ [P.d, P.YF3Qd1], [P.u, P.YF3Qu1] ], [ [P.s, P.YF3d2] ], [ [P.t, P.YF3u3] ], [ [P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_133_44,(0,0,1):C.R2GC_133_45,(0,0,2):C.R2GC_133_46,(0,0,3):C.R2GC_133_47,(0,0,4):C.R2GC_133_48,(0,0,5):C.R2GC_133_49,(0,0,6):C.R2GC_133_50,(0,0,7):C.R2GC_133_51,(0,0,8):C.R2GC_133_52})

V_390 = CTVertex(name = 'V_390',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Xv, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV5 ],
                 loop_particles = [ [ [P.b, P.YF3d3] ], [ [P.b, P.YF3Qd3], [P.t, P.YF3Qu3] ], [ [P.c, P.YF3Qu2], [P.s, P.YF3Qd2] ], [ [P.c, P.YF3u2] ], [ [P.d, P.YF3d1] ], [ [P.d, P.YF3Qd1], [P.u, P.YF3Qu1] ], [ [P.s, P.YF3d2] ], [ [P.t, P.YF3u3] ], [ [P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_133_44,(0,0,1):C.R2GC_133_45,(0,0,2):C.R2GC_133_46,(0,0,3):C.R2GC_133_47,(0,0,4):C.R2GC_133_48,(0,0,5):C.R2GC_133_49,(0,0,6):C.R2GC_133_50,(0,0,7):C.R2GC_133_51,(0,0,8):C.R2GC_133_52})

V_391 = CTVertex(name = 'V_391',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Xw__tilde__, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV5 ],
                 loop_particles = [ [ [P.b, P.YF3d3] ], [ [P.b, P.YF3Qd3], [P.t, P.YF3Qu3] ], [ [P.c, P.YF3Qu2], [P.s, P.YF3Qd2] ], [ [P.c, P.YF3u2] ], [ [P.d, P.YF3d1] ], [ [P.d, P.YF3Qd1], [P.u, P.YF3Qu1] ], [ [P.s, P.YF3d2] ], [ [P.t, P.YF3u3] ], [ [P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_133_44,(0,0,1):C.R2GC_133_45,(0,0,2):C.R2GC_133_46,(0,0,3):C.R2GC_133_47,(0,0,4):C.R2GC_133_48,(0,0,5):C.R2GC_133_49,(0,0,6):C.R2GC_133_50,(0,0,7):C.R2GC_133_51,(0,0,8):C.R2GC_133_52})

V_392 = CTVertex(name = 'V_392',
                 type = 'R2',
                 particles = [ P.a, P.a, P.g, P.g ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVVV5 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s], [P.YF3d1], [P.YF3d2], [P.YF3d3], [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3] ], [ [P.c], [P.t], [P.u], [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3], [P.YF3u1], [P.YF3u2], [P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_127_9,(0,0,1):C.R2GC_127_10})

V_393 = CTVertex(name = 'V_393',
                 type = 'R2',
                 particles = [ P.a, P.g, P.g, P.Z ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VVVV5 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.YF3d1], [P.YF3d2], [P.YF3d3] ], [ [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3] ], [ [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3] ], [ [P.YF3u1], [P.YF3u2], [P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_130_26,(0,0,1):C.R2GC_130_27,(0,0,2):C.R2GC_130_28,(0,0,3):C.R2GC_130_29,(0,0,4):C.R2GC_130_30,(0,0,5):C.R2GC_130_31})

V_394 = CTVertex(name = 'V_394',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Z, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV5 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.YF3d1], [P.YF3d2], [P.YF3d3] ], [ [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3] ], [ [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3] ], [ [P.YF3u1], [P.YF3u2], [P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_132_38,(0,0,1):C.R2GC_132_39,(0,0,2):C.R2GC_132_40,(0,0,3):C.R2GC_132_41,(0,0,4):C.R2GC_132_42,(0,0,5):C.R2GC_132_43})

V_395 = CTVertex(name = 'V_395',
                 type = 'R2',
                 particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV5 ],
                 loop_particles = [ [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ], [ [P.YF3Qd1, P.YF3Qu1], [P.YF3Qd2, P.YF3Qu2], [P.YF3Qd3, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_137_80,(0,0,1):C.R2GC_137_81})

V_396 = CTVertex(name = 'V_396',
                 type = 'R2',
                 particles = [ P.a, P.g, P.g, P.g ],
                 color = [ 'd(2,3,4)' ],
                 lorentz = [ L.VVVV5 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s], [P.YF3d1], [P.YF3d2], [P.YF3d3], [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3] ], [ [P.c], [P.t], [P.u], [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3], [P.YF3u1], [P.YF3u2], [P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_128_11,(0,0,1):C.R2GC_128_12})

V_397 = CTVertex(name = 'V_397',
                 type = 'R2',
                 particles = [ P.g, P.g, P.g, P.Z ],
                 color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                 lorentz = [ L.VVVV1, L.VVVV5 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.YF3d1], [P.YF3d2], [P.YF3d3] ], [ [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3] ], [ [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3] ], [ [P.YF3u1], [P.YF3u2], [P.YF3u3] ] ],
                 couplings = {(1,0,0):C.R2GC_125_6,(1,0,1):C.R2GC_125_7,(0,1,0):C.R2GC_131_32,(0,1,1):C.R2GC_131_33,(0,1,2):C.R2GC_131_34,(0,1,3):C.R2GC_131_35,(0,1,4):C.R2GC_131_36,(0,1,5):C.R2GC_131_37})

V_398 = CTVertex(name = 'V_398',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_122_3})

V_399 = CTVertex(name = 'V_399',
                 type = 'R2',
                 particles = [ P.g, P.g, P.G0, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_122_3})

V_400 = CTVertex(name = 'V_400',
                 type = 'R2',
                 particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_122_3})

V_401 = CTVertex(name = 'V_401',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Xs, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.YF3d3] ], [ [P.b, P.YF3Qd3], [P.t, P.YF3Qu3] ], [ [P.c, P.YF3Qu2], [P.s, P.YF3Qd2] ], [ [P.c, P.YF3u2] ], [ [P.d, P.YF3d1] ], [ [P.d, P.YF3Qd1], [P.u, P.YF3Qu1] ], [ [P.s, P.YF3d2] ], [ [P.t, P.YF3u3] ], [ [P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_136_71,(0,0,1):C.R2GC_136_72,(0,0,2):C.R2GC_136_73,(0,0,3):C.R2GC_136_74,(0,0,4):C.R2GC_136_75,(0,0,5):C.R2GC_136_76,(0,0,6):C.R2GC_136_77,(0,0,7):C.R2GC_136_78,(0,0,8):C.R2GC_136_79})

V_402 = CTVertex(name = 'V_402',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Xc, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.YF3d3] ], [ [P.b, P.YF3Qd3], [P.t, P.YF3Qu3] ], [ [P.c, P.YF3Qu2], [P.s, P.YF3Qd2] ], [ [P.c, P.YF3u2] ], [ [P.d, P.YF3d1] ], [ [P.d, P.YF3Qd1], [P.u, P.YF3Qu1] ], [ [P.s, P.YF3d2] ], [ [P.t, P.YF3u3] ], [ [P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_135_62,(0,0,1):C.R2GC_135_63,(0,0,2):C.R2GC_135_64,(0,0,3):C.R2GC_135_65,(0,0,4):C.R2GC_135_66,(0,0,5):C.R2GC_135_67,(0,0,6):C.R2GC_135_68,(0,0,7):C.R2GC_135_69,(0,0,8):C.R2GC_135_70})

V_403 = CTVertex(name = 'V_403',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Xc__tilde__, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.YF3d3] ], [ [P.b, P.YF3Qd3], [P.t, P.YF3Qu3] ], [ [P.c, P.YF3Qu2], [P.s, P.YF3Qd2] ], [ [P.c, P.YF3u2] ], [ [P.d, P.YF3d1] ], [ [P.d, P.YF3Qd1], [P.u, P.YF3Qu1] ], [ [P.s, P.YF3d2] ], [ [P.t, P.YF3u3] ], [ [P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_135_62,(0,0,1):C.R2GC_135_63,(0,0,2):C.R2GC_135_64,(0,0,3):C.R2GC_135_65,(0,0,4):C.R2GC_135_66,(0,0,5):C.R2GC_135_67,(0,0,6):C.R2GC_135_68,(0,0,7):C.R2GC_135_69,(0,0,8):C.R2GC_135_70})

V_404 = CTVertex(name = 'V_404',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Xc__tilde__, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.YF3d3] ], [ [P.b, P.YF3Qd3], [P.t, P.YF3Qu3] ], [ [P.c, P.YF3Qu2], [P.s, P.YF3Qd2] ], [ [P.c, P.YF3u2] ], [ [P.d, P.YF3d1] ], [ [P.d, P.YF3Qd1], [P.u, P.YF3Qu1] ], [ [P.s, P.YF3d2] ], [ [P.t, P.YF3u3] ], [ [P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_135_62,(0,0,1):C.R2GC_135_63,(0,0,2):C.R2GC_135_64,(0,0,3):C.R2GC_135_65,(0,0,4):C.R2GC_135_66,(0,0,5):C.R2GC_135_67,(0,0,6):C.R2GC_135_68,(0,0,7):C.R2GC_135_69,(0,0,8):C.R2GC_135_70})

V_405 = CTVertex(name = 'V_405',
                 type = 'R2',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3Qu1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_268_118,(1,0,3):C.R2GC_268_119,(1,0,0):C.R2GC_788_224,(1,0,5):C.R2GC_788_225,(1,0,1):C.R2GC_788_226,(1,0,4):C.R2GC_788_227,(0,0,2):C.R2GC_268_118,(0,0,3):C.R2GC_268_119,(0,0,0):C.R2GC_788_224,(0,0,5):C.R2GC_788_225,(0,0,1):C.R2GC_788_226,(0,0,4):C.R2GC_788_227})

V_406 = CTVertex(name = 'V_406',
                 type = 'R2',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qu1, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu1, P.YS3Qu2] ], [ [P.g, P.YS3Qu1, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_861_292,(1,0,8):C.R2GC_861_293,(1,0,1):C.R2GC_861_294,(1,0,7):C.R2GC_861_295,(1,0,2):C.R2GC_861_296,(1,0,6):C.R2GC_861_297,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_860_286,(0,0,8):C.R2GC_860_287,(0,0,1):C.R2GC_860_288,(0,0,7):C.R2GC_860_289,(0,0,2):C.R2GC_860_290,(0,0,6):C.R2GC_860_291})

V_407 = CTVertex(name = 'V_407',
                 type = 'R2',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3Qu2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_268_118,(1,0,3):C.R2GC_268_119,(1,0,0):C.R2GC_788_224,(1,0,5):C.R2GC_788_225,(1,0,1):C.R2GC_788_226,(1,0,4):C.R2GC_788_227,(0,0,2):C.R2GC_268_118,(0,0,3):C.R2GC_268_119,(0,0,0):C.R2GC_788_224,(0,0,5):C.R2GC_788_225,(0,0,1):C.R2GC_788_226,(0,0,4):C.R2GC_788_227})

V_408 = CTVertex(name = 'V_408',
                 type = 'R2',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qu1, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qu1, P.YS3Qu3] ], [ [P.g, P.YS3Qu1, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_861_292,(1,0,8):C.R2GC_861_293,(1,0,1):C.R2GC_861_294,(1,0,7):C.R2GC_861_295,(1,0,2):C.R2GC_861_296,(1,0,6):C.R2GC_861_297,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_860_286,(0,0,8):C.R2GC_860_287,(0,0,1):C.R2GC_860_288,(0,0,7):C.R2GC_860_289,(0,0,2):C.R2GC_860_290,(0,0,6):C.R2GC_860_291})

V_409 = CTVertex(name = 'V_409',
                 type = 'R2',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qu2, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qu2, P.YS3Qu3] ], [ [P.g, P.YS3Qu2, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_861_292,(1,0,8):C.R2GC_861_293,(1,0,1):C.R2GC_861_294,(1,0,7):C.R2GC_861_295,(1,0,2):C.R2GC_861_296,(1,0,6):C.R2GC_861_297,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_860_286,(0,0,8):C.R2GC_860_287,(0,0,1):C.R2GC_860_288,(0,0,7):C.R2GC_860_289,(0,0,2):C.R2GC_860_290,(0,0,6):C.R2GC_860_291})

V_410 = CTVertex(name = 'V_410',
                 type = 'R2',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3Qu3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_268_118,(1,0,3):C.R2GC_268_119,(1,0,0):C.R2GC_788_224,(1,0,5):C.R2GC_788_225,(1,0,1):C.R2GC_788_226,(1,0,4):C.R2GC_788_227,(0,0,2):C.R2GC_268_118,(0,0,3):C.R2GC_268_119,(0,0,0):C.R2GC_788_224,(0,0,5):C.R2GC_788_225,(0,0,1):C.R2GC_788_226,(0,0,4):C.R2GC_788_227})

V_411 = CTVertex(name = 'V_411',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qu1] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,7):C.R2GC_599_197,(1,0,8):C.R2GC_599_198,(1,0,0):C.R2GC_817_264,(1,0,4):C.R2GC_794_230,(1,0,11):C.R2GC_855_281,(1,0,1):C.R2GC_817_266,(1,0,5):C.R2GC_855_282,(1,0,10):C.R2GC_855_283,(1,0,2):C.R2GC_817_268,(1,0,6):C.R2GC_855_284,(1,0,9):C.R2GC_855_285,(0,0,3):C.R2GC_598_193,(0,0,7):C.R2GC_598_194,(0,0,8):C.R2GC_598_195,(0,0,0):C.R2GC_782_218,(0,0,4):C.R2GC_795_233,(0,0,11):C.R2GC_854_276,(0,0,1):C.R2GC_127_9,(0,0,5):C.R2GC_854_277,(0,0,10):C.R2GC_854_278,(0,0,2):C.R2GC_816_262,(0,0,6):C.R2GC_854_279,(0,0,9):C.R2GC_854_280})

V_412 = CTVertex(name = 'V_412',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd1, P.YS3Qu2] ], [ [P.g, P.YS3Qd1, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_817_264,(1,0,8):C.R2GC_855_281,(1,0,1):C.R2GC_817_266,(1,0,7):C.R2GC_855_283,(1,0,2):C.R2GC_817_268,(1,0,6):C.R2GC_855_285,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_782_218,(0,0,8):C.R2GC_854_276,(0,0,1):C.R2GC_127_9,(0,0,7):C.R2GC_854_278,(0,0,2):C.R2GC_816_262,(0,0,6):C.R2GC_854_280})

V_413 = CTVertex(name = 'V_413',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd1, P.YS3Qu3] ], [ [P.g, P.YS3Qd1, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_817_264,(1,0,8):C.R2GC_855_281,(1,0,1):C.R2GC_817_266,(1,0,7):C.R2GC_855_283,(1,0,2):C.R2GC_817_268,(1,0,6):C.R2GC_855_285,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_782_218,(0,0,8):C.R2GC_854_276,(0,0,1):C.R2GC_127_9,(0,0,7):C.R2GC_854_278,(0,0,2):C.R2GC_816_262,(0,0,6):C.R2GC_854_280})

V_414 = CTVertex(name = 'V_414',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qd1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_268_118,(1,0,3):C.R2GC_268_119,(1,0,0):C.R2GC_782_218,(1,0,5):C.R2GC_785_222,(1,0,1):C.R2GC_782_220,(1,0,4):C.R2GC_785_223,(0,0,2):C.R2GC_268_118,(0,0,3):C.R2GC_268_119,(0,0,0):C.R2GC_782_218,(0,0,5):C.R2GC_785_222,(0,0,1):C.R2GC_782_220,(0,0,4):C.R2GC_785_223})

V_415 = CTVertex(name = 'V_415',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd2, P.YS3Qu1, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu2] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu2] ] ],
                 couplings = {(1,0,0):C.R2GC_794_230,(1,0,1):C.R2GC_794_231,(1,0,2):C.R2GC_794_232,(0,0,0):C.R2GC_795_233,(0,0,1):C.R2GC_795_234,(0,0,2):C.R2GC_795_235})

V_416 = CTVertex(name = 'V_416',
                 type = 'R2',
                 particles = [ P.YS3Qd1, P.YS3Qd2__tilde__, P.YS3Qu1__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu2] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu2] ] ],
                 couplings = {(1,0,0):C.R2GC_794_230,(1,0,1):C.R2GC_794_231,(1,0,2):C.R2GC_794_232,(0,0,0):C.R2GC_795_233,(0,0,1):C.R2GC_795_234,(0,0,2):C.R2GC_795_235})

V_417 = CTVertex(name = 'V_417',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd2, P.YS3Qu1] ], [ [P.g, P.YS3Qd2, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_817_264,(1,0,8):C.R2GC_855_281,(1,0,1):C.R2GC_817_266,(1,0,7):C.R2GC_855_283,(1,0,2):C.R2GC_817_268,(1,0,6):C.R2GC_855_285,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_782_218,(0,0,8):C.R2GC_854_276,(0,0,1):C.R2GC_127_9,(0,0,7):C.R2GC_854_278,(0,0,2):C.R2GC_816_262,(0,0,6):C.R2GC_854_280})

V_418 = CTVertex(name = 'V_418',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qu2] ], [ [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,7):C.R2GC_599_197,(1,0,8):C.R2GC_599_198,(1,0,0):C.R2GC_817_264,(1,0,4):C.R2GC_794_230,(1,0,11):C.R2GC_855_281,(1,0,1):C.R2GC_817_266,(1,0,5):C.R2GC_855_282,(1,0,10):C.R2GC_855_283,(1,0,2):C.R2GC_817_268,(1,0,6):C.R2GC_855_284,(1,0,9):C.R2GC_855_285,(0,0,3):C.R2GC_598_193,(0,0,7):C.R2GC_598_194,(0,0,8):C.R2GC_598_195,(0,0,0):C.R2GC_782_218,(0,0,4):C.R2GC_795_233,(0,0,11):C.R2GC_854_276,(0,0,1):C.R2GC_127_9,(0,0,5):C.R2GC_854_277,(0,0,10):C.R2GC_854_278,(0,0,2):C.R2GC_816_262,(0,0,6):C.R2GC_854_279,(0,0,9):C.R2GC_854_280})

V_419 = CTVertex(name = 'V_419',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd2, P.YS3Qu3] ], [ [P.g, P.YS3Qd2, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_817_264,(1,0,8):C.R2GC_855_281,(1,0,1):C.R2GC_817_266,(1,0,7):C.R2GC_855_283,(1,0,2):C.R2GC_817_268,(1,0,6):C.R2GC_855_285,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_782_218,(0,0,8):C.R2GC_854_276,(0,0,1):C.R2GC_127_9,(0,0,7):C.R2GC_854_278,(0,0,2):C.R2GC_816_262,(0,0,6):C.R2GC_854_280})

V_420 = CTVertex(name = 'V_420',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd1, P.YS3Qd2] ], [ [P.g, P.YS3Qd1, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_801_242,(1,0,8):C.R2GC_813_257,(1,0,1):C.R2GC_801_244,(1,0,7):C.R2GC_813_258,(1,0,2):C.R2GC_801_246,(1,0,6):C.R2GC_813_259,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_800_236,(0,0,8):C.R2GC_812_254,(0,0,1):C.R2GC_800_238,(0,0,7):C.R2GC_812_255,(0,0,2):C.R2GC_800_240,(0,0,6):C.R2GC_812_256})

V_421 = CTVertex(name = 'V_421',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qd2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_268_118,(1,0,3):C.R2GC_268_119,(1,0,0):C.R2GC_782_218,(1,0,5):C.R2GC_785_222,(1,0,1):C.R2GC_782_220,(1,0,4):C.R2GC_785_223,(0,0,2):C.R2GC_268_118,(0,0,3):C.R2GC_268_119,(0,0,0):C.R2GC_782_218,(0,0,5):C.R2GC_785_222,(0,0,1):C.R2GC_782_220,(0,0,4):C.R2GC_785_223})

V_422 = CTVertex(name = 'V_422',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd3, P.YS3Qu1, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.R2GC_794_230,(1,0,1):C.R2GC_794_231,(1,0,2):C.R2GC_794_232,(0,0,0):C.R2GC_795_233,(0,0,1):C.R2GC_795_234,(0,0,2):C.R2GC_795_235})

V_423 = CTVertex(name = 'V_423',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd3, P.YS3Qu2, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu2, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.R2GC_794_230,(1,0,1):C.R2GC_794_231,(1,0,2):C.R2GC_794_232,(0,0,0):C.R2GC_795_233,(0,0,1):C.R2GC_795_234,(0,0,2):C.R2GC_795_235})

V_424 = CTVertex(name = 'V_424',
                 type = 'R2',
                 particles = [ P.YS3Qd1, P.YS3Qd3__tilde__, P.YS3Qu1__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.R2GC_794_230,(1,0,1):C.R2GC_794_231,(1,0,2):C.R2GC_794_232,(0,0,0):C.R2GC_795_233,(0,0,1):C.R2GC_795_234,(0,0,2):C.R2GC_795_235})

V_425 = CTVertex(name = 'V_425',
                 type = 'R2',
                 particles = [ P.YS3Qd2, P.YS3Qd3__tilde__, P.YS3Qu2__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu2, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.R2GC_794_230,(1,0,1):C.R2GC_794_231,(1,0,2):C.R2GC_794_232,(0,0,0):C.R2GC_795_233,(0,0,1):C.R2GC_795_234,(0,0,2):C.R2GC_795_235})

V_426 = CTVertex(name = 'V_426',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3Qd3, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd3, P.YS3Qu1] ], [ [P.g, P.YS3Qd3, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_817_264,(1,0,8):C.R2GC_855_281,(1,0,1):C.R2GC_817_266,(1,0,7):C.R2GC_855_283,(1,0,2):C.R2GC_817_268,(1,0,6):C.R2GC_855_285,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_782_218,(0,0,8):C.R2GC_854_276,(0,0,1):C.R2GC_127_9,(0,0,7):C.R2GC_854_278,(0,0,2):C.R2GC_816_262,(0,0,6):C.R2GC_854_280})

V_427 = CTVertex(name = 'V_427',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qd3, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd3, P.YS3Qu2] ], [ [P.g, P.YS3Qd3, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_817_264,(1,0,8):C.R2GC_855_281,(1,0,1):C.R2GC_817_266,(1,0,7):C.R2GC_855_283,(1,0,2):C.R2GC_817_268,(1,0,6):C.R2GC_855_285,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_782_218,(0,0,8):C.R2GC_854_276,(0,0,1):C.R2GC_127_9,(0,0,7):C.R2GC_854_278,(0,0,2):C.R2GC_816_262,(0,0,6):C.R2GC_854_280})

V_428 = CTVertex(name = 'V_428',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,7):C.R2GC_599_197,(1,0,8):C.R2GC_599_198,(1,0,0):C.R2GC_817_264,(1,0,4):C.R2GC_794_230,(1,0,11):C.R2GC_855_281,(1,0,1):C.R2GC_817_266,(1,0,5):C.R2GC_855_282,(1,0,10):C.R2GC_855_283,(1,0,2):C.R2GC_817_268,(1,0,6):C.R2GC_855_284,(1,0,9):C.R2GC_855_285,(0,0,3):C.R2GC_598_193,(0,0,7):C.R2GC_598_194,(0,0,8):C.R2GC_598_195,(0,0,0):C.R2GC_782_218,(0,0,4):C.R2GC_795_233,(0,0,11):C.R2GC_854_276,(0,0,1):C.R2GC_127_9,(0,0,5):C.R2GC_854_277,(0,0,10):C.R2GC_854_278,(0,0,2):C.R2GC_816_262,(0,0,6):C.R2GC_854_279,(0,0,9):C.R2GC_854_280})

V_429 = CTVertex(name = 'V_429',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd1, P.YS3Qd3] ], [ [P.g, P.YS3Qd1, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_801_242,(1,0,8):C.R2GC_813_257,(1,0,1):C.R2GC_801_244,(1,0,7):C.R2GC_813_258,(1,0,2):C.R2GC_801_246,(1,0,6):C.R2GC_813_259,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_800_236,(0,0,8):C.R2GC_812_254,(0,0,1):C.R2GC_800_238,(0,0,7):C.R2GC_812_255,(0,0,2):C.R2GC_800_240,(0,0,6):C.R2GC_812_256})

V_430 = CTVertex(name = 'V_430',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd2, P.YS3Qd3] ], [ [P.g, P.YS3Qd2, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_801_242,(1,0,8):C.R2GC_813_257,(1,0,1):C.R2GC_801_244,(1,0,7):C.R2GC_813_258,(1,0,2):C.R2GC_801_246,(1,0,6):C.R2GC_813_259,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_800_236,(0,0,8):C.R2GC_812_254,(0,0,1):C.R2GC_800_238,(0,0,7):C.R2GC_812_255,(0,0,2):C.R2GC_800_240,(0,0,6):C.R2GC_812_256})

V_431 = CTVertex(name = 'V_431',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qd3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_268_118,(1,0,3):C.R2GC_268_119,(1,0,0):C.R2GC_782_218,(1,0,5):C.R2GC_785_222,(1,0,1):C.R2GC_782_220,(1,0,4):C.R2GC_785_223,(0,0,2):C.R2GC_268_118,(0,0,3):C.R2GC_268_119,(0,0,0):C.R2GC_782_218,(0,0,5):C.R2GC_785_222,(0,0,1):C.R2GC_782_220,(0,0,4):C.R2GC_785_223})

V_432 = CTVertex(name = 'V_432',
                 type = 'R2',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qu1, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qu1, P.YS3u1] ], [ [P.g, P.YS3Qu1, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_861_292,(1,0,8):C.R2GC_865_301,(1,0,1):C.R2GC_861_294,(1,0,7):C.R2GC_865_302,(1,0,2):C.R2GC_861_296,(1,0,6):C.R2GC_865_303,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_860_286,(0,0,8):C.R2GC_864_298,(0,0,1):C.R2GC_860_288,(0,0,7):C.R2GC_864_299,(0,0,2):C.R2GC_860_290,(0,0,6):C.R2GC_864_300})

V_433 = CTVertex(name = 'V_433',
                 type = 'R2',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qu2, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qu2, P.YS3u1] ], [ [P.g, P.YS3Qu2, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_861_292,(1,0,8):C.R2GC_865_301,(1,0,1):C.R2GC_861_294,(1,0,7):C.R2GC_865_302,(1,0,2):C.R2GC_861_296,(1,0,6):C.R2GC_865_303,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_860_286,(0,0,8):C.R2GC_864_298,(0,0,1):C.R2GC_860_288,(0,0,7):C.R2GC_864_299,(0,0,2):C.R2GC_860_290,(0,0,6):C.R2GC_864_300})

V_434 = CTVertex(name = 'V_434',
                 type = 'R2',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qu3, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qu3], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qu3, P.YS3u1] ], [ [P.g, P.YS3Qu3, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qu3, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_861_292,(1,0,8):C.R2GC_865_301,(1,0,1):C.R2GC_861_294,(1,0,7):C.R2GC_865_302,(1,0,2):C.R2GC_861_296,(1,0,6):C.R2GC_865_303,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_860_286,(0,0,8):C.R2GC_864_298,(0,0,1):C.R2GC_860_288,(0,0,7):C.R2GC_864_299,(0,0,2):C.R2GC_860_290,(0,0,6):C.R2GC_864_300})

V_435 = CTVertex(name = 'V_435',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qd1, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qd1, P.YS3u1] ], [ [P.g, P.YS3Qd1, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_817_264,(1,0,8):C.R2GC_817_265,(1,0,1):C.R2GC_817_266,(1,0,7):C.R2GC_817_267,(1,0,2):C.R2GC_817_268,(1,0,6):C.R2GC_817_269,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_782_218,(0,0,8):C.R2GC_816_260,(0,0,1):C.R2GC_127_9,(0,0,7):C.R2GC_816_261,(0,0,2):C.R2GC_816_262,(0,0,6):C.R2GC_816_263})

V_436 = CTVertex(name = 'V_436',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qd2, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qd2, P.YS3u1] ], [ [P.g, P.YS3Qd2, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_817_264,(1,0,8):C.R2GC_817_265,(1,0,1):C.R2GC_817_266,(1,0,7):C.R2GC_817_267,(1,0,2):C.R2GC_817_268,(1,0,6):C.R2GC_817_269,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_782_218,(0,0,8):C.R2GC_816_260,(0,0,1):C.R2GC_127_9,(0,0,7):C.R2GC_816_261,(0,0,2):C.R2GC_816_262,(0,0,6):C.R2GC_816_263})

V_437 = CTVertex(name = 'V_437',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qd3, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qd3, P.YS3u1] ], [ [P.g, P.YS3Qd3, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_817_264,(1,0,8):C.R2GC_817_265,(1,0,1):C.R2GC_817_266,(1,0,7):C.R2GC_817_267,(1,0,2):C.R2GC_817_268,(1,0,6):C.R2GC_817_269,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_782_218,(0,0,8):C.R2GC_816_260,(0,0,1):C.R2GC_127_9,(0,0,7):C.R2GC_816_261,(0,0,2):C.R2GC_816_262,(0,0,6):C.R2GC_816_263})

V_438 = CTVertex(name = 'V_438',
                 type = 'R2',
                 particles = [ P.YS3u1__tilde__, P.YS3u1__tilde__, P.YS3u1, P.YS3u1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3u1] ], [ [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_268_118,(1,0,3):C.R2GC_268_119,(1,0,0):C.R2GC_788_224,(1,0,5):C.R2GC_791_228,(1,0,1):C.R2GC_788_226,(1,0,4):C.R2GC_791_229,(0,0,2):C.R2GC_268_118,(0,0,3):C.R2GC_268_119,(0,0,0):C.R2GC_788_224,(0,0,5):C.R2GC_791_228,(0,0,1):C.R2GC_788_226,(0,0,4):C.R2GC_791_229})

V_439 = CTVertex(name = 'V_439',
                 type = 'R2',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qu1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qu1, P.YS3u2] ], [ [P.g, P.YS3Qu1, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_861_292,(1,0,8):C.R2GC_865_301,(1,0,1):C.R2GC_861_294,(1,0,7):C.R2GC_865_302,(1,0,2):C.R2GC_861_296,(1,0,6):C.R2GC_865_303,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_860_286,(0,0,8):C.R2GC_864_298,(0,0,1):C.R2GC_860_288,(0,0,7):C.R2GC_864_299,(0,0,2):C.R2GC_860_290,(0,0,6):C.R2GC_864_300})

V_440 = CTVertex(name = 'V_440',
                 type = 'R2',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qu2, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qu2, P.YS3u2] ], [ [P.g, P.YS3Qu2, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_861_292,(1,0,8):C.R2GC_865_301,(1,0,1):C.R2GC_861_294,(1,0,7):C.R2GC_865_302,(1,0,2):C.R2GC_861_296,(1,0,6):C.R2GC_865_303,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_860_286,(0,0,8):C.R2GC_864_298,(0,0,1):C.R2GC_860_288,(0,0,7):C.R2GC_864_299,(0,0,2):C.R2GC_860_290,(0,0,6):C.R2GC_864_300})

V_441 = CTVertex(name = 'V_441',
                 type = 'R2',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qu3, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qu3], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qu3, P.YS3u2] ], [ [P.g, P.YS3Qu3, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qu3, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_861_292,(1,0,8):C.R2GC_865_301,(1,0,1):C.R2GC_861_294,(1,0,7):C.R2GC_865_302,(1,0,2):C.R2GC_861_296,(1,0,6):C.R2GC_865_303,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_860_286,(0,0,8):C.R2GC_864_298,(0,0,1):C.R2GC_860_288,(0,0,7):C.R2GC_864_299,(0,0,2):C.R2GC_860_290,(0,0,6):C.R2GC_864_300})

V_442 = CTVertex(name = 'V_442',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qd1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qd1, P.YS3u2] ], [ [P.g, P.YS3Qd1, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_817_264,(1,0,8):C.R2GC_817_265,(1,0,1):C.R2GC_817_266,(1,0,7):C.R2GC_817_267,(1,0,2):C.R2GC_817_268,(1,0,6):C.R2GC_817_269,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_782_218,(0,0,8):C.R2GC_816_260,(0,0,1):C.R2GC_127_9,(0,0,7):C.R2GC_816_261,(0,0,2):C.R2GC_816_262,(0,0,6):C.R2GC_816_263})

V_443 = CTVertex(name = 'V_443',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qd2, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qd2, P.YS3u2] ], [ [P.g, P.YS3Qd2, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_817_264,(1,0,8):C.R2GC_817_265,(1,0,1):C.R2GC_817_266,(1,0,7):C.R2GC_817_267,(1,0,2):C.R2GC_817_268,(1,0,6):C.R2GC_817_269,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_782_218,(0,0,8):C.R2GC_816_260,(0,0,1):C.R2GC_127_9,(0,0,7):C.R2GC_816_261,(0,0,2):C.R2GC_816_262,(0,0,6):C.R2GC_816_263})

V_444 = CTVertex(name = 'V_444',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qd3, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qd3, P.YS3u2] ], [ [P.g, P.YS3Qd3, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_817_264,(1,0,8):C.R2GC_817_265,(1,0,1):C.R2GC_817_266,(1,0,7):C.R2GC_817_267,(1,0,2):C.R2GC_817_268,(1,0,6):C.R2GC_817_269,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_782_218,(0,0,8):C.R2GC_816_260,(0,0,1):C.R2GC_127_9,(0,0,7):C.R2GC_816_261,(0,0,2):C.R2GC_816_262,(0,0,6):C.R2GC_816_263})

V_445 = CTVertex(name = 'V_445',
                 type = 'R2',
                 particles = [ P.YS3u1__tilde__, P.YS3u1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3u1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3u1], [P.g, P.YS3u2] ], [ [P.g, P.YS3u1, P.YS3u2] ], [ [P.g, P.YS3u1, P.YS3u2, P.Z] ], [ [P.g, P.YS3u1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_861_292,(1,0,8):C.R2GC_915_311,(1,0,1):C.R2GC_861_294,(1,0,7):C.R2GC_915_312,(1,0,2):C.R2GC_861_296,(1,0,6):C.R2GC_915_313,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_860_286,(0,0,8):C.R2GC_914_308,(0,0,1):C.R2GC_860_288,(0,0,7):C.R2GC_914_309,(0,0,2):C.R2GC_860_290,(0,0,6):C.R2GC_914_310})

V_446 = CTVertex(name = 'V_446',
                 type = 'R2',
                 particles = [ P.YS3u2__tilde__, P.YS3u2__tilde__, P.YS3u2, P.YS3u2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3u2] ], [ [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_268_118,(1,0,3):C.R2GC_268_119,(1,0,0):C.R2GC_788_224,(1,0,5):C.R2GC_791_228,(1,0,1):C.R2GC_788_226,(1,0,4):C.R2GC_791_229,(0,0,2):C.R2GC_268_118,(0,0,3):C.R2GC_268_119,(0,0,0):C.R2GC_788_224,(0,0,5):C.R2GC_791_228,(0,0,1):C.R2GC_788_226,(0,0,4):C.R2GC_791_229})

V_447 = CTVertex(name = 'V_447',
                 type = 'R2',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qu1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qu1, P.YS3u3] ], [ [P.g, P.YS3Qu1, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_861_292,(1,0,8):C.R2GC_865_301,(1,0,1):C.R2GC_861_294,(1,0,7):C.R2GC_865_302,(1,0,2):C.R2GC_861_296,(1,0,6):C.R2GC_865_303,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_860_286,(0,0,8):C.R2GC_864_298,(0,0,1):C.R2GC_860_288,(0,0,7):C.R2GC_864_299,(0,0,2):C.R2GC_860_290,(0,0,6):C.R2GC_864_300})

V_448 = CTVertex(name = 'V_448',
                 type = 'R2',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qu2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qu2, P.YS3u3] ], [ [P.g, P.YS3Qu2, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_861_292,(1,0,8):C.R2GC_865_301,(1,0,1):C.R2GC_861_294,(1,0,7):C.R2GC_865_302,(1,0,2):C.R2GC_861_296,(1,0,6):C.R2GC_865_303,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_860_286,(0,0,8):C.R2GC_864_298,(0,0,1):C.R2GC_860_288,(0,0,7):C.R2GC_864_299,(0,0,2):C.R2GC_860_290,(0,0,6):C.R2GC_864_300})

V_449 = CTVertex(name = 'V_449',
                 type = 'R2',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qu3, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qu3], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qu3, P.YS3u3] ], [ [P.g, P.YS3Qu3, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qu3, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_861_292,(1,0,8):C.R2GC_865_301,(1,0,1):C.R2GC_861_294,(1,0,7):C.R2GC_865_302,(1,0,2):C.R2GC_861_296,(1,0,6):C.R2GC_865_303,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_860_286,(0,0,8):C.R2GC_864_298,(0,0,1):C.R2GC_860_288,(0,0,7):C.R2GC_864_299,(0,0,2):C.R2GC_860_290,(0,0,6):C.R2GC_864_300})

V_450 = CTVertex(name = 'V_450',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qd1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qd1, P.YS3u3] ], [ [P.g, P.YS3Qd1, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_817_264,(1,0,8):C.R2GC_817_265,(1,0,1):C.R2GC_817_266,(1,0,7):C.R2GC_817_267,(1,0,2):C.R2GC_817_268,(1,0,6):C.R2GC_817_269,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_782_218,(0,0,8):C.R2GC_816_260,(0,0,1):C.R2GC_127_9,(0,0,7):C.R2GC_816_261,(0,0,2):C.R2GC_816_262,(0,0,6):C.R2GC_816_263})

V_451 = CTVertex(name = 'V_451',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qd2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qd2, P.YS3u3] ], [ [P.g, P.YS3Qd2, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_817_264,(1,0,8):C.R2GC_817_265,(1,0,1):C.R2GC_817_266,(1,0,7):C.R2GC_817_267,(1,0,2):C.R2GC_817_268,(1,0,6):C.R2GC_817_269,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_782_218,(0,0,8):C.R2GC_816_260,(0,0,1):C.R2GC_127_9,(0,0,7):C.R2GC_816_261,(0,0,2):C.R2GC_816_262,(0,0,6):C.R2GC_816_263})

V_452 = CTVertex(name = 'V_452',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qd3, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qd3, P.YS3u3] ], [ [P.g, P.YS3Qd3, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_817_264,(1,0,8):C.R2GC_817_265,(1,0,1):C.R2GC_817_266,(1,0,7):C.R2GC_817_267,(1,0,2):C.R2GC_817_268,(1,0,6):C.R2GC_817_269,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_782_218,(0,0,8):C.R2GC_816_260,(0,0,1):C.R2GC_127_9,(0,0,7):C.R2GC_816_261,(0,0,2):C.R2GC_816_262,(0,0,6):C.R2GC_816_263})

V_453 = CTVertex(name = 'V_453',
                 type = 'R2',
                 particles = [ P.YS3u1__tilde__, P.YS3u1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3u1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3u1], [P.g, P.YS3u3] ], [ [P.g, P.YS3u1, P.YS3u3] ], [ [P.g, P.YS3u1, P.YS3u3, P.Z] ], [ [P.g, P.YS3u1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_861_292,(1,0,8):C.R2GC_915_311,(1,0,1):C.R2GC_861_294,(1,0,7):C.R2GC_915_312,(1,0,2):C.R2GC_861_296,(1,0,6):C.R2GC_915_313,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_860_286,(0,0,8):C.R2GC_914_308,(0,0,1):C.R2GC_860_288,(0,0,7):C.R2GC_914_309,(0,0,2):C.R2GC_860_290,(0,0,6):C.R2GC_914_310})

V_454 = CTVertex(name = 'V_454',
                 type = 'R2',
                 particles = [ P.YS3u2__tilde__, P.YS3u2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3u2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3u2], [P.g, P.YS3u3] ], [ [P.g, P.YS3u2, P.YS3u3] ], [ [P.g, P.YS3u2, P.YS3u3, P.Z] ], [ [P.g, P.YS3u2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_861_292,(1,0,8):C.R2GC_915_311,(1,0,1):C.R2GC_861_294,(1,0,7):C.R2GC_915_312,(1,0,2):C.R2GC_861_296,(1,0,6):C.R2GC_915_313,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_860_286,(0,0,8):C.R2GC_914_308,(0,0,1):C.R2GC_860_288,(0,0,7):C.R2GC_914_309,(0,0,2):C.R2GC_860_290,(0,0,6):C.R2GC_914_310})

V_455 = CTVertex(name = 'V_455',
                 type = 'R2',
                 particles = [ P.YS3u3__tilde__, P.YS3u3__tilde__, P.YS3u3, P.YS3u3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3u3] ], [ [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_268_118,(1,0,3):C.R2GC_268_119,(1,0,0):C.R2GC_788_224,(1,0,5):C.R2GC_791_228,(1,0,1):C.R2GC_788_226,(1,0,4):C.R2GC_791_229,(0,0,2):C.R2GC_268_118,(0,0,3):C.R2GC_268_119,(0,0,0):C.R2GC_788_224,(0,0,5):C.R2GC_791_228,(0,0,1):C.R2GC_788_226,(0,0,4):C.R2GC_791_229})

V_456 = CTVertex(name = 'V_456',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3d1, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3d1, P.YS3Qu1] ], [ [P.g, P.YS3d1, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_817_264,(1,0,8):C.R2GC_849_273,(1,0,1):C.R2GC_817_266,(1,0,7):C.R2GC_849_274,(1,0,2):C.R2GC_817_268,(1,0,6):C.R2GC_849_275,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_782_218,(0,0,8):C.R2GC_848_270,(0,0,1):C.R2GC_127_9,(0,0,7):C.R2GC_848_271,(0,0,2):C.R2GC_816_262,(0,0,6):C.R2GC_848_272})

V_457 = CTVertex(name = 'V_457',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3d1, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3d1, P.YS3Qu2] ], [ [P.g, P.YS3d1, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_817_264,(1,0,8):C.R2GC_849_273,(1,0,1):C.R2GC_817_266,(1,0,7):C.R2GC_849_274,(1,0,2):C.R2GC_817_268,(1,0,6):C.R2GC_849_275,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_782_218,(0,0,8):C.R2GC_848_270,(0,0,1):C.R2GC_127_9,(0,0,7):C.R2GC_848_271,(0,0,2):C.R2GC_816_262,(0,0,6):C.R2GC_848_272})

V_458 = CTVertex(name = 'V_458',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3d1, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3d1, P.YS3Qu3] ], [ [P.g, P.YS3d1, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_817_264,(1,0,8):C.R2GC_849_273,(1,0,1):C.R2GC_817_266,(1,0,7):C.R2GC_849_274,(1,0,2):C.R2GC_817_268,(1,0,6):C.R2GC_849_275,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_782_218,(0,0,8):C.R2GC_848_270,(0,0,1):C.R2GC_127_9,(0,0,7):C.R2GC_848_271,(0,0,2):C.R2GC_816_262,(0,0,6):C.R2GC_848_272})

V_459 = CTVertex(name = 'V_459',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qd1] ], [ [P.a, P.g, P.YS3d1, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qd1] ], [ [P.g, P.YS3d1, P.YS3Qd1] ], [ [P.g, P.YS3d1, P.YS3Qd1, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_801_242,(1,0,8):C.R2GC_807_251,(1,0,1):C.R2GC_801_244,(1,0,7):C.R2GC_807_252,(1,0,2):C.R2GC_801_246,(1,0,6):C.R2GC_807_253,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_800_236,(0,0,8):C.R2GC_806_248,(0,0,1):C.R2GC_800_238,(0,0,7):C.R2GC_806_249,(0,0,2):C.R2GC_800_240,(0,0,6):C.R2GC_806_250})

V_460 = CTVertex(name = 'V_460',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3d1, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3d1, P.YS3Qd2] ], [ [P.g, P.YS3d1, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_801_242,(1,0,8):C.R2GC_807_251,(1,0,1):C.R2GC_801_244,(1,0,7):C.R2GC_807_252,(1,0,2):C.R2GC_801_246,(1,0,6):C.R2GC_807_253,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_800_236,(0,0,8):C.R2GC_806_248,(0,0,1):C.R2GC_800_238,(0,0,7):C.R2GC_806_249,(0,0,2):C.R2GC_800_240,(0,0,6):C.R2GC_806_250})

V_461 = CTVertex(name = 'V_461',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3d1, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3d1, P.YS3Qd3] ], [ [P.g, P.YS3d1, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_801_242,(1,0,8):C.R2GC_807_251,(1,0,1):C.R2GC_801_244,(1,0,7):C.R2GC_807_252,(1,0,2):C.R2GC_801_246,(1,0,6):C.R2GC_807_253,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_800_236,(0,0,8):C.R2GC_806_248,(0,0,1):C.R2GC_800_238,(0,0,7):C.R2GC_806_249,(0,0,2):C.R2GC_800_240,(0,0,6):C.R2GC_806_250})

V_462 = CTVertex(name = 'V_462',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3d1, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3u1] ], [ [P.g, P.YS3d1, P.YS3u1] ], [ [P.g, P.YS3d1, P.YS3u1, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_817_264,(1,0,8):C.R2GC_909_305,(1,0,1):C.R2GC_817_266,(1,0,7):C.R2GC_909_306,(1,0,2):C.R2GC_817_268,(1,0,6):C.R2GC_909_307,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_782_218,(0,0,8):C.R2GC_782_219,(0,0,1):C.R2GC_127_9,(0,0,7):C.R2GC_132_40,(0,0,2):C.R2GC_816_262,(0,0,6):C.R2GC_908_304})

V_463 = CTVertex(name = 'V_463',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3d1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3u2] ], [ [P.g, P.YS3d1, P.YS3u2] ], [ [P.g, P.YS3d1, P.YS3u2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_817_264,(1,0,8):C.R2GC_909_305,(1,0,1):C.R2GC_817_266,(1,0,7):C.R2GC_909_306,(1,0,2):C.R2GC_817_268,(1,0,6):C.R2GC_909_307,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_782_218,(0,0,8):C.R2GC_782_219,(0,0,1):C.R2GC_127_9,(0,0,7):C.R2GC_132_40,(0,0,2):C.R2GC_816_262,(0,0,6):C.R2GC_908_304})

V_464 = CTVertex(name = 'V_464',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3d1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3u3] ], [ [P.g, P.YS3d1, P.YS3u3] ], [ [P.g, P.YS3d1, P.YS3u3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_817_264,(1,0,8):C.R2GC_909_305,(1,0,1):C.R2GC_817_266,(1,0,7):C.R2GC_909_306,(1,0,2):C.R2GC_817_268,(1,0,6):C.R2GC_909_307,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_782_218,(0,0,8):C.R2GC_782_219,(0,0,1):C.R2GC_127_9,(0,0,7):C.R2GC_132_40,(0,0,2):C.R2GC_816_262,(0,0,6):C.R2GC_908_304})

V_465 = CTVertex(name = 'V_465',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1__tilde__, P.YS3d1, P.YS3d1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1] ], [ [P.g] ], [ [P.g, P.YS3d1] ], [ [P.g, P.YS3d1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_268_118,(1,0,3):C.R2GC_268_119,(1,0,0):C.R2GC_782_218,(1,0,5):C.R2GC_782_219,(1,0,1):C.R2GC_782_220,(1,0,4):C.R2GC_782_221,(0,0,2):C.R2GC_268_118,(0,0,3):C.R2GC_268_119,(0,0,0):C.R2GC_782_218,(0,0,5):C.R2GC_782_219,(0,0,1):C.R2GC_782_220,(0,0,4):C.R2GC_782_221})

V_466 = CTVertex(name = 'V_466',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3d2, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3d2, P.YS3Qu1] ], [ [P.g, P.YS3d2, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_817_264,(1,0,8):C.R2GC_849_273,(1,0,1):C.R2GC_817_266,(1,0,7):C.R2GC_849_274,(1,0,2):C.R2GC_817_268,(1,0,6):C.R2GC_849_275,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_782_218,(0,0,8):C.R2GC_848_270,(0,0,1):C.R2GC_127_9,(0,0,7):C.R2GC_848_271,(0,0,2):C.R2GC_816_262,(0,0,6):C.R2GC_848_272})

V_467 = CTVertex(name = 'V_467',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3d2, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3d2, P.YS3Qu2] ], [ [P.g, P.YS3d2, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_817_264,(1,0,8):C.R2GC_849_273,(1,0,1):C.R2GC_817_266,(1,0,7):C.R2GC_849_274,(1,0,2):C.R2GC_817_268,(1,0,6):C.R2GC_849_275,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_782_218,(0,0,8):C.R2GC_848_270,(0,0,1):C.R2GC_127_9,(0,0,7):C.R2GC_848_271,(0,0,2):C.R2GC_816_262,(0,0,6):C.R2GC_848_272})

V_468 = CTVertex(name = 'V_468',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3d2, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3d2, P.YS3Qu3] ], [ [P.g, P.YS3d2, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_817_264,(1,0,8):C.R2GC_849_273,(1,0,1):C.R2GC_817_266,(1,0,7):C.R2GC_849_274,(1,0,2):C.R2GC_817_268,(1,0,6):C.R2GC_849_275,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_782_218,(0,0,8):C.R2GC_848_270,(0,0,1):C.R2GC_127_9,(0,0,7):C.R2GC_848_271,(0,0,2):C.R2GC_816_262,(0,0,6):C.R2GC_848_272})

V_469 = CTVertex(name = 'V_469',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qd1] ], [ [P.a, P.g, P.YS3d2, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qd1] ], [ [P.g, P.YS3d2, P.YS3Qd1] ], [ [P.g, P.YS3d2, P.YS3Qd1, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_801_242,(1,0,8):C.R2GC_807_251,(1,0,1):C.R2GC_801_244,(1,0,7):C.R2GC_807_252,(1,0,2):C.R2GC_801_246,(1,0,6):C.R2GC_807_253,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_800_236,(0,0,8):C.R2GC_806_248,(0,0,1):C.R2GC_800_238,(0,0,7):C.R2GC_806_249,(0,0,2):C.R2GC_800_240,(0,0,6):C.R2GC_806_250})

V_470 = CTVertex(name = 'V_470',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3d2, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3d2, P.YS3Qd2] ], [ [P.g, P.YS3d2, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_801_242,(1,0,8):C.R2GC_807_251,(1,0,1):C.R2GC_801_244,(1,0,7):C.R2GC_807_252,(1,0,2):C.R2GC_801_246,(1,0,6):C.R2GC_807_253,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_800_236,(0,0,8):C.R2GC_806_248,(0,0,1):C.R2GC_800_238,(0,0,7):C.R2GC_806_249,(0,0,2):C.R2GC_800_240,(0,0,6):C.R2GC_806_250})

V_471 = CTVertex(name = 'V_471',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3d2, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3d2, P.YS3Qd3] ], [ [P.g, P.YS3d2, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_801_242,(1,0,8):C.R2GC_807_251,(1,0,1):C.R2GC_801_244,(1,0,7):C.R2GC_807_252,(1,0,2):C.R2GC_801_246,(1,0,6):C.R2GC_807_253,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_800_236,(0,0,8):C.R2GC_806_248,(0,0,1):C.R2GC_800_238,(0,0,7):C.R2GC_806_249,(0,0,2):C.R2GC_800_240,(0,0,6):C.R2GC_806_250})

V_472 = CTVertex(name = 'V_472',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3d2, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3u1] ], [ [P.g, P.YS3d2, P.YS3u1] ], [ [P.g, P.YS3d2, P.YS3u1, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_817_264,(1,0,8):C.R2GC_909_305,(1,0,1):C.R2GC_817_266,(1,0,7):C.R2GC_909_306,(1,0,2):C.R2GC_817_268,(1,0,6):C.R2GC_909_307,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_782_218,(0,0,8):C.R2GC_782_219,(0,0,1):C.R2GC_127_9,(0,0,7):C.R2GC_132_40,(0,0,2):C.R2GC_816_262,(0,0,6):C.R2GC_908_304})

V_473 = CTVertex(name = 'V_473',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3d2, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3u2] ], [ [P.g, P.YS3d2, P.YS3u2] ], [ [P.g, P.YS3d2, P.YS3u2, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_817_264,(1,0,8):C.R2GC_909_305,(1,0,1):C.R2GC_817_266,(1,0,7):C.R2GC_909_306,(1,0,2):C.R2GC_817_268,(1,0,6):C.R2GC_909_307,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_782_218,(0,0,8):C.R2GC_782_219,(0,0,1):C.R2GC_127_9,(0,0,7):C.R2GC_132_40,(0,0,2):C.R2GC_816_262,(0,0,6):C.R2GC_908_304})

V_474 = CTVertex(name = 'V_474',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3d2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3u3] ], [ [P.g, P.YS3d2, P.YS3u3] ], [ [P.g, P.YS3d2, P.YS3u3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_817_264,(1,0,8):C.R2GC_909_305,(1,0,1):C.R2GC_817_266,(1,0,7):C.R2GC_909_306,(1,0,2):C.R2GC_817_268,(1,0,6):C.R2GC_909_307,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_782_218,(0,0,8):C.R2GC_782_219,(0,0,1):C.R2GC_127_9,(0,0,7):C.R2GC_132_40,(0,0,2):C.R2GC_816_262,(0,0,6):C.R2GC_908_304})

V_475 = CTVertex(name = 'V_475',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3d2] ], [ [P.a, P.g, P.YS3d1, P.YS3d2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3d2] ], [ [P.g, P.YS3d1, P.YS3d2] ], [ [P.g, P.YS3d1, P.YS3d2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3d2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_801_242,(1,0,8):C.R2GC_801_243,(1,0,1):C.R2GC_801_244,(1,0,7):C.R2GC_801_245,(1,0,2):C.R2GC_801_246,(1,0,6):C.R2GC_801_247,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_800_236,(0,0,8):C.R2GC_800_237,(0,0,1):C.R2GC_800_238,(0,0,7):C.R2GC_800_239,(0,0,2):C.R2GC_800_240,(0,0,6):C.R2GC_800_241})

V_476 = CTVertex(name = 'V_476',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2__tilde__, P.YS3d2, P.YS3d2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2] ], [ [P.g] ], [ [P.g, P.YS3d2] ], [ [P.g, P.YS3d2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_268_118,(1,0,3):C.R2GC_268_119,(1,0,0):C.R2GC_782_218,(1,0,5):C.R2GC_782_219,(1,0,1):C.R2GC_782_220,(1,0,4):C.R2GC_782_221,(0,0,2):C.R2GC_268_118,(0,0,3):C.R2GC_268_119,(0,0,0):C.R2GC_782_218,(0,0,5):C.R2GC_782_219,(0,0,1):C.R2GC_782_220,(0,0,4):C.R2GC_782_221})

V_477 = CTVertex(name = 'V_477',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3d3, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3d3, P.YS3Qu1] ], [ [P.g, P.YS3d3, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_817_264,(1,0,8):C.R2GC_849_273,(1,0,1):C.R2GC_817_266,(1,0,7):C.R2GC_849_274,(1,0,2):C.R2GC_817_268,(1,0,6):C.R2GC_849_275,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_782_218,(0,0,8):C.R2GC_848_270,(0,0,1):C.R2GC_127_9,(0,0,7):C.R2GC_848_271,(0,0,2):C.R2GC_816_262,(0,0,6):C.R2GC_848_272})

V_478 = CTVertex(name = 'V_478',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3d3, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3d3, P.YS3Qu2] ], [ [P.g, P.YS3d3, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_817_264,(1,0,8):C.R2GC_849_273,(1,0,1):C.R2GC_817_266,(1,0,7):C.R2GC_849_274,(1,0,2):C.R2GC_817_268,(1,0,6):C.R2GC_849_275,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_782_218,(0,0,8):C.R2GC_848_270,(0,0,1):C.R2GC_127_9,(0,0,7):C.R2GC_848_271,(0,0,2):C.R2GC_816_262,(0,0,6):C.R2GC_848_272})

V_479 = CTVertex(name = 'V_479',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3d3, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3d3, P.YS3Qu3] ], [ [P.g, P.YS3d3, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_817_264,(1,0,8):C.R2GC_849_273,(1,0,1):C.R2GC_817_266,(1,0,7):C.R2GC_849_274,(1,0,2):C.R2GC_817_268,(1,0,6):C.R2GC_849_275,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_782_218,(0,0,8):C.R2GC_848_270,(0,0,1):C.R2GC_127_9,(0,0,7):C.R2GC_848_271,(0,0,2):C.R2GC_816_262,(0,0,6):C.R2GC_848_272})

V_480 = CTVertex(name = 'V_480',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qd1] ], [ [P.a, P.g, P.YS3d3, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qd1] ], [ [P.g, P.YS3d3, P.YS3Qd1] ], [ [P.g, P.YS3d3, P.YS3Qd1, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_801_242,(1,0,8):C.R2GC_807_251,(1,0,1):C.R2GC_801_244,(1,0,7):C.R2GC_807_252,(1,0,2):C.R2GC_801_246,(1,0,6):C.R2GC_807_253,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_800_236,(0,0,8):C.R2GC_806_248,(0,0,1):C.R2GC_800_238,(0,0,7):C.R2GC_806_249,(0,0,2):C.R2GC_800_240,(0,0,6):C.R2GC_806_250})

V_481 = CTVertex(name = 'V_481',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3d3, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3d3, P.YS3Qd2] ], [ [P.g, P.YS3d3, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_801_242,(1,0,8):C.R2GC_807_251,(1,0,1):C.R2GC_801_244,(1,0,7):C.R2GC_807_252,(1,0,2):C.R2GC_801_246,(1,0,6):C.R2GC_807_253,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_800_236,(0,0,8):C.R2GC_806_248,(0,0,1):C.R2GC_800_238,(0,0,7):C.R2GC_806_249,(0,0,2):C.R2GC_800_240,(0,0,6):C.R2GC_806_250})

V_482 = CTVertex(name = 'V_482',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3d3, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3d3, P.YS3Qd3] ], [ [P.g, P.YS3d3, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_801_242,(1,0,8):C.R2GC_807_251,(1,0,1):C.R2GC_801_244,(1,0,7):C.R2GC_807_252,(1,0,2):C.R2GC_801_246,(1,0,6):C.R2GC_807_253,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_800_236,(0,0,8):C.R2GC_806_248,(0,0,1):C.R2GC_800_238,(0,0,7):C.R2GC_806_249,(0,0,2):C.R2GC_800_240,(0,0,6):C.R2GC_806_250})

V_483 = CTVertex(name = 'V_483',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3d3, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3u1] ], [ [P.g, P.YS3d3, P.YS3u1] ], [ [P.g, P.YS3d3, P.YS3u1, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_817_264,(1,0,8):C.R2GC_909_305,(1,0,1):C.R2GC_817_266,(1,0,7):C.R2GC_909_306,(1,0,2):C.R2GC_817_268,(1,0,6):C.R2GC_909_307,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_782_218,(0,0,8):C.R2GC_782_219,(0,0,1):C.R2GC_127_9,(0,0,7):C.R2GC_132_40,(0,0,2):C.R2GC_816_262,(0,0,6):C.R2GC_908_304})

V_484 = CTVertex(name = 'V_484',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3d3, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3u2] ], [ [P.g, P.YS3d3, P.YS3u2] ], [ [P.g, P.YS3d3, P.YS3u2, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_817_264,(1,0,8):C.R2GC_909_305,(1,0,1):C.R2GC_817_266,(1,0,7):C.R2GC_909_306,(1,0,2):C.R2GC_817_268,(1,0,6):C.R2GC_909_307,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_782_218,(0,0,8):C.R2GC_782_219,(0,0,1):C.R2GC_127_9,(0,0,7):C.R2GC_132_40,(0,0,2):C.R2GC_816_262,(0,0,6):C.R2GC_908_304})

V_485 = CTVertex(name = 'V_485',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3d3, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3u3] ], [ [P.g, P.YS3d3, P.YS3u3] ], [ [P.g, P.YS3d3, P.YS3u3, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_817_264,(1,0,8):C.R2GC_909_305,(1,0,1):C.R2GC_817_266,(1,0,7):C.R2GC_909_306,(1,0,2):C.R2GC_817_268,(1,0,6):C.R2GC_909_307,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_782_218,(0,0,8):C.R2GC_782_219,(0,0,1):C.R2GC_127_9,(0,0,7):C.R2GC_132_40,(0,0,2):C.R2GC_816_262,(0,0,6):C.R2GC_908_304})

V_486 = CTVertex(name = 'V_486',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3d3] ], [ [P.a, P.g, P.YS3d1, P.YS3d3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3d3] ], [ [P.g, P.YS3d1, P.YS3d3] ], [ [P.g, P.YS3d1, P.YS3d3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3d3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_801_242,(1,0,8):C.R2GC_801_243,(1,0,1):C.R2GC_801_244,(1,0,7):C.R2GC_801_245,(1,0,2):C.R2GC_801_246,(1,0,6):C.R2GC_801_247,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_800_236,(0,0,8):C.R2GC_800_237,(0,0,1):C.R2GC_800_238,(0,0,7):C.R2GC_800_239,(0,0,2):C.R2GC_800_240,(0,0,6):C.R2GC_800_241})

V_487 = CTVertex(name = 'V_487',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3d3] ], [ [P.a, P.g, P.YS3d2, P.YS3d3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3d3] ], [ [P.g, P.YS3d2, P.YS3d3] ], [ [P.g, P.YS3d2, P.YS3d3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3d3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_599_196,(1,0,4):C.R2GC_599_197,(1,0,5):C.R2GC_599_198,(1,0,0):C.R2GC_801_242,(1,0,8):C.R2GC_801_243,(1,0,1):C.R2GC_801_244,(1,0,7):C.R2GC_801_245,(1,0,2):C.R2GC_801_246,(1,0,6):C.R2GC_801_247,(0,0,3):C.R2GC_598_193,(0,0,4):C.R2GC_598_194,(0,0,5):C.R2GC_598_195,(0,0,0):C.R2GC_800_236,(0,0,8):C.R2GC_800_237,(0,0,1):C.R2GC_800_238,(0,0,7):C.R2GC_800_239,(0,0,2):C.R2GC_800_240,(0,0,6):C.R2GC_800_241})

V_488 = CTVertex(name = 'V_488',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3__tilde__, P.YS3d3, P.YS3d3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3] ], [ [P.g] ], [ [P.g, P.YS3d3] ], [ [P.g, P.YS3d3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_268_118,(1,0,3):C.R2GC_268_119,(1,0,0):C.R2GC_782_218,(1,0,5):C.R2GC_782_219,(1,0,1):C.R2GC_782_220,(1,0,4):C.R2GC_782_221,(0,0,2):C.R2GC_268_118,(0,0,3):C.R2GC_268_119,(0,0,0):C.R2GC_782_218,(0,0,5):C.R2GC_782_219,(0,0,1):C.R2GC_782_220,(0,0,4):C.R2GC_782_221})

V_489 = CTVertex(name = 'V_489',
                 type = 'UV',
                 particles = [ P.g, P.g, P.g ],
                 color = [ 'f(1,2,3)' ],
                 lorentz = [ L.VVV2, L.VVV3, L.VVV4, L.VVV5, L.VVV6, L.VVV7 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_231_159,(0,0,1):C.UVGC_231_160,(0,0,2):C.UVGC_231_161,(0,0,3):C.UVGC_231_162,(0,0,4):C.UVGC_231_163,(0,0,5):C.UVGC_231_164,(0,0,6):C.UVGC_231_165,(0,0,7):C.UVGC_231_166,(0,0,8):C.UVGC_231_167,(0,0,9):C.UVGC_231_168,(0,0,10):C.UVGC_231_169,(0,0,11):C.UVGC_231_170,(0,0,12):C.UVGC_231_171,(0,0,13):C.UVGC_231_172,(0,0,14):C.UVGC_231_173,(0,0,15):C.UVGC_231_174,(0,0,16):C.UVGC_231_175,(0,0,17):C.UVGC_231_176,(0,0,18):C.UVGC_231_177,(0,0,19):C.UVGC_231_178,(0,0,20):C.UVGC_231_179,(0,0,21):C.UVGC_231_180,(0,0,22):C.UVGC_231_181,(0,0,23):C.UVGC_231_182,(0,0,24):C.UVGC_231_183,(0,0,25):C.UVGC_231_184,(0,0,26):C.UVGC_231_185,(0,0,27):C.UVGC_231_186,(0,0,28):C.UVGC_231_187,(0,0,29):C.UVGC_231_188,(0,0,30):C.UVGC_231_189,(0,0,31):C.UVGC_231_190,(0,1,0):C.UVGC_230_127,(0,1,1):C.UVGC_230_128,(0,1,2):C.UVGC_230_129,(0,1,3):C.UVGC_230_130,(0,1,4):C.UVGC_230_131,(0,1,5):C.UVGC_230_132,(0,1,6):C.UVGC_230_133,(0,1,7):C.UVGC_230_134,(0,1,8):C.UVGC_230_135,(0,1,9):C.UVGC_230_136,(0,1,10):C.UVGC_230_137,(0,1,11):C.UVGC_230_138,(0,1,12):C.UVGC_230_139,(0,1,13):C.UVGC_230_140,(0,1,14):C.UVGC_230_141,(0,1,15):C.UVGC_230_142,(0,1,16):C.UVGC_230_143,(0,1,17):C.UVGC_230_144,(0,1,18):C.UVGC_230_145,(0,1,19):C.UVGC_230_146,(0,1,20):C.UVGC_230_147,(0,1,21):C.UVGC_230_148,(0,1,22):C.UVGC_230_149,(0,1,23):C.UVGC_230_150,(0,1,24):C.UVGC_230_151,(0,1,25):C.UVGC_230_152,(0,1,26):C.UVGC_230_153,(0,1,27):C.UVGC_230_154,(0,1,28):C.UVGC_230_155,(0,1,29):C.UVGC_230_156,(0,1,30):C.UVGC_230_157,(0,1,31):C.UVGC_230_158,(0,2,0):C.UVGC_230_127,(0,2,1):C.UVGC_230_128,(0,2,2):C.UVGC_230_129,(0,2,3):C.UVGC_230_130,(0,2,4):C.UVGC_230_131,(0,2,5):C.UVGC_230_132,(0,2,6):C.UVGC_230_133,(0,2,7):C.UVGC_230_134,(0,2,8):C.UVGC_230_135,(0,2,9):C.UVGC_230_136,(0,2,10):C.UVGC_230_137,(0,2,11):C.UVGC_230_138,(0,2,12):C.UVGC_230_139,(0,2,13):C.UVGC_230_140,(0,2,14):C.UVGC_230_141,(0,2,15):C.UVGC_230_142,(0,2,16):C.UVGC_230_143,(0,2,17):C.UVGC_230_144,(0,2,18):C.UVGC_230_145,(0,2,19):C.UVGC_230_146,(0,2,20):C.UVGC_230_147,(0,2,21):C.UVGC_230_148,(0,2,22):C.UVGC_230_149,(0,2,23):C.UVGC_230_150,(0,2,24):C.UVGC_230_151,(0,2,25):C.UVGC_230_152,(0,2,26):C.UVGC_230_153,(0,2,27):C.UVGC_230_154,(0,2,28):C.UVGC_230_155,(0,2,29):C.UVGC_230_156,(0,2,30):C.UVGC_230_157,(0,2,31):C.UVGC_230_158,(0,3,0):C.UVGC_231_159,(0,3,1):C.UVGC_231_160,(0,3,2):C.UVGC_231_161,(0,3,3):C.UVGC_231_162,(0,3,4):C.UVGC_231_163,(0,3,5):C.UVGC_231_164,(0,3,6):C.UVGC_231_165,(0,3,7):C.UVGC_231_166,(0,3,8):C.UVGC_231_167,(0,3,9):C.UVGC_231_168,(0,3,10):C.UVGC_231_169,(0,3,11):C.UVGC_231_170,(0,3,12):C.UVGC_231_171,(0,3,13):C.UVGC_231_172,(0,3,14):C.UVGC_231_173,(0,3,15):C.UVGC_231_174,(0,3,16):C.UVGC_231_175,(0,3,17):C.UVGC_231_176,(0,3,18):C.UVGC_231_177,(0,3,19):C.UVGC_231_178,(0,3,20):C.UVGC_231_179,(0,3,21):C.UVGC_231_180,(0,3,22):C.UVGC_231_181,(0,3,23):C.UVGC_231_182,(0,3,24):C.UVGC_231_183,(0,3,25):C.UVGC_231_184,(0,3,26):C.UVGC_231_185,(0,3,27):C.UVGC_231_186,(0,3,28):C.UVGC_231_187,(0,3,29):C.UVGC_231_188,(0,3,30):C.UVGC_231_189,(0,3,31):C.UVGC_231_190,(0,4,0):C.UVGC_231_159,(0,4,1):C.UVGC_231_160,(0,4,2):C.UVGC_231_161,(0,4,3):C.UVGC_231_162,(0,4,4):C.UVGC_231_163,(0,4,5):C.UVGC_231_164,(0,4,6):C.UVGC_231_165,(0,4,7):C.UVGC_231_166,(0,4,8):C.UVGC_231_167,(0,4,9):C.UVGC_231_168,(0,4,10):C.UVGC_231_169,(0,4,11):C.UVGC_231_170,(0,4,12):C.UVGC_231_171,(0,4,13):C.UVGC_231_172,(0,4,14):C.UVGC_231_173,(0,4,15):C.UVGC_231_174,(0,4,16):C.UVGC_231_175,(0,4,17):C.UVGC_231_176,(0,4,18):C.UVGC_231_177,(0,4,19):C.UVGC_231_178,(0,4,20):C.UVGC_231_179,(0,4,21):C.UVGC_231_180,(0,4,22):C.UVGC_231_181,(0,4,23):C.UVGC_231_182,(0,4,24):C.UVGC_231_183,(0,4,25):C.UVGC_231_184,(0,4,26):C.UVGC_231_185,(0,4,27):C.UVGC_231_186,(0,4,28):C.UVGC_231_187,(0,4,29):C.UVGC_231_188,(0,4,30):C.UVGC_231_189,(0,4,31):C.UVGC_231_190,(0,5,0):C.UVGC_230_127,(0,5,1):C.UVGC_230_128,(0,5,2):C.UVGC_230_129,(0,5,3):C.UVGC_230_130,(0,5,4):C.UVGC_230_131,(0,5,5):C.UVGC_230_132,(0,5,6):C.UVGC_230_133,(0,5,7):C.UVGC_230_134,(0,5,8):C.UVGC_230_135,(0,5,9):C.UVGC_230_136,(0,5,10):C.UVGC_230_137,(0,5,11):C.UVGC_230_138,(0,5,12):C.UVGC_230_139,(0,5,13):C.UVGC_230_140,(0,5,14):C.UVGC_230_141,(0,5,15):C.UVGC_230_142,(0,5,16):C.UVGC_230_143,(0,5,17):C.UVGC_230_144,(0,5,18):C.UVGC_230_145,(0,5,19):C.UVGC_230_146,(0,5,20):C.UVGC_230_147,(0,5,21):C.UVGC_230_148,(0,5,22):C.UVGC_230_149,(0,5,23):C.UVGC_230_150,(0,5,24):C.UVGC_230_151,(0,5,25):C.UVGC_230_152,(0,5,26):C.UVGC_230_153,(0,5,27):C.UVGC_230_154,(0,5,28):C.UVGC_230_155,(0,5,29):C.UVGC_230_156,(0,5,30):C.UVGC_230_157,(0,5,31):C.UVGC_230_158})

V_490 = CTVertex(name = 'V_490',
                 type = 'UV',
                 particles = [ P.g, P.g, P.g, P.g ],
                 color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u], [P.YF3d1], [P.YF3d2], [P.YF3d3], [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3], [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3], [P.YF3u1], [P.YF3u2], [P.YF3u3] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u], [P.YF3d1], [P.YF3d2], [P.YF3d3], [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3], [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3], [P.YF3u1], [P.YF3u2], [P.YF3u3], [P.YS3d1], [P.YS3d2], [P.YS3d3], [P.YS3Qd1], [P.YS3Qd2], [P.YS3Qd3], [P.YS3Qu1], [P.YS3Qu2], [P.YS3Qu3], [P.YS3u1], [P.YS3u2], [P.YS3u3] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d1], [P.YS3d2], [P.YS3d3], [P.YS3Qd1], [P.YS3Qd2], [P.YS3Qd3], [P.YS3Qu1], [P.YS3Qu2], [P.YS3Qu3], [P.YS3u1], [P.YS3u2], [P.YS3u3] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_225_90,(0,0,6):C.UVGC_225_89,(2,0,5):C.UVGC_225_90,(2,0,6):C.UVGC_225_89,(5,0,5):C.UVGC_224_87,(5,0,6):C.UVGC_224_88,(1,0,5):C.UVGC_224_87,(1,0,6):C.UVGC_224_88,(7,0,0):C.UVGC_233_223,(7,0,3):C.UVGC_233_224,(7,0,4):C.UVGC_233_225,(7,0,5):C.UVGC_234_255,(7,0,6):C.UVGC_234_256,(7,0,7):C.UVGC_233_228,(7,0,8):C.UVGC_233_229,(7,0,9):C.UVGC_233_230,(7,0,10):C.UVGC_233_231,(7,0,11):C.UVGC_233_232,(7,0,12):C.UVGC_233_233,(7,0,13):C.UVGC_233_234,(7,0,14):C.UVGC_233_235,(7,0,15):C.UVGC_233_236,(7,0,16):C.UVGC_233_237,(7,0,17):C.UVGC_233_238,(7,0,18):C.UVGC_233_239,(7,0,19):C.UVGC_233_240,(7,0,20):C.UVGC_233_241,(7,0,21):C.UVGC_233_242,(7,0,22):C.UVGC_233_243,(7,0,24):C.UVGC_233_244,(7,0,25):C.UVGC_233_245,(7,0,26):C.UVGC_233_246,(7,0,27):C.UVGC_233_247,(7,0,28):C.UVGC_233_248,(7,0,29):C.UVGC_233_249,(7,0,30):C.UVGC_233_250,(7,0,31):C.UVGC_233_251,(7,0,32):C.UVGC_233_252,(7,0,33):C.UVGC_233_253,(7,0,34):C.UVGC_233_254,(6,0,0):C.UVGC_233_223,(6,0,3):C.UVGC_233_224,(6,0,4):C.UVGC_233_225,(6,0,5):C.UVGC_233_226,(6,0,6):C.UVGC_233_227,(6,0,7):C.UVGC_233_228,(6,0,8):C.UVGC_233_229,(6,0,9):C.UVGC_233_230,(6,0,10):C.UVGC_233_231,(6,0,11):C.UVGC_233_232,(6,0,12):C.UVGC_233_233,(6,0,13):C.UVGC_233_234,(6,0,14):C.UVGC_233_235,(6,0,15):C.UVGC_233_236,(6,0,16):C.UVGC_233_237,(6,0,17):C.UVGC_233_238,(6,0,18):C.UVGC_233_239,(6,0,19):C.UVGC_233_240,(6,0,20):C.UVGC_233_241,(6,0,21):C.UVGC_233_242,(6,0,22):C.UVGC_233_243,(6,0,24):C.UVGC_233_244,(6,0,25):C.UVGC_233_245,(6,0,26):C.UVGC_233_246,(6,0,27):C.UVGC_233_247,(6,0,28):C.UVGC_233_248,(6,0,29):C.UVGC_233_249,(6,0,30):C.UVGC_233_250,(6,0,31):C.UVGC_233_251,(6,0,32):C.UVGC_233_252,(6,0,33):C.UVGC_233_253,(6,0,34):C.UVGC_233_254,(4,0,5):C.UVGC_224_87,(4,0,6):C.UVGC_224_88,(3,0,5):C.UVGC_224_87,(3,0,6):C.UVGC_224_88,(8,0,5):C.UVGC_225_89,(8,0,6):C.UVGC_225_90,(11,0,5):C.UVGC_228_93,(11,0,6):C.UVGC_228_94,(10,0,5):C.UVGC_228_93,(10,0,6):C.UVGC_228_94,(9,0,5):C.UVGC_227_91,(9,0,6):C.UVGC_227_92,(0,1,5):C.UVGC_225_90,(0,1,6):C.UVGC_225_89,(2,1,5):C.UVGC_225_90,(2,1,6):C.UVGC_225_89,(7,1,2):C.UVGC_235_257,(7,1,5):C.UVGC_225_89,(7,1,6):C.UVGC_238_321,(5,1,5):C.UVGC_224_87,(5,1,6):C.UVGC_224_88,(1,1,5):C.UVGC_224_87,(1,1,6):C.UVGC_224_88,(4,1,5):C.UVGC_224_87,(4,1,6):C.UVGC_224_88,(3,1,5):C.UVGC_224_87,(3,1,6):C.UVGC_224_88,(8,1,0):C.UVGC_237_290,(8,1,3):C.UVGC_237_291,(8,1,4):C.UVGC_237_292,(8,1,5):C.UVGC_234_255,(8,1,6):C.UVGC_237_293,(8,1,7):C.UVGC_237_294,(8,1,8):C.UVGC_237_295,(8,1,9):C.UVGC_237_296,(8,1,10):C.UVGC_237_297,(8,1,11):C.UVGC_237_298,(8,1,12):C.UVGC_237_299,(8,1,13):C.UVGC_237_300,(8,1,14):C.UVGC_237_301,(8,1,15):C.UVGC_237_302,(8,1,16):C.UVGC_237_303,(8,1,17):C.UVGC_237_304,(8,1,18):C.UVGC_237_305,(8,1,19):C.UVGC_237_306,(8,1,20):C.UVGC_237_307,(8,1,21):C.UVGC_237_308,(8,1,22):C.UVGC_237_309,(8,1,24):C.UVGC_237_310,(8,1,25):C.UVGC_237_311,(8,1,26):C.UVGC_237_312,(8,1,27):C.UVGC_237_313,(8,1,28):C.UVGC_237_314,(8,1,29):C.UVGC_237_315,(8,1,30):C.UVGC_237_316,(8,1,31):C.UVGC_237_317,(8,1,32):C.UVGC_237_318,(8,1,33):C.UVGC_237_319,(8,1,34):C.UVGC_237_320,(6,1,0):C.UVGC_232_191,(6,1,3):C.UVGC_232_192,(6,1,4):C.UVGC_232_193,(6,1,5):C.UVGC_239_322,(6,1,6):C.UVGC_239_323,(6,1,7):C.UVGC_232_196,(6,1,8):C.UVGC_232_197,(6,1,9):C.UVGC_232_198,(6,1,10):C.UVGC_232_199,(6,1,11):C.UVGC_232_200,(6,1,12):C.UVGC_232_201,(6,1,13):C.UVGC_232_202,(6,1,14):C.UVGC_232_203,(6,1,15):C.UVGC_232_204,(6,1,16):C.UVGC_232_205,(6,1,17):C.UVGC_232_206,(6,1,18):C.UVGC_232_207,(6,1,19):C.UVGC_232_208,(6,1,20):C.UVGC_232_209,(6,1,21):C.UVGC_232_210,(6,1,22):C.UVGC_239_324,(6,1,24):C.UVGC_239_325,(6,1,25):C.UVGC_239_326,(6,1,26):C.UVGC_239_327,(6,1,27):C.UVGC_239_328,(6,1,28):C.UVGC_239_329,(6,1,29):C.UVGC_239_330,(6,1,30):C.UVGC_239_331,(6,1,31):C.UVGC_239_332,(6,1,32):C.UVGC_239_333,(6,1,33):C.UVGC_239_334,(6,1,34):C.UVGC_239_335,(11,1,5):C.UVGC_228_93,(11,1,6):C.UVGC_228_94,(10,1,5):C.UVGC_228_93,(10,1,6):C.UVGC_228_94,(9,1,5):C.UVGC_227_91,(9,1,6):C.UVGC_227_92,(0,2,5):C.UVGC_225_90,(0,2,6):C.UVGC_225_89,(2,2,5):C.UVGC_225_90,(2,2,6):C.UVGC_225_89,(7,2,0):C.UVGC_232_191,(7,2,3):C.UVGC_232_192,(7,2,4):C.UVGC_232_193,(7,2,5):C.UVGC_232_194,(7,2,6):C.UVGC_232_195,(7,2,7):C.UVGC_232_196,(7,2,8):C.UVGC_232_197,(7,2,9):C.UVGC_232_198,(7,2,10):C.UVGC_232_199,(7,2,11):C.UVGC_232_200,(7,2,12):C.UVGC_232_201,(7,2,13):C.UVGC_232_202,(7,2,14):C.UVGC_232_203,(7,2,15):C.UVGC_232_204,(7,2,16):C.UVGC_232_205,(7,2,17):C.UVGC_232_206,(7,2,18):C.UVGC_232_207,(7,2,19):C.UVGC_232_208,(7,2,20):C.UVGC_232_209,(7,2,21):C.UVGC_232_210,(7,2,22):C.UVGC_232_211,(7,2,24):C.UVGC_232_212,(7,2,25):C.UVGC_232_213,(7,2,26):C.UVGC_232_214,(7,2,27):C.UVGC_232_215,(7,2,28):C.UVGC_232_216,(7,2,29):C.UVGC_232_217,(7,2,30):C.UVGC_232_218,(7,2,31):C.UVGC_232_219,(7,2,32):C.UVGC_232_220,(7,2,33):C.UVGC_232_221,(7,2,34):C.UVGC_232_222,(5,2,5):C.UVGC_224_87,(5,2,6):C.UVGC_224_88,(1,2,5):C.UVGC_224_87,(1,2,6):C.UVGC_224_88,(4,2,5):C.UVGC_224_87,(4,2,6):C.UVGC_224_88,(3,2,5):C.UVGC_224_87,(3,2,6):C.UVGC_224_88,(8,2,0):C.UVGC_236_259,(8,2,3):C.UVGC_236_260,(8,2,4):C.UVGC_236_261,(8,2,5):C.UVGC_232_194,(8,2,6):C.UVGC_236_262,(8,2,7):C.UVGC_236_263,(8,2,8):C.UVGC_236_264,(8,2,9):C.UVGC_236_265,(8,2,10):C.UVGC_236_266,(8,2,11):C.UVGC_236_267,(8,2,12):C.UVGC_236_268,(8,2,13):C.UVGC_236_269,(8,2,14):C.UVGC_236_270,(8,2,15):C.UVGC_236_271,(8,2,16):C.UVGC_236_272,(8,2,17):C.UVGC_236_273,(8,2,18):C.UVGC_236_274,(8,2,19):C.UVGC_236_275,(8,2,20):C.UVGC_236_276,(8,2,21):C.UVGC_236_277,(8,2,22):C.UVGC_236_278,(8,2,24):C.UVGC_236_279,(8,2,25):C.UVGC_236_280,(8,2,26):C.UVGC_236_281,(8,2,27):C.UVGC_236_282,(8,2,28):C.UVGC_236_283,(8,2,29):C.UVGC_236_284,(8,2,30):C.UVGC_236_285,(8,2,31):C.UVGC_236_286,(8,2,32):C.UVGC_236_287,(8,2,33):C.UVGC_236_288,(8,2,34):C.UVGC_236_289,(6,2,1):C.UVGC_235_257,(6,2,6):C.UVGC_227_91,(6,2,23):C.UVGC_235_258,(11,2,5):C.UVGC_228_93,(11,2,6):C.UVGC_228_94,(10,2,5):C.UVGC_228_93,(10,2,6):C.UVGC_228_94,(9,2,5):C.UVGC_227_91,(9,2,6):C.UVGC_227_92})

V_491 = CTVertex(name = 'V_491',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.YF3d1, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_243_371,(0,1,0):C.UVGC_165_28,(0,2,0):C.UVGC_167_30})

V_492 = CTVertex(name = 'V_492',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.YF3d2, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_243_371,(0,1,0):C.UVGC_171_34,(0,2,0):C.UVGC_173_36})

V_493 = CTVertex(name = 'V_493',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.YF3d3, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_243_371,(0,1,0):C.UVGC_177_40,(0,2,0):C.UVGC_179_42})

V_494 = CTVertex(name = 'V_494',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.YF3Qd1, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_243_371,(0,1,0):C.UVGC_183_46,(0,2,0):C.UVGC_185_48})

V_495 = CTVertex(name = 'V_495',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.YF3Qd2, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_243_371,(0,1,0):C.UVGC_187_50,(0,2,0):C.UVGC_189_52})

V_496 = CTVertex(name = 'V_496',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.YF3Qd3, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_243_371,(0,1,0):C.UVGC_191_54,(0,2,0):C.UVGC_193_56})

V_497 = CTVertex(name = 'V_497',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.YF3Qu1, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_250_377,(0,1,0):C.UVGC_195_58,(0,2,0):C.UVGC_197_60})

V_498 = CTVertex(name = 'V_498',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.YF3Qu2, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_250_377,(0,1,0):C.UVGC_199_62,(0,2,0):C.UVGC_201_64})

V_499 = CTVertex(name = 'V_499',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.YF3Qu3, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_250_377,(0,1,0):C.UVGC_203_66,(0,2,0):C.UVGC_205_68})

V_500 = CTVertex(name = 'V_500',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.YF3u1, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_250_377,(0,1,0):C.UVGC_207_70,(0,2,0):C.UVGC_209_72})

V_501 = CTVertex(name = 'V_501',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.YF3u2, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_250_377,(0,1,0):C.UVGC_213_76,(0,2,0):C.UVGC_215_78})

V_502 = CTVertex(name = 'V_502',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.YF3u3, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_250_377,(0,1,0):C.UVGC_219_82,(0,2,0):C.UVGC_221_84})

V_503 = CTVertex(name = 'V_503',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3Qu1, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_775_1075,(0,0,2):C.UVGC_776_1077,(0,0,1):C.UVGC_597_941})

V_504 = CTVertex(name = 'V_504',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3Qu1, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_775_1075,(0,0,2):C.UVGC_776_1077,(0,0,1):C.UVGC_597_941})

V_505 = CTVertex(name = 'V_505',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3Qd1, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_596_937,(0,0,2):C.UVGC_597_940,(0,0,1):C.UVGC_597_941})

V_506 = CTVertex(name = 'V_506',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3Qd1, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_596_937,(0,0,2):C.UVGC_597_940,(0,0,1):C.UVGC_597_941})

V_507 = CTVertex(name = 'V_507',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3Qu2, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_588_916,(0,0,2):C.UVGC_589_919,(0,0,1):C.UVGC_589_920})

V_508 = CTVertex(name = 'V_508',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3Qu2, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_588_916,(0,0,2):C.UVGC_589_919,(0,0,1):C.UVGC_589_920})

V_509 = CTVertex(name = 'V_509',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3Qd2, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_761_1044,(0,0,2):C.UVGC_762_1046,(0,0,1):C.UVGC_589_920})

V_510 = CTVertex(name = 'V_510',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3Qd2, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_761_1044,(0,0,2):C.UVGC_762_1046,(0,0,1):C.UVGC_589_920})

V_511 = CTVertex(name = 'V_511',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3Qu3, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_768_1060,(0,0,2):C.UVGC_769_1062,(0,0,1):C.UVGC_584_906})

V_512 = CTVertex(name = 'V_512',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3Qu3, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_768_1060,(0,0,2):C.UVGC_769_1062,(0,0,1):C.UVGC_584_906})

V_513 = CTVertex(name = 'V_513',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3Qd3, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_583_902,(0,0,2):C.UVGC_584_905,(0,0,1):C.UVGC_584_906})

V_514 = CTVertex(name = 'V_514',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3Qd3, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_583_902,(0,0,2):C.UVGC_584_905,(0,0,1):C.UVGC_584_906})

V_515 = CTVertex(name = 'V_515',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.d, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_594_932,(0,0,2):C.UVGC_595_935,(0,0,1):C.UVGC_595_936})

V_516 = CTVertex(name = 'V_516',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.s, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_759_1039,(0,0,2):C.UVGC_760_1042,(0,0,1):C.UVGC_760_1043})

V_517 = CTVertex(name = 'V_517',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.b, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_581_897,(0,0,2):C.UVGC_582_900,(0,0,1):C.UVGC_582_901})

V_518 = CTVertex(name = 'V_518',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.d, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_594_932,(0,0,2):C.UVGC_595_935,(0,0,1):C.UVGC_595_936})

V_519 = CTVertex(name = 'V_519',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.s, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_759_1039,(0,0,2):C.UVGC_760_1042,(0,0,1):C.UVGC_760_1043})

V_520 = CTVertex(name = 'V_520',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.b, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_581_897,(0,0,2):C.UVGC_582_900,(0,0,1):C.UVGC_582_901})

V_521 = CTVertex(name = 'V_521',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.u, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_777_1078,(0,0,2):C.UVGC_778_1081,(0,0,1):C.UVGC_778_1082})

V_522 = CTVertex(name = 'V_522',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.c, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_590_921,(0,0,2):C.UVGC_591_924,(0,0,1):C.UVGC_591_925})

V_523 = CTVertex(name = 'V_523',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.t, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_770_1063,(0,0,2):C.UVGC_771_1066,(0,0,1):C.UVGC_771_1067})

V_524 = CTVertex(name = 'V_524',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.u, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_777_1078,(0,0,2):C.UVGC_778_1081,(0,0,1):C.UVGC_778_1082})

V_525 = CTVertex(name = 'V_525',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.c, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_590_921,(0,0,2):C.UVGC_591_924,(0,0,1):C.UVGC_591_925})

V_526 = CTVertex(name = 'V_526',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.t, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_770_1063,(0,0,2):C.UVGC_771_1066,(0,0,1):C.UVGC_771_1067})

V_527 = CTVertex(name = 'V_527',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_764_1049,(0,0,2):C.UVGC_764_1050,(0,0,1):C.UVGC_764_1051})

V_528 = CTVertex(name = 'V_528',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_469_822})

V_529 = CTVertex(name = 'V_529',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_468_821})

V_530 = CTVertex(name = 'V_530',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3d1, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_594_932,(0,0,2):C.UVGC_595_935,(0,0,1):C.UVGC_595_936})

V_531 = CTVertex(name = 'V_531',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3d2, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_759_1039,(0,0,2):C.UVGC_760_1042,(0,0,1):C.UVGC_760_1043})

V_532 = CTVertex(name = 'V_532',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3d3, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_581_897,(0,0,2):C.UVGC_582_900,(0,0,1):C.UVGC_582_901})

V_533 = CTVertex(name = 'V_533',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3d1, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_594_932,(0,0,2):C.UVGC_595_935,(0,0,1):C.UVGC_595_936})

V_534 = CTVertex(name = 'V_534',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3d2, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_759_1039,(0,0,2):C.UVGC_760_1042,(0,0,1):C.UVGC_760_1043})

V_535 = CTVertex(name = 'V_535',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3d3, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_581_897,(0,0,2):C.UVGC_582_900,(0,0,1):C.UVGC_582_901})

V_536 = CTVertex(name = 'V_536',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3u1, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_777_1078,(0,0,2):C.UVGC_778_1081,(0,0,1):C.UVGC_778_1082})

V_537 = CTVertex(name = 'V_537',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3u2, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_590_921,(0,0,2):C.UVGC_591_924,(0,0,1):C.UVGC_591_925})

V_538 = CTVertex(name = 'V_538',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3u3, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_770_1063,(0,0,2):C.UVGC_771_1066,(0,0,1):C.UVGC_771_1067})

V_539 = CTVertex(name = 'V_539',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3u1, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_777_1078,(0,0,2):C.UVGC_778_1081,(0,0,1):C.UVGC_778_1082})

V_540 = CTVertex(name = 'V_540',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3u2, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_590_921,(0,0,2):C.UVGC_591_924,(0,0,1):C.UVGC_591_925})

V_541 = CTVertex(name = 'V_541',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3u3, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_770_1063,(0,0,2):C.UVGC_771_1066,(0,0,1):C.UVGC_771_1067})

V_542 = CTVertex(name = 'V_542',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.u, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_775_1075,(0,0,2):C.UVGC_776_1077,(0,0,1):C.UVGC_597_941})

V_543 = CTVertex(name = 'V_543',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.u, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_775_1075,(0,0,2):C.UVGC_776_1077,(0,0,1):C.UVGC_597_941})

V_544 = CTVertex(name = 'V_544',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.d, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_596_937,(0,0,2):C.UVGC_597_940,(0,0,1):C.UVGC_597_941})

V_545 = CTVertex(name = 'V_545',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.d, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_596_937,(0,0,2):C.UVGC_597_940,(0,0,1):C.UVGC_597_941})

V_546 = CTVertex(name = 'V_546',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.c, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_588_916,(0,0,2):C.UVGC_589_919,(0,0,1):C.UVGC_589_920})

V_547 = CTVertex(name = 'V_547',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.c, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_588_916,(0,0,2):C.UVGC_589_919,(0,0,1):C.UVGC_589_920})

V_548 = CTVertex(name = 'V_548',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.s, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_761_1044,(0,0,2):C.UVGC_762_1046,(0,0,1):C.UVGC_589_920})

V_549 = CTVertex(name = 'V_549',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.s, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_761_1044,(0,0,2):C.UVGC_762_1046,(0,0,1):C.UVGC_589_920})

V_550 = CTVertex(name = 'V_550',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.t, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_768_1060,(0,0,2):C.UVGC_769_1062,(0,0,1):C.UVGC_584_906})

V_551 = CTVertex(name = 'V_551',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.t, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_768_1060,(0,0,2):C.UVGC_769_1062,(0,0,1):C.UVGC_584_906})

V_552 = CTVertex(name = 'V_552',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.b, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_583_902,(0,0,2):C.UVGC_584_905,(0,0,1):C.UVGC_584_906})

V_553 = CTVertex(name = 'V_553',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.b, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_583_902,(0,0,2):C.UVGC_584_905,(0,0,1):C.UVGC_584_906})

V_554 = CTVertex(name = 'V_554',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.YF3Qd1, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3Qd1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_244_372,(0,1,0):C.UVGC_240_336,(0,1,1):C.UVGC_240_337,(0,1,2):C.UVGC_240_338,(0,1,3):C.UVGC_240_339,(0,1,4):C.UVGC_240_340,(0,1,6):C.UVGC_240_341,(0,1,7):C.UVGC_240_342,(0,1,8):C.UVGC_240_343,(0,1,9):C.UVGC_240_344,(0,1,10):C.UVGC_240_345,(0,1,11):C.UVGC_240_346,(0,1,12):C.UVGC_240_347,(0,1,13):C.UVGC_240_348,(0,1,14):C.UVGC_240_349,(0,1,15):C.UVGC_240_350,(0,1,16):C.UVGC_240_351,(0,1,17):C.UVGC_240_352,(0,1,18):C.UVGC_240_353,(0,1,19):C.UVGC_240_354,(0,1,20):C.UVGC_240_355,(0,1,21):C.UVGC_240_356,(0,1,22):C.UVGC_240_357,(0,1,23):C.UVGC_240_358,(0,1,24):C.UVGC_240_359,(0,1,25):C.UVGC_240_360,(0,1,26):C.UVGC_240_361,(0,1,27):C.UVGC_240_362,(0,1,28):C.UVGC_240_363,(0,1,29):C.UVGC_240_364,(0,1,30):C.UVGC_240_365,(0,1,31):C.UVGC_240_366,(0,1,32):C.UVGC_240_367,(0,1,5):C.UVGC_498_837,(0,2,0):C.UVGC_240_336,(0,2,1):C.UVGC_240_337,(0,2,2):C.UVGC_240_338,(0,2,3):C.UVGC_240_339,(0,2,4):C.UVGC_240_340,(0,2,6):C.UVGC_240_341,(0,2,7):C.UVGC_240_342,(0,2,8):C.UVGC_240_343,(0,2,9):C.UVGC_240_344,(0,2,10):C.UVGC_240_345,(0,2,11):C.UVGC_240_346,(0,2,12):C.UVGC_240_347,(0,2,13):C.UVGC_240_348,(0,2,14):C.UVGC_240_349,(0,2,15):C.UVGC_240_350,(0,2,16):C.UVGC_240_351,(0,2,17):C.UVGC_240_352,(0,2,18):C.UVGC_240_353,(0,2,19):C.UVGC_240_354,(0,2,20):C.UVGC_240_355,(0,2,21):C.UVGC_240_356,(0,2,22):C.UVGC_240_357,(0,2,23):C.UVGC_240_358,(0,2,24):C.UVGC_240_359,(0,2,25):C.UVGC_240_360,(0,2,26):C.UVGC_240_361,(0,2,27):C.UVGC_240_362,(0,2,28):C.UVGC_240_363,(0,2,29):C.UVGC_240_364,(0,2,30):C.UVGC_240_365,(0,2,31):C.UVGC_240_366,(0,2,32):C.UVGC_240_367,(0,2,5):C.UVGC_499_838})

V_555 = CTVertex(name = 'V_555',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.YF3Qd2, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3Qd2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_244_372,(0,1,0):C.UVGC_240_336,(0,1,1):C.UVGC_240_337,(0,1,2):C.UVGC_240_338,(0,1,3):C.UVGC_240_339,(0,1,4):C.UVGC_240_340,(0,1,6):C.UVGC_240_341,(0,1,7):C.UVGC_240_342,(0,1,8):C.UVGC_240_343,(0,1,9):C.UVGC_240_344,(0,1,10):C.UVGC_240_345,(0,1,11):C.UVGC_240_346,(0,1,12):C.UVGC_240_347,(0,1,13):C.UVGC_240_348,(0,1,14):C.UVGC_240_349,(0,1,15):C.UVGC_240_350,(0,1,16):C.UVGC_240_351,(0,1,17):C.UVGC_240_352,(0,1,18):C.UVGC_240_353,(0,1,19):C.UVGC_240_354,(0,1,20):C.UVGC_240_355,(0,1,21):C.UVGC_240_356,(0,1,22):C.UVGC_240_357,(0,1,23):C.UVGC_240_358,(0,1,24):C.UVGC_240_359,(0,1,25):C.UVGC_240_360,(0,1,26):C.UVGC_240_361,(0,1,27):C.UVGC_240_362,(0,1,28):C.UVGC_240_363,(0,1,29):C.UVGC_240_364,(0,1,30):C.UVGC_240_365,(0,1,31):C.UVGC_240_366,(0,1,32):C.UVGC_240_367,(0,1,5):C.UVGC_507_843,(0,2,0):C.UVGC_240_336,(0,2,1):C.UVGC_240_337,(0,2,2):C.UVGC_240_338,(0,2,3):C.UVGC_240_339,(0,2,4):C.UVGC_240_340,(0,2,6):C.UVGC_240_341,(0,2,7):C.UVGC_240_342,(0,2,8):C.UVGC_240_343,(0,2,9):C.UVGC_240_344,(0,2,10):C.UVGC_240_345,(0,2,11):C.UVGC_240_346,(0,2,12):C.UVGC_240_347,(0,2,13):C.UVGC_240_348,(0,2,14):C.UVGC_240_349,(0,2,15):C.UVGC_240_350,(0,2,16):C.UVGC_240_351,(0,2,17):C.UVGC_240_352,(0,2,18):C.UVGC_240_353,(0,2,19):C.UVGC_240_354,(0,2,20):C.UVGC_240_355,(0,2,21):C.UVGC_240_356,(0,2,22):C.UVGC_240_357,(0,2,23):C.UVGC_240_358,(0,2,24):C.UVGC_240_359,(0,2,25):C.UVGC_240_360,(0,2,26):C.UVGC_240_361,(0,2,27):C.UVGC_240_362,(0,2,28):C.UVGC_240_363,(0,2,29):C.UVGC_240_364,(0,2,30):C.UVGC_240_365,(0,2,31):C.UVGC_240_366,(0,2,32):C.UVGC_240_367,(0,2,5):C.UVGC_508_844})

V_556 = CTVertex(name = 'V_556',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.YF3Qd3, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3Qd3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_244_372,(0,1,0):C.UVGC_240_336,(0,1,1):C.UVGC_240_337,(0,1,2):C.UVGC_240_338,(0,1,3):C.UVGC_240_339,(0,1,4):C.UVGC_240_340,(0,1,6):C.UVGC_240_341,(0,1,7):C.UVGC_240_342,(0,1,8):C.UVGC_240_343,(0,1,9):C.UVGC_240_344,(0,1,10):C.UVGC_240_345,(0,1,11):C.UVGC_240_346,(0,1,12):C.UVGC_240_347,(0,1,13):C.UVGC_240_348,(0,1,14):C.UVGC_240_349,(0,1,15):C.UVGC_240_350,(0,1,16):C.UVGC_240_351,(0,1,17):C.UVGC_240_352,(0,1,18):C.UVGC_240_353,(0,1,19):C.UVGC_240_354,(0,1,20):C.UVGC_240_355,(0,1,21):C.UVGC_240_356,(0,1,22):C.UVGC_240_357,(0,1,23):C.UVGC_240_358,(0,1,24):C.UVGC_240_359,(0,1,25):C.UVGC_240_360,(0,1,26):C.UVGC_240_361,(0,1,27):C.UVGC_240_362,(0,1,28):C.UVGC_240_363,(0,1,29):C.UVGC_240_364,(0,1,30):C.UVGC_240_365,(0,1,31):C.UVGC_240_366,(0,1,32):C.UVGC_240_367,(0,1,5):C.UVGC_516_848,(0,2,0):C.UVGC_240_336,(0,2,1):C.UVGC_240_337,(0,2,2):C.UVGC_240_338,(0,2,3):C.UVGC_240_339,(0,2,4):C.UVGC_240_340,(0,2,6):C.UVGC_240_341,(0,2,7):C.UVGC_240_342,(0,2,8):C.UVGC_240_343,(0,2,9):C.UVGC_240_344,(0,2,10):C.UVGC_240_345,(0,2,11):C.UVGC_240_346,(0,2,12):C.UVGC_240_347,(0,2,13):C.UVGC_240_348,(0,2,14):C.UVGC_240_349,(0,2,15):C.UVGC_240_350,(0,2,16):C.UVGC_240_351,(0,2,17):C.UVGC_240_352,(0,2,18):C.UVGC_240_353,(0,2,19):C.UVGC_240_354,(0,2,20):C.UVGC_240_355,(0,2,21):C.UVGC_240_356,(0,2,22):C.UVGC_240_357,(0,2,23):C.UVGC_240_358,(0,2,24):C.UVGC_240_359,(0,2,25):C.UVGC_240_360,(0,2,26):C.UVGC_240_361,(0,2,27):C.UVGC_240_362,(0,2,28):C.UVGC_240_363,(0,2,29):C.UVGC_240_364,(0,2,30):C.UVGC_240_365,(0,2,31):C.UVGC_240_366,(0,2,32):C.UVGC_240_367,(0,2,5):C.UVGC_517_849})

V_557 = CTVertex(name = 'V_557',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.YF3Qu1, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3Qu1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_244_372,(0,1,0):C.UVGC_240_336,(0,1,1):C.UVGC_240_337,(0,1,2):C.UVGC_240_338,(0,1,3):C.UVGC_240_339,(0,1,4):C.UVGC_240_340,(0,1,6):C.UVGC_240_341,(0,1,7):C.UVGC_240_342,(0,1,8):C.UVGC_240_343,(0,1,9):C.UVGC_240_344,(0,1,10):C.UVGC_240_345,(0,1,11):C.UVGC_240_346,(0,1,12):C.UVGC_240_347,(0,1,13):C.UVGC_240_348,(0,1,14):C.UVGC_240_349,(0,1,15):C.UVGC_240_350,(0,1,16):C.UVGC_240_351,(0,1,17):C.UVGC_240_352,(0,1,18):C.UVGC_240_353,(0,1,19):C.UVGC_240_354,(0,1,20):C.UVGC_240_355,(0,1,21):C.UVGC_240_356,(0,1,22):C.UVGC_240_357,(0,1,23):C.UVGC_240_358,(0,1,24):C.UVGC_240_359,(0,1,25):C.UVGC_240_360,(0,1,26):C.UVGC_240_361,(0,1,27):C.UVGC_240_362,(0,1,28):C.UVGC_240_363,(0,1,29):C.UVGC_240_364,(0,1,30):C.UVGC_240_365,(0,1,31):C.UVGC_240_366,(0,1,32):C.UVGC_240_367,(0,1,5):C.UVGC_525_853,(0,2,0):C.UVGC_240_336,(0,2,1):C.UVGC_240_337,(0,2,2):C.UVGC_240_338,(0,2,3):C.UVGC_240_339,(0,2,4):C.UVGC_240_340,(0,2,6):C.UVGC_240_341,(0,2,7):C.UVGC_240_342,(0,2,8):C.UVGC_240_343,(0,2,9):C.UVGC_240_344,(0,2,10):C.UVGC_240_345,(0,2,11):C.UVGC_240_346,(0,2,12):C.UVGC_240_347,(0,2,13):C.UVGC_240_348,(0,2,14):C.UVGC_240_349,(0,2,15):C.UVGC_240_350,(0,2,16):C.UVGC_240_351,(0,2,17):C.UVGC_240_352,(0,2,18):C.UVGC_240_353,(0,2,19):C.UVGC_240_354,(0,2,20):C.UVGC_240_355,(0,2,21):C.UVGC_240_356,(0,2,22):C.UVGC_240_357,(0,2,23):C.UVGC_240_358,(0,2,24):C.UVGC_240_359,(0,2,25):C.UVGC_240_360,(0,2,26):C.UVGC_240_361,(0,2,27):C.UVGC_240_362,(0,2,28):C.UVGC_240_363,(0,2,29):C.UVGC_240_364,(0,2,30):C.UVGC_240_365,(0,2,31):C.UVGC_240_366,(0,2,32):C.UVGC_240_367,(0,2,5):C.UVGC_526_854})

V_558 = CTVertex(name = 'V_558',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.YF3Qu2, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3Qu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_244_372,(0,1,0):C.UVGC_240_336,(0,1,1):C.UVGC_240_337,(0,1,2):C.UVGC_240_338,(0,1,3):C.UVGC_240_339,(0,1,4):C.UVGC_240_340,(0,1,6):C.UVGC_240_341,(0,1,7):C.UVGC_240_342,(0,1,8):C.UVGC_240_343,(0,1,9):C.UVGC_240_344,(0,1,10):C.UVGC_240_345,(0,1,11):C.UVGC_240_346,(0,1,12):C.UVGC_240_347,(0,1,13):C.UVGC_240_348,(0,1,14):C.UVGC_240_349,(0,1,15):C.UVGC_240_350,(0,1,16):C.UVGC_240_351,(0,1,17):C.UVGC_240_352,(0,1,18):C.UVGC_240_353,(0,1,19):C.UVGC_240_354,(0,1,20):C.UVGC_240_355,(0,1,21):C.UVGC_240_356,(0,1,22):C.UVGC_240_357,(0,1,23):C.UVGC_240_358,(0,1,24):C.UVGC_240_359,(0,1,25):C.UVGC_240_360,(0,1,26):C.UVGC_240_361,(0,1,27):C.UVGC_240_362,(0,1,28):C.UVGC_240_363,(0,1,29):C.UVGC_240_364,(0,1,30):C.UVGC_240_365,(0,1,31):C.UVGC_240_366,(0,1,32):C.UVGC_240_367,(0,1,5):C.UVGC_536_863,(0,2,0):C.UVGC_240_336,(0,2,1):C.UVGC_240_337,(0,2,2):C.UVGC_240_338,(0,2,3):C.UVGC_240_339,(0,2,4):C.UVGC_240_340,(0,2,6):C.UVGC_240_341,(0,2,7):C.UVGC_240_342,(0,2,8):C.UVGC_240_343,(0,2,9):C.UVGC_240_344,(0,2,10):C.UVGC_240_345,(0,2,11):C.UVGC_240_346,(0,2,12):C.UVGC_240_347,(0,2,13):C.UVGC_240_348,(0,2,14):C.UVGC_240_349,(0,2,15):C.UVGC_240_350,(0,2,16):C.UVGC_240_351,(0,2,17):C.UVGC_240_352,(0,2,18):C.UVGC_240_353,(0,2,19):C.UVGC_240_354,(0,2,20):C.UVGC_240_355,(0,2,21):C.UVGC_240_356,(0,2,22):C.UVGC_240_357,(0,2,23):C.UVGC_240_358,(0,2,24):C.UVGC_240_359,(0,2,25):C.UVGC_240_360,(0,2,26):C.UVGC_240_361,(0,2,27):C.UVGC_240_362,(0,2,28):C.UVGC_240_363,(0,2,29):C.UVGC_240_364,(0,2,30):C.UVGC_240_365,(0,2,31):C.UVGC_240_366,(0,2,32):C.UVGC_240_367,(0,2,5):C.UVGC_537_864})

V_559 = CTVertex(name = 'V_559',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.YF3Qu3, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3Qu3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_244_372,(0,1,0):C.UVGC_240_336,(0,1,1):C.UVGC_240_337,(0,1,2):C.UVGC_240_338,(0,1,3):C.UVGC_240_339,(0,1,4):C.UVGC_240_340,(0,1,6):C.UVGC_240_341,(0,1,7):C.UVGC_240_342,(0,1,8):C.UVGC_240_343,(0,1,9):C.UVGC_240_344,(0,1,10):C.UVGC_240_345,(0,1,11):C.UVGC_240_346,(0,1,12):C.UVGC_240_347,(0,1,13):C.UVGC_240_348,(0,1,14):C.UVGC_240_349,(0,1,15):C.UVGC_240_350,(0,1,16):C.UVGC_240_351,(0,1,17):C.UVGC_240_352,(0,1,18):C.UVGC_240_353,(0,1,19):C.UVGC_240_354,(0,1,20):C.UVGC_240_355,(0,1,21):C.UVGC_240_356,(0,1,22):C.UVGC_240_357,(0,1,23):C.UVGC_240_358,(0,1,24):C.UVGC_240_359,(0,1,25):C.UVGC_240_360,(0,1,26):C.UVGC_240_361,(0,1,27):C.UVGC_240_362,(0,1,28):C.UVGC_240_363,(0,1,29):C.UVGC_240_364,(0,1,30):C.UVGC_240_365,(0,1,31):C.UVGC_240_366,(0,1,32):C.UVGC_240_367,(0,1,5):C.UVGC_547_872,(0,2,0):C.UVGC_240_336,(0,2,1):C.UVGC_240_337,(0,2,2):C.UVGC_240_338,(0,2,3):C.UVGC_240_339,(0,2,4):C.UVGC_240_340,(0,2,6):C.UVGC_240_341,(0,2,7):C.UVGC_240_342,(0,2,8):C.UVGC_240_343,(0,2,9):C.UVGC_240_344,(0,2,10):C.UVGC_240_345,(0,2,11):C.UVGC_240_346,(0,2,12):C.UVGC_240_347,(0,2,13):C.UVGC_240_348,(0,2,14):C.UVGC_240_349,(0,2,15):C.UVGC_240_350,(0,2,16):C.UVGC_240_351,(0,2,17):C.UVGC_240_352,(0,2,18):C.UVGC_240_353,(0,2,19):C.UVGC_240_354,(0,2,20):C.UVGC_240_355,(0,2,21):C.UVGC_240_356,(0,2,22):C.UVGC_240_357,(0,2,23):C.UVGC_240_358,(0,2,24):C.UVGC_240_359,(0,2,25):C.UVGC_240_360,(0,2,26):C.UVGC_240_361,(0,2,27):C.UVGC_240_362,(0,2,28):C.UVGC_240_363,(0,2,29):C.UVGC_240_364,(0,2,30):C.UVGC_240_365,(0,2,31):C.UVGC_240_366,(0,2,32):C.UVGC_240_367,(0,2,5):C.UVGC_548_873})

V_560 = CTVertex(name = 'V_560',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.YF3u1, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3u1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_244_372,(0,1,0):C.UVGC_240_336,(0,1,1):C.UVGC_240_337,(0,1,2):C.UVGC_240_338,(0,1,3):C.UVGC_240_339,(0,1,4):C.UVGC_240_340,(0,1,6):C.UVGC_240_341,(0,1,7):C.UVGC_240_342,(0,1,8):C.UVGC_240_343,(0,1,9):C.UVGC_240_344,(0,1,10):C.UVGC_240_345,(0,1,11):C.UVGC_240_346,(0,1,12):C.UVGC_240_347,(0,1,13):C.UVGC_240_348,(0,1,14):C.UVGC_240_349,(0,1,15):C.UVGC_240_350,(0,1,16):C.UVGC_240_351,(0,1,17):C.UVGC_240_352,(0,1,18):C.UVGC_240_353,(0,1,19):C.UVGC_240_354,(0,1,20):C.UVGC_240_355,(0,1,21):C.UVGC_240_356,(0,1,22):C.UVGC_240_357,(0,1,23):C.UVGC_240_358,(0,1,24):C.UVGC_240_359,(0,1,25):C.UVGC_240_360,(0,1,26):C.UVGC_240_361,(0,1,27):C.UVGC_240_362,(0,1,28):C.UVGC_240_363,(0,1,29):C.UVGC_240_364,(0,1,30):C.UVGC_240_365,(0,1,31):C.UVGC_240_366,(0,1,32):C.UVGC_240_367,(0,1,5):C.UVGC_558_881,(0,2,0):C.UVGC_240_336,(0,2,1):C.UVGC_240_337,(0,2,2):C.UVGC_240_338,(0,2,3):C.UVGC_240_339,(0,2,4):C.UVGC_240_340,(0,2,6):C.UVGC_240_341,(0,2,7):C.UVGC_240_342,(0,2,8):C.UVGC_240_343,(0,2,9):C.UVGC_240_344,(0,2,10):C.UVGC_240_345,(0,2,11):C.UVGC_240_346,(0,2,12):C.UVGC_240_347,(0,2,13):C.UVGC_240_348,(0,2,14):C.UVGC_240_349,(0,2,15):C.UVGC_240_350,(0,2,16):C.UVGC_240_351,(0,2,17):C.UVGC_240_352,(0,2,18):C.UVGC_240_353,(0,2,19):C.UVGC_240_354,(0,2,20):C.UVGC_240_355,(0,2,21):C.UVGC_240_356,(0,2,22):C.UVGC_240_357,(0,2,23):C.UVGC_240_358,(0,2,24):C.UVGC_240_359,(0,2,25):C.UVGC_240_360,(0,2,26):C.UVGC_240_361,(0,2,27):C.UVGC_240_362,(0,2,28):C.UVGC_240_363,(0,2,29):C.UVGC_240_364,(0,2,30):C.UVGC_240_365,(0,2,31):C.UVGC_240_366,(0,2,32):C.UVGC_240_367,(0,2,5):C.UVGC_559_882})

V_561 = CTVertex(name = 'V_561',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.YF3u2, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3u2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_244_372,(0,1,0):C.UVGC_240_336,(0,1,1):C.UVGC_240_337,(0,1,2):C.UVGC_240_338,(0,1,3):C.UVGC_240_339,(0,1,4):C.UVGC_240_340,(0,1,6):C.UVGC_240_341,(0,1,7):C.UVGC_240_342,(0,1,8):C.UVGC_240_343,(0,1,9):C.UVGC_240_344,(0,1,10):C.UVGC_240_345,(0,1,11):C.UVGC_240_346,(0,1,12):C.UVGC_240_347,(0,1,13):C.UVGC_240_348,(0,1,14):C.UVGC_240_349,(0,1,15):C.UVGC_240_350,(0,1,16):C.UVGC_240_351,(0,1,17):C.UVGC_240_352,(0,1,18):C.UVGC_240_353,(0,1,19):C.UVGC_240_354,(0,1,20):C.UVGC_240_355,(0,1,21):C.UVGC_240_356,(0,1,22):C.UVGC_240_357,(0,1,23):C.UVGC_240_358,(0,1,24):C.UVGC_240_359,(0,1,25):C.UVGC_240_360,(0,1,26):C.UVGC_240_361,(0,1,27):C.UVGC_240_362,(0,1,28):C.UVGC_240_363,(0,1,29):C.UVGC_240_364,(0,1,30):C.UVGC_240_365,(0,1,31):C.UVGC_240_366,(0,1,32):C.UVGC_240_367,(0,1,5):C.UVGC_565_885,(0,2,0):C.UVGC_240_336,(0,2,1):C.UVGC_240_337,(0,2,2):C.UVGC_240_338,(0,2,3):C.UVGC_240_339,(0,2,4):C.UVGC_240_340,(0,2,6):C.UVGC_240_341,(0,2,7):C.UVGC_240_342,(0,2,8):C.UVGC_240_343,(0,2,9):C.UVGC_240_344,(0,2,10):C.UVGC_240_345,(0,2,11):C.UVGC_240_346,(0,2,12):C.UVGC_240_347,(0,2,13):C.UVGC_240_348,(0,2,14):C.UVGC_240_349,(0,2,15):C.UVGC_240_350,(0,2,16):C.UVGC_240_351,(0,2,17):C.UVGC_240_352,(0,2,18):C.UVGC_240_353,(0,2,19):C.UVGC_240_354,(0,2,20):C.UVGC_240_355,(0,2,21):C.UVGC_240_356,(0,2,22):C.UVGC_240_357,(0,2,23):C.UVGC_240_358,(0,2,24):C.UVGC_240_359,(0,2,25):C.UVGC_240_360,(0,2,26):C.UVGC_240_361,(0,2,27):C.UVGC_240_362,(0,2,28):C.UVGC_240_363,(0,2,29):C.UVGC_240_364,(0,2,30):C.UVGC_240_365,(0,2,31):C.UVGC_240_366,(0,2,32):C.UVGC_240_367,(0,2,5):C.UVGC_566_886})

V_562 = CTVertex(name = 'V_562',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.YF3u3, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3u3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_244_372,(0,1,0):C.UVGC_240_336,(0,1,1):C.UVGC_240_337,(0,1,2):C.UVGC_240_338,(0,1,3):C.UVGC_240_339,(0,1,4):C.UVGC_240_340,(0,1,6):C.UVGC_240_341,(0,1,7):C.UVGC_240_342,(0,1,8):C.UVGC_240_343,(0,1,9):C.UVGC_240_344,(0,1,10):C.UVGC_240_345,(0,1,11):C.UVGC_240_346,(0,1,12):C.UVGC_240_347,(0,1,13):C.UVGC_240_348,(0,1,14):C.UVGC_240_349,(0,1,15):C.UVGC_240_350,(0,1,16):C.UVGC_240_351,(0,1,17):C.UVGC_240_352,(0,1,18):C.UVGC_240_353,(0,1,19):C.UVGC_240_354,(0,1,20):C.UVGC_240_355,(0,1,21):C.UVGC_240_356,(0,1,22):C.UVGC_240_357,(0,1,23):C.UVGC_240_358,(0,1,24):C.UVGC_240_359,(0,1,25):C.UVGC_240_360,(0,1,26):C.UVGC_240_361,(0,1,27):C.UVGC_240_362,(0,1,28):C.UVGC_240_363,(0,1,29):C.UVGC_240_364,(0,1,30):C.UVGC_240_365,(0,1,31):C.UVGC_240_366,(0,1,32):C.UVGC_240_367,(0,1,5):C.UVGC_572_888,(0,2,0):C.UVGC_240_336,(0,2,1):C.UVGC_240_337,(0,2,2):C.UVGC_240_338,(0,2,3):C.UVGC_240_339,(0,2,4):C.UVGC_240_340,(0,2,6):C.UVGC_240_341,(0,2,7):C.UVGC_240_342,(0,2,8):C.UVGC_240_343,(0,2,9):C.UVGC_240_344,(0,2,10):C.UVGC_240_345,(0,2,11):C.UVGC_240_346,(0,2,12):C.UVGC_240_347,(0,2,13):C.UVGC_240_348,(0,2,14):C.UVGC_240_349,(0,2,15):C.UVGC_240_350,(0,2,16):C.UVGC_240_351,(0,2,17):C.UVGC_240_352,(0,2,18):C.UVGC_240_353,(0,2,19):C.UVGC_240_354,(0,2,20):C.UVGC_240_355,(0,2,21):C.UVGC_240_356,(0,2,22):C.UVGC_240_357,(0,2,23):C.UVGC_240_358,(0,2,24):C.UVGC_240_359,(0,2,25):C.UVGC_240_360,(0,2,26):C.UVGC_240_361,(0,2,27):C.UVGC_240_362,(0,2,28):C.UVGC_240_363,(0,2,29):C.UVGC_240_364,(0,2,30):C.UVGC_240_365,(0,2,31):C.UVGC_240_366,(0,2,32):C.UVGC_240_367,(0,2,5):C.UVGC_573_889})

V_563 = CTVertex(name = 'V_563',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.YF3d1, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3d1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_244_372,(0,1,0):C.UVGC_240_336,(0,1,1):C.UVGC_240_337,(0,1,2):C.UVGC_240_338,(0,1,3):C.UVGC_240_339,(0,1,4):C.UVGC_240_340,(0,1,6):C.UVGC_240_341,(0,1,7):C.UVGC_240_342,(0,1,8):C.UVGC_240_343,(0,1,9):C.UVGC_240_344,(0,1,10):C.UVGC_240_345,(0,1,11):C.UVGC_240_346,(0,1,12):C.UVGC_240_347,(0,1,13):C.UVGC_240_348,(0,1,14):C.UVGC_240_349,(0,1,15):C.UVGC_240_350,(0,1,16):C.UVGC_240_351,(0,1,17):C.UVGC_240_352,(0,1,18):C.UVGC_240_353,(0,1,19):C.UVGC_240_354,(0,1,20):C.UVGC_240_355,(0,1,21):C.UVGC_240_356,(0,1,22):C.UVGC_240_357,(0,1,23):C.UVGC_240_358,(0,1,24):C.UVGC_240_359,(0,1,25):C.UVGC_240_360,(0,1,26):C.UVGC_240_361,(0,1,27):C.UVGC_240_362,(0,1,28):C.UVGC_240_363,(0,1,29):C.UVGC_240_364,(0,1,30):C.UVGC_240_365,(0,1,31):C.UVGC_240_366,(0,1,32):C.UVGC_240_367,(0,1,5):C.UVGC_477_827,(0,2,0):C.UVGC_240_336,(0,2,1):C.UVGC_240_337,(0,2,2):C.UVGC_240_338,(0,2,3):C.UVGC_240_339,(0,2,4):C.UVGC_240_340,(0,2,6):C.UVGC_240_341,(0,2,7):C.UVGC_240_342,(0,2,8):C.UVGC_240_343,(0,2,9):C.UVGC_240_344,(0,2,10):C.UVGC_240_345,(0,2,11):C.UVGC_240_346,(0,2,12):C.UVGC_240_347,(0,2,13):C.UVGC_240_348,(0,2,14):C.UVGC_240_349,(0,2,15):C.UVGC_240_350,(0,2,16):C.UVGC_240_351,(0,2,17):C.UVGC_240_352,(0,2,18):C.UVGC_240_353,(0,2,19):C.UVGC_240_354,(0,2,20):C.UVGC_240_355,(0,2,21):C.UVGC_240_356,(0,2,22):C.UVGC_240_357,(0,2,23):C.UVGC_240_358,(0,2,24):C.UVGC_240_359,(0,2,25):C.UVGC_240_360,(0,2,26):C.UVGC_240_361,(0,2,27):C.UVGC_240_362,(0,2,28):C.UVGC_240_363,(0,2,29):C.UVGC_240_364,(0,2,30):C.UVGC_240_365,(0,2,31):C.UVGC_240_366,(0,2,32):C.UVGC_240_367,(0,2,5):C.UVGC_478_828})

V_564 = CTVertex(name = 'V_564',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.YF3d2, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3d2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_244_372,(0,1,0):C.UVGC_240_336,(0,1,1):C.UVGC_240_337,(0,1,2):C.UVGC_240_338,(0,1,3):C.UVGC_240_339,(0,1,4):C.UVGC_240_340,(0,1,6):C.UVGC_240_341,(0,1,7):C.UVGC_240_342,(0,1,8):C.UVGC_240_343,(0,1,9):C.UVGC_240_344,(0,1,10):C.UVGC_240_345,(0,1,11):C.UVGC_240_346,(0,1,12):C.UVGC_240_347,(0,1,13):C.UVGC_240_348,(0,1,14):C.UVGC_240_349,(0,1,15):C.UVGC_240_350,(0,1,16):C.UVGC_240_351,(0,1,17):C.UVGC_240_352,(0,1,18):C.UVGC_240_353,(0,1,19):C.UVGC_240_354,(0,1,20):C.UVGC_240_355,(0,1,21):C.UVGC_240_356,(0,1,22):C.UVGC_240_357,(0,1,23):C.UVGC_240_358,(0,1,24):C.UVGC_240_359,(0,1,25):C.UVGC_240_360,(0,1,26):C.UVGC_240_361,(0,1,27):C.UVGC_240_362,(0,1,28):C.UVGC_240_363,(0,1,29):C.UVGC_240_364,(0,1,30):C.UVGC_240_365,(0,1,31):C.UVGC_240_366,(0,1,32):C.UVGC_240_367,(0,1,5):C.UVGC_484_831,(0,2,0):C.UVGC_240_336,(0,2,1):C.UVGC_240_337,(0,2,2):C.UVGC_240_338,(0,2,3):C.UVGC_240_339,(0,2,4):C.UVGC_240_340,(0,2,6):C.UVGC_240_341,(0,2,7):C.UVGC_240_342,(0,2,8):C.UVGC_240_343,(0,2,9):C.UVGC_240_344,(0,2,10):C.UVGC_240_345,(0,2,11):C.UVGC_240_346,(0,2,12):C.UVGC_240_347,(0,2,13):C.UVGC_240_348,(0,2,14):C.UVGC_240_349,(0,2,15):C.UVGC_240_350,(0,2,16):C.UVGC_240_351,(0,2,17):C.UVGC_240_352,(0,2,18):C.UVGC_240_353,(0,2,19):C.UVGC_240_354,(0,2,20):C.UVGC_240_355,(0,2,21):C.UVGC_240_356,(0,2,22):C.UVGC_240_357,(0,2,23):C.UVGC_240_358,(0,2,24):C.UVGC_240_359,(0,2,25):C.UVGC_240_360,(0,2,26):C.UVGC_240_361,(0,2,27):C.UVGC_240_362,(0,2,28):C.UVGC_240_363,(0,2,29):C.UVGC_240_364,(0,2,30):C.UVGC_240_365,(0,2,31):C.UVGC_240_366,(0,2,32):C.UVGC_240_367,(0,2,5):C.UVGC_485_832})

V_565 = CTVertex(name = 'V_565',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.YF3d3, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3d3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_244_372,(0,1,0):C.UVGC_240_336,(0,1,1):C.UVGC_240_337,(0,1,2):C.UVGC_240_338,(0,1,3):C.UVGC_240_339,(0,1,4):C.UVGC_240_340,(0,1,6):C.UVGC_240_341,(0,1,7):C.UVGC_240_342,(0,1,8):C.UVGC_240_343,(0,1,9):C.UVGC_240_344,(0,1,10):C.UVGC_240_345,(0,1,11):C.UVGC_240_346,(0,1,12):C.UVGC_240_347,(0,1,13):C.UVGC_240_348,(0,1,14):C.UVGC_240_349,(0,1,15):C.UVGC_240_350,(0,1,16):C.UVGC_240_351,(0,1,17):C.UVGC_240_352,(0,1,18):C.UVGC_240_353,(0,1,19):C.UVGC_240_354,(0,1,20):C.UVGC_240_355,(0,1,21):C.UVGC_240_356,(0,1,22):C.UVGC_240_357,(0,1,23):C.UVGC_240_358,(0,1,24):C.UVGC_240_359,(0,1,25):C.UVGC_240_360,(0,1,26):C.UVGC_240_361,(0,1,27):C.UVGC_240_362,(0,1,28):C.UVGC_240_363,(0,1,29):C.UVGC_240_364,(0,1,30):C.UVGC_240_365,(0,1,31):C.UVGC_240_366,(0,1,32):C.UVGC_240_367,(0,1,5):C.UVGC_491_834,(0,2,0):C.UVGC_240_336,(0,2,1):C.UVGC_240_337,(0,2,2):C.UVGC_240_338,(0,2,3):C.UVGC_240_339,(0,2,4):C.UVGC_240_340,(0,2,6):C.UVGC_240_341,(0,2,7):C.UVGC_240_342,(0,2,8):C.UVGC_240_343,(0,2,9):C.UVGC_240_344,(0,2,10):C.UVGC_240_345,(0,2,11):C.UVGC_240_346,(0,2,12):C.UVGC_240_347,(0,2,13):C.UVGC_240_348,(0,2,14):C.UVGC_240_349,(0,2,15):C.UVGC_240_350,(0,2,16):C.UVGC_240_351,(0,2,17):C.UVGC_240_352,(0,2,18):C.UVGC_240_353,(0,2,19):C.UVGC_240_354,(0,2,20):C.UVGC_240_355,(0,2,21):C.UVGC_240_356,(0,2,22):C.UVGC_240_357,(0,2,23):C.UVGC_240_358,(0,2,24):C.UVGC_240_359,(0,2,25):C.UVGC_240_360,(0,2,26):C.UVGC_240_361,(0,2,27):C.UVGC_240_362,(0,2,28):C.UVGC_240_363,(0,2,29):C.UVGC_240_364,(0,2,30):C.UVGC_240_365,(0,2,31):C.UVGC_240_366,(0,2,32):C.UVGC_240_367,(0,2,5):C.UVGC_492_835})

V_566 = CTVertex(name = 'V_566',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.YF3Qu1, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,1):C.UVGC_587_915,(0,1,0):C.UVGC_531_856,(0,1,2):C.UVGC_531_857,(0,2,0):C.UVGC_532_858,(0,2,2):C.UVGC_532_859})

V_567 = CTVertex(name = 'V_567',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.YF3Qu2, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd2] ], [ [P.g, P.YF3Qd2, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,1):C.UVGC_587_915,(0,1,0):C.UVGC_542_866,(0,1,2):C.UVGC_542_867,(0,2,0):C.UVGC_543_868,(0,2,2):C.UVGC_543_869})

V_568 = CTVertex(name = 'V_568',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.YF3Qu3, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,1):C.UVGC_587_915,(0,1,0):C.UVGC_553_875,(0,1,2):C.UVGC_553_876,(0,2,0):C.UVGC_554_877,(0,2,2):C.UVGC_554_878})

V_569 = CTVertex(name = 'V_569',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.YF3Qd1, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,1):C.UVGC_587_915,(0,1,0):C.UVGC_531_856,(0,1,2):C.UVGC_531_857,(0,2,0):C.UVGC_532_858,(0,2,2):C.UVGC_532_859})

V_570 = CTVertex(name = 'V_570',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.YF3Qd2, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd2] ], [ [P.g, P.YF3Qd2, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,1):C.UVGC_587_915,(0,1,0):C.UVGC_542_866,(0,1,2):C.UVGC_542_867,(0,2,0):C.UVGC_543_868,(0,2,2):C.UVGC_543_869})

V_571 = CTVertex(name = 'V_571',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.YF3Qd3, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,1):C.UVGC_587_915,(0,1,0):C.UVGC_553_875,(0,1,2):C.UVGC_553_876,(0,2,0):C.UVGC_554_877,(0,2,2):C.UVGC_554_878})

V_572 = CTVertex(name = 'V_572',
                 type = 'UV',
                 particles = [ P.a, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_263_386,(0,1,0):C.UVGC_262_385})

V_573 = CTVertex(name = 'V_573',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.d, P.YS3d1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YS3d1] ], [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_592_926,(0,0,2):C.UVGC_592_927,(0,0,1):C.UVGC_592_928})

V_574 = CTVertex(name = 'V_574',
                 type = 'UV',
                 particles = [ P.Xm, P.d, P.YS3d1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YS3d1] ], [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_592_926,(0,0,2):C.UVGC_592_927,(0,0,1):C.UVGC_592_928})

V_575 = CTVertex(name = 'V_575',
                 type = 'UV',
                 particles = [ P.g, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_266_389,(0,0,1):C.UVGC_266_390,(0,0,2):C.UVGC_266_391,(0,0,3):C.UVGC_266_392,(0,0,4):C.UVGC_266_393,(0,0,6):C.UVGC_266_394,(0,0,7):C.UVGC_266_395,(0,0,8):C.UVGC_266_396,(0,0,9):C.UVGC_266_397,(0,0,10):C.UVGC_266_398,(0,0,11):C.UVGC_266_399,(0,0,12):C.UVGC_266_400,(0,0,13):C.UVGC_266_401,(0,0,14):C.UVGC_266_402,(0,0,15):C.UVGC_266_403,(0,0,16):C.UVGC_266_404,(0,0,17):C.UVGC_266_405,(0,0,18):C.UVGC_266_406,(0,0,19):C.UVGC_266_407,(0,0,20):C.UVGC_266_408,(0,0,21):C.UVGC_266_409,(0,0,22):C.UVGC_266_410,(0,0,23):C.UVGC_266_411,(0,0,24):C.UVGC_266_412,(0,0,25):C.UVGC_266_413,(0,0,26):C.UVGC_266_414,(0,0,27):C.UVGC_266_415,(0,0,28):C.UVGC_266_416,(0,0,29):C.UVGC_266_417,(0,0,30):C.UVGC_266_418,(0,0,31):C.UVGC_266_419,(0,0,32):C.UVGC_266_420,(0,0,5):C.UVGC_266_421,(0,1,0):C.UVGC_240_336,(0,1,1):C.UVGC_240_337,(0,1,2):C.UVGC_240_338,(0,1,3):C.UVGC_240_339,(0,1,4):C.UVGC_240_340,(0,1,6):C.UVGC_240_341,(0,1,7):C.UVGC_240_342,(0,1,8):C.UVGC_240_343,(0,1,9):C.UVGC_240_344,(0,1,10):C.UVGC_240_345,(0,1,11):C.UVGC_240_346,(0,1,12):C.UVGC_240_347,(0,1,13):C.UVGC_240_348,(0,1,14):C.UVGC_240_349,(0,1,15):C.UVGC_240_350,(0,1,16):C.UVGC_240_351,(0,1,17):C.UVGC_240_352,(0,1,18):C.UVGC_240_353,(0,1,19):C.UVGC_240_354,(0,1,20):C.UVGC_240_355,(0,1,21):C.UVGC_240_356,(0,1,22):C.UVGC_240_357,(0,1,23):C.UVGC_240_358,(0,1,24):C.UVGC_240_359,(0,1,25):C.UVGC_240_360,(0,1,26):C.UVGC_240_361,(0,1,27):C.UVGC_240_362,(0,1,28):C.UVGC_240_363,(0,1,29):C.UVGC_240_364,(0,1,30):C.UVGC_240_365,(0,1,31):C.UVGC_240_366,(0,1,32):C.UVGC_240_367,(0,1,5):C.UVGC_265_388})

V_576 = CTVertex(name = 'V_576',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.Xd, P.YS3d1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YS3d1] ], [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_592_926,(0,0,2):C.UVGC_592_927,(0,0,1):C.UVGC_592_928})

V_577 = CTVertex(name = 'V_577',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.Xm, P.YS3d1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YS3d1] ], [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_592_926,(0,0,2):C.UVGC_592_927,(0,0,1):C.UVGC_592_928})

V_578 = CTVertex(name = 'V_578',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_264_387})

V_579 = CTVertex(name = 'V_579',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_267_422,(0,0,1):C.UVGC_267_423,(0,0,2):C.UVGC_267_424,(0,0,3):C.UVGC_267_425,(0,0,4):C.UVGC_267_426,(0,0,6):C.UVGC_267_427,(0,0,7):C.UVGC_267_428,(0,0,8):C.UVGC_267_429,(0,0,9):C.UVGC_267_430,(0,0,10):C.UVGC_267_431,(0,0,11):C.UVGC_267_432,(0,0,12):C.UVGC_267_433,(0,0,13):C.UVGC_267_434,(0,0,14):C.UVGC_267_435,(0,0,15):C.UVGC_267_436,(0,0,16):C.UVGC_267_437,(0,0,17):C.UVGC_267_438,(0,0,18):C.UVGC_267_439,(0,0,19):C.UVGC_267_440,(0,0,20):C.UVGC_267_441,(0,0,21):C.UVGC_267_442,(0,0,22):C.UVGC_267_443,(0,0,23):C.UVGC_267_444,(0,0,24):C.UVGC_267_445,(0,0,25):C.UVGC_267_446,(0,0,26):C.UVGC_267_447,(0,0,27):C.UVGC_267_448,(0,0,28):C.UVGC_267_449,(0,0,29):C.UVGC_267_450,(0,0,30):C.UVGC_267_451,(0,0,31):C.UVGC_267_452,(0,0,32):C.UVGC_267_453,(0,0,5):C.UVGC_267_454})

V_580 = CTVertex(name = 'V_580',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_270_459,(2,0,1):C.UVGC_270_460,(2,0,2):C.UVGC_270_461,(2,0,3):C.UVGC_270_462,(2,0,4):C.UVGC_270_463,(2,0,6):C.UVGC_270_464,(2,0,7):C.UVGC_270_465,(2,0,8):C.UVGC_270_466,(2,0,9):C.UVGC_270_467,(2,0,10):C.UVGC_270_468,(2,0,11):C.UVGC_270_469,(2,0,12):C.UVGC_270_470,(2,0,13):C.UVGC_270_471,(2,0,14):C.UVGC_270_472,(2,0,15):C.UVGC_270_473,(2,0,16):C.UVGC_270_474,(2,0,17):C.UVGC_270_475,(2,0,18):C.UVGC_270_476,(2,0,19):C.UVGC_270_477,(2,0,20):C.UVGC_270_478,(2,0,21):C.UVGC_270_479,(2,0,22):C.UVGC_270_480,(2,0,23):C.UVGC_270_481,(2,0,24):C.UVGC_270_482,(2,0,25):C.UVGC_270_483,(2,0,26):C.UVGC_270_484,(2,0,27):C.UVGC_270_485,(2,0,28):C.UVGC_270_486,(2,0,29):C.UVGC_270_487,(2,0,30):C.UVGC_270_488,(2,0,31):C.UVGC_270_489,(2,0,32):C.UVGC_270_490,(2,0,5):C.UVGC_270_491,(1,0,0):C.UVGC_270_459,(1,0,1):C.UVGC_270_460,(1,0,2):C.UVGC_270_461,(1,0,3):C.UVGC_270_462,(1,0,4):C.UVGC_270_463,(1,0,6):C.UVGC_270_464,(1,0,7):C.UVGC_270_465,(1,0,8):C.UVGC_270_466,(1,0,9):C.UVGC_270_467,(1,0,10):C.UVGC_270_468,(1,0,11):C.UVGC_270_469,(1,0,12):C.UVGC_270_470,(1,0,13):C.UVGC_270_471,(1,0,14):C.UVGC_270_472,(1,0,15):C.UVGC_270_473,(1,0,16):C.UVGC_270_474,(1,0,17):C.UVGC_270_475,(1,0,18):C.UVGC_270_476,(1,0,19):C.UVGC_270_477,(1,0,20):C.UVGC_270_478,(1,0,21):C.UVGC_270_479,(1,0,22):C.UVGC_270_480,(1,0,23):C.UVGC_270_481,(1,0,24):C.UVGC_270_482,(1,0,25):C.UVGC_270_483,(1,0,26):C.UVGC_270_484,(1,0,27):C.UVGC_270_485,(1,0,28):C.UVGC_270_486,(1,0,29):C.UVGC_270_487,(1,0,30):C.UVGC_270_488,(1,0,31):C.UVGC_270_489,(1,0,32):C.UVGC_270_490,(1,0,5):C.UVGC_270_491,(0,0,3):C.UVGC_269_457,(0,0,5):C.UVGC_269_458})

V_581 = CTVertex(name = 'V_581',
                 type = 'UV',
                 particles = [ P.a, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_279_532,(0,1,0):C.UVGC_278_531})

V_582 = CTVertex(name = 'V_582',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.s, P.YS3d2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YS3d2] ], [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_757_1034,(0,0,2):C.UVGC_757_1035,(0,0,1):C.UVGC_757_1036})

V_583 = CTVertex(name = 'V_583',
                 type = 'UV',
                 particles = [ P.Xm, P.s, P.YS3d2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YS3d2] ], [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_757_1034,(0,0,2):C.UVGC_757_1035,(0,0,1):C.UVGC_757_1036})

V_584 = CTVertex(name = 'V_584',
                 type = 'UV',
                 particles = [ P.g, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_266_389,(0,0,1):C.UVGC_266_390,(0,0,2):C.UVGC_266_391,(0,0,3):C.UVGC_266_392,(0,0,4):C.UVGC_266_393,(0,0,6):C.UVGC_266_394,(0,0,7):C.UVGC_266_395,(0,0,8):C.UVGC_266_396,(0,0,9):C.UVGC_266_397,(0,0,10):C.UVGC_266_398,(0,0,11):C.UVGC_266_399,(0,0,12):C.UVGC_266_400,(0,0,13):C.UVGC_266_401,(0,0,14):C.UVGC_266_402,(0,0,15):C.UVGC_266_403,(0,0,16):C.UVGC_266_404,(0,0,17):C.UVGC_266_405,(0,0,18):C.UVGC_266_406,(0,0,19):C.UVGC_266_407,(0,0,20):C.UVGC_266_408,(0,0,21):C.UVGC_266_409,(0,0,22):C.UVGC_266_410,(0,0,23):C.UVGC_266_411,(0,0,24):C.UVGC_266_412,(0,0,25):C.UVGC_266_413,(0,0,26):C.UVGC_266_414,(0,0,27):C.UVGC_266_415,(0,0,28):C.UVGC_266_416,(0,0,29):C.UVGC_266_417,(0,0,30):C.UVGC_266_418,(0,0,31):C.UVGC_266_419,(0,0,32):C.UVGC_266_420,(0,0,5):C.UVGC_282_535,(0,1,0):C.UVGC_240_336,(0,1,1):C.UVGC_240_337,(0,1,2):C.UVGC_240_338,(0,1,3):C.UVGC_240_339,(0,1,4):C.UVGC_240_340,(0,1,6):C.UVGC_240_341,(0,1,7):C.UVGC_240_342,(0,1,8):C.UVGC_240_343,(0,1,9):C.UVGC_240_344,(0,1,10):C.UVGC_240_345,(0,1,11):C.UVGC_240_346,(0,1,12):C.UVGC_240_347,(0,1,13):C.UVGC_240_348,(0,1,14):C.UVGC_240_349,(0,1,15):C.UVGC_240_350,(0,1,16):C.UVGC_240_351,(0,1,17):C.UVGC_240_352,(0,1,18):C.UVGC_240_353,(0,1,19):C.UVGC_240_354,(0,1,20):C.UVGC_240_355,(0,1,21):C.UVGC_240_356,(0,1,22):C.UVGC_240_357,(0,1,23):C.UVGC_240_358,(0,1,24):C.UVGC_240_359,(0,1,25):C.UVGC_240_360,(0,1,26):C.UVGC_240_361,(0,1,27):C.UVGC_240_362,(0,1,28):C.UVGC_240_363,(0,1,29):C.UVGC_240_364,(0,1,30):C.UVGC_240_365,(0,1,31):C.UVGC_240_366,(0,1,32):C.UVGC_240_367,(0,1,5):C.UVGC_281_534})

V_585 = CTVertex(name = 'V_585',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.Xd, P.YS3d2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YS3d2] ], [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_757_1034,(0,0,2):C.UVGC_757_1035,(0,0,1):C.UVGC_757_1036})

V_586 = CTVertex(name = 'V_586',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.Xm, P.YS3d2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YS3d2] ], [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_757_1034,(0,0,2):C.UVGC_757_1035,(0,0,1):C.UVGC_757_1036})

V_587 = CTVertex(name = 'V_587',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_280_533})

V_588 = CTVertex(name = 'V_588',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_267_422,(0,0,1):C.UVGC_267_423,(0,0,2):C.UVGC_267_424,(0,0,3):C.UVGC_267_425,(0,0,4):C.UVGC_267_426,(0,0,6):C.UVGC_267_427,(0,0,7):C.UVGC_267_428,(0,0,8):C.UVGC_267_429,(0,0,9):C.UVGC_267_430,(0,0,10):C.UVGC_267_431,(0,0,11):C.UVGC_267_432,(0,0,12):C.UVGC_267_433,(0,0,13):C.UVGC_267_434,(0,0,14):C.UVGC_267_435,(0,0,15):C.UVGC_267_436,(0,0,16):C.UVGC_267_437,(0,0,17):C.UVGC_267_438,(0,0,18):C.UVGC_267_439,(0,0,19):C.UVGC_267_440,(0,0,20):C.UVGC_267_441,(0,0,21):C.UVGC_267_442,(0,0,22):C.UVGC_267_443,(0,0,23):C.UVGC_267_444,(0,0,24):C.UVGC_267_445,(0,0,25):C.UVGC_267_446,(0,0,26):C.UVGC_267_447,(0,0,27):C.UVGC_267_448,(0,0,28):C.UVGC_267_449,(0,0,29):C.UVGC_267_450,(0,0,30):C.UVGC_267_451,(0,0,31):C.UVGC_267_452,(0,0,32):C.UVGC_267_453,(0,0,5):C.UVGC_283_536})

V_589 = CTVertex(name = 'V_589',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_270_459,(2,0,1):C.UVGC_270_460,(2,0,2):C.UVGC_270_461,(2,0,3):C.UVGC_270_462,(2,0,4):C.UVGC_270_463,(2,0,6):C.UVGC_270_464,(2,0,7):C.UVGC_270_465,(2,0,8):C.UVGC_270_466,(2,0,9):C.UVGC_270_467,(2,0,10):C.UVGC_270_468,(2,0,11):C.UVGC_270_469,(2,0,12):C.UVGC_270_470,(2,0,13):C.UVGC_270_471,(2,0,14):C.UVGC_270_472,(2,0,15):C.UVGC_270_473,(2,0,16):C.UVGC_270_474,(2,0,17):C.UVGC_270_475,(2,0,18):C.UVGC_270_476,(2,0,19):C.UVGC_270_477,(2,0,20):C.UVGC_270_478,(2,0,21):C.UVGC_270_479,(2,0,22):C.UVGC_270_480,(2,0,23):C.UVGC_270_481,(2,0,24):C.UVGC_270_482,(2,0,25):C.UVGC_270_483,(2,0,26):C.UVGC_270_484,(2,0,27):C.UVGC_270_485,(2,0,28):C.UVGC_270_486,(2,0,29):C.UVGC_270_487,(2,0,30):C.UVGC_270_488,(2,0,31):C.UVGC_270_489,(2,0,32):C.UVGC_270_490,(2,0,5):C.UVGC_286_537,(1,0,0):C.UVGC_270_459,(1,0,1):C.UVGC_270_460,(1,0,2):C.UVGC_270_461,(1,0,3):C.UVGC_270_462,(1,0,4):C.UVGC_270_463,(1,0,6):C.UVGC_270_464,(1,0,7):C.UVGC_270_465,(1,0,8):C.UVGC_270_466,(1,0,9):C.UVGC_270_467,(1,0,10):C.UVGC_270_468,(1,0,11):C.UVGC_270_469,(1,0,12):C.UVGC_270_470,(1,0,13):C.UVGC_270_471,(1,0,14):C.UVGC_270_472,(1,0,15):C.UVGC_270_473,(1,0,16):C.UVGC_270_474,(1,0,17):C.UVGC_270_475,(1,0,18):C.UVGC_270_476,(1,0,19):C.UVGC_270_477,(1,0,20):C.UVGC_270_478,(1,0,21):C.UVGC_270_479,(1,0,22):C.UVGC_270_480,(1,0,23):C.UVGC_270_481,(1,0,24):C.UVGC_270_482,(1,0,25):C.UVGC_270_483,(1,0,26):C.UVGC_270_484,(1,0,27):C.UVGC_270_485,(1,0,28):C.UVGC_270_486,(1,0,29):C.UVGC_270_487,(1,0,30):C.UVGC_270_488,(1,0,31):C.UVGC_270_489,(1,0,32):C.UVGC_270_490,(1,0,5):C.UVGC_286_537,(0,0,3):C.UVGC_269_457,(0,0,5):C.UVGC_269_458})

V_590 = CTVertex(name = 'V_590',
                 type = 'UV',
                 particles = [ P.a, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_295_546,(0,1,0):C.UVGC_294_545})

V_591 = CTVertex(name = 'V_591',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.b, P.YS3d3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YS3d3] ], [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_579_891,(0,0,2):C.UVGC_579_892,(0,0,1):C.UVGC_579_893})

V_592 = CTVertex(name = 'V_592',
                 type = 'UV',
                 particles = [ P.Xm, P.b, P.YS3d3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YS3d3] ], [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_579_891,(0,0,2):C.UVGC_579_892,(0,0,1):C.UVGC_579_893})

V_593 = CTVertex(name = 'V_593',
                 type = 'UV',
                 particles = [ P.g, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_266_389,(0,0,1):C.UVGC_266_390,(0,0,2):C.UVGC_266_391,(0,0,3):C.UVGC_266_392,(0,0,4):C.UVGC_266_393,(0,0,6):C.UVGC_266_394,(0,0,7):C.UVGC_266_395,(0,0,8):C.UVGC_266_396,(0,0,9):C.UVGC_266_397,(0,0,10):C.UVGC_266_398,(0,0,11):C.UVGC_266_399,(0,0,12):C.UVGC_266_400,(0,0,13):C.UVGC_266_401,(0,0,14):C.UVGC_266_402,(0,0,15):C.UVGC_266_403,(0,0,16):C.UVGC_266_404,(0,0,17):C.UVGC_266_405,(0,0,18):C.UVGC_266_406,(0,0,19):C.UVGC_266_407,(0,0,20):C.UVGC_266_408,(0,0,21):C.UVGC_266_409,(0,0,22):C.UVGC_266_410,(0,0,23):C.UVGC_266_411,(0,0,24):C.UVGC_266_412,(0,0,25):C.UVGC_266_413,(0,0,26):C.UVGC_266_414,(0,0,27):C.UVGC_266_415,(0,0,28):C.UVGC_266_416,(0,0,29):C.UVGC_266_417,(0,0,30):C.UVGC_266_418,(0,0,31):C.UVGC_266_419,(0,0,32):C.UVGC_266_420,(0,0,5):C.UVGC_298_549,(0,1,0):C.UVGC_240_336,(0,1,1):C.UVGC_240_337,(0,1,2):C.UVGC_240_338,(0,1,3):C.UVGC_240_339,(0,1,4):C.UVGC_240_340,(0,1,6):C.UVGC_240_341,(0,1,7):C.UVGC_240_342,(0,1,8):C.UVGC_240_343,(0,1,9):C.UVGC_240_344,(0,1,10):C.UVGC_240_345,(0,1,11):C.UVGC_240_346,(0,1,12):C.UVGC_240_347,(0,1,13):C.UVGC_240_348,(0,1,14):C.UVGC_240_349,(0,1,15):C.UVGC_240_350,(0,1,16):C.UVGC_240_351,(0,1,17):C.UVGC_240_352,(0,1,18):C.UVGC_240_353,(0,1,19):C.UVGC_240_354,(0,1,20):C.UVGC_240_355,(0,1,21):C.UVGC_240_356,(0,1,22):C.UVGC_240_357,(0,1,23):C.UVGC_240_358,(0,1,24):C.UVGC_240_359,(0,1,25):C.UVGC_240_360,(0,1,26):C.UVGC_240_361,(0,1,27):C.UVGC_240_362,(0,1,28):C.UVGC_240_363,(0,1,29):C.UVGC_240_364,(0,1,30):C.UVGC_240_365,(0,1,31):C.UVGC_240_366,(0,1,32):C.UVGC_240_367,(0,1,5):C.UVGC_297_548})

V_594 = CTVertex(name = 'V_594',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.Xd, P.YS3d3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YS3d3] ], [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_579_891,(0,0,2):C.UVGC_579_892,(0,0,1):C.UVGC_579_893})

V_595 = CTVertex(name = 'V_595',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.Xm, P.YS3d3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YS3d3] ], [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_579_891,(0,0,2):C.UVGC_579_892,(0,0,1):C.UVGC_579_893})

V_596 = CTVertex(name = 'V_596',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_296_547})

V_597 = CTVertex(name = 'V_597',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_267_422,(0,0,1):C.UVGC_267_423,(0,0,2):C.UVGC_267_424,(0,0,3):C.UVGC_267_425,(0,0,4):C.UVGC_267_426,(0,0,6):C.UVGC_267_427,(0,0,7):C.UVGC_267_428,(0,0,8):C.UVGC_267_429,(0,0,9):C.UVGC_267_430,(0,0,10):C.UVGC_267_431,(0,0,11):C.UVGC_267_432,(0,0,12):C.UVGC_267_433,(0,0,13):C.UVGC_267_434,(0,0,14):C.UVGC_267_435,(0,0,15):C.UVGC_267_436,(0,0,16):C.UVGC_267_437,(0,0,17):C.UVGC_267_438,(0,0,18):C.UVGC_267_439,(0,0,19):C.UVGC_267_440,(0,0,20):C.UVGC_267_441,(0,0,21):C.UVGC_267_442,(0,0,22):C.UVGC_267_443,(0,0,23):C.UVGC_267_444,(0,0,24):C.UVGC_267_445,(0,0,25):C.UVGC_267_446,(0,0,26):C.UVGC_267_447,(0,0,27):C.UVGC_267_448,(0,0,28):C.UVGC_267_449,(0,0,29):C.UVGC_267_450,(0,0,30):C.UVGC_267_451,(0,0,31):C.UVGC_267_452,(0,0,32):C.UVGC_267_453,(0,0,5):C.UVGC_299_550})

V_598 = CTVertex(name = 'V_598',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_270_459,(2,0,1):C.UVGC_270_460,(2,0,2):C.UVGC_270_461,(2,0,3):C.UVGC_270_462,(2,0,4):C.UVGC_270_463,(2,0,6):C.UVGC_270_464,(2,0,7):C.UVGC_270_465,(2,0,8):C.UVGC_270_466,(2,0,9):C.UVGC_270_467,(2,0,10):C.UVGC_270_468,(2,0,11):C.UVGC_270_469,(2,0,12):C.UVGC_270_470,(2,0,13):C.UVGC_270_471,(2,0,14):C.UVGC_270_472,(2,0,15):C.UVGC_270_473,(2,0,16):C.UVGC_270_474,(2,0,17):C.UVGC_270_475,(2,0,18):C.UVGC_270_476,(2,0,19):C.UVGC_270_477,(2,0,20):C.UVGC_270_478,(2,0,21):C.UVGC_270_479,(2,0,22):C.UVGC_270_480,(2,0,23):C.UVGC_270_481,(2,0,24):C.UVGC_270_482,(2,0,25):C.UVGC_270_483,(2,0,26):C.UVGC_270_484,(2,0,27):C.UVGC_270_485,(2,0,28):C.UVGC_270_486,(2,0,29):C.UVGC_270_487,(2,0,30):C.UVGC_270_488,(2,0,31):C.UVGC_270_489,(2,0,32):C.UVGC_270_490,(2,0,5):C.UVGC_302_551,(1,0,0):C.UVGC_270_459,(1,0,1):C.UVGC_270_460,(1,0,2):C.UVGC_270_461,(1,0,3):C.UVGC_270_462,(1,0,4):C.UVGC_270_463,(1,0,6):C.UVGC_270_464,(1,0,7):C.UVGC_270_465,(1,0,8):C.UVGC_270_466,(1,0,9):C.UVGC_270_467,(1,0,10):C.UVGC_270_468,(1,0,11):C.UVGC_270_469,(1,0,12):C.UVGC_270_470,(1,0,13):C.UVGC_270_471,(1,0,14):C.UVGC_270_472,(1,0,15):C.UVGC_270_473,(1,0,16):C.UVGC_270_474,(1,0,17):C.UVGC_270_475,(1,0,18):C.UVGC_270_476,(1,0,19):C.UVGC_270_477,(1,0,20):C.UVGC_270_478,(1,0,21):C.UVGC_270_479,(1,0,22):C.UVGC_270_480,(1,0,23):C.UVGC_270_481,(1,0,24):C.UVGC_270_482,(1,0,25):C.UVGC_270_483,(1,0,26):C.UVGC_270_484,(1,0,27):C.UVGC_270_485,(1,0,28):C.UVGC_270_486,(1,0,29):C.UVGC_270_487,(1,0,30):C.UVGC_270_488,(1,0,31):C.UVGC_270_489,(1,0,32):C.UVGC_270_490,(1,0,5):C.UVGC_302_551,(0,0,3):C.UVGC_269_457,(0,0,5):C.UVGC_269_458})

V_599 = CTVertex(name = 'V_599',
                 type = 'UV',
                 particles = [ P.a, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_311_560,(0,1,0):C.UVGC_310_559})

V_600 = CTVertex(name = 'V_600',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.d, P.YS3Qd1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_593_929,(0,0,2):C.UVGC_593_930,(0,0,1):C.UVGC_593_931})

V_601 = CTVertex(name = 'V_601',
                 type = 'UV',
                 particles = [ P.Xm, P.d, P.YS3Qd1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_593_929,(0,0,2):C.UVGC_593_930,(0,0,1):C.UVGC_593_931})

V_602 = CTVertex(name = 'V_602',
                 type = 'UV',
                 particles = [ P.W__minus__, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_659_959,(0,0,2):C.UVGC_659_960,(0,0,1):C.UVGC_659_961,(0,1,0):C.UVGC_658_957,(0,1,2):C.UVGC_658_958,(0,1,1):C.UVGC_587_915})

V_603 = CTVertex(name = 'V_603',
                 type = 'UV',
                 particles = [ P.g, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_266_389,(0,0,1):C.UVGC_266_390,(0,0,2):C.UVGC_266_391,(0,0,3):C.UVGC_266_392,(0,0,4):C.UVGC_266_393,(0,0,6):C.UVGC_266_394,(0,0,7):C.UVGC_266_395,(0,0,8):C.UVGC_266_396,(0,0,9):C.UVGC_266_397,(0,0,10):C.UVGC_266_398,(0,0,11):C.UVGC_266_399,(0,0,12):C.UVGC_266_400,(0,0,13):C.UVGC_266_401,(0,0,14):C.UVGC_266_402,(0,0,15):C.UVGC_266_403,(0,0,16):C.UVGC_266_404,(0,0,17):C.UVGC_266_405,(0,0,18):C.UVGC_266_406,(0,0,19):C.UVGC_266_407,(0,0,20):C.UVGC_266_408,(0,0,21):C.UVGC_266_409,(0,0,22):C.UVGC_266_410,(0,0,23):C.UVGC_266_411,(0,0,24):C.UVGC_266_412,(0,0,25):C.UVGC_266_413,(0,0,26):C.UVGC_266_414,(0,0,27):C.UVGC_266_415,(0,0,28):C.UVGC_266_416,(0,0,29):C.UVGC_266_417,(0,0,30):C.UVGC_266_418,(0,0,31):C.UVGC_266_419,(0,0,32):C.UVGC_266_420,(0,0,5):C.UVGC_314_563,(0,1,0):C.UVGC_240_336,(0,1,1):C.UVGC_240_337,(0,1,2):C.UVGC_240_338,(0,1,3):C.UVGC_240_339,(0,1,4):C.UVGC_240_340,(0,1,6):C.UVGC_240_341,(0,1,7):C.UVGC_240_342,(0,1,8):C.UVGC_240_343,(0,1,9):C.UVGC_240_344,(0,1,10):C.UVGC_240_345,(0,1,11):C.UVGC_240_346,(0,1,12):C.UVGC_240_347,(0,1,13):C.UVGC_240_348,(0,1,14):C.UVGC_240_349,(0,1,15):C.UVGC_240_350,(0,1,16):C.UVGC_240_351,(0,1,17):C.UVGC_240_352,(0,1,18):C.UVGC_240_353,(0,1,19):C.UVGC_240_354,(0,1,20):C.UVGC_240_355,(0,1,21):C.UVGC_240_356,(0,1,22):C.UVGC_240_357,(0,1,23):C.UVGC_240_358,(0,1,24):C.UVGC_240_359,(0,1,25):C.UVGC_240_360,(0,1,26):C.UVGC_240_361,(0,1,27):C.UVGC_240_362,(0,1,28):C.UVGC_240_363,(0,1,29):C.UVGC_240_364,(0,1,30):C.UVGC_240_365,(0,1,31):C.UVGC_240_366,(0,1,32):C.UVGC_240_367,(0,1,5):C.UVGC_313_562})

V_604 = CTVertex(name = 'V_604',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.Xd, P.YS3Qd1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_593_929,(0,0,2):C.UVGC_593_930,(0,0,1):C.UVGC_593_931})

V_605 = CTVertex(name = 'V_605',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.Xm, P.YS3Qd1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_593_929,(0,0,2):C.UVGC_593_930,(0,0,1):C.UVGC_593_931})

V_606 = CTVertex(name = 'V_606',
                 type = 'UV',
                 particles = [ P.W__plus__, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_657_955,(0,0,2):C.UVGC_657_956,(0,0,1):C.UVGC_587_915,(0,1,0):C.UVGC_660_962,(0,1,2):C.UVGC_660_963,(0,1,1):C.UVGC_659_961})

V_607 = CTVertex(name = 'V_607',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_312_561})

V_608 = CTVertex(name = 'V_608',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_656_954,(0,0,2):C.UVGC_655_951,(0,0,1):C.UVGC_655_953})

V_609 = CTVertex(name = 'V_609',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_267_422,(0,0,1):C.UVGC_267_423,(0,0,2):C.UVGC_267_424,(0,0,3):C.UVGC_267_425,(0,0,4):C.UVGC_267_426,(0,0,6):C.UVGC_267_427,(0,0,7):C.UVGC_267_428,(0,0,8):C.UVGC_267_429,(0,0,9):C.UVGC_267_430,(0,0,10):C.UVGC_267_431,(0,0,11):C.UVGC_267_432,(0,0,12):C.UVGC_267_433,(0,0,13):C.UVGC_267_434,(0,0,14):C.UVGC_267_435,(0,0,15):C.UVGC_267_436,(0,0,16):C.UVGC_267_437,(0,0,17):C.UVGC_267_438,(0,0,18):C.UVGC_267_439,(0,0,19):C.UVGC_267_440,(0,0,20):C.UVGC_267_441,(0,0,21):C.UVGC_267_442,(0,0,22):C.UVGC_267_443,(0,0,23):C.UVGC_267_444,(0,0,24):C.UVGC_267_445,(0,0,25):C.UVGC_267_446,(0,0,26):C.UVGC_267_447,(0,0,27):C.UVGC_267_448,(0,0,28):C.UVGC_267_449,(0,0,29):C.UVGC_267_450,(0,0,30):C.UVGC_267_451,(0,0,31):C.UVGC_267_452,(0,0,32):C.UVGC_267_453,(0,0,5):C.UVGC_315_564})

V_610 = CTVertex(name = 'V_610',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_270_459,(2,0,1):C.UVGC_270_460,(2,0,2):C.UVGC_270_461,(2,0,3):C.UVGC_270_462,(2,0,4):C.UVGC_270_463,(2,0,6):C.UVGC_270_464,(2,0,7):C.UVGC_270_465,(2,0,8):C.UVGC_270_466,(2,0,9):C.UVGC_270_467,(2,0,10):C.UVGC_270_468,(2,0,11):C.UVGC_270_469,(2,0,12):C.UVGC_270_470,(2,0,13):C.UVGC_270_471,(2,0,14):C.UVGC_270_472,(2,0,15):C.UVGC_270_473,(2,0,16):C.UVGC_270_474,(2,0,17):C.UVGC_270_475,(2,0,18):C.UVGC_270_476,(2,0,19):C.UVGC_270_477,(2,0,20):C.UVGC_270_478,(2,0,21):C.UVGC_270_479,(2,0,22):C.UVGC_270_480,(2,0,23):C.UVGC_270_481,(2,0,24):C.UVGC_270_482,(2,0,25):C.UVGC_270_483,(2,0,26):C.UVGC_270_484,(2,0,27):C.UVGC_270_485,(2,0,28):C.UVGC_270_486,(2,0,29):C.UVGC_270_487,(2,0,30):C.UVGC_270_488,(2,0,31):C.UVGC_270_489,(2,0,32):C.UVGC_270_490,(2,0,5):C.UVGC_318_565,(1,0,0):C.UVGC_270_459,(1,0,1):C.UVGC_270_460,(1,0,2):C.UVGC_270_461,(1,0,3):C.UVGC_270_462,(1,0,4):C.UVGC_270_463,(1,0,6):C.UVGC_270_464,(1,0,7):C.UVGC_270_465,(1,0,8):C.UVGC_270_466,(1,0,9):C.UVGC_270_467,(1,0,10):C.UVGC_270_468,(1,0,11):C.UVGC_270_469,(1,0,12):C.UVGC_270_470,(1,0,13):C.UVGC_270_471,(1,0,14):C.UVGC_270_472,(1,0,15):C.UVGC_270_473,(1,0,16):C.UVGC_270_474,(1,0,17):C.UVGC_270_475,(1,0,18):C.UVGC_270_476,(1,0,19):C.UVGC_270_477,(1,0,20):C.UVGC_270_478,(1,0,21):C.UVGC_270_479,(1,0,22):C.UVGC_270_480,(1,0,23):C.UVGC_270_481,(1,0,24):C.UVGC_270_482,(1,0,25):C.UVGC_270_483,(1,0,26):C.UVGC_270_484,(1,0,27):C.UVGC_270_485,(1,0,28):C.UVGC_270_486,(1,0,29):C.UVGC_270_487,(1,0,30):C.UVGC_270_488,(1,0,31):C.UVGC_270_489,(1,0,32):C.UVGC_270_490,(1,0,5):C.UVGC_318_565,(0,0,3):C.UVGC_269_457,(0,0,5):C.UVGC_269_458})

V_611 = CTVertex(name = 'V_611',
                 type = 'UV',
                 particles = [ P.a, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_327_606,(0,1,0):C.UVGC_326_605})

V_612 = CTVertex(name = 'V_612',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.s, P.YS3Qd2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YS3Qd2] ], [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_758_1037,(0,0,2):C.UVGC_758_1038,(0,0,1):C.UVGC_585_909})

V_613 = CTVertex(name = 'V_613',
                 type = 'UV',
                 particles = [ P.Xm, P.s, P.YS3Qd2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YS3Qd2] ], [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_758_1037,(0,0,2):C.UVGC_758_1038,(0,0,1):C.UVGC_585_909})

V_614 = CTVertex(name = 'V_614',
                 type = 'UV',
                 particles = [ P.W__minus__, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_692_1010,(0,0,2):C.UVGC_692_1011,(0,0,1):C.UVGC_659_961,(0,1,0):C.UVGC_691_1008,(0,1,2):C.UVGC_691_1009,(0,1,1):C.UVGC_587_915})

V_615 = CTVertex(name = 'V_615',
                 type = 'UV',
                 particles = [ P.g, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_266_389,(0,0,1):C.UVGC_266_390,(0,0,2):C.UVGC_266_391,(0,0,3):C.UVGC_266_392,(0,0,4):C.UVGC_266_393,(0,0,6):C.UVGC_266_394,(0,0,7):C.UVGC_266_395,(0,0,8):C.UVGC_266_396,(0,0,9):C.UVGC_266_397,(0,0,10):C.UVGC_266_398,(0,0,11):C.UVGC_266_399,(0,0,12):C.UVGC_266_400,(0,0,13):C.UVGC_266_401,(0,0,14):C.UVGC_266_402,(0,0,15):C.UVGC_266_403,(0,0,16):C.UVGC_266_404,(0,0,17):C.UVGC_266_405,(0,0,18):C.UVGC_266_406,(0,0,19):C.UVGC_266_407,(0,0,20):C.UVGC_266_408,(0,0,21):C.UVGC_266_409,(0,0,22):C.UVGC_266_410,(0,0,23):C.UVGC_266_411,(0,0,24):C.UVGC_266_412,(0,0,25):C.UVGC_266_413,(0,0,26):C.UVGC_266_414,(0,0,27):C.UVGC_266_415,(0,0,28):C.UVGC_266_416,(0,0,29):C.UVGC_266_417,(0,0,30):C.UVGC_266_418,(0,0,31):C.UVGC_266_419,(0,0,32):C.UVGC_266_420,(0,0,5):C.UVGC_330_609,(0,1,0):C.UVGC_240_336,(0,1,1):C.UVGC_240_337,(0,1,2):C.UVGC_240_338,(0,1,3):C.UVGC_240_339,(0,1,4):C.UVGC_240_340,(0,1,6):C.UVGC_240_341,(0,1,7):C.UVGC_240_342,(0,1,8):C.UVGC_240_343,(0,1,9):C.UVGC_240_344,(0,1,10):C.UVGC_240_345,(0,1,11):C.UVGC_240_346,(0,1,12):C.UVGC_240_347,(0,1,13):C.UVGC_240_348,(0,1,14):C.UVGC_240_349,(0,1,15):C.UVGC_240_350,(0,1,16):C.UVGC_240_351,(0,1,17):C.UVGC_240_352,(0,1,18):C.UVGC_240_353,(0,1,19):C.UVGC_240_354,(0,1,20):C.UVGC_240_355,(0,1,21):C.UVGC_240_356,(0,1,22):C.UVGC_240_357,(0,1,23):C.UVGC_240_358,(0,1,24):C.UVGC_240_359,(0,1,25):C.UVGC_240_360,(0,1,26):C.UVGC_240_361,(0,1,27):C.UVGC_240_362,(0,1,28):C.UVGC_240_363,(0,1,29):C.UVGC_240_364,(0,1,30):C.UVGC_240_365,(0,1,31):C.UVGC_240_366,(0,1,32):C.UVGC_240_367,(0,1,5):C.UVGC_329_608})

V_616 = CTVertex(name = 'V_616',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.Xd, P.YS3Qd2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YS3Qd2] ], [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_758_1037,(0,0,2):C.UVGC_758_1038,(0,0,1):C.UVGC_585_909})

V_617 = CTVertex(name = 'V_617',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.Xm, P.YS3Qd2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YS3Qd2] ], [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_758_1037,(0,0,2):C.UVGC_758_1038,(0,0,1):C.UVGC_585_909})

V_618 = CTVertex(name = 'V_618',
                 type = 'UV',
                 particles = [ P.W__plus__, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_690_1006,(0,0,2):C.UVGC_690_1007,(0,0,1):C.UVGC_587_915,(0,1,0):C.UVGC_693_1012,(0,1,2):C.UVGC_693_1013,(0,1,1):C.UVGC_659_961})

V_619 = CTVertex(name = 'V_619',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_328_607})

V_620 = CTVertex(name = 'V_620',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_689_1005,(0,0,2):C.UVGC_655_951,(0,0,1):C.UVGC_655_953})

V_621 = CTVertex(name = 'V_621',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_267_422,(0,0,1):C.UVGC_267_423,(0,0,2):C.UVGC_267_424,(0,0,3):C.UVGC_267_425,(0,0,4):C.UVGC_267_426,(0,0,6):C.UVGC_267_427,(0,0,7):C.UVGC_267_428,(0,0,8):C.UVGC_267_429,(0,0,9):C.UVGC_267_430,(0,0,10):C.UVGC_267_431,(0,0,11):C.UVGC_267_432,(0,0,12):C.UVGC_267_433,(0,0,13):C.UVGC_267_434,(0,0,14):C.UVGC_267_435,(0,0,15):C.UVGC_267_436,(0,0,16):C.UVGC_267_437,(0,0,17):C.UVGC_267_438,(0,0,18):C.UVGC_267_439,(0,0,19):C.UVGC_267_440,(0,0,20):C.UVGC_267_441,(0,0,21):C.UVGC_267_442,(0,0,22):C.UVGC_267_443,(0,0,23):C.UVGC_267_444,(0,0,24):C.UVGC_267_445,(0,0,25):C.UVGC_267_446,(0,0,26):C.UVGC_267_447,(0,0,27):C.UVGC_267_448,(0,0,28):C.UVGC_267_449,(0,0,29):C.UVGC_267_450,(0,0,30):C.UVGC_267_451,(0,0,31):C.UVGC_267_452,(0,0,32):C.UVGC_267_453,(0,0,5):C.UVGC_331_610})

V_622 = CTVertex(name = 'V_622',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_270_459,(2,0,1):C.UVGC_270_460,(2,0,2):C.UVGC_270_461,(2,0,3):C.UVGC_270_462,(2,0,4):C.UVGC_270_463,(2,0,6):C.UVGC_270_464,(2,0,7):C.UVGC_270_465,(2,0,8):C.UVGC_270_466,(2,0,9):C.UVGC_270_467,(2,0,10):C.UVGC_270_468,(2,0,11):C.UVGC_270_469,(2,0,12):C.UVGC_270_470,(2,0,13):C.UVGC_270_471,(2,0,14):C.UVGC_270_472,(2,0,15):C.UVGC_270_473,(2,0,16):C.UVGC_270_474,(2,0,17):C.UVGC_270_475,(2,0,18):C.UVGC_270_476,(2,0,19):C.UVGC_270_477,(2,0,20):C.UVGC_270_478,(2,0,21):C.UVGC_270_479,(2,0,22):C.UVGC_270_480,(2,0,23):C.UVGC_270_481,(2,0,24):C.UVGC_270_482,(2,0,25):C.UVGC_270_483,(2,0,26):C.UVGC_270_484,(2,0,27):C.UVGC_270_485,(2,0,28):C.UVGC_270_486,(2,0,29):C.UVGC_270_487,(2,0,30):C.UVGC_270_488,(2,0,31):C.UVGC_270_489,(2,0,32):C.UVGC_270_490,(2,0,5):C.UVGC_334_611,(1,0,0):C.UVGC_270_459,(1,0,1):C.UVGC_270_460,(1,0,2):C.UVGC_270_461,(1,0,3):C.UVGC_270_462,(1,0,4):C.UVGC_270_463,(1,0,6):C.UVGC_270_464,(1,0,7):C.UVGC_270_465,(1,0,8):C.UVGC_270_466,(1,0,9):C.UVGC_270_467,(1,0,10):C.UVGC_270_468,(1,0,11):C.UVGC_270_469,(1,0,12):C.UVGC_270_470,(1,0,13):C.UVGC_270_471,(1,0,14):C.UVGC_270_472,(1,0,15):C.UVGC_270_473,(1,0,16):C.UVGC_270_474,(1,0,17):C.UVGC_270_475,(1,0,18):C.UVGC_270_476,(1,0,19):C.UVGC_270_477,(1,0,20):C.UVGC_270_478,(1,0,21):C.UVGC_270_479,(1,0,22):C.UVGC_270_480,(1,0,23):C.UVGC_270_481,(1,0,24):C.UVGC_270_482,(1,0,25):C.UVGC_270_483,(1,0,26):C.UVGC_270_484,(1,0,27):C.UVGC_270_485,(1,0,28):C.UVGC_270_486,(1,0,29):C.UVGC_270_487,(1,0,30):C.UVGC_270_488,(1,0,31):C.UVGC_270_489,(1,0,32):C.UVGC_270_490,(1,0,5):C.UVGC_334_611,(0,0,3):C.UVGC_269_457,(0,0,5):C.UVGC_269_458})

V_623 = CTVertex(name = 'V_623',
                 type = 'UV',
                 particles = [ P.a, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_343_620,(0,1,0):C.UVGC_342_619})

V_624 = CTVertex(name = 'V_624',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.b, P.YS3Qd3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_580_894,(0,0,2):C.UVGC_580_895,(0,0,1):C.UVGC_580_896})

V_625 = CTVertex(name = 'V_625',
                 type = 'UV',
                 particles = [ P.Xm, P.b, P.YS3Qd3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_580_894,(0,0,2):C.UVGC_580_895,(0,0,1):C.UVGC_580_896})

V_626 = CTVertex(name = 'V_626',
                 type = 'UV',
                 particles = [ P.W__minus__, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_723_1026,(0,0,2):C.UVGC_723_1027,(0,0,1):C.UVGC_659_961,(0,1,0):C.UVGC_722_1024,(0,1,2):C.UVGC_722_1025,(0,1,1):C.UVGC_587_915})

V_627 = CTVertex(name = 'V_627',
                 type = 'UV',
                 particles = [ P.g, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_266_389,(0,0,1):C.UVGC_266_390,(0,0,2):C.UVGC_266_391,(0,0,3):C.UVGC_266_392,(0,0,4):C.UVGC_266_393,(0,0,6):C.UVGC_266_394,(0,0,7):C.UVGC_266_395,(0,0,8):C.UVGC_266_396,(0,0,9):C.UVGC_266_397,(0,0,10):C.UVGC_266_398,(0,0,11):C.UVGC_266_399,(0,0,12):C.UVGC_266_400,(0,0,13):C.UVGC_266_401,(0,0,14):C.UVGC_266_402,(0,0,15):C.UVGC_266_403,(0,0,16):C.UVGC_266_404,(0,0,17):C.UVGC_266_405,(0,0,18):C.UVGC_266_406,(0,0,19):C.UVGC_266_407,(0,0,20):C.UVGC_266_408,(0,0,21):C.UVGC_266_409,(0,0,22):C.UVGC_266_410,(0,0,23):C.UVGC_266_411,(0,0,24):C.UVGC_266_412,(0,0,25):C.UVGC_266_413,(0,0,26):C.UVGC_266_414,(0,0,27):C.UVGC_266_415,(0,0,28):C.UVGC_266_416,(0,0,29):C.UVGC_266_417,(0,0,30):C.UVGC_266_418,(0,0,31):C.UVGC_266_419,(0,0,32):C.UVGC_266_420,(0,0,5):C.UVGC_346_623,(0,1,0):C.UVGC_240_336,(0,1,1):C.UVGC_240_337,(0,1,2):C.UVGC_240_338,(0,1,3):C.UVGC_240_339,(0,1,4):C.UVGC_240_340,(0,1,6):C.UVGC_240_341,(0,1,7):C.UVGC_240_342,(0,1,8):C.UVGC_240_343,(0,1,9):C.UVGC_240_344,(0,1,10):C.UVGC_240_345,(0,1,11):C.UVGC_240_346,(0,1,12):C.UVGC_240_347,(0,1,13):C.UVGC_240_348,(0,1,14):C.UVGC_240_349,(0,1,15):C.UVGC_240_350,(0,1,16):C.UVGC_240_351,(0,1,17):C.UVGC_240_352,(0,1,18):C.UVGC_240_353,(0,1,19):C.UVGC_240_354,(0,1,20):C.UVGC_240_355,(0,1,21):C.UVGC_240_356,(0,1,22):C.UVGC_240_357,(0,1,23):C.UVGC_240_358,(0,1,24):C.UVGC_240_359,(0,1,25):C.UVGC_240_360,(0,1,26):C.UVGC_240_361,(0,1,27):C.UVGC_240_362,(0,1,28):C.UVGC_240_363,(0,1,29):C.UVGC_240_364,(0,1,30):C.UVGC_240_365,(0,1,31):C.UVGC_240_366,(0,1,32):C.UVGC_240_367,(0,1,5):C.UVGC_345_622})

V_628 = CTVertex(name = 'V_628',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.Xd, P.YS3Qd3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_580_894,(0,0,2):C.UVGC_580_895,(0,0,1):C.UVGC_580_896})

V_629 = CTVertex(name = 'V_629',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.Xm, P.YS3Qd3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_580_894,(0,0,2):C.UVGC_580_895,(0,0,1):C.UVGC_580_896})

V_630 = CTVertex(name = 'V_630',
                 type = 'UV',
                 particles = [ P.W__plus__, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_721_1022,(0,0,2):C.UVGC_721_1023,(0,0,1):C.UVGC_587_915,(0,1,0):C.UVGC_724_1028,(0,1,2):C.UVGC_724_1029,(0,1,1):C.UVGC_659_961})

V_631 = CTVertex(name = 'V_631',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_344_621})

V_632 = CTVertex(name = 'V_632',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_720_1021,(0,0,2):C.UVGC_655_951,(0,0,1):C.UVGC_655_953})

V_633 = CTVertex(name = 'V_633',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_267_422,(0,0,1):C.UVGC_267_423,(0,0,2):C.UVGC_267_424,(0,0,3):C.UVGC_267_425,(0,0,4):C.UVGC_267_426,(0,0,6):C.UVGC_267_427,(0,0,7):C.UVGC_267_428,(0,0,8):C.UVGC_267_429,(0,0,9):C.UVGC_267_430,(0,0,10):C.UVGC_267_431,(0,0,11):C.UVGC_267_432,(0,0,12):C.UVGC_267_433,(0,0,13):C.UVGC_267_434,(0,0,14):C.UVGC_267_435,(0,0,15):C.UVGC_267_436,(0,0,16):C.UVGC_267_437,(0,0,17):C.UVGC_267_438,(0,0,18):C.UVGC_267_439,(0,0,19):C.UVGC_267_440,(0,0,20):C.UVGC_267_441,(0,0,21):C.UVGC_267_442,(0,0,22):C.UVGC_267_443,(0,0,23):C.UVGC_267_444,(0,0,24):C.UVGC_267_445,(0,0,25):C.UVGC_267_446,(0,0,26):C.UVGC_267_447,(0,0,27):C.UVGC_267_448,(0,0,28):C.UVGC_267_449,(0,0,29):C.UVGC_267_450,(0,0,30):C.UVGC_267_451,(0,0,31):C.UVGC_267_452,(0,0,32):C.UVGC_267_453,(0,0,5):C.UVGC_347_624})

V_634 = CTVertex(name = 'V_634',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_270_459,(2,0,1):C.UVGC_270_460,(2,0,2):C.UVGC_270_461,(2,0,3):C.UVGC_270_462,(2,0,4):C.UVGC_270_463,(2,0,6):C.UVGC_270_464,(2,0,7):C.UVGC_270_465,(2,0,8):C.UVGC_270_466,(2,0,9):C.UVGC_270_467,(2,0,10):C.UVGC_270_468,(2,0,11):C.UVGC_270_469,(2,0,12):C.UVGC_270_470,(2,0,13):C.UVGC_270_471,(2,0,14):C.UVGC_270_472,(2,0,15):C.UVGC_270_473,(2,0,16):C.UVGC_270_474,(2,0,17):C.UVGC_270_475,(2,0,18):C.UVGC_270_476,(2,0,19):C.UVGC_270_477,(2,0,20):C.UVGC_270_478,(2,0,21):C.UVGC_270_479,(2,0,22):C.UVGC_270_480,(2,0,23):C.UVGC_270_481,(2,0,24):C.UVGC_270_482,(2,0,25):C.UVGC_270_483,(2,0,26):C.UVGC_270_484,(2,0,27):C.UVGC_270_485,(2,0,28):C.UVGC_270_486,(2,0,29):C.UVGC_270_487,(2,0,30):C.UVGC_270_488,(2,0,31):C.UVGC_270_489,(2,0,32):C.UVGC_270_490,(2,0,5):C.UVGC_350_625,(1,0,0):C.UVGC_270_459,(1,0,1):C.UVGC_270_460,(1,0,2):C.UVGC_270_461,(1,0,3):C.UVGC_270_462,(1,0,4):C.UVGC_270_463,(1,0,6):C.UVGC_270_464,(1,0,7):C.UVGC_270_465,(1,0,8):C.UVGC_270_466,(1,0,9):C.UVGC_270_467,(1,0,10):C.UVGC_270_468,(1,0,11):C.UVGC_270_469,(1,0,12):C.UVGC_270_470,(1,0,13):C.UVGC_270_471,(1,0,14):C.UVGC_270_472,(1,0,15):C.UVGC_270_473,(1,0,16):C.UVGC_270_474,(1,0,17):C.UVGC_270_475,(1,0,18):C.UVGC_270_476,(1,0,19):C.UVGC_270_477,(1,0,20):C.UVGC_270_478,(1,0,21):C.UVGC_270_479,(1,0,22):C.UVGC_270_480,(1,0,23):C.UVGC_270_481,(1,0,24):C.UVGC_270_482,(1,0,25):C.UVGC_270_483,(1,0,26):C.UVGC_270_484,(1,0,27):C.UVGC_270_485,(1,0,28):C.UVGC_270_486,(1,0,29):C.UVGC_270_487,(1,0,30):C.UVGC_270_488,(1,0,31):C.UVGC_270_489,(1,0,32):C.UVGC_270_490,(1,0,5):C.UVGC_350_625,(0,0,3):C.UVGC_269_457,(0,0,5):C.UVGC_269_458})

V_635 = CTVertex(name = 'V_635',
                 type = 'UV',
                 particles = [ P.a, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_358_633,(0,1,0):C.UVGC_359_634})

V_636 = CTVertex(name = 'V_636',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.u, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_773_1070,(0,0,2):C.UVGC_773_1071,(0,0,1):C.UVGC_593_931})

V_637 = CTVertex(name = 'V_637',
                 type = 'UV',
                 particles = [ P.Xm, P.u, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_773_1070,(0,0,2):C.UVGC_773_1071,(0,0,1):C.UVGC_593_931})

V_638 = CTVertex(name = 'V_638',
                 type = 'UV',
                 particles = [ P.a, P.W__plus__, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_661_964,(0,0,2):C.UVGC_661_965,(0,0,1):C.UVGC_661_966})

V_639 = CTVertex(name = 'V_639',
                 type = 'UV',
                 particles = [ P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_662_967,(0,0,1):C.UVGC_662_968,(0,0,2):C.UVGC_662_969,(0,0,3):C.UVGC_662_970,(0,0,4):C.UVGC_662_971,(0,0,8):C.UVGC_662_972,(0,0,9):C.UVGC_662_973,(0,0,10):C.UVGC_662_974,(0,0,11):C.UVGC_662_975,(0,0,12):C.UVGC_662_976,(0,0,13):C.UVGC_662_977,(0,0,14):C.UVGC_662_978,(0,0,15):C.UVGC_662_979,(0,0,16):C.UVGC_662_980,(0,0,17):C.UVGC_662_981,(0,0,18):C.UVGC_662_982,(0,0,19):C.UVGC_662_983,(0,0,20):C.UVGC_662_984,(0,0,21):C.UVGC_662_985,(0,0,22):C.UVGC_662_986,(0,0,23):C.UVGC_662_987,(0,0,24):C.UVGC_662_988,(0,0,25):C.UVGC_662_989,(0,0,26):C.UVGC_662_990,(0,0,27):C.UVGC_662_991,(0,0,28):C.UVGC_662_992,(0,0,29):C.UVGC_662_993,(0,0,30):C.UVGC_662_994,(0,0,31):C.UVGC_662_995,(0,0,32):C.UVGC_662_996,(0,0,33):C.UVGC_662_997,(0,0,34):C.UVGC_662_998,(0,0,5):C.UVGC_662_999,(0,0,7):C.UVGC_662_1000,(0,0,6):C.UVGC_662_1001})

V_640 = CTVertex(name = 'V_640',
                 type = 'UV',
                 particles = [ P.g, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_266_389,(0,0,1):C.UVGC_266_390,(0,0,2):C.UVGC_266_391,(0,0,3):C.UVGC_266_392,(0,0,4):C.UVGC_266_393,(0,0,6):C.UVGC_266_394,(0,0,7):C.UVGC_266_395,(0,0,8):C.UVGC_266_396,(0,0,9):C.UVGC_266_397,(0,0,10):C.UVGC_266_398,(0,0,11):C.UVGC_266_399,(0,0,12):C.UVGC_266_400,(0,0,13):C.UVGC_266_401,(0,0,14):C.UVGC_266_402,(0,0,15):C.UVGC_266_403,(0,0,16):C.UVGC_266_404,(0,0,17):C.UVGC_266_405,(0,0,18):C.UVGC_266_406,(0,0,19):C.UVGC_266_407,(0,0,20):C.UVGC_266_408,(0,0,21):C.UVGC_266_409,(0,0,22):C.UVGC_266_410,(0,0,23):C.UVGC_266_411,(0,0,24):C.UVGC_266_412,(0,0,25):C.UVGC_266_413,(0,0,26):C.UVGC_266_414,(0,0,27):C.UVGC_266_415,(0,0,28):C.UVGC_266_416,(0,0,29):C.UVGC_266_417,(0,0,30):C.UVGC_266_418,(0,0,31):C.UVGC_266_419,(0,0,32):C.UVGC_266_420,(0,0,5):C.UVGC_362_637,(0,1,0):C.UVGC_240_336,(0,1,1):C.UVGC_240_337,(0,1,2):C.UVGC_240_338,(0,1,3):C.UVGC_240_339,(0,1,4):C.UVGC_240_340,(0,1,6):C.UVGC_240_341,(0,1,7):C.UVGC_240_342,(0,1,8):C.UVGC_240_343,(0,1,9):C.UVGC_240_344,(0,1,10):C.UVGC_240_345,(0,1,11):C.UVGC_240_346,(0,1,12):C.UVGC_240_347,(0,1,13):C.UVGC_240_348,(0,1,14):C.UVGC_240_349,(0,1,15):C.UVGC_240_350,(0,1,16):C.UVGC_240_351,(0,1,17):C.UVGC_240_352,(0,1,18):C.UVGC_240_353,(0,1,19):C.UVGC_240_354,(0,1,20):C.UVGC_240_355,(0,1,21):C.UVGC_240_356,(0,1,22):C.UVGC_240_357,(0,1,23):C.UVGC_240_358,(0,1,24):C.UVGC_240_359,(0,1,25):C.UVGC_240_360,(0,1,26):C.UVGC_240_361,(0,1,27):C.UVGC_240_362,(0,1,28):C.UVGC_240_363,(0,1,29):C.UVGC_240_364,(0,1,30):C.UVGC_240_365,(0,1,31):C.UVGC_240_366,(0,1,32):C.UVGC_240_367,(0,1,5):C.UVGC_361_636})

V_641 = CTVertex(name = 'V_641',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.Xd, P.YS3Qu1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_773_1070,(0,0,2):C.UVGC_773_1071,(0,0,1):C.UVGC_593_931})

V_642 = CTVertex(name = 'V_642',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.Xm, P.YS3Qu1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_773_1070,(0,0,2):C.UVGC_773_1071,(0,0,1):C.UVGC_593_931})

V_643 = CTVertex(name = 'V_643',
                 type = 'UV',
                 particles = [ P.a, P.W__minus__, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_661_964,(0,0,2):C.UVGC_661_965,(0,0,1):C.UVGC_661_966})

V_644 = CTVertex(name = 'V_644',
                 type = 'UV',
                 particles = [ P.g, P.W__minus__, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_662_967,(0,0,1):C.UVGC_662_968,(0,0,2):C.UVGC_662_969,(0,0,3):C.UVGC_662_970,(0,0,4):C.UVGC_662_971,(0,0,8):C.UVGC_662_972,(0,0,9):C.UVGC_662_973,(0,0,10):C.UVGC_662_974,(0,0,11):C.UVGC_662_975,(0,0,12):C.UVGC_662_976,(0,0,13):C.UVGC_662_977,(0,0,14):C.UVGC_662_978,(0,0,15):C.UVGC_662_979,(0,0,16):C.UVGC_662_980,(0,0,17):C.UVGC_662_981,(0,0,18):C.UVGC_662_982,(0,0,19):C.UVGC_662_983,(0,0,20):C.UVGC_662_984,(0,0,21):C.UVGC_662_985,(0,0,22):C.UVGC_662_986,(0,0,23):C.UVGC_662_987,(0,0,24):C.UVGC_662_988,(0,0,25):C.UVGC_662_989,(0,0,26):C.UVGC_662_990,(0,0,27):C.UVGC_662_991,(0,0,28):C.UVGC_662_992,(0,0,29):C.UVGC_662_993,(0,0,30):C.UVGC_662_994,(0,0,31):C.UVGC_662_995,(0,0,32):C.UVGC_662_996,(0,0,33):C.UVGC_662_997,(0,0,34):C.UVGC_662_998,(0,0,5):C.UVGC_662_999,(0,0,7):C.UVGC_662_1000,(0,0,6):C.UVGC_662_1001})

V_645 = CTVertex(name = 'V_645',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_360_635})

V_646 = CTVertex(name = 'V_646',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_655_951,(0,0,2):C.UVGC_655_952,(0,0,1):C.UVGC_655_953})

V_647 = CTVertex(name = 'V_647',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_363_638,(0,0,1):C.UVGC_363_639,(0,0,2):C.UVGC_363_640,(0,0,3):C.UVGC_363_641,(0,0,4):C.UVGC_363_642,(0,0,6):C.UVGC_363_643,(0,0,7):C.UVGC_363_644,(0,0,8):C.UVGC_363_645,(0,0,9):C.UVGC_363_646,(0,0,10):C.UVGC_363_647,(0,0,11):C.UVGC_363_648,(0,0,12):C.UVGC_363_649,(0,0,13):C.UVGC_363_650,(0,0,14):C.UVGC_363_651,(0,0,15):C.UVGC_363_652,(0,0,16):C.UVGC_363_653,(0,0,17):C.UVGC_363_654,(0,0,18):C.UVGC_363_655,(0,0,19):C.UVGC_363_656,(0,0,20):C.UVGC_363_657,(0,0,21):C.UVGC_363_658,(0,0,22):C.UVGC_363_659,(0,0,23):C.UVGC_363_660,(0,0,24):C.UVGC_363_661,(0,0,25):C.UVGC_363_662,(0,0,26):C.UVGC_363_663,(0,0,27):C.UVGC_363_664,(0,0,28):C.UVGC_363_665,(0,0,29):C.UVGC_363_666,(0,0,30):C.UVGC_363_667,(0,0,31):C.UVGC_363_668,(0,0,32):C.UVGC_363_669,(0,0,5):C.UVGC_363_670})

V_648 = CTVertex(name = 'V_648',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_270_459,(2,0,1):C.UVGC_270_460,(2,0,2):C.UVGC_270_461,(2,0,3):C.UVGC_270_462,(2,0,4):C.UVGC_270_463,(2,0,6):C.UVGC_270_464,(2,0,7):C.UVGC_270_465,(2,0,8):C.UVGC_270_466,(2,0,9):C.UVGC_270_467,(2,0,10):C.UVGC_270_468,(2,0,11):C.UVGC_270_469,(2,0,12):C.UVGC_270_470,(2,0,13):C.UVGC_270_471,(2,0,14):C.UVGC_270_472,(2,0,15):C.UVGC_270_473,(2,0,16):C.UVGC_270_474,(2,0,17):C.UVGC_270_475,(2,0,18):C.UVGC_270_476,(2,0,19):C.UVGC_270_477,(2,0,20):C.UVGC_270_478,(2,0,21):C.UVGC_270_479,(2,0,22):C.UVGC_270_480,(2,0,23):C.UVGC_270_481,(2,0,24):C.UVGC_270_482,(2,0,25):C.UVGC_270_483,(2,0,26):C.UVGC_270_484,(2,0,27):C.UVGC_270_485,(2,0,28):C.UVGC_270_486,(2,0,29):C.UVGC_270_487,(2,0,30):C.UVGC_270_488,(2,0,31):C.UVGC_270_489,(2,0,32):C.UVGC_270_490,(2,0,5):C.UVGC_366_671,(1,0,0):C.UVGC_270_459,(1,0,1):C.UVGC_270_460,(1,0,2):C.UVGC_270_461,(1,0,3):C.UVGC_270_462,(1,0,4):C.UVGC_270_463,(1,0,6):C.UVGC_270_464,(1,0,7):C.UVGC_270_465,(1,0,8):C.UVGC_270_466,(1,0,9):C.UVGC_270_467,(1,0,10):C.UVGC_270_468,(1,0,11):C.UVGC_270_469,(1,0,12):C.UVGC_270_470,(1,0,13):C.UVGC_270_471,(1,0,14):C.UVGC_270_472,(1,0,15):C.UVGC_270_473,(1,0,16):C.UVGC_270_474,(1,0,17):C.UVGC_270_475,(1,0,18):C.UVGC_270_476,(1,0,19):C.UVGC_270_477,(1,0,20):C.UVGC_270_478,(1,0,21):C.UVGC_270_479,(1,0,22):C.UVGC_270_480,(1,0,23):C.UVGC_270_481,(1,0,24):C.UVGC_270_482,(1,0,25):C.UVGC_270_483,(1,0,26):C.UVGC_270_484,(1,0,27):C.UVGC_270_485,(1,0,28):C.UVGC_270_486,(1,0,29):C.UVGC_270_487,(1,0,30):C.UVGC_270_488,(1,0,31):C.UVGC_270_489,(1,0,32):C.UVGC_270_490,(1,0,5):C.UVGC_366_671,(0,0,3):C.UVGC_269_457,(0,0,5):C.UVGC_269_458})

V_649 = CTVertex(name = 'V_649',
                 type = 'UV',
                 particles = [ P.a, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_374_711,(0,1,0):C.UVGC_375_712})

V_650 = CTVertex(name = 'V_650',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.c, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_585_907,(0,0,2):C.UVGC_585_908,(0,0,1):C.UVGC_585_909})

V_651 = CTVertex(name = 'V_651',
                 type = 'UV',
                 particles = [ P.Xm, P.c, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_585_907,(0,0,2):C.UVGC_585_908,(0,0,1):C.UVGC_585_909})

V_652 = CTVertex(name = 'V_652',
                 type = 'UV',
                 particles = [ P.a, P.W__plus__, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_694_1014,(0,0,2):C.UVGC_694_1015,(0,0,1):C.UVGC_661_966})

V_653 = CTVertex(name = 'V_653',
                 type = 'UV',
                 particles = [ P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_662_967,(0,0,1):C.UVGC_662_968,(0,0,2):C.UVGC_662_969,(0,0,3):C.UVGC_662_970,(0,0,4):C.UVGC_662_971,(0,0,8):C.UVGC_662_972,(0,0,9):C.UVGC_662_973,(0,0,10):C.UVGC_662_974,(0,0,11):C.UVGC_662_975,(0,0,12):C.UVGC_662_976,(0,0,13):C.UVGC_662_977,(0,0,14):C.UVGC_662_978,(0,0,15):C.UVGC_662_979,(0,0,16):C.UVGC_662_980,(0,0,17):C.UVGC_662_981,(0,0,18):C.UVGC_662_982,(0,0,19):C.UVGC_662_983,(0,0,20):C.UVGC_662_984,(0,0,21):C.UVGC_662_985,(0,0,22):C.UVGC_662_986,(0,0,23):C.UVGC_662_987,(0,0,24):C.UVGC_662_988,(0,0,25):C.UVGC_662_989,(0,0,26):C.UVGC_662_990,(0,0,27):C.UVGC_662_991,(0,0,28):C.UVGC_662_992,(0,0,29):C.UVGC_662_993,(0,0,30):C.UVGC_662_994,(0,0,31):C.UVGC_662_995,(0,0,32):C.UVGC_662_996,(0,0,33):C.UVGC_662_997,(0,0,34):C.UVGC_662_998,(0,0,5):C.UVGC_695_1016,(0,0,7):C.UVGC_695_1017,(0,0,6):C.UVGC_662_1001})

V_654 = CTVertex(name = 'V_654',
                 type = 'UV',
                 particles = [ P.g, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_266_389,(0,0,1):C.UVGC_266_390,(0,0,2):C.UVGC_266_391,(0,0,3):C.UVGC_266_392,(0,0,4):C.UVGC_266_393,(0,0,6):C.UVGC_266_394,(0,0,7):C.UVGC_266_395,(0,0,8):C.UVGC_266_396,(0,0,9):C.UVGC_266_397,(0,0,10):C.UVGC_266_398,(0,0,11):C.UVGC_266_399,(0,0,12):C.UVGC_266_400,(0,0,13):C.UVGC_266_401,(0,0,14):C.UVGC_266_402,(0,0,15):C.UVGC_266_403,(0,0,16):C.UVGC_266_404,(0,0,17):C.UVGC_266_405,(0,0,18):C.UVGC_266_406,(0,0,19):C.UVGC_266_407,(0,0,20):C.UVGC_266_408,(0,0,21):C.UVGC_266_409,(0,0,22):C.UVGC_266_410,(0,0,23):C.UVGC_266_411,(0,0,24):C.UVGC_266_412,(0,0,25):C.UVGC_266_413,(0,0,26):C.UVGC_266_414,(0,0,27):C.UVGC_266_415,(0,0,28):C.UVGC_266_416,(0,0,29):C.UVGC_266_417,(0,0,30):C.UVGC_266_418,(0,0,31):C.UVGC_266_419,(0,0,32):C.UVGC_266_420,(0,0,5):C.UVGC_378_715,(0,1,0):C.UVGC_240_336,(0,1,1):C.UVGC_240_337,(0,1,2):C.UVGC_240_338,(0,1,3):C.UVGC_240_339,(0,1,4):C.UVGC_240_340,(0,1,6):C.UVGC_240_341,(0,1,7):C.UVGC_240_342,(0,1,8):C.UVGC_240_343,(0,1,9):C.UVGC_240_344,(0,1,10):C.UVGC_240_345,(0,1,11):C.UVGC_240_346,(0,1,12):C.UVGC_240_347,(0,1,13):C.UVGC_240_348,(0,1,14):C.UVGC_240_349,(0,1,15):C.UVGC_240_350,(0,1,16):C.UVGC_240_351,(0,1,17):C.UVGC_240_352,(0,1,18):C.UVGC_240_353,(0,1,19):C.UVGC_240_354,(0,1,20):C.UVGC_240_355,(0,1,21):C.UVGC_240_356,(0,1,22):C.UVGC_240_357,(0,1,23):C.UVGC_240_358,(0,1,24):C.UVGC_240_359,(0,1,25):C.UVGC_240_360,(0,1,26):C.UVGC_240_361,(0,1,27):C.UVGC_240_362,(0,1,28):C.UVGC_240_363,(0,1,29):C.UVGC_240_364,(0,1,30):C.UVGC_240_365,(0,1,31):C.UVGC_240_366,(0,1,32):C.UVGC_240_367,(0,1,5):C.UVGC_377_714})

V_655 = CTVertex(name = 'V_655',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.Xd, P.YS3Qu2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_585_907,(0,0,2):C.UVGC_585_908,(0,0,1):C.UVGC_585_909})

V_656 = CTVertex(name = 'V_656',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.Xm, P.YS3Qu2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_585_907,(0,0,2):C.UVGC_585_908,(0,0,1):C.UVGC_585_909})

V_657 = CTVertex(name = 'V_657',
                 type = 'UV',
                 particles = [ P.a, P.W__minus__, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_694_1014,(0,0,2):C.UVGC_694_1015,(0,0,1):C.UVGC_661_966})

V_658 = CTVertex(name = 'V_658',
                 type = 'UV',
                 particles = [ P.g, P.W__minus__, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_662_967,(0,0,1):C.UVGC_662_968,(0,0,2):C.UVGC_662_969,(0,0,3):C.UVGC_662_970,(0,0,4):C.UVGC_662_971,(0,0,8):C.UVGC_662_972,(0,0,9):C.UVGC_662_973,(0,0,10):C.UVGC_662_974,(0,0,11):C.UVGC_662_975,(0,0,12):C.UVGC_662_976,(0,0,13):C.UVGC_662_977,(0,0,14):C.UVGC_662_978,(0,0,15):C.UVGC_662_979,(0,0,16):C.UVGC_662_980,(0,0,17):C.UVGC_662_981,(0,0,18):C.UVGC_662_982,(0,0,19):C.UVGC_662_983,(0,0,20):C.UVGC_662_984,(0,0,21):C.UVGC_662_985,(0,0,22):C.UVGC_662_986,(0,0,23):C.UVGC_662_987,(0,0,24):C.UVGC_662_988,(0,0,25):C.UVGC_662_989,(0,0,26):C.UVGC_662_990,(0,0,27):C.UVGC_662_991,(0,0,28):C.UVGC_662_992,(0,0,29):C.UVGC_662_993,(0,0,30):C.UVGC_662_994,(0,0,31):C.UVGC_662_995,(0,0,32):C.UVGC_662_996,(0,0,33):C.UVGC_662_997,(0,0,34):C.UVGC_662_998,(0,0,5):C.UVGC_695_1016,(0,0,7):C.UVGC_695_1017,(0,0,6):C.UVGC_662_1001})

V_659 = CTVertex(name = 'V_659',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_376_713})

V_660 = CTVertex(name = 'V_660',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_655_951,(0,0,2):C.UVGC_688_1004,(0,0,1):C.UVGC_655_953})

V_661 = CTVertex(name = 'V_661',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_363_638,(0,0,1):C.UVGC_363_639,(0,0,2):C.UVGC_363_640,(0,0,3):C.UVGC_363_641,(0,0,4):C.UVGC_363_642,(0,0,6):C.UVGC_363_643,(0,0,7):C.UVGC_363_644,(0,0,8):C.UVGC_363_645,(0,0,9):C.UVGC_363_646,(0,0,10):C.UVGC_363_647,(0,0,11):C.UVGC_363_648,(0,0,12):C.UVGC_363_649,(0,0,13):C.UVGC_363_650,(0,0,14):C.UVGC_363_651,(0,0,15):C.UVGC_363_652,(0,0,16):C.UVGC_363_653,(0,0,17):C.UVGC_363_654,(0,0,18):C.UVGC_363_655,(0,0,19):C.UVGC_363_656,(0,0,20):C.UVGC_363_657,(0,0,21):C.UVGC_363_658,(0,0,22):C.UVGC_363_659,(0,0,23):C.UVGC_363_660,(0,0,24):C.UVGC_363_661,(0,0,25):C.UVGC_363_662,(0,0,26):C.UVGC_363_663,(0,0,27):C.UVGC_363_664,(0,0,28):C.UVGC_363_665,(0,0,29):C.UVGC_363_666,(0,0,30):C.UVGC_363_667,(0,0,31):C.UVGC_363_668,(0,0,32):C.UVGC_363_669,(0,0,5):C.UVGC_379_716})

V_662 = CTVertex(name = 'V_662',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_270_459,(2,0,1):C.UVGC_270_460,(2,0,2):C.UVGC_270_461,(2,0,3):C.UVGC_270_462,(2,0,4):C.UVGC_270_463,(2,0,6):C.UVGC_270_464,(2,0,7):C.UVGC_270_465,(2,0,8):C.UVGC_270_466,(2,0,9):C.UVGC_270_467,(2,0,10):C.UVGC_270_468,(2,0,11):C.UVGC_270_469,(2,0,12):C.UVGC_270_470,(2,0,13):C.UVGC_270_471,(2,0,14):C.UVGC_270_472,(2,0,15):C.UVGC_270_473,(2,0,16):C.UVGC_270_474,(2,0,17):C.UVGC_270_475,(2,0,18):C.UVGC_270_476,(2,0,19):C.UVGC_270_477,(2,0,20):C.UVGC_270_478,(2,0,21):C.UVGC_270_479,(2,0,22):C.UVGC_270_480,(2,0,23):C.UVGC_270_481,(2,0,24):C.UVGC_270_482,(2,0,25):C.UVGC_270_483,(2,0,26):C.UVGC_270_484,(2,0,27):C.UVGC_270_485,(2,0,28):C.UVGC_270_486,(2,0,29):C.UVGC_270_487,(2,0,30):C.UVGC_270_488,(2,0,31):C.UVGC_270_489,(2,0,32):C.UVGC_270_490,(2,0,5):C.UVGC_382_717,(1,0,0):C.UVGC_270_459,(1,0,1):C.UVGC_270_460,(1,0,2):C.UVGC_270_461,(1,0,3):C.UVGC_270_462,(1,0,4):C.UVGC_270_463,(1,0,6):C.UVGC_270_464,(1,0,7):C.UVGC_270_465,(1,0,8):C.UVGC_270_466,(1,0,9):C.UVGC_270_467,(1,0,10):C.UVGC_270_468,(1,0,11):C.UVGC_270_469,(1,0,12):C.UVGC_270_470,(1,0,13):C.UVGC_270_471,(1,0,14):C.UVGC_270_472,(1,0,15):C.UVGC_270_473,(1,0,16):C.UVGC_270_474,(1,0,17):C.UVGC_270_475,(1,0,18):C.UVGC_270_476,(1,0,19):C.UVGC_270_477,(1,0,20):C.UVGC_270_478,(1,0,21):C.UVGC_270_479,(1,0,22):C.UVGC_270_480,(1,0,23):C.UVGC_270_481,(1,0,24):C.UVGC_270_482,(1,0,25):C.UVGC_270_483,(1,0,26):C.UVGC_270_484,(1,0,27):C.UVGC_270_485,(1,0,28):C.UVGC_270_486,(1,0,29):C.UVGC_270_487,(1,0,30):C.UVGC_270_488,(1,0,31):C.UVGC_270_489,(1,0,32):C.UVGC_270_490,(1,0,5):C.UVGC_382_717,(0,0,3):C.UVGC_269_457,(0,0,5):C.UVGC_269_458})

V_663 = CTVertex(name = 'V_663',
                 type = 'UV',
                 particles = [ P.a, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_390_725,(0,1,0):C.UVGC_391_726})

V_664 = CTVertex(name = 'V_664',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.t, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_766_1055,(0,0,2):C.UVGC_766_1056,(0,0,1):C.UVGC_580_896})

V_665 = CTVertex(name = 'V_665',
                 type = 'UV',
                 particles = [ P.Xm, P.t, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_766_1055,(0,0,2):C.UVGC_766_1056,(0,0,1):C.UVGC_580_896})

V_666 = CTVertex(name = 'V_666',
                 type = 'UV',
                 particles = [ P.a, P.W__plus__, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_725_1030,(0,0,2):C.UVGC_725_1031,(0,0,1):C.UVGC_661_966})

V_667 = CTVertex(name = 'V_667',
                 type = 'UV',
                 particles = [ P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_662_967,(0,0,1):C.UVGC_662_968,(0,0,2):C.UVGC_662_969,(0,0,3):C.UVGC_662_970,(0,0,4):C.UVGC_662_971,(0,0,8):C.UVGC_662_972,(0,0,9):C.UVGC_662_973,(0,0,10):C.UVGC_662_974,(0,0,11):C.UVGC_662_975,(0,0,12):C.UVGC_662_976,(0,0,13):C.UVGC_662_977,(0,0,14):C.UVGC_662_978,(0,0,15):C.UVGC_662_979,(0,0,16):C.UVGC_662_980,(0,0,17):C.UVGC_662_981,(0,0,18):C.UVGC_662_982,(0,0,19):C.UVGC_662_983,(0,0,20):C.UVGC_662_984,(0,0,21):C.UVGC_662_985,(0,0,22):C.UVGC_662_986,(0,0,23):C.UVGC_662_987,(0,0,24):C.UVGC_662_988,(0,0,25):C.UVGC_662_989,(0,0,26):C.UVGC_662_990,(0,0,27):C.UVGC_662_991,(0,0,28):C.UVGC_662_992,(0,0,29):C.UVGC_662_993,(0,0,30):C.UVGC_662_994,(0,0,31):C.UVGC_662_995,(0,0,32):C.UVGC_662_996,(0,0,33):C.UVGC_662_997,(0,0,34):C.UVGC_662_998,(0,0,5):C.UVGC_726_1032,(0,0,7):C.UVGC_726_1033,(0,0,6):C.UVGC_662_1001})

V_668 = CTVertex(name = 'V_668',
                 type = 'UV',
                 particles = [ P.g, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_266_389,(0,0,1):C.UVGC_266_390,(0,0,2):C.UVGC_266_391,(0,0,3):C.UVGC_266_392,(0,0,4):C.UVGC_266_393,(0,0,6):C.UVGC_266_394,(0,0,7):C.UVGC_266_395,(0,0,8):C.UVGC_266_396,(0,0,9):C.UVGC_266_397,(0,0,10):C.UVGC_266_398,(0,0,11):C.UVGC_266_399,(0,0,12):C.UVGC_266_400,(0,0,13):C.UVGC_266_401,(0,0,14):C.UVGC_266_402,(0,0,15):C.UVGC_266_403,(0,0,16):C.UVGC_266_404,(0,0,17):C.UVGC_266_405,(0,0,18):C.UVGC_266_406,(0,0,19):C.UVGC_266_407,(0,0,20):C.UVGC_266_408,(0,0,21):C.UVGC_266_409,(0,0,22):C.UVGC_266_410,(0,0,23):C.UVGC_266_411,(0,0,24):C.UVGC_266_412,(0,0,25):C.UVGC_266_413,(0,0,26):C.UVGC_266_414,(0,0,27):C.UVGC_266_415,(0,0,28):C.UVGC_266_416,(0,0,29):C.UVGC_266_417,(0,0,30):C.UVGC_266_418,(0,0,31):C.UVGC_266_419,(0,0,32):C.UVGC_266_420,(0,0,5):C.UVGC_394_729,(0,1,0):C.UVGC_240_336,(0,1,1):C.UVGC_240_337,(0,1,2):C.UVGC_240_338,(0,1,3):C.UVGC_240_339,(0,1,4):C.UVGC_240_340,(0,1,6):C.UVGC_240_341,(0,1,7):C.UVGC_240_342,(0,1,8):C.UVGC_240_343,(0,1,9):C.UVGC_240_344,(0,1,10):C.UVGC_240_345,(0,1,11):C.UVGC_240_346,(0,1,12):C.UVGC_240_347,(0,1,13):C.UVGC_240_348,(0,1,14):C.UVGC_240_349,(0,1,15):C.UVGC_240_350,(0,1,16):C.UVGC_240_351,(0,1,17):C.UVGC_240_352,(0,1,18):C.UVGC_240_353,(0,1,19):C.UVGC_240_354,(0,1,20):C.UVGC_240_355,(0,1,21):C.UVGC_240_356,(0,1,22):C.UVGC_240_357,(0,1,23):C.UVGC_240_358,(0,1,24):C.UVGC_240_359,(0,1,25):C.UVGC_240_360,(0,1,26):C.UVGC_240_361,(0,1,27):C.UVGC_240_362,(0,1,28):C.UVGC_240_363,(0,1,29):C.UVGC_240_364,(0,1,30):C.UVGC_240_365,(0,1,31):C.UVGC_240_366,(0,1,32):C.UVGC_240_367,(0,1,5):C.UVGC_393_728})

V_669 = CTVertex(name = 'V_669',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.Xd, P.YS3Qu3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_766_1055,(0,0,2):C.UVGC_766_1056,(0,0,1):C.UVGC_580_896})

V_670 = CTVertex(name = 'V_670',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.Xm, P.YS3Qu3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_766_1055,(0,0,2):C.UVGC_766_1056,(0,0,1):C.UVGC_580_896})

V_671 = CTVertex(name = 'V_671',
                 type = 'UV',
                 particles = [ P.a, P.W__minus__, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_725_1030,(0,0,2):C.UVGC_725_1031,(0,0,1):C.UVGC_661_966})

V_672 = CTVertex(name = 'V_672',
                 type = 'UV',
                 particles = [ P.g, P.W__minus__, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_662_967,(0,0,1):C.UVGC_662_968,(0,0,2):C.UVGC_662_969,(0,0,3):C.UVGC_662_970,(0,0,4):C.UVGC_662_971,(0,0,8):C.UVGC_662_972,(0,0,9):C.UVGC_662_973,(0,0,10):C.UVGC_662_974,(0,0,11):C.UVGC_662_975,(0,0,12):C.UVGC_662_976,(0,0,13):C.UVGC_662_977,(0,0,14):C.UVGC_662_978,(0,0,15):C.UVGC_662_979,(0,0,16):C.UVGC_662_980,(0,0,17):C.UVGC_662_981,(0,0,18):C.UVGC_662_982,(0,0,19):C.UVGC_662_983,(0,0,20):C.UVGC_662_984,(0,0,21):C.UVGC_662_985,(0,0,22):C.UVGC_662_986,(0,0,23):C.UVGC_662_987,(0,0,24):C.UVGC_662_988,(0,0,25):C.UVGC_662_989,(0,0,26):C.UVGC_662_990,(0,0,27):C.UVGC_662_991,(0,0,28):C.UVGC_662_992,(0,0,29):C.UVGC_662_993,(0,0,30):C.UVGC_662_994,(0,0,31):C.UVGC_662_995,(0,0,32):C.UVGC_662_996,(0,0,33):C.UVGC_662_997,(0,0,34):C.UVGC_662_998,(0,0,5):C.UVGC_726_1032,(0,0,7):C.UVGC_726_1033,(0,0,6):C.UVGC_662_1001})

V_673 = CTVertex(name = 'V_673',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_392_727})

V_674 = CTVertex(name = 'V_674',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_655_951,(0,0,2):C.UVGC_719_1020,(0,0,1):C.UVGC_655_953})

V_675 = CTVertex(name = 'V_675',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_363_638,(0,0,1):C.UVGC_363_639,(0,0,2):C.UVGC_363_640,(0,0,3):C.UVGC_363_641,(0,0,4):C.UVGC_363_642,(0,0,6):C.UVGC_363_643,(0,0,7):C.UVGC_363_644,(0,0,8):C.UVGC_363_645,(0,0,9):C.UVGC_363_646,(0,0,10):C.UVGC_363_647,(0,0,11):C.UVGC_363_648,(0,0,12):C.UVGC_363_649,(0,0,13):C.UVGC_363_650,(0,0,14):C.UVGC_363_651,(0,0,15):C.UVGC_363_652,(0,0,16):C.UVGC_363_653,(0,0,17):C.UVGC_363_654,(0,0,18):C.UVGC_363_655,(0,0,19):C.UVGC_363_656,(0,0,20):C.UVGC_363_657,(0,0,21):C.UVGC_363_658,(0,0,22):C.UVGC_363_659,(0,0,23):C.UVGC_363_660,(0,0,24):C.UVGC_363_661,(0,0,25):C.UVGC_363_662,(0,0,26):C.UVGC_363_663,(0,0,27):C.UVGC_363_664,(0,0,28):C.UVGC_363_665,(0,0,29):C.UVGC_363_666,(0,0,30):C.UVGC_363_667,(0,0,31):C.UVGC_363_668,(0,0,32):C.UVGC_363_669,(0,0,5):C.UVGC_395_730})

V_676 = CTVertex(name = 'V_676',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_270_459,(2,0,1):C.UVGC_270_460,(2,0,2):C.UVGC_270_461,(2,0,3):C.UVGC_270_462,(2,0,4):C.UVGC_270_463,(2,0,6):C.UVGC_270_464,(2,0,7):C.UVGC_270_465,(2,0,8):C.UVGC_270_466,(2,0,9):C.UVGC_270_467,(2,0,10):C.UVGC_270_468,(2,0,11):C.UVGC_270_469,(2,0,12):C.UVGC_270_470,(2,0,13):C.UVGC_270_471,(2,0,14):C.UVGC_270_472,(2,0,15):C.UVGC_270_473,(2,0,16):C.UVGC_270_474,(2,0,17):C.UVGC_270_475,(2,0,18):C.UVGC_270_476,(2,0,19):C.UVGC_270_477,(2,0,20):C.UVGC_270_478,(2,0,21):C.UVGC_270_479,(2,0,22):C.UVGC_270_480,(2,0,23):C.UVGC_270_481,(2,0,24):C.UVGC_270_482,(2,0,25):C.UVGC_270_483,(2,0,26):C.UVGC_270_484,(2,0,27):C.UVGC_270_485,(2,0,28):C.UVGC_270_486,(2,0,29):C.UVGC_270_487,(2,0,30):C.UVGC_270_488,(2,0,31):C.UVGC_270_489,(2,0,32):C.UVGC_270_490,(2,0,5):C.UVGC_398_731,(1,0,0):C.UVGC_270_459,(1,0,1):C.UVGC_270_460,(1,0,2):C.UVGC_270_461,(1,0,3):C.UVGC_270_462,(1,0,4):C.UVGC_270_463,(1,0,6):C.UVGC_270_464,(1,0,7):C.UVGC_270_465,(1,0,8):C.UVGC_270_466,(1,0,9):C.UVGC_270_467,(1,0,10):C.UVGC_270_468,(1,0,11):C.UVGC_270_469,(1,0,12):C.UVGC_270_470,(1,0,13):C.UVGC_270_471,(1,0,14):C.UVGC_270_472,(1,0,15):C.UVGC_270_473,(1,0,16):C.UVGC_270_474,(1,0,17):C.UVGC_270_475,(1,0,18):C.UVGC_270_476,(1,0,19):C.UVGC_270_477,(1,0,20):C.UVGC_270_478,(1,0,21):C.UVGC_270_479,(1,0,22):C.UVGC_270_480,(1,0,23):C.UVGC_270_481,(1,0,24):C.UVGC_270_482,(1,0,25):C.UVGC_270_483,(1,0,26):C.UVGC_270_484,(1,0,27):C.UVGC_270_485,(1,0,28):C.UVGC_270_486,(1,0,29):C.UVGC_270_487,(1,0,30):C.UVGC_270_488,(1,0,31):C.UVGC_270_489,(1,0,32):C.UVGC_270_490,(1,0,5):C.UVGC_398_731,(0,0,3):C.UVGC_269_457,(0,0,5):C.UVGC_269_458})

V_677 = CTVertex(name = 'V_677',
                 type = 'UV',
                 particles = [ P.a, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_406_739,(0,1,0):C.UVGC_407_740})

V_678 = CTVertex(name = 'V_678',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.u, P.YS3u1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YS3u1] ], [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_774_1072,(0,0,2):C.UVGC_774_1073,(0,0,1):C.UVGC_774_1074})

V_679 = CTVertex(name = 'V_679',
                 type = 'UV',
                 particles = [ P.Xm, P.u, P.YS3u1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YS3u1] ], [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_774_1072,(0,0,2):C.UVGC_774_1073,(0,0,1):C.UVGC_774_1074})

V_680 = CTVertex(name = 'V_680',
                 type = 'UV',
                 particles = [ P.g, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_266_389,(0,0,1):C.UVGC_266_390,(0,0,2):C.UVGC_266_391,(0,0,3):C.UVGC_266_392,(0,0,4):C.UVGC_266_393,(0,0,6):C.UVGC_266_394,(0,0,7):C.UVGC_266_395,(0,0,8):C.UVGC_266_396,(0,0,9):C.UVGC_266_397,(0,0,10):C.UVGC_266_398,(0,0,11):C.UVGC_266_399,(0,0,12):C.UVGC_266_400,(0,0,13):C.UVGC_266_401,(0,0,14):C.UVGC_266_402,(0,0,15):C.UVGC_266_403,(0,0,16):C.UVGC_266_404,(0,0,17):C.UVGC_266_405,(0,0,18):C.UVGC_266_406,(0,0,19):C.UVGC_266_407,(0,0,20):C.UVGC_266_408,(0,0,21):C.UVGC_266_409,(0,0,22):C.UVGC_266_410,(0,0,23):C.UVGC_266_411,(0,0,24):C.UVGC_266_412,(0,0,25):C.UVGC_266_413,(0,0,26):C.UVGC_266_414,(0,0,27):C.UVGC_266_415,(0,0,28):C.UVGC_266_416,(0,0,29):C.UVGC_266_417,(0,0,30):C.UVGC_266_418,(0,0,31):C.UVGC_266_419,(0,0,32):C.UVGC_266_420,(0,0,5):C.UVGC_410_743,(0,1,0):C.UVGC_240_336,(0,1,1):C.UVGC_240_337,(0,1,2):C.UVGC_240_338,(0,1,3):C.UVGC_240_339,(0,1,4):C.UVGC_240_340,(0,1,6):C.UVGC_240_341,(0,1,7):C.UVGC_240_342,(0,1,8):C.UVGC_240_343,(0,1,9):C.UVGC_240_344,(0,1,10):C.UVGC_240_345,(0,1,11):C.UVGC_240_346,(0,1,12):C.UVGC_240_347,(0,1,13):C.UVGC_240_348,(0,1,14):C.UVGC_240_349,(0,1,15):C.UVGC_240_350,(0,1,16):C.UVGC_240_351,(0,1,17):C.UVGC_240_352,(0,1,18):C.UVGC_240_353,(0,1,19):C.UVGC_240_354,(0,1,20):C.UVGC_240_355,(0,1,21):C.UVGC_240_356,(0,1,22):C.UVGC_240_357,(0,1,23):C.UVGC_240_358,(0,1,24):C.UVGC_240_359,(0,1,25):C.UVGC_240_360,(0,1,26):C.UVGC_240_361,(0,1,27):C.UVGC_240_362,(0,1,28):C.UVGC_240_363,(0,1,29):C.UVGC_240_364,(0,1,30):C.UVGC_240_365,(0,1,31):C.UVGC_240_366,(0,1,32):C.UVGC_240_367,(0,1,5):C.UVGC_409_742})

V_681 = CTVertex(name = 'V_681',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.Xd, P.YS3u1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YS3u1] ], [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_774_1072,(0,0,2):C.UVGC_774_1073,(0,0,1):C.UVGC_774_1074})

V_682 = CTVertex(name = 'V_682',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.Xm, P.YS3u1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YS3u1] ], [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_774_1072,(0,0,2):C.UVGC_774_1073,(0,0,1):C.UVGC_774_1074})

V_683 = CTVertex(name = 'V_683',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_408_741})

V_684 = CTVertex(name = 'V_684',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_363_638,(0,0,1):C.UVGC_363_639,(0,0,2):C.UVGC_363_640,(0,0,3):C.UVGC_363_641,(0,0,4):C.UVGC_363_642,(0,0,6):C.UVGC_363_643,(0,0,7):C.UVGC_363_644,(0,0,8):C.UVGC_363_645,(0,0,9):C.UVGC_363_646,(0,0,10):C.UVGC_363_647,(0,0,11):C.UVGC_363_648,(0,0,12):C.UVGC_363_649,(0,0,13):C.UVGC_363_650,(0,0,14):C.UVGC_363_651,(0,0,15):C.UVGC_363_652,(0,0,16):C.UVGC_363_653,(0,0,17):C.UVGC_363_654,(0,0,18):C.UVGC_363_655,(0,0,19):C.UVGC_363_656,(0,0,20):C.UVGC_363_657,(0,0,21):C.UVGC_363_658,(0,0,22):C.UVGC_363_659,(0,0,23):C.UVGC_363_660,(0,0,24):C.UVGC_363_661,(0,0,25):C.UVGC_363_662,(0,0,26):C.UVGC_363_663,(0,0,27):C.UVGC_363_664,(0,0,28):C.UVGC_363_665,(0,0,29):C.UVGC_363_666,(0,0,30):C.UVGC_363_667,(0,0,31):C.UVGC_363_668,(0,0,32):C.UVGC_363_669,(0,0,5):C.UVGC_411_744})

V_685 = CTVertex(name = 'V_685',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_270_459,(2,0,1):C.UVGC_270_460,(2,0,2):C.UVGC_270_461,(2,0,3):C.UVGC_270_462,(2,0,4):C.UVGC_270_463,(2,0,6):C.UVGC_270_464,(2,0,7):C.UVGC_270_465,(2,0,8):C.UVGC_270_466,(2,0,9):C.UVGC_270_467,(2,0,10):C.UVGC_270_468,(2,0,11):C.UVGC_270_469,(2,0,12):C.UVGC_270_470,(2,0,13):C.UVGC_270_471,(2,0,14):C.UVGC_270_472,(2,0,15):C.UVGC_270_473,(2,0,16):C.UVGC_270_474,(2,0,17):C.UVGC_270_475,(2,0,18):C.UVGC_270_476,(2,0,19):C.UVGC_270_477,(2,0,20):C.UVGC_270_478,(2,0,21):C.UVGC_270_479,(2,0,22):C.UVGC_270_480,(2,0,23):C.UVGC_270_481,(2,0,24):C.UVGC_270_482,(2,0,25):C.UVGC_270_483,(2,0,26):C.UVGC_270_484,(2,0,27):C.UVGC_270_485,(2,0,28):C.UVGC_270_486,(2,0,29):C.UVGC_270_487,(2,0,30):C.UVGC_270_488,(2,0,31):C.UVGC_270_489,(2,0,32):C.UVGC_270_490,(2,0,5):C.UVGC_414_745,(1,0,0):C.UVGC_270_459,(1,0,1):C.UVGC_270_460,(1,0,2):C.UVGC_270_461,(1,0,3):C.UVGC_270_462,(1,0,4):C.UVGC_270_463,(1,0,6):C.UVGC_270_464,(1,0,7):C.UVGC_270_465,(1,0,8):C.UVGC_270_466,(1,0,9):C.UVGC_270_467,(1,0,10):C.UVGC_270_468,(1,0,11):C.UVGC_270_469,(1,0,12):C.UVGC_270_470,(1,0,13):C.UVGC_270_471,(1,0,14):C.UVGC_270_472,(1,0,15):C.UVGC_270_473,(1,0,16):C.UVGC_270_474,(1,0,17):C.UVGC_270_475,(1,0,18):C.UVGC_270_476,(1,0,19):C.UVGC_270_477,(1,0,20):C.UVGC_270_478,(1,0,21):C.UVGC_270_479,(1,0,22):C.UVGC_270_480,(1,0,23):C.UVGC_270_481,(1,0,24):C.UVGC_270_482,(1,0,25):C.UVGC_270_483,(1,0,26):C.UVGC_270_484,(1,0,27):C.UVGC_270_485,(1,0,28):C.UVGC_270_486,(1,0,29):C.UVGC_270_487,(1,0,30):C.UVGC_270_488,(1,0,31):C.UVGC_270_489,(1,0,32):C.UVGC_270_490,(1,0,5):C.UVGC_414_745,(0,0,3):C.UVGC_269_457,(0,0,5):C.UVGC_269_458})

V_686 = CTVertex(name = 'V_686',
                 type = 'UV',
                 particles = [ P.a, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_422_785,(0,1,0):C.UVGC_423_786})

V_687 = CTVertex(name = 'V_687',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.c, P.YS3u2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YS3u2] ], [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_586_910,(0,0,2):C.UVGC_586_911,(0,0,1):C.UVGC_586_912})

V_688 = CTVertex(name = 'V_688',
                 type = 'UV',
                 particles = [ P.Xm, P.c, P.YS3u2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YS3u2] ], [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_586_910,(0,0,2):C.UVGC_586_911,(0,0,1):C.UVGC_586_912})

V_689 = CTVertex(name = 'V_689',
                 type = 'UV',
                 particles = [ P.g, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_266_389,(0,0,1):C.UVGC_266_390,(0,0,2):C.UVGC_266_391,(0,0,3):C.UVGC_266_392,(0,0,4):C.UVGC_266_393,(0,0,6):C.UVGC_266_394,(0,0,7):C.UVGC_266_395,(0,0,8):C.UVGC_266_396,(0,0,9):C.UVGC_266_397,(0,0,10):C.UVGC_266_398,(0,0,11):C.UVGC_266_399,(0,0,12):C.UVGC_266_400,(0,0,13):C.UVGC_266_401,(0,0,14):C.UVGC_266_402,(0,0,15):C.UVGC_266_403,(0,0,16):C.UVGC_266_404,(0,0,17):C.UVGC_266_405,(0,0,18):C.UVGC_266_406,(0,0,19):C.UVGC_266_407,(0,0,20):C.UVGC_266_408,(0,0,21):C.UVGC_266_409,(0,0,22):C.UVGC_266_410,(0,0,23):C.UVGC_266_411,(0,0,24):C.UVGC_266_412,(0,0,25):C.UVGC_266_413,(0,0,26):C.UVGC_266_414,(0,0,27):C.UVGC_266_415,(0,0,28):C.UVGC_266_416,(0,0,29):C.UVGC_266_417,(0,0,30):C.UVGC_266_418,(0,0,31):C.UVGC_266_419,(0,0,32):C.UVGC_266_420,(0,0,5):C.UVGC_426_789,(0,1,0):C.UVGC_240_336,(0,1,1):C.UVGC_240_337,(0,1,2):C.UVGC_240_338,(0,1,3):C.UVGC_240_339,(0,1,4):C.UVGC_240_340,(0,1,6):C.UVGC_240_341,(0,1,7):C.UVGC_240_342,(0,1,8):C.UVGC_240_343,(0,1,9):C.UVGC_240_344,(0,1,10):C.UVGC_240_345,(0,1,11):C.UVGC_240_346,(0,1,12):C.UVGC_240_347,(0,1,13):C.UVGC_240_348,(0,1,14):C.UVGC_240_349,(0,1,15):C.UVGC_240_350,(0,1,16):C.UVGC_240_351,(0,1,17):C.UVGC_240_352,(0,1,18):C.UVGC_240_353,(0,1,19):C.UVGC_240_354,(0,1,20):C.UVGC_240_355,(0,1,21):C.UVGC_240_356,(0,1,22):C.UVGC_240_357,(0,1,23):C.UVGC_240_358,(0,1,24):C.UVGC_240_359,(0,1,25):C.UVGC_240_360,(0,1,26):C.UVGC_240_361,(0,1,27):C.UVGC_240_362,(0,1,28):C.UVGC_240_363,(0,1,29):C.UVGC_240_364,(0,1,30):C.UVGC_240_365,(0,1,31):C.UVGC_240_366,(0,1,32):C.UVGC_240_367,(0,1,5):C.UVGC_425_788})

V_690 = CTVertex(name = 'V_690',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.Xd, P.YS3u2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YS3u2] ], [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_586_910,(0,0,2):C.UVGC_586_911,(0,0,1):C.UVGC_586_912})

V_691 = CTVertex(name = 'V_691',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.Xm, P.YS3u2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YS3u2] ], [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_586_910,(0,0,2):C.UVGC_586_911,(0,0,1):C.UVGC_586_912})

V_692 = CTVertex(name = 'V_692',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_424_787})

V_693 = CTVertex(name = 'V_693',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_363_638,(0,0,1):C.UVGC_363_639,(0,0,2):C.UVGC_363_640,(0,0,3):C.UVGC_363_641,(0,0,4):C.UVGC_363_642,(0,0,6):C.UVGC_363_643,(0,0,7):C.UVGC_363_644,(0,0,8):C.UVGC_363_645,(0,0,9):C.UVGC_363_646,(0,0,10):C.UVGC_363_647,(0,0,11):C.UVGC_363_648,(0,0,12):C.UVGC_363_649,(0,0,13):C.UVGC_363_650,(0,0,14):C.UVGC_363_651,(0,0,15):C.UVGC_363_652,(0,0,16):C.UVGC_363_653,(0,0,17):C.UVGC_363_654,(0,0,18):C.UVGC_363_655,(0,0,19):C.UVGC_363_656,(0,0,20):C.UVGC_363_657,(0,0,21):C.UVGC_363_658,(0,0,22):C.UVGC_363_659,(0,0,23):C.UVGC_363_660,(0,0,24):C.UVGC_363_661,(0,0,25):C.UVGC_363_662,(0,0,26):C.UVGC_363_663,(0,0,27):C.UVGC_363_664,(0,0,28):C.UVGC_363_665,(0,0,29):C.UVGC_363_666,(0,0,30):C.UVGC_363_667,(0,0,31):C.UVGC_363_668,(0,0,32):C.UVGC_363_669,(0,0,5):C.UVGC_427_790})

V_694 = CTVertex(name = 'V_694',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_270_459,(2,0,1):C.UVGC_270_460,(2,0,2):C.UVGC_270_461,(2,0,3):C.UVGC_270_462,(2,0,4):C.UVGC_270_463,(2,0,6):C.UVGC_270_464,(2,0,7):C.UVGC_270_465,(2,0,8):C.UVGC_270_466,(2,0,9):C.UVGC_270_467,(2,0,10):C.UVGC_270_468,(2,0,11):C.UVGC_270_469,(2,0,12):C.UVGC_270_470,(2,0,13):C.UVGC_270_471,(2,0,14):C.UVGC_270_472,(2,0,15):C.UVGC_270_473,(2,0,16):C.UVGC_270_474,(2,0,17):C.UVGC_270_475,(2,0,18):C.UVGC_270_476,(2,0,19):C.UVGC_270_477,(2,0,20):C.UVGC_270_478,(2,0,21):C.UVGC_270_479,(2,0,22):C.UVGC_270_480,(2,0,23):C.UVGC_270_481,(2,0,24):C.UVGC_270_482,(2,0,25):C.UVGC_270_483,(2,0,26):C.UVGC_270_484,(2,0,27):C.UVGC_270_485,(2,0,28):C.UVGC_270_486,(2,0,29):C.UVGC_270_487,(2,0,30):C.UVGC_270_488,(2,0,31):C.UVGC_270_489,(2,0,32):C.UVGC_270_490,(2,0,5):C.UVGC_430_791,(1,0,0):C.UVGC_270_459,(1,0,1):C.UVGC_270_460,(1,0,2):C.UVGC_270_461,(1,0,3):C.UVGC_270_462,(1,0,4):C.UVGC_270_463,(1,0,6):C.UVGC_270_464,(1,0,7):C.UVGC_270_465,(1,0,8):C.UVGC_270_466,(1,0,9):C.UVGC_270_467,(1,0,10):C.UVGC_270_468,(1,0,11):C.UVGC_270_469,(1,0,12):C.UVGC_270_470,(1,0,13):C.UVGC_270_471,(1,0,14):C.UVGC_270_472,(1,0,15):C.UVGC_270_473,(1,0,16):C.UVGC_270_474,(1,0,17):C.UVGC_270_475,(1,0,18):C.UVGC_270_476,(1,0,19):C.UVGC_270_477,(1,0,20):C.UVGC_270_478,(1,0,21):C.UVGC_270_479,(1,0,22):C.UVGC_270_480,(1,0,23):C.UVGC_270_481,(1,0,24):C.UVGC_270_482,(1,0,25):C.UVGC_270_483,(1,0,26):C.UVGC_270_484,(1,0,27):C.UVGC_270_485,(1,0,28):C.UVGC_270_486,(1,0,29):C.UVGC_270_487,(1,0,30):C.UVGC_270_488,(1,0,31):C.UVGC_270_489,(1,0,32):C.UVGC_270_490,(1,0,5):C.UVGC_430_791,(0,0,3):C.UVGC_269_457,(0,0,5):C.UVGC_269_458})

V_695 = CTVertex(name = 'V_695',
                 type = 'UV',
                 particles = [ P.a, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_438_799,(0,1,0):C.UVGC_439_800})

V_696 = CTVertex(name = 'V_696',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.t, P.YS3u3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YS3u3] ], [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_767_1057,(0,0,2):C.UVGC_767_1058,(0,0,1):C.UVGC_767_1059})

V_697 = CTVertex(name = 'V_697',
                 type = 'UV',
                 particles = [ P.Xm, P.t, P.YS3u3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YS3u3] ], [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_767_1057,(0,0,2):C.UVGC_767_1058,(0,0,1):C.UVGC_767_1059})

V_698 = CTVertex(name = 'V_698',
                 type = 'UV',
                 particles = [ P.g, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_266_389,(0,0,1):C.UVGC_266_390,(0,0,2):C.UVGC_266_391,(0,0,3):C.UVGC_266_392,(0,0,4):C.UVGC_266_393,(0,0,6):C.UVGC_266_394,(0,0,7):C.UVGC_266_395,(0,0,8):C.UVGC_266_396,(0,0,9):C.UVGC_266_397,(0,0,10):C.UVGC_266_398,(0,0,11):C.UVGC_266_399,(0,0,12):C.UVGC_266_400,(0,0,13):C.UVGC_266_401,(0,0,14):C.UVGC_266_402,(0,0,15):C.UVGC_266_403,(0,0,16):C.UVGC_266_404,(0,0,17):C.UVGC_266_405,(0,0,18):C.UVGC_266_406,(0,0,19):C.UVGC_266_407,(0,0,20):C.UVGC_266_408,(0,0,21):C.UVGC_266_409,(0,0,22):C.UVGC_266_410,(0,0,23):C.UVGC_266_411,(0,0,24):C.UVGC_266_412,(0,0,25):C.UVGC_266_413,(0,0,26):C.UVGC_266_414,(0,0,27):C.UVGC_266_415,(0,0,28):C.UVGC_266_416,(0,0,29):C.UVGC_266_417,(0,0,30):C.UVGC_266_418,(0,0,31):C.UVGC_266_419,(0,0,32):C.UVGC_266_420,(0,0,5):C.UVGC_442_803,(0,1,0):C.UVGC_240_336,(0,1,1):C.UVGC_240_337,(0,1,2):C.UVGC_240_338,(0,1,3):C.UVGC_240_339,(0,1,4):C.UVGC_240_340,(0,1,6):C.UVGC_240_341,(0,1,7):C.UVGC_240_342,(0,1,8):C.UVGC_240_343,(0,1,9):C.UVGC_240_344,(0,1,10):C.UVGC_240_345,(0,1,11):C.UVGC_240_346,(0,1,12):C.UVGC_240_347,(0,1,13):C.UVGC_240_348,(0,1,14):C.UVGC_240_349,(0,1,15):C.UVGC_240_350,(0,1,16):C.UVGC_240_351,(0,1,17):C.UVGC_240_352,(0,1,18):C.UVGC_240_353,(0,1,19):C.UVGC_240_354,(0,1,20):C.UVGC_240_355,(0,1,21):C.UVGC_240_356,(0,1,22):C.UVGC_240_357,(0,1,23):C.UVGC_240_358,(0,1,24):C.UVGC_240_359,(0,1,25):C.UVGC_240_360,(0,1,26):C.UVGC_240_361,(0,1,27):C.UVGC_240_362,(0,1,28):C.UVGC_240_363,(0,1,29):C.UVGC_240_364,(0,1,30):C.UVGC_240_365,(0,1,31):C.UVGC_240_366,(0,1,32):C.UVGC_240_367,(0,1,5):C.UVGC_441_802})

V_699 = CTVertex(name = 'V_699',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.Xd, P.YS3u3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YS3u3] ], [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_767_1057,(0,0,2):C.UVGC_767_1058,(0,0,1):C.UVGC_767_1059})

V_700 = CTVertex(name = 'V_700',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.Xm, P.YS3u3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YS3u3] ], [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_767_1057,(0,0,2):C.UVGC_767_1058,(0,0,1):C.UVGC_767_1059})

V_701 = CTVertex(name = 'V_701',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_440_801})

V_702 = CTVertex(name = 'V_702',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_363_638,(0,0,1):C.UVGC_363_639,(0,0,2):C.UVGC_363_640,(0,0,3):C.UVGC_363_641,(0,0,4):C.UVGC_363_642,(0,0,6):C.UVGC_363_643,(0,0,7):C.UVGC_363_644,(0,0,8):C.UVGC_363_645,(0,0,9):C.UVGC_363_646,(0,0,10):C.UVGC_363_647,(0,0,11):C.UVGC_363_648,(0,0,12):C.UVGC_363_649,(0,0,13):C.UVGC_363_650,(0,0,14):C.UVGC_363_651,(0,0,15):C.UVGC_363_652,(0,0,16):C.UVGC_363_653,(0,0,17):C.UVGC_363_654,(0,0,18):C.UVGC_363_655,(0,0,19):C.UVGC_363_656,(0,0,20):C.UVGC_363_657,(0,0,21):C.UVGC_363_658,(0,0,22):C.UVGC_363_659,(0,0,23):C.UVGC_363_660,(0,0,24):C.UVGC_363_661,(0,0,25):C.UVGC_363_662,(0,0,26):C.UVGC_363_663,(0,0,27):C.UVGC_363_664,(0,0,28):C.UVGC_363_665,(0,0,29):C.UVGC_363_666,(0,0,30):C.UVGC_363_667,(0,0,31):C.UVGC_363_668,(0,0,32):C.UVGC_363_669,(0,0,5):C.UVGC_443_804})

V_703 = CTVertex(name = 'V_703',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_270_459,(2,0,1):C.UVGC_270_460,(2,0,2):C.UVGC_270_461,(2,0,3):C.UVGC_270_462,(2,0,4):C.UVGC_270_463,(2,0,6):C.UVGC_270_464,(2,0,7):C.UVGC_270_465,(2,0,8):C.UVGC_270_466,(2,0,9):C.UVGC_270_467,(2,0,10):C.UVGC_270_468,(2,0,11):C.UVGC_270_469,(2,0,12):C.UVGC_270_470,(2,0,13):C.UVGC_270_471,(2,0,14):C.UVGC_270_472,(2,0,15):C.UVGC_270_473,(2,0,16):C.UVGC_270_474,(2,0,17):C.UVGC_270_475,(2,0,18):C.UVGC_270_476,(2,0,19):C.UVGC_270_477,(2,0,20):C.UVGC_270_478,(2,0,21):C.UVGC_270_479,(2,0,22):C.UVGC_270_480,(2,0,23):C.UVGC_270_481,(2,0,24):C.UVGC_270_482,(2,0,25):C.UVGC_270_483,(2,0,26):C.UVGC_270_484,(2,0,27):C.UVGC_270_485,(2,0,28):C.UVGC_270_486,(2,0,29):C.UVGC_270_487,(2,0,30):C.UVGC_270_488,(2,0,31):C.UVGC_270_489,(2,0,32):C.UVGC_270_490,(2,0,5):C.UVGC_446_805,(1,0,0):C.UVGC_270_459,(1,0,1):C.UVGC_270_460,(1,0,2):C.UVGC_270_461,(1,0,3):C.UVGC_270_462,(1,0,4):C.UVGC_270_463,(1,0,6):C.UVGC_270_464,(1,0,7):C.UVGC_270_465,(1,0,8):C.UVGC_270_466,(1,0,9):C.UVGC_270_467,(1,0,10):C.UVGC_270_468,(1,0,11):C.UVGC_270_469,(1,0,12):C.UVGC_270_470,(1,0,13):C.UVGC_270_471,(1,0,14):C.UVGC_270_472,(1,0,15):C.UVGC_270_473,(1,0,16):C.UVGC_270_474,(1,0,17):C.UVGC_270_475,(1,0,18):C.UVGC_270_476,(1,0,19):C.UVGC_270_477,(1,0,20):C.UVGC_270_478,(1,0,21):C.UVGC_270_479,(1,0,22):C.UVGC_270_480,(1,0,23):C.UVGC_270_481,(1,0,24):C.UVGC_270_482,(1,0,25):C.UVGC_270_483,(1,0,26):C.UVGC_270_484,(1,0,27):C.UVGC_270_485,(1,0,28):C.UVGC_270_486,(1,0,29):C.UVGC_270_487,(1,0,30):C.UVGC_270_488,(1,0,31):C.UVGC_270_489,(1,0,32):C.UVGC_270_490,(1,0,5):C.UVGC_446_805,(0,0,3):C.UVGC_269_457,(0,0,5):C.UVGC_269_458})

V_704 = CTVertex(name = 'V_704',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_765_1052,(0,0,2):C.UVGC_765_1053,(0,0,1):C.UVGC_765_1054})

V_705 = CTVertex(name = 'V_705',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.YF3Qd1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_506_842,(0,1,0):C.UVGC_504_840,(0,2,0):C.UVGC_505_841})

V_706 = CTVertex(name = 'V_706',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.YF3Qd2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_506_842,(0,1,0):C.UVGC_513_846,(0,2,0):C.UVGC_514_847})

V_707 = CTVertex(name = 'V_707',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.YF3Qd3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_506_842,(0,1,0):C.UVGC_522_851,(0,2,0):C.UVGC_523_852})

V_708 = CTVertex(name = 'V_708',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.YF3Qu1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_535_862,(0,1,0):C.UVGC_533_860,(0,2,0):C.UVGC_534_861})

V_709 = CTVertex(name = 'V_709',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.YF3Qu2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_535_862,(0,1,0):C.UVGC_544_870,(0,2,0):C.UVGC_545_871})

V_710 = CTVertex(name = 'V_710',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.YF3Qu3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_535_862,(0,1,0):C.UVGC_555_879,(0,2,0):C.UVGC_556_880})

V_711 = CTVertex(name = 'V_711',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.YF3d1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_483_830,(0,1,0):C.UVGC_168_31,(0,2,0):C.UVGC_169_32})

V_712 = CTVertex(name = 'V_712',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.YF3d2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_483_830,(0,1,0):C.UVGC_174_37,(0,2,0):C.UVGC_175_38})

V_713 = CTVertex(name = 'V_713',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.YF3d3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_483_830,(0,1,0):C.UVGC_180_43,(0,2,0):C.UVGC_181_44})

V_714 = CTVertex(name = 'V_714',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.YF3u1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_564_884,(0,1,0):C.UVGC_210_73,(0,2,0):C.UVGC_211_74})

V_715 = CTVertex(name = 'V_715',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.YF3u2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_564_884,(0,1,0):C.UVGC_216_79,(0,2,0):C.UVGC_217_80})

V_716 = CTVertex(name = 'V_716',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.YF3u3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_564_884,(0,1,0):C.UVGC_222_85,(0,2,0):C.UVGC_223_86})

V_717 = CTVertex(name = 'V_717',
                 type = 'UV',
                 particles = [ P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_272_493,(0,1,0):C.UVGC_273_494})

V_718 = CTVertex(name = 'V_718',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_274_495})

V_719 = CTVertex(name = 'V_719',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_275_496,(0,0,1):C.UVGC_275_497,(0,0,2):C.UVGC_275_498,(0,0,3):C.UVGC_275_499,(0,0,4):C.UVGC_275_500,(0,0,6):C.UVGC_275_501,(0,0,7):C.UVGC_275_502,(0,0,8):C.UVGC_275_503,(0,0,9):C.UVGC_275_504,(0,0,10):C.UVGC_275_505,(0,0,11):C.UVGC_275_506,(0,0,12):C.UVGC_275_507,(0,0,13):C.UVGC_275_508,(0,0,14):C.UVGC_275_509,(0,0,15):C.UVGC_275_510,(0,0,16):C.UVGC_275_511,(0,0,17):C.UVGC_275_512,(0,0,18):C.UVGC_275_513,(0,0,19):C.UVGC_275_514,(0,0,20):C.UVGC_275_515,(0,0,21):C.UVGC_275_516,(0,0,22):C.UVGC_275_517,(0,0,23):C.UVGC_275_518,(0,0,24):C.UVGC_275_519,(0,0,25):C.UVGC_275_520,(0,0,26):C.UVGC_275_521,(0,0,27):C.UVGC_275_522,(0,0,28):C.UVGC_275_523,(0,0,29):C.UVGC_275_524,(0,0,30):C.UVGC_275_525,(0,0,31):C.UVGC_275_526,(0,0,32):C.UVGC_275_527,(0,0,5):C.UVGC_275_528})

V_720 = CTVertex(name = 'V_720',
                 type = 'UV',
                 particles = [ P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_288_539,(0,1,0):C.UVGC_289_540})

V_721 = CTVertex(name = 'V_721',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_290_541})

V_722 = CTVertex(name = 'V_722',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_275_496,(0,0,1):C.UVGC_275_497,(0,0,2):C.UVGC_275_498,(0,0,3):C.UVGC_275_499,(0,0,4):C.UVGC_275_500,(0,0,6):C.UVGC_275_501,(0,0,7):C.UVGC_275_502,(0,0,8):C.UVGC_275_503,(0,0,9):C.UVGC_275_504,(0,0,10):C.UVGC_275_505,(0,0,11):C.UVGC_275_506,(0,0,12):C.UVGC_275_507,(0,0,13):C.UVGC_275_508,(0,0,14):C.UVGC_275_509,(0,0,15):C.UVGC_275_510,(0,0,16):C.UVGC_275_511,(0,0,17):C.UVGC_275_512,(0,0,18):C.UVGC_275_513,(0,0,19):C.UVGC_275_514,(0,0,20):C.UVGC_275_515,(0,0,21):C.UVGC_275_516,(0,0,22):C.UVGC_275_517,(0,0,23):C.UVGC_275_518,(0,0,24):C.UVGC_275_519,(0,0,25):C.UVGC_275_520,(0,0,26):C.UVGC_275_521,(0,0,27):C.UVGC_275_522,(0,0,28):C.UVGC_275_523,(0,0,29):C.UVGC_275_524,(0,0,30):C.UVGC_275_525,(0,0,31):C.UVGC_275_526,(0,0,32):C.UVGC_275_527,(0,0,5):C.UVGC_291_542})

V_723 = CTVertex(name = 'V_723',
                 type = 'UV',
                 particles = [ P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_304_553,(0,1,0):C.UVGC_305_554})

V_724 = CTVertex(name = 'V_724',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_306_555})

V_725 = CTVertex(name = 'V_725',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_275_496,(0,0,1):C.UVGC_275_497,(0,0,2):C.UVGC_275_498,(0,0,3):C.UVGC_275_499,(0,0,4):C.UVGC_275_500,(0,0,6):C.UVGC_275_501,(0,0,7):C.UVGC_275_502,(0,0,8):C.UVGC_275_503,(0,0,9):C.UVGC_275_504,(0,0,10):C.UVGC_275_505,(0,0,11):C.UVGC_275_506,(0,0,12):C.UVGC_275_507,(0,0,13):C.UVGC_275_508,(0,0,14):C.UVGC_275_509,(0,0,15):C.UVGC_275_510,(0,0,16):C.UVGC_275_511,(0,0,17):C.UVGC_275_512,(0,0,18):C.UVGC_275_513,(0,0,19):C.UVGC_275_514,(0,0,20):C.UVGC_275_515,(0,0,21):C.UVGC_275_516,(0,0,22):C.UVGC_275_517,(0,0,23):C.UVGC_275_518,(0,0,24):C.UVGC_275_519,(0,0,25):C.UVGC_275_520,(0,0,26):C.UVGC_275_521,(0,0,27):C.UVGC_275_522,(0,0,28):C.UVGC_275_523,(0,0,29):C.UVGC_275_524,(0,0,30):C.UVGC_275_525,(0,0,31):C.UVGC_275_526,(0,0,32):C.UVGC_275_527,(0,0,5):C.UVGC_307_556})

V_726 = CTVertex(name = 'V_726',
                 type = 'UV',
                 particles = [ P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_321_568,(0,1,0):C.UVGC_320_567})

V_727 = CTVertex(name = 'V_727',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_322_569})

V_728 = CTVertex(name = 'V_728',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_323_570,(0,0,1):C.UVGC_323_571,(0,0,2):C.UVGC_323_572,(0,0,3):C.UVGC_323_573,(0,0,4):C.UVGC_323_574,(0,0,6):C.UVGC_323_575,(0,0,7):C.UVGC_323_576,(0,0,8):C.UVGC_323_577,(0,0,9):C.UVGC_323_578,(0,0,10):C.UVGC_323_579,(0,0,11):C.UVGC_323_580,(0,0,12):C.UVGC_323_581,(0,0,13):C.UVGC_323_582,(0,0,14):C.UVGC_323_583,(0,0,15):C.UVGC_323_584,(0,0,16):C.UVGC_323_585,(0,0,17):C.UVGC_323_586,(0,0,18):C.UVGC_323_587,(0,0,19):C.UVGC_323_588,(0,0,20):C.UVGC_323_589,(0,0,21):C.UVGC_323_590,(0,0,22):C.UVGC_323_591,(0,0,23):C.UVGC_323_592,(0,0,24):C.UVGC_323_593,(0,0,25):C.UVGC_323_594,(0,0,26):C.UVGC_323_595,(0,0,27):C.UVGC_323_596,(0,0,28):C.UVGC_323_597,(0,0,29):C.UVGC_323_598,(0,0,30):C.UVGC_323_599,(0,0,31):C.UVGC_323_600,(0,0,32):C.UVGC_323_601,(0,0,5):C.UVGC_323_602})

V_729 = CTVertex(name = 'V_729',
                 type = 'UV',
                 particles = [ P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_337_614,(0,1,0):C.UVGC_336_613})

V_730 = CTVertex(name = 'V_730',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_338_615})

V_731 = CTVertex(name = 'V_731',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_323_570,(0,0,1):C.UVGC_323_571,(0,0,2):C.UVGC_323_572,(0,0,3):C.UVGC_323_573,(0,0,4):C.UVGC_323_574,(0,0,6):C.UVGC_323_575,(0,0,7):C.UVGC_323_576,(0,0,8):C.UVGC_323_577,(0,0,9):C.UVGC_323_578,(0,0,10):C.UVGC_323_579,(0,0,11):C.UVGC_323_580,(0,0,12):C.UVGC_323_581,(0,0,13):C.UVGC_323_582,(0,0,14):C.UVGC_323_583,(0,0,15):C.UVGC_323_584,(0,0,16):C.UVGC_323_585,(0,0,17):C.UVGC_323_586,(0,0,18):C.UVGC_323_587,(0,0,19):C.UVGC_323_588,(0,0,20):C.UVGC_323_589,(0,0,21):C.UVGC_323_590,(0,0,22):C.UVGC_323_591,(0,0,23):C.UVGC_323_592,(0,0,24):C.UVGC_323_593,(0,0,25):C.UVGC_323_594,(0,0,26):C.UVGC_323_595,(0,0,27):C.UVGC_323_596,(0,0,28):C.UVGC_323_597,(0,0,29):C.UVGC_323_598,(0,0,30):C.UVGC_323_599,(0,0,31):C.UVGC_323_600,(0,0,32):C.UVGC_323_601,(0,0,5):C.UVGC_339_616})

V_732 = CTVertex(name = 'V_732',
                 type = 'UV',
                 particles = [ P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_353_628,(0,1,0):C.UVGC_352_627})

V_733 = CTVertex(name = 'V_733',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_354_629})

V_734 = CTVertex(name = 'V_734',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_323_570,(0,0,1):C.UVGC_323_571,(0,0,2):C.UVGC_323_572,(0,0,3):C.UVGC_323_573,(0,0,4):C.UVGC_323_574,(0,0,6):C.UVGC_323_575,(0,0,7):C.UVGC_323_576,(0,0,8):C.UVGC_323_577,(0,0,9):C.UVGC_323_578,(0,0,10):C.UVGC_323_579,(0,0,11):C.UVGC_323_580,(0,0,12):C.UVGC_323_581,(0,0,13):C.UVGC_323_582,(0,0,14):C.UVGC_323_583,(0,0,15):C.UVGC_323_584,(0,0,16):C.UVGC_323_585,(0,0,17):C.UVGC_323_586,(0,0,18):C.UVGC_323_587,(0,0,19):C.UVGC_323_588,(0,0,20):C.UVGC_323_589,(0,0,21):C.UVGC_323_590,(0,0,22):C.UVGC_323_591,(0,0,23):C.UVGC_323_592,(0,0,24):C.UVGC_323_593,(0,0,25):C.UVGC_323_594,(0,0,26):C.UVGC_323_595,(0,0,27):C.UVGC_323_596,(0,0,28):C.UVGC_323_597,(0,0,29):C.UVGC_323_598,(0,0,30):C.UVGC_323_599,(0,0,31):C.UVGC_323_600,(0,0,32):C.UVGC_323_601,(0,0,5):C.UVGC_355_630})

V_735 = CTVertex(name = 'V_735',
                 type = 'UV',
                 particles = [ P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_369_674,(0,1,0):C.UVGC_368_673})

V_736 = CTVertex(name = 'V_736',
                 type = 'UV',
                 particles = [ P.W__plus__, P.Z, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_652_948,(0,0,2):C.UVGC_652_949,(0,0,1):C.UVGC_652_950})

V_737 = CTVertex(name = 'V_737',
                 type = 'UV',
                 particles = [ P.W__minus__, P.Z, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_652_948,(0,0,2):C.UVGC_652_949,(0,0,1):C.UVGC_652_950})

V_738 = CTVertex(name = 'V_738',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_370_675})

V_739 = CTVertex(name = 'V_739',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_371_676,(0,0,1):C.UVGC_371_677,(0,0,2):C.UVGC_371_678,(0,0,3):C.UVGC_371_679,(0,0,4):C.UVGC_371_680,(0,0,6):C.UVGC_371_681,(0,0,7):C.UVGC_371_682,(0,0,8):C.UVGC_371_683,(0,0,9):C.UVGC_371_684,(0,0,10):C.UVGC_371_685,(0,0,11):C.UVGC_371_686,(0,0,12):C.UVGC_371_687,(0,0,13):C.UVGC_371_688,(0,0,14):C.UVGC_371_689,(0,0,15):C.UVGC_371_690,(0,0,16):C.UVGC_371_691,(0,0,17):C.UVGC_371_692,(0,0,18):C.UVGC_371_693,(0,0,19):C.UVGC_371_694,(0,0,20):C.UVGC_371_695,(0,0,21):C.UVGC_371_696,(0,0,22):C.UVGC_371_697,(0,0,23):C.UVGC_371_698,(0,0,24):C.UVGC_371_699,(0,0,25):C.UVGC_371_700,(0,0,26):C.UVGC_371_701,(0,0,27):C.UVGC_371_702,(0,0,28):C.UVGC_371_703,(0,0,29):C.UVGC_371_704,(0,0,30):C.UVGC_371_705,(0,0,31):C.UVGC_371_706,(0,0,32):C.UVGC_371_707,(0,0,5):C.UVGC_371_708})

V_740 = CTVertex(name = 'V_740',
                 type = 'UV',
                 particles = [ P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_385_720,(0,1,0):C.UVGC_384_719})

V_741 = CTVertex(name = 'V_741',
                 type = 'UV',
                 particles = [ P.W__plus__, P.Z, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_685_1002,(0,0,2):C.UVGC_685_1003,(0,0,1):C.UVGC_652_950})

V_742 = CTVertex(name = 'V_742',
                 type = 'UV',
                 particles = [ P.W__minus__, P.Z, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_685_1002,(0,0,2):C.UVGC_685_1003,(0,0,1):C.UVGC_652_950})

V_743 = CTVertex(name = 'V_743',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_386_721})

V_744 = CTVertex(name = 'V_744',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_371_676,(0,0,1):C.UVGC_371_677,(0,0,2):C.UVGC_371_678,(0,0,3):C.UVGC_371_679,(0,0,4):C.UVGC_371_680,(0,0,6):C.UVGC_371_681,(0,0,7):C.UVGC_371_682,(0,0,8):C.UVGC_371_683,(0,0,9):C.UVGC_371_684,(0,0,10):C.UVGC_371_685,(0,0,11):C.UVGC_371_686,(0,0,12):C.UVGC_371_687,(0,0,13):C.UVGC_371_688,(0,0,14):C.UVGC_371_689,(0,0,15):C.UVGC_371_690,(0,0,16):C.UVGC_371_691,(0,0,17):C.UVGC_371_692,(0,0,18):C.UVGC_371_693,(0,0,19):C.UVGC_371_694,(0,0,20):C.UVGC_371_695,(0,0,21):C.UVGC_371_696,(0,0,22):C.UVGC_371_697,(0,0,23):C.UVGC_371_698,(0,0,24):C.UVGC_371_699,(0,0,25):C.UVGC_371_700,(0,0,26):C.UVGC_371_701,(0,0,27):C.UVGC_371_702,(0,0,28):C.UVGC_371_703,(0,0,29):C.UVGC_371_704,(0,0,30):C.UVGC_371_705,(0,0,31):C.UVGC_371_706,(0,0,32):C.UVGC_371_707,(0,0,5):C.UVGC_387_722})

V_745 = CTVertex(name = 'V_745',
                 type = 'UV',
                 particles = [ P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_401_734,(0,1,0):C.UVGC_400_733})

V_746 = CTVertex(name = 'V_746',
                 type = 'UV',
                 particles = [ P.W__plus__, P.Z, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_716_1018,(0,0,2):C.UVGC_716_1019,(0,0,1):C.UVGC_652_950})

V_747 = CTVertex(name = 'V_747',
                 type = 'UV',
                 particles = [ P.W__minus__, P.Z, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_716_1018,(0,0,2):C.UVGC_716_1019,(0,0,1):C.UVGC_652_950})

V_748 = CTVertex(name = 'V_748',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_402_735})

V_749 = CTVertex(name = 'V_749',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_371_676,(0,0,1):C.UVGC_371_677,(0,0,2):C.UVGC_371_678,(0,0,3):C.UVGC_371_679,(0,0,4):C.UVGC_371_680,(0,0,6):C.UVGC_371_681,(0,0,7):C.UVGC_371_682,(0,0,8):C.UVGC_371_683,(0,0,9):C.UVGC_371_684,(0,0,10):C.UVGC_371_685,(0,0,11):C.UVGC_371_686,(0,0,12):C.UVGC_371_687,(0,0,13):C.UVGC_371_688,(0,0,14):C.UVGC_371_689,(0,0,15):C.UVGC_371_690,(0,0,16):C.UVGC_371_691,(0,0,17):C.UVGC_371_692,(0,0,18):C.UVGC_371_693,(0,0,19):C.UVGC_371_694,(0,0,20):C.UVGC_371_695,(0,0,21):C.UVGC_371_696,(0,0,22):C.UVGC_371_697,(0,0,23):C.UVGC_371_698,(0,0,24):C.UVGC_371_699,(0,0,25):C.UVGC_371_700,(0,0,26):C.UVGC_371_701,(0,0,27):C.UVGC_371_702,(0,0,28):C.UVGC_371_703,(0,0,29):C.UVGC_371_704,(0,0,30):C.UVGC_371_705,(0,0,31):C.UVGC_371_706,(0,0,32):C.UVGC_371_707,(0,0,5):C.UVGC_403_736})

V_750 = CTVertex(name = 'V_750',
                 type = 'UV',
                 particles = [ P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_417_748,(0,1,0):C.UVGC_416_747})

V_751 = CTVertex(name = 'V_751',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_418_749})

V_752 = CTVertex(name = 'V_752',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_419_750,(0,0,1):C.UVGC_419_751,(0,0,2):C.UVGC_419_752,(0,0,3):C.UVGC_419_753,(0,0,4):C.UVGC_419_754,(0,0,6):C.UVGC_419_755,(0,0,7):C.UVGC_419_756,(0,0,8):C.UVGC_419_757,(0,0,9):C.UVGC_419_758,(0,0,10):C.UVGC_419_759,(0,0,11):C.UVGC_419_760,(0,0,12):C.UVGC_419_761,(0,0,13):C.UVGC_419_762,(0,0,14):C.UVGC_419_763,(0,0,15):C.UVGC_419_764,(0,0,16):C.UVGC_419_765,(0,0,17):C.UVGC_419_766,(0,0,18):C.UVGC_419_767,(0,0,19):C.UVGC_419_768,(0,0,20):C.UVGC_419_769,(0,0,21):C.UVGC_419_770,(0,0,22):C.UVGC_419_771,(0,0,23):C.UVGC_419_772,(0,0,24):C.UVGC_419_773,(0,0,25):C.UVGC_419_774,(0,0,26):C.UVGC_419_775,(0,0,27):C.UVGC_419_776,(0,0,28):C.UVGC_419_777,(0,0,29):C.UVGC_419_778,(0,0,30):C.UVGC_419_779,(0,0,31):C.UVGC_419_780,(0,0,32):C.UVGC_419_781,(0,0,5):C.UVGC_419_782})

V_753 = CTVertex(name = 'V_753',
                 type = 'UV',
                 particles = [ P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_433_794,(0,1,0):C.UVGC_432_793})

V_754 = CTVertex(name = 'V_754',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_434_795})

V_755 = CTVertex(name = 'V_755',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_419_750,(0,0,1):C.UVGC_419_751,(0,0,2):C.UVGC_419_752,(0,0,3):C.UVGC_419_753,(0,0,4):C.UVGC_419_754,(0,0,6):C.UVGC_419_755,(0,0,7):C.UVGC_419_756,(0,0,8):C.UVGC_419_757,(0,0,9):C.UVGC_419_758,(0,0,10):C.UVGC_419_759,(0,0,11):C.UVGC_419_760,(0,0,12):C.UVGC_419_761,(0,0,13):C.UVGC_419_762,(0,0,14):C.UVGC_419_763,(0,0,15):C.UVGC_419_764,(0,0,16):C.UVGC_419_765,(0,0,17):C.UVGC_419_766,(0,0,18):C.UVGC_419_767,(0,0,19):C.UVGC_419_768,(0,0,20):C.UVGC_419_769,(0,0,21):C.UVGC_419_770,(0,0,22):C.UVGC_419_771,(0,0,23):C.UVGC_419_772,(0,0,24):C.UVGC_419_773,(0,0,25):C.UVGC_419_774,(0,0,26):C.UVGC_419_775,(0,0,27):C.UVGC_419_776,(0,0,28):C.UVGC_419_777,(0,0,29):C.UVGC_419_778,(0,0,30):C.UVGC_419_779,(0,0,31):C.UVGC_419_780,(0,0,32):C.UVGC_419_781,(0,0,5):C.UVGC_435_796})

V_756 = CTVertex(name = 'V_756',
                 type = 'UV',
                 particles = [ P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_449_808,(0,1,0):C.UVGC_448_807})

V_757 = CTVertex(name = 'V_757',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_450_809})

V_758 = CTVertex(name = 'V_758',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_419_750,(0,0,1):C.UVGC_419_751,(0,0,2):C.UVGC_419_752,(0,0,3):C.UVGC_419_753,(0,0,4):C.UVGC_419_754,(0,0,6):C.UVGC_419_755,(0,0,7):C.UVGC_419_756,(0,0,8):C.UVGC_419_757,(0,0,9):C.UVGC_419_758,(0,0,10):C.UVGC_419_759,(0,0,11):C.UVGC_419_760,(0,0,12):C.UVGC_419_761,(0,0,13):C.UVGC_419_762,(0,0,14):C.UVGC_419_763,(0,0,15):C.UVGC_419_764,(0,0,16):C.UVGC_419_765,(0,0,17):C.UVGC_419_766,(0,0,18):C.UVGC_419_767,(0,0,19):C.UVGC_419_768,(0,0,20):C.UVGC_419_769,(0,0,21):C.UVGC_419_770,(0,0,22):C.UVGC_419_771,(0,0,23):C.UVGC_419_772,(0,0,24):C.UVGC_419_773,(0,0,25):C.UVGC_419_774,(0,0,26):C.UVGC_419_775,(0,0,27):C.UVGC_419_776,(0,0,28):C.UVGC_419_777,(0,0,29):C.UVGC_419_778,(0,0,30):C.UVGC_419_779,(0,0,31):C.UVGC_419_780,(0,0,32):C.UVGC_419_781,(0,0,5):C.UVGC_451_810})

V_759 = CTVertex(name = 'V_759',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_276_529})

V_760 = CTVertex(name = 'V_760',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_292_543})

V_761 = CTVertex(name = 'V_761',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_308_557})

V_762 = CTVertex(name = 'V_762',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_324_603})

V_763 = CTVertex(name = 'V_763',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_340_617})

V_764 = CTVertex(name = 'V_764',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_356_631})

V_765 = CTVertex(name = 'V_765',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_372_709})

V_766 = CTVertex(name = 'V_766',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_388_723})

V_767 = CTVertex(name = 'V_767',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_404_737})

V_768 = CTVertex(name = 'V_768',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_420_783})

V_769 = CTVertex(name = 'V_769',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_436_797})

V_770 = CTVertex(name = 'V_770',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_452_811})

V_771 = CTVertex(name = 'V_771',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3Qu1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_775_1075,(0,0,2):C.UVGC_775_1076,(0,0,1):C.UVGC_596_939})

V_772 = CTVertex(name = 'V_772',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3Qd1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_596_937,(0,0,2):C.UVGC_596_938,(0,0,1):C.UVGC_596_939})

V_773 = CTVertex(name = 'V_773',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3Qu2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_588_916,(0,0,2):C.UVGC_588_917,(0,0,1):C.UVGC_588_918})

V_774 = CTVertex(name = 'V_774',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3Qd2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_761_1044,(0,0,2):C.UVGC_761_1045,(0,0,1):C.UVGC_588_918})

V_775 = CTVertex(name = 'V_775',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3Qu3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_768_1060,(0,0,2):C.UVGC_768_1061,(0,0,1):C.UVGC_583_904})

V_776 = CTVertex(name = 'V_776',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3Qd3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_583_902,(0,0,2):C.UVGC_583_903,(0,0,1):C.UVGC_583_904})

V_777 = CTVertex(name = 'V_777',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3Qu1, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_775_1075,(0,0,2):C.UVGC_775_1076,(0,0,1):C.UVGC_596_939})

V_778 = CTVertex(name = 'V_778',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3Qd1, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_596_937,(0,0,2):C.UVGC_596_938,(0,0,1):C.UVGC_596_939})

V_779 = CTVertex(name = 'V_779',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3Qu2, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_588_916,(0,0,2):C.UVGC_588_917,(0,0,1):C.UVGC_588_918})

V_780 = CTVertex(name = 'V_780',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3Qd2, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_761_1044,(0,0,2):C.UVGC_761_1045,(0,0,1):C.UVGC_588_918})

V_781 = CTVertex(name = 'V_781',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3Qu3, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_768_1060,(0,0,2):C.UVGC_768_1061,(0,0,1):C.UVGC_583_904})

V_782 = CTVertex(name = 'V_782',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3Qd3, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_583_902,(0,0,2):C.UVGC_583_903,(0,0,1):C.UVGC_583_904})

V_783 = CTVertex(name = 'V_783',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_250_377,(0,1,0):C.UVGC_161_24,(0,2,0):C.UVGC_163_26})

V_784 = CTVertex(name = 'V_784',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_250_377,(0,1,0):C.UVGC_145_8,(0,2,0):C.UVGC_147_10})

V_785 = CTVertex(name = 'V_785',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_250_377,(0,1,0):C.UVGC_157_20,(0,2,0):C.UVGC_159_22})

V_786 = CTVertex(name = 'V_786',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_243_371,(0,1,0):C.UVGC_149_12,(0,2,0):C.UVGC_151_14})

V_787 = CTVertex(name = 'V_787',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_243_371,(0,1,0):C.UVGC_153_16,(0,2,0):C.UVGC_155_18})

V_788 = CTVertex(name = 'V_788',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_243_371,(0,1,0):C.UVGC_141_4,(0,2,0):C.UVGC_143_6})

V_789 = CTVertex(name = 'V_789',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_244_372,(0,1,0):C.UVGC_240_336,(0,1,1):C.UVGC_240_337,(0,1,2):C.UVGC_240_338,(0,1,3):C.UVGC_240_339,(0,1,4):C.UVGC_240_340,(0,1,6):C.UVGC_240_341,(0,1,7):C.UVGC_240_342,(0,1,8):C.UVGC_240_343,(0,1,9):C.UVGC_240_344,(0,1,10):C.UVGC_240_345,(0,1,11):C.UVGC_240_346,(0,1,12):C.UVGC_240_347,(0,1,13):C.UVGC_240_348,(0,1,14):C.UVGC_240_349,(0,1,15):C.UVGC_240_350,(0,1,16):C.UVGC_240_351,(0,1,17):C.UVGC_240_352,(0,1,18):C.UVGC_240_353,(0,1,19):C.UVGC_240_354,(0,1,20):C.UVGC_240_355,(0,1,21):C.UVGC_240_356,(0,1,22):C.UVGC_240_357,(0,1,23):C.UVGC_240_358,(0,1,24):C.UVGC_240_359,(0,1,25):C.UVGC_240_360,(0,1,26):C.UVGC_240_361,(0,1,27):C.UVGC_240_362,(0,1,28):C.UVGC_240_363,(0,1,29):C.UVGC_240_364,(0,1,30):C.UVGC_240_365,(0,1,31):C.UVGC_240_366,(0,1,32):C.UVGC_240_367,(0,1,5):C.UVGC_470_823,(0,2,0):C.UVGC_240_336,(0,2,1):C.UVGC_240_337,(0,2,2):C.UVGC_240_338,(0,2,3):C.UVGC_240_339,(0,2,4):C.UVGC_240_340,(0,2,6):C.UVGC_240_341,(0,2,7):C.UVGC_240_342,(0,2,8):C.UVGC_240_343,(0,2,9):C.UVGC_240_344,(0,2,10):C.UVGC_240_345,(0,2,11):C.UVGC_240_346,(0,2,12):C.UVGC_240_347,(0,2,13):C.UVGC_240_348,(0,2,14):C.UVGC_240_349,(0,2,15):C.UVGC_240_350,(0,2,16):C.UVGC_240_351,(0,2,17):C.UVGC_240_352,(0,2,18):C.UVGC_240_353,(0,2,19):C.UVGC_240_354,(0,2,20):C.UVGC_240_355,(0,2,21):C.UVGC_240_356,(0,2,22):C.UVGC_240_357,(0,2,23):C.UVGC_240_358,(0,2,24):C.UVGC_240_359,(0,2,25):C.UVGC_240_360,(0,2,26):C.UVGC_240_361,(0,2,27):C.UVGC_240_362,(0,2,28):C.UVGC_240_363,(0,2,29):C.UVGC_240_364,(0,2,30):C.UVGC_240_365,(0,2,31):C.UVGC_240_366,(0,2,32):C.UVGC_240_367,(0,2,5):C.UVGC_471_824})

V_790 = CTVertex(name = 'V_790',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.c, P.g] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,2):C.UVGC_244_372,(0,1,0):C.UVGC_240_336,(0,1,1):C.UVGC_240_337,(0,1,3):C.UVGC_240_338,(0,1,4):C.UVGC_240_339,(0,1,5):C.UVGC_240_340,(0,1,6):C.UVGC_240_341,(0,1,7):C.UVGC_240_342,(0,1,8):C.UVGC_240_343,(0,1,9):C.UVGC_240_344,(0,1,10):C.UVGC_240_345,(0,1,11):C.UVGC_240_346,(0,1,12):C.UVGC_240_347,(0,1,13):C.UVGC_240_348,(0,1,14):C.UVGC_240_349,(0,1,15):C.UVGC_240_350,(0,1,16):C.UVGC_240_351,(0,1,17):C.UVGC_240_352,(0,1,18):C.UVGC_240_353,(0,1,19):C.UVGC_240_354,(0,1,20):C.UVGC_240_355,(0,1,21):C.UVGC_240_356,(0,1,22):C.UVGC_240_357,(0,1,23):C.UVGC_240_358,(0,1,24):C.UVGC_240_359,(0,1,25):C.UVGC_240_360,(0,1,26):C.UVGC_240_361,(0,1,27):C.UVGC_240_362,(0,1,28):C.UVGC_240_363,(0,1,29):C.UVGC_240_364,(0,1,30):C.UVGC_240_365,(0,1,31):C.UVGC_240_366,(0,1,32):C.UVGC_240_367,(0,1,2):C.UVGC_247_375,(0,2,0):C.UVGC_240_336,(0,2,1):C.UVGC_240_337,(0,2,3):C.UVGC_240_338,(0,2,4):C.UVGC_240_339,(0,2,5):C.UVGC_240_340,(0,2,6):C.UVGC_240_341,(0,2,7):C.UVGC_240_342,(0,2,8):C.UVGC_240_343,(0,2,9):C.UVGC_240_344,(0,2,10):C.UVGC_240_345,(0,2,11):C.UVGC_240_346,(0,2,12):C.UVGC_240_347,(0,2,13):C.UVGC_240_348,(0,2,14):C.UVGC_240_349,(0,2,15):C.UVGC_240_350,(0,2,16):C.UVGC_240_351,(0,2,17):C.UVGC_240_352,(0,2,18):C.UVGC_240_353,(0,2,19):C.UVGC_240_354,(0,2,20):C.UVGC_240_355,(0,2,21):C.UVGC_240_356,(0,2,22):C.UVGC_240_357,(0,2,23):C.UVGC_240_358,(0,2,24):C.UVGC_240_359,(0,2,25):C.UVGC_240_360,(0,2,26):C.UVGC_240_361,(0,2,27):C.UVGC_240_362,(0,2,28):C.UVGC_240_363,(0,2,29):C.UVGC_240_364,(0,2,30):C.UVGC_240_365,(0,2,31):C.UVGC_240_366,(0,2,32):C.UVGC_240_367,(0,2,2):C.UVGC_248_376})

V_791 = CTVertex(name = 'V_791',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_244_372,(0,1,0):C.UVGC_240_336,(0,1,1):C.UVGC_240_337,(0,1,2):C.UVGC_240_338,(0,1,3):C.UVGC_240_339,(0,1,4):C.UVGC_240_340,(0,1,6):C.UVGC_240_341,(0,1,7):C.UVGC_240_342,(0,1,8):C.UVGC_240_343,(0,1,9):C.UVGC_240_344,(0,1,10):C.UVGC_240_345,(0,1,11):C.UVGC_240_346,(0,1,12):C.UVGC_240_347,(0,1,13):C.UVGC_240_348,(0,1,14):C.UVGC_240_349,(0,1,15):C.UVGC_240_350,(0,1,16):C.UVGC_240_351,(0,1,17):C.UVGC_240_352,(0,1,18):C.UVGC_240_353,(0,1,19):C.UVGC_240_354,(0,1,20):C.UVGC_240_355,(0,1,21):C.UVGC_240_356,(0,1,22):C.UVGC_240_357,(0,1,23):C.UVGC_240_358,(0,1,24):C.UVGC_240_359,(0,1,25):C.UVGC_240_360,(0,1,26):C.UVGC_240_361,(0,1,27):C.UVGC_240_362,(0,1,28):C.UVGC_240_363,(0,1,29):C.UVGC_240_364,(0,1,30):C.UVGC_240_365,(0,1,31):C.UVGC_240_366,(0,1,32):C.UVGC_240_367,(0,1,5):C.UVGC_460_816,(0,2,0):C.UVGC_240_336,(0,2,1):C.UVGC_240_337,(0,2,2):C.UVGC_240_338,(0,2,3):C.UVGC_240_339,(0,2,4):C.UVGC_240_340,(0,2,6):C.UVGC_240_341,(0,2,7):C.UVGC_240_342,(0,2,8):C.UVGC_240_343,(0,2,9):C.UVGC_240_344,(0,2,10):C.UVGC_240_345,(0,2,11):C.UVGC_240_346,(0,2,12):C.UVGC_240_347,(0,2,13):C.UVGC_240_348,(0,2,14):C.UVGC_240_349,(0,2,15):C.UVGC_240_350,(0,2,16):C.UVGC_240_351,(0,2,17):C.UVGC_240_352,(0,2,18):C.UVGC_240_353,(0,2,19):C.UVGC_240_354,(0,2,20):C.UVGC_240_355,(0,2,21):C.UVGC_240_356,(0,2,22):C.UVGC_240_357,(0,2,23):C.UVGC_240_358,(0,2,24):C.UVGC_240_359,(0,2,25):C.UVGC_240_360,(0,2,26):C.UVGC_240_361,(0,2,27):C.UVGC_240_362,(0,2,28):C.UVGC_240_363,(0,2,29):C.UVGC_240_364,(0,2,30):C.UVGC_240_365,(0,2,31):C.UVGC_240_366,(0,2,32):C.UVGC_240_367,(0,2,5):C.UVGC_461_817})

V_792 = CTVertex(name = 'V_792',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,3):C.UVGC_244_372,(0,1,0):C.UVGC_240_336,(0,1,1):C.UVGC_240_337,(0,1,2):C.UVGC_240_338,(0,1,4):C.UVGC_240_339,(0,1,5):C.UVGC_240_340,(0,1,6):C.UVGC_240_341,(0,1,7):C.UVGC_240_342,(0,1,8):C.UVGC_240_343,(0,1,9):C.UVGC_240_344,(0,1,10):C.UVGC_240_345,(0,1,11):C.UVGC_240_346,(0,1,12):C.UVGC_240_347,(0,1,13):C.UVGC_240_348,(0,1,14):C.UVGC_240_349,(0,1,15):C.UVGC_240_350,(0,1,16):C.UVGC_240_351,(0,1,17):C.UVGC_240_352,(0,1,18):C.UVGC_240_353,(0,1,19):C.UVGC_240_354,(0,1,20):C.UVGC_240_355,(0,1,21):C.UVGC_240_356,(0,1,22):C.UVGC_240_357,(0,1,23):C.UVGC_240_358,(0,1,24):C.UVGC_240_359,(0,1,25):C.UVGC_240_360,(0,1,26):C.UVGC_240_361,(0,1,27):C.UVGC_240_362,(0,1,28):C.UVGC_240_363,(0,1,29):C.UVGC_240_364,(0,1,30):C.UVGC_240_365,(0,1,31):C.UVGC_240_366,(0,1,32):C.UVGC_240_367,(0,1,3):C.UVGC_254_380,(0,2,0):C.UVGC_240_336,(0,2,1):C.UVGC_240_337,(0,2,2):C.UVGC_240_338,(0,2,4):C.UVGC_240_339,(0,2,5):C.UVGC_240_340,(0,2,6):C.UVGC_240_341,(0,2,7):C.UVGC_240_342,(0,2,8):C.UVGC_240_343,(0,2,9):C.UVGC_240_344,(0,2,10):C.UVGC_240_345,(0,2,11):C.UVGC_240_346,(0,2,12):C.UVGC_240_347,(0,2,13):C.UVGC_240_348,(0,2,14):C.UVGC_240_349,(0,2,15):C.UVGC_240_350,(0,2,16):C.UVGC_240_351,(0,2,17):C.UVGC_240_352,(0,2,18):C.UVGC_240_353,(0,2,19):C.UVGC_240_354,(0,2,20):C.UVGC_240_355,(0,2,21):C.UVGC_240_356,(0,2,22):C.UVGC_240_357,(0,2,23):C.UVGC_240_358,(0,2,24):C.UVGC_240_359,(0,2,25):C.UVGC_240_360,(0,2,26):C.UVGC_240_361,(0,2,27):C.UVGC_240_362,(0,2,28):C.UVGC_240_363,(0,2,29):C.UVGC_240_364,(0,2,30):C.UVGC_240_365,(0,2,31):C.UVGC_240_366,(0,2,32):C.UVGC_240_367,(0,2,3):C.UVGC_255_381})

V_793 = CTVertex(name = 'V_793',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_244_372,(0,1,0):C.UVGC_240_336,(0,1,1):C.UVGC_240_337,(0,1,2):C.UVGC_240_338,(0,1,3):C.UVGC_240_339,(0,1,4):C.UVGC_240_340,(0,1,6):C.UVGC_240_341,(0,1,7):C.UVGC_240_342,(0,1,8):C.UVGC_240_343,(0,1,9):C.UVGC_240_344,(0,1,10):C.UVGC_240_345,(0,1,11):C.UVGC_240_346,(0,1,12):C.UVGC_240_347,(0,1,13):C.UVGC_240_348,(0,1,14):C.UVGC_240_349,(0,1,15):C.UVGC_240_350,(0,1,16):C.UVGC_240_351,(0,1,17):C.UVGC_240_352,(0,1,18):C.UVGC_240_353,(0,1,19):C.UVGC_240_354,(0,1,20):C.UVGC_240_355,(0,1,21):C.UVGC_240_356,(0,1,22):C.UVGC_240_357,(0,1,23):C.UVGC_240_358,(0,1,24):C.UVGC_240_359,(0,1,25):C.UVGC_240_360,(0,1,26):C.UVGC_240_361,(0,1,27):C.UVGC_240_362,(0,1,28):C.UVGC_240_363,(0,1,29):C.UVGC_240_364,(0,1,30):C.UVGC_240_365,(0,1,31):C.UVGC_240_366,(0,1,32):C.UVGC_240_367,(0,1,5):C.UVGC_453_812,(0,2,0):C.UVGC_240_336,(0,2,1):C.UVGC_240_337,(0,2,2):C.UVGC_240_338,(0,2,3):C.UVGC_240_339,(0,2,4):C.UVGC_240_340,(0,2,6):C.UVGC_240_341,(0,2,7):C.UVGC_240_342,(0,2,8):C.UVGC_240_343,(0,2,9):C.UVGC_240_344,(0,2,10):C.UVGC_240_345,(0,2,11):C.UVGC_240_346,(0,2,12):C.UVGC_240_347,(0,2,13):C.UVGC_240_348,(0,2,14):C.UVGC_240_349,(0,2,15):C.UVGC_240_350,(0,2,16):C.UVGC_240_351,(0,2,17):C.UVGC_240_352,(0,2,18):C.UVGC_240_353,(0,2,19):C.UVGC_240_354,(0,2,20):C.UVGC_240_355,(0,2,21):C.UVGC_240_356,(0,2,22):C.UVGC_240_357,(0,2,23):C.UVGC_240_358,(0,2,24):C.UVGC_240_359,(0,2,25):C.UVGC_240_360,(0,2,26):C.UVGC_240_361,(0,2,27):C.UVGC_240_362,(0,2,28):C.UVGC_240_363,(0,2,29):C.UVGC_240_364,(0,2,30):C.UVGC_240_365,(0,2,31):C.UVGC_240_366,(0,2,32):C.UVGC_240_367,(0,2,5):C.UVGC_454_813})

V_794 = CTVertex(name = 'V_794',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.b, P.g] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,1):C.UVGC_244_372,(0,1,0):C.UVGC_240_336,(0,1,2):C.UVGC_240_337,(0,1,3):C.UVGC_240_338,(0,1,4):C.UVGC_240_339,(0,1,5):C.UVGC_240_340,(0,1,6):C.UVGC_240_341,(0,1,7):C.UVGC_240_342,(0,1,8):C.UVGC_240_343,(0,1,9):C.UVGC_240_344,(0,1,10):C.UVGC_240_345,(0,1,11):C.UVGC_240_346,(0,1,12):C.UVGC_240_347,(0,1,13):C.UVGC_240_348,(0,1,14):C.UVGC_240_349,(0,1,15):C.UVGC_240_350,(0,1,16):C.UVGC_240_351,(0,1,17):C.UVGC_240_352,(0,1,18):C.UVGC_240_353,(0,1,19):C.UVGC_240_354,(0,1,20):C.UVGC_240_355,(0,1,21):C.UVGC_240_356,(0,1,22):C.UVGC_240_357,(0,1,23):C.UVGC_240_358,(0,1,24):C.UVGC_240_359,(0,1,25):C.UVGC_240_360,(0,1,26):C.UVGC_240_361,(0,1,27):C.UVGC_240_362,(0,1,28):C.UVGC_240_363,(0,1,29):C.UVGC_240_364,(0,1,30):C.UVGC_240_365,(0,1,31):C.UVGC_240_366,(0,1,32):C.UVGC_240_367,(0,1,1):C.UVGC_240_368,(0,2,0):C.UVGC_240_336,(0,2,2):C.UVGC_240_337,(0,2,3):C.UVGC_240_338,(0,2,4):C.UVGC_240_339,(0,2,5):C.UVGC_240_340,(0,2,6):C.UVGC_240_341,(0,2,7):C.UVGC_240_342,(0,2,8):C.UVGC_240_343,(0,2,9):C.UVGC_240_344,(0,2,10):C.UVGC_240_345,(0,2,11):C.UVGC_240_346,(0,2,12):C.UVGC_240_347,(0,2,13):C.UVGC_240_348,(0,2,14):C.UVGC_240_349,(0,2,15):C.UVGC_240_350,(0,2,16):C.UVGC_240_351,(0,2,17):C.UVGC_240_352,(0,2,18):C.UVGC_240_353,(0,2,19):C.UVGC_240_354,(0,2,20):C.UVGC_240_355,(0,2,21):C.UVGC_240_356,(0,2,22):C.UVGC_240_357,(0,2,23):C.UVGC_240_358,(0,2,24):C.UVGC_240_359,(0,2,25):C.UVGC_240_360,(0,2,26):C.UVGC_240_361,(0,2,27):C.UVGC_240_362,(0,2,28):C.UVGC_240_363,(0,2,29):C.UVGC_240_364,(0,2,30):C.UVGC_240_365,(0,2,31):C.UVGC_240_366,(0,2,32):C.UVGC_240_367,(0,2,1):C.UVGC_241_369})

V_795 = CTVertex(name = 'V_795',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_772_1068,(0,0,2):C.UVGC_772_1069,(0,0,1):C.UVGC_587_915})

V_796 = CTVertex(name = 'V_796',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_587_913,(0,0,2):C.UVGC_587_914,(0,0,1):C.UVGC_587_915})

V_797 = CTVertex(name = 'V_797',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_763_1047,(0,0,2):C.UVGC_763_1048,(0,0,1):C.UVGC_587_915})

V_798 = CTVertex(name = 'V_798',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_772_1068,(0,0,2):C.UVGC_772_1069,(0,0,1):C.UVGC_587_915})

V_799 = CTVertex(name = 'V_799',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_587_913,(0,0,2):C.UVGC_587_914,(0,0,1):C.UVGC_587_915})

V_800 = CTVertex(name = 'V_800',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_763_1047,(0,0,2):C.UVGC_763_1048,(0,0,1):C.UVGC_587_915})

V_801 = CTVertex(name = 'V_801',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_475_825,(0,1,0):C.UVGC_476_826})

V_802 = CTVertex(name = 'V_802',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_252_378,(0,1,0):C.UVGC_253_379})

V_803 = CTVertex(name = 'V_803',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_466_819,(0,1,0):C.UVGC_467_820})

V_804 = CTVertex(name = 'V_804',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_259_382,(0,1,0):C.UVGC_260_383})

V_805 = CTVertex(name = 'V_805',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_458_814,(0,1,0):C.UVGC_459_815})

V_806 = CTVertex(name = 'V_806',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_245_373,(0,1,0):C.UVGC_246_374})

V_807 = CTVertex(name = 'V_807',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.u, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_775_1075,(0,0,2):C.UVGC_775_1076,(0,0,1):C.UVGC_596_939})

V_808 = CTVertex(name = 'V_808',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.d, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_596_937,(0,0,2):C.UVGC_596_938,(0,0,1):C.UVGC_596_939})

V_809 = CTVertex(name = 'V_809',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.c, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_588_916,(0,0,2):C.UVGC_588_917,(0,0,1):C.UVGC_588_918})

V_810 = CTVertex(name = 'V_810',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.s, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_761_1044,(0,0,2):C.UVGC_761_1045,(0,0,1):C.UVGC_588_918})

V_811 = CTVertex(name = 'V_811',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.t, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_768_1060,(0,0,2):C.UVGC_768_1061,(0,0,1):C.UVGC_583_904})

V_812 = CTVertex(name = 'V_812',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.b, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_583_902,(0,0,2):C.UVGC_583_903,(0,0,1):C.UVGC_583_904})

V_813 = CTVertex(name = 'V_813',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.u, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_775_1075,(0,0,2):C.UVGC_775_1076,(0,0,1):C.UVGC_596_939})

V_814 = CTVertex(name = 'V_814',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.d, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_596_937,(0,0,2):C.UVGC_596_938,(0,0,1):C.UVGC_596_939})

V_815 = CTVertex(name = 'V_815',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.c, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_588_916,(0,0,2):C.UVGC_588_917,(0,0,1):C.UVGC_588_918})

V_816 = CTVertex(name = 'V_816',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.s, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_761_1044,(0,0,2):C.UVGC_761_1045,(0,0,1):C.UVGC_588_918})

V_817 = CTVertex(name = 'V_817',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.t, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_768_1060,(0,0,2):C.UVGC_768_1061,(0,0,1):C.UVGC_583_904})

V_818 = CTVertex(name = 'V_818',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.b, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_583_902,(0,0,2):C.UVGC_583_903,(0,0,1):C.UVGC_583_904})

V_819 = CTVertex(name = 'V_819',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3d1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_594_932,(0,0,2):C.UVGC_594_933,(0,0,1):C.UVGC_594_934})

V_820 = CTVertex(name = 'V_820',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3d2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_759_1039,(0,0,2):C.UVGC_759_1040,(0,0,1):C.UVGC_759_1041})

V_821 = CTVertex(name = 'V_821',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3d3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_581_897,(0,0,2):C.UVGC_581_898,(0,0,1):C.UVGC_581_899})

V_822 = CTVertex(name = 'V_822',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3u1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_777_1078,(0,0,2):C.UVGC_777_1079,(0,0,1):C.UVGC_777_1080})

V_823 = CTVertex(name = 'V_823',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3u2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_590_921,(0,0,2):C.UVGC_590_922,(0,0,1):C.UVGC_590_923})

V_824 = CTVertex(name = 'V_824',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3u3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_770_1063,(0,0,2):C.UVGC_770_1064,(0,0,1):C.UVGC_770_1065})

V_825 = CTVertex(name = 'V_825',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3d1, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_594_932,(0,0,2):C.UVGC_594_933,(0,0,1):C.UVGC_594_934})

V_826 = CTVertex(name = 'V_826',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3d2, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_759_1039,(0,0,2):C.UVGC_759_1040,(0,0,1):C.UVGC_759_1041})

V_827 = CTVertex(name = 'V_827',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3d3, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_581_897,(0,0,2):C.UVGC_581_898,(0,0,1):C.UVGC_581_899})

V_828 = CTVertex(name = 'V_828',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3u1, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_777_1078,(0,0,2):C.UVGC_777_1079,(0,0,1):C.UVGC_777_1080})

V_829 = CTVertex(name = 'V_829',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3u2, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_590_921,(0,0,2):C.UVGC_590_922,(0,0,1):C.UVGC_590_923})

V_830 = CTVertex(name = 'V_830',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3u3, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_770_1063,(0,0,2):C.UVGC_770_1064,(0,0,1):C.UVGC_770_1065})

V_831 = CTVertex(name = 'V_831',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.d, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_594_932,(0,0,2):C.UVGC_594_933,(0,0,1):C.UVGC_594_934})

V_832 = CTVertex(name = 'V_832',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.s, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_759_1039,(0,0,2):C.UVGC_759_1040,(0,0,1):C.UVGC_759_1041})

V_833 = CTVertex(name = 'V_833',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.b, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_581_897,(0,0,2):C.UVGC_581_898,(0,0,1):C.UVGC_581_899})

V_834 = CTVertex(name = 'V_834',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.u, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_777_1078,(0,0,2):C.UVGC_777_1079,(0,0,1):C.UVGC_777_1080})

V_835 = CTVertex(name = 'V_835',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.c, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_590_921,(0,0,2):C.UVGC_590_922,(0,0,1):C.UVGC_590_923})

V_836 = CTVertex(name = 'V_836',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.t, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_770_1063,(0,0,2):C.UVGC_770_1064,(0,0,1):C.UVGC_770_1065})

V_837 = CTVertex(name = 'V_837',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.d, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_594_932,(0,0,2):C.UVGC_594_933,(0,0,1):C.UVGC_594_934})

V_838 = CTVertex(name = 'V_838',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.s, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_759_1039,(0,0,2):C.UVGC_759_1040,(0,0,1):C.UVGC_759_1041})

V_839 = CTVertex(name = 'V_839',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.b, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_581_897,(0,0,2):C.UVGC_581_898,(0,0,1):C.UVGC_581_899})

V_840 = CTVertex(name = 'V_840',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.u, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_777_1078,(0,0,2):C.UVGC_777_1079,(0,0,1):C.UVGC_777_1080})

V_841 = CTVertex(name = 'V_841',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.c, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_590_921,(0,0,2):C.UVGC_590_922,(0,0,1):C.UVGC_590_923})

V_842 = CTVertex(name = 'V_842',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.t, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_770_1063,(0,0,2):C.UVGC_770_1064,(0,0,1):C.UVGC_770_1065})

V_843 = CTVertex(name = 'V_843',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF4 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_242_370,(0,1,0):C.UVGC_160_23,(0,2,0):C.UVGC_162_25})

V_844 = CTVertex(name = 'V_844',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF4 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_242_370,(0,1,0):C.UVGC_144_7,(0,2,0):C.UVGC_146_9})

V_845 = CTVertex(name = 'V_845',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,1,0):C.UVGC_465_818,(0,3,0):C.UVGC_242_370,(0,0,0):C.UVGC_156_19,(0,2,0):C.UVGC_158_21})

V_846 = CTVertex(name = 'V_846',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF4 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_242_370,(0,1,0):C.UVGC_148_11,(0,2,0):C.UVGC_150_13})

V_847 = CTVertex(name = 'V_847',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF4 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_242_370,(0,1,0):C.UVGC_152_15,(0,2,0):C.UVGC_154_17})

V_848 = CTVertex(name = 'V_848',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF4 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_242_370,(0,1,0):C.UVGC_140_3,(0,2,0):C.UVGC_142_5})

V_849 = CTVertex(name = 'V_849',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.YF3Qu1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,1,0):C.UVGC_530_855,(0,3,0):C.UVGC_242_370,(0,0,0):C.UVGC_194_57,(0,2,0):C.UVGC_196_59})

V_850 = CTVertex(name = 'V_850',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.YF3Qu2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,1,0):C.UVGC_541_865,(0,3,0):C.UVGC_242_370,(0,0,0):C.UVGC_198_61,(0,2,0):C.UVGC_200_63})

V_851 = CTVertex(name = 'V_851',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.YF3Qu3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,1,0):C.UVGC_552_874,(0,3,0):C.UVGC_242_370,(0,0,0):C.UVGC_202_65,(0,2,0):C.UVGC_204_67})

V_852 = CTVertex(name = 'V_852',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.YF3Qd1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,1,0):C.UVGC_503_839,(0,3,0):C.UVGC_242_370,(0,0,0):C.UVGC_182_45,(0,2,0):C.UVGC_184_47})

V_853 = CTVertex(name = 'V_853',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.YF3Qd2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,1,0):C.UVGC_512_845,(0,3,0):C.UVGC_242_370,(0,2,0):C.UVGC_188_51,(0,0,0):C.UVGC_186_49})

V_854 = CTVertex(name = 'V_854',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.YF3Qd3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,1,0):C.UVGC_521_850,(0,3,0):C.UVGC_242_370,(0,0,0):C.UVGC_190_53,(0,2,0):C.UVGC_192_55})

V_855 = CTVertex(name = 'V_855',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.YF3u1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,1,0):C.UVGC_563_883,(0,3,0):C.UVGC_242_370,(0,0,0):C.UVGC_206_69,(0,2,0):C.UVGC_208_71})

V_856 = CTVertex(name = 'V_856',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.YF3u2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,1,0):C.UVGC_570_887,(0,3,0):C.UVGC_242_370,(0,0,0):C.UVGC_212_75,(0,2,0):C.UVGC_214_77})

V_857 = CTVertex(name = 'V_857',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.YF3u3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,1,0):C.UVGC_577_890,(0,3,0):C.UVGC_242_370,(0,0,0):C.UVGC_218_81,(0,2,0):C.UVGC_220_83})

V_858 = CTVertex(name = 'V_858',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.YF3d1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,1,0):C.UVGC_482_829,(0,3,0):C.UVGC_242_370,(0,0,0):C.UVGC_164_27,(0,2,0):C.UVGC_166_29})

V_859 = CTVertex(name = 'V_859',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.YF3d2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,1,0):C.UVGC_489_833,(0,3,0):C.UVGC_242_370,(0,0,0):C.UVGC_170_33,(0,2,0):C.UVGC_172_35})

V_860 = CTVertex(name = 'V_860',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.YF3d3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,1,0):C.UVGC_496_836,(0,3,0):C.UVGC_242_370,(0,0,0):C.UVGC_176_39,(0,2,0):C.UVGC_178_41})

V_861 = CTVertex(name = 'V_861',
                 type = 'UV',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV4, L.VV5, L.VV6 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_229_95,(0,0,1):C.UVGC_229_96,(0,0,2):C.UVGC_229_97,(0,0,3):C.UVGC_229_98,(0,0,4):C.UVGC_229_99,(0,0,5):C.UVGC_229_100,(0,0,6):C.UVGC_229_101,(0,0,7):C.UVGC_229_102,(0,0,8):C.UVGC_229_103,(0,0,9):C.UVGC_229_104,(0,0,10):C.UVGC_229_105,(0,0,11):C.UVGC_229_106,(0,0,12):C.UVGC_229_107,(0,0,13):C.UVGC_229_108,(0,0,14):C.UVGC_229_109,(0,0,15):C.UVGC_229_110,(0,0,16):C.UVGC_229_111,(0,0,17):C.UVGC_229_112,(0,0,18):C.UVGC_229_113,(0,0,19):C.UVGC_229_114,(0,0,20):C.UVGC_229_115,(0,0,21):C.UVGC_229_116,(0,0,22):C.UVGC_229_117,(0,0,23):C.UVGC_229_118,(0,0,24):C.UVGC_229_119,(0,0,25):C.UVGC_229_120,(0,0,26):C.UVGC_229_121,(0,0,27):C.UVGC_229_122,(0,0,28):C.UVGC_229_123,(0,0,29):C.UVGC_229_124,(0,0,30):C.UVGC_229_125,(0,0,31):C.UVGC_229_126,(0,1,3):C.UVGC_138_1,(0,2,4):C.UVGC_139_2})

V_862 = CTVertex(name = 'V_862',
                 type = 'UV',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_367_672,(0,1,0):C.UVGC_357_632})

V_863 = CTVertex(name = 'V_863',
                 type = 'UV',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_383_718,(0,1,0):C.UVGC_373_710})

V_864 = CTVertex(name = 'V_864',
                 type = 'UV',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_399_732,(0,1,0):C.UVGC_389_724})

V_865 = CTVertex(name = 'V_865',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_319_566,(0,1,0):C.UVGC_309_558})

V_866 = CTVertex(name = 'V_866',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_335_612,(0,1,0):C.UVGC_325_604})

V_867 = CTVertex(name = 'V_867',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_351_626,(0,1,0):C.UVGC_341_618})

V_868 = CTVertex(name = 'V_868',
                 type = 'UV',
                 particles = [ P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_415_746,(0,1,0):C.UVGC_405_738})

V_869 = CTVertex(name = 'V_869',
                 type = 'UV',
                 particles = [ P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_431_792,(0,1,0):C.UVGC_421_784})

V_870 = CTVertex(name = 'V_870',
                 type = 'UV',
                 particles = [ P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_447_806,(0,1,0):C.UVGC_437_798})

V_871 = CTVertex(name = 'V_871',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_271_492,(0,1,0):C.UVGC_261_384})

V_872 = CTVertex(name = 'V_872',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_287_538,(0,1,0):C.UVGC_277_530})

V_873 = CTVertex(name = 'V_873',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_303_552,(0,1,0):C.UVGC_293_544})

V_874 = CTVertex(name = 'V_874',
                 type = 'UV',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3Qu1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_268_455,(1,0,3):C.UVGC_268_456,(1,0,0):C.UVGC_788_1089,(1,0,5):C.UVGC_788_1090,(1,0,1):C.UVGC_788_1091,(1,0,4):C.UVGC_788_1092,(0,0,2):C.UVGC_268_455,(0,0,3):C.UVGC_268_456,(0,0,0):C.UVGC_788_1089,(0,0,5):C.UVGC_788_1090,(0,0,1):C.UVGC_788_1091,(0,0,4):C.UVGC_788_1092})

V_875 = CTVertex(name = 'V_875',
                 type = 'UV',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qu1, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu1, P.YS3Qu2] ], [ [P.g, P.YS3Qu1, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_861_1155,(1,0,8):C.UVGC_861_1156,(1,0,1):C.UVGC_861_1157,(1,0,7):C.UVGC_861_1158,(1,0,2):C.UVGC_801_1107,(1,0,6):C.UVGC_861_1159,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_860_1150,(0,0,8):C.UVGC_860_1151,(0,0,1):C.UVGC_860_1152,(0,0,7):C.UVGC_860_1153,(0,0,2):C.UVGC_800_1101,(0,0,6):C.UVGC_860_1154})

V_876 = CTVertex(name = 'V_876',
                 type = 'UV',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3Qu2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_268_455,(1,0,3):C.UVGC_268_456,(1,0,0):C.UVGC_788_1089,(1,0,5):C.UVGC_788_1090,(1,0,1):C.UVGC_788_1091,(1,0,4):C.UVGC_788_1092,(0,0,2):C.UVGC_268_455,(0,0,3):C.UVGC_268_456,(0,0,0):C.UVGC_788_1089,(0,0,5):C.UVGC_788_1090,(0,0,1):C.UVGC_788_1091,(0,0,4):C.UVGC_788_1092})

V_877 = CTVertex(name = 'V_877',
                 type = 'UV',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qu1, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qu1, P.YS3Qu3] ], [ [P.g, P.YS3Qu1, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_861_1155,(1,0,8):C.UVGC_861_1156,(1,0,1):C.UVGC_861_1157,(1,0,7):C.UVGC_861_1158,(1,0,2):C.UVGC_801_1107,(1,0,6):C.UVGC_861_1159,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_860_1150,(0,0,8):C.UVGC_860_1151,(0,0,1):C.UVGC_860_1152,(0,0,7):C.UVGC_860_1153,(0,0,2):C.UVGC_800_1101,(0,0,6):C.UVGC_860_1154})

V_878 = CTVertex(name = 'V_878',
                 type = 'UV',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qu2, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qu2, P.YS3Qu3] ], [ [P.g, P.YS3Qu2, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_861_1155,(1,0,8):C.UVGC_861_1156,(1,0,1):C.UVGC_861_1157,(1,0,7):C.UVGC_861_1158,(1,0,2):C.UVGC_801_1107,(1,0,6):C.UVGC_861_1159,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_860_1150,(0,0,8):C.UVGC_860_1151,(0,0,1):C.UVGC_860_1152,(0,0,7):C.UVGC_860_1153,(0,0,2):C.UVGC_800_1101,(0,0,6):C.UVGC_860_1154})

V_879 = CTVertex(name = 'V_879',
                 type = 'UV',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3Qu3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_268_455,(1,0,3):C.UVGC_268_456,(1,0,0):C.UVGC_788_1089,(1,0,5):C.UVGC_788_1090,(1,0,1):C.UVGC_788_1091,(1,0,4):C.UVGC_788_1092,(0,0,2):C.UVGC_268_455,(0,0,3):C.UVGC_268_456,(0,0,0):C.UVGC_788_1089,(0,0,5):C.UVGC_788_1090,(0,0,1):C.UVGC_788_1091,(0,0,4):C.UVGC_788_1092})

V_880 = CTVertex(name = 'V_880',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qu1] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,7):C.UVGC_599_946,(1,0,8):C.UVGC_599_947,(1,0,0):C.UVGC_817_1129,(1,0,4):C.UVGC_794_1095,(1,0,11):C.UVGC_855_1146,(1,0,1):C.UVGC_817_1131,(1,0,5):C.UVGC_795_1100,(1,0,10):C.UVGC_855_1147,(1,0,2):C.UVGC_817_1133,(1,0,6):C.UVGC_855_1148,(1,0,9):C.UVGC_855_1149,(0,0,3):C.UVGC_598_942,(0,0,7):C.UVGC_598_943,(0,0,8):C.UVGC_598_944,(0,0,0):C.UVGC_782_1083,(0,0,4):C.UVGC_795_1098,(0,0,11):C.UVGC_854_1141,(0,0,1):C.UVGC_782_1085,(0,0,5):C.UVGC_854_1142,(0,0,10):C.UVGC_854_1143,(0,0,2):C.UVGC_816_1127,(0,0,6):C.UVGC_854_1144,(0,0,9):C.UVGC_854_1145})

V_881 = CTVertex(name = 'V_881',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd1, P.YS3Qu2] ], [ [P.g, P.YS3Qd1, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_817_1129,(1,0,8):C.UVGC_855_1146,(1,0,1):C.UVGC_817_1131,(1,0,7):C.UVGC_855_1147,(1,0,2):C.UVGC_817_1133,(1,0,6):C.UVGC_855_1149,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_782_1083,(0,0,8):C.UVGC_854_1141,(0,0,1):C.UVGC_782_1085,(0,0,7):C.UVGC_854_1143,(0,0,2):C.UVGC_816_1127,(0,0,6):C.UVGC_854_1145})

V_882 = CTVertex(name = 'V_882',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd1, P.YS3Qu3] ], [ [P.g, P.YS3Qd1, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_817_1129,(1,0,8):C.UVGC_855_1146,(1,0,1):C.UVGC_817_1131,(1,0,7):C.UVGC_855_1147,(1,0,2):C.UVGC_817_1133,(1,0,6):C.UVGC_855_1149,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_782_1083,(0,0,8):C.UVGC_854_1141,(0,0,1):C.UVGC_782_1085,(0,0,7):C.UVGC_854_1143,(0,0,2):C.UVGC_816_1127,(0,0,6):C.UVGC_854_1145})

V_883 = CTVertex(name = 'V_883',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qd1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_268_455,(1,0,3):C.UVGC_268_456,(1,0,0):C.UVGC_782_1083,(1,0,5):C.UVGC_785_1087,(1,0,1):C.UVGC_782_1085,(1,0,4):C.UVGC_785_1088,(0,0,2):C.UVGC_268_455,(0,0,3):C.UVGC_268_456,(0,0,0):C.UVGC_782_1083,(0,0,5):C.UVGC_785_1087,(0,0,1):C.UVGC_782_1085,(0,0,4):C.UVGC_785_1088})

V_884 = CTVertex(name = 'V_884',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd2, P.YS3Qu1, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu2] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu2] ] ],
                 couplings = {(1,0,0):C.UVGC_794_1095,(1,0,1):C.UVGC_794_1096,(1,0,2):C.UVGC_794_1097,(0,0,0):C.UVGC_795_1098,(0,0,1):C.UVGC_795_1099,(0,0,2):C.UVGC_795_1100})

V_885 = CTVertex(name = 'V_885',
                 type = 'UV',
                 particles = [ P.YS3Qd1, P.YS3Qd2__tilde__, P.YS3Qu1__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu2] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu2] ] ],
                 couplings = {(1,0,0):C.UVGC_794_1095,(1,0,1):C.UVGC_794_1096,(1,0,2):C.UVGC_794_1097,(0,0,0):C.UVGC_795_1098,(0,0,1):C.UVGC_795_1099,(0,0,2):C.UVGC_795_1100})

V_886 = CTVertex(name = 'V_886',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd2, P.YS3Qu1] ], [ [P.g, P.YS3Qd2, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_817_1129,(1,0,8):C.UVGC_855_1146,(1,0,1):C.UVGC_817_1131,(1,0,7):C.UVGC_855_1147,(1,0,2):C.UVGC_817_1133,(1,0,6):C.UVGC_855_1149,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_782_1083,(0,0,8):C.UVGC_854_1141,(0,0,1):C.UVGC_782_1085,(0,0,7):C.UVGC_854_1143,(0,0,2):C.UVGC_816_1127,(0,0,6):C.UVGC_854_1145})

V_887 = CTVertex(name = 'V_887',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qu2] ], [ [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,7):C.UVGC_599_946,(1,0,8):C.UVGC_599_947,(1,0,0):C.UVGC_817_1129,(1,0,4):C.UVGC_794_1095,(1,0,11):C.UVGC_855_1146,(1,0,1):C.UVGC_817_1131,(1,0,5):C.UVGC_795_1100,(1,0,10):C.UVGC_855_1147,(1,0,2):C.UVGC_817_1133,(1,0,6):C.UVGC_855_1148,(1,0,9):C.UVGC_855_1149,(0,0,3):C.UVGC_598_942,(0,0,7):C.UVGC_598_943,(0,0,8):C.UVGC_598_944,(0,0,0):C.UVGC_782_1083,(0,0,4):C.UVGC_795_1098,(0,0,11):C.UVGC_854_1141,(0,0,1):C.UVGC_782_1085,(0,0,5):C.UVGC_854_1142,(0,0,10):C.UVGC_854_1143,(0,0,2):C.UVGC_816_1127,(0,0,6):C.UVGC_854_1144,(0,0,9):C.UVGC_854_1145})

V_888 = CTVertex(name = 'V_888',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd2, P.YS3Qu3] ], [ [P.g, P.YS3Qd2, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_817_1129,(1,0,8):C.UVGC_855_1146,(1,0,1):C.UVGC_817_1131,(1,0,7):C.UVGC_855_1147,(1,0,2):C.UVGC_817_1133,(1,0,6):C.UVGC_855_1149,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_782_1083,(0,0,8):C.UVGC_854_1141,(0,0,1):C.UVGC_782_1085,(0,0,7):C.UVGC_854_1143,(0,0,2):C.UVGC_816_1127,(0,0,6):C.UVGC_854_1145})

V_889 = CTVertex(name = 'V_889',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd1, P.YS3Qd2] ], [ [P.g, P.YS3Qd1, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_801_1107,(1,0,8):C.UVGC_813_1122,(1,0,1):C.UVGC_801_1109,(1,0,7):C.UVGC_813_1123,(1,0,2):C.UVGC_801_1111,(1,0,6):C.UVGC_813_1124,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_800_1101,(0,0,8):C.UVGC_812_1119,(0,0,1):C.UVGC_800_1103,(0,0,7):C.UVGC_812_1120,(0,0,2):C.UVGC_800_1105,(0,0,6):C.UVGC_812_1121})

V_890 = CTVertex(name = 'V_890',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qd2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_268_455,(1,0,3):C.UVGC_268_456,(1,0,0):C.UVGC_782_1083,(1,0,5):C.UVGC_785_1087,(1,0,1):C.UVGC_782_1085,(1,0,4):C.UVGC_785_1088,(0,0,2):C.UVGC_268_455,(0,0,3):C.UVGC_268_456,(0,0,0):C.UVGC_782_1083,(0,0,5):C.UVGC_785_1087,(0,0,1):C.UVGC_782_1085,(0,0,4):C.UVGC_785_1088})

V_891 = CTVertex(name = 'V_891',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd3, P.YS3Qu1, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.UVGC_794_1095,(1,0,1):C.UVGC_794_1096,(1,0,2):C.UVGC_794_1097,(0,0,0):C.UVGC_795_1098,(0,0,1):C.UVGC_795_1099,(0,0,2):C.UVGC_795_1100})

V_892 = CTVertex(name = 'V_892',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd3, P.YS3Qu2, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu2, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.UVGC_794_1095,(1,0,1):C.UVGC_794_1096,(1,0,2):C.UVGC_794_1097,(0,0,0):C.UVGC_795_1098,(0,0,1):C.UVGC_795_1099,(0,0,2):C.UVGC_795_1100})

V_893 = CTVertex(name = 'V_893',
                 type = 'UV',
                 particles = [ P.YS3Qd1, P.YS3Qd3__tilde__, P.YS3Qu1__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.UVGC_794_1095,(1,0,1):C.UVGC_794_1096,(1,0,2):C.UVGC_794_1097,(0,0,0):C.UVGC_795_1098,(0,0,1):C.UVGC_795_1099,(0,0,2):C.UVGC_795_1100})

V_894 = CTVertex(name = 'V_894',
                 type = 'UV',
                 particles = [ P.YS3Qd2, P.YS3Qd3__tilde__, P.YS3Qu2__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu2, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.UVGC_794_1095,(1,0,1):C.UVGC_794_1096,(1,0,2):C.UVGC_794_1097,(0,0,0):C.UVGC_795_1098,(0,0,1):C.UVGC_795_1099,(0,0,2):C.UVGC_795_1100})

V_895 = CTVertex(name = 'V_895',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3Qd3, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd3, P.YS3Qu1] ], [ [P.g, P.YS3Qd3, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_817_1129,(1,0,8):C.UVGC_855_1146,(1,0,1):C.UVGC_817_1131,(1,0,7):C.UVGC_855_1147,(1,0,2):C.UVGC_817_1133,(1,0,6):C.UVGC_855_1149,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_782_1083,(0,0,8):C.UVGC_854_1141,(0,0,1):C.UVGC_782_1085,(0,0,7):C.UVGC_854_1143,(0,0,2):C.UVGC_816_1127,(0,0,6):C.UVGC_854_1145})

V_896 = CTVertex(name = 'V_896',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qd3, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd3, P.YS3Qu2] ], [ [P.g, P.YS3Qd3, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_817_1129,(1,0,8):C.UVGC_855_1146,(1,0,1):C.UVGC_817_1131,(1,0,7):C.UVGC_855_1147,(1,0,2):C.UVGC_817_1133,(1,0,6):C.UVGC_855_1149,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_782_1083,(0,0,8):C.UVGC_854_1141,(0,0,1):C.UVGC_782_1085,(0,0,7):C.UVGC_854_1143,(0,0,2):C.UVGC_816_1127,(0,0,6):C.UVGC_854_1145})

V_897 = CTVertex(name = 'V_897',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,7):C.UVGC_599_946,(1,0,8):C.UVGC_599_947,(1,0,0):C.UVGC_817_1129,(1,0,4):C.UVGC_794_1095,(1,0,11):C.UVGC_855_1146,(1,0,1):C.UVGC_817_1131,(1,0,5):C.UVGC_795_1100,(1,0,10):C.UVGC_855_1147,(1,0,2):C.UVGC_817_1133,(1,0,6):C.UVGC_855_1148,(1,0,9):C.UVGC_855_1149,(0,0,3):C.UVGC_598_942,(0,0,7):C.UVGC_598_943,(0,0,8):C.UVGC_598_944,(0,0,0):C.UVGC_782_1083,(0,0,4):C.UVGC_795_1098,(0,0,11):C.UVGC_854_1141,(0,0,1):C.UVGC_782_1085,(0,0,5):C.UVGC_854_1142,(0,0,10):C.UVGC_854_1143,(0,0,2):C.UVGC_816_1127,(0,0,6):C.UVGC_854_1144,(0,0,9):C.UVGC_854_1145})

V_898 = CTVertex(name = 'V_898',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd1, P.YS3Qd3] ], [ [P.g, P.YS3Qd1, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_801_1107,(1,0,8):C.UVGC_813_1122,(1,0,1):C.UVGC_801_1109,(1,0,7):C.UVGC_813_1123,(1,0,2):C.UVGC_801_1111,(1,0,6):C.UVGC_813_1124,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_800_1101,(0,0,8):C.UVGC_812_1119,(0,0,1):C.UVGC_800_1103,(0,0,7):C.UVGC_812_1120,(0,0,2):C.UVGC_800_1105,(0,0,6):C.UVGC_812_1121})

V_899 = CTVertex(name = 'V_899',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd2, P.YS3Qd3] ], [ [P.g, P.YS3Qd2, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_801_1107,(1,0,8):C.UVGC_813_1122,(1,0,1):C.UVGC_801_1109,(1,0,7):C.UVGC_813_1123,(1,0,2):C.UVGC_801_1111,(1,0,6):C.UVGC_813_1124,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_800_1101,(0,0,8):C.UVGC_812_1119,(0,0,1):C.UVGC_800_1103,(0,0,7):C.UVGC_812_1120,(0,0,2):C.UVGC_800_1105,(0,0,6):C.UVGC_812_1121})

V_900 = CTVertex(name = 'V_900',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qd3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_268_455,(1,0,3):C.UVGC_268_456,(1,0,0):C.UVGC_782_1083,(1,0,5):C.UVGC_785_1087,(1,0,1):C.UVGC_782_1085,(1,0,4):C.UVGC_785_1088,(0,0,2):C.UVGC_268_455,(0,0,3):C.UVGC_268_456,(0,0,0):C.UVGC_782_1083,(0,0,5):C.UVGC_785_1087,(0,0,1):C.UVGC_782_1085,(0,0,4):C.UVGC_785_1088})

V_901 = CTVertex(name = 'V_901',
                 type = 'UV',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qu1, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qu1, P.YS3u1] ], [ [P.g, P.YS3Qu1, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_861_1155,(1,0,8):C.UVGC_865_1163,(1,0,1):C.UVGC_861_1157,(1,0,7):C.UVGC_865_1164,(1,0,2):C.UVGC_801_1107,(1,0,6):C.UVGC_865_1165,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_860_1150,(0,0,8):C.UVGC_864_1160,(0,0,1):C.UVGC_860_1152,(0,0,7):C.UVGC_864_1161,(0,0,2):C.UVGC_800_1101,(0,0,6):C.UVGC_864_1162})

V_902 = CTVertex(name = 'V_902',
                 type = 'UV',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qu2, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qu2, P.YS3u1] ], [ [P.g, P.YS3Qu2, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_861_1155,(1,0,8):C.UVGC_865_1163,(1,0,1):C.UVGC_861_1157,(1,0,7):C.UVGC_865_1164,(1,0,2):C.UVGC_801_1107,(1,0,6):C.UVGC_865_1165,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_860_1150,(0,0,8):C.UVGC_864_1160,(0,0,1):C.UVGC_860_1152,(0,0,7):C.UVGC_864_1161,(0,0,2):C.UVGC_800_1101,(0,0,6):C.UVGC_864_1162})

V_903 = CTVertex(name = 'V_903',
                 type = 'UV',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qu3, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qu3], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qu3, P.YS3u1] ], [ [P.g, P.YS3Qu3, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qu3, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_861_1155,(1,0,8):C.UVGC_865_1163,(1,0,1):C.UVGC_861_1157,(1,0,7):C.UVGC_865_1164,(1,0,2):C.UVGC_801_1107,(1,0,6):C.UVGC_865_1165,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_860_1150,(0,0,8):C.UVGC_864_1160,(0,0,1):C.UVGC_860_1152,(0,0,7):C.UVGC_864_1161,(0,0,2):C.UVGC_800_1101,(0,0,6):C.UVGC_864_1162})

V_904 = CTVertex(name = 'V_904',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qd1, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qd1, P.YS3u1] ], [ [P.g, P.YS3Qd1, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_817_1129,(1,0,8):C.UVGC_817_1130,(1,0,1):C.UVGC_817_1131,(1,0,7):C.UVGC_817_1132,(1,0,2):C.UVGC_817_1133,(1,0,6):C.UVGC_817_1134,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_782_1083,(0,0,8):C.UVGC_816_1125,(0,0,1):C.UVGC_782_1085,(0,0,7):C.UVGC_816_1126,(0,0,2):C.UVGC_816_1127,(0,0,6):C.UVGC_816_1128})

V_905 = CTVertex(name = 'V_905',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qd2, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qd2, P.YS3u1] ], [ [P.g, P.YS3Qd2, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_817_1129,(1,0,8):C.UVGC_817_1130,(1,0,1):C.UVGC_817_1131,(1,0,7):C.UVGC_817_1132,(1,0,2):C.UVGC_817_1133,(1,0,6):C.UVGC_817_1134,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_782_1083,(0,0,8):C.UVGC_816_1125,(0,0,1):C.UVGC_782_1085,(0,0,7):C.UVGC_816_1126,(0,0,2):C.UVGC_816_1127,(0,0,6):C.UVGC_816_1128})

V_906 = CTVertex(name = 'V_906',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qd3, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qd3, P.YS3u1] ], [ [P.g, P.YS3Qd3, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_817_1129,(1,0,8):C.UVGC_817_1130,(1,0,1):C.UVGC_817_1131,(1,0,7):C.UVGC_817_1132,(1,0,2):C.UVGC_817_1133,(1,0,6):C.UVGC_817_1134,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_782_1083,(0,0,8):C.UVGC_816_1125,(0,0,1):C.UVGC_782_1085,(0,0,7):C.UVGC_816_1126,(0,0,2):C.UVGC_816_1127,(0,0,6):C.UVGC_816_1128})

V_907 = CTVertex(name = 'V_907',
                 type = 'UV',
                 particles = [ P.YS3u1__tilde__, P.YS3u1__tilde__, P.YS3u1, P.YS3u1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3u1] ], [ [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_268_455,(1,0,3):C.UVGC_268_456,(1,0,0):C.UVGC_788_1089,(1,0,5):C.UVGC_791_1093,(1,0,1):C.UVGC_788_1091,(1,0,4):C.UVGC_791_1094,(0,0,2):C.UVGC_268_455,(0,0,3):C.UVGC_268_456,(0,0,0):C.UVGC_788_1089,(0,0,5):C.UVGC_791_1093,(0,0,1):C.UVGC_788_1091,(0,0,4):C.UVGC_791_1094})

V_908 = CTVertex(name = 'V_908',
                 type = 'UV',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qu1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qu1, P.YS3u2] ], [ [P.g, P.YS3Qu1, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_861_1155,(1,0,8):C.UVGC_865_1163,(1,0,1):C.UVGC_861_1157,(1,0,7):C.UVGC_865_1164,(1,0,2):C.UVGC_801_1107,(1,0,6):C.UVGC_865_1165,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_860_1150,(0,0,8):C.UVGC_864_1160,(0,0,1):C.UVGC_860_1152,(0,0,7):C.UVGC_864_1161,(0,0,2):C.UVGC_800_1101,(0,0,6):C.UVGC_864_1162})

V_909 = CTVertex(name = 'V_909',
                 type = 'UV',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qu2, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qu2, P.YS3u2] ], [ [P.g, P.YS3Qu2, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_861_1155,(1,0,8):C.UVGC_865_1163,(1,0,1):C.UVGC_861_1157,(1,0,7):C.UVGC_865_1164,(1,0,2):C.UVGC_801_1107,(1,0,6):C.UVGC_865_1165,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_860_1150,(0,0,8):C.UVGC_864_1160,(0,0,1):C.UVGC_860_1152,(0,0,7):C.UVGC_864_1161,(0,0,2):C.UVGC_800_1101,(0,0,6):C.UVGC_864_1162})

V_910 = CTVertex(name = 'V_910',
                 type = 'UV',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qu3, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qu3], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qu3, P.YS3u2] ], [ [P.g, P.YS3Qu3, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qu3, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_861_1155,(1,0,8):C.UVGC_865_1163,(1,0,1):C.UVGC_861_1157,(1,0,7):C.UVGC_865_1164,(1,0,2):C.UVGC_801_1107,(1,0,6):C.UVGC_865_1165,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_860_1150,(0,0,8):C.UVGC_864_1160,(0,0,1):C.UVGC_860_1152,(0,0,7):C.UVGC_864_1161,(0,0,2):C.UVGC_800_1101,(0,0,6):C.UVGC_864_1162})

V_911 = CTVertex(name = 'V_911',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qd1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qd1, P.YS3u2] ], [ [P.g, P.YS3Qd1, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_817_1129,(1,0,8):C.UVGC_817_1130,(1,0,1):C.UVGC_817_1131,(1,0,7):C.UVGC_817_1132,(1,0,2):C.UVGC_817_1133,(1,0,6):C.UVGC_817_1134,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_782_1083,(0,0,8):C.UVGC_816_1125,(0,0,1):C.UVGC_782_1085,(0,0,7):C.UVGC_816_1126,(0,0,2):C.UVGC_816_1127,(0,0,6):C.UVGC_816_1128})

V_912 = CTVertex(name = 'V_912',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qd2, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qd2, P.YS3u2] ], [ [P.g, P.YS3Qd2, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_817_1129,(1,0,8):C.UVGC_817_1130,(1,0,1):C.UVGC_817_1131,(1,0,7):C.UVGC_817_1132,(1,0,2):C.UVGC_817_1133,(1,0,6):C.UVGC_817_1134,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_782_1083,(0,0,8):C.UVGC_816_1125,(0,0,1):C.UVGC_782_1085,(0,0,7):C.UVGC_816_1126,(0,0,2):C.UVGC_816_1127,(0,0,6):C.UVGC_816_1128})

V_913 = CTVertex(name = 'V_913',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qd3, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qd3, P.YS3u2] ], [ [P.g, P.YS3Qd3, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_817_1129,(1,0,8):C.UVGC_817_1130,(1,0,1):C.UVGC_817_1131,(1,0,7):C.UVGC_817_1132,(1,0,2):C.UVGC_817_1133,(1,0,6):C.UVGC_817_1134,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_782_1083,(0,0,8):C.UVGC_816_1125,(0,0,1):C.UVGC_782_1085,(0,0,7):C.UVGC_816_1126,(0,0,2):C.UVGC_816_1127,(0,0,6):C.UVGC_816_1128})

V_914 = CTVertex(name = 'V_914',
                 type = 'UV',
                 particles = [ P.YS3u1__tilde__, P.YS3u1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3u1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3u1], [P.g, P.YS3u2] ], [ [P.g, P.YS3u1, P.YS3u2] ], [ [P.g, P.YS3u1, P.YS3u2, P.Z] ], [ [P.g, P.YS3u1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_861_1155,(1,0,8):C.UVGC_915_1172,(1,0,1):C.UVGC_861_1157,(1,0,7):C.UVGC_915_1173,(1,0,2):C.UVGC_801_1107,(1,0,6):C.UVGC_801_1108,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_860_1150,(0,0,8):C.UVGC_914_1170,(0,0,1):C.UVGC_860_1152,(0,0,7):C.UVGC_914_1171,(0,0,2):C.UVGC_800_1101,(0,0,6):C.UVGC_800_1102})

V_915 = CTVertex(name = 'V_915',
                 type = 'UV',
                 particles = [ P.YS3u2__tilde__, P.YS3u2__tilde__, P.YS3u2, P.YS3u2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3u2] ], [ [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_268_455,(1,0,3):C.UVGC_268_456,(1,0,0):C.UVGC_788_1089,(1,0,5):C.UVGC_791_1093,(1,0,1):C.UVGC_788_1091,(1,0,4):C.UVGC_791_1094,(0,0,2):C.UVGC_268_455,(0,0,3):C.UVGC_268_456,(0,0,0):C.UVGC_788_1089,(0,0,5):C.UVGC_791_1093,(0,0,1):C.UVGC_788_1091,(0,0,4):C.UVGC_791_1094})

V_916 = CTVertex(name = 'V_916',
                 type = 'UV',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qu1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qu1, P.YS3u3] ], [ [P.g, P.YS3Qu1, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_861_1155,(1,0,8):C.UVGC_865_1163,(1,0,1):C.UVGC_861_1157,(1,0,7):C.UVGC_865_1164,(1,0,2):C.UVGC_801_1107,(1,0,6):C.UVGC_865_1165,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_860_1150,(0,0,8):C.UVGC_864_1160,(0,0,1):C.UVGC_860_1152,(0,0,7):C.UVGC_864_1161,(0,0,2):C.UVGC_800_1101,(0,0,6):C.UVGC_864_1162})

V_917 = CTVertex(name = 'V_917',
                 type = 'UV',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qu2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qu2, P.YS3u3] ], [ [P.g, P.YS3Qu2, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_861_1155,(1,0,8):C.UVGC_865_1163,(1,0,1):C.UVGC_861_1157,(1,0,7):C.UVGC_865_1164,(1,0,2):C.UVGC_801_1107,(1,0,6):C.UVGC_865_1165,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_860_1150,(0,0,8):C.UVGC_864_1160,(0,0,1):C.UVGC_860_1152,(0,0,7):C.UVGC_864_1161,(0,0,2):C.UVGC_800_1101,(0,0,6):C.UVGC_864_1162})

V_918 = CTVertex(name = 'V_918',
                 type = 'UV',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qu3, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qu3], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qu3, P.YS3u3] ], [ [P.g, P.YS3Qu3, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qu3, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_861_1155,(1,0,8):C.UVGC_865_1163,(1,0,1):C.UVGC_861_1157,(1,0,7):C.UVGC_865_1164,(1,0,2):C.UVGC_801_1107,(1,0,6):C.UVGC_865_1165,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_860_1150,(0,0,8):C.UVGC_864_1160,(0,0,1):C.UVGC_860_1152,(0,0,7):C.UVGC_864_1161,(0,0,2):C.UVGC_800_1101,(0,0,6):C.UVGC_864_1162})

V_919 = CTVertex(name = 'V_919',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qd1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qd1, P.YS3u3] ], [ [P.g, P.YS3Qd1, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_817_1129,(1,0,8):C.UVGC_817_1130,(1,0,1):C.UVGC_817_1131,(1,0,7):C.UVGC_817_1132,(1,0,2):C.UVGC_817_1133,(1,0,6):C.UVGC_817_1134,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_782_1083,(0,0,8):C.UVGC_816_1125,(0,0,1):C.UVGC_782_1085,(0,0,7):C.UVGC_816_1126,(0,0,2):C.UVGC_816_1127,(0,0,6):C.UVGC_816_1128})

V_920 = CTVertex(name = 'V_920',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qd2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qd2, P.YS3u3] ], [ [P.g, P.YS3Qd2, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_817_1129,(1,0,8):C.UVGC_817_1130,(1,0,1):C.UVGC_817_1131,(1,0,7):C.UVGC_817_1132,(1,0,2):C.UVGC_817_1133,(1,0,6):C.UVGC_817_1134,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_782_1083,(0,0,8):C.UVGC_816_1125,(0,0,1):C.UVGC_782_1085,(0,0,7):C.UVGC_816_1126,(0,0,2):C.UVGC_816_1127,(0,0,6):C.UVGC_816_1128})

V_921 = CTVertex(name = 'V_921',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qd3, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qd3, P.YS3u3] ], [ [P.g, P.YS3Qd3, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_817_1129,(1,0,8):C.UVGC_817_1130,(1,0,1):C.UVGC_817_1131,(1,0,7):C.UVGC_817_1132,(1,0,2):C.UVGC_817_1133,(1,0,6):C.UVGC_817_1134,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_782_1083,(0,0,8):C.UVGC_816_1125,(0,0,1):C.UVGC_782_1085,(0,0,7):C.UVGC_816_1126,(0,0,2):C.UVGC_816_1127,(0,0,6):C.UVGC_816_1128})

V_922 = CTVertex(name = 'V_922',
                 type = 'UV',
                 particles = [ P.YS3u1__tilde__, P.YS3u1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3u1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3u1], [P.g, P.YS3u3] ], [ [P.g, P.YS3u1, P.YS3u3] ], [ [P.g, P.YS3u1, P.YS3u3, P.Z] ], [ [P.g, P.YS3u1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_861_1155,(1,0,8):C.UVGC_915_1172,(1,0,1):C.UVGC_861_1157,(1,0,7):C.UVGC_915_1173,(1,0,2):C.UVGC_801_1107,(1,0,6):C.UVGC_801_1108,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_860_1150,(0,0,8):C.UVGC_914_1170,(0,0,1):C.UVGC_860_1152,(0,0,7):C.UVGC_914_1171,(0,0,2):C.UVGC_800_1101,(0,0,6):C.UVGC_800_1102})

V_923 = CTVertex(name = 'V_923',
                 type = 'UV',
                 particles = [ P.YS3u2__tilde__, P.YS3u2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3u2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3u2], [P.g, P.YS3u3] ], [ [P.g, P.YS3u2, P.YS3u3] ], [ [P.g, P.YS3u2, P.YS3u3, P.Z] ], [ [P.g, P.YS3u2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_861_1155,(1,0,8):C.UVGC_915_1172,(1,0,1):C.UVGC_861_1157,(1,0,7):C.UVGC_915_1173,(1,0,2):C.UVGC_801_1107,(1,0,6):C.UVGC_801_1108,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_860_1150,(0,0,8):C.UVGC_914_1170,(0,0,1):C.UVGC_860_1152,(0,0,7):C.UVGC_914_1171,(0,0,2):C.UVGC_800_1101,(0,0,6):C.UVGC_800_1102})

V_924 = CTVertex(name = 'V_924',
                 type = 'UV',
                 particles = [ P.YS3u3__tilde__, P.YS3u3__tilde__, P.YS3u3, P.YS3u3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3u3] ], [ [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_268_455,(1,0,3):C.UVGC_268_456,(1,0,0):C.UVGC_788_1089,(1,0,5):C.UVGC_791_1093,(1,0,1):C.UVGC_788_1091,(1,0,4):C.UVGC_791_1094,(0,0,2):C.UVGC_268_455,(0,0,3):C.UVGC_268_456,(0,0,0):C.UVGC_788_1089,(0,0,5):C.UVGC_791_1093,(0,0,1):C.UVGC_788_1091,(0,0,4):C.UVGC_791_1094})

V_925 = CTVertex(name = 'V_925',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3d1, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3d1, P.YS3Qu1] ], [ [P.g, P.YS3d1, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_817_1129,(1,0,8):C.UVGC_849_1138,(1,0,1):C.UVGC_817_1131,(1,0,7):C.UVGC_849_1139,(1,0,2):C.UVGC_817_1133,(1,0,6):C.UVGC_849_1140,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_782_1083,(0,0,8):C.UVGC_848_1135,(0,0,1):C.UVGC_782_1085,(0,0,7):C.UVGC_848_1136,(0,0,2):C.UVGC_816_1127,(0,0,6):C.UVGC_848_1137})

V_926 = CTVertex(name = 'V_926',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3d1, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3d1, P.YS3Qu2] ], [ [P.g, P.YS3d1, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_817_1129,(1,0,8):C.UVGC_849_1138,(1,0,1):C.UVGC_817_1131,(1,0,7):C.UVGC_849_1139,(1,0,2):C.UVGC_817_1133,(1,0,6):C.UVGC_849_1140,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_782_1083,(0,0,8):C.UVGC_848_1135,(0,0,1):C.UVGC_782_1085,(0,0,7):C.UVGC_848_1136,(0,0,2):C.UVGC_816_1127,(0,0,6):C.UVGC_848_1137})

V_927 = CTVertex(name = 'V_927',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3d1, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3d1, P.YS3Qu3] ], [ [P.g, P.YS3d1, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_817_1129,(1,0,8):C.UVGC_849_1138,(1,0,1):C.UVGC_817_1131,(1,0,7):C.UVGC_849_1139,(1,0,2):C.UVGC_817_1133,(1,0,6):C.UVGC_849_1140,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_782_1083,(0,0,8):C.UVGC_848_1135,(0,0,1):C.UVGC_782_1085,(0,0,7):C.UVGC_848_1136,(0,0,2):C.UVGC_816_1127,(0,0,6):C.UVGC_848_1137})

V_928 = CTVertex(name = 'V_928',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qd1] ], [ [P.a, P.g, P.YS3d1, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qd1] ], [ [P.g, P.YS3d1, P.YS3Qd1] ], [ [P.g, P.YS3d1, P.YS3Qd1, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_801_1107,(1,0,8):C.UVGC_807_1116,(1,0,1):C.UVGC_801_1109,(1,0,7):C.UVGC_807_1117,(1,0,2):C.UVGC_801_1111,(1,0,6):C.UVGC_807_1118,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_800_1101,(0,0,8):C.UVGC_806_1113,(0,0,1):C.UVGC_800_1103,(0,0,7):C.UVGC_806_1114,(0,0,2):C.UVGC_800_1105,(0,0,6):C.UVGC_806_1115})

V_929 = CTVertex(name = 'V_929',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3d1, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3d1, P.YS3Qd2] ], [ [P.g, P.YS3d1, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_801_1107,(1,0,8):C.UVGC_807_1116,(1,0,1):C.UVGC_801_1109,(1,0,7):C.UVGC_807_1117,(1,0,2):C.UVGC_801_1111,(1,0,6):C.UVGC_807_1118,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_800_1101,(0,0,8):C.UVGC_806_1113,(0,0,1):C.UVGC_800_1103,(0,0,7):C.UVGC_806_1114,(0,0,2):C.UVGC_800_1105,(0,0,6):C.UVGC_806_1115})

V_930 = CTVertex(name = 'V_930',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3d1, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3d1, P.YS3Qd3] ], [ [P.g, P.YS3d1, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_801_1107,(1,0,8):C.UVGC_807_1116,(1,0,1):C.UVGC_801_1109,(1,0,7):C.UVGC_807_1117,(1,0,2):C.UVGC_801_1111,(1,0,6):C.UVGC_807_1118,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_800_1101,(0,0,8):C.UVGC_806_1113,(0,0,1):C.UVGC_800_1103,(0,0,7):C.UVGC_806_1114,(0,0,2):C.UVGC_800_1105,(0,0,6):C.UVGC_806_1115})

V_931 = CTVertex(name = 'V_931',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3d1, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3u1] ], [ [P.g, P.YS3d1, P.YS3u1] ], [ [P.g, P.YS3d1, P.YS3u1, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_817_1129,(1,0,8):C.UVGC_909_1167,(1,0,1):C.UVGC_817_1131,(1,0,7):C.UVGC_909_1168,(1,0,2):C.UVGC_817_1133,(1,0,6):C.UVGC_909_1169,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_782_1083,(0,0,8):C.UVGC_782_1084,(0,0,1):C.UVGC_782_1085,(0,0,7):C.UVGC_782_1086,(0,0,2):C.UVGC_816_1127,(0,0,6):C.UVGC_908_1166})

V_932 = CTVertex(name = 'V_932',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3d1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3u2] ], [ [P.g, P.YS3d1, P.YS3u2] ], [ [P.g, P.YS3d1, P.YS3u2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_817_1129,(1,0,8):C.UVGC_909_1167,(1,0,1):C.UVGC_817_1131,(1,0,7):C.UVGC_909_1168,(1,0,2):C.UVGC_817_1133,(1,0,6):C.UVGC_909_1169,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_782_1083,(0,0,8):C.UVGC_782_1084,(0,0,1):C.UVGC_782_1085,(0,0,7):C.UVGC_782_1086,(0,0,2):C.UVGC_816_1127,(0,0,6):C.UVGC_908_1166})

V_933 = CTVertex(name = 'V_933',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3d1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3u3] ], [ [P.g, P.YS3d1, P.YS3u3] ], [ [P.g, P.YS3d1, P.YS3u3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_817_1129,(1,0,8):C.UVGC_909_1167,(1,0,1):C.UVGC_817_1131,(1,0,7):C.UVGC_909_1168,(1,0,2):C.UVGC_817_1133,(1,0,6):C.UVGC_909_1169,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_782_1083,(0,0,8):C.UVGC_782_1084,(0,0,1):C.UVGC_782_1085,(0,0,7):C.UVGC_782_1086,(0,0,2):C.UVGC_816_1127,(0,0,6):C.UVGC_908_1166})

V_934 = CTVertex(name = 'V_934',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1__tilde__, P.YS3d1, P.YS3d1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1] ], [ [P.g] ], [ [P.g, P.YS3d1] ], [ [P.g, P.YS3d1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_268_455,(1,0,3):C.UVGC_268_456,(1,0,0):C.UVGC_782_1083,(1,0,5):C.UVGC_782_1084,(1,0,1):C.UVGC_782_1085,(1,0,4):C.UVGC_782_1086,(0,0,2):C.UVGC_268_455,(0,0,3):C.UVGC_268_456,(0,0,0):C.UVGC_782_1083,(0,0,5):C.UVGC_782_1084,(0,0,1):C.UVGC_782_1085,(0,0,4):C.UVGC_782_1086})

V_935 = CTVertex(name = 'V_935',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3d2, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3d2, P.YS3Qu1] ], [ [P.g, P.YS3d2, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_817_1129,(1,0,8):C.UVGC_849_1138,(1,0,1):C.UVGC_817_1131,(1,0,7):C.UVGC_849_1139,(1,0,2):C.UVGC_817_1133,(1,0,6):C.UVGC_849_1140,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_782_1083,(0,0,8):C.UVGC_848_1135,(0,0,1):C.UVGC_782_1085,(0,0,7):C.UVGC_848_1136,(0,0,2):C.UVGC_816_1127,(0,0,6):C.UVGC_848_1137})

V_936 = CTVertex(name = 'V_936',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3d2, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3d2, P.YS3Qu2] ], [ [P.g, P.YS3d2, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_817_1129,(1,0,8):C.UVGC_849_1138,(1,0,1):C.UVGC_817_1131,(1,0,7):C.UVGC_849_1139,(1,0,2):C.UVGC_817_1133,(1,0,6):C.UVGC_849_1140,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_782_1083,(0,0,8):C.UVGC_848_1135,(0,0,1):C.UVGC_782_1085,(0,0,7):C.UVGC_848_1136,(0,0,2):C.UVGC_816_1127,(0,0,6):C.UVGC_848_1137})

V_937 = CTVertex(name = 'V_937',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3d2, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3d2, P.YS3Qu3] ], [ [P.g, P.YS3d2, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_817_1129,(1,0,8):C.UVGC_849_1138,(1,0,1):C.UVGC_817_1131,(1,0,7):C.UVGC_849_1139,(1,0,2):C.UVGC_817_1133,(1,0,6):C.UVGC_849_1140,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_782_1083,(0,0,8):C.UVGC_848_1135,(0,0,1):C.UVGC_782_1085,(0,0,7):C.UVGC_848_1136,(0,0,2):C.UVGC_816_1127,(0,0,6):C.UVGC_848_1137})

V_938 = CTVertex(name = 'V_938',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qd1] ], [ [P.a, P.g, P.YS3d2, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qd1] ], [ [P.g, P.YS3d2, P.YS3Qd1] ], [ [P.g, P.YS3d2, P.YS3Qd1, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_801_1107,(1,0,8):C.UVGC_807_1116,(1,0,1):C.UVGC_801_1109,(1,0,7):C.UVGC_807_1117,(1,0,2):C.UVGC_801_1111,(1,0,6):C.UVGC_807_1118,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_800_1101,(0,0,8):C.UVGC_806_1113,(0,0,1):C.UVGC_800_1103,(0,0,7):C.UVGC_806_1114,(0,0,2):C.UVGC_800_1105,(0,0,6):C.UVGC_806_1115})

V_939 = CTVertex(name = 'V_939',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3d2, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3d2, P.YS3Qd2] ], [ [P.g, P.YS3d2, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_801_1107,(1,0,8):C.UVGC_807_1116,(1,0,1):C.UVGC_801_1109,(1,0,7):C.UVGC_807_1117,(1,0,2):C.UVGC_801_1111,(1,0,6):C.UVGC_807_1118,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_800_1101,(0,0,8):C.UVGC_806_1113,(0,0,1):C.UVGC_800_1103,(0,0,7):C.UVGC_806_1114,(0,0,2):C.UVGC_800_1105,(0,0,6):C.UVGC_806_1115})

V_940 = CTVertex(name = 'V_940',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3d2, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3d2, P.YS3Qd3] ], [ [P.g, P.YS3d2, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_801_1107,(1,0,8):C.UVGC_807_1116,(1,0,1):C.UVGC_801_1109,(1,0,7):C.UVGC_807_1117,(1,0,2):C.UVGC_801_1111,(1,0,6):C.UVGC_807_1118,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_800_1101,(0,0,8):C.UVGC_806_1113,(0,0,1):C.UVGC_800_1103,(0,0,7):C.UVGC_806_1114,(0,0,2):C.UVGC_800_1105,(0,0,6):C.UVGC_806_1115})

V_941 = CTVertex(name = 'V_941',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3d2, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3u1] ], [ [P.g, P.YS3d2, P.YS3u1] ], [ [P.g, P.YS3d2, P.YS3u1, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_817_1129,(1,0,8):C.UVGC_909_1167,(1,0,1):C.UVGC_817_1131,(1,0,7):C.UVGC_909_1168,(1,0,2):C.UVGC_817_1133,(1,0,6):C.UVGC_909_1169,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_782_1083,(0,0,8):C.UVGC_782_1084,(0,0,1):C.UVGC_782_1085,(0,0,7):C.UVGC_782_1086,(0,0,2):C.UVGC_816_1127,(0,0,6):C.UVGC_908_1166})

V_942 = CTVertex(name = 'V_942',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3d2, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3u2] ], [ [P.g, P.YS3d2, P.YS3u2] ], [ [P.g, P.YS3d2, P.YS3u2, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_817_1129,(1,0,8):C.UVGC_909_1167,(1,0,1):C.UVGC_817_1131,(1,0,7):C.UVGC_909_1168,(1,0,2):C.UVGC_817_1133,(1,0,6):C.UVGC_909_1169,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_782_1083,(0,0,8):C.UVGC_782_1084,(0,0,1):C.UVGC_782_1085,(0,0,7):C.UVGC_782_1086,(0,0,2):C.UVGC_816_1127,(0,0,6):C.UVGC_908_1166})

V_943 = CTVertex(name = 'V_943',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3d2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3u3] ], [ [P.g, P.YS3d2, P.YS3u3] ], [ [P.g, P.YS3d2, P.YS3u3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_817_1129,(1,0,8):C.UVGC_909_1167,(1,0,1):C.UVGC_817_1131,(1,0,7):C.UVGC_909_1168,(1,0,2):C.UVGC_817_1133,(1,0,6):C.UVGC_909_1169,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_782_1083,(0,0,8):C.UVGC_782_1084,(0,0,1):C.UVGC_782_1085,(0,0,7):C.UVGC_782_1086,(0,0,2):C.UVGC_816_1127,(0,0,6):C.UVGC_908_1166})

V_944 = CTVertex(name = 'V_944',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3d2] ], [ [P.a, P.g, P.YS3d1, P.YS3d2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3d2] ], [ [P.g, P.YS3d1, P.YS3d2] ], [ [P.g, P.YS3d1, P.YS3d2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3d2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_801_1107,(1,0,8):C.UVGC_801_1108,(1,0,1):C.UVGC_801_1109,(1,0,7):C.UVGC_801_1110,(1,0,2):C.UVGC_801_1111,(1,0,6):C.UVGC_801_1112,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_800_1101,(0,0,8):C.UVGC_800_1102,(0,0,1):C.UVGC_800_1103,(0,0,7):C.UVGC_800_1104,(0,0,2):C.UVGC_800_1105,(0,0,6):C.UVGC_800_1106})

V_945 = CTVertex(name = 'V_945',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2__tilde__, P.YS3d2, P.YS3d2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2] ], [ [P.g] ], [ [P.g, P.YS3d2] ], [ [P.g, P.YS3d2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_268_455,(1,0,3):C.UVGC_268_456,(1,0,0):C.UVGC_782_1083,(1,0,5):C.UVGC_782_1084,(1,0,1):C.UVGC_782_1085,(1,0,4):C.UVGC_782_1086,(0,0,2):C.UVGC_268_455,(0,0,3):C.UVGC_268_456,(0,0,0):C.UVGC_782_1083,(0,0,5):C.UVGC_782_1084,(0,0,1):C.UVGC_782_1085,(0,0,4):C.UVGC_782_1086})

V_946 = CTVertex(name = 'V_946',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3d3, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3d3, P.YS3Qu1] ], [ [P.g, P.YS3d3, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_817_1129,(1,0,8):C.UVGC_849_1138,(1,0,1):C.UVGC_817_1131,(1,0,7):C.UVGC_849_1139,(1,0,2):C.UVGC_817_1133,(1,0,6):C.UVGC_849_1140,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_782_1083,(0,0,8):C.UVGC_848_1135,(0,0,1):C.UVGC_782_1085,(0,0,7):C.UVGC_848_1136,(0,0,2):C.UVGC_816_1127,(0,0,6):C.UVGC_848_1137})

V_947 = CTVertex(name = 'V_947',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3d3, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3d3, P.YS3Qu2] ], [ [P.g, P.YS3d3, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_817_1129,(1,0,8):C.UVGC_849_1138,(1,0,1):C.UVGC_817_1131,(1,0,7):C.UVGC_849_1139,(1,0,2):C.UVGC_817_1133,(1,0,6):C.UVGC_849_1140,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_782_1083,(0,0,8):C.UVGC_848_1135,(0,0,1):C.UVGC_782_1085,(0,0,7):C.UVGC_848_1136,(0,0,2):C.UVGC_816_1127,(0,0,6):C.UVGC_848_1137})

V_948 = CTVertex(name = 'V_948',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3d3, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3d3, P.YS3Qu3] ], [ [P.g, P.YS3d3, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_817_1129,(1,0,8):C.UVGC_849_1138,(1,0,1):C.UVGC_817_1131,(1,0,7):C.UVGC_849_1139,(1,0,2):C.UVGC_817_1133,(1,0,6):C.UVGC_849_1140,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_782_1083,(0,0,8):C.UVGC_848_1135,(0,0,1):C.UVGC_782_1085,(0,0,7):C.UVGC_848_1136,(0,0,2):C.UVGC_816_1127,(0,0,6):C.UVGC_848_1137})

V_949 = CTVertex(name = 'V_949',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qd1] ], [ [P.a, P.g, P.YS3d3, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qd1] ], [ [P.g, P.YS3d3, P.YS3Qd1] ], [ [P.g, P.YS3d3, P.YS3Qd1, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_801_1107,(1,0,8):C.UVGC_807_1116,(1,0,1):C.UVGC_801_1109,(1,0,7):C.UVGC_807_1117,(1,0,2):C.UVGC_801_1111,(1,0,6):C.UVGC_807_1118,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_800_1101,(0,0,8):C.UVGC_806_1113,(0,0,1):C.UVGC_800_1103,(0,0,7):C.UVGC_806_1114,(0,0,2):C.UVGC_800_1105,(0,0,6):C.UVGC_806_1115})

V_950 = CTVertex(name = 'V_950',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3d3, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3d3, P.YS3Qd2] ], [ [P.g, P.YS3d3, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_801_1107,(1,0,8):C.UVGC_807_1116,(1,0,1):C.UVGC_801_1109,(1,0,7):C.UVGC_807_1117,(1,0,2):C.UVGC_801_1111,(1,0,6):C.UVGC_807_1118,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_800_1101,(0,0,8):C.UVGC_806_1113,(0,0,1):C.UVGC_800_1103,(0,0,7):C.UVGC_806_1114,(0,0,2):C.UVGC_800_1105,(0,0,6):C.UVGC_806_1115})

V_951 = CTVertex(name = 'V_951',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3d3, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3d3, P.YS3Qd3] ], [ [P.g, P.YS3d3, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_801_1107,(1,0,8):C.UVGC_807_1116,(1,0,1):C.UVGC_801_1109,(1,0,7):C.UVGC_807_1117,(1,0,2):C.UVGC_801_1111,(1,0,6):C.UVGC_807_1118,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_800_1101,(0,0,8):C.UVGC_806_1113,(0,0,1):C.UVGC_800_1103,(0,0,7):C.UVGC_806_1114,(0,0,2):C.UVGC_800_1105,(0,0,6):C.UVGC_806_1115})

V_952 = CTVertex(name = 'V_952',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3d3, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3u1] ], [ [P.g, P.YS3d3, P.YS3u1] ], [ [P.g, P.YS3d3, P.YS3u1, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_817_1129,(1,0,8):C.UVGC_909_1167,(1,0,1):C.UVGC_817_1131,(1,0,7):C.UVGC_909_1168,(1,0,2):C.UVGC_817_1133,(1,0,6):C.UVGC_909_1169,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_782_1083,(0,0,8):C.UVGC_782_1084,(0,0,1):C.UVGC_782_1085,(0,0,7):C.UVGC_782_1086,(0,0,2):C.UVGC_816_1127,(0,0,6):C.UVGC_908_1166})

V_953 = CTVertex(name = 'V_953',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3d3, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3u2] ], [ [P.g, P.YS3d3, P.YS3u2] ], [ [P.g, P.YS3d3, P.YS3u2, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_817_1129,(1,0,8):C.UVGC_909_1167,(1,0,1):C.UVGC_817_1131,(1,0,7):C.UVGC_909_1168,(1,0,2):C.UVGC_817_1133,(1,0,6):C.UVGC_909_1169,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_782_1083,(0,0,8):C.UVGC_782_1084,(0,0,1):C.UVGC_782_1085,(0,0,7):C.UVGC_782_1086,(0,0,2):C.UVGC_816_1127,(0,0,6):C.UVGC_908_1166})

V_954 = CTVertex(name = 'V_954',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3d3, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3u3] ], [ [P.g, P.YS3d3, P.YS3u3] ], [ [P.g, P.YS3d3, P.YS3u3, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_817_1129,(1,0,8):C.UVGC_909_1167,(1,0,1):C.UVGC_817_1131,(1,0,7):C.UVGC_909_1168,(1,0,2):C.UVGC_817_1133,(1,0,6):C.UVGC_909_1169,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_782_1083,(0,0,8):C.UVGC_782_1084,(0,0,1):C.UVGC_782_1085,(0,0,7):C.UVGC_782_1086,(0,0,2):C.UVGC_816_1127,(0,0,6):C.UVGC_908_1166})

V_955 = CTVertex(name = 'V_955',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3d3] ], [ [P.a, P.g, P.YS3d1, P.YS3d3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3d3] ], [ [P.g, P.YS3d1, P.YS3d3] ], [ [P.g, P.YS3d1, P.YS3d3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3d3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_801_1107,(1,0,8):C.UVGC_801_1108,(1,0,1):C.UVGC_801_1109,(1,0,7):C.UVGC_801_1110,(1,0,2):C.UVGC_801_1111,(1,0,6):C.UVGC_801_1112,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_800_1101,(0,0,8):C.UVGC_800_1102,(0,0,1):C.UVGC_800_1103,(0,0,7):C.UVGC_800_1104,(0,0,2):C.UVGC_800_1105,(0,0,6):C.UVGC_800_1106})

V_956 = CTVertex(name = 'V_956',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3d3] ], [ [P.a, P.g, P.YS3d2, P.YS3d3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3d3] ], [ [P.g, P.YS3d2, P.YS3d3] ], [ [P.g, P.YS3d2, P.YS3d3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3d3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_599_945,(1,0,4):C.UVGC_599_946,(1,0,5):C.UVGC_599_947,(1,0,0):C.UVGC_801_1107,(1,0,8):C.UVGC_801_1108,(1,0,1):C.UVGC_801_1109,(1,0,7):C.UVGC_801_1110,(1,0,2):C.UVGC_801_1111,(1,0,6):C.UVGC_801_1112,(0,0,3):C.UVGC_598_942,(0,0,4):C.UVGC_598_943,(0,0,5):C.UVGC_598_944,(0,0,0):C.UVGC_800_1101,(0,0,8):C.UVGC_800_1102,(0,0,1):C.UVGC_800_1103,(0,0,7):C.UVGC_800_1104,(0,0,2):C.UVGC_800_1105,(0,0,6):C.UVGC_800_1106})

V_957 = CTVertex(name = 'V_957',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3__tilde__, P.YS3d3, P.YS3d3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3] ], [ [P.g] ], [ [P.g, P.YS3d3] ], [ [P.g, P.YS3d3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_268_455,(1,0,3):C.UVGC_268_456,(1,0,0):C.UVGC_782_1083,(1,0,5):C.UVGC_782_1084,(1,0,1):C.UVGC_782_1085,(1,0,4):C.UVGC_782_1086,(0,0,2):C.UVGC_268_455,(0,0,3):C.UVGC_268_456,(0,0,0):C.UVGC_782_1083,(0,0,5):C.UVGC_782_1084,(0,0,1):C.UVGC_782_1085,(0,0,4):C.UVGC_782_1086})

