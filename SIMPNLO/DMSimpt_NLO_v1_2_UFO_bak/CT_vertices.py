# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.3.1 for Linux x86 (64-bit) (July 24, 2023)
# Date: Tue 23 Jun 2026 11:47:35


from object_library import all_vertices, all_CTvertices, Vertex, CTVertex
import particles as P
import CT_couplings as C
import lorentz as L


V_1 = CTVertex(name = 'V_1',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV1, L.VVV2, L.VVV3, L.VVV4, L.VVV5, L.VVV6, L.VVV8, L.VVV9 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u], [P.YF3d1], [P.YF3d2], [P.YF3d3], [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3], [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3], [P.YF3u1], [P.YF3u2], [P.YF3u3] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_664_297,(0,0,1):C.R2GC_664_298,(0,1,0):C.R2GC_619_291,(0,1,1):C.R2GC_619_292,(0,3,0):C.R2GC_619_291,(0,3,1):C.R2GC_621_294,(0,5,0):C.R2GC_664_297,(0,5,1):C.R2GC_665_299,(0,6,0):C.R2GC_664_297,(0,6,1):C.R2GC_666_300,(0,7,0):C.R2GC_619_291,(0,7,1):C.R2GC_620_293,(0,2,1):C.R2GC_269_118,(0,4,1):C.R2GC_261_108})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u], [P.YF3d1], [P.YF3d2], [P.YF3d3], [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3], [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3], [P.YF3u1], [P.YF3u2], [P.YF3u3] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_264_113,(0,0,1):C.R2GC_264_114,(2,0,0):C.R2GC_264_113,(2,0,1):C.R2GC_264_114,(5,0,0):C.R2GC_262_109,(5,0,1):C.R2GC_262_110,(1,0,0):C.R2GC_262_109,(1,0,1):C.R2GC_262_110,(7,0,0):C.R2GC_271_120,(7,0,1):C.R2GC_680_304,(6,0,0):C.R2GC_270_119,(6,0,1):C.R2GC_679_303,(4,0,0):C.R2GC_262_109,(4,0,1):C.R2GC_262_110,(3,0,0):C.R2GC_262_109,(3,0,1):C.R2GC_262_110,(8,0,0):C.R2GC_263_111,(8,0,1):C.R2GC_263_112,(11,0,0):C.R2GC_266_116,(11,0,1):C.R2GC_266_117,(10,0,0):C.R2GC_266_116,(10,0,1):C.R2GC_266_117,(9,0,1):C.R2GC_265_115,(0,1,0):C.R2GC_264_113,(0,1,1):C.R2GC_264_114,(2,1,0):C.R2GC_264_113,(2,1,1):C.R2GC_264_114,(7,1,0):C.R2GC_271_120,(7,1,1):C.R2GC_263_112,(5,1,0):C.R2GC_262_109,(5,1,1):C.R2GC_262_110,(1,1,0):C.R2GC_262_109,(1,1,1):C.R2GC_262_110,(4,1,0):C.R2GC_262_109,(4,1,1):C.R2GC_262_110,(3,1,0):C.R2GC_262_109,(3,1,1):C.R2GC_262_110,(8,1,0):C.R2GC_263_111,(8,1,1):C.R2GC_680_304,(6,1,0):C.R2GC_696_309,(6,1,1):C.R2GC_696_310,(11,1,0):C.R2GC_266_116,(11,1,1):C.R2GC_266_117,(10,1,0):C.R2GC_266_116,(10,1,1):C.R2GC_266_117,(9,1,1):C.R2GC_265_115,(0,2,0):C.R2GC_264_113,(0,2,1):C.R2GC_264_114,(2,2,0):C.R2GC_264_113,(2,2,1):C.R2GC_264_114,(7,2,0):C.R2GC_694_307,(7,2,1):C.R2GC_694_308,(5,2,0):C.R2GC_262_109,(5,2,1):C.R2GC_262_110,(1,2,0):C.R2GC_262_109,(1,2,1):C.R2GC_262_110,(4,2,0):C.R2GC_262_109,(4,2,1):C.R2GC_262_110,(3,2,0):C.R2GC_262_109,(3,2,1):C.R2GC_262_110,(8,2,0):C.R2GC_263_111,(8,2,1):C.R2GC_694_308,(6,2,0):C.R2GC_270_119,(11,2,0):C.R2GC_266_116,(11,2,1):C.R2GC_266_117,(10,2,0):C.R2GC_266_116,(10,2,1):C.R2GC_266_117,(9,2,1):C.R2GC_265_115})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.YF3d1__tilde__, P.YF3d1, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.YF3d1] ] ],
               couplings = {(0,0,0):C.R2GC_272_121})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.YF3d2__tilde__, P.YF3d2, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.YF3d2] ] ],
               couplings = {(0,0,0):C.R2GC_272_121})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.YF3d3__tilde__, P.YF3d3, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.YF3d3] ] ],
               couplings = {(0,0,0):C.R2GC_272_121})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.YF3Qd1__tilde__, P.YF3Qd1, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.YF3Qd1] ] ],
               couplings = {(0,0,0):C.R2GC_272_121})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.YF3Qd2__tilde__, P.YF3Qd2, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.YF3Qd2] ] ],
               couplings = {(0,0,0):C.R2GC_272_121})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.YF3Qd3__tilde__, P.YF3Qd3, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.YF3Qd3] ] ],
               couplings = {(0,0,0):C.R2GC_272_121})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.YF3Qu1__tilde__, P.YF3Qu1, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.YF3Qu1] ] ],
               couplings = {(0,0,0):C.R2GC_274_123})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.YF3Qu2__tilde__, P.YF3Qu2, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_274_123})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.YF3Qu3__tilde__, P.YF3Qu3, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_274_123})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.YF3u1__tilde__, P.YF3u1, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3u1] ] ],
                couplings = {(0,0,0):C.R2GC_274_123})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.YF3u2__tilde__, P.YF3u2, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3u2] ] ],
                couplings = {(0,0,0):C.R2GC_274_123})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.YF3u3__tilde__, P.YF3u3, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3u3] ] ],
                couplings = {(0,0,0):C.R2GC_274_123})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.u__tilde__, P.YF3Qu1, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                couplings = {(0,0,0):C.R2GC_554_260})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.u__tilde__, P.YF3Qu1, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                couplings = {(0,0,0):C.R2GC_554_260})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.d__tilde__, P.YF3Qd1, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                couplings = {(0,0,0):C.R2GC_554_260})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.d__tilde__, P.YF3Qd1, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                couplings = {(0,0,0):C.R2GC_554_260})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.c__tilde__, P.YF3Qu2, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_560_263})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.c__tilde__, P.YF3Qu2, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_560_263})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.s__tilde__, P.YF3Qd2, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                couplings = {(0,0,0):C.R2GC_560_263})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.s__tilde__, P.YF3Qd2, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                couplings = {(0,0,0):C.R2GC_560_263})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.t__tilde__, P.YF3Qu3, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_566_266})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.t__tilde__, P.YF3Qu3, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_566_266})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.b__tilde__, P.YF3Qd3, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                couplings = {(0,0,0):C.R2GC_566_266})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.b__tilde__, P.YF3Qd3, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                couplings = {(0,0,0):C.R2GC_566_266})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.YF3d1__tilde__, P.d, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                couplings = {(0,0,0):C.R2GC_536_251})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.YF3d2__tilde__, P.s, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                couplings = {(0,0,0):C.R2GC_542_254})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.YF3d3__tilde__, P.b, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                couplings = {(0,0,0):C.R2GC_548_257})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.YF3d1__tilde__, P.d, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                couplings = {(0,0,0):C.R2GC_536_251})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.YF3d2__tilde__, P.s, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                couplings = {(0,0,0):C.R2GC_542_254})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.YF3d3__tilde__, P.b, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                couplings = {(0,0,0):C.R2GC_548_257})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.YF3u1__tilde__, P.u, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                couplings = {(0,0,0):C.R2GC_593_272})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.YF3u2__tilde__, P.c, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                couplings = {(0,0,0):C.R2GC_599_275})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.YF3u3__tilde__, P.t, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                couplings = {(0,0,0):C.R2GC_605_278})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.YF3u1__tilde__, P.u, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                couplings = {(0,0,0):C.R2GC_593_272})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.YF3u2__tilde__, P.c, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                couplings = {(0,0,0):C.R2GC_599_275})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.YF3u3__tilde__, P.t, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                couplings = {(0,0,0):C.R2GC_605_278})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_530_247})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_531_248})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_532_249})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.d__tilde__, P.YF3d1, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                couplings = {(0,0,0):C.R2GC_536_251})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.s__tilde__, P.YF3d2, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                couplings = {(0,0,0):C.R2GC_542_254})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.b__tilde__, P.YF3d3, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                couplings = {(0,0,0):C.R2GC_548_257})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.d__tilde__, P.YF3d1, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                couplings = {(0,0,0):C.R2GC_536_251})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.s__tilde__, P.YF3d2, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                couplings = {(0,0,0):C.R2GC_542_254})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.b__tilde__, P.YF3d3, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                couplings = {(0,0,0):C.R2GC_548_257})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.u__tilde__, P.YF3u1, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                couplings = {(0,0,0):C.R2GC_593_272})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.c__tilde__, P.YF3u2, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                couplings = {(0,0,0):C.R2GC_599_275})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.t__tilde__, P.YF3u3, P.Xc__tilde__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                couplings = {(0,0,0):C.R2GC_605_278})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.u__tilde__, P.YF3u1, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                couplings = {(0,0,0):C.R2GC_593_272})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.c__tilde__, P.YF3u2, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                couplings = {(0,0,0):C.R2GC_599_275})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.t__tilde__, P.YF3u3, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                couplings = {(0,0,0):C.R2GC_605_278})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.YF3Qu1__tilde__, P.u, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                couplings = {(0,0,0):C.R2GC_554_260})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.YF3Qu1__tilde__, P.u, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                couplings = {(0,0,0):C.R2GC_554_260})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.YF3Qd1__tilde__, P.d, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                couplings = {(0,0,0):C.R2GC_554_260})

V_57 = CTVertex(name = 'V_57',
                type = 'R2',
                particles = [ P.YF3Qd1__tilde__, P.d, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                couplings = {(0,0,0):C.R2GC_554_260})

V_58 = CTVertex(name = 'V_58',
                type = 'R2',
                particles = [ P.YF3Qu2__tilde__, P.c, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_560_263})

V_59 = CTVertex(name = 'V_59',
                type = 'R2',
                particles = [ P.YF3Qu2__tilde__, P.c, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_560_263})

V_60 = CTVertex(name = 'V_60',
                type = 'R2',
                particles = [ P.YF3Qd2__tilde__, P.s, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                couplings = {(0,0,0):C.R2GC_560_263})

V_61 = CTVertex(name = 'V_61',
                type = 'R2',
                particles = [ P.YF3Qd2__tilde__, P.s, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                couplings = {(0,0,0):C.R2GC_560_263})

V_62 = CTVertex(name = 'V_62',
                type = 'R2',
                particles = [ P.YF3Qu3__tilde__, P.t, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_566_266})

V_63 = CTVertex(name = 'V_63',
                type = 'R2',
                particles = [ P.YF3Qu3__tilde__, P.t, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_566_266})

V_64 = CTVertex(name = 'V_64',
                type = 'R2',
                particles = [ P.YF3Qd3__tilde__, P.b, P.Xc ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                couplings = {(0,0,0):C.R2GC_566_266})

V_65 = CTVertex(name = 'V_65',
                type = 'R2',
                particles = [ P.YF3Qd3__tilde__, P.b, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                couplings = {(0,0,0):C.R2GC_566_266})

V_66 = CTVertex(name = 'V_66',
                type = 'R2',
                particles = [ P.YF3Qd1__tilde__, P.YF3Qd1, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd1] ] ],
                couplings = {(0,0,0):C.R2GC_273_122})

V_67 = CTVertex(name = 'V_67',
                type = 'R2',
                particles = [ P.YF3Qd2__tilde__, P.YF3Qd2, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd2] ] ],
                couplings = {(0,0,0):C.R2GC_273_122})

V_68 = CTVertex(name = 'V_68',
                type = 'R2',
                particles = [ P.YF3Qd3__tilde__, P.YF3Qd3, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd3] ] ],
                couplings = {(0,0,0):C.R2GC_273_122})

V_69 = CTVertex(name = 'V_69',
                type = 'R2',
                particles = [ P.YF3Qu1__tilde__, P.YF3Qu1, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qu1] ] ],
                couplings = {(0,0,0):C.R2GC_273_122})

V_70 = CTVertex(name = 'V_70',
                type = 'R2',
                particles = [ P.YF3Qu2__tilde__, P.YF3Qu2, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_273_122})

V_71 = CTVertex(name = 'V_71',
                type = 'R2',
                particles = [ P.YF3Qu3__tilde__, P.YF3Qu3, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_273_122})

V_72 = CTVertex(name = 'V_72',
                type = 'R2',
                particles = [ P.YF3u1__tilde__, P.YF3u1, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3u1] ] ],
                couplings = {(0,0,0):C.R2GC_273_122})

V_73 = CTVertex(name = 'V_73',
                type = 'R2',
                particles = [ P.YF3u2__tilde__, P.YF3u2, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3u2] ] ],
                couplings = {(0,0,0):C.R2GC_273_122})

V_74 = CTVertex(name = 'V_74',
                type = 'R2',
                particles = [ P.YF3u3__tilde__, P.YF3u3, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3u3] ] ],
                couplings = {(0,0,0):C.R2GC_273_122})

V_75 = CTVertex(name = 'V_75',
                type = 'R2',
                particles = [ P.YF3d1__tilde__, P.YF3d1, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3d1] ] ],
                couplings = {(0,0,0):C.R2GC_273_122})

V_76 = CTVertex(name = 'V_76',
                type = 'R2',
                particles = [ P.YF3d2__tilde__, P.YF3d2, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3d2] ] ],
                couplings = {(0,0,0):C.R2GC_273_122})

V_77 = CTVertex(name = 'V_77',
                type = 'R2',
                particles = [ P.YF3d3__tilde__, P.YF3d3, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3d3] ] ],
                couplings = {(0,0,0):C.R2GC_273_122})

V_78 = CTVertex(name = 'V_78',
                type = 'R2',
                particles = [ P.YF3Qd1__tilde__, P.YF3Qu1, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd1, P.YF3Qu1] ] ],
                couplings = {(0,0,0):C.R2GC_336_129})

V_79 = CTVertex(name = 'V_79',
                type = 'R2',
                particles = [ P.YF3Qd2__tilde__, P.YF3Qu2, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd2, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_336_129})

V_80 = CTVertex(name = 'V_80',
                type = 'R2',
                particles = [ P.YF3Qd3__tilde__, P.YF3Qu3, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd3, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_336_129})

V_81 = CTVertex(name = 'V_81',
                type = 'R2',
                particles = [ P.YF3Qu1__tilde__, P.YF3Qd1, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd1, P.YF3Qu1] ] ],
                couplings = {(0,0,0):C.R2GC_336_129})

V_82 = CTVertex(name = 'V_82',
                type = 'R2',
                particles = [ P.YF3Qu2__tilde__, P.YF3Qd2, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd2, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_336_129})

V_83 = CTVertex(name = 'V_83',
                type = 'R2',
                particles = [ P.YF3Qu3__tilde__, P.YF3Qd3, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd3, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_336_129})

V_84 = CTVertex(name = 'V_84',
                type = 'R2',
                particles = [ P.a, P.YS3d1__tilde__, P.YS3d1 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1, L.VSS2 ],
                loop_particles = [ [ [P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_130_8,(0,1,0):C.R2GC_131_9})

V_85 = CTVertex(name = 'V_85',
                type = 'R2',
                particles = [ P.Xd__tilde__, P.d, P.YS3d1__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_337_130})

V_86 = CTVertex(name = 'V_86',
                type = 'R2',
                particles = [ P.Xm, P.d, P.YS3d1__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_337_130})

V_87 = CTVertex(name = 'V_87',
                type = 'R2',
                particles = [ P.g, P.YS3d1__tilde__, P.YS3d1 ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS1, L.VSS2 ],
                loop_particles = [ [ [P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_652_296,(0,1,0):C.R2GC_625_295})

V_88 = CTVertex(name = 'V_88',
                type = 'R2',
                particles = [ P.d__tilde__, P.Xd, P.YS3d1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_337_130})

V_89 = CTVertex(name = 'V_89',
                type = 'R2',
                particles = [ P.d__tilde__, P.Xm, P.YS3d1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_337_130})

V_90 = CTVertex(name = 'V_90',
                type = 'R2',
                particles = [ P.a, P.a, P.YS3d1__tilde__, P.YS3d1 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_132_10})

V_91 = CTVertex(name = 'V_91',
                type = 'R2',
                particles = [ P.a, P.g, P.YS3d1__tilde__, P.YS3d1 ],
                color = [ 'T(2,4,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_667_301})

V_92 = CTVertex(name = 'V_92',
                type = 'R2',
                particles = [ P.g, P.g, P.YS3d1__tilde__, P.YS3d1 ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g] ], [ [P.g, P.YS3d1] ] ],
                couplings = {(2,0,0):C.R2GC_682_305,(2,0,1):C.R2GC_682_306,(1,0,0):C.R2GC_682_305,(1,0,1):C.R2GC_682_306,(0,0,0):C.R2GC_266_117,(0,0,1):C.R2GC_278_124})

V_93 = CTVertex(name = 'V_93',
                type = 'R2',
                particles = [ P.a, P.YS3d2__tilde__, P.YS3d2 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1, L.VSS2 ],
                loop_particles = [ [ [P.g, P.YS3d2] ] ],
                couplings = {(0,0,0):C.R2GC_130_8,(0,1,0):C.R2GC_131_9})

V_94 = CTVertex(name = 'V_94',
                type = 'R2',
                particles = [ P.Xd__tilde__, P.s, P.YS3d2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.YS3d2] ] ],
                couplings = {(0,0,0):C.R2GC_363_138})

V_95 = CTVertex(name = 'V_95',
                type = 'R2',
                particles = [ P.Xm, P.s, P.YS3d2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.YS3d2] ] ],
                couplings = {(0,0,0):C.R2GC_363_138})

V_96 = CTVertex(name = 'V_96',
                type = 'R2',
                particles = [ P.g, P.YS3d2__tilde__, P.YS3d2 ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS1, L.VSS2 ],
                loop_particles = [ [ [P.g, P.YS3d2] ] ],
                couplings = {(0,0,0):C.R2GC_652_296,(0,1,0):C.R2GC_625_295})

V_97 = CTVertex(name = 'V_97',
                type = 'R2',
                particles = [ P.s__tilde__, P.Xd, P.YS3d2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.s, P.YS3d2] ] ],
                couplings = {(0,0,0):C.R2GC_363_138})

V_98 = CTVertex(name = 'V_98',
                type = 'R2',
                particles = [ P.s__tilde__, P.Xm, P.YS3d2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.s, P.YS3d2] ] ],
                couplings = {(0,0,0):C.R2GC_363_138})

V_99 = CTVertex(name = 'V_99',
                type = 'R2',
                particles = [ P.a, P.a, P.YS3d2__tilde__, P.YS3d2 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.YS3d2] ] ],
                couplings = {(0,0,0):C.R2GC_132_10})

V_100 = CTVertex(name = 'V_100',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_667_301})

V_101 = CTVertex(name = 'V_101',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3d2] ] ],
                 couplings = {(2,0,0):C.R2GC_682_305,(2,0,1):C.R2GC_682_306,(1,0,0):C.R2GC_682_305,(1,0,1):C.R2GC_682_306,(0,0,0):C.R2GC_266_117,(0,0,1):C.R2GC_278_124})

V_102 = CTVertex(name = 'V_102',
                 type = 'R2',
                 particles = [ P.a, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_130_8,(0,1,0):C.R2GC_131_9})

V_103 = CTVertex(name = 'V_103',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.b, P.YS3d3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_332_125})

V_104 = CTVertex(name = 'V_104',
                 type = 'R2',
                 particles = [ P.Xm, P.b, P.YS3d3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_332_125})

V_105 = CTVertex(name = 'V_105',
                 type = 'R2',
                 particles = [ P.g, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_652_296,(0,1,0):C.R2GC_625_295})

V_106 = CTVertex(name = 'V_106',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.Xd, P.YS3d3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_332_125})

V_107 = CTVertex(name = 'V_107',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.Xm, P.YS3d3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_332_125})

V_108 = CTVertex(name = 'V_108',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_132_10})

V_109 = CTVertex(name = 'V_109',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_667_301})

V_110 = CTVertex(name = 'V_110',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3d3] ] ],
                 couplings = {(2,0,0):C.R2GC_682_305,(2,0,1):C.R2GC_682_306,(1,0,0):C.R2GC_682_305,(1,0,1):C.R2GC_682_306,(0,0,0):C.R2GC_266_117,(0,0,1):C.R2GC_278_124})

V_111 = CTVertex(name = 'V_111',
                 type = 'R2',
                 particles = [ P.a, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_130_8,(0,1,0):C.R2GC_131_9})

V_112 = CTVertex(name = 'V_112',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.d, P.YS3Qd1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_338_131})

V_113 = CTVertex(name = 'V_113',
                 type = 'R2',
                 particles = [ P.Xm, P.d, P.YS3Qd1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_338_131})

V_114 = CTVertex(name = 'V_114',
                 type = 'R2',
                 particles = [ P.W__minus__, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_344_136,(0,1,0):C.R2GC_342_135})

V_115 = CTVertex(name = 'V_115',
                 type = 'R2',
                 particles = [ P.g, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_652_296,(0,1,0):C.R2GC_625_295})

V_116 = CTVertex(name = 'V_116',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.Xd, P.YS3Qd1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_338_131})

V_117 = CTVertex(name = 'V_117',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.Xm, P.YS3Qd1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_338_131})

V_118 = CTVertex(name = 'V_118',
                 type = 'R2',
                 particles = [ P.W__plus__, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_342_135,(0,1,0):C.R2GC_344_136})

V_119 = CTVertex(name = 'V_119',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_132_10})

V_120 = CTVertex(name = 'V_120',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_340_133,(0,0,1):C.R2GC_340_134})

V_121 = CTVertex(name = 'V_121',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_667_301})

V_122 = CTVertex(name = 'V_122',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(2,0,0):C.R2GC_682_305,(2,0,1):C.R2GC_682_306,(1,0,0):C.R2GC_682_305,(1,0,1):C.R2GC_682_306,(0,0,0):C.R2GC_266_117,(0,0,1):C.R2GC_278_124})

V_123 = CTVertex(name = 'V_123',
                 type = 'R2',
                 particles = [ P.a, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_130_8,(0,1,0):C.R2GC_131_9})

V_124 = CTVertex(name = 'V_124',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.s, P.YS3Qd2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_334_127})

V_125 = CTVertex(name = 'V_125',
                 type = 'R2',
                 particles = [ P.Xm, P.s, P.YS3Qd2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_334_127})

V_126 = CTVertex(name = 'V_126',
                 type = 'R2',
                 particles = [ P.W__minus__, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_344_136,(0,1,0):C.R2GC_342_135})

V_127 = CTVertex(name = 'V_127',
                 type = 'R2',
                 particles = [ P.g, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_652_296,(0,1,0):C.R2GC_625_295})

V_128 = CTVertex(name = 'V_128',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.Xd, P.YS3Qd2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_334_127})

V_129 = CTVertex(name = 'V_129',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.Xm, P.YS3Qd2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_334_127})

V_130 = CTVertex(name = 'V_130',
                 type = 'R2',
                 particles = [ P.W__plus__, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_342_135,(0,1,0):C.R2GC_344_136})

V_131 = CTVertex(name = 'V_131',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_132_10})

V_132 = CTVertex(name = 'V_132',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_340_133,(0,0,1):C.R2GC_340_134})

V_133 = CTVertex(name = 'V_133',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_667_301})

V_134 = CTVertex(name = 'V_134',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(2,0,0):C.R2GC_682_305,(2,0,1):C.R2GC_682_306,(1,0,0):C.R2GC_682_305,(1,0,1):C.R2GC_682_306,(0,0,0):C.R2GC_266_117,(0,0,1):C.R2GC_278_124})

V_135 = CTVertex(name = 'V_135',
                 type = 'R2',
                 particles = [ P.a, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_130_8,(0,1,0):C.R2GC_131_9})

V_136 = CTVertex(name = 'V_136',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.b, P.YS3Qd3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_333_126})

V_137 = CTVertex(name = 'V_137',
                 type = 'R2',
                 particles = [ P.Xm, P.b, P.YS3Qd3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_333_126})

V_138 = CTVertex(name = 'V_138',
                 type = 'R2',
                 particles = [ P.W__minus__, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_344_136,(0,1,0):C.R2GC_342_135})

V_139 = CTVertex(name = 'V_139',
                 type = 'R2',
                 particles = [ P.g, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_652_296,(0,1,0):C.R2GC_625_295})

V_140 = CTVertex(name = 'V_140',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.Xd, P.YS3Qd3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_333_126})

V_141 = CTVertex(name = 'V_141',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.Xm, P.YS3Qd3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_333_126})

V_142 = CTVertex(name = 'V_142',
                 type = 'R2',
                 particles = [ P.W__plus__, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_342_135,(0,1,0):C.R2GC_344_136})

V_143 = CTVertex(name = 'V_143',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_132_10})

V_144 = CTVertex(name = 'V_144',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_340_133,(0,0,1):C.R2GC_340_134})

V_145 = CTVertex(name = 'V_145',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_667_301})

V_146 = CTVertex(name = 'V_146',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(2,0,0):C.R2GC_682_305,(2,0,1):C.R2GC_682_306,(1,0,0):C.R2GC_682_305,(1,0,1):C.R2GC_682_306,(0,0,0):C.R2GC_266_117,(0,0,1):C.R2GC_278_124})

V_147 = CTVertex(name = 'V_147',
                 type = 'R2',
                 particles = [ P.a, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_167_16,(0,1,0):C.R2GC_166_15})

V_148 = CTVertex(name = 'V_148',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.u, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_338_131})

V_149 = CTVertex(name = 'V_149',
                 type = 'R2',
                 particles = [ P.Xm, P.u, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_338_131})

V_150 = CTVertex(name = 'V_150',
                 type = 'R2',
                 particles = [ P.a, P.W__plus__, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_346_137})

V_151 = CTVertex(name = 'V_151',
                 type = 'R2',
                 particles = [ P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_697_311,(0,0,1):C.R2GC_697_312})

V_152 = CTVertex(name = 'V_152',
                 type = 'R2',
                 particles = [ P.g, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_652_296,(0,1,0):C.R2GC_625_295})

V_153 = CTVertex(name = 'V_153',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.Xd, P.YS3Qu1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_338_131})

V_154 = CTVertex(name = 'V_154',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.Xm, P.YS3Qu1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_338_131})

V_155 = CTVertex(name = 'V_155',
                 type = 'R2',
                 particles = [ P.a, P.W__minus__, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_346_137})

V_156 = CTVertex(name = 'V_156',
                 type = 'R2',
                 particles = [ P.g, P.W__minus__, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_697_311,(0,0,1):C.R2GC_697_312})

V_157 = CTVertex(name = 'V_157',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_168_17})

V_158 = CTVertex(name = 'V_158',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,1):C.R2GC_340_133,(0,0,0):C.R2GC_340_134})

V_159 = CTVertex(name = 'V_159',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_673_302})

V_160 = CTVertex(name = 'V_160',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(2,0,0):C.R2GC_682_305,(2,0,1):C.R2GC_682_306,(1,0,0):C.R2GC_682_305,(1,0,1):C.R2GC_682_306,(0,0,0):C.R2GC_266_117,(0,0,1):C.R2GC_278_124})

V_161 = CTVertex(name = 'V_161',
                 type = 'R2',
                 particles = [ P.a, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_167_16,(0,1,0):C.R2GC_166_15})

V_162 = CTVertex(name = 'V_162',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.c, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_334_127})

V_163 = CTVertex(name = 'V_163',
                 type = 'R2',
                 particles = [ P.Xm, P.c, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_334_127})

V_164 = CTVertex(name = 'V_164',
                 type = 'R2',
                 particles = [ P.a, P.W__plus__, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_346_137})

V_165 = CTVertex(name = 'V_165',
                 type = 'R2',
                 particles = [ P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_697_311,(0,0,1):C.R2GC_697_312})

V_166 = CTVertex(name = 'V_166',
                 type = 'R2',
                 particles = [ P.g, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_652_296,(0,1,0):C.R2GC_625_295})

V_167 = CTVertex(name = 'V_167',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.Xd, P.YS3Qu2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_334_127})

V_168 = CTVertex(name = 'V_168',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.Xm, P.YS3Qu2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_334_127})

V_169 = CTVertex(name = 'V_169',
                 type = 'R2',
                 particles = [ P.a, P.W__minus__, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_346_137})

V_170 = CTVertex(name = 'V_170',
                 type = 'R2',
                 particles = [ P.g, P.W__minus__, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_697_311,(0,0,1):C.R2GC_697_312})

V_171 = CTVertex(name = 'V_171',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_168_17})

V_172 = CTVertex(name = 'V_172',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,1):C.R2GC_340_133,(0,0,0):C.R2GC_340_134})

V_173 = CTVertex(name = 'V_173',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_673_302})

V_174 = CTVertex(name = 'V_174',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(2,0,0):C.R2GC_682_305,(2,0,1):C.R2GC_682_306,(1,0,0):C.R2GC_682_305,(1,0,1):C.R2GC_682_306,(0,0,0):C.R2GC_266_117,(0,0,1):C.R2GC_278_124})

V_175 = CTVertex(name = 'V_175',
                 type = 'R2',
                 particles = [ P.a, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_167_16,(0,1,0):C.R2GC_166_15})

V_176 = CTVertex(name = 'V_176',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.t, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_333_126})

V_177 = CTVertex(name = 'V_177',
                 type = 'R2',
                 particles = [ P.Xm, P.t, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_333_126})

V_178 = CTVertex(name = 'V_178',
                 type = 'R2',
                 particles = [ P.a, P.W__plus__, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_346_137})

V_179 = CTVertex(name = 'V_179',
                 type = 'R2',
                 particles = [ P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_697_311,(0,0,1):C.R2GC_697_312})

V_180 = CTVertex(name = 'V_180',
                 type = 'R2',
                 particles = [ P.g, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_652_296,(0,1,0):C.R2GC_625_295})

V_181 = CTVertex(name = 'V_181',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.Xd, P.YS3Qu3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_333_126})

V_182 = CTVertex(name = 'V_182',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.Xm, P.YS3Qu3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_333_126})

V_183 = CTVertex(name = 'V_183',
                 type = 'R2',
                 particles = [ P.a, P.W__minus__, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_346_137})

V_184 = CTVertex(name = 'V_184',
                 type = 'R2',
                 particles = [ P.g, P.W__minus__, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_697_311,(0,0,1):C.R2GC_697_312})

V_185 = CTVertex(name = 'V_185',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_168_17})

V_186 = CTVertex(name = 'V_186',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,1):C.R2GC_340_133,(0,0,0):C.R2GC_340_134})

V_187 = CTVertex(name = 'V_187',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_673_302})

V_188 = CTVertex(name = 'V_188',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(2,0,0):C.R2GC_682_305,(2,0,1):C.R2GC_682_306,(1,0,0):C.R2GC_682_305,(1,0,1):C.R2GC_682_306,(0,0,0):C.R2GC_266_117,(0,0,1):C.R2GC_278_124})

V_189 = CTVertex(name = 'V_189',
                 type = 'R2',
                 particles = [ P.a, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_167_16,(0,1,0):C.R2GC_166_15})

V_190 = CTVertex(name = 'V_190',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.u, P.YS3u1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_367_139})

V_191 = CTVertex(name = 'V_191',
                 type = 'R2',
                 particles = [ P.Xm, P.u, P.YS3u1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_367_139})

V_192 = CTVertex(name = 'V_192',
                 type = 'R2',
                 particles = [ P.g, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_652_296,(0,1,0):C.R2GC_625_295})

V_193 = CTVertex(name = 'V_193',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.Xd, P.YS3u1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_367_139})

V_194 = CTVertex(name = 'V_194',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.Xm, P.YS3u1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_367_139})

V_195 = CTVertex(name = 'V_195',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_168_17})

V_196 = CTVertex(name = 'V_196',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_673_302})

V_197 = CTVertex(name = 'V_197',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3u1] ] ],
                 couplings = {(2,0,0):C.R2GC_682_305,(2,0,1):C.R2GC_682_306,(1,0,0):C.R2GC_682_305,(1,0,1):C.R2GC_682_306,(0,0,0):C.R2GC_266_117,(0,0,1):C.R2GC_278_124})

V_198 = CTVertex(name = 'V_198',
                 type = 'R2',
                 particles = [ P.a, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_167_16,(0,1,0):C.R2GC_166_15})

V_199 = CTVertex(name = 'V_199',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.c, P.YS3u2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_335_128})

V_200 = CTVertex(name = 'V_200',
                 type = 'R2',
                 particles = [ P.Xm, P.c, P.YS3u2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_335_128})

V_201 = CTVertex(name = 'V_201',
                 type = 'R2',
                 particles = [ P.g, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_652_296,(0,1,0):C.R2GC_625_295})

V_202 = CTVertex(name = 'V_202',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.Xd, P.YS3u2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_335_128})

V_203 = CTVertex(name = 'V_203',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.Xm, P.YS3u2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_335_128})

V_204 = CTVertex(name = 'V_204',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_168_17})

V_205 = CTVertex(name = 'V_205',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_673_302})

V_206 = CTVertex(name = 'V_206',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3u2] ] ],
                 couplings = {(2,0,0):C.R2GC_682_305,(2,0,1):C.R2GC_682_306,(1,0,0):C.R2GC_682_305,(1,0,1):C.R2GC_682_306,(0,0,0):C.R2GC_266_117,(0,0,1):C.R2GC_278_124})

V_207 = CTVertex(name = 'V_207',
                 type = 'R2',
                 particles = [ P.a, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_167_16,(0,1,0):C.R2GC_166_15})

V_208 = CTVertex(name = 'V_208',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.t, P.YS3u3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_524_244})

V_209 = CTVertex(name = 'V_209',
                 type = 'R2',
                 particles = [ P.Xm, P.t, P.YS3u3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_524_244})

V_210 = CTVertex(name = 'V_210',
                 type = 'R2',
                 particles = [ P.g, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_652_296,(0,1,0):C.R2GC_625_295})

V_211 = CTVertex(name = 'V_211',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.Xd, P.YS3u3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_524_244})

V_212 = CTVertex(name = 'V_212',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.Xm, P.YS3u3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_524_244})

V_213 = CTVertex(name = 'V_213',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_168_17})

V_214 = CTVertex(name = 'V_214',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_673_302})

V_215 = CTVertex(name = 'V_215',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3u3] ] ],
                 couplings = {(2,0,0):C.R2GC_682_305,(2,0,1):C.R2GC_682_306,(1,0,0):C.R2GC_682_305,(1,0,1):C.R2GC_682_306,(0,0,0):C.R2GC_266_117,(0,0,1):C.R2GC_278_124})

V_216 = CTVertex(name = 'V_216',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_529_246})

V_217 = CTVertex(name = 'V_217',
                 type = 'R2',
                 particles = [ P.YF3Qd1__tilde__, P.YF3Qd1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_214_60})

V_218 = CTVertex(name = 'V_218',
                 type = 'R2',
                 particles = [ P.YF3Qd2__tilde__, P.YF3Qd2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_214_60})

V_219 = CTVertex(name = 'V_219',
                 type = 'R2',
                 particles = [ P.YF3Qd3__tilde__, P.YF3Qd3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_214_60})

V_220 = CTVertex(name = 'V_220',
                 type = 'R2',
                 particles = [ P.YF3Qu1__tilde__, P.YF3Qu1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_215_61})

V_221 = CTVertex(name = 'V_221',
                 type = 'R2',
                 particles = [ P.YF3Qu2__tilde__, P.YF3Qu2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_215_61})

V_222 = CTVertex(name = 'V_222',
                 type = 'R2',
                 particles = [ P.YF3Qu3__tilde__, P.YF3Qu3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_215_61})

V_223 = CTVertex(name = 'V_223',
                 type = 'R2',
                 particles = [ P.YF3d1__tilde__, P.YF3d1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_124_5})

V_224 = CTVertex(name = 'V_224',
                 type = 'R2',
                 particles = [ P.YF3d2__tilde__, P.YF3d2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_124_5})

V_225 = CTVertex(name = 'V_225',
                 type = 'R2',
                 particles = [ P.YF3d3__tilde__, P.YF3d3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_124_5})

V_226 = CTVertex(name = 'V_226',
                 type = 'R2',
                 particles = [ P.YF3u1__tilde__, P.YF3u1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_126_6})

V_227 = CTVertex(name = 'V_227',
                 type = 'R2',
                 particles = [ P.YF3u2__tilde__, P.YF3u2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_126_6})

V_228 = CTVertex(name = 'V_228',
                 type = 'R2',
                 particles = [ P.YF3u3__tilde__, P.YF3u3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_126_6})

V_229 = CTVertex(name = 'V_229',
                 type = 'R2',
                 particles = [ P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_134_12,(0,1,0):C.R2GC_133_11})

V_230 = CTVertex(name = 'V_230',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_135_13})

V_231 = CTVertex(name = 'V_231',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_706_315})

V_232 = CTVertex(name = 'V_232',
                 type = 'R2',
                 particles = [ P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_134_12,(0,1,0):C.R2GC_133_11})

V_233 = CTVertex(name = 'V_233',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_135_13})

V_234 = CTVertex(name = 'V_234',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_706_315})

V_235 = CTVertex(name = 'V_235',
                 type = 'R2',
                 particles = [ P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_134_12,(0,1,0):C.R2GC_133_11})

V_236 = CTVertex(name = 'V_236',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_135_13})

V_237 = CTVertex(name = 'V_237',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_706_315})

V_238 = CTVertex(name = 'V_238',
                 type = 'R2',
                 particles = [ P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_217_62,(0,1,0):C.R2GC_218_63})

V_239 = CTVertex(name = 'V_239',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_219_64})

V_240 = CTVertex(name = 'V_240',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_703_314})

V_241 = CTVertex(name = 'V_241',
                 type = 'R2',
                 particles = [ P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_217_62,(0,1,0):C.R2GC_218_63})

V_242 = CTVertex(name = 'V_242',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_219_64})

V_243 = CTVertex(name = 'V_243',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_703_314})

V_244 = CTVertex(name = 'V_244',
                 type = 'R2',
                 particles = [ P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_217_62,(0,1,0):C.R2GC_218_63})

V_245 = CTVertex(name = 'V_245',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_219_64})

V_246 = CTVertex(name = 'V_246',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_703_314})

V_247 = CTVertex(name = 'V_247',
                 type = 'R2',
                 particles = [ P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_229_66,(0,1,0):C.R2GC_230_67})

V_248 = CTVertex(name = 'V_248',
                 type = 'R2',
                 particles = [ P.W__plus__, P.Z, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_339_132})

V_249 = CTVertex(name = 'V_249',
                 type = 'R2',
                 particles = [ P.W__minus__, P.Z, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_339_132})

V_250 = CTVertex(name = 'V_250',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_231_68})

V_251 = CTVertex(name = 'V_251',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_700_313})

V_252 = CTVertex(name = 'V_252',
                 type = 'R2',
                 particles = [ P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_229_66,(0,1,0):C.R2GC_230_67})

V_253 = CTVertex(name = 'V_253',
                 type = 'R2',
                 particles = [ P.W__plus__, P.Z, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_339_132})

V_254 = CTVertex(name = 'V_254',
                 type = 'R2',
                 particles = [ P.W__minus__, P.Z, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_339_132})

V_255 = CTVertex(name = 'V_255',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_231_68})

V_256 = CTVertex(name = 'V_256',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_700_313})

V_257 = CTVertex(name = 'V_257',
                 type = 'R2',
                 particles = [ P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_229_66,(0,1,0):C.R2GC_230_67})

V_258 = CTVertex(name = 'V_258',
                 type = 'R2',
                 particles = [ P.W__plus__, P.Z, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_339_132})

V_259 = CTVertex(name = 'V_259',
                 type = 'R2',
                 particles = [ P.W__minus__, P.Z, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_339_132})

V_260 = CTVertex(name = 'V_260',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_231_68})

V_261 = CTVertex(name = 'V_261',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_700_313})

V_262 = CTVertex(name = 'V_262',
                 type = 'R2',
                 particles = [ P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_181_18,(0,1,0):C.R2GC_182_19})

V_263 = CTVertex(name = 'V_263',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_183_20})

V_264 = CTVertex(name = 'V_264',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_709_316})

V_265 = CTVertex(name = 'V_265',
                 type = 'R2',
                 particles = [ P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_181_18,(0,1,0):C.R2GC_182_19})

V_266 = CTVertex(name = 'V_266',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_183_20})

V_267 = CTVertex(name = 'V_267',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_709_316})

V_268 = CTVertex(name = 'V_268',
                 type = 'R2',
                 particles = [ P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_181_18,(0,1,0):C.R2GC_182_19})

V_269 = CTVertex(name = 'V_269',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_183_20})

V_270 = CTVertex(name = 'V_270',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_709_316})

V_271 = CTVertex(name = 'V_271',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_136_14})

V_272 = CTVertex(name = 'V_272',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_136_14})

V_273 = CTVertex(name = 'V_273',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_136_14})

V_274 = CTVertex(name = 'V_274',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_220_65})

V_275 = CTVertex(name = 'V_275',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_220_65})

V_276 = CTVertex(name = 'V_276',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_220_65})

V_277 = CTVertex(name = 'V_277',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_232_69})

V_278 = CTVertex(name = 'V_278',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_232_69})

V_279 = CTVertex(name = 'V_279',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_232_69})

V_280 = CTVertex(name = 'V_280',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_184_21})

V_281 = CTVertex(name = 'V_281',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_184_21})

V_282 = CTVertex(name = 'V_282',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_184_21})

V_283 = CTVertex(name = 'V_283',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.YF3Qu1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_553_259})

V_284 = CTVertex(name = 'V_284',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.YF3Qd1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_553_259})

V_285 = CTVertex(name = 'V_285',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.YF3Qu2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_559_262})

V_286 = CTVertex(name = 'V_286',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.YF3Qd2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_559_262})

V_287 = CTVertex(name = 'V_287',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.YF3Qu3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_565_265})

V_288 = CTVertex(name = 'V_288',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.YF3Qd3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_565_265})

V_289 = CTVertex(name = 'V_289',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.YF3Qu1, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_553_259})

V_290 = CTVertex(name = 'V_290',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.YF3Qd1, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_553_259})

V_291 = CTVertex(name = 'V_291',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.YF3Qu2, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_559_262})

V_292 = CTVertex(name = 'V_292',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.YF3Qd2, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_559_262})

V_293 = CTVertex(name = 'V_293',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.YF3Qu3, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_565_265})

V_294 = CTVertex(name = 'V_294',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.YF3Qd3, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_565_265})

V_295 = CTVertex(name = 'V_295',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_274_123})

V_296 = CTVertex(name = 'V_296',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_274_123})

V_297 = CTVertex(name = 'V_297',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_274_123})

V_298 = CTVertex(name = 'V_298',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_272_121})

V_299 = CTVertex(name = 'V_299',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_272_121})

V_300 = CTVertex(name = 'V_300',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_272_121})

V_301 = CTVertex(name = 'V_301',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_273_122})

V_302 = CTVertex(name = 'V_302',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_273_122})

V_303 = CTVertex(name = 'V_303',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_273_122})

V_304 = CTVertex(name = 'V_304',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_273_122})

V_305 = CTVertex(name = 'V_305',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_273_122})

V_306 = CTVertex(name = 'V_306',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_273_122})

V_307 = CTVertex(name = 'V_307',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_336_129})

V_308 = CTVertex(name = 'V_308',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_336_129})

V_309 = CTVertex(name = 'V_309',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_336_129})

V_310 = CTVertex(name = 'V_310',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_336_129})

V_311 = CTVertex(name = 'V_311',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_336_129})

V_312 = CTVertex(name = 'V_312',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_336_129})

V_313 = CTVertex(name = 'V_313',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_215_61,(0,1,0):C.R2GC_126_6})

V_314 = CTVertex(name = 'V_314',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_215_61,(0,1,0):C.R2GC_126_6})

V_315 = CTVertex(name = 'V_315',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_215_61,(0,1,0):C.R2GC_126_6})

V_316 = CTVertex(name = 'V_316',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_214_60,(0,1,0):C.R2GC_124_5})

V_317 = CTVertex(name = 'V_317',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_214_60,(0,1,0):C.R2GC_124_5})

V_318 = CTVertex(name = 'V_318',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_214_60,(0,1,0):C.R2GC_124_5})

V_319 = CTVertex(name = 'V_319',
                 type = 'R2',
                 particles = [ P.YF3Qu1__tilde__, P.u, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_553_259})

V_320 = CTVertex(name = 'V_320',
                 type = 'R2',
                 particles = [ P.YF3Qd1__tilde__, P.d, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_553_259})

V_321 = CTVertex(name = 'V_321',
                 type = 'R2',
                 particles = [ P.YF3Qu2__tilde__, P.c, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_559_262})

V_322 = CTVertex(name = 'V_322',
                 type = 'R2',
                 particles = [ P.YF3Qd2__tilde__, P.s, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_559_262})

V_323 = CTVertex(name = 'V_323',
                 type = 'R2',
                 particles = [ P.YF3Qu3__tilde__, P.t, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_565_265})

V_324 = CTVertex(name = 'V_324',
                 type = 'R2',
                 particles = [ P.YF3Qd3__tilde__, P.b, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_565_265})

V_325 = CTVertex(name = 'V_325',
                 type = 'R2',
                 particles = [ P.YF3Qu1__tilde__, P.u, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_553_259})

V_326 = CTVertex(name = 'V_326',
                 type = 'R2',
                 particles = [ P.YF3Qd1__tilde__, P.d, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_553_259})

V_327 = CTVertex(name = 'V_327',
                 type = 'R2',
                 particles = [ P.YF3Qu2__tilde__, P.c, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_559_262})

V_328 = CTVertex(name = 'V_328',
                 type = 'R2',
                 particles = [ P.YF3Qd2__tilde__, P.s, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_559_262})

V_329 = CTVertex(name = 'V_329',
                 type = 'R2',
                 particles = [ P.YF3Qu3__tilde__, P.t, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_565_265})

V_330 = CTVertex(name = 'V_330',
                 type = 'R2',
                 particles = [ P.YF3Qd3__tilde__, P.b, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_565_265})

V_331 = CTVertex(name = 'V_331',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.YF3d1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_535_250})

V_332 = CTVertex(name = 'V_332',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.YF3d2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_541_253})

V_333 = CTVertex(name = 'V_333',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.YF3d3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_547_256})

V_334 = CTVertex(name = 'V_334',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.YF3u1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_592_271})

V_335 = CTVertex(name = 'V_335',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.YF3u2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_598_274})

V_336 = CTVertex(name = 'V_336',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.YF3u3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_604_277})

V_337 = CTVertex(name = 'V_337',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.YF3d1, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_535_250})

V_338 = CTVertex(name = 'V_338',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.YF3d2, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_541_253})

V_339 = CTVertex(name = 'V_339',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.YF3d3, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_547_256})

V_340 = CTVertex(name = 'V_340',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.YF3u1, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_592_271})

V_341 = CTVertex(name = 'V_341',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.YF3u2, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_598_274})

V_342 = CTVertex(name = 'V_342',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.YF3u3, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_604_277})

V_343 = CTVertex(name = 'V_343',
                 type = 'R2',
                 particles = [ P.YF3d1__tilde__, P.d, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_535_250})

V_344 = CTVertex(name = 'V_344',
                 type = 'R2',
                 particles = [ P.YF3d2__tilde__, P.s, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_541_253})

V_345 = CTVertex(name = 'V_345',
                 type = 'R2',
                 particles = [ P.YF3d3__tilde__, P.b, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_547_256})

V_346 = CTVertex(name = 'V_346',
                 type = 'R2',
                 particles = [ P.YF3u1__tilde__, P.u, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_592_271})

V_347 = CTVertex(name = 'V_347',
                 type = 'R2',
                 particles = [ P.YF3u2__tilde__, P.c, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_598_274})

V_348 = CTVertex(name = 'V_348',
                 type = 'R2',
                 particles = [ P.YF3u3__tilde__, P.t, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_604_277})

V_349 = CTVertex(name = 'V_349',
                 type = 'R2',
                 particles = [ P.YF3d1__tilde__, P.d, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_535_250})

V_350 = CTVertex(name = 'V_350',
                 type = 'R2',
                 particles = [ P.YF3d2__tilde__, P.s, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_541_253})

V_351 = CTVertex(name = 'V_351',
                 type = 'R2',
                 particles = [ P.YF3d3__tilde__, P.b, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_547_256})

V_352 = CTVertex(name = 'V_352',
                 type = 'R2',
                 particles = [ P.YF3u1__tilde__, P.u, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_592_271})

V_353 = CTVertex(name = 'V_353',
                 type = 'R2',
                 particles = [ P.YF3u2__tilde__, P.c, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_598_274})

V_354 = CTVertex(name = 'V_354',
                 type = 'R2',
                 particles = [ P.YF3u3__tilde__, P.t, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_604_277})

V_355 = CTVertex(name = 'V_355',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_123_4})

V_356 = CTVertex(name = 'V_356',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_123_4})

V_357 = CTVertex(name = 'V_357',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_525_245,(0,1,0):C.R2GC_123_4})

V_358 = CTVertex(name = 'V_358',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_123_4})

V_359 = CTVertex(name = 'V_359',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_123_4})

V_360 = CTVertex(name = 'V_360',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_123_4})

V_361 = CTVertex(name = 'V_361',
                 type = 'R2',
                 particles = [ P.YF3Qu1__tilde__, P.YF3Qu1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_573_268,(0,1,0):C.R2GC_123_4})

V_362 = CTVertex(name = 'V_362',
                 type = 'R2',
                 particles = [ P.YF3Qu2__tilde__, P.YF3Qu2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_580_269,(0,1,0):C.R2GC_123_4})

V_363 = CTVertex(name = 'V_363',
                 type = 'R2',
                 particles = [ P.YF3Qu3__tilde__, P.YF3Qu3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_587_270,(0,1,0):C.R2GC_123_4})

V_364 = CTVertex(name = 'V_364',
                 type = 'R2',
                 particles = [ P.YF3Qd1__tilde__, P.YF3Qd1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_555_261,(0,1,0):C.R2GC_123_4})

V_365 = CTVertex(name = 'V_365',
                 type = 'R2',
                 particles = [ P.YF3Qd2__tilde__, P.YF3Qd2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_561_264,(0,1,0):C.R2GC_123_4})

V_366 = CTVertex(name = 'V_366',
                 type = 'R2',
                 particles = [ P.YF3Qd3__tilde__, P.YF3Qd3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_567_267,(0,1,0):C.R2GC_123_4})

V_367 = CTVertex(name = 'V_367',
                 type = 'R2',
                 particles = [ P.YF3u1__tilde__, P.YF3u1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_594_273,(0,1,0):C.R2GC_123_4})

V_368 = CTVertex(name = 'V_368',
                 type = 'R2',
                 particles = [ P.YF3u2__tilde__, P.YF3u2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_600_276,(0,1,0):C.R2GC_123_4})

V_369 = CTVertex(name = 'V_369',
                 type = 'R2',
                 particles = [ P.YF3u3__tilde__, P.YF3u3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_606_279,(0,1,0):C.R2GC_123_4})

V_370 = CTVertex(name = 'V_370',
                 type = 'R2',
                 particles = [ P.YF3d1__tilde__, P.YF3d1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_537_252,(0,1,0):C.R2GC_123_4})

V_371 = CTVertex(name = 'V_371',
                 type = 'R2',
                 particles = [ P.YF3d2__tilde__, P.YF3d2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_543_255,(0,1,0):C.R2GC_123_4})

V_372 = CTVertex(name = 'V_372',
                 type = 'R2',
                 particles = [ P.YF3d3__tilde__, P.YF3d3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_549_258,(0,1,0):C.R2GC_123_4})

V_373 = CTVertex(name = 'V_373',
                 type = 'R2',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_614_286,(0,1,0):C.R2GC_129_7})

V_374 = CTVertex(name = 'V_374',
                 type = 'R2',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_615_287,(0,1,0):C.R2GC_129_7})

V_375 = CTVertex(name = 'V_375',
                 type = 'R2',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_616_288,(0,1,0):C.R2GC_129_7})

V_376 = CTVertex(name = 'V_376',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_611_283,(0,1,0):C.R2GC_129_7})

V_377 = CTVertex(name = 'V_377',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_612_284,(0,1,0):C.R2GC_129_7})

V_378 = CTVertex(name = 'V_378',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_613_285,(0,1,0):C.R2GC_129_7})

V_379 = CTVertex(name = 'V_379',
                 type = 'R2',
                 particles = [ P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_617_289,(0,1,0):C.R2GC_129_7})

V_380 = CTVertex(name = 'V_380',
                 type = 'R2',
                 particles = [ P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_618_290,(0,1,0):C.R2GC_129_7})

V_381 = CTVertex(name = 'V_381',
                 type = 'R2',
                 particles = [ P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_712_317,(0,1,0):C.R2GC_129_7})

V_382 = CTVertex(name = 'V_382',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_608_280,(0,1,0):C.R2GC_129_7})

V_383 = CTVertex(name = 'V_383',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_609_281,(0,1,0):C.R2GC_129_7})

V_384 = CTVertex(name = 'V_384',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_610_282,(0,1,0):C.R2GC_129_7})

V_385 = CTVertex(name = 'V_385',
                 type = 'R2',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV2, L.VV3 ],
                 loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u], [P.YF3d1], [P.YF3d2], [P.YF3d3], [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3], [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3], [P.YF3u1], [P.YF3u2], [P.YF3u3] ], [ [P.g] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ] ],
                 couplings = {(0,2,1):C.R2GC_120_1,(0,0,2):C.R2GC_210_29,(0,0,3):C.R2GC_210_30,(0,0,4):C.R2GC_210_31,(0,0,5):C.R2GC_210_32,(0,0,6):C.R2GC_210_33,(0,0,7):C.R2GC_210_34,(0,0,8):C.R2GC_210_35,(0,0,9):C.R2GC_210_36,(0,0,10):C.R2GC_210_37,(0,0,11):C.R2GC_210_38,(0,0,12):C.R2GC_210_39,(0,0,13):C.R2GC_210_40,(0,0,14):C.R2GC_210_41,(0,1,0):C.R2GC_207_24})

V_386 = CTVertex(name = 'V_386',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVS1 ],
                 loop_particles = [ [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_121_2})

V_387 = CTVertex(name = 'V_387',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Xv, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV5 ],
                 loop_particles = [ [ [P.b, P.YF3d3] ], [ [P.b, P.YF3Qd3], [P.t, P.YF3Qu3] ], [ [P.c, P.YF3Qu2], [P.s, P.YF3Qd2] ], [ [P.c, P.YF3u2] ], [ [P.d, P.YF3d1] ], [ [P.d, P.YF3Qd1], [P.u, P.YF3Qu1] ], [ [P.s, P.YF3d2] ], [ [P.t, P.YF3u3] ], [ [P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_244_79,(0,0,1):C.R2GC_244_80,(0,0,2):C.R2GC_244_81,(0,0,3):C.R2GC_244_82,(0,0,4):C.R2GC_244_83,(0,0,5):C.R2GC_244_84,(0,0,6):C.R2GC_244_85,(0,0,7):C.R2GC_244_86,(0,0,8):C.R2GC_244_87})

V_388 = CTVertex(name = 'V_388',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Xv, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV5 ],
                 loop_particles = [ [ [P.b, P.YF3d3] ], [ [P.b, P.YF3Qd3], [P.t, P.YF3Qu3] ], [ [P.c, P.YF3Qu2], [P.s, P.YF3Qd2] ], [ [P.c, P.YF3u2] ], [ [P.d, P.YF3d1] ], [ [P.d, P.YF3Qd1], [P.u, P.YF3Qu1] ], [ [P.s, P.YF3d2] ], [ [P.t, P.YF3u3] ], [ [P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_243_70,(0,0,1):C.R2GC_243_71,(0,0,2):C.R2GC_243_72,(0,0,3):C.R2GC_243_73,(0,0,4):C.R2GC_243_74,(0,0,5):C.R2GC_243_75,(0,0,6):C.R2GC_243_76,(0,0,7):C.R2GC_243_77,(0,0,8):C.R2GC_243_78})

V_389 = CTVertex(name = 'V_389',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Xv, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV5 ],
                 loop_particles = [ [ [P.b, P.YF3d3] ], [ [P.b, P.YF3Qd3], [P.t, P.YF3Qu3] ], [ [P.c, P.YF3Qu2], [P.s, P.YF3Qd2] ], [ [P.c, P.YF3u2] ], [ [P.d, P.YF3d1] ], [ [P.d, P.YF3Qd1], [P.u, P.YF3Qu1] ], [ [P.s, P.YF3d2] ], [ [P.t, P.YF3u3] ], [ [P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_243_70,(0,0,1):C.R2GC_243_71,(0,0,2):C.R2GC_243_72,(0,0,3):C.R2GC_243_73,(0,0,4):C.R2GC_243_74,(0,0,5):C.R2GC_243_75,(0,0,6):C.R2GC_243_76,(0,0,7):C.R2GC_243_77,(0,0,8):C.R2GC_243_78})

V_390 = CTVertex(name = 'V_390',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Xw__tilde__, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV5 ],
                 loop_particles = [ [ [P.b, P.YF3d3] ], [ [P.b, P.YF3Qd3], [P.t, P.YF3Qu3] ], [ [P.c, P.YF3Qu2], [P.s, P.YF3Qd2] ], [ [P.c, P.YF3u2] ], [ [P.d, P.YF3d1] ], [ [P.d, P.YF3Qd1], [P.u, P.YF3Qu1] ], [ [P.s, P.YF3d2] ], [ [P.t, P.YF3u3] ], [ [P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_243_70,(0,0,1):C.R2GC_243_71,(0,0,2):C.R2GC_243_72,(0,0,3):C.R2GC_243_73,(0,0,4):C.R2GC_243_74,(0,0,5):C.R2GC_243_75,(0,0,6):C.R2GC_243_76,(0,0,7):C.R2GC_243_77,(0,0,8):C.R2GC_243_78})

V_391 = CTVertex(name = 'V_391',
                 type = 'R2',
                 particles = [ P.a, P.a, P.g, P.g ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVVV5 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s], [P.YF3d1], [P.YF3d2], [P.YF3d3], [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3] ], [ [P.c], [P.t], [P.u], [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3], [P.YF3u1], [P.YF3u2], [P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_208_25,(0,0,1):C.R2GC_208_26})

V_392 = CTVertex(name = 'V_392',
                 type = 'R2',
                 particles = [ P.a, P.g, P.g, P.Z ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VVVV5 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.YF3d1], [P.YF3d2], [P.YF3d3] ], [ [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3] ], [ [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3] ], [ [P.YF3u1], [P.YF3u2], [P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_211_42,(0,0,1):C.R2GC_211_43,(0,0,2):C.R2GC_211_44,(0,0,3):C.R2GC_211_45,(0,0,4):C.R2GC_211_46,(0,0,5):C.R2GC_211_47})

V_393 = CTVertex(name = 'V_393',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Z, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV5 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.YF3d1], [P.YF3d2], [P.YF3d3] ], [ [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3] ], [ [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3] ], [ [P.YF3u1], [P.YF3u2], [P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_213_54,(0,0,1):C.R2GC_213_55,(0,0,2):C.R2GC_213_56,(0,0,3):C.R2GC_213_57,(0,0,4):C.R2GC_213_58,(0,0,5):C.R2GC_213_59})

V_394 = CTVertex(name = 'V_394',
                 type = 'R2',
                 particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV5 ],
                 loop_particles = [ [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ], [ [P.YF3Qd1, P.YF3Qu1], [P.YF3Qd2, P.YF3Qu2], [P.YF3Qd3, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_247_106,(0,0,1):C.R2GC_247_107})

V_395 = CTVertex(name = 'V_395',
                 type = 'R2',
                 particles = [ P.a, P.g, P.g, P.g ],
                 color = [ 'd(2,3,4)' ],
                 lorentz = [ L.VVVV5 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s], [P.YF3d1], [P.YF3d2], [P.YF3d3], [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3] ], [ [P.c], [P.t], [P.u], [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3], [P.YF3u1], [P.YF3u2], [P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_209_27,(0,0,1):C.R2GC_209_28})

V_396 = CTVertex(name = 'V_396',
                 type = 'R2',
                 particles = [ P.g, P.g, P.g, P.Z ],
                 color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                 lorentz = [ L.VVVV1, L.VVVV5 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.YF3d1], [P.YF3d2], [P.YF3d3] ], [ [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3] ], [ [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3] ], [ [P.YF3u1], [P.YF3u2], [P.YF3u3] ] ],
                 couplings = {(1,0,0):C.R2GC_206_22,(1,0,1):C.R2GC_206_23,(0,1,0):C.R2GC_212_48,(0,1,1):C.R2GC_212_49,(0,1,2):C.R2GC_212_50,(0,1,3):C.R2GC_212_51,(0,1,4):C.R2GC_212_52,(0,1,5):C.R2GC_212_53})

V_397 = CTVertex(name = 'V_397',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_122_3})

V_398 = CTVertex(name = 'V_398',
                 type = 'R2',
                 particles = [ P.g, P.g, P.G0, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_122_3})

V_399 = CTVertex(name = 'V_399',
                 type = 'R2',
                 particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_122_3})

V_400 = CTVertex(name = 'V_400',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Xs, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.YF3d3] ], [ [P.b, P.YF3Qd3], [P.t, P.YF3Qu3] ], [ [P.c, P.YF3Qu2], [P.s, P.YF3Qd2] ], [ [P.c, P.YF3u2] ], [ [P.d, P.YF3d1] ], [ [P.d, P.YF3Qd1], [P.u, P.YF3Qu1] ], [ [P.s, P.YF3d2] ], [ [P.t, P.YF3u3] ], [ [P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_246_97,(0,0,1):C.R2GC_246_98,(0,0,2):C.R2GC_246_99,(0,0,3):C.R2GC_246_100,(0,0,4):C.R2GC_246_101,(0,0,5):C.R2GC_246_102,(0,0,6):C.R2GC_246_103,(0,0,7):C.R2GC_246_104,(0,0,8):C.R2GC_246_105})

V_401 = CTVertex(name = 'V_401',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Xc, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.YF3d3] ], [ [P.b, P.YF3Qd3], [P.t, P.YF3Qu3] ], [ [P.c, P.YF3Qu2], [P.s, P.YF3Qd2] ], [ [P.c, P.YF3u2] ], [ [P.d, P.YF3d1] ], [ [P.d, P.YF3Qd1], [P.u, P.YF3Qu1] ], [ [P.s, P.YF3d2] ], [ [P.t, P.YF3u3] ], [ [P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_245_88,(0,0,1):C.R2GC_245_89,(0,0,2):C.R2GC_245_90,(0,0,3):C.R2GC_245_91,(0,0,4):C.R2GC_245_92,(0,0,5):C.R2GC_245_93,(0,0,6):C.R2GC_245_94,(0,0,7):C.R2GC_245_95,(0,0,8):C.R2GC_245_96})

V_402 = CTVertex(name = 'V_402',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Xc__tilde__, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.YF3d3] ], [ [P.b, P.YF3Qd3], [P.t, P.YF3Qu3] ], [ [P.c, P.YF3Qu2], [P.s, P.YF3Qd2] ], [ [P.c, P.YF3u2] ], [ [P.d, P.YF3d1] ], [ [P.d, P.YF3Qd1], [P.u, P.YF3Qu1] ], [ [P.s, P.YF3d2] ], [ [P.t, P.YF3u3] ], [ [P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_245_88,(0,0,1):C.R2GC_245_89,(0,0,2):C.R2GC_245_90,(0,0,3):C.R2GC_245_91,(0,0,4):C.R2GC_245_92,(0,0,5):C.R2GC_245_93,(0,0,6):C.R2GC_245_94,(0,0,7):C.R2GC_245_95,(0,0,8):C.R2GC_245_96})

V_403 = CTVertex(name = 'V_403',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Xc__tilde__, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.YF3d3] ], [ [P.b, P.YF3Qd3], [P.t, P.YF3Qu3] ], [ [P.c, P.YF3Qu2], [P.s, P.YF3Qd2] ], [ [P.c, P.YF3u2] ], [ [P.d, P.YF3d1] ], [ [P.d, P.YF3Qd1], [P.u, P.YF3Qu1] ], [ [P.s, P.YF3d2] ], [ [P.t, P.YF3u3] ], [ [P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_245_88,(0,0,1):C.R2GC_245_89,(0,0,2):C.R2GC_245_90,(0,0,3):C.R2GC_245_91,(0,0,4):C.R2GC_245_92,(0,0,5):C.R2GC_245_93,(0,0,6):C.R2GC_245_94,(0,0,7):C.R2GC_245_95,(0,0,8):C.R2GC_245_96})

V_404 = CTVertex(name = 'V_404',
                 type = 'R2',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3Qu1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_371_140,(1,0,0):C.R2GC_377_148,(1,0,3):C.R2GC_371_142,(1,0,5):C.R2GC_377_149,(1,0,1):C.R2GC_377_150,(1,0,4):C.R2GC_377_151,(0,0,2):C.R2GC_371_140,(0,0,0):C.R2GC_377_148,(0,0,3):C.R2GC_371_142,(0,0,5):C.R2GC_377_149,(0,0,1):C.R2GC_377_150,(0,0,4):C.R2GC_377_151})

V_405 = CTVertex(name = 'V_405',
                 type = 'R2',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qu1, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu1, P.YS3Qu2] ], [ [P.g, P.YS3Qu1, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_450_222,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_450_223,(1,0,1):C.R2GC_450_224,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_450_225,(1,0,2):C.R2GC_450_226,(1,0,6):C.R2GC_450_227,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_449_216,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_449_217,(0,0,1):C.R2GC_449_218,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_449_219,(0,0,2):C.R2GC_449_220,(0,0,6):C.R2GC_449_221})

V_406 = CTVertex(name = 'V_406',
                 type = 'R2',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3Qu2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_371_140,(1,0,0):C.R2GC_377_148,(1,0,3):C.R2GC_371_142,(1,0,5):C.R2GC_377_149,(1,0,1):C.R2GC_377_150,(1,0,4):C.R2GC_377_151,(0,0,2):C.R2GC_371_140,(0,0,0):C.R2GC_377_148,(0,0,3):C.R2GC_371_142,(0,0,5):C.R2GC_377_149,(0,0,1):C.R2GC_377_150,(0,0,4):C.R2GC_377_151})

V_407 = CTVertex(name = 'V_407',
                 type = 'R2',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qu1, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qu1, P.YS3Qu3] ], [ [P.g, P.YS3Qu1, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_450_222,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_450_223,(1,0,1):C.R2GC_450_224,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_450_225,(1,0,2):C.R2GC_450_226,(1,0,6):C.R2GC_450_227,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_449_216,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_449_217,(0,0,1):C.R2GC_449_218,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_449_219,(0,0,2):C.R2GC_449_220,(0,0,6):C.R2GC_449_221})

V_408 = CTVertex(name = 'V_408',
                 type = 'R2',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qu2, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qu2, P.YS3Qu3] ], [ [P.g, P.YS3Qu2, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_450_222,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_450_223,(1,0,1):C.R2GC_450_224,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_450_225,(1,0,2):C.R2GC_450_226,(1,0,6):C.R2GC_450_227,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_449_216,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_449_217,(0,0,1):C.R2GC_449_218,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_449_219,(0,0,2):C.R2GC_449_220,(0,0,6):C.R2GC_449_221})

V_409 = CTVertex(name = 'V_409',
                 type = 'R2',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3Qu3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_371_140,(1,0,0):C.R2GC_377_148,(1,0,3):C.R2GC_371_142,(1,0,5):C.R2GC_377_149,(1,0,1):C.R2GC_377_150,(1,0,4):C.R2GC_377_151,(0,0,2):C.R2GC_371_140,(0,0,0):C.R2GC_377_148,(0,0,3):C.R2GC_371_142,(0,0,5):C.R2GC_377_149,(0,0,1):C.R2GC_377_150,(0,0,4):C.R2GC_377_151})

V_410 = CTVertex(name = 'V_410',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qu1] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_406_194,(1,0,4):C.R2GC_383_154,(1,0,7):C.R2GC_390_171,(1,0,11):C.R2GC_444_211,(1,0,1):C.R2GC_406_196,(1,0,5):C.R2GC_444_212,(1,0,8):C.R2GC_390_174,(1,0,10):C.R2GC_444_213,(1,0,2):C.R2GC_406_198,(1,0,6):C.R2GC_444_214,(1,0,9):C.R2GC_444_215,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_371_141,(0,0,4):C.R2GC_384_157,(0,0,7):C.R2GC_389_162,(0,0,11):C.R2GC_443_206,(0,0,1):C.R2GC_208_25,(0,0,5):C.R2GC_443_207,(0,0,8):C.R2GC_389_165,(0,0,10):C.R2GC_443_208,(0,0,2):C.R2GC_405_192,(0,0,6):C.R2GC_443_209,(0,0,9):C.R2GC_443_210})

V_411 = CTVertex(name = 'V_411',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd1, P.YS3Qu2] ], [ [P.g, P.YS3Qd1, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_406_194,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_444_211,(1,0,1):C.R2GC_406_196,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_444_213,(1,0,2):C.R2GC_406_198,(1,0,6):C.R2GC_444_215,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_371_141,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_443_206,(0,0,1):C.R2GC_208_25,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_443_208,(0,0,2):C.R2GC_405_192,(0,0,6):C.R2GC_443_210})

V_412 = CTVertex(name = 'V_412',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd1, P.YS3Qu3] ], [ [P.g, P.YS3Qd1, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_406_194,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_444_211,(1,0,1):C.R2GC_406_196,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_444_213,(1,0,2):C.R2GC_406_198,(1,0,6):C.R2GC_444_215,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_371_141,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_443_206,(0,0,1):C.R2GC_208_25,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_443_208,(0,0,2):C.R2GC_405_192,(0,0,6):C.R2GC_443_210})

V_413 = CTVertex(name = 'V_413',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qd1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_371_140,(1,0,0):C.R2GC_371_141,(1,0,3):C.R2GC_371_142,(1,0,5):C.R2GC_374_146,(1,0,1):C.R2GC_371_144,(1,0,4):C.R2GC_374_147,(0,0,2):C.R2GC_371_140,(0,0,0):C.R2GC_371_141,(0,0,3):C.R2GC_371_142,(0,0,5):C.R2GC_374_146,(0,0,1):C.R2GC_371_144,(0,0,4):C.R2GC_374_147})

V_414 = CTVertex(name = 'V_414',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd2, P.YS3Qu1, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu2] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu2] ] ],
                 couplings = {(1,0,0):C.R2GC_383_154,(1,0,1):C.R2GC_383_155,(1,0,2):C.R2GC_383_156,(0,0,0):C.R2GC_384_157,(0,0,1):C.R2GC_384_158,(0,0,2):C.R2GC_384_159})

V_415 = CTVertex(name = 'V_415',
                 type = 'R2',
                 particles = [ P.YS3Qd1, P.YS3Qd2__tilde__, P.YS3Qu1__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu2] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu2] ] ],
                 couplings = {(1,0,0):C.R2GC_383_154,(1,0,1):C.R2GC_383_155,(1,0,2):C.R2GC_383_156,(0,0,0):C.R2GC_384_157,(0,0,1):C.R2GC_384_158,(0,0,2):C.R2GC_384_159})

V_416 = CTVertex(name = 'V_416',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd2, P.YS3Qu1] ], [ [P.g, P.YS3Qd2, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_406_194,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_444_211,(1,0,1):C.R2GC_406_196,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_444_213,(1,0,2):C.R2GC_406_198,(1,0,6):C.R2GC_444_215,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_371_141,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_443_206,(0,0,1):C.R2GC_208_25,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_443_208,(0,0,2):C.R2GC_405_192,(0,0,6):C.R2GC_443_210})

V_417 = CTVertex(name = 'V_417',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qu2] ], [ [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_406_194,(1,0,4):C.R2GC_383_154,(1,0,7):C.R2GC_390_171,(1,0,11):C.R2GC_444_211,(1,0,1):C.R2GC_406_196,(1,0,5):C.R2GC_444_212,(1,0,8):C.R2GC_390_174,(1,0,10):C.R2GC_444_213,(1,0,2):C.R2GC_406_198,(1,0,6):C.R2GC_444_214,(1,0,9):C.R2GC_444_215,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_371_141,(0,0,4):C.R2GC_384_157,(0,0,7):C.R2GC_389_162,(0,0,11):C.R2GC_443_206,(0,0,1):C.R2GC_208_25,(0,0,5):C.R2GC_443_207,(0,0,8):C.R2GC_389_165,(0,0,10):C.R2GC_443_208,(0,0,2):C.R2GC_405_192,(0,0,6):C.R2GC_443_209,(0,0,9):C.R2GC_443_210})

V_418 = CTVertex(name = 'V_418',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd2, P.YS3Qu3] ], [ [P.g, P.YS3Qd2, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_406_194,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_444_211,(1,0,1):C.R2GC_406_196,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_444_213,(1,0,2):C.R2GC_406_198,(1,0,6):C.R2GC_444_215,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_371_141,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_443_206,(0,0,1):C.R2GC_208_25,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_443_208,(0,0,2):C.R2GC_405_192,(0,0,6):C.R2GC_443_210})

V_419 = CTVertex(name = 'V_419',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd1, P.YS3Qd2] ], [ [P.g, P.YS3Qd1, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_390_170,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_402_187,(1,0,1):C.R2GC_390_173,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_402_188,(1,0,2):C.R2GC_390_176,(1,0,6):C.R2GC_402_189,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_389_161,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_401_184,(0,0,1):C.R2GC_389_164,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_401_185,(0,0,2):C.R2GC_389_167,(0,0,6):C.R2GC_401_186})

V_420 = CTVertex(name = 'V_420',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qd2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_371_140,(1,0,0):C.R2GC_371_141,(1,0,3):C.R2GC_371_142,(1,0,5):C.R2GC_374_146,(1,0,1):C.R2GC_371_144,(1,0,4):C.R2GC_374_147,(0,0,2):C.R2GC_371_140,(0,0,0):C.R2GC_371_141,(0,0,3):C.R2GC_371_142,(0,0,5):C.R2GC_374_146,(0,0,1):C.R2GC_371_144,(0,0,4):C.R2GC_374_147})

V_421 = CTVertex(name = 'V_421',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd3, P.YS3Qu1, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.R2GC_383_154,(1,0,1):C.R2GC_383_155,(1,0,2):C.R2GC_383_156,(0,0,0):C.R2GC_384_157,(0,0,1):C.R2GC_384_158,(0,0,2):C.R2GC_384_159})

V_422 = CTVertex(name = 'V_422',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd3, P.YS3Qu2, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu2, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.R2GC_383_154,(1,0,1):C.R2GC_383_155,(1,0,2):C.R2GC_383_156,(0,0,0):C.R2GC_384_157,(0,0,1):C.R2GC_384_158,(0,0,2):C.R2GC_384_159})

V_423 = CTVertex(name = 'V_423',
                 type = 'R2',
                 particles = [ P.YS3Qd1, P.YS3Qd3__tilde__, P.YS3Qu1__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.R2GC_383_154,(1,0,1):C.R2GC_383_155,(1,0,2):C.R2GC_383_156,(0,0,0):C.R2GC_384_157,(0,0,1):C.R2GC_384_158,(0,0,2):C.R2GC_384_159})

V_424 = CTVertex(name = 'V_424',
                 type = 'R2',
                 particles = [ P.YS3Qd2, P.YS3Qd3__tilde__, P.YS3Qu2__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu2, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.R2GC_383_154,(1,0,1):C.R2GC_383_155,(1,0,2):C.R2GC_383_156,(0,0,0):C.R2GC_384_157,(0,0,1):C.R2GC_384_158,(0,0,2):C.R2GC_384_159})

V_425 = CTVertex(name = 'V_425',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3Qd3, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd3, P.YS3Qu1] ], [ [P.g, P.YS3Qd3, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_406_194,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_444_211,(1,0,1):C.R2GC_406_196,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_444_213,(1,0,2):C.R2GC_406_198,(1,0,6):C.R2GC_444_215,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_371_141,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_443_206,(0,0,1):C.R2GC_208_25,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_443_208,(0,0,2):C.R2GC_405_192,(0,0,6):C.R2GC_443_210})

V_426 = CTVertex(name = 'V_426',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qd3, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd3, P.YS3Qu2] ], [ [P.g, P.YS3Qd3, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_406_194,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_444_211,(1,0,1):C.R2GC_406_196,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_444_213,(1,0,2):C.R2GC_406_198,(1,0,6):C.R2GC_444_215,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_371_141,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_443_206,(0,0,1):C.R2GC_208_25,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_443_208,(0,0,2):C.R2GC_405_192,(0,0,6):C.R2GC_443_210})

V_427 = CTVertex(name = 'V_427',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_406_194,(1,0,4):C.R2GC_383_154,(1,0,7):C.R2GC_390_171,(1,0,11):C.R2GC_444_211,(1,0,1):C.R2GC_406_196,(1,0,5):C.R2GC_444_212,(1,0,8):C.R2GC_390_174,(1,0,10):C.R2GC_444_213,(1,0,2):C.R2GC_406_198,(1,0,6):C.R2GC_444_214,(1,0,9):C.R2GC_444_215,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_371_141,(0,0,4):C.R2GC_384_157,(0,0,7):C.R2GC_389_162,(0,0,11):C.R2GC_443_206,(0,0,1):C.R2GC_208_25,(0,0,5):C.R2GC_443_207,(0,0,8):C.R2GC_389_165,(0,0,10):C.R2GC_443_208,(0,0,2):C.R2GC_405_192,(0,0,6):C.R2GC_443_209,(0,0,9):C.R2GC_443_210})

V_428 = CTVertex(name = 'V_428',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd1, P.YS3Qd3] ], [ [P.g, P.YS3Qd1, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_390_170,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_402_187,(1,0,1):C.R2GC_390_173,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_402_188,(1,0,2):C.R2GC_390_176,(1,0,6):C.R2GC_402_189,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_389_161,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_401_184,(0,0,1):C.R2GC_389_164,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_401_185,(0,0,2):C.R2GC_389_167,(0,0,6):C.R2GC_401_186})

V_429 = CTVertex(name = 'V_429',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd2, P.YS3Qd3] ], [ [P.g, P.YS3Qd2, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_390_170,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_402_187,(1,0,1):C.R2GC_390_173,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_402_188,(1,0,2):C.R2GC_390_176,(1,0,6):C.R2GC_402_189,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_389_161,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_401_184,(0,0,1):C.R2GC_389_164,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_401_185,(0,0,2):C.R2GC_389_167,(0,0,6):C.R2GC_401_186})

V_430 = CTVertex(name = 'V_430',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qd3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_371_140,(1,0,0):C.R2GC_371_141,(1,0,3):C.R2GC_371_142,(1,0,5):C.R2GC_374_146,(1,0,1):C.R2GC_371_144,(1,0,4):C.R2GC_374_147,(0,0,2):C.R2GC_371_140,(0,0,0):C.R2GC_371_141,(0,0,3):C.R2GC_371_142,(0,0,5):C.R2GC_374_146,(0,0,1):C.R2GC_371_144,(0,0,4):C.R2GC_374_147})

V_431 = CTVertex(name = 'V_431',
                 type = 'R2',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qu1, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qu1, P.YS3u1] ], [ [P.g, P.YS3Qu1, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_450_222,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_454_231,(1,0,1):C.R2GC_450_224,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_454_232,(1,0,2):C.R2GC_450_226,(1,0,6):C.R2GC_454_233,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_449_216,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_453_228,(0,0,1):C.R2GC_449_218,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_453_229,(0,0,2):C.R2GC_449_220,(0,0,6):C.R2GC_453_230})

V_432 = CTVertex(name = 'V_432',
                 type = 'R2',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qu2, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qu2, P.YS3u1] ], [ [P.g, P.YS3Qu2, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_450_222,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_454_231,(1,0,1):C.R2GC_450_224,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_454_232,(1,0,2):C.R2GC_450_226,(1,0,6):C.R2GC_454_233,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_449_216,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_453_228,(0,0,1):C.R2GC_449_218,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_453_229,(0,0,2):C.R2GC_449_220,(0,0,6):C.R2GC_453_230})

V_433 = CTVertex(name = 'V_433',
                 type = 'R2',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qu3, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qu3], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qu3, P.YS3u1] ], [ [P.g, P.YS3Qu3, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qu3, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_450_222,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_454_231,(1,0,1):C.R2GC_450_224,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_454_232,(1,0,2):C.R2GC_450_226,(1,0,6):C.R2GC_454_233,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_449_216,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_453_228,(0,0,1):C.R2GC_449_218,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_453_229,(0,0,2):C.R2GC_449_220,(0,0,6):C.R2GC_453_230})

V_434 = CTVertex(name = 'V_434',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qd1, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qd1, P.YS3u1] ], [ [P.g, P.YS3Qd1, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_406_194,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_406_195,(1,0,1):C.R2GC_406_196,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_406_197,(1,0,2):C.R2GC_406_198,(1,0,6):C.R2GC_406_199,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_371_141,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_405_190,(0,0,1):C.R2GC_208_25,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_405_191,(0,0,2):C.R2GC_405_192,(0,0,6):C.R2GC_405_193})

V_435 = CTVertex(name = 'V_435',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qd2, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qd2, P.YS3u1] ], [ [P.g, P.YS3Qd2, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_406_194,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_406_195,(1,0,1):C.R2GC_406_196,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_406_197,(1,0,2):C.R2GC_406_198,(1,0,6):C.R2GC_406_199,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_371_141,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_405_190,(0,0,1):C.R2GC_208_25,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_405_191,(0,0,2):C.R2GC_405_192,(0,0,6):C.R2GC_405_193})

V_436 = CTVertex(name = 'V_436',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qd3, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qd3, P.YS3u1] ], [ [P.g, P.YS3Qd3, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_406_194,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_406_195,(1,0,1):C.R2GC_406_196,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_406_197,(1,0,2):C.R2GC_406_198,(1,0,6):C.R2GC_406_199,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_371_141,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_405_190,(0,0,1):C.R2GC_208_25,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_405_191,(0,0,2):C.R2GC_405_192,(0,0,6):C.R2GC_405_193})

V_437 = CTVertex(name = 'V_437',
                 type = 'R2',
                 particles = [ P.YS3u1__tilde__, P.YS3u1__tilde__, P.YS3u1, P.YS3u1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3u1] ], [ [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_371_140,(1,0,0):C.R2GC_377_148,(1,0,3):C.R2GC_371_142,(1,0,5):C.R2GC_380_152,(1,0,1):C.R2GC_377_150,(1,0,4):C.R2GC_380_153,(0,0,2):C.R2GC_371_140,(0,0,0):C.R2GC_377_148,(0,0,3):C.R2GC_371_142,(0,0,5):C.R2GC_380_152,(0,0,1):C.R2GC_377_150,(0,0,4):C.R2GC_380_153})

V_438 = CTVertex(name = 'V_438',
                 type = 'R2',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qu1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qu1, P.YS3u2] ], [ [P.g, P.YS3Qu1, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_450_222,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_454_231,(1,0,1):C.R2GC_450_224,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_454_232,(1,0,2):C.R2GC_450_226,(1,0,6):C.R2GC_454_233,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_449_216,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_453_228,(0,0,1):C.R2GC_449_218,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_453_229,(0,0,2):C.R2GC_449_220,(0,0,6):C.R2GC_453_230})

V_439 = CTVertex(name = 'V_439',
                 type = 'R2',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qu2, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qu2, P.YS3u2] ], [ [P.g, P.YS3Qu2, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_450_222,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_454_231,(1,0,1):C.R2GC_450_224,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_454_232,(1,0,2):C.R2GC_450_226,(1,0,6):C.R2GC_454_233,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_449_216,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_453_228,(0,0,1):C.R2GC_449_218,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_453_229,(0,0,2):C.R2GC_449_220,(0,0,6):C.R2GC_453_230})

V_440 = CTVertex(name = 'V_440',
                 type = 'R2',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qu3, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qu3], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qu3, P.YS3u2] ], [ [P.g, P.YS3Qu3, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qu3, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_450_222,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_454_231,(1,0,1):C.R2GC_450_224,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_454_232,(1,0,2):C.R2GC_450_226,(1,0,6):C.R2GC_454_233,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_449_216,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_453_228,(0,0,1):C.R2GC_449_218,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_453_229,(0,0,2):C.R2GC_449_220,(0,0,6):C.R2GC_453_230})

V_441 = CTVertex(name = 'V_441',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qd1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qd1, P.YS3u2] ], [ [P.g, P.YS3Qd1, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_406_194,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_406_195,(1,0,1):C.R2GC_406_196,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_406_197,(1,0,2):C.R2GC_406_198,(1,0,6):C.R2GC_406_199,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_371_141,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_405_190,(0,0,1):C.R2GC_208_25,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_405_191,(0,0,2):C.R2GC_405_192,(0,0,6):C.R2GC_405_193})

V_442 = CTVertex(name = 'V_442',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qd2, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qd2, P.YS3u2] ], [ [P.g, P.YS3Qd2, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_406_194,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_406_195,(1,0,1):C.R2GC_406_196,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_406_197,(1,0,2):C.R2GC_406_198,(1,0,6):C.R2GC_406_199,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_371_141,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_405_190,(0,0,1):C.R2GC_208_25,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_405_191,(0,0,2):C.R2GC_405_192,(0,0,6):C.R2GC_405_193})

V_443 = CTVertex(name = 'V_443',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qd3, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qd3, P.YS3u2] ], [ [P.g, P.YS3Qd3, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_406_194,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_406_195,(1,0,1):C.R2GC_406_196,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_406_197,(1,0,2):C.R2GC_406_198,(1,0,6):C.R2GC_406_199,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_371_141,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_405_190,(0,0,1):C.R2GC_208_25,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_405_191,(0,0,2):C.R2GC_405_192,(0,0,6):C.R2GC_405_193})

V_444 = CTVertex(name = 'V_444',
                 type = 'R2',
                 particles = [ P.YS3u1__tilde__, P.YS3u1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3u1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3u1], [P.g, P.YS3u2] ], [ [P.g, P.YS3u1, P.YS3u2] ], [ [P.g, P.YS3u1, P.YS3u2, P.Z] ], [ [P.g, P.YS3u1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_450_222,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_504_241,(1,0,1):C.R2GC_450_224,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_504_242,(1,0,2):C.R2GC_450_226,(1,0,6):C.R2GC_504_243,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_449_216,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_503_238,(0,0,1):C.R2GC_449_218,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_503_239,(0,0,2):C.R2GC_449_220,(0,0,6):C.R2GC_503_240})

V_445 = CTVertex(name = 'V_445',
                 type = 'R2',
                 particles = [ P.YS3u2__tilde__, P.YS3u2__tilde__, P.YS3u2, P.YS3u2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3u2] ], [ [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_371_140,(1,0,0):C.R2GC_377_148,(1,0,3):C.R2GC_371_142,(1,0,5):C.R2GC_380_152,(1,0,1):C.R2GC_377_150,(1,0,4):C.R2GC_380_153,(0,0,2):C.R2GC_371_140,(0,0,0):C.R2GC_377_148,(0,0,3):C.R2GC_371_142,(0,0,5):C.R2GC_380_152,(0,0,1):C.R2GC_377_150,(0,0,4):C.R2GC_380_153})

V_446 = CTVertex(name = 'V_446',
                 type = 'R2',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qu1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qu1, P.YS3u3] ], [ [P.g, P.YS3Qu1, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_450_222,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_454_231,(1,0,1):C.R2GC_450_224,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_454_232,(1,0,2):C.R2GC_450_226,(1,0,6):C.R2GC_454_233,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_449_216,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_453_228,(0,0,1):C.R2GC_449_218,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_453_229,(0,0,2):C.R2GC_449_220,(0,0,6):C.R2GC_453_230})

V_447 = CTVertex(name = 'V_447',
                 type = 'R2',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qu2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qu2, P.YS3u3] ], [ [P.g, P.YS3Qu2, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_450_222,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_454_231,(1,0,1):C.R2GC_450_224,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_454_232,(1,0,2):C.R2GC_450_226,(1,0,6):C.R2GC_454_233,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_449_216,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_453_228,(0,0,1):C.R2GC_449_218,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_453_229,(0,0,2):C.R2GC_449_220,(0,0,6):C.R2GC_453_230})

V_448 = CTVertex(name = 'V_448',
                 type = 'R2',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qu3, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qu3], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qu3, P.YS3u3] ], [ [P.g, P.YS3Qu3, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qu3, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_450_222,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_454_231,(1,0,1):C.R2GC_450_224,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_454_232,(1,0,2):C.R2GC_450_226,(1,0,6):C.R2GC_454_233,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_449_216,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_453_228,(0,0,1):C.R2GC_449_218,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_453_229,(0,0,2):C.R2GC_449_220,(0,0,6):C.R2GC_453_230})

V_449 = CTVertex(name = 'V_449',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qd1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qd1, P.YS3u3] ], [ [P.g, P.YS3Qd1, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_406_194,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_406_195,(1,0,1):C.R2GC_406_196,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_406_197,(1,0,2):C.R2GC_406_198,(1,0,6):C.R2GC_406_199,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_371_141,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_405_190,(0,0,1):C.R2GC_208_25,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_405_191,(0,0,2):C.R2GC_405_192,(0,0,6):C.R2GC_405_193})

V_450 = CTVertex(name = 'V_450',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qd2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qd2, P.YS3u3] ], [ [P.g, P.YS3Qd2, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_406_194,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_406_195,(1,0,1):C.R2GC_406_196,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_406_197,(1,0,2):C.R2GC_406_198,(1,0,6):C.R2GC_406_199,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_371_141,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_405_190,(0,0,1):C.R2GC_208_25,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_405_191,(0,0,2):C.R2GC_405_192,(0,0,6):C.R2GC_405_193})

V_451 = CTVertex(name = 'V_451',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qd3, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qd3, P.YS3u3] ], [ [P.g, P.YS3Qd3, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_406_194,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_406_195,(1,0,1):C.R2GC_406_196,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_406_197,(1,0,2):C.R2GC_406_198,(1,0,6):C.R2GC_406_199,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_371_141,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_405_190,(0,0,1):C.R2GC_208_25,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_405_191,(0,0,2):C.R2GC_405_192,(0,0,6):C.R2GC_405_193})

V_452 = CTVertex(name = 'V_452',
                 type = 'R2',
                 particles = [ P.YS3u1__tilde__, P.YS3u1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3u1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3u1], [P.g, P.YS3u3] ], [ [P.g, P.YS3u1, P.YS3u3] ], [ [P.g, P.YS3u1, P.YS3u3, P.Z] ], [ [P.g, P.YS3u1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_450_222,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_504_241,(1,0,1):C.R2GC_450_224,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_504_242,(1,0,2):C.R2GC_450_226,(1,0,6):C.R2GC_504_243,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_449_216,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_503_238,(0,0,1):C.R2GC_449_218,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_503_239,(0,0,2):C.R2GC_449_220,(0,0,6):C.R2GC_503_240})

V_453 = CTVertex(name = 'V_453',
                 type = 'R2',
                 particles = [ P.YS3u2__tilde__, P.YS3u2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3u2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3u2], [P.g, P.YS3u3] ], [ [P.g, P.YS3u2, P.YS3u3] ], [ [P.g, P.YS3u2, P.YS3u3, P.Z] ], [ [P.g, P.YS3u2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_450_222,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_504_241,(1,0,1):C.R2GC_450_224,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_504_242,(1,0,2):C.R2GC_450_226,(1,0,6):C.R2GC_504_243,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_449_216,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_503_238,(0,0,1):C.R2GC_449_218,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_503_239,(0,0,2):C.R2GC_449_220,(0,0,6):C.R2GC_503_240})

V_454 = CTVertex(name = 'V_454',
                 type = 'R2',
                 particles = [ P.YS3u3__tilde__, P.YS3u3__tilde__, P.YS3u3, P.YS3u3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3u3] ], [ [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_371_140,(1,0,0):C.R2GC_377_148,(1,0,3):C.R2GC_371_142,(1,0,5):C.R2GC_380_152,(1,0,1):C.R2GC_377_150,(1,0,4):C.R2GC_380_153,(0,0,2):C.R2GC_371_140,(0,0,0):C.R2GC_377_148,(0,0,3):C.R2GC_371_142,(0,0,5):C.R2GC_380_152,(0,0,1):C.R2GC_377_150,(0,0,4):C.R2GC_380_153})

V_455 = CTVertex(name = 'V_455',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3d1, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3d1, P.YS3Qu1] ], [ [P.g, P.YS3d1, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_406_194,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_438_203,(1,0,1):C.R2GC_406_196,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_438_204,(1,0,2):C.R2GC_406_198,(1,0,6):C.R2GC_438_205,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_371_141,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_437_200,(0,0,1):C.R2GC_208_25,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_437_201,(0,0,2):C.R2GC_405_192,(0,0,6):C.R2GC_437_202})

V_456 = CTVertex(name = 'V_456',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3d1, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3d1, P.YS3Qu2] ], [ [P.g, P.YS3d1, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_406_194,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_438_203,(1,0,1):C.R2GC_406_196,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_438_204,(1,0,2):C.R2GC_406_198,(1,0,6):C.R2GC_438_205,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_371_141,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_437_200,(0,0,1):C.R2GC_208_25,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_437_201,(0,0,2):C.R2GC_405_192,(0,0,6):C.R2GC_437_202})

V_457 = CTVertex(name = 'V_457',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3d1, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3d1, P.YS3Qu3] ], [ [P.g, P.YS3d1, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_406_194,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_438_203,(1,0,1):C.R2GC_406_196,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_438_204,(1,0,2):C.R2GC_406_198,(1,0,6):C.R2GC_438_205,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_371_141,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_437_200,(0,0,1):C.R2GC_208_25,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_437_201,(0,0,2):C.R2GC_405_192,(0,0,6):C.R2GC_437_202})

V_458 = CTVertex(name = 'V_458',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qd1] ], [ [P.a, P.g, P.YS3d1, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qd1] ], [ [P.g, P.YS3d1, P.YS3Qd1] ], [ [P.g, P.YS3d1, P.YS3Qd1, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_390_170,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_396_181,(1,0,1):C.R2GC_390_173,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_396_182,(1,0,2):C.R2GC_390_176,(1,0,6):C.R2GC_396_183,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_389_161,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_395_178,(0,0,1):C.R2GC_389_164,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_395_179,(0,0,2):C.R2GC_389_167,(0,0,6):C.R2GC_395_180})

V_459 = CTVertex(name = 'V_459',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3d1, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3d1, P.YS3Qd2] ], [ [P.g, P.YS3d1, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_390_170,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_396_181,(1,0,1):C.R2GC_390_173,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_396_182,(1,0,2):C.R2GC_390_176,(1,0,6):C.R2GC_396_183,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_389_161,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_395_178,(0,0,1):C.R2GC_389_164,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_395_179,(0,0,2):C.R2GC_389_167,(0,0,6):C.R2GC_395_180})

V_460 = CTVertex(name = 'V_460',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3d1, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3d1, P.YS3Qd3] ], [ [P.g, P.YS3d1, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_390_170,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_396_181,(1,0,1):C.R2GC_390_173,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_396_182,(1,0,2):C.R2GC_390_176,(1,0,6):C.R2GC_396_183,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_389_161,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_395_178,(0,0,1):C.R2GC_389_164,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_395_179,(0,0,2):C.R2GC_389_167,(0,0,6):C.R2GC_395_180})

V_461 = CTVertex(name = 'V_461',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3d1, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3u1] ], [ [P.g, P.YS3d1, P.YS3u1] ], [ [P.g, P.YS3d1, P.YS3u1, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_406_194,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_498_235,(1,0,1):C.R2GC_406_196,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_498_236,(1,0,2):C.R2GC_406_198,(1,0,6):C.R2GC_498_237,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_371_141,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_371_143,(0,0,1):C.R2GC_208_25,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_213_56,(0,0,2):C.R2GC_405_192,(0,0,6):C.R2GC_497_234})

V_462 = CTVertex(name = 'V_462',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3d1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3u2] ], [ [P.g, P.YS3d1, P.YS3u2] ], [ [P.g, P.YS3d1, P.YS3u2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_406_194,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_498_235,(1,0,1):C.R2GC_406_196,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_498_236,(1,0,2):C.R2GC_406_198,(1,0,6):C.R2GC_498_237,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_371_141,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_371_143,(0,0,1):C.R2GC_208_25,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_213_56,(0,0,2):C.R2GC_405_192,(0,0,6):C.R2GC_497_234})

V_463 = CTVertex(name = 'V_463',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3d1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3u3] ], [ [P.g, P.YS3d1, P.YS3u3] ], [ [P.g, P.YS3d1, P.YS3u3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_406_194,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_498_235,(1,0,1):C.R2GC_406_196,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_498_236,(1,0,2):C.R2GC_406_198,(1,0,6):C.R2GC_498_237,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_371_141,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_371_143,(0,0,1):C.R2GC_208_25,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_213_56,(0,0,2):C.R2GC_405_192,(0,0,6):C.R2GC_497_234})

V_464 = CTVertex(name = 'V_464',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1__tilde__, P.YS3d1, P.YS3d1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1] ], [ [P.g] ], [ [P.g, P.YS3d1] ], [ [P.g, P.YS3d1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_371_140,(1,0,0):C.R2GC_371_141,(1,0,3):C.R2GC_371_142,(1,0,5):C.R2GC_371_143,(1,0,1):C.R2GC_371_144,(1,0,4):C.R2GC_371_145,(0,0,2):C.R2GC_371_140,(0,0,0):C.R2GC_371_141,(0,0,3):C.R2GC_371_142,(0,0,5):C.R2GC_371_143,(0,0,1):C.R2GC_371_144,(0,0,4):C.R2GC_371_145})

V_465 = CTVertex(name = 'V_465',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3d2, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3d2, P.YS3Qu1] ], [ [P.g, P.YS3d2, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_406_194,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_438_203,(1,0,1):C.R2GC_406_196,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_438_204,(1,0,2):C.R2GC_406_198,(1,0,6):C.R2GC_438_205,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_371_141,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_437_200,(0,0,1):C.R2GC_208_25,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_437_201,(0,0,2):C.R2GC_405_192,(0,0,6):C.R2GC_437_202})

V_466 = CTVertex(name = 'V_466',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3d2, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3d2, P.YS3Qu2] ], [ [P.g, P.YS3d2, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_406_194,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_438_203,(1,0,1):C.R2GC_406_196,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_438_204,(1,0,2):C.R2GC_406_198,(1,0,6):C.R2GC_438_205,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_371_141,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_437_200,(0,0,1):C.R2GC_208_25,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_437_201,(0,0,2):C.R2GC_405_192,(0,0,6):C.R2GC_437_202})

V_467 = CTVertex(name = 'V_467',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3d2, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3d2, P.YS3Qu3] ], [ [P.g, P.YS3d2, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_406_194,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_438_203,(1,0,1):C.R2GC_406_196,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_438_204,(1,0,2):C.R2GC_406_198,(1,0,6):C.R2GC_438_205,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_371_141,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_437_200,(0,0,1):C.R2GC_208_25,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_437_201,(0,0,2):C.R2GC_405_192,(0,0,6):C.R2GC_437_202})

V_468 = CTVertex(name = 'V_468',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qd1] ], [ [P.a, P.g, P.YS3d2, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qd1] ], [ [P.g, P.YS3d2, P.YS3Qd1] ], [ [P.g, P.YS3d2, P.YS3Qd1, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_390_170,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_396_181,(1,0,1):C.R2GC_390_173,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_396_182,(1,0,2):C.R2GC_390_176,(1,0,6):C.R2GC_396_183,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_389_161,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_395_178,(0,0,1):C.R2GC_389_164,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_395_179,(0,0,2):C.R2GC_389_167,(0,0,6):C.R2GC_395_180})

V_469 = CTVertex(name = 'V_469',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3d2, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3d2, P.YS3Qd2] ], [ [P.g, P.YS3d2, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_390_170,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_396_181,(1,0,1):C.R2GC_390_173,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_396_182,(1,0,2):C.R2GC_390_176,(1,0,6):C.R2GC_396_183,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_389_161,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_395_178,(0,0,1):C.R2GC_389_164,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_395_179,(0,0,2):C.R2GC_389_167,(0,0,6):C.R2GC_395_180})

V_470 = CTVertex(name = 'V_470',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3d2, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3d2, P.YS3Qd3] ], [ [P.g, P.YS3d2, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_390_170,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_396_181,(1,0,1):C.R2GC_390_173,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_396_182,(1,0,2):C.R2GC_390_176,(1,0,6):C.R2GC_396_183,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_389_161,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_395_178,(0,0,1):C.R2GC_389_164,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_395_179,(0,0,2):C.R2GC_389_167,(0,0,6):C.R2GC_395_180})

V_471 = CTVertex(name = 'V_471',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3d2, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3u1] ], [ [P.g, P.YS3d2, P.YS3u1] ], [ [P.g, P.YS3d2, P.YS3u1, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_406_194,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_498_235,(1,0,1):C.R2GC_406_196,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_498_236,(1,0,2):C.R2GC_406_198,(1,0,6):C.R2GC_498_237,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_371_141,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_371_143,(0,0,1):C.R2GC_208_25,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_213_56,(0,0,2):C.R2GC_405_192,(0,0,6):C.R2GC_497_234})

V_472 = CTVertex(name = 'V_472',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3d2, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3u2] ], [ [P.g, P.YS3d2, P.YS3u2] ], [ [P.g, P.YS3d2, P.YS3u2, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_406_194,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_498_235,(1,0,1):C.R2GC_406_196,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_498_236,(1,0,2):C.R2GC_406_198,(1,0,6):C.R2GC_498_237,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_371_141,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_371_143,(0,0,1):C.R2GC_208_25,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_213_56,(0,0,2):C.R2GC_405_192,(0,0,6):C.R2GC_497_234})

V_473 = CTVertex(name = 'V_473',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3d2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3u3] ], [ [P.g, P.YS3d2, P.YS3u3] ], [ [P.g, P.YS3d2, P.YS3u3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_406_194,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_498_235,(1,0,1):C.R2GC_406_196,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_498_236,(1,0,2):C.R2GC_406_198,(1,0,6):C.R2GC_498_237,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_371_141,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_371_143,(0,0,1):C.R2GC_208_25,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_213_56,(0,0,2):C.R2GC_405_192,(0,0,6):C.R2GC_497_234})

V_474 = CTVertex(name = 'V_474',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3d2] ], [ [P.a, P.g, P.YS3d1, P.YS3d2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3d2] ], [ [P.g, P.YS3d1, P.YS3d2] ], [ [P.g, P.YS3d1, P.YS3d2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3d2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_390_170,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_390_172,(1,0,1):C.R2GC_390_173,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_390_175,(1,0,2):C.R2GC_390_176,(1,0,6):C.R2GC_390_177,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_389_161,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_389_163,(0,0,1):C.R2GC_389_164,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_389_166,(0,0,2):C.R2GC_389_167,(0,0,6):C.R2GC_389_168})

V_475 = CTVertex(name = 'V_475',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2__tilde__, P.YS3d2, P.YS3d2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2] ], [ [P.g] ], [ [P.g, P.YS3d2] ], [ [P.g, P.YS3d2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_371_140,(1,0,0):C.R2GC_371_141,(1,0,3):C.R2GC_371_142,(1,0,5):C.R2GC_371_143,(1,0,1):C.R2GC_371_144,(1,0,4):C.R2GC_371_145,(0,0,2):C.R2GC_371_140,(0,0,0):C.R2GC_371_141,(0,0,3):C.R2GC_371_142,(0,0,5):C.R2GC_371_143,(0,0,1):C.R2GC_371_144,(0,0,4):C.R2GC_371_145})

V_476 = CTVertex(name = 'V_476',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3d3, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3d3, P.YS3Qu1] ], [ [P.g, P.YS3d3, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_406_194,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_438_203,(1,0,1):C.R2GC_406_196,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_438_204,(1,0,2):C.R2GC_406_198,(1,0,6):C.R2GC_438_205,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_371_141,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_437_200,(0,0,1):C.R2GC_208_25,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_437_201,(0,0,2):C.R2GC_405_192,(0,0,6):C.R2GC_437_202})

V_477 = CTVertex(name = 'V_477',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3d3, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3d3, P.YS3Qu2] ], [ [P.g, P.YS3d3, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_406_194,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_438_203,(1,0,1):C.R2GC_406_196,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_438_204,(1,0,2):C.R2GC_406_198,(1,0,6):C.R2GC_438_205,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_371_141,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_437_200,(0,0,1):C.R2GC_208_25,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_437_201,(0,0,2):C.R2GC_405_192,(0,0,6):C.R2GC_437_202})

V_478 = CTVertex(name = 'V_478',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3d3, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3d3, P.YS3Qu3] ], [ [P.g, P.YS3d3, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_406_194,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_438_203,(1,0,1):C.R2GC_406_196,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_438_204,(1,0,2):C.R2GC_406_198,(1,0,6):C.R2GC_438_205,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_371_141,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_437_200,(0,0,1):C.R2GC_208_25,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_437_201,(0,0,2):C.R2GC_405_192,(0,0,6):C.R2GC_437_202})

V_479 = CTVertex(name = 'V_479',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qd1] ], [ [P.a, P.g, P.YS3d3, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qd1] ], [ [P.g, P.YS3d3, P.YS3Qd1] ], [ [P.g, P.YS3d3, P.YS3Qd1, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_390_170,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_396_181,(1,0,1):C.R2GC_390_173,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_396_182,(1,0,2):C.R2GC_390_176,(1,0,6):C.R2GC_396_183,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_389_161,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_395_178,(0,0,1):C.R2GC_389_164,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_395_179,(0,0,2):C.R2GC_389_167,(0,0,6):C.R2GC_395_180})

V_480 = CTVertex(name = 'V_480',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3d3, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3d3, P.YS3Qd2] ], [ [P.g, P.YS3d3, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_390_170,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_396_181,(1,0,1):C.R2GC_390_173,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_396_182,(1,0,2):C.R2GC_390_176,(1,0,6):C.R2GC_396_183,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_389_161,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_395_178,(0,0,1):C.R2GC_389_164,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_395_179,(0,0,2):C.R2GC_389_167,(0,0,6):C.R2GC_395_180})

V_481 = CTVertex(name = 'V_481',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3d3, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3d3, P.YS3Qd3] ], [ [P.g, P.YS3d3, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_390_170,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_396_181,(1,0,1):C.R2GC_390_173,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_396_182,(1,0,2):C.R2GC_390_176,(1,0,6):C.R2GC_396_183,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_389_161,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_395_178,(0,0,1):C.R2GC_389_164,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_395_179,(0,0,2):C.R2GC_389_167,(0,0,6):C.R2GC_395_180})

V_482 = CTVertex(name = 'V_482',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3d3, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3u1] ], [ [P.g, P.YS3d3, P.YS3u1] ], [ [P.g, P.YS3d3, P.YS3u1, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_406_194,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_498_235,(1,0,1):C.R2GC_406_196,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_498_236,(1,0,2):C.R2GC_406_198,(1,0,6):C.R2GC_498_237,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_371_141,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_371_143,(0,0,1):C.R2GC_208_25,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_213_56,(0,0,2):C.R2GC_405_192,(0,0,6):C.R2GC_497_234})

V_483 = CTVertex(name = 'V_483',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3d3, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3u2] ], [ [P.g, P.YS3d3, P.YS3u2] ], [ [P.g, P.YS3d3, P.YS3u2, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_406_194,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_498_235,(1,0,1):C.R2GC_406_196,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_498_236,(1,0,2):C.R2GC_406_198,(1,0,6):C.R2GC_498_237,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_371_141,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_371_143,(0,0,1):C.R2GC_208_25,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_213_56,(0,0,2):C.R2GC_405_192,(0,0,6):C.R2GC_497_234})

V_484 = CTVertex(name = 'V_484',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3d3, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3u3] ], [ [P.g, P.YS3d3, P.YS3u3] ], [ [P.g, P.YS3d3, P.YS3u3, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_406_194,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_498_235,(1,0,1):C.R2GC_406_196,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_498_236,(1,0,2):C.R2GC_406_198,(1,0,6):C.R2GC_498_237,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_371_141,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_371_143,(0,0,1):C.R2GC_208_25,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_213_56,(0,0,2):C.R2GC_405_192,(0,0,6):C.R2GC_497_234})

V_485 = CTVertex(name = 'V_485',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3d3] ], [ [P.a, P.g, P.YS3d1, P.YS3d3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3d3] ], [ [P.g, P.YS3d1, P.YS3d3] ], [ [P.g, P.YS3d1, P.YS3d3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3d3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_390_170,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_390_172,(1,0,1):C.R2GC_390_173,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_390_175,(1,0,2):C.R2GC_390_176,(1,0,6):C.R2GC_390_177,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_389_161,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_389_163,(0,0,1):C.R2GC_389_164,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_389_166,(0,0,2):C.R2GC_389_167,(0,0,6):C.R2GC_389_168})

V_486 = CTVertex(name = 'V_486',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3d3] ], [ [P.a, P.g, P.YS3d2, P.YS3d3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3d3] ], [ [P.g, P.YS3d2, P.YS3d3] ], [ [P.g, P.YS3d2, P.YS3d3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3d3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_390_169,(1,0,0):C.R2GC_390_170,(1,0,4):C.R2GC_390_171,(1,0,8):C.R2GC_390_172,(1,0,1):C.R2GC_390_173,(1,0,5):C.R2GC_390_174,(1,0,7):C.R2GC_390_175,(1,0,2):C.R2GC_390_176,(1,0,6):C.R2GC_390_177,(0,0,3):C.R2GC_389_160,(0,0,0):C.R2GC_389_161,(0,0,4):C.R2GC_389_162,(0,0,8):C.R2GC_389_163,(0,0,1):C.R2GC_389_164,(0,0,5):C.R2GC_389_165,(0,0,7):C.R2GC_389_166,(0,0,2):C.R2GC_389_167,(0,0,6):C.R2GC_389_168})

V_487 = CTVertex(name = 'V_487',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3__tilde__, P.YS3d3, P.YS3d3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3] ], [ [P.g] ], [ [P.g, P.YS3d3] ], [ [P.g, P.YS3d3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_371_140,(1,0,0):C.R2GC_371_141,(1,0,3):C.R2GC_371_142,(1,0,5):C.R2GC_371_143,(1,0,1):C.R2GC_371_144,(1,0,4):C.R2GC_371_145,(0,0,2):C.R2GC_371_140,(0,0,0):C.R2GC_371_141,(0,0,3):C.R2GC_371_142,(0,0,5):C.R2GC_371_143,(0,0,1):C.R2GC_371_144,(0,0,4):C.R2GC_371_145})

V_488 = CTVertex(name = 'V_488',
                 type = 'UV',
                 particles = [ P.g, P.g, P.g ],
                 color = [ 'f(1,2,3)' ],
                 lorentz = [ L.VVV1, L.VVV2, L.VVV3, L.VVV4, L.VVV5, L.VVV6, L.VVV7, L.VVV8, L.VVV9 ],
                 loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d1], [P.YS3d2], [P.YS3d3], [P.YS3Qd1], [P.YS3Qd2], [P.YS3Qd3], [P.YS3Qu1], [P.YS3Qu2], [P.YS3Qu3], [P.YS3u1], [P.YS3u2], [P.YS3u3] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,3):C.UVGC_664_398,(0,0,0):C.UVGC_664_399,(0,0,1):C.UVGC_664_400,(0,0,2):C.UVGC_261_8,(0,0,4):C.UVGC_664_401,(0,0,5):C.UVGC_664_402,(0,0,6):C.UVGC_664_403,(0,0,7):C.UVGC_664_404,(0,0,8):C.UVGC_664_405,(0,0,9):C.UVGC_664_406,(0,0,10):C.UVGC_664_407,(0,0,11):C.UVGC_664_408,(0,0,12):C.UVGC_664_409,(0,0,13):C.UVGC_664_410,(0,0,14):C.UVGC_664_411,(0,0,15):C.UVGC_664_412,(0,0,16):C.UVGC_664_413,(0,0,17):C.UVGC_664_414,(0,0,19):C.UVGC_664_415,(0,0,20):C.UVGC_664_416,(0,0,21):C.UVGC_664_417,(0,0,22):C.UVGC_664_418,(0,0,23):C.UVGC_664_419,(0,0,24):C.UVGC_664_420,(0,0,25):C.UVGC_664_421,(0,0,26):C.UVGC_664_422,(0,0,27):C.UVGC_664_423,(0,0,28):C.UVGC_664_424,(0,0,29):C.UVGC_664_425,(0,1,3):C.UVGC_619_287,(0,1,0):C.UVGC_619_288,(0,1,1):C.UVGC_619_289,(0,1,2):C.UVGC_619_290,(0,1,4):C.UVGC_619_291,(0,1,5):C.UVGC_619_292,(0,1,6):C.UVGC_619_293,(0,1,7):C.UVGC_619_294,(0,1,8):C.UVGC_619_295,(0,1,9):C.UVGC_619_296,(0,1,10):C.UVGC_619_297,(0,1,11):C.UVGC_619_298,(0,1,12):C.UVGC_619_299,(0,1,13):C.UVGC_619_300,(0,1,14):C.UVGC_619_301,(0,1,15):C.UVGC_619_302,(0,1,16):C.UVGC_619_303,(0,1,17):C.UVGC_619_304,(0,1,19):C.UVGC_619_305,(0,1,20):C.UVGC_619_306,(0,1,21):C.UVGC_619_307,(0,1,22):C.UVGC_619_308,(0,1,23):C.UVGC_619_309,(0,1,24):C.UVGC_619_310,(0,1,25):C.UVGC_619_311,(0,1,26):C.UVGC_619_312,(0,1,27):C.UVGC_619_313,(0,1,28):C.UVGC_619_314,(0,1,29):C.UVGC_619_315,(0,3,3):C.UVGC_619_287,(0,3,0):C.UVGC_619_288,(0,3,1):C.UVGC_621_329,(0,3,2):C.UVGC_269_22,(0,3,4):C.UVGC_619_291,(0,3,5):C.UVGC_619_292,(0,3,6):C.UVGC_619_293,(0,3,7):C.UVGC_619_294,(0,3,8):C.UVGC_619_295,(0,3,9):C.UVGC_619_296,(0,3,10):C.UVGC_619_297,(0,3,11):C.UVGC_619_298,(0,3,12):C.UVGC_619_299,(0,3,13):C.UVGC_619_300,(0,3,14):C.UVGC_619_301,(0,3,15):C.UVGC_619_302,(0,3,16):C.UVGC_619_303,(0,3,17):C.UVGC_620_317,(0,3,19):C.UVGC_620_318,(0,3,20):C.UVGC_620_319,(0,3,21):C.UVGC_620_320,(0,3,22):C.UVGC_620_321,(0,3,23):C.UVGC_620_322,(0,3,24):C.UVGC_620_323,(0,3,25):C.UVGC_620_324,(0,3,26):C.UVGC_620_325,(0,3,27):C.UVGC_620_326,(0,3,28):C.UVGC_620_327,(0,3,29):C.UVGC_620_328,(0,5,3):C.UVGC_664_398,(0,5,0):C.UVGC_664_399,(0,5,1):C.UVGC_665_426,(0,5,4):C.UVGC_664_401,(0,5,5):C.UVGC_664_402,(0,5,6):C.UVGC_664_403,(0,5,7):C.UVGC_664_404,(0,5,8):C.UVGC_664_405,(0,5,9):C.UVGC_664_406,(0,5,10):C.UVGC_664_407,(0,5,11):C.UVGC_664_408,(0,5,12):C.UVGC_664_409,(0,5,13):C.UVGC_664_410,(0,5,14):C.UVGC_664_411,(0,5,15):C.UVGC_664_412,(0,5,16):C.UVGC_664_413,(0,5,17):C.UVGC_665_427,(0,5,19):C.UVGC_665_428,(0,5,20):C.UVGC_665_429,(0,5,21):C.UVGC_665_430,(0,5,22):C.UVGC_665_431,(0,5,23):C.UVGC_665_432,(0,5,24):C.UVGC_665_433,(0,5,25):C.UVGC_665_434,(0,5,26):C.UVGC_665_435,(0,5,27):C.UVGC_665_436,(0,5,28):C.UVGC_665_437,(0,5,29):C.UVGC_665_438,(0,7,3):C.UVGC_664_398,(0,7,0):C.UVGC_664_399,(0,7,1):C.UVGC_666_439,(0,7,2):C.UVGC_666_440,(0,7,4):C.UVGC_664_401,(0,7,5):C.UVGC_664_402,(0,7,6):C.UVGC_664_403,(0,7,7):C.UVGC_664_404,(0,7,8):C.UVGC_664_405,(0,7,9):C.UVGC_664_406,(0,7,10):C.UVGC_664_407,(0,7,11):C.UVGC_664_408,(0,7,12):C.UVGC_664_409,(0,7,13):C.UVGC_664_410,(0,7,14):C.UVGC_664_411,(0,7,15):C.UVGC_664_412,(0,7,16):C.UVGC_664_413,(0,7,17):C.UVGC_665_427,(0,7,19):C.UVGC_665_428,(0,7,20):C.UVGC_665_429,(0,7,21):C.UVGC_665_430,(0,7,22):C.UVGC_665_431,(0,7,23):C.UVGC_665_432,(0,7,24):C.UVGC_665_433,(0,7,25):C.UVGC_665_434,(0,7,26):C.UVGC_665_435,(0,7,27):C.UVGC_665_436,(0,7,28):C.UVGC_665_437,(0,7,29):C.UVGC_665_438,(0,8,3):C.UVGC_619_287,(0,8,0):C.UVGC_619_288,(0,8,1):C.UVGC_620_316,(0,8,2):C.UVGC_261_8,(0,8,4):C.UVGC_619_291,(0,8,5):C.UVGC_619_292,(0,8,6):C.UVGC_619_293,(0,8,7):C.UVGC_619_294,(0,8,8):C.UVGC_619_295,(0,8,9):C.UVGC_619_296,(0,8,10):C.UVGC_619_297,(0,8,11):C.UVGC_619_298,(0,8,12):C.UVGC_619_299,(0,8,13):C.UVGC_619_300,(0,8,14):C.UVGC_619_301,(0,8,15):C.UVGC_619_302,(0,8,16):C.UVGC_619_303,(0,8,17):C.UVGC_620_317,(0,8,19):C.UVGC_620_318,(0,8,20):C.UVGC_620_319,(0,8,21):C.UVGC_620_320,(0,8,22):C.UVGC_620_321,(0,8,23):C.UVGC_620_322,(0,8,24):C.UVGC_620_323,(0,8,25):C.UVGC_620_324,(0,8,26):C.UVGC_620_325,(0,8,27):C.UVGC_620_326,(0,8,28):C.UVGC_620_327,(0,8,29):C.UVGC_620_328,(0,2,1):C.UVGC_269_21,(0,2,2):C.UVGC_269_22,(0,2,18):C.UVGC_269_23,(0,4,1):C.UVGC_261_7,(0,4,2):C.UVGC_261_8,(0,6,1):C.UVGC_249_2})

V_489 = CTVertex(name = 'V_489',
                 type = 'UV',
                 particles = [ P.g, P.g, P.g, P.g ],
                 color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                 loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u], [P.YF3d1], [P.YF3d2], [P.YF3d3], [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3], [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3], [P.YF3u1], [P.YF3u2], [P.YF3u3] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u], [P.YF3d1], [P.YF3d2], [P.YF3d3], [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3], [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3], [P.YF3u1], [P.YF3u2], [P.YF3u3], [P.YS3d1], [P.YS3d2], [P.YS3d3], [P.YS3Qd1], [P.YS3Qd2], [P.YS3Qd3], [P.YS3Qu1], [P.YS3Qu2], [P.YS3Qu3], [P.YS3u1], [P.YS3u2], [P.YS3u3] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d1], [P.YS3d2], [P.YS3d3], [P.YS3Qd1], [P.YS3Qd2], [P.YS3Qd3], [P.YS3Qu1], [P.YS3Qu2], [P.YS3Qu3], [P.YS3u1], [P.YS3u2], [P.YS3u3] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,3):C.UVGC_263_12,(0,0,4):C.UVGC_263_11,(2,0,3):C.UVGC_263_12,(2,0,4):C.UVGC_263_11,(5,0,3):C.UVGC_262_9,(5,0,4):C.UVGC_262_10,(1,0,3):C.UVGC_262_9,(1,0,4):C.UVGC_262_10,(7,0,5):C.UVGC_679_495,(7,0,2):C.UVGC_270_24,(7,0,3):C.UVGC_680_522,(7,0,4):C.UVGC_271_26,(7,0,6):C.UVGC_679_497,(7,0,7):C.UVGC_679_498,(7,0,8):C.UVGC_679_499,(7,0,9):C.UVGC_679_500,(7,0,10):C.UVGC_679_501,(7,0,11):C.UVGC_679_502,(7,0,12):C.UVGC_679_503,(7,0,13):C.UVGC_679_504,(7,0,14):C.UVGC_679_505,(7,0,15):C.UVGC_679_506,(7,0,16):C.UVGC_679_507,(7,0,17):C.UVGC_679_508,(7,0,18):C.UVGC_679_509,(7,0,19):C.UVGC_679_510,(7,0,21):C.UVGC_679_511,(7,0,22):C.UVGC_679_512,(7,0,23):C.UVGC_679_513,(7,0,24):C.UVGC_679_514,(7,0,25):C.UVGC_679_515,(7,0,26):C.UVGC_679_516,(7,0,27):C.UVGC_679_517,(7,0,28):C.UVGC_679_518,(7,0,29):C.UVGC_679_519,(7,0,30):C.UVGC_679_520,(7,0,31):C.UVGC_679_521,(6,0,5):C.UVGC_679_495,(6,0,2):C.UVGC_270_24,(6,0,3):C.UVGC_679_496,(6,0,4):C.UVGC_265_13,(6,0,6):C.UVGC_679_497,(6,0,7):C.UVGC_679_498,(6,0,8):C.UVGC_679_499,(6,0,9):C.UVGC_679_500,(6,0,10):C.UVGC_679_501,(6,0,11):C.UVGC_679_502,(6,0,12):C.UVGC_679_503,(6,0,13):C.UVGC_679_504,(6,0,14):C.UVGC_679_505,(6,0,15):C.UVGC_679_506,(6,0,16):C.UVGC_679_507,(6,0,17):C.UVGC_679_508,(6,0,18):C.UVGC_679_509,(6,0,19):C.UVGC_679_510,(6,0,21):C.UVGC_679_511,(6,0,22):C.UVGC_679_512,(6,0,23):C.UVGC_679_513,(6,0,24):C.UVGC_679_514,(6,0,25):C.UVGC_679_515,(6,0,26):C.UVGC_679_516,(6,0,27):C.UVGC_679_517,(6,0,28):C.UVGC_679_518,(6,0,29):C.UVGC_679_519,(6,0,30):C.UVGC_679_520,(6,0,31):C.UVGC_679_521,(4,0,3):C.UVGC_262_9,(4,0,4):C.UVGC_262_10,(3,0,3):C.UVGC_262_9,(3,0,4):C.UVGC_262_10,(8,0,3):C.UVGC_263_11,(8,0,4):C.UVGC_263_12,(11,0,3):C.UVGC_266_15,(11,0,4):C.UVGC_266_16,(10,0,3):C.UVGC_266_15,(10,0,4):C.UVGC_266_16,(9,0,3):C.UVGC_265_13,(9,0,4):C.UVGC_265_14,(0,1,3):C.UVGC_263_12,(0,1,4):C.UVGC_263_11,(2,1,3):C.UVGC_263_12,(2,1,4):C.UVGC_263_11,(7,1,1):C.UVGC_270_24,(7,1,3):C.UVGC_263_11,(7,1,4):C.UVGC_271_26,(5,1,3):C.UVGC_262_9,(5,1,4):C.UVGC_262_10,(1,1,3):C.UVGC_262_9,(1,1,4):C.UVGC_262_10,(4,1,3):C.UVGC_262_9,(4,1,4):C.UVGC_262_10,(3,1,3):C.UVGC_262_9,(3,1,4):C.UVGC_262_10,(8,1,5):C.UVGC_679_495,(8,1,3):C.UVGC_680_522,(8,1,4):C.UVGC_263_12,(8,1,6):C.UVGC_681_523,(8,1,7):C.UVGC_681_524,(8,1,8):C.UVGC_681_525,(8,1,9):C.UVGC_681_526,(8,1,10):C.UVGC_681_527,(8,1,11):C.UVGC_681_528,(8,1,12):C.UVGC_681_529,(8,1,13):C.UVGC_681_530,(8,1,14):C.UVGC_681_531,(8,1,15):C.UVGC_681_532,(8,1,16):C.UVGC_681_533,(8,1,17):C.UVGC_681_534,(8,1,18):C.UVGC_681_535,(8,1,19):C.UVGC_681_536,(8,1,21):C.UVGC_681_537,(8,1,22):C.UVGC_681_538,(8,1,23):C.UVGC_681_539,(8,1,24):C.UVGC_681_540,(8,1,25):C.UVGC_681_541,(8,1,26):C.UVGC_681_542,(8,1,27):C.UVGC_681_543,(8,1,28):C.UVGC_681_544,(8,1,29):C.UVGC_681_545,(8,1,30):C.UVGC_681_546,(8,1,31):C.UVGC_681_547,(6,1,5):C.UVGC_694_563,(6,1,2):C.UVGC_694_564,(6,1,3):C.UVGC_696_616,(6,1,4):C.UVGC_265_13,(6,1,6):C.UVGC_694_566,(6,1,7):C.UVGC_694_567,(6,1,8):C.UVGC_694_568,(6,1,9):C.UVGC_694_569,(6,1,10):C.UVGC_694_570,(6,1,11):C.UVGC_694_571,(6,1,12):C.UVGC_694_572,(6,1,13):C.UVGC_694_573,(6,1,14):C.UVGC_694_574,(6,1,15):C.UVGC_694_575,(6,1,16):C.UVGC_694_576,(6,1,17):C.UVGC_694_577,(6,1,18):C.UVGC_694_578,(6,1,19):C.UVGC_696_617,(6,1,21):C.UVGC_696_618,(6,1,22):C.UVGC_696_619,(6,1,23):C.UVGC_696_620,(6,1,24):C.UVGC_696_621,(6,1,25):C.UVGC_696_622,(6,1,26):C.UVGC_696_623,(6,1,27):C.UVGC_696_624,(6,1,28):C.UVGC_696_625,(6,1,29):C.UVGC_696_626,(6,1,30):C.UVGC_696_627,(6,1,31):C.UVGC_696_628,(11,1,3):C.UVGC_266_15,(11,1,4):C.UVGC_266_16,(10,1,3):C.UVGC_266_15,(10,1,4):C.UVGC_266_16,(9,1,3):C.UVGC_265_13,(9,1,4):C.UVGC_265_14,(0,2,3):C.UVGC_263_12,(0,2,4):C.UVGC_263_11,(2,2,3):C.UVGC_263_12,(2,2,4):C.UVGC_263_11,(7,2,5):C.UVGC_694_563,(7,2,2):C.UVGC_694_564,(7,2,3):C.UVGC_694_565,(7,2,4):C.UVGC_271_26,(7,2,6):C.UVGC_694_566,(7,2,7):C.UVGC_694_567,(7,2,8):C.UVGC_694_568,(7,2,9):C.UVGC_694_569,(7,2,10):C.UVGC_694_570,(7,2,11):C.UVGC_694_571,(7,2,12):C.UVGC_694_572,(7,2,13):C.UVGC_694_573,(7,2,14):C.UVGC_694_574,(7,2,15):C.UVGC_694_575,(7,2,16):C.UVGC_694_576,(7,2,17):C.UVGC_694_577,(7,2,18):C.UVGC_694_578,(7,2,19):C.UVGC_694_579,(7,2,21):C.UVGC_694_580,(7,2,22):C.UVGC_694_581,(7,2,23):C.UVGC_694_582,(7,2,24):C.UVGC_694_583,(7,2,25):C.UVGC_694_584,(7,2,26):C.UVGC_694_585,(7,2,27):C.UVGC_694_586,(7,2,28):C.UVGC_694_587,(7,2,29):C.UVGC_694_588,(7,2,30):C.UVGC_694_589,(7,2,31):C.UVGC_694_590,(5,2,3):C.UVGC_262_9,(5,2,4):C.UVGC_262_10,(1,2,3):C.UVGC_262_9,(1,2,4):C.UVGC_262_10,(4,2,3):C.UVGC_262_9,(4,2,4):C.UVGC_262_10,(3,2,3):C.UVGC_262_9,(3,2,4):C.UVGC_262_10,(8,2,5):C.UVGC_694_563,(8,2,3):C.UVGC_694_565,(8,2,4):C.UVGC_263_12,(8,2,6):C.UVGC_695_591,(8,2,7):C.UVGC_695_592,(8,2,8):C.UVGC_695_593,(8,2,9):C.UVGC_695_594,(8,2,10):C.UVGC_695_595,(8,2,11):C.UVGC_695_596,(8,2,12):C.UVGC_695_597,(8,2,13):C.UVGC_695_598,(8,2,14):C.UVGC_695_599,(8,2,15):C.UVGC_695_600,(8,2,16):C.UVGC_695_601,(8,2,17):C.UVGC_695_602,(8,2,18):C.UVGC_695_603,(8,2,19):C.UVGC_695_604,(8,2,21):C.UVGC_695_605,(8,2,22):C.UVGC_695_606,(8,2,23):C.UVGC_695_607,(8,2,24):C.UVGC_695_608,(8,2,25):C.UVGC_695_609,(8,2,26):C.UVGC_695_610,(8,2,27):C.UVGC_695_611,(8,2,28):C.UVGC_695_612,(8,2,29):C.UVGC_695_613,(8,2,30):C.UVGC_695_614,(8,2,31):C.UVGC_695_615,(6,2,0):C.UVGC_270_24,(6,2,4):C.UVGC_265_13,(6,2,20):C.UVGC_270_25,(11,2,3):C.UVGC_266_15,(11,2,4):C.UVGC_266_16,(10,2,3):C.UVGC_266_15,(10,2,4):C.UVGC_266_16,(9,2,3):C.UVGC_265_13,(9,2,4):C.UVGC_265_14})

V_490 = CTVertex(name = 'V_490',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.YF3d1, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_272_27,(0,1,0):C.UVGC_534_183,(0,2,0):C.UVGC_534_183})

V_491 = CTVertex(name = 'V_491',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.YF3d2, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_272_27,(0,1,0):C.UVGC_540_191,(0,2,0):C.UVGC_540_191})

V_492 = CTVertex(name = 'V_492',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.YF3d3, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_272_27,(0,1,0):C.UVGC_546_199,(0,2,0):C.UVGC_546_199})

V_493 = CTVertex(name = 'V_493',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.YF3Qd1, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_272_27,(0,1,0):C.UVGC_552_207,(0,2,0):C.UVGC_552_207})

V_494 = CTVertex(name = 'V_494',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.YF3Qd2, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_272_27,(0,1,0):C.UVGC_558_215,(0,2,0):C.UVGC_558_215})

V_495 = CTVertex(name = 'V_495',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.YF3Qd3, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_272_27,(0,1,0):C.UVGC_564_223,(0,2,0):C.UVGC_564_223})

V_496 = CTVertex(name = 'V_496',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.YF3Qu1, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_274_29,(0,1,0):C.UVGC_570_231,(0,2,0):C.UVGC_570_231})

V_497 = CTVertex(name = 'V_497',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.YF3Qu2, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_274_29,(0,1,0):C.UVGC_577_238,(0,2,0):C.UVGC_577_238})

V_498 = CTVertex(name = 'V_498',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.YF3Qu3, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_274_29,(0,1,0):C.UVGC_584_245,(0,2,0):C.UVGC_584_245})

V_499 = CTVertex(name = 'V_499',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.YF3u1, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_274_29,(0,1,0):C.UVGC_591_253,(0,2,0):C.UVGC_591_253})

V_500 = CTVertex(name = 'V_500',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.YF3u2, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_274_29,(0,1,0):C.UVGC_597_261,(0,2,0):C.UVGC_597_261})

V_501 = CTVertex(name = 'V_501',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.YF3u3, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_274_29,(0,1,0):C.UVGC_603_269,(0,2,0):C.UVGC_603_269})

V_502 = CTVertex(name = 'V_502',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3Qu1, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_553_208,(0,0,2):C.UVGC_571_232,(0,0,1):C.UVGC_554_211})

V_503 = CTVertex(name = 'V_503',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3Qu1, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_553_208,(0,0,2):C.UVGC_571_232,(0,0,1):C.UVGC_554_211})

V_504 = CTVertex(name = 'V_504',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3Qd1, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_553_208,(0,0,2):C.UVGC_553_209,(0,0,1):C.UVGC_554_211})

V_505 = CTVertex(name = 'V_505',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3Qd1, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_553_208,(0,0,2):C.UVGC_553_209,(0,0,1):C.UVGC_554_211})

V_506 = CTVertex(name = 'V_506',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3Qu2, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_559_216,(0,0,2):C.UVGC_578_239,(0,0,1):C.UVGC_560_219})

V_507 = CTVertex(name = 'V_507',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3Qu2, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_559_216,(0,0,2):C.UVGC_578_239,(0,0,1):C.UVGC_560_219})

V_508 = CTVertex(name = 'V_508',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3Qd2, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_559_216,(0,0,2):C.UVGC_559_217,(0,0,1):C.UVGC_560_219})

V_509 = CTVertex(name = 'V_509',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3Qd2, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_559_216,(0,0,2):C.UVGC_559_217,(0,0,1):C.UVGC_560_219})

V_510 = CTVertex(name = 'V_510',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3Qu3, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_585_246,(0,0,2):C.UVGC_585_247,(0,0,1):C.UVGC_566_227})

V_511 = CTVertex(name = 'V_511',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3Qu3, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_585_246,(0,0,2):C.UVGC_585_247,(0,0,1):C.UVGC_566_227})

V_512 = CTVertex(name = 'V_512',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3Qd3, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_565_224,(0,0,2):C.UVGC_565_225,(0,0,1):C.UVGC_566_227})

V_513 = CTVertex(name = 'V_513',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3Qd3, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_565_224,(0,0,2):C.UVGC_565_225,(0,0,1):C.UVGC_566_227})

V_514 = CTVertex(name = 'V_514',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.d, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_535_184,(0,0,2):C.UVGC_535_185,(0,0,1):C.UVGC_536_187})

V_515 = CTVertex(name = 'V_515',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.s, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_541_192,(0,0,2):C.UVGC_541_193,(0,0,1):C.UVGC_542_195})

V_516 = CTVertex(name = 'V_516',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.b, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_547_200,(0,0,2):C.UVGC_547_201,(0,0,1):C.UVGC_548_203})

V_517 = CTVertex(name = 'V_517',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.d, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_535_184,(0,0,2):C.UVGC_535_185,(0,0,1):C.UVGC_536_187})

V_518 = CTVertex(name = 'V_518',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.s, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_541_192,(0,0,2):C.UVGC_541_193,(0,0,1):C.UVGC_542_195})

V_519 = CTVertex(name = 'V_519',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.b, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_547_200,(0,0,2):C.UVGC_547_201,(0,0,1):C.UVGC_548_203})

V_520 = CTVertex(name = 'V_520',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.u, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_592_254,(0,0,2):C.UVGC_592_255,(0,0,1):C.UVGC_593_257})

V_521 = CTVertex(name = 'V_521',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.c, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_598_262,(0,0,2):C.UVGC_598_263,(0,0,1):C.UVGC_599_265})

V_522 = CTVertex(name = 'V_522',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.t, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_604_270,(0,0,2):C.UVGC_604_271,(0,0,1):C.UVGC_605_273})

V_523 = CTVertex(name = 'V_523',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.u, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_592_254,(0,0,2):C.UVGC_592_255,(0,0,1):C.UVGC_593_257})

V_524 = CTVertex(name = 'V_524',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.c, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_598_262,(0,0,2):C.UVGC_598_263,(0,0,1):C.UVGC_599_265})

V_525 = CTVertex(name = 'V_525',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.t, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_604_270,(0,0,2):C.UVGC_604_271,(0,0,1):C.UVGC_605_273})

V_526 = CTVertex(name = 'V_526',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_530_177,(0,0,2):C.UVGC_530_178,(0,0,1):C.UVGC_530_179})

V_527 = CTVertex(name = 'V_527',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_531_180})

V_528 = CTVertex(name = 'V_528',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_532_181})

V_529 = CTVertex(name = 'V_529',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3d1, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_535_184,(0,0,2):C.UVGC_535_185,(0,0,1):C.UVGC_536_187})

V_530 = CTVertex(name = 'V_530',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3d2, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_541_192,(0,0,2):C.UVGC_541_193,(0,0,1):C.UVGC_542_195})

V_531 = CTVertex(name = 'V_531',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3d3, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_547_200,(0,0,2):C.UVGC_547_201,(0,0,1):C.UVGC_548_203})

V_532 = CTVertex(name = 'V_532',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3d1, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_535_184,(0,0,2):C.UVGC_535_185,(0,0,1):C.UVGC_536_187})

V_533 = CTVertex(name = 'V_533',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3d2, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_541_192,(0,0,2):C.UVGC_541_193,(0,0,1):C.UVGC_542_195})

V_534 = CTVertex(name = 'V_534',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3d3, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_547_200,(0,0,2):C.UVGC_547_201,(0,0,1):C.UVGC_548_203})

V_535 = CTVertex(name = 'V_535',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3u1, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_592_254,(0,0,2):C.UVGC_592_255,(0,0,1):C.UVGC_593_257})

V_536 = CTVertex(name = 'V_536',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3u2, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_598_262,(0,0,2):C.UVGC_598_263,(0,0,1):C.UVGC_599_265})

V_537 = CTVertex(name = 'V_537',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3u3, P.Xc__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_604_270,(0,0,2):C.UVGC_604_271,(0,0,1):C.UVGC_605_273})

V_538 = CTVertex(name = 'V_538',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3u1, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_592_254,(0,0,2):C.UVGC_592_255,(0,0,1):C.UVGC_593_257})

V_539 = CTVertex(name = 'V_539',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3u2, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_598_262,(0,0,2):C.UVGC_598_263,(0,0,1):C.UVGC_599_265})

V_540 = CTVertex(name = 'V_540',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3u3, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_604_270,(0,0,2):C.UVGC_604_271,(0,0,1):C.UVGC_605_273})

V_541 = CTVertex(name = 'V_541',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.u, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_553_208,(0,0,2):C.UVGC_571_232,(0,0,1):C.UVGC_554_211})

V_542 = CTVertex(name = 'V_542',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.u, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_553_208,(0,0,2):C.UVGC_571_232,(0,0,1):C.UVGC_554_211})

V_543 = CTVertex(name = 'V_543',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.d, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_553_208,(0,0,2):C.UVGC_553_209,(0,0,1):C.UVGC_554_211})

V_544 = CTVertex(name = 'V_544',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.d, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_553_208,(0,0,2):C.UVGC_553_209,(0,0,1):C.UVGC_554_211})

V_545 = CTVertex(name = 'V_545',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.c, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_559_216,(0,0,2):C.UVGC_578_239,(0,0,1):C.UVGC_560_219})

V_546 = CTVertex(name = 'V_546',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.c, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_559_216,(0,0,2):C.UVGC_578_239,(0,0,1):C.UVGC_560_219})

V_547 = CTVertex(name = 'V_547',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.s, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_559_216,(0,0,2):C.UVGC_559_217,(0,0,1):C.UVGC_560_219})

V_548 = CTVertex(name = 'V_548',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.s, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_559_216,(0,0,2):C.UVGC_559_217,(0,0,1):C.UVGC_560_219})

V_549 = CTVertex(name = 'V_549',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.t, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_585_246,(0,0,2):C.UVGC_585_247,(0,0,1):C.UVGC_566_227})

V_550 = CTVertex(name = 'V_550',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.t, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_585_246,(0,0,2):C.UVGC_585_247,(0,0,1):C.UVGC_566_227})

V_551 = CTVertex(name = 'V_551',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.b, P.Xc ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_565_224,(0,0,2):C.UVGC_565_225,(0,0,1):C.UVGC_566_227})

V_552 = CTVertex(name = 'V_552',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.b, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_565_224,(0,0,2):C.UVGC_565_225,(0,0,1):C.UVGC_566_227})

V_553 = CTVertex(name = 'V_553',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.YF3Qd1, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd1] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_273_28,(0,1,1):C.UVGC_622_330,(0,1,2):C.UVGC_622_331,(0,1,3):C.UVGC_622_332,(0,1,4):C.UVGC_622_333,(0,1,5):C.UVGC_622_334,(0,1,6):C.UVGC_622_335,(0,1,7):C.UVGC_622_336,(0,1,8):C.UVGC_622_337,(0,1,9):C.UVGC_622_338,(0,1,10):C.UVGC_622_339,(0,1,11):C.UVGC_622_340,(0,1,12):C.UVGC_622_341,(0,1,13):C.UVGC_622_342,(0,1,14):C.UVGC_622_343,(0,1,15):C.UVGC_622_344,(0,1,16):C.UVGC_622_345,(0,1,17):C.UVGC_622_346,(0,1,18):C.UVGC_622_347,(0,1,19):C.UVGC_622_348,(0,1,20):C.UVGC_622_349,(0,1,21):C.UVGC_622_350,(0,1,22):C.UVGC_622_351,(0,1,23):C.UVGC_622_352,(0,1,24):C.UVGC_622_353,(0,1,25):C.UVGC_622_354,(0,1,26):C.UVGC_622_355,(0,1,0):C.UVGC_643_362,(0,2,1):C.UVGC_622_330,(0,2,2):C.UVGC_622_331,(0,2,3):C.UVGC_622_332,(0,2,4):C.UVGC_622_333,(0,2,5):C.UVGC_622_334,(0,2,6):C.UVGC_622_335,(0,2,7):C.UVGC_622_336,(0,2,8):C.UVGC_622_337,(0,2,9):C.UVGC_622_338,(0,2,10):C.UVGC_622_339,(0,2,11):C.UVGC_622_340,(0,2,12):C.UVGC_622_341,(0,2,13):C.UVGC_622_342,(0,2,14):C.UVGC_622_343,(0,2,15):C.UVGC_622_344,(0,2,16):C.UVGC_622_345,(0,2,17):C.UVGC_622_346,(0,2,18):C.UVGC_622_347,(0,2,19):C.UVGC_622_348,(0,2,20):C.UVGC_622_349,(0,2,21):C.UVGC_622_350,(0,2,22):C.UVGC_622_351,(0,2,23):C.UVGC_622_352,(0,2,24):C.UVGC_622_353,(0,2,25):C.UVGC_622_354,(0,2,26):C.UVGC_622_355,(0,2,0):C.UVGC_643_362})

V_554 = CTVertex(name = 'V_554',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.YF3Qd2, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd2] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_273_28,(0,1,1):C.UVGC_622_330,(0,1,2):C.UVGC_622_331,(0,1,3):C.UVGC_622_332,(0,1,4):C.UVGC_622_333,(0,1,5):C.UVGC_622_334,(0,1,6):C.UVGC_622_335,(0,1,7):C.UVGC_622_336,(0,1,8):C.UVGC_622_337,(0,1,9):C.UVGC_622_338,(0,1,10):C.UVGC_622_339,(0,1,11):C.UVGC_622_340,(0,1,12):C.UVGC_622_341,(0,1,13):C.UVGC_622_342,(0,1,14):C.UVGC_622_343,(0,1,15):C.UVGC_622_344,(0,1,16):C.UVGC_622_345,(0,1,17):C.UVGC_622_346,(0,1,18):C.UVGC_622_347,(0,1,19):C.UVGC_622_348,(0,1,20):C.UVGC_622_349,(0,1,21):C.UVGC_622_350,(0,1,22):C.UVGC_622_351,(0,1,23):C.UVGC_622_352,(0,1,24):C.UVGC_622_353,(0,1,25):C.UVGC_622_354,(0,1,26):C.UVGC_622_355,(0,1,0):C.UVGC_644_363,(0,2,1):C.UVGC_622_330,(0,2,2):C.UVGC_622_331,(0,2,3):C.UVGC_622_332,(0,2,4):C.UVGC_622_333,(0,2,5):C.UVGC_622_334,(0,2,6):C.UVGC_622_335,(0,2,7):C.UVGC_622_336,(0,2,8):C.UVGC_622_337,(0,2,9):C.UVGC_622_338,(0,2,10):C.UVGC_622_339,(0,2,11):C.UVGC_622_340,(0,2,12):C.UVGC_622_341,(0,2,13):C.UVGC_622_342,(0,2,14):C.UVGC_622_343,(0,2,15):C.UVGC_622_344,(0,2,16):C.UVGC_622_345,(0,2,17):C.UVGC_622_346,(0,2,18):C.UVGC_622_347,(0,2,19):C.UVGC_622_348,(0,2,20):C.UVGC_622_349,(0,2,21):C.UVGC_622_350,(0,2,22):C.UVGC_622_351,(0,2,23):C.UVGC_622_352,(0,2,24):C.UVGC_622_353,(0,2,25):C.UVGC_622_354,(0,2,26):C.UVGC_622_355,(0,2,0):C.UVGC_644_363})

V_555 = CTVertex(name = 'V_555',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.YF3Qd3, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd3] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_273_28,(0,1,1):C.UVGC_622_330,(0,1,2):C.UVGC_622_331,(0,1,3):C.UVGC_622_332,(0,1,4):C.UVGC_622_333,(0,1,5):C.UVGC_622_334,(0,1,6):C.UVGC_622_335,(0,1,7):C.UVGC_622_336,(0,1,8):C.UVGC_622_337,(0,1,9):C.UVGC_622_338,(0,1,10):C.UVGC_622_339,(0,1,11):C.UVGC_622_340,(0,1,12):C.UVGC_622_341,(0,1,13):C.UVGC_622_342,(0,1,14):C.UVGC_622_343,(0,1,15):C.UVGC_622_344,(0,1,16):C.UVGC_622_345,(0,1,17):C.UVGC_622_346,(0,1,18):C.UVGC_622_347,(0,1,19):C.UVGC_622_348,(0,1,20):C.UVGC_622_349,(0,1,21):C.UVGC_622_350,(0,1,22):C.UVGC_622_351,(0,1,23):C.UVGC_622_352,(0,1,24):C.UVGC_622_353,(0,1,25):C.UVGC_622_354,(0,1,26):C.UVGC_622_355,(0,1,0):C.UVGC_645_364,(0,2,1):C.UVGC_622_330,(0,2,2):C.UVGC_622_331,(0,2,3):C.UVGC_622_332,(0,2,4):C.UVGC_622_333,(0,2,5):C.UVGC_622_334,(0,2,6):C.UVGC_622_335,(0,2,7):C.UVGC_622_336,(0,2,8):C.UVGC_622_337,(0,2,9):C.UVGC_622_338,(0,2,10):C.UVGC_622_339,(0,2,11):C.UVGC_622_340,(0,2,12):C.UVGC_622_341,(0,2,13):C.UVGC_622_342,(0,2,14):C.UVGC_622_343,(0,2,15):C.UVGC_622_344,(0,2,16):C.UVGC_622_345,(0,2,17):C.UVGC_622_346,(0,2,18):C.UVGC_622_347,(0,2,19):C.UVGC_622_348,(0,2,20):C.UVGC_622_349,(0,2,21):C.UVGC_622_350,(0,2,22):C.UVGC_622_351,(0,2,23):C.UVGC_622_352,(0,2,24):C.UVGC_622_353,(0,2,25):C.UVGC_622_354,(0,2,26):C.UVGC_622_355,(0,2,0):C.UVGC_645_364})

V_556 = CTVertex(name = 'V_556',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.YF3Qu1, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu1] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_273_28,(0,1,1):C.UVGC_622_330,(0,1,2):C.UVGC_622_331,(0,1,3):C.UVGC_622_332,(0,1,4):C.UVGC_622_333,(0,1,5):C.UVGC_622_334,(0,1,6):C.UVGC_622_335,(0,1,7):C.UVGC_622_336,(0,1,8):C.UVGC_622_337,(0,1,9):C.UVGC_622_338,(0,1,10):C.UVGC_622_339,(0,1,11):C.UVGC_622_340,(0,1,12):C.UVGC_622_341,(0,1,13):C.UVGC_622_342,(0,1,14):C.UVGC_622_343,(0,1,15):C.UVGC_622_344,(0,1,16):C.UVGC_622_345,(0,1,17):C.UVGC_622_346,(0,1,18):C.UVGC_622_347,(0,1,19):C.UVGC_622_348,(0,1,20):C.UVGC_622_349,(0,1,21):C.UVGC_622_350,(0,1,22):C.UVGC_622_351,(0,1,23):C.UVGC_622_352,(0,1,24):C.UVGC_622_353,(0,1,25):C.UVGC_622_354,(0,1,26):C.UVGC_622_355,(0,1,0):C.UVGC_646_365,(0,2,1):C.UVGC_622_330,(0,2,2):C.UVGC_622_331,(0,2,3):C.UVGC_622_332,(0,2,4):C.UVGC_622_333,(0,2,5):C.UVGC_622_334,(0,2,6):C.UVGC_622_335,(0,2,7):C.UVGC_622_336,(0,2,8):C.UVGC_622_337,(0,2,9):C.UVGC_622_338,(0,2,10):C.UVGC_622_339,(0,2,11):C.UVGC_622_340,(0,2,12):C.UVGC_622_341,(0,2,13):C.UVGC_622_342,(0,2,14):C.UVGC_622_343,(0,2,15):C.UVGC_622_344,(0,2,16):C.UVGC_622_345,(0,2,17):C.UVGC_622_346,(0,2,18):C.UVGC_622_347,(0,2,19):C.UVGC_622_348,(0,2,20):C.UVGC_622_349,(0,2,21):C.UVGC_622_350,(0,2,22):C.UVGC_622_351,(0,2,23):C.UVGC_622_352,(0,2,24):C.UVGC_622_353,(0,2,25):C.UVGC_622_354,(0,2,26):C.UVGC_622_355,(0,2,0):C.UVGC_646_365})

V_557 = CTVertex(name = 'V_557',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.YF3Qu2, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu2] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_273_28,(0,1,1):C.UVGC_622_330,(0,1,2):C.UVGC_622_331,(0,1,3):C.UVGC_622_332,(0,1,4):C.UVGC_622_333,(0,1,5):C.UVGC_622_334,(0,1,6):C.UVGC_622_335,(0,1,7):C.UVGC_622_336,(0,1,8):C.UVGC_622_337,(0,1,9):C.UVGC_622_338,(0,1,10):C.UVGC_622_339,(0,1,11):C.UVGC_622_340,(0,1,12):C.UVGC_622_341,(0,1,13):C.UVGC_622_342,(0,1,14):C.UVGC_622_343,(0,1,15):C.UVGC_622_344,(0,1,16):C.UVGC_622_345,(0,1,17):C.UVGC_622_346,(0,1,18):C.UVGC_622_347,(0,1,19):C.UVGC_622_348,(0,1,20):C.UVGC_622_349,(0,1,21):C.UVGC_622_350,(0,1,22):C.UVGC_622_351,(0,1,23):C.UVGC_622_352,(0,1,24):C.UVGC_622_353,(0,1,25):C.UVGC_622_354,(0,1,26):C.UVGC_622_355,(0,1,0):C.UVGC_647_366,(0,2,1):C.UVGC_622_330,(0,2,2):C.UVGC_622_331,(0,2,3):C.UVGC_622_332,(0,2,4):C.UVGC_622_333,(0,2,5):C.UVGC_622_334,(0,2,6):C.UVGC_622_335,(0,2,7):C.UVGC_622_336,(0,2,8):C.UVGC_622_337,(0,2,9):C.UVGC_622_338,(0,2,10):C.UVGC_622_339,(0,2,11):C.UVGC_622_340,(0,2,12):C.UVGC_622_341,(0,2,13):C.UVGC_622_342,(0,2,14):C.UVGC_622_343,(0,2,15):C.UVGC_622_344,(0,2,16):C.UVGC_622_345,(0,2,17):C.UVGC_622_346,(0,2,18):C.UVGC_622_347,(0,2,19):C.UVGC_622_348,(0,2,20):C.UVGC_622_349,(0,2,21):C.UVGC_622_350,(0,2,22):C.UVGC_622_351,(0,2,23):C.UVGC_622_352,(0,2,24):C.UVGC_622_353,(0,2,25):C.UVGC_622_354,(0,2,26):C.UVGC_622_355,(0,2,0):C.UVGC_647_366})

V_558 = CTVertex(name = 'V_558',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.YF3Qu3, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu3] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_273_28,(0,1,1):C.UVGC_622_330,(0,1,2):C.UVGC_622_331,(0,1,3):C.UVGC_622_332,(0,1,4):C.UVGC_622_333,(0,1,5):C.UVGC_622_334,(0,1,6):C.UVGC_622_335,(0,1,7):C.UVGC_622_336,(0,1,8):C.UVGC_622_337,(0,1,9):C.UVGC_622_338,(0,1,10):C.UVGC_622_339,(0,1,11):C.UVGC_622_340,(0,1,12):C.UVGC_622_341,(0,1,13):C.UVGC_622_342,(0,1,14):C.UVGC_622_343,(0,1,15):C.UVGC_622_344,(0,1,16):C.UVGC_622_345,(0,1,17):C.UVGC_622_346,(0,1,18):C.UVGC_622_347,(0,1,19):C.UVGC_622_348,(0,1,20):C.UVGC_622_349,(0,1,21):C.UVGC_622_350,(0,1,22):C.UVGC_622_351,(0,1,23):C.UVGC_622_352,(0,1,24):C.UVGC_622_353,(0,1,25):C.UVGC_622_354,(0,1,26):C.UVGC_622_355,(0,1,0):C.UVGC_648_367,(0,2,1):C.UVGC_622_330,(0,2,2):C.UVGC_622_331,(0,2,3):C.UVGC_622_332,(0,2,4):C.UVGC_622_333,(0,2,5):C.UVGC_622_334,(0,2,6):C.UVGC_622_335,(0,2,7):C.UVGC_622_336,(0,2,8):C.UVGC_622_337,(0,2,9):C.UVGC_622_338,(0,2,10):C.UVGC_622_339,(0,2,11):C.UVGC_622_340,(0,2,12):C.UVGC_622_341,(0,2,13):C.UVGC_622_342,(0,2,14):C.UVGC_622_343,(0,2,15):C.UVGC_622_344,(0,2,16):C.UVGC_622_345,(0,2,17):C.UVGC_622_346,(0,2,18):C.UVGC_622_347,(0,2,19):C.UVGC_622_348,(0,2,20):C.UVGC_622_349,(0,2,21):C.UVGC_622_350,(0,2,22):C.UVGC_622_351,(0,2,23):C.UVGC_622_352,(0,2,24):C.UVGC_622_353,(0,2,25):C.UVGC_622_354,(0,2,26):C.UVGC_622_355,(0,2,0):C.UVGC_648_367})

V_559 = CTVertex(name = 'V_559',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.YF3u1, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3u1] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_273_28,(0,1,1):C.UVGC_622_330,(0,1,2):C.UVGC_622_331,(0,1,3):C.UVGC_622_332,(0,1,4):C.UVGC_622_333,(0,1,5):C.UVGC_622_334,(0,1,6):C.UVGC_622_335,(0,1,7):C.UVGC_622_336,(0,1,8):C.UVGC_622_337,(0,1,9):C.UVGC_622_338,(0,1,10):C.UVGC_622_339,(0,1,11):C.UVGC_622_340,(0,1,12):C.UVGC_622_341,(0,1,13):C.UVGC_622_342,(0,1,14):C.UVGC_622_343,(0,1,15):C.UVGC_622_344,(0,1,16):C.UVGC_622_345,(0,1,17):C.UVGC_622_346,(0,1,18):C.UVGC_622_347,(0,1,19):C.UVGC_622_348,(0,1,20):C.UVGC_622_349,(0,1,21):C.UVGC_622_350,(0,1,22):C.UVGC_622_351,(0,1,23):C.UVGC_622_352,(0,1,24):C.UVGC_622_353,(0,1,25):C.UVGC_622_354,(0,1,26):C.UVGC_622_355,(0,1,0):C.UVGC_649_368,(0,2,1):C.UVGC_622_330,(0,2,2):C.UVGC_622_331,(0,2,3):C.UVGC_622_332,(0,2,4):C.UVGC_622_333,(0,2,5):C.UVGC_622_334,(0,2,6):C.UVGC_622_335,(0,2,7):C.UVGC_622_336,(0,2,8):C.UVGC_622_337,(0,2,9):C.UVGC_622_338,(0,2,10):C.UVGC_622_339,(0,2,11):C.UVGC_622_340,(0,2,12):C.UVGC_622_341,(0,2,13):C.UVGC_622_342,(0,2,14):C.UVGC_622_343,(0,2,15):C.UVGC_622_344,(0,2,16):C.UVGC_622_345,(0,2,17):C.UVGC_622_346,(0,2,18):C.UVGC_622_347,(0,2,19):C.UVGC_622_348,(0,2,20):C.UVGC_622_349,(0,2,21):C.UVGC_622_350,(0,2,22):C.UVGC_622_351,(0,2,23):C.UVGC_622_352,(0,2,24):C.UVGC_622_353,(0,2,25):C.UVGC_622_354,(0,2,26):C.UVGC_622_355,(0,2,0):C.UVGC_649_368})

V_560 = CTVertex(name = 'V_560',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.YF3u2, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3u2] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_273_28,(0,1,1):C.UVGC_622_330,(0,1,2):C.UVGC_622_331,(0,1,3):C.UVGC_622_332,(0,1,4):C.UVGC_622_333,(0,1,5):C.UVGC_622_334,(0,1,6):C.UVGC_622_335,(0,1,7):C.UVGC_622_336,(0,1,8):C.UVGC_622_337,(0,1,9):C.UVGC_622_338,(0,1,10):C.UVGC_622_339,(0,1,11):C.UVGC_622_340,(0,1,12):C.UVGC_622_341,(0,1,13):C.UVGC_622_342,(0,1,14):C.UVGC_622_343,(0,1,15):C.UVGC_622_344,(0,1,16):C.UVGC_622_345,(0,1,17):C.UVGC_622_346,(0,1,18):C.UVGC_622_347,(0,1,19):C.UVGC_622_348,(0,1,20):C.UVGC_622_349,(0,1,21):C.UVGC_622_350,(0,1,22):C.UVGC_622_351,(0,1,23):C.UVGC_622_352,(0,1,24):C.UVGC_622_353,(0,1,25):C.UVGC_622_354,(0,1,26):C.UVGC_622_355,(0,1,0):C.UVGC_650_369,(0,2,1):C.UVGC_622_330,(0,2,2):C.UVGC_622_331,(0,2,3):C.UVGC_622_332,(0,2,4):C.UVGC_622_333,(0,2,5):C.UVGC_622_334,(0,2,6):C.UVGC_622_335,(0,2,7):C.UVGC_622_336,(0,2,8):C.UVGC_622_337,(0,2,9):C.UVGC_622_338,(0,2,10):C.UVGC_622_339,(0,2,11):C.UVGC_622_340,(0,2,12):C.UVGC_622_341,(0,2,13):C.UVGC_622_342,(0,2,14):C.UVGC_622_343,(0,2,15):C.UVGC_622_344,(0,2,16):C.UVGC_622_345,(0,2,17):C.UVGC_622_346,(0,2,18):C.UVGC_622_347,(0,2,19):C.UVGC_622_348,(0,2,20):C.UVGC_622_349,(0,2,21):C.UVGC_622_350,(0,2,22):C.UVGC_622_351,(0,2,23):C.UVGC_622_352,(0,2,24):C.UVGC_622_353,(0,2,25):C.UVGC_622_354,(0,2,26):C.UVGC_622_355,(0,2,0):C.UVGC_650_369})

V_561 = CTVertex(name = 'V_561',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.YF3u3, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3u3] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_273_28,(0,1,1):C.UVGC_622_330,(0,1,2):C.UVGC_622_331,(0,1,3):C.UVGC_622_332,(0,1,4):C.UVGC_622_333,(0,1,5):C.UVGC_622_334,(0,1,6):C.UVGC_622_335,(0,1,7):C.UVGC_622_336,(0,1,8):C.UVGC_622_337,(0,1,9):C.UVGC_622_338,(0,1,10):C.UVGC_622_339,(0,1,11):C.UVGC_622_340,(0,1,12):C.UVGC_622_341,(0,1,13):C.UVGC_622_342,(0,1,14):C.UVGC_622_343,(0,1,15):C.UVGC_622_344,(0,1,16):C.UVGC_622_345,(0,1,17):C.UVGC_622_346,(0,1,18):C.UVGC_622_347,(0,1,19):C.UVGC_622_348,(0,1,20):C.UVGC_622_349,(0,1,21):C.UVGC_622_350,(0,1,22):C.UVGC_622_351,(0,1,23):C.UVGC_622_352,(0,1,24):C.UVGC_622_353,(0,1,25):C.UVGC_622_354,(0,1,26):C.UVGC_622_355,(0,1,0):C.UVGC_651_370,(0,2,1):C.UVGC_622_330,(0,2,2):C.UVGC_622_331,(0,2,3):C.UVGC_622_332,(0,2,4):C.UVGC_622_333,(0,2,5):C.UVGC_622_334,(0,2,6):C.UVGC_622_335,(0,2,7):C.UVGC_622_336,(0,2,8):C.UVGC_622_337,(0,2,9):C.UVGC_622_338,(0,2,10):C.UVGC_622_339,(0,2,11):C.UVGC_622_340,(0,2,12):C.UVGC_622_341,(0,2,13):C.UVGC_622_342,(0,2,14):C.UVGC_622_343,(0,2,15):C.UVGC_622_344,(0,2,16):C.UVGC_622_345,(0,2,17):C.UVGC_622_346,(0,2,18):C.UVGC_622_347,(0,2,19):C.UVGC_622_348,(0,2,20):C.UVGC_622_349,(0,2,21):C.UVGC_622_350,(0,2,22):C.UVGC_622_351,(0,2,23):C.UVGC_622_352,(0,2,24):C.UVGC_622_353,(0,2,25):C.UVGC_622_354,(0,2,26):C.UVGC_622_355,(0,2,0):C.UVGC_651_370})

V_562 = CTVertex(name = 'V_562',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.YF3d1, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3d1] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_273_28,(0,1,1):C.UVGC_622_330,(0,1,2):C.UVGC_622_331,(0,1,3):C.UVGC_622_332,(0,1,4):C.UVGC_622_333,(0,1,5):C.UVGC_622_334,(0,1,6):C.UVGC_622_335,(0,1,7):C.UVGC_622_336,(0,1,8):C.UVGC_622_337,(0,1,9):C.UVGC_622_338,(0,1,10):C.UVGC_622_339,(0,1,11):C.UVGC_622_340,(0,1,12):C.UVGC_622_341,(0,1,13):C.UVGC_622_342,(0,1,14):C.UVGC_622_343,(0,1,15):C.UVGC_622_344,(0,1,16):C.UVGC_622_345,(0,1,17):C.UVGC_622_346,(0,1,18):C.UVGC_622_347,(0,1,19):C.UVGC_622_348,(0,1,20):C.UVGC_622_349,(0,1,21):C.UVGC_622_350,(0,1,22):C.UVGC_622_351,(0,1,23):C.UVGC_622_352,(0,1,24):C.UVGC_622_353,(0,1,25):C.UVGC_622_354,(0,1,26):C.UVGC_622_355,(0,1,0):C.UVGC_640_359,(0,2,1):C.UVGC_622_330,(0,2,2):C.UVGC_622_331,(0,2,3):C.UVGC_622_332,(0,2,4):C.UVGC_622_333,(0,2,5):C.UVGC_622_334,(0,2,6):C.UVGC_622_335,(0,2,7):C.UVGC_622_336,(0,2,8):C.UVGC_622_337,(0,2,9):C.UVGC_622_338,(0,2,10):C.UVGC_622_339,(0,2,11):C.UVGC_622_340,(0,2,12):C.UVGC_622_341,(0,2,13):C.UVGC_622_342,(0,2,14):C.UVGC_622_343,(0,2,15):C.UVGC_622_344,(0,2,16):C.UVGC_622_345,(0,2,17):C.UVGC_622_346,(0,2,18):C.UVGC_622_347,(0,2,19):C.UVGC_622_348,(0,2,20):C.UVGC_622_349,(0,2,21):C.UVGC_622_350,(0,2,22):C.UVGC_622_351,(0,2,23):C.UVGC_622_352,(0,2,24):C.UVGC_622_353,(0,2,25):C.UVGC_622_354,(0,2,26):C.UVGC_622_355,(0,2,0):C.UVGC_640_359})

V_563 = CTVertex(name = 'V_563',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.YF3d2, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3d2] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_273_28,(0,1,1):C.UVGC_622_330,(0,1,2):C.UVGC_622_331,(0,1,3):C.UVGC_622_332,(0,1,4):C.UVGC_622_333,(0,1,5):C.UVGC_622_334,(0,1,6):C.UVGC_622_335,(0,1,7):C.UVGC_622_336,(0,1,8):C.UVGC_622_337,(0,1,9):C.UVGC_622_338,(0,1,10):C.UVGC_622_339,(0,1,11):C.UVGC_622_340,(0,1,12):C.UVGC_622_341,(0,1,13):C.UVGC_622_342,(0,1,14):C.UVGC_622_343,(0,1,15):C.UVGC_622_344,(0,1,16):C.UVGC_622_345,(0,1,17):C.UVGC_622_346,(0,1,18):C.UVGC_622_347,(0,1,19):C.UVGC_622_348,(0,1,20):C.UVGC_622_349,(0,1,21):C.UVGC_622_350,(0,1,22):C.UVGC_622_351,(0,1,23):C.UVGC_622_352,(0,1,24):C.UVGC_622_353,(0,1,25):C.UVGC_622_354,(0,1,26):C.UVGC_622_355,(0,1,0):C.UVGC_641_360,(0,2,1):C.UVGC_622_330,(0,2,2):C.UVGC_622_331,(0,2,3):C.UVGC_622_332,(0,2,4):C.UVGC_622_333,(0,2,5):C.UVGC_622_334,(0,2,6):C.UVGC_622_335,(0,2,7):C.UVGC_622_336,(0,2,8):C.UVGC_622_337,(0,2,9):C.UVGC_622_338,(0,2,10):C.UVGC_622_339,(0,2,11):C.UVGC_622_340,(0,2,12):C.UVGC_622_341,(0,2,13):C.UVGC_622_342,(0,2,14):C.UVGC_622_343,(0,2,15):C.UVGC_622_344,(0,2,16):C.UVGC_622_345,(0,2,17):C.UVGC_622_346,(0,2,18):C.UVGC_622_347,(0,2,19):C.UVGC_622_348,(0,2,20):C.UVGC_622_349,(0,2,21):C.UVGC_622_350,(0,2,22):C.UVGC_622_351,(0,2,23):C.UVGC_622_352,(0,2,24):C.UVGC_622_353,(0,2,25):C.UVGC_622_354,(0,2,26):C.UVGC_622_355,(0,2,0):C.UVGC_641_360})

V_564 = CTVertex(name = 'V_564',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.YF3d3, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3d3] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_273_28,(0,1,1):C.UVGC_622_330,(0,1,2):C.UVGC_622_331,(0,1,3):C.UVGC_622_332,(0,1,4):C.UVGC_622_333,(0,1,5):C.UVGC_622_334,(0,1,6):C.UVGC_622_335,(0,1,7):C.UVGC_622_336,(0,1,8):C.UVGC_622_337,(0,1,9):C.UVGC_622_338,(0,1,10):C.UVGC_622_339,(0,1,11):C.UVGC_622_340,(0,1,12):C.UVGC_622_341,(0,1,13):C.UVGC_622_342,(0,1,14):C.UVGC_622_343,(0,1,15):C.UVGC_622_344,(0,1,16):C.UVGC_622_345,(0,1,17):C.UVGC_622_346,(0,1,18):C.UVGC_622_347,(0,1,19):C.UVGC_622_348,(0,1,20):C.UVGC_622_349,(0,1,21):C.UVGC_622_350,(0,1,22):C.UVGC_622_351,(0,1,23):C.UVGC_622_352,(0,1,24):C.UVGC_622_353,(0,1,25):C.UVGC_622_354,(0,1,26):C.UVGC_622_355,(0,1,0):C.UVGC_642_361,(0,2,1):C.UVGC_622_330,(0,2,2):C.UVGC_622_331,(0,2,3):C.UVGC_622_332,(0,2,4):C.UVGC_622_333,(0,2,5):C.UVGC_622_334,(0,2,6):C.UVGC_622_335,(0,2,7):C.UVGC_622_336,(0,2,8):C.UVGC_622_337,(0,2,9):C.UVGC_622_338,(0,2,10):C.UVGC_622_339,(0,2,11):C.UVGC_622_340,(0,2,12):C.UVGC_622_341,(0,2,13):C.UVGC_622_342,(0,2,14):C.UVGC_622_343,(0,2,15):C.UVGC_622_344,(0,2,16):C.UVGC_622_345,(0,2,17):C.UVGC_622_346,(0,2,18):C.UVGC_622_347,(0,2,19):C.UVGC_622_348,(0,2,20):C.UVGC_622_349,(0,2,21):C.UVGC_622_350,(0,2,22):C.UVGC_622_351,(0,2,23):C.UVGC_622_352,(0,2,24):C.UVGC_622_353,(0,2,25):C.UVGC_622_354,(0,2,26):C.UVGC_622_355,(0,2,0):C.UVGC_642_361})

V_565 = CTVertex(name = 'V_565',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.YF3Qu1, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,1):C.UVGC_336_45,(0,1,0):C.UVGC_574_234,(0,1,2):C.UVGC_574_235,(0,2,0):C.UVGC_574_234,(0,2,2):C.UVGC_574_235})

V_566 = CTVertex(name = 'V_566',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.YF3Qu2, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd2] ], [ [P.g, P.YF3Qd2, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,1):C.UVGC_336_45,(0,1,0):C.UVGC_581_241,(0,1,2):C.UVGC_581_242,(0,2,0):C.UVGC_581_241,(0,2,2):C.UVGC_581_242})

V_567 = CTVertex(name = 'V_567',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.YF3Qu3, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,1):C.UVGC_336_45,(0,1,0):C.UVGC_588_249,(0,1,2):C.UVGC_588_250,(0,2,0):C.UVGC_588_249,(0,2,2):C.UVGC_588_250})

V_568 = CTVertex(name = 'V_568',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.YF3Qd1, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,1):C.UVGC_336_45,(0,1,0):C.UVGC_574_234,(0,1,2):C.UVGC_574_235,(0,2,0):C.UVGC_574_234,(0,2,2):C.UVGC_574_235})

V_569 = CTVertex(name = 'V_569',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.YF3Qd2, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd2] ], [ [P.g, P.YF3Qd2, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,1):C.UVGC_336_45,(0,1,0):C.UVGC_581_241,(0,1,2):C.UVGC_581_242,(0,2,0):C.UVGC_581_241,(0,2,2):C.UVGC_581_242})

V_570 = CTVertex(name = 'V_570',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.YF3Qd3, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,1):C.UVGC_336_45,(0,1,0):C.UVGC_588_249,(0,1,2):C.UVGC_588_250,(0,2,0):C.UVGC_588_249,(0,2,2):C.UVGC_588_250})

V_571 = CTVertex(name = 'V_571',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.d, P.YS3d1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.g, P.YS3d1], [P.d, P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_337_46,(0,0,1):C.UVGC_337_47})

V_572 = CTVertex(name = 'V_572',
                 type = 'UV',
                 particles = [ P.Xm, P.d, P.YS3d1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.g, P.YS3d1], [P.d, P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_337_46,(0,0,1):C.UVGC_337_47})

V_573 = CTVertex(name = 'V_573',
                 type = 'UV',
                 particles = [ P.g, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,1):C.UVGC_652_371,(0,0,2):C.UVGC_652_372,(0,0,3):C.UVGC_652_373,(0,0,4):C.UVGC_652_374,(0,0,5):C.UVGC_652_375,(0,0,6):C.UVGC_652_376,(0,0,7):C.UVGC_652_377,(0,0,8):C.UVGC_652_378,(0,0,9):C.UVGC_652_379,(0,0,10):C.UVGC_652_380,(0,0,11):C.UVGC_652_381,(0,0,12):C.UVGC_652_382,(0,0,13):C.UVGC_652_383,(0,0,14):C.UVGC_652_384,(0,0,15):C.UVGC_652_385,(0,0,16):C.UVGC_652_386,(0,0,17):C.UVGC_652_387,(0,0,18):C.UVGC_652_388,(0,0,19):C.UVGC_652_389,(0,0,20):C.UVGC_652_390,(0,0,21):C.UVGC_652_391,(0,0,22):C.UVGC_652_392,(0,0,23):C.UVGC_652_393,(0,0,24):C.UVGC_652_394,(0,0,25):C.UVGC_652_395,(0,0,26):C.UVGC_652_396,(0,0,0):C.UVGC_652_397,(0,1,1):C.UVGC_622_330,(0,1,2):C.UVGC_622_331,(0,1,3):C.UVGC_622_332,(0,1,4):C.UVGC_622_333,(0,1,5):C.UVGC_622_334,(0,1,6):C.UVGC_622_335,(0,1,7):C.UVGC_622_336,(0,1,8):C.UVGC_622_337,(0,1,9):C.UVGC_622_338,(0,1,10):C.UVGC_622_339,(0,1,11):C.UVGC_622_340,(0,1,12):C.UVGC_622_341,(0,1,13):C.UVGC_622_342,(0,1,14):C.UVGC_622_343,(0,1,15):C.UVGC_622_344,(0,1,16):C.UVGC_622_345,(0,1,17):C.UVGC_622_346,(0,1,18):C.UVGC_622_347,(0,1,19):C.UVGC_622_348,(0,1,20):C.UVGC_622_349,(0,1,21):C.UVGC_622_350,(0,1,22):C.UVGC_622_351,(0,1,23):C.UVGC_622_352,(0,1,24):C.UVGC_622_353,(0,1,25):C.UVGC_622_354,(0,1,26):C.UVGC_622_355,(0,1,0):C.UVGC_625_357})

V_574 = CTVertex(name = 'V_574',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.Xd, P.YS3d1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.g, P.YS3d1], [P.d, P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_337_46,(0,0,1):C.UVGC_337_47})

V_575 = CTVertex(name = 'V_575',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.Xm, P.YS3d1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.g, P.YS3d1], [P.d, P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_337_46,(0,0,1):C.UVGC_337_47})

V_576 = CTVertex(name = 'V_576',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,1):C.UVGC_667_441,(0,0,2):C.UVGC_667_442,(0,0,3):C.UVGC_667_443,(0,0,4):C.UVGC_667_444,(0,0,5):C.UVGC_667_445,(0,0,6):C.UVGC_667_446,(0,0,7):C.UVGC_667_447,(0,0,8):C.UVGC_667_448,(0,0,9):C.UVGC_667_449,(0,0,10):C.UVGC_667_450,(0,0,11):C.UVGC_667_451,(0,0,12):C.UVGC_667_452,(0,0,13):C.UVGC_667_453,(0,0,14):C.UVGC_667_454,(0,0,15):C.UVGC_667_455,(0,0,16):C.UVGC_667_456,(0,0,17):C.UVGC_667_457,(0,0,18):C.UVGC_667_458,(0,0,19):C.UVGC_667_459,(0,0,20):C.UVGC_667_460,(0,0,21):C.UVGC_667_461,(0,0,22):C.UVGC_667_462,(0,0,23):C.UVGC_667_463,(0,0,24):C.UVGC_667_464,(0,0,25):C.UVGC_667_465,(0,0,26):C.UVGC_667_466,(0,0,0):C.UVGC_667_467})

V_577 = CTVertex(name = 'V_577',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3d1] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,2):C.UVGC_682_548,(2,0,0):C.UVGC_682_549,(2,0,3):C.UVGC_681_523,(2,0,4):C.UVGC_681_524,(2,0,5):C.UVGC_681_525,(2,0,6):C.UVGC_681_526,(2,0,7):C.UVGC_681_527,(2,0,8):C.UVGC_681_528,(2,0,9):C.UVGC_681_529,(2,0,10):C.UVGC_681_530,(2,0,11):C.UVGC_681_531,(2,0,12):C.UVGC_681_532,(2,0,13):C.UVGC_681_533,(2,0,14):C.UVGC_681_534,(2,0,15):C.UVGC_681_535,(2,0,16):C.UVGC_682_550,(2,0,17):C.UVGC_682_551,(2,0,18):C.UVGC_682_552,(2,0,19):C.UVGC_682_553,(2,0,20):C.UVGC_682_554,(2,0,21):C.UVGC_682_555,(2,0,22):C.UVGC_682_556,(2,0,23):C.UVGC_682_557,(2,0,24):C.UVGC_682_558,(2,0,25):C.UVGC_682_559,(2,0,26):C.UVGC_682_560,(2,0,27):C.UVGC_682_561,(2,0,1):C.UVGC_682_562,(1,0,2):C.UVGC_682_548,(1,0,0):C.UVGC_682_549,(1,0,3):C.UVGC_681_523,(1,0,4):C.UVGC_681_524,(1,0,5):C.UVGC_681_525,(1,0,6):C.UVGC_681_526,(1,0,7):C.UVGC_681_527,(1,0,8):C.UVGC_681_528,(1,0,9):C.UVGC_681_529,(1,0,10):C.UVGC_681_530,(1,0,11):C.UVGC_681_531,(1,0,12):C.UVGC_681_532,(1,0,13):C.UVGC_681_533,(1,0,14):C.UVGC_681_534,(1,0,15):C.UVGC_681_535,(1,0,16):C.UVGC_682_550,(1,0,17):C.UVGC_682_551,(1,0,18):C.UVGC_682_552,(1,0,19):C.UVGC_682_553,(1,0,20):C.UVGC_682_554,(1,0,21):C.UVGC_682_555,(1,0,22):C.UVGC_682_556,(1,0,23):C.UVGC_682_557,(1,0,24):C.UVGC_682_558,(1,0,25):C.UVGC_682_559,(1,0,26):C.UVGC_682_560,(1,0,27):C.UVGC_682_561,(1,0,1):C.UVGC_682_562,(0,0,0):C.UVGC_278_30,(0,0,1):C.UVGC_278_31})

V_578 = CTVertex(name = 'V_578',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.s, P.YS3d2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.YS3d2], [P.g, P.s, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_363_62,(0,0,1):C.UVGC_363_63})

V_579 = CTVertex(name = 'V_579',
                 type = 'UV',
                 particles = [ P.Xm, P.s, P.YS3d2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.YS3d2], [P.g, P.s, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_363_62,(0,0,1):C.UVGC_363_63})

V_580 = CTVertex(name = 'V_580',
                 type = 'UV',
                 particles = [ P.g, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,1):C.UVGC_652_371,(0,0,2):C.UVGC_652_372,(0,0,3):C.UVGC_652_373,(0,0,4):C.UVGC_652_374,(0,0,5):C.UVGC_652_375,(0,0,6):C.UVGC_652_376,(0,0,7):C.UVGC_652_377,(0,0,8):C.UVGC_652_378,(0,0,9):C.UVGC_652_379,(0,0,10):C.UVGC_652_380,(0,0,11):C.UVGC_652_381,(0,0,12):C.UVGC_652_382,(0,0,13):C.UVGC_652_383,(0,0,14):C.UVGC_652_384,(0,0,15):C.UVGC_652_385,(0,0,16):C.UVGC_652_386,(0,0,17):C.UVGC_652_387,(0,0,18):C.UVGC_652_388,(0,0,19):C.UVGC_652_389,(0,0,20):C.UVGC_652_390,(0,0,21):C.UVGC_652_391,(0,0,22):C.UVGC_652_392,(0,0,23):C.UVGC_652_393,(0,0,24):C.UVGC_652_394,(0,0,25):C.UVGC_652_395,(0,0,26):C.UVGC_652_396,(0,0,0):C.UVGC_652_397,(0,1,1):C.UVGC_622_330,(0,1,2):C.UVGC_622_331,(0,1,3):C.UVGC_622_332,(0,1,4):C.UVGC_622_333,(0,1,5):C.UVGC_622_334,(0,1,6):C.UVGC_622_335,(0,1,7):C.UVGC_622_336,(0,1,8):C.UVGC_622_337,(0,1,9):C.UVGC_622_338,(0,1,10):C.UVGC_622_339,(0,1,11):C.UVGC_622_340,(0,1,12):C.UVGC_622_341,(0,1,13):C.UVGC_622_342,(0,1,14):C.UVGC_622_343,(0,1,15):C.UVGC_622_344,(0,1,16):C.UVGC_622_345,(0,1,17):C.UVGC_622_346,(0,1,18):C.UVGC_622_347,(0,1,19):C.UVGC_622_348,(0,1,20):C.UVGC_622_349,(0,1,21):C.UVGC_622_350,(0,1,22):C.UVGC_622_351,(0,1,23):C.UVGC_622_352,(0,1,24):C.UVGC_622_353,(0,1,25):C.UVGC_622_354,(0,1,26):C.UVGC_622_355,(0,1,0):C.UVGC_625_357})

V_581 = CTVertex(name = 'V_581',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.Xd, P.YS3d2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.YS3d2], [P.g, P.s, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_363_62,(0,0,1):C.UVGC_363_63})

V_582 = CTVertex(name = 'V_582',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.Xm, P.YS3d2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.YS3d2], [P.g, P.s, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_363_62,(0,0,1):C.UVGC_363_63})

V_583 = CTVertex(name = 'V_583',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,1):C.UVGC_667_441,(0,0,2):C.UVGC_667_442,(0,0,3):C.UVGC_667_443,(0,0,4):C.UVGC_667_444,(0,0,5):C.UVGC_667_445,(0,0,6):C.UVGC_667_446,(0,0,7):C.UVGC_667_447,(0,0,8):C.UVGC_667_448,(0,0,9):C.UVGC_667_449,(0,0,10):C.UVGC_667_450,(0,0,11):C.UVGC_667_451,(0,0,12):C.UVGC_667_452,(0,0,13):C.UVGC_667_453,(0,0,14):C.UVGC_667_454,(0,0,15):C.UVGC_667_455,(0,0,16):C.UVGC_667_456,(0,0,17):C.UVGC_667_457,(0,0,18):C.UVGC_667_458,(0,0,19):C.UVGC_667_459,(0,0,20):C.UVGC_667_460,(0,0,21):C.UVGC_667_461,(0,0,22):C.UVGC_667_462,(0,0,23):C.UVGC_667_463,(0,0,24):C.UVGC_667_464,(0,0,25):C.UVGC_667_465,(0,0,26):C.UVGC_667_466,(0,0,0):C.UVGC_667_467})

V_584 = CTVertex(name = 'V_584',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3d2] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,2):C.UVGC_682_548,(2,0,0):C.UVGC_682_549,(2,0,3):C.UVGC_681_523,(2,0,4):C.UVGC_681_524,(2,0,5):C.UVGC_681_525,(2,0,6):C.UVGC_681_526,(2,0,7):C.UVGC_681_527,(2,0,8):C.UVGC_681_528,(2,0,9):C.UVGC_681_529,(2,0,10):C.UVGC_681_530,(2,0,11):C.UVGC_681_531,(2,0,12):C.UVGC_681_532,(2,0,13):C.UVGC_681_533,(2,0,14):C.UVGC_681_534,(2,0,15):C.UVGC_681_535,(2,0,16):C.UVGC_682_550,(2,0,17):C.UVGC_682_551,(2,0,18):C.UVGC_682_552,(2,0,19):C.UVGC_682_553,(2,0,20):C.UVGC_682_554,(2,0,21):C.UVGC_682_555,(2,0,22):C.UVGC_682_556,(2,0,23):C.UVGC_682_557,(2,0,24):C.UVGC_682_558,(2,0,25):C.UVGC_682_559,(2,0,26):C.UVGC_682_560,(2,0,27):C.UVGC_682_561,(2,0,1):C.UVGC_682_562,(1,0,2):C.UVGC_682_548,(1,0,0):C.UVGC_682_549,(1,0,3):C.UVGC_681_523,(1,0,4):C.UVGC_681_524,(1,0,5):C.UVGC_681_525,(1,0,6):C.UVGC_681_526,(1,0,7):C.UVGC_681_527,(1,0,8):C.UVGC_681_528,(1,0,9):C.UVGC_681_529,(1,0,10):C.UVGC_681_530,(1,0,11):C.UVGC_681_531,(1,0,12):C.UVGC_681_532,(1,0,13):C.UVGC_681_533,(1,0,14):C.UVGC_681_534,(1,0,15):C.UVGC_681_535,(1,0,16):C.UVGC_682_550,(1,0,17):C.UVGC_682_551,(1,0,18):C.UVGC_682_552,(1,0,19):C.UVGC_682_553,(1,0,20):C.UVGC_682_554,(1,0,21):C.UVGC_682_555,(1,0,22):C.UVGC_682_556,(1,0,23):C.UVGC_682_557,(1,0,24):C.UVGC_682_558,(1,0,25):C.UVGC_682_559,(1,0,26):C.UVGC_682_560,(1,0,27):C.UVGC_682_561,(1,0,1):C.UVGC_682_562,(0,0,0):C.UVGC_278_30,(0,0,1):C.UVGC_278_31})

V_585 = CTVertex(name = 'V_585',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.b, P.YS3d3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.g, P.YS3d3], [P.b, P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_332_36,(0,0,1):C.UVGC_332_37})

V_586 = CTVertex(name = 'V_586',
                 type = 'UV',
                 particles = [ P.Xm, P.b, P.YS3d3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.g, P.YS3d3], [P.b, P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_332_36,(0,0,1):C.UVGC_332_37})

V_587 = CTVertex(name = 'V_587',
                 type = 'UV',
                 particles = [ P.g, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,1):C.UVGC_652_371,(0,0,2):C.UVGC_652_372,(0,0,3):C.UVGC_652_373,(0,0,4):C.UVGC_652_374,(0,0,5):C.UVGC_652_375,(0,0,6):C.UVGC_652_376,(0,0,7):C.UVGC_652_377,(0,0,8):C.UVGC_652_378,(0,0,9):C.UVGC_652_379,(0,0,10):C.UVGC_652_380,(0,0,11):C.UVGC_652_381,(0,0,12):C.UVGC_652_382,(0,0,13):C.UVGC_652_383,(0,0,14):C.UVGC_652_384,(0,0,15):C.UVGC_652_385,(0,0,16):C.UVGC_652_386,(0,0,17):C.UVGC_652_387,(0,0,18):C.UVGC_652_388,(0,0,19):C.UVGC_652_389,(0,0,20):C.UVGC_652_390,(0,0,21):C.UVGC_652_391,(0,0,22):C.UVGC_652_392,(0,0,23):C.UVGC_652_393,(0,0,24):C.UVGC_652_394,(0,0,25):C.UVGC_652_395,(0,0,26):C.UVGC_652_396,(0,0,0):C.UVGC_652_397,(0,1,1):C.UVGC_622_330,(0,1,2):C.UVGC_622_331,(0,1,3):C.UVGC_622_332,(0,1,4):C.UVGC_622_333,(0,1,5):C.UVGC_622_334,(0,1,6):C.UVGC_622_335,(0,1,7):C.UVGC_622_336,(0,1,8):C.UVGC_622_337,(0,1,9):C.UVGC_622_338,(0,1,10):C.UVGC_622_339,(0,1,11):C.UVGC_622_340,(0,1,12):C.UVGC_622_341,(0,1,13):C.UVGC_622_342,(0,1,14):C.UVGC_622_343,(0,1,15):C.UVGC_622_344,(0,1,16):C.UVGC_622_345,(0,1,17):C.UVGC_622_346,(0,1,18):C.UVGC_622_347,(0,1,19):C.UVGC_622_348,(0,1,20):C.UVGC_622_349,(0,1,21):C.UVGC_622_350,(0,1,22):C.UVGC_622_351,(0,1,23):C.UVGC_622_352,(0,1,24):C.UVGC_622_353,(0,1,25):C.UVGC_622_354,(0,1,26):C.UVGC_622_355,(0,1,0):C.UVGC_625_357})

V_588 = CTVertex(name = 'V_588',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.Xd, P.YS3d3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.g, P.YS3d3], [P.b, P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_332_36,(0,0,1):C.UVGC_332_37})

V_589 = CTVertex(name = 'V_589',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.Xm, P.YS3d3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.g, P.YS3d3], [P.b, P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_332_36,(0,0,1):C.UVGC_332_37})

V_590 = CTVertex(name = 'V_590',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,1):C.UVGC_667_441,(0,0,2):C.UVGC_667_442,(0,0,3):C.UVGC_667_443,(0,0,4):C.UVGC_667_444,(0,0,5):C.UVGC_667_445,(0,0,6):C.UVGC_667_446,(0,0,7):C.UVGC_667_447,(0,0,8):C.UVGC_667_448,(0,0,9):C.UVGC_667_449,(0,0,10):C.UVGC_667_450,(0,0,11):C.UVGC_667_451,(0,0,12):C.UVGC_667_452,(0,0,13):C.UVGC_667_453,(0,0,14):C.UVGC_667_454,(0,0,15):C.UVGC_667_455,(0,0,16):C.UVGC_667_456,(0,0,17):C.UVGC_667_457,(0,0,18):C.UVGC_667_458,(0,0,19):C.UVGC_667_459,(0,0,20):C.UVGC_667_460,(0,0,21):C.UVGC_667_461,(0,0,22):C.UVGC_667_462,(0,0,23):C.UVGC_667_463,(0,0,24):C.UVGC_667_464,(0,0,25):C.UVGC_667_465,(0,0,26):C.UVGC_667_466,(0,0,0):C.UVGC_667_467})

V_591 = CTVertex(name = 'V_591',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3d3] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,2):C.UVGC_682_548,(2,0,0):C.UVGC_682_549,(2,0,3):C.UVGC_681_523,(2,0,4):C.UVGC_681_524,(2,0,5):C.UVGC_681_525,(2,0,6):C.UVGC_681_526,(2,0,7):C.UVGC_681_527,(2,0,8):C.UVGC_681_528,(2,0,9):C.UVGC_681_529,(2,0,10):C.UVGC_681_530,(2,0,11):C.UVGC_681_531,(2,0,12):C.UVGC_681_532,(2,0,13):C.UVGC_681_533,(2,0,14):C.UVGC_681_534,(2,0,15):C.UVGC_681_535,(2,0,16):C.UVGC_682_550,(2,0,17):C.UVGC_682_551,(2,0,18):C.UVGC_682_552,(2,0,19):C.UVGC_682_553,(2,0,20):C.UVGC_682_554,(2,0,21):C.UVGC_682_555,(2,0,22):C.UVGC_682_556,(2,0,23):C.UVGC_682_557,(2,0,24):C.UVGC_682_558,(2,0,25):C.UVGC_682_559,(2,0,26):C.UVGC_682_560,(2,0,27):C.UVGC_682_561,(2,0,1):C.UVGC_682_562,(1,0,2):C.UVGC_682_548,(1,0,0):C.UVGC_682_549,(1,0,3):C.UVGC_681_523,(1,0,4):C.UVGC_681_524,(1,0,5):C.UVGC_681_525,(1,0,6):C.UVGC_681_526,(1,0,7):C.UVGC_681_527,(1,0,8):C.UVGC_681_528,(1,0,9):C.UVGC_681_529,(1,0,10):C.UVGC_681_530,(1,0,11):C.UVGC_681_531,(1,0,12):C.UVGC_681_532,(1,0,13):C.UVGC_681_533,(1,0,14):C.UVGC_681_534,(1,0,15):C.UVGC_681_535,(1,0,16):C.UVGC_682_550,(1,0,17):C.UVGC_682_551,(1,0,18):C.UVGC_682_552,(1,0,19):C.UVGC_682_553,(1,0,20):C.UVGC_682_554,(1,0,21):C.UVGC_682_555,(1,0,22):C.UVGC_682_556,(1,0,23):C.UVGC_682_557,(1,0,24):C.UVGC_682_558,(1,0,25):C.UVGC_682_559,(1,0,26):C.UVGC_682_560,(1,0,27):C.UVGC_682_561,(1,0,1):C.UVGC_682_562,(0,0,0):C.UVGC_278_30,(0,0,1):C.UVGC_278_31})

V_592 = CTVertex(name = 'V_592',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.d, P.YS3Qd1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.g, P.YS3Qd1], [P.d, P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_338_48,(0,0,1):C.UVGC_338_49})

V_593 = CTVertex(name = 'V_593',
                 type = 'UV',
                 particles = [ P.Xm, P.d, P.YS3Qd1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.g, P.YS3Qd1], [P.d, P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_338_48,(0,0,1):C.UVGC_338_49})

V_594 = CTVertex(name = 'V_594',
                 type = 'UV',
                 particles = [ P.W__minus__, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_344_57,(0,0,3):C.UVGC_344_58,(0,1,1):C.UVGC_336_45,(0,1,2):C.UVGC_342_56})

V_595 = CTVertex(name = 'V_595',
                 type = 'UV',
                 particles = [ P.g, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,1):C.UVGC_652_371,(0,0,2):C.UVGC_652_372,(0,0,3):C.UVGC_652_373,(0,0,4):C.UVGC_652_374,(0,0,5):C.UVGC_652_375,(0,0,6):C.UVGC_652_376,(0,0,7):C.UVGC_652_377,(0,0,8):C.UVGC_652_378,(0,0,9):C.UVGC_652_379,(0,0,10):C.UVGC_652_380,(0,0,11):C.UVGC_652_381,(0,0,12):C.UVGC_652_382,(0,0,13):C.UVGC_652_383,(0,0,14):C.UVGC_652_384,(0,0,15):C.UVGC_652_385,(0,0,16):C.UVGC_652_386,(0,0,17):C.UVGC_652_387,(0,0,18):C.UVGC_652_388,(0,0,19):C.UVGC_652_389,(0,0,20):C.UVGC_652_390,(0,0,21):C.UVGC_652_391,(0,0,22):C.UVGC_652_392,(0,0,23):C.UVGC_652_393,(0,0,24):C.UVGC_652_394,(0,0,25):C.UVGC_652_395,(0,0,26):C.UVGC_652_396,(0,0,0):C.UVGC_652_397,(0,1,1):C.UVGC_622_330,(0,1,2):C.UVGC_622_331,(0,1,3):C.UVGC_622_332,(0,1,4):C.UVGC_622_333,(0,1,5):C.UVGC_622_334,(0,1,6):C.UVGC_622_335,(0,1,7):C.UVGC_622_336,(0,1,8):C.UVGC_622_337,(0,1,9):C.UVGC_622_338,(0,1,10):C.UVGC_622_339,(0,1,11):C.UVGC_622_340,(0,1,12):C.UVGC_622_341,(0,1,13):C.UVGC_622_342,(0,1,14):C.UVGC_622_343,(0,1,15):C.UVGC_622_344,(0,1,16):C.UVGC_622_345,(0,1,17):C.UVGC_622_346,(0,1,18):C.UVGC_622_347,(0,1,19):C.UVGC_622_348,(0,1,20):C.UVGC_622_349,(0,1,21):C.UVGC_622_350,(0,1,22):C.UVGC_622_351,(0,1,23):C.UVGC_622_352,(0,1,24):C.UVGC_622_353,(0,1,25):C.UVGC_622_354,(0,1,26):C.UVGC_622_355,(0,1,0):C.UVGC_625_357})

V_596 = CTVertex(name = 'V_596',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.Xd, P.YS3Qd1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.g, P.YS3Qd1], [P.d, P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_338_48,(0,0,1):C.UVGC_338_49})

V_597 = CTVertex(name = 'V_597',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.Xm, P.YS3Qd1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.g, P.YS3Qd1], [P.d, P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_338_48,(0,0,1):C.UVGC_338_49})

V_598 = CTVertex(name = 'V_598',
                 type = 'UV',
                 particles = [ P.W__plus__, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_342_56,(0,0,3):C.UVGC_336_45,(0,1,1):C.UVGC_344_58,(0,1,2):C.UVGC_344_57})

V_599 = CTVertex(name = 'V_599',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_340_54,(0,0,2):C.UVGC_340_53,(0,0,1):C.UVGC_340_55})

V_600 = CTVertex(name = 'V_600',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,1):C.UVGC_667_441,(0,0,2):C.UVGC_667_442,(0,0,3):C.UVGC_667_443,(0,0,4):C.UVGC_667_444,(0,0,5):C.UVGC_667_445,(0,0,6):C.UVGC_667_446,(0,0,7):C.UVGC_667_447,(0,0,8):C.UVGC_667_448,(0,0,9):C.UVGC_667_449,(0,0,10):C.UVGC_667_450,(0,0,11):C.UVGC_667_451,(0,0,12):C.UVGC_667_452,(0,0,13):C.UVGC_667_453,(0,0,14):C.UVGC_667_454,(0,0,15):C.UVGC_667_455,(0,0,16):C.UVGC_667_456,(0,0,17):C.UVGC_667_457,(0,0,18):C.UVGC_667_458,(0,0,19):C.UVGC_667_459,(0,0,20):C.UVGC_667_460,(0,0,21):C.UVGC_667_461,(0,0,22):C.UVGC_667_462,(0,0,23):C.UVGC_667_463,(0,0,24):C.UVGC_667_464,(0,0,25):C.UVGC_667_465,(0,0,26):C.UVGC_667_466,(0,0,0):C.UVGC_667_467})

V_601 = CTVertex(name = 'V_601',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3Qd1] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,2):C.UVGC_682_548,(2,0,0):C.UVGC_682_549,(2,0,3):C.UVGC_681_523,(2,0,4):C.UVGC_681_524,(2,0,5):C.UVGC_681_525,(2,0,6):C.UVGC_681_526,(2,0,7):C.UVGC_681_527,(2,0,8):C.UVGC_681_528,(2,0,9):C.UVGC_681_529,(2,0,10):C.UVGC_681_530,(2,0,11):C.UVGC_681_531,(2,0,12):C.UVGC_681_532,(2,0,13):C.UVGC_681_533,(2,0,14):C.UVGC_681_534,(2,0,15):C.UVGC_681_535,(2,0,16):C.UVGC_682_550,(2,0,17):C.UVGC_682_551,(2,0,18):C.UVGC_682_552,(2,0,19):C.UVGC_682_553,(2,0,20):C.UVGC_682_554,(2,0,21):C.UVGC_682_555,(2,0,22):C.UVGC_682_556,(2,0,23):C.UVGC_682_557,(2,0,24):C.UVGC_682_558,(2,0,25):C.UVGC_682_559,(2,0,26):C.UVGC_682_560,(2,0,27):C.UVGC_682_561,(2,0,1):C.UVGC_682_562,(1,0,2):C.UVGC_682_548,(1,0,0):C.UVGC_682_549,(1,0,3):C.UVGC_681_523,(1,0,4):C.UVGC_681_524,(1,0,5):C.UVGC_681_525,(1,0,6):C.UVGC_681_526,(1,0,7):C.UVGC_681_527,(1,0,8):C.UVGC_681_528,(1,0,9):C.UVGC_681_529,(1,0,10):C.UVGC_681_530,(1,0,11):C.UVGC_681_531,(1,0,12):C.UVGC_681_532,(1,0,13):C.UVGC_681_533,(1,0,14):C.UVGC_681_534,(1,0,15):C.UVGC_681_535,(1,0,16):C.UVGC_682_550,(1,0,17):C.UVGC_682_551,(1,0,18):C.UVGC_682_552,(1,0,19):C.UVGC_682_553,(1,0,20):C.UVGC_682_554,(1,0,21):C.UVGC_682_555,(1,0,22):C.UVGC_682_556,(1,0,23):C.UVGC_682_557,(1,0,24):C.UVGC_682_558,(1,0,25):C.UVGC_682_559,(1,0,26):C.UVGC_682_560,(1,0,27):C.UVGC_682_561,(1,0,1):C.UVGC_682_562,(0,0,0):C.UVGC_278_30,(0,0,1):C.UVGC_278_31})

V_602 = CTVertex(name = 'V_602',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.s, P.YS3Qd2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.YS3Qd2], [P.g, P.s, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_334_40,(0,0,1):C.UVGC_334_41})

V_603 = CTVertex(name = 'V_603',
                 type = 'UV',
                 particles = [ P.Xm, P.s, P.YS3Qd2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.YS3Qd2], [P.g, P.s, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_334_40,(0,0,1):C.UVGC_334_41})

V_604 = CTVertex(name = 'V_604',
                 type = 'UV',
                 particles = [ P.W__minus__, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_344_57,(0,0,3):C.UVGC_344_58,(0,1,1):C.UVGC_336_45,(0,1,2):C.UVGC_342_56})

V_605 = CTVertex(name = 'V_605',
                 type = 'UV',
                 particles = [ P.g, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,1):C.UVGC_652_371,(0,0,2):C.UVGC_652_372,(0,0,3):C.UVGC_652_373,(0,0,4):C.UVGC_652_374,(0,0,5):C.UVGC_652_375,(0,0,6):C.UVGC_652_376,(0,0,7):C.UVGC_652_377,(0,0,8):C.UVGC_652_378,(0,0,9):C.UVGC_652_379,(0,0,10):C.UVGC_652_380,(0,0,11):C.UVGC_652_381,(0,0,12):C.UVGC_652_382,(0,0,13):C.UVGC_652_383,(0,0,14):C.UVGC_652_384,(0,0,15):C.UVGC_652_385,(0,0,16):C.UVGC_652_386,(0,0,17):C.UVGC_652_387,(0,0,18):C.UVGC_652_388,(0,0,19):C.UVGC_652_389,(0,0,20):C.UVGC_652_390,(0,0,21):C.UVGC_652_391,(0,0,22):C.UVGC_652_392,(0,0,23):C.UVGC_652_393,(0,0,24):C.UVGC_652_394,(0,0,25):C.UVGC_652_395,(0,0,26):C.UVGC_652_396,(0,0,0):C.UVGC_652_397,(0,1,1):C.UVGC_622_330,(0,1,2):C.UVGC_622_331,(0,1,3):C.UVGC_622_332,(0,1,4):C.UVGC_622_333,(0,1,5):C.UVGC_622_334,(0,1,6):C.UVGC_622_335,(0,1,7):C.UVGC_622_336,(0,1,8):C.UVGC_622_337,(0,1,9):C.UVGC_622_338,(0,1,10):C.UVGC_622_339,(0,1,11):C.UVGC_622_340,(0,1,12):C.UVGC_622_341,(0,1,13):C.UVGC_622_342,(0,1,14):C.UVGC_622_343,(0,1,15):C.UVGC_622_344,(0,1,16):C.UVGC_622_345,(0,1,17):C.UVGC_622_346,(0,1,18):C.UVGC_622_347,(0,1,19):C.UVGC_622_348,(0,1,20):C.UVGC_622_349,(0,1,21):C.UVGC_622_350,(0,1,22):C.UVGC_622_351,(0,1,23):C.UVGC_622_352,(0,1,24):C.UVGC_622_353,(0,1,25):C.UVGC_622_354,(0,1,26):C.UVGC_622_355,(0,1,0):C.UVGC_625_357})

V_606 = CTVertex(name = 'V_606',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.Xd, P.YS3Qd2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.YS3Qd2], [P.g, P.s, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_334_40,(0,0,1):C.UVGC_334_41})

V_607 = CTVertex(name = 'V_607',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.Xm, P.YS3Qd2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.YS3Qd2], [P.g, P.s, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_334_40,(0,0,1):C.UVGC_334_41})

V_608 = CTVertex(name = 'V_608',
                 type = 'UV',
                 particles = [ P.W__plus__, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_342_56,(0,0,3):C.UVGC_336_45,(0,1,1):C.UVGC_344_58,(0,1,2):C.UVGC_344_57})

V_609 = CTVertex(name = 'V_609',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_340_54,(0,0,2):C.UVGC_340_53,(0,0,1):C.UVGC_340_55})

V_610 = CTVertex(name = 'V_610',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,1):C.UVGC_667_441,(0,0,2):C.UVGC_667_442,(0,0,3):C.UVGC_667_443,(0,0,4):C.UVGC_667_444,(0,0,5):C.UVGC_667_445,(0,0,6):C.UVGC_667_446,(0,0,7):C.UVGC_667_447,(0,0,8):C.UVGC_667_448,(0,0,9):C.UVGC_667_449,(0,0,10):C.UVGC_667_450,(0,0,11):C.UVGC_667_451,(0,0,12):C.UVGC_667_452,(0,0,13):C.UVGC_667_453,(0,0,14):C.UVGC_667_454,(0,0,15):C.UVGC_667_455,(0,0,16):C.UVGC_667_456,(0,0,17):C.UVGC_667_457,(0,0,18):C.UVGC_667_458,(0,0,19):C.UVGC_667_459,(0,0,20):C.UVGC_667_460,(0,0,21):C.UVGC_667_461,(0,0,22):C.UVGC_667_462,(0,0,23):C.UVGC_667_463,(0,0,24):C.UVGC_667_464,(0,0,25):C.UVGC_667_465,(0,0,26):C.UVGC_667_466,(0,0,0):C.UVGC_667_467})

V_611 = CTVertex(name = 'V_611',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3Qd2] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,2):C.UVGC_682_548,(2,0,0):C.UVGC_682_549,(2,0,3):C.UVGC_681_523,(2,0,4):C.UVGC_681_524,(2,0,5):C.UVGC_681_525,(2,0,6):C.UVGC_681_526,(2,0,7):C.UVGC_681_527,(2,0,8):C.UVGC_681_528,(2,0,9):C.UVGC_681_529,(2,0,10):C.UVGC_681_530,(2,0,11):C.UVGC_681_531,(2,0,12):C.UVGC_681_532,(2,0,13):C.UVGC_681_533,(2,0,14):C.UVGC_681_534,(2,0,15):C.UVGC_681_535,(2,0,16):C.UVGC_682_550,(2,0,17):C.UVGC_682_551,(2,0,18):C.UVGC_682_552,(2,0,19):C.UVGC_682_553,(2,0,20):C.UVGC_682_554,(2,0,21):C.UVGC_682_555,(2,0,22):C.UVGC_682_556,(2,0,23):C.UVGC_682_557,(2,0,24):C.UVGC_682_558,(2,0,25):C.UVGC_682_559,(2,0,26):C.UVGC_682_560,(2,0,27):C.UVGC_682_561,(2,0,1):C.UVGC_682_562,(1,0,2):C.UVGC_682_548,(1,0,0):C.UVGC_682_549,(1,0,3):C.UVGC_681_523,(1,0,4):C.UVGC_681_524,(1,0,5):C.UVGC_681_525,(1,0,6):C.UVGC_681_526,(1,0,7):C.UVGC_681_527,(1,0,8):C.UVGC_681_528,(1,0,9):C.UVGC_681_529,(1,0,10):C.UVGC_681_530,(1,0,11):C.UVGC_681_531,(1,0,12):C.UVGC_681_532,(1,0,13):C.UVGC_681_533,(1,0,14):C.UVGC_681_534,(1,0,15):C.UVGC_681_535,(1,0,16):C.UVGC_682_550,(1,0,17):C.UVGC_682_551,(1,0,18):C.UVGC_682_552,(1,0,19):C.UVGC_682_553,(1,0,20):C.UVGC_682_554,(1,0,21):C.UVGC_682_555,(1,0,22):C.UVGC_682_556,(1,0,23):C.UVGC_682_557,(1,0,24):C.UVGC_682_558,(1,0,25):C.UVGC_682_559,(1,0,26):C.UVGC_682_560,(1,0,27):C.UVGC_682_561,(1,0,1):C.UVGC_682_562,(0,0,0):C.UVGC_278_30,(0,0,1):C.UVGC_278_31})

V_612 = CTVertex(name = 'V_612',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.b, P.YS3Qd3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.g, P.YS3Qd3], [P.b, P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_333_38,(0,0,1):C.UVGC_333_39})

V_613 = CTVertex(name = 'V_613',
                 type = 'UV',
                 particles = [ P.Xm, P.b, P.YS3Qd3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.g, P.YS3Qd3], [P.b, P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_333_38,(0,0,1):C.UVGC_333_39})

V_614 = CTVertex(name = 'V_614',
                 type = 'UV',
                 particles = [ P.W__minus__, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qu3], [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_344_57,(0,0,3):C.UVGC_344_58,(0,1,1):C.UVGC_336_45,(0,1,2):C.UVGC_342_56})

V_615 = CTVertex(name = 'V_615',
                 type = 'UV',
                 particles = [ P.g, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,1):C.UVGC_652_371,(0,0,2):C.UVGC_652_372,(0,0,3):C.UVGC_652_373,(0,0,4):C.UVGC_652_374,(0,0,5):C.UVGC_652_375,(0,0,6):C.UVGC_652_376,(0,0,7):C.UVGC_652_377,(0,0,8):C.UVGC_652_378,(0,0,9):C.UVGC_652_379,(0,0,10):C.UVGC_652_380,(0,0,11):C.UVGC_652_381,(0,0,12):C.UVGC_652_382,(0,0,13):C.UVGC_652_383,(0,0,14):C.UVGC_652_384,(0,0,15):C.UVGC_652_385,(0,0,16):C.UVGC_652_386,(0,0,17):C.UVGC_652_387,(0,0,18):C.UVGC_652_388,(0,0,19):C.UVGC_652_389,(0,0,20):C.UVGC_652_390,(0,0,21):C.UVGC_652_391,(0,0,22):C.UVGC_652_392,(0,0,23):C.UVGC_652_393,(0,0,24):C.UVGC_652_394,(0,0,25):C.UVGC_652_395,(0,0,26):C.UVGC_652_396,(0,0,0):C.UVGC_652_397,(0,1,1):C.UVGC_622_330,(0,1,2):C.UVGC_622_331,(0,1,3):C.UVGC_622_332,(0,1,4):C.UVGC_622_333,(0,1,5):C.UVGC_622_334,(0,1,6):C.UVGC_622_335,(0,1,7):C.UVGC_622_336,(0,1,8):C.UVGC_622_337,(0,1,9):C.UVGC_622_338,(0,1,10):C.UVGC_622_339,(0,1,11):C.UVGC_622_340,(0,1,12):C.UVGC_622_341,(0,1,13):C.UVGC_622_342,(0,1,14):C.UVGC_622_343,(0,1,15):C.UVGC_622_344,(0,1,16):C.UVGC_622_345,(0,1,17):C.UVGC_622_346,(0,1,18):C.UVGC_622_347,(0,1,19):C.UVGC_622_348,(0,1,20):C.UVGC_622_349,(0,1,21):C.UVGC_622_350,(0,1,22):C.UVGC_622_351,(0,1,23):C.UVGC_622_352,(0,1,24):C.UVGC_622_353,(0,1,25):C.UVGC_622_354,(0,1,26):C.UVGC_622_355,(0,1,0):C.UVGC_625_357})

V_616 = CTVertex(name = 'V_616',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.Xd, P.YS3Qd3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.g, P.YS3Qd3], [P.b, P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_333_38,(0,0,1):C.UVGC_333_39})

V_617 = CTVertex(name = 'V_617',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.Xm, P.YS3Qd3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.g, P.YS3Qd3], [P.b, P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_333_38,(0,0,1):C.UVGC_333_39})

V_618 = CTVertex(name = 'V_618',
                 type = 'UV',
                 particles = [ P.W__plus__, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qu3], [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_342_56,(0,0,3):C.UVGC_336_45,(0,1,1):C.UVGC_344_58,(0,1,2):C.UVGC_344_57})

V_619 = CTVertex(name = 'V_619',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_340_54,(0,0,2):C.UVGC_340_53,(0,0,1):C.UVGC_340_55})

V_620 = CTVertex(name = 'V_620',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,1):C.UVGC_667_441,(0,0,2):C.UVGC_667_442,(0,0,3):C.UVGC_667_443,(0,0,4):C.UVGC_667_444,(0,0,5):C.UVGC_667_445,(0,0,6):C.UVGC_667_446,(0,0,7):C.UVGC_667_447,(0,0,8):C.UVGC_667_448,(0,0,9):C.UVGC_667_449,(0,0,10):C.UVGC_667_450,(0,0,11):C.UVGC_667_451,(0,0,12):C.UVGC_667_452,(0,0,13):C.UVGC_667_453,(0,0,14):C.UVGC_667_454,(0,0,15):C.UVGC_667_455,(0,0,16):C.UVGC_667_456,(0,0,17):C.UVGC_667_457,(0,0,18):C.UVGC_667_458,(0,0,19):C.UVGC_667_459,(0,0,20):C.UVGC_667_460,(0,0,21):C.UVGC_667_461,(0,0,22):C.UVGC_667_462,(0,0,23):C.UVGC_667_463,(0,0,24):C.UVGC_667_464,(0,0,25):C.UVGC_667_465,(0,0,26):C.UVGC_667_466,(0,0,0):C.UVGC_667_467})

V_621 = CTVertex(name = 'V_621',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3Qd3] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,2):C.UVGC_682_548,(2,0,0):C.UVGC_682_549,(2,0,3):C.UVGC_681_523,(2,0,4):C.UVGC_681_524,(2,0,5):C.UVGC_681_525,(2,0,6):C.UVGC_681_526,(2,0,7):C.UVGC_681_527,(2,0,8):C.UVGC_681_528,(2,0,9):C.UVGC_681_529,(2,0,10):C.UVGC_681_530,(2,0,11):C.UVGC_681_531,(2,0,12):C.UVGC_681_532,(2,0,13):C.UVGC_681_533,(2,0,14):C.UVGC_681_534,(2,0,15):C.UVGC_681_535,(2,0,16):C.UVGC_682_550,(2,0,17):C.UVGC_682_551,(2,0,18):C.UVGC_682_552,(2,0,19):C.UVGC_682_553,(2,0,20):C.UVGC_682_554,(2,0,21):C.UVGC_682_555,(2,0,22):C.UVGC_682_556,(2,0,23):C.UVGC_682_557,(2,0,24):C.UVGC_682_558,(2,0,25):C.UVGC_682_559,(2,0,26):C.UVGC_682_560,(2,0,27):C.UVGC_682_561,(2,0,1):C.UVGC_682_562,(1,0,2):C.UVGC_682_548,(1,0,0):C.UVGC_682_549,(1,0,3):C.UVGC_681_523,(1,0,4):C.UVGC_681_524,(1,0,5):C.UVGC_681_525,(1,0,6):C.UVGC_681_526,(1,0,7):C.UVGC_681_527,(1,0,8):C.UVGC_681_528,(1,0,9):C.UVGC_681_529,(1,0,10):C.UVGC_681_530,(1,0,11):C.UVGC_681_531,(1,0,12):C.UVGC_681_532,(1,0,13):C.UVGC_681_533,(1,0,14):C.UVGC_681_534,(1,0,15):C.UVGC_681_535,(1,0,16):C.UVGC_682_550,(1,0,17):C.UVGC_682_551,(1,0,18):C.UVGC_682_552,(1,0,19):C.UVGC_682_553,(1,0,20):C.UVGC_682_554,(1,0,21):C.UVGC_682_555,(1,0,22):C.UVGC_682_556,(1,0,23):C.UVGC_682_557,(1,0,24):C.UVGC_682_558,(1,0,25):C.UVGC_682_559,(1,0,26):C.UVGC_682_560,(1,0,27):C.UVGC_682_561,(1,0,1):C.UVGC_682_562,(0,0,0):C.UVGC_278_30,(0,0,1):C.UVGC_278_31})

V_622 = CTVertex(name = 'V_622',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.u, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.YS3Qu1], [P.g, P.u, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_338_48,(0,0,1):C.UVGC_338_49})

V_623 = CTVertex(name = 'V_623',
                 type = 'UV',
                 particles = [ P.Xm, P.u, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.YS3Qu1], [P.g, P.u, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_338_48,(0,0,1):C.UVGC_338_49})

V_624 = CTVertex(name = 'V_624',
                 type = 'UV',
                 particles = [ P.a, P.W__plus__, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_346_59,(0,0,2):C.UVGC_346_60,(0,0,1):C.UVGC_346_61})

V_625 = CTVertex(name = 'V_625',
                 type = 'UV',
                 particles = [ P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,2):C.UVGC_697_629,(0,0,3):C.UVGC_697_630,(0,0,4):C.UVGC_697_631,(0,0,5):C.UVGC_697_632,(0,0,6):C.UVGC_697_633,(0,0,7):C.UVGC_697_634,(0,0,8):C.UVGC_697_635,(0,0,9):C.UVGC_697_636,(0,0,10):C.UVGC_697_637,(0,0,11):C.UVGC_697_638,(0,0,12):C.UVGC_697_639,(0,0,13):C.UVGC_697_640,(0,0,14):C.UVGC_697_641,(0,0,15):C.UVGC_697_642,(0,0,16):C.UVGC_697_643,(0,0,17):C.UVGC_697_644,(0,0,18):C.UVGC_697_645,(0,0,19):C.UVGC_697_646,(0,0,20):C.UVGC_697_647,(0,0,21):C.UVGC_697_648,(0,0,22):C.UVGC_697_649,(0,0,23):C.UVGC_697_650,(0,0,24):C.UVGC_697_651,(0,0,25):C.UVGC_697_652,(0,0,26):C.UVGC_697_653,(0,0,27):C.UVGC_697_654,(0,0,0):C.UVGC_697_655,(0,0,1):C.UVGC_697_656})

V_626 = CTVertex(name = 'V_626',
                 type = 'UV',
                 particles = [ P.g, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,1):C.UVGC_652_371,(0,0,2):C.UVGC_652_372,(0,0,3):C.UVGC_652_373,(0,0,4):C.UVGC_652_374,(0,0,5):C.UVGC_652_375,(0,0,6):C.UVGC_652_376,(0,0,7):C.UVGC_652_377,(0,0,8):C.UVGC_652_378,(0,0,9):C.UVGC_652_379,(0,0,10):C.UVGC_652_380,(0,0,11):C.UVGC_652_381,(0,0,12):C.UVGC_652_382,(0,0,13):C.UVGC_652_383,(0,0,14):C.UVGC_652_384,(0,0,15):C.UVGC_652_385,(0,0,16):C.UVGC_652_386,(0,0,17):C.UVGC_652_387,(0,0,18):C.UVGC_652_388,(0,0,19):C.UVGC_652_389,(0,0,20):C.UVGC_652_390,(0,0,21):C.UVGC_652_391,(0,0,22):C.UVGC_652_392,(0,0,23):C.UVGC_652_393,(0,0,24):C.UVGC_652_394,(0,0,25):C.UVGC_652_395,(0,0,26):C.UVGC_652_396,(0,0,0):C.UVGC_652_397,(0,1,1):C.UVGC_622_330,(0,1,2):C.UVGC_622_331,(0,1,3):C.UVGC_622_332,(0,1,4):C.UVGC_622_333,(0,1,5):C.UVGC_622_334,(0,1,6):C.UVGC_622_335,(0,1,7):C.UVGC_622_336,(0,1,8):C.UVGC_622_337,(0,1,9):C.UVGC_622_338,(0,1,10):C.UVGC_622_339,(0,1,11):C.UVGC_622_340,(0,1,12):C.UVGC_622_341,(0,1,13):C.UVGC_622_342,(0,1,14):C.UVGC_622_343,(0,1,15):C.UVGC_622_344,(0,1,16):C.UVGC_622_345,(0,1,17):C.UVGC_622_346,(0,1,18):C.UVGC_622_347,(0,1,19):C.UVGC_622_348,(0,1,20):C.UVGC_622_349,(0,1,21):C.UVGC_622_350,(0,1,22):C.UVGC_622_351,(0,1,23):C.UVGC_622_352,(0,1,24):C.UVGC_622_353,(0,1,25):C.UVGC_622_354,(0,1,26):C.UVGC_622_355,(0,1,0):C.UVGC_625_357})

V_627 = CTVertex(name = 'V_627',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.Xd, P.YS3Qu1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.YS3Qu1], [P.g, P.u, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_338_48,(0,0,1):C.UVGC_338_49})

V_628 = CTVertex(name = 'V_628',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.Xm, P.YS3Qu1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.YS3Qu1], [P.g, P.u, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_338_48,(0,0,1):C.UVGC_338_49})

V_629 = CTVertex(name = 'V_629',
                 type = 'UV',
                 particles = [ P.a, P.W__minus__, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_346_59,(0,0,2):C.UVGC_346_60,(0,0,1):C.UVGC_346_61})

V_630 = CTVertex(name = 'V_630',
                 type = 'UV',
                 particles = [ P.g, P.W__minus__, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,2):C.UVGC_697_629,(0,0,3):C.UVGC_697_630,(0,0,4):C.UVGC_697_631,(0,0,5):C.UVGC_697_632,(0,0,6):C.UVGC_697_633,(0,0,7):C.UVGC_697_634,(0,0,8):C.UVGC_697_635,(0,0,9):C.UVGC_697_636,(0,0,10):C.UVGC_697_637,(0,0,11):C.UVGC_697_638,(0,0,12):C.UVGC_697_639,(0,0,13):C.UVGC_697_640,(0,0,14):C.UVGC_697_641,(0,0,15):C.UVGC_697_642,(0,0,16):C.UVGC_697_643,(0,0,17):C.UVGC_697_644,(0,0,18):C.UVGC_697_645,(0,0,19):C.UVGC_697_646,(0,0,20):C.UVGC_697_647,(0,0,21):C.UVGC_697_648,(0,0,22):C.UVGC_697_649,(0,0,23):C.UVGC_697_650,(0,0,24):C.UVGC_697_651,(0,0,25):C.UVGC_697_652,(0,0,26):C.UVGC_697_653,(0,0,27):C.UVGC_697_654,(0,0,0):C.UVGC_697_655,(0,0,1):C.UVGC_697_656})

V_631 = CTVertex(name = 'V_631',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_340_53,(0,0,2):C.UVGC_340_54,(0,0,1):C.UVGC_340_55})

V_632 = CTVertex(name = 'V_632',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,1):C.UVGC_673_468,(0,0,2):C.UVGC_673_469,(0,0,3):C.UVGC_673_470,(0,0,4):C.UVGC_673_471,(0,0,5):C.UVGC_673_472,(0,0,6):C.UVGC_673_473,(0,0,7):C.UVGC_673_474,(0,0,8):C.UVGC_673_475,(0,0,9):C.UVGC_673_476,(0,0,10):C.UVGC_673_477,(0,0,11):C.UVGC_673_478,(0,0,12):C.UVGC_673_479,(0,0,13):C.UVGC_673_480,(0,0,14):C.UVGC_673_481,(0,0,15):C.UVGC_673_482,(0,0,16):C.UVGC_673_483,(0,0,17):C.UVGC_673_484,(0,0,18):C.UVGC_673_485,(0,0,19):C.UVGC_673_486,(0,0,20):C.UVGC_673_487,(0,0,21):C.UVGC_673_488,(0,0,22):C.UVGC_673_489,(0,0,23):C.UVGC_673_490,(0,0,24):C.UVGC_673_491,(0,0,25):C.UVGC_673_492,(0,0,26):C.UVGC_673_493,(0,0,0):C.UVGC_673_494})

V_633 = CTVertex(name = 'V_633',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3Qu1] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,2):C.UVGC_682_548,(2,0,0):C.UVGC_682_549,(2,0,3):C.UVGC_681_523,(2,0,4):C.UVGC_681_524,(2,0,5):C.UVGC_681_525,(2,0,6):C.UVGC_681_526,(2,0,7):C.UVGC_681_527,(2,0,8):C.UVGC_681_528,(2,0,9):C.UVGC_681_529,(2,0,10):C.UVGC_681_530,(2,0,11):C.UVGC_681_531,(2,0,12):C.UVGC_681_532,(2,0,13):C.UVGC_681_533,(2,0,14):C.UVGC_681_534,(2,0,15):C.UVGC_681_535,(2,0,16):C.UVGC_682_550,(2,0,17):C.UVGC_682_551,(2,0,18):C.UVGC_682_552,(2,0,19):C.UVGC_682_553,(2,0,20):C.UVGC_682_554,(2,0,21):C.UVGC_682_555,(2,0,22):C.UVGC_682_556,(2,0,23):C.UVGC_682_557,(2,0,24):C.UVGC_682_558,(2,0,25):C.UVGC_682_559,(2,0,26):C.UVGC_682_560,(2,0,27):C.UVGC_682_561,(2,0,1):C.UVGC_682_562,(1,0,2):C.UVGC_682_548,(1,0,0):C.UVGC_682_549,(1,0,3):C.UVGC_681_523,(1,0,4):C.UVGC_681_524,(1,0,5):C.UVGC_681_525,(1,0,6):C.UVGC_681_526,(1,0,7):C.UVGC_681_527,(1,0,8):C.UVGC_681_528,(1,0,9):C.UVGC_681_529,(1,0,10):C.UVGC_681_530,(1,0,11):C.UVGC_681_531,(1,0,12):C.UVGC_681_532,(1,0,13):C.UVGC_681_533,(1,0,14):C.UVGC_681_534,(1,0,15):C.UVGC_681_535,(1,0,16):C.UVGC_682_550,(1,0,17):C.UVGC_682_551,(1,0,18):C.UVGC_682_552,(1,0,19):C.UVGC_682_553,(1,0,20):C.UVGC_682_554,(1,0,21):C.UVGC_682_555,(1,0,22):C.UVGC_682_556,(1,0,23):C.UVGC_682_557,(1,0,24):C.UVGC_682_558,(1,0,25):C.UVGC_682_559,(1,0,26):C.UVGC_682_560,(1,0,27):C.UVGC_682_561,(1,0,1):C.UVGC_682_562,(0,0,0):C.UVGC_278_30,(0,0,1):C.UVGC_278_31})

V_634 = CTVertex(name = 'V_634',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.c, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.g, P.YS3Qu2], [P.c, P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_334_40,(0,0,1):C.UVGC_334_41})

V_635 = CTVertex(name = 'V_635',
                 type = 'UV',
                 particles = [ P.Xm, P.c, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.g, P.YS3Qu2], [P.c, P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_334_40,(0,0,1):C.UVGC_334_41})

V_636 = CTVertex(name = 'V_636',
                 type = 'UV',
                 particles = [ P.a, P.W__plus__, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_346_59,(0,0,2):C.UVGC_346_60,(0,0,1):C.UVGC_346_61})

V_637 = CTVertex(name = 'V_637',
                 type = 'UV',
                 particles = [ P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,2):C.UVGC_697_629,(0,0,3):C.UVGC_697_630,(0,0,4):C.UVGC_697_631,(0,0,5):C.UVGC_697_632,(0,0,6):C.UVGC_697_633,(0,0,7):C.UVGC_697_634,(0,0,8):C.UVGC_697_635,(0,0,9):C.UVGC_697_636,(0,0,10):C.UVGC_697_637,(0,0,11):C.UVGC_697_638,(0,0,12):C.UVGC_697_639,(0,0,13):C.UVGC_697_640,(0,0,14):C.UVGC_697_641,(0,0,15):C.UVGC_697_642,(0,0,16):C.UVGC_697_643,(0,0,17):C.UVGC_697_644,(0,0,18):C.UVGC_697_645,(0,0,19):C.UVGC_697_646,(0,0,20):C.UVGC_697_647,(0,0,21):C.UVGC_697_648,(0,0,22):C.UVGC_697_649,(0,0,23):C.UVGC_697_650,(0,0,24):C.UVGC_697_651,(0,0,25):C.UVGC_697_652,(0,0,26):C.UVGC_697_653,(0,0,27):C.UVGC_697_654,(0,0,0):C.UVGC_697_655,(0,0,1):C.UVGC_697_656})

V_638 = CTVertex(name = 'V_638',
                 type = 'UV',
                 particles = [ P.g, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,1):C.UVGC_652_371,(0,0,2):C.UVGC_652_372,(0,0,3):C.UVGC_652_373,(0,0,4):C.UVGC_652_374,(0,0,5):C.UVGC_652_375,(0,0,6):C.UVGC_652_376,(0,0,7):C.UVGC_652_377,(0,0,8):C.UVGC_652_378,(0,0,9):C.UVGC_652_379,(0,0,10):C.UVGC_652_380,(0,0,11):C.UVGC_652_381,(0,0,12):C.UVGC_652_382,(0,0,13):C.UVGC_652_383,(0,0,14):C.UVGC_652_384,(0,0,15):C.UVGC_652_385,(0,0,16):C.UVGC_652_386,(0,0,17):C.UVGC_652_387,(0,0,18):C.UVGC_652_388,(0,0,19):C.UVGC_652_389,(0,0,20):C.UVGC_652_390,(0,0,21):C.UVGC_652_391,(0,0,22):C.UVGC_652_392,(0,0,23):C.UVGC_652_393,(0,0,24):C.UVGC_652_394,(0,0,25):C.UVGC_652_395,(0,0,26):C.UVGC_652_396,(0,0,0):C.UVGC_652_397,(0,1,1):C.UVGC_622_330,(0,1,2):C.UVGC_622_331,(0,1,3):C.UVGC_622_332,(0,1,4):C.UVGC_622_333,(0,1,5):C.UVGC_622_334,(0,1,6):C.UVGC_622_335,(0,1,7):C.UVGC_622_336,(0,1,8):C.UVGC_622_337,(0,1,9):C.UVGC_622_338,(0,1,10):C.UVGC_622_339,(0,1,11):C.UVGC_622_340,(0,1,12):C.UVGC_622_341,(0,1,13):C.UVGC_622_342,(0,1,14):C.UVGC_622_343,(0,1,15):C.UVGC_622_344,(0,1,16):C.UVGC_622_345,(0,1,17):C.UVGC_622_346,(0,1,18):C.UVGC_622_347,(0,1,19):C.UVGC_622_348,(0,1,20):C.UVGC_622_349,(0,1,21):C.UVGC_622_350,(0,1,22):C.UVGC_622_351,(0,1,23):C.UVGC_622_352,(0,1,24):C.UVGC_622_353,(0,1,25):C.UVGC_622_354,(0,1,26):C.UVGC_622_355,(0,1,0):C.UVGC_625_357})

V_639 = CTVertex(name = 'V_639',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.Xd, P.YS3Qu2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.g, P.YS3Qu2], [P.c, P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_334_40,(0,0,1):C.UVGC_334_41})

V_640 = CTVertex(name = 'V_640',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.Xm, P.YS3Qu2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.g, P.YS3Qu2], [P.c, P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_334_40,(0,0,1):C.UVGC_334_41})

V_641 = CTVertex(name = 'V_641',
                 type = 'UV',
                 particles = [ P.a, P.W__minus__, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_346_59,(0,0,2):C.UVGC_346_60,(0,0,1):C.UVGC_346_61})

V_642 = CTVertex(name = 'V_642',
                 type = 'UV',
                 particles = [ P.g, P.W__minus__, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,2):C.UVGC_697_629,(0,0,3):C.UVGC_697_630,(0,0,4):C.UVGC_697_631,(0,0,5):C.UVGC_697_632,(0,0,6):C.UVGC_697_633,(0,0,7):C.UVGC_697_634,(0,0,8):C.UVGC_697_635,(0,0,9):C.UVGC_697_636,(0,0,10):C.UVGC_697_637,(0,0,11):C.UVGC_697_638,(0,0,12):C.UVGC_697_639,(0,0,13):C.UVGC_697_640,(0,0,14):C.UVGC_697_641,(0,0,15):C.UVGC_697_642,(0,0,16):C.UVGC_697_643,(0,0,17):C.UVGC_697_644,(0,0,18):C.UVGC_697_645,(0,0,19):C.UVGC_697_646,(0,0,20):C.UVGC_697_647,(0,0,21):C.UVGC_697_648,(0,0,22):C.UVGC_697_649,(0,0,23):C.UVGC_697_650,(0,0,24):C.UVGC_697_651,(0,0,25):C.UVGC_697_652,(0,0,26):C.UVGC_697_653,(0,0,27):C.UVGC_697_654,(0,0,0):C.UVGC_697_655,(0,0,1):C.UVGC_697_656})

V_643 = CTVertex(name = 'V_643',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_340_53,(0,0,2):C.UVGC_340_54,(0,0,1):C.UVGC_340_55})

V_644 = CTVertex(name = 'V_644',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,1):C.UVGC_673_468,(0,0,2):C.UVGC_673_469,(0,0,3):C.UVGC_673_470,(0,0,4):C.UVGC_673_471,(0,0,5):C.UVGC_673_472,(0,0,6):C.UVGC_673_473,(0,0,7):C.UVGC_673_474,(0,0,8):C.UVGC_673_475,(0,0,9):C.UVGC_673_476,(0,0,10):C.UVGC_673_477,(0,0,11):C.UVGC_673_478,(0,0,12):C.UVGC_673_479,(0,0,13):C.UVGC_673_480,(0,0,14):C.UVGC_673_481,(0,0,15):C.UVGC_673_482,(0,0,16):C.UVGC_673_483,(0,0,17):C.UVGC_673_484,(0,0,18):C.UVGC_673_485,(0,0,19):C.UVGC_673_486,(0,0,20):C.UVGC_673_487,(0,0,21):C.UVGC_673_488,(0,0,22):C.UVGC_673_489,(0,0,23):C.UVGC_673_490,(0,0,24):C.UVGC_673_491,(0,0,25):C.UVGC_673_492,(0,0,26):C.UVGC_673_493,(0,0,0):C.UVGC_673_494})

V_645 = CTVertex(name = 'V_645',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3Qu2] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,2):C.UVGC_682_548,(2,0,0):C.UVGC_682_549,(2,0,3):C.UVGC_681_523,(2,0,4):C.UVGC_681_524,(2,0,5):C.UVGC_681_525,(2,0,6):C.UVGC_681_526,(2,0,7):C.UVGC_681_527,(2,0,8):C.UVGC_681_528,(2,0,9):C.UVGC_681_529,(2,0,10):C.UVGC_681_530,(2,0,11):C.UVGC_681_531,(2,0,12):C.UVGC_681_532,(2,0,13):C.UVGC_681_533,(2,0,14):C.UVGC_681_534,(2,0,15):C.UVGC_681_535,(2,0,16):C.UVGC_682_550,(2,0,17):C.UVGC_682_551,(2,0,18):C.UVGC_682_552,(2,0,19):C.UVGC_682_553,(2,0,20):C.UVGC_682_554,(2,0,21):C.UVGC_682_555,(2,0,22):C.UVGC_682_556,(2,0,23):C.UVGC_682_557,(2,0,24):C.UVGC_682_558,(2,0,25):C.UVGC_682_559,(2,0,26):C.UVGC_682_560,(2,0,27):C.UVGC_682_561,(2,0,1):C.UVGC_682_562,(1,0,2):C.UVGC_682_548,(1,0,0):C.UVGC_682_549,(1,0,3):C.UVGC_681_523,(1,0,4):C.UVGC_681_524,(1,0,5):C.UVGC_681_525,(1,0,6):C.UVGC_681_526,(1,0,7):C.UVGC_681_527,(1,0,8):C.UVGC_681_528,(1,0,9):C.UVGC_681_529,(1,0,10):C.UVGC_681_530,(1,0,11):C.UVGC_681_531,(1,0,12):C.UVGC_681_532,(1,0,13):C.UVGC_681_533,(1,0,14):C.UVGC_681_534,(1,0,15):C.UVGC_681_535,(1,0,16):C.UVGC_682_550,(1,0,17):C.UVGC_682_551,(1,0,18):C.UVGC_682_552,(1,0,19):C.UVGC_682_553,(1,0,20):C.UVGC_682_554,(1,0,21):C.UVGC_682_555,(1,0,22):C.UVGC_682_556,(1,0,23):C.UVGC_682_557,(1,0,24):C.UVGC_682_558,(1,0,25):C.UVGC_682_559,(1,0,26):C.UVGC_682_560,(1,0,27):C.UVGC_682_561,(1,0,1):C.UVGC_682_562,(0,0,0):C.UVGC_278_30,(0,0,1):C.UVGC_278_31})

V_646 = CTVertex(name = 'V_646',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.t, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.YS3Qu3], [P.g, P.t, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_523_167,(0,0,1):C.UVGC_333_39})

V_647 = CTVertex(name = 'V_647',
                 type = 'UV',
                 particles = [ P.Xm, P.t, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.YS3Qu3], [P.g, P.t, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_523_167,(0,0,1):C.UVGC_333_39})

V_648 = CTVertex(name = 'V_648',
                 type = 'UV',
                 particles = [ P.a, P.W__plus__, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_346_59,(0,0,2):C.UVGC_346_60,(0,0,1):C.UVGC_346_61})

V_649 = CTVertex(name = 'V_649',
                 type = 'UV',
                 particles = [ P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,2):C.UVGC_697_629,(0,0,3):C.UVGC_697_630,(0,0,4):C.UVGC_697_631,(0,0,5):C.UVGC_697_632,(0,0,6):C.UVGC_697_633,(0,0,7):C.UVGC_697_634,(0,0,8):C.UVGC_697_635,(0,0,9):C.UVGC_697_636,(0,0,10):C.UVGC_697_637,(0,0,11):C.UVGC_697_638,(0,0,12):C.UVGC_697_639,(0,0,13):C.UVGC_697_640,(0,0,14):C.UVGC_697_641,(0,0,15):C.UVGC_697_642,(0,0,16):C.UVGC_697_643,(0,0,17):C.UVGC_697_644,(0,0,18):C.UVGC_697_645,(0,0,19):C.UVGC_697_646,(0,0,20):C.UVGC_697_647,(0,0,21):C.UVGC_697_648,(0,0,22):C.UVGC_697_649,(0,0,23):C.UVGC_697_650,(0,0,24):C.UVGC_697_651,(0,0,25):C.UVGC_697_652,(0,0,26):C.UVGC_697_653,(0,0,27):C.UVGC_697_654,(0,0,0):C.UVGC_697_655,(0,0,1):C.UVGC_697_656})

V_650 = CTVertex(name = 'V_650',
                 type = 'UV',
                 particles = [ P.g, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,1):C.UVGC_652_371,(0,0,2):C.UVGC_652_372,(0,0,3):C.UVGC_652_373,(0,0,4):C.UVGC_652_374,(0,0,5):C.UVGC_652_375,(0,0,6):C.UVGC_652_376,(0,0,7):C.UVGC_652_377,(0,0,8):C.UVGC_652_378,(0,0,9):C.UVGC_652_379,(0,0,10):C.UVGC_652_380,(0,0,11):C.UVGC_652_381,(0,0,12):C.UVGC_652_382,(0,0,13):C.UVGC_652_383,(0,0,14):C.UVGC_652_384,(0,0,15):C.UVGC_652_385,(0,0,16):C.UVGC_652_386,(0,0,17):C.UVGC_652_387,(0,0,18):C.UVGC_652_388,(0,0,19):C.UVGC_652_389,(0,0,20):C.UVGC_652_390,(0,0,21):C.UVGC_652_391,(0,0,22):C.UVGC_652_392,(0,0,23):C.UVGC_652_393,(0,0,24):C.UVGC_652_394,(0,0,25):C.UVGC_652_395,(0,0,26):C.UVGC_652_396,(0,0,0):C.UVGC_652_397,(0,1,1):C.UVGC_622_330,(0,1,2):C.UVGC_622_331,(0,1,3):C.UVGC_622_332,(0,1,4):C.UVGC_622_333,(0,1,5):C.UVGC_622_334,(0,1,6):C.UVGC_622_335,(0,1,7):C.UVGC_622_336,(0,1,8):C.UVGC_622_337,(0,1,9):C.UVGC_622_338,(0,1,10):C.UVGC_622_339,(0,1,11):C.UVGC_622_340,(0,1,12):C.UVGC_622_341,(0,1,13):C.UVGC_622_342,(0,1,14):C.UVGC_622_343,(0,1,15):C.UVGC_622_344,(0,1,16):C.UVGC_622_345,(0,1,17):C.UVGC_622_346,(0,1,18):C.UVGC_622_347,(0,1,19):C.UVGC_622_348,(0,1,20):C.UVGC_622_349,(0,1,21):C.UVGC_622_350,(0,1,22):C.UVGC_622_351,(0,1,23):C.UVGC_622_352,(0,1,24):C.UVGC_622_353,(0,1,25):C.UVGC_622_354,(0,1,26):C.UVGC_622_355,(0,1,0):C.UVGC_625_357})

V_651 = CTVertex(name = 'V_651',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.Xd, P.YS3Qu3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.YS3Qu3], [P.g, P.t, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_523_167,(0,0,1):C.UVGC_333_39})

V_652 = CTVertex(name = 'V_652',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.Xm, P.YS3Qu3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.YS3Qu3], [P.g, P.t, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_523_167,(0,0,1):C.UVGC_333_39})

V_653 = CTVertex(name = 'V_653',
                 type = 'UV',
                 particles = [ P.a, P.W__minus__, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_346_59,(0,0,2):C.UVGC_346_60,(0,0,1):C.UVGC_346_61})

V_654 = CTVertex(name = 'V_654',
                 type = 'UV',
                 particles = [ P.g, P.W__minus__, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,2):C.UVGC_697_629,(0,0,3):C.UVGC_697_630,(0,0,4):C.UVGC_697_631,(0,0,5):C.UVGC_697_632,(0,0,6):C.UVGC_697_633,(0,0,7):C.UVGC_697_634,(0,0,8):C.UVGC_697_635,(0,0,9):C.UVGC_697_636,(0,0,10):C.UVGC_697_637,(0,0,11):C.UVGC_697_638,(0,0,12):C.UVGC_697_639,(0,0,13):C.UVGC_697_640,(0,0,14):C.UVGC_697_641,(0,0,15):C.UVGC_697_642,(0,0,16):C.UVGC_697_643,(0,0,17):C.UVGC_697_644,(0,0,18):C.UVGC_697_645,(0,0,19):C.UVGC_697_646,(0,0,20):C.UVGC_697_647,(0,0,21):C.UVGC_697_648,(0,0,22):C.UVGC_697_649,(0,0,23):C.UVGC_697_650,(0,0,24):C.UVGC_697_651,(0,0,25):C.UVGC_697_652,(0,0,26):C.UVGC_697_653,(0,0,27):C.UVGC_697_654,(0,0,0):C.UVGC_697_655,(0,0,1):C.UVGC_697_656})

V_655 = CTVertex(name = 'V_655',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_340_53,(0,0,2):C.UVGC_340_54,(0,0,1):C.UVGC_340_55})

V_656 = CTVertex(name = 'V_656',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,1):C.UVGC_673_468,(0,0,2):C.UVGC_673_469,(0,0,3):C.UVGC_673_470,(0,0,4):C.UVGC_673_471,(0,0,5):C.UVGC_673_472,(0,0,6):C.UVGC_673_473,(0,0,7):C.UVGC_673_474,(0,0,8):C.UVGC_673_475,(0,0,9):C.UVGC_673_476,(0,0,10):C.UVGC_673_477,(0,0,11):C.UVGC_673_478,(0,0,12):C.UVGC_673_479,(0,0,13):C.UVGC_673_480,(0,0,14):C.UVGC_673_481,(0,0,15):C.UVGC_673_482,(0,0,16):C.UVGC_673_483,(0,0,17):C.UVGC_673_484,(0,0,18):C.UVGC_673_485,(0,0,19):C.UVGC_673_486,(0,0,20):C.UVGC_673_487,(0,0,21):C.UVGC_673_488,(0,0,22):C.UVGC_673_489,(0,0,23):C.UVGC_673_490,(0,0,24):C.UVGC_673_491,(0,0,25):C.UVGC_673_492,(0,0,26):C.UVGC_673_493,(0,0,0):C.UVGC_673_494})

V_657 = CTVertex(name = 'V_657',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3Qu3] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,2):C.UVGC_682_548,(2,0,0):C.UVGC_682_549,(2,0,3):C.UVGC_681_523,(2,0,4):C.UVGC_681_524,(2,0,5):C.UVGC_681_525,(2,0,6):C.UVGC_681_526,(2,0,7):C.UVGC_681_527,(2,0,8):C.UVGC_681_528,(2,0,9):C.UVGC_681_529,(2,0,10):C.UVGC_681_530,(2,0,11):C.UVGC_681_531,(2,0,12):C.UVGC_681_532,(2,0,13):C.UVGC_681_533,(2,0,14):C.UVGC_681_534,(2,0,15):C.UVGC_681_535,(2,0,16):C.UVGC_682_550,(2,0,17):C.UVGC_682_551,(2,0,18):C.UVGC_682_552,(2,0,19):C.UVGC_682_553,(2,0,20):C.UVGC_682_554,(2,0,21):C.UVGC_682_555,(2,0,22):C.UVGC_682_556,(2,0,23):C.UVGC_682_557,(2,0,24):C.UVGC_682_558,(2,0,25):C.UVGC_682_559,(2,0,26):C.UVGC_682_560,(2,0,27):C.UVGC_682_561,(2,0,1):C.UVGC_682_562,(1,0,2):C.UVGC_682_548,(1,0,0):C.UVGC_682_549,(1,0,3):C.UVGC_681_523,(1,0,4):C.UVGC_681_524,(1,0,5):C.UVGC_681_525,(1,0,6):C.UVGC_681_526,(1,0,7):C.UVGC_681_527,(1,0,8):C.UVGC_681_528,(1,0,9):C.UVGC_681_529,(1,0,10):C.UVGC_681_530,(1,0,11):C.UVGC_681_531,(1,0,12):C.UVGC_681_532,(1,0,13):C.UVGC_681_533,(1,0,14):C.UVGC_681_534,(1,0,15):C.UVGC_681_535,(1,0,16):C.UVGC_682_550,(1,0,17):C.UVGC_682_551,(1,0,18):C.UVGC_682_552,(1,0,19):C.UVGC_682_553,(1,0,20):C.UVGC_682_554,(1,0,21):C.UVGC_682_555,(1,0,22):C.UVGC_682_556,(1,0,23):C.UVGC_682_557,(1,0,24):C.UVGC_682_558,(1,0,25):C.UVGC_682_559,(1,0,26):C.UVGC_682_560,(1,0,27):C.UVGC_682_561,(1,0,1):C.UVGC_682_562,(0,0,0):C.UVGC_278_30,(0,0,1):C.UVGC_278_31})

V_658 = CTVertex(name = 'V_658',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.u, P.YS3u1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.YS3u1], [P.g, P.u, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_367_64,(0,0,1):C.UVGC_367_65})

V_659 = CTVertex(name = 'V_659',
                 type = 'UV',
                 particles = [ P.Xm, P.u, P.YS3u1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.YS3u1], [P.g, P.u, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_367_64,(0,0,1):C.UVGC_367_65})

V_660 = CTVertex(name = 'V_660',
                 type = 'UV',
                 particles = [ P.g, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,1):C.UVGC_652_371,(0,0,2):C.UVGC_652_372,(0,0,3):C.UVGC_652_373,(0,0,4):C.UVGC_652_374,(0,0,5):C.UVGC_652_375,(0,0,6):C.UVGC_652_376,(0,0,7):C.UVGC_652_377,(0,0,8):C.UVGC_652_378,(0,0,9):C.UVGC_652_379,(0,0,10):C.UVGC_652_380,(0,0,11):C.UVGC_652_381,(0,0,12):C.UVGC_652_382,(0,0,13):C.UVGC_652_383,(0,0,14):C.UVGC_652_384,(0,0,15):C.UVGC_652_385,(0,0,16):C.UVGC_652_386,(0,0,17):C.UVGC_652_387,(0,0,18):C.UVGC_652_388,(0,0,19):C.UVGC_652_389,(0,0,20):C.UVGC_652_390,(0,0,21):C.UVGC_652_391,(0,0,22):C.UVGC_652_392,(0,0,23):C.UVGC_652_393,(0,0,24):C.UVGC_652_394,(0,0,25):C.UVGC_652_395,(0,0,26):C.UVGC_652_396,(0,0,0):C.UVGC_652_397,(0,1,1):C.UVGC_622_330,(0,1,2):C.UVGC_622_331,(0,1,3):C.UVGC_622_332,(0,1,4):C.UVGC_622_333,(0,1,5):C.UVGC_622_334,(0,1,6):C.UVGC_622_335,(0,1,7):C.UVGC_622_336,(0,1,8):C.UVGC_622_337,(0,1,9):C.UVGC_622_338,(0,1,10):C.UVGC_622_339,(0,1,11):C.UVGC_622_340,(0,1,12):C.UVGC_622_341,(0,1,13):C.UVGC_622_342,(0,1,14):C.UVGC_622_343,(0,1,15):C.UVGC_622_344,(0,1,16):C.UVGC_622_345,(0,1,17):C.UVGC_622_346,(0,1,18):C.UVGC_622_347,(0,1,19):C.UVGC_622_348,(0,1,20):C.UVGC_622_349,(0,1,21):C.UVGC_622_350,(0,1,22):C.UVGC_622_351,(0,1,23):C.UVGC_622_352,(0,1,24):C.UVGC_622_353,(0,1,25):C.UVGC_622_354,(0,1,26):C.UVGC_622_355,(0,1,0):C.UVGC_625_357})

V_661 = CTVertex(name = 'V_661',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.Xd, P.YS3u1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.YS3u1], [P.g, P.u, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_367_64,(0,0,1):C.UVGC_367_65})

V_662 = CTVertex(name = 'V_662',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.Xm, P.YS3u1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.YS3u1], [P.g, P.u, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_367_64,(0,0,1):C.UVGC_367_65})

V_663 = CTVertex(name = 'V_663',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,1):C.UVGC_673_468,(0,0,2):C.UVGC_673_469,(0,0,3):C.UVGC_673_470,(0,0,4):C.UVGC_673_471,(0,0,5):C.UVGC_673_472,(0,0,6):C.UVGC_673_473,(0,0,7):C.UVGC_673_474,(0,0,8):C.UVGC_673_475,(0,0,9):C.UVGC_673_476,(0,0,10):C.UVGC_673_477,(0,0,11):C.UVGC_673_478,(0,0,12):C.UVGC_673_479,(0,0,13):C.UVGC_673_480,(0,0,14):C.UVGC_673_481,(0,0,15):C.UVGC_673_482,(0,0,16):C.UVGC_673_483,(0,0,17):C.UVGC_673_484,(0,0,18):C.UVGC_673_485,(0,0,19):C.UVGC_673_486,(0,0,20):C.UVGC_673_487,(0,0,21):C.UVGC_673_488,(0,0,22):C.UVGC_673_489,(0,0,23):C.UVGC_673_490,(0,0,24):C.UVGC_673_491,(0,0,25):C.UVGC_673_492,(0,0,26):C.UVGC_673_493,(0,0,0):C.UVGC_673_494})

V_664 = CTVertex(name = 'V_664',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3u1] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,2):C.UVGC_682_548,(2,0,0):C.UVGC_682_549,(2,0,3):C.UVGC_681_523,(2,0,4):C.UVGC_681_524,(2,0,5):C.UVGC_681_525,(2,0,6):C.UVGC_681_526,(2,0,7):C.UVGC_681_527,(2,0,8):C.UVGC_681_528,(2,0,9):C.UVGC_681_529,(2,0,10):C.UVGC_681_530,(2,0,11):C.UVGC_681_531,(2,0,12):C.UVGC_681_532,(2,0,13):C.UVGC_681_533,(2,0,14):C.UVGC_681_534,(2,0,15):C.UVGC_681_535,(2,0,16):C.UVGC_682_550,(2,0,17):C.UVGC_682_551,(2,0,18):C.UVGC_682_552,(2,0,19):C.UVGC_682_553,(2,0,20):C.UVGC_682_554,(2,0,21):C.UVGC_682_555,(2,0,22):C.UVGC_682_556,(2,0,23):C.UVGC_682_557,(2,0,24):C.UVGC_682_558,(2,0,25):C.UVGC_682_559,(2,0,26):C.UVGC_682_560,(2,0,27):C.UVGC_682_561,(2,0,1):C.UVGC_682_562,(1,0,2):C.UVGC_682_548,(1,0,0):C.UVGC_682_549,(1,0,3):C.UVGC_681_523,(1,0,4):C.UVGC_681_524,(1,0,5):C.UVGC_681_525,(1,0,6):C.UVGC_681_526,(1,0,7):C.UVGC_681_527,(1,0,8):C.UVGC_681_528,(1,0,9):C.UVGC_681_529,(1,0,10):C.UVGC_681_530,(1,0,11):C.UVGC_681_531,(1,0,12):C.UVGC_681_532,(1,0,13):C.UVGC_681_533,(1,0,14):C.UVGC_681_534,(1,0,15):C.UVGC_681_535,(1,0,16):C.UVGC_682_550,(1,0,17):C.UVGC_682_551,(1,0,18):C.UVGC_682_552,(1,0,19):C.UVGC_682_553,(1,0,20):C.UVGC_682_554,(1,0,21):C.UVGC_682_555,(1,0,22):C.UVGC_682_556,(1,0,23):C.UVGC_682_557,(1,0,24):C.UVGC_682_558,(1,0,25):C.UVGC_682_559,(1,0,26):C.UVGC_682_560,(1,0,27):C.UVGC_682_561,(1,0,1):C.UVGC_682_562,(0,0,0):C.UVGC_278_30,(0,0,1):C.UVGC_278_31})

V_665 = CTVertex(name = 'V_665',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.c, P.YS3u2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.g, P.YS3u2], [P.c, P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_335_42,(0,0,1):C.UVGC_335_43})

V_666 = CTVertex(name = 'V_666',
                 type = 'UV',
                 particles = [ P.Xm, P.c, P.YS3u2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.g, P.YS3u2], [P.c, P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_335_42,(0,0,1):C.UVGC_335_43})

V_667 = CTVertex(name = 'V_667',
                 type = 'UV',
                 particles = [ P.g, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,1):C.UVGC_652_371,(0,0,2):C.UVGC_652_372,(0,0,3):C.UVGC_652_373,(0,0,4):C.UVGC_652_374,(0,0,5):C.UVGC_652_375,(0,0,6):C.UVGC_652_376,(0,0,7):C.UVGC_652_377,(0,0,8):C.UVGC_652_378,(0,0,9):C.UVGC_652_379,(0,0,10):C.UVGC_652_380,(0,0,11):C.UVGC_652_381,(0,0,12):C.UVGC_652_382,(0,0,13):C.UVGC_652_383,(0,0,14):C.UVGC_652_384,(0,0,15):C.UVGC_652_385,(0,0,16):C.UVGC_652_386,(0,0,17):C.UVGC_652_387,(0,0,18):C.UVGC_652_388,(0,0,19):C.UVGC_652_389,(0,0,20):C.UVGC_652_390,(0,0,21):C.UVGC_652_391,(0,0,22):C.UVGC_652_392,(0,0,23):C.UVGC_652_393,(0,0,24):C.UVGC_652_394,(0,0,25):C.UVGC_652_395,(0,0,26):C.UVGC_652_396,(0,0,0):C.UVGC_652_397,(0,1,1):C.UVGC_622_330,(0,1,2):C.UVGC_622_331,(0,1,3):C.UVGC_622_332,(0,1,4):C.UVGC_622_333,(0,1,5):C.UVGC_622_334,(0,1,6):C.UVGC_622_335,(0,1,7):C.UVGC_622_336,(0,1,8):C.UVGC_622_337,(0,1,9):C.UVGC_622_338,(0,1,10):C.UVGC_622_339,(0,1,11):C.UVGC_622_340,(0,1,12):C.UVGC_622_341,(0,1,13):C.UVGC_622_342,(0,1,14):C.UVGC_622_343,(0,1,15):C.UVGC_622_344,(0,1,16):C.UVGC_622_345,(0,1,17):C.UVGC_622_346,(0,1,18):C.UVGC_622_347,(0,1,19):C.UVGC_622_348,(0,1,20):C.UVGC_622_349,(0,1,21):C.UVGC_622_350,(0,1,22):C.UVGC_622_351,(0,1,23):C.UVGC_622_352,(0,1,24):C.UVGC_622_353,(0,1,25):C.UVGC_622_354,(0,1,26):C.UVGC_622_355,(0,1,0):C.UVGC_625_357})

V_668 = CTVertex(name = 'V_668',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.Xd, P.YS3u2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.g, P.YS3u2], [P.c, P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_335_42,(0,0,1):C.UVGC_335_43})

V_669 = CTVertex(name = 'V_669',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.Xm, P.YS3u2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.g, P.YS3u2], [P.c, P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_335_42,(0,0,1):C.UVGC_335_43})

V_670 = CTVertex(name = 'V_670',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,1):C.UVGC_673_468,(0,0,2):C.UVGC_673_469,(0,0,3):C.UVGC_673_470,(0,0,4):C.UVGC_673_471,(0,0,5):C.UVGC_673_472,(0,0,6):C.UVGC_673_473,(0,0,7):C.UVGC_673_474,(0,0,8):C.UVGC_673_475,(0,0,9):C.UVGC_673_476,(0,0,10):C.UVGC_673_477,(0,0,11):C.UVGC_673_478,(0,0,12):C.UVGC_673_479,(0,0,13):C.UVGC_673_480,(0,0,14):C.UVGC_673_481,(0,0,15):C.UVGC_673_482,(0,0,16):C.UVGC_673_483,(0,0,17):C.UVGC_673_484,(0,0,18):C.UVGC_673_485,(0,0,19):C.UVGC_673_486,(0,0,20):C.UVGC_673_487,(0,0,21):C.UVGC_673_488,(0,0,22):C.UVGC_673_489,(0,0,23):C.UVGC_673_490,(0,0,24):C.UVGC_673_491,(0,0,25):C.UVGC_673_492,(0,0,26):C.UVGC_673_493,(0,0,0):C.UVGC_673_494})

V_671 = CTVertex(name = 'V_671',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3u2] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,2):C.UVGC_682_548,(2,0,0):C.UVGC_682_549,(2,0,3):C.UVGC_681_523,(2,0,4):C.UVGC_681_524,(2,0,5):C.UVGC_681_525,(2,0,6):C.UVGC_681_526,(2,0,7):C.UVGC_681_527,(2,0,8):C.UVGC_681_528,(2,0,9):C.UVGC_681_529,(2,0,10):C.UVGC_681_530,(2,0,11):C.UVGC_681_531,(2,0,12):C.UVGC_681_532,(2,0,13):C.UVGC_681_533,(2,0,14):C.UVGC_681_534,(2,0,15):C.UVGC_681_535,(2,0,16):C.UVGC_682_550,(2,0,17):C.UVGC_682_551,(2,0,18):C.UVGC_682_552,(2,0,19):C.UVGC_682_553,(2,0,20):C.UVGC_682_554,(2,0,21):C.UVGC_682_555,(2,0,22):C.UVGC_682_556,(2,0,23):C.UVGC_682_557,(2,0,24):C.UVGC_682_558,(2,0,25):C.UVGC_682_559,(2,0,26):C.UVGC_682_560,(2,0,27):C.UVGC_682_561,(2,0,1):C.UVGC_682_562,(1,0,2):C.UVGC_682_548,(1,0,0):C.UVGC_682_549,(1,0,3):C.UVGC_681_523,(1,0,4):C.UVGC_681_524,(1,0,5):C.UVGC_681_525,(1,0,6):C.UVGC_681_526,(1,0,7):C.UVGC_681_527,(1,0,8):C.UVGC_681_528,(1,0,9):C.UVGC_681_529,(1,0,10):C.UVGC_681_530,(1,0,11):C.UVGC_681_531,(1,0,12):C.UVGC_681_532,(1,0,13):C.UVGC_681_533,(1,0,14):C.UVGC_681_534,(1,0,15):C.UVGC_681_535,(1,0,16):C.UVGC_682_550,(1,0,17):C.UVGC_682_551,(1,0,18):C.UVGC_682_552,(1,0,19):C.UVGC_682_553,(1,0,20):C.UVGC_682_554,(1,0,21):C.UVGC_682_555,(1,0,22):C.UVGC_682_556,(1,0,23):C.UVGC_682_557,(1,0,24):C.UVGC_682_558,(1,0,25):C.UVGC_682_559,(1,0,26):C.UVGC_682_560,(1,0,27):C.UVGC_682_561,(1,0,1):C.UVGC_682_562,(0,0,0):C.UVGC_278_30,(0,0,1):C.UVGC_278_31})

V_672 = CTVertex(name = 'V_672',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.t, P.YS3u3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.YS3u3], [P.g, P.t, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_524_168,(0,0,1):C.UVGC_524_169})

V_673 = CTVertex(name = 'V_673',
                 type = 'UV',
                 particles = [ P.Xm, P.t, P.YS3u3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.YS3u3], [P.g, P.t, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_524_168,(0,0,1):C.UVGC_524_169})

V_674 = CTVertex(name = 'V_674',
                 type = 'UV',
                 particles = [ P.g, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,1):C.UVGC_652_371,(0,0,2):C.UVGC_652_372,(0,0,3):C.UVGC_652_373,(0,0,4):C.UVGC_652_374,(0,0,5):C.UVGC_652_375,(0,0,6):C.UVGC_652_376,(0,0,7):C.UVGC_652_377,(0,0,8):C.UVGC_652_378,(0,0,9):C.UVGC_652_379,(0,0,10):C.UVGC_652_380,(0,0,11):C.UVGC_652_381,(0,0,12):C.UVGC_652_382,(0,0,13):C.UVGC_652_383,(0,0,14):C.UVGC_652_384,(0,0,15):C.UVGC_652_385,(0,0,16):C.UVGC_652_386,(0,0,17):C.UVGC_652_387,(0,0,18):C.UVGC_652_388,(0,0,19):C.UVGC_652_389,(0,0,20):C.UVGC_652_390,(0,0,21):C.UVGC_652_391,(0,0,22):C.UVGC_652_392,(0,0,23):C.UVGC_652_393,(0,0,24):C.UVGC_652_394,(0,0,25):C.UVGC_652_395,(0,0,26):C.UVGC_652_396,(0,0,0):C.UVGC_652_397,(0,1,1):C.UVGC_622_330,(0,1,2):C.UVGC_622_331,(0,1,3):C.UVGC_622_332,(0,1,4):C.UVGC_622_333,(0,1,5):C.UVGC_622_334,(0,1,6):C.UVGC_622_335,(0,1,7):C.UVGC_622_336,(0,1,8):C.UVGC_622_337,(0,1,9):C.UVGC_622_338,(0,1,10):C.UVGC_622_339,(0,1,11):C.UVGC_622_340,(0,1,12):C.UVGC_622_341,(0,1,13):C.UVGC_622_342,(0,1,14):C.UVGC_622_343,(0,1,15):C.UVGC_622_344,(0,1,16):C.UVGC_622_345,(0,1,17):C.UVGC_622_346,(0,1,18):C.UVGC_622_347,(0,1,19):C.UVGC_622_348,(0,1,20):C.UVGC_622_349,(0,1,21):C.UVGC_622_350,(0,1,22):C.UVGC_622_351,(0,1,23):C.UVGC_622_352,(0,1,24):C.UVGC_622_353,(0,1,25):C.UVGC_622_354,(0,1,26):C.UVGC_622_355,(0,1,0):C.UVGC_625_357})

V_675 = CTVertex(name = 'V_675',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.Xd, P.YS3u3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.YS3u3], [P.g, P.t, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_524_168,(0,0,1):C.UVGC_524_169})

V_676 = CTVertex(name = 'V_676',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.Xm, P.YS3u3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.YS3u3], [P.g, P.t, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_524_168,(0,0,1):C.UVGC_524_169})

V_677 = CTVertex(name = 'V_677',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,1):C.UVGC_673_468,(0,0,2):C.UVGC_673_469,(0,0,3):C.UVGC_673_470,(0,0,4):C.UVGC_673_471,(0,0,5):C.UVGC_673_472,(0,0,6):C.UVGC_673_473,(0,0,7):C.UVGC_673_474,(0,0,8):C.UVGC_673_475,(0,0,9):C.UVGC_673_476,(0,0,10):C.UVGC_673_477,(0,0,11):C.UVGC_673_478,(0,0,12):C.UVGC_673_479,(0,0,13):C.UVGC_673_480,(0,0,14):C.UVGC_673_481,(0,0,15):C.UVGC_673_482,(0,0,16):C.UVGC_673_483,(0,0,17):C.UVGC_673_484,(0,0,18):C.UVGC_673_485,(0,0,19):C.UVGC_673_486,(0,0,20):C.UVGC_673_487,(0,0,21):C.UVGC_673_488,(0,0,22):C.UVGC_673_489,(0,0,23):C.UVGC_673_490,(0,0,24):C.UVGC_673_491,(0,0,25):C.UVGC_673_492,(0,0,26):C.UVGC_673_493,(0,0,0):C.UVGC_673_494})

V_678 = CTVertex(name = 'V_678',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3u3] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,2):C.UVGC_682_548,(2,0,0):C.UVGC_682_549,(2,0,3):C.UVGC_681_523,(2,0,4):C.UVGC_681_524,(2,0,5):C.UVGC_681_525,(2,0,6):C.UVGC_681_526,(2,0,7):C.UVGC_681_527,(2,0,8):C.UVGC_681_528,(2,0,9):C.UVGC_681_529,(2,0,10):C.UVGC_681_530,(2,0,11):C.UVGC_681_531,(2,0,12):C.UVGC_681_532,(2,0,13):C.UVGC_681_533,(2,0,14):C.UVGC_681_534,(2,0,15):C.UVGC_681_535,(2,0,16):C.UVGC_682_550,(2,0,17):C.UVGC_682_551,(2,0,18):C.UVGC_682_552,(2,0,19):C.UVGC_682_553,(2,0,20):C.UVGC_682_554,(2,0,21):C.UVGC_682_555,(2,0,22):C.UVGC_682_556,(2,0,23):C.UVGC_682_557,(2,0,24):C.UVGC_682_558,(2,0,25):C.UVGC_682_559,(2,0,26):C.UVGC_682_560,(2,0,27):C.UVGC_682_561,(2,0,1):C.UVGC_682_562,(1,0,2):C.UVGC_682_548,(1,0,0):C.UVGC_682_549,(1,0,3):C.UVGC_681_523,(1,0,4):C.UVGC_681_524,(1,0,5):C.UVGC_681_525,(1,0,6):C.UVGC_681_526,(1,0,7):C.UVGC_681_527,(1,0,8):C.UVGC_681_528,(1,0,9):C.UVGC_681_529,(1,0,10):C.UVGC_681_530,(1,0,11):C.UVGC_681_531,(1,0,12):C.UVGC_681_532,(1,0,13):C.UVGC_681_533,(1,0,14):C.UVGC_681_534,(1,0,15):C.UVGC_681_535,(1,0,16):C.UVGC_682_550,(1,0,17):C.UVGC_682_551,(1,0,18):C.UVGC_682_552,(1,0,19):C.UVGC_682_553,(1,0,20):C.UVGC_682_554,(1,0,21):C.UVGC_682_555,(1,0,22):C.UVGC_682_556,(1,0,23):C.UVGC_682_557,(1,0,24):C.UVGC_682_558,(1,0,25):C.UVGC_682_559,(1,0,26):C.UVGC_682_560,(1,0,27):C.UVGC_682_561,(1,0,1):C.UVGC_682_562,(0,0,0):C.UVGC_278_30,(0,0,1):C.UVGC_278_31})

V_679 = CTVertex(name = 'V_679',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_529_174,(0,0,2):C.UVGC_529_175,(0,0,1):C.UVGC_529_176})

V_680 = CTVertex(name = 'V_680',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.YF3Qd1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_307_33,(0,1,0):C.UVGC_556_213,(0,2,0):C.UVGC_556_213})

V_681 = CTVertex(name = 'V_681',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.YF3Qd2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_307_33,(0,1,0):C.UVGC_562_221,(0,2,0):C.UVGC_562_221})

V_682 = CTVertex(name = 'V_682',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.YF3Qd3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_307_33,(0,1,0):C.UVGC_568_229,(0,2,0):C.UVGC_568_229})

V_683 = CTVertex(name = 'V_683',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.YF3Qu1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_316_34,(0,1,0):C.UVGC_575_236,(0,2,0):C.UVGC_575_236})

V_684 = CTVertex(name = 'V_684',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.YF3Qu2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_316_34,(0,1,0):C.UVGC_582_243,(0,2,0):C.UVGC_582_243})

V_685 = CTVertex(name = 'V_685',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.YF3Qu3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_316_34,(0,1,0):C.UVGC_589_251,(0,2,0):C.UVGC_589_251})

V_686 = CTVertex(name = 'V_686',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.YF3d1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_298_32,(0,1,0):C.UVGC_538_189,(0,2,0):C.UVGC_538_189})

V_687 = CTVertex(name = 'V_687',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.YF3d2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_298_32,(0,1,0):C.UVGC_544_197,(0,2,0):C.UVGC_544_197})

V_688 = CTVertex(name = 'V_688',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.YF3d3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_298_32,(0,1,0):C.UVGC_550_205,(0,2,0):C.UVGC_550_205})

V_689 = CTVertex(name = 'V_689',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.YF3u1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_325_35,(0,1,0):C.UVGC_595_259,(0,2,0):C.UVGC_595_259})

V_690 = CTVertex(name = 'V_690',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.YF3u2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_325_35,(0,1,0):C.UVGC_601_267,(0,2,0):C.UVGC_601_267})

V_691 = CTVertex(name = 'V_691',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.YF3u3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_325_35,(0,1,0):C.UVGC_607_275,(0,2,0):C.UVGC_607_275})

V_692 = CTVertex(name = 'V_692',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,1):C.UVGC_706_711,(0,0,2):C.UVGC_706_712,(0,0,3):C.UVGC_706_713,(0,0,4):C.UVGC_706_714,(0,0,5):C.UVGC_706_715,(0,0,6):C.UVGC_706_716,(0,0,7):C.UVGC_706_717,(0,0,8):C.UVGC_706_718,(0,0,9):C.UVGC_706_719,(0,0,10):C.UVGC_706_720,(0,0,11):C.UVGC_706_721,(0,0,12):C.UVGC_706_722,(0,0,13):C.UVGC_706_723,(0,0,14):C.UVGC_706_724,(0,0,15):C.UVGC_706_725,(0,0,16):C.UVGC_706_726,(0,0,17):C.UVGC_706_727,(0,0,18):C.UVGC_706_728,(0,0,19):C.UVGC_706_729,(0,0,20):C.UVGC_706_730,(0,0,21):C.UVGC_706_731,(0,0,22):C.UVGC_706_732,(0,0,23):C.UVGC_706_733,(0,0,24):C.UVGC_706_734,(0,0,25):C.UVGC_706_735,(0,0,26):C.UVGC_706_736,(0,0,0):C.UVGC_706_737})

V_693 = CTVertex(name = 'V_693',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,1):C.UVGC_706_711,(0,0,2):C.UVGC_706_712,(0,0,3):C.UVGC_706_713,(0,0,4):C.UVGC_706_714,(0,0,5):C.UVGC_706_715,(0,0,6):C.UVGC_706_716,(0,0,7):C.UVGC_706_717,(0,0,8):C.UVGC_706_718,(0,0,9):C.UVGC_706_719,(0,0,10):C.UVGC_706_720,(0,0,11):C.UVGC_706_721,(0,0,12):C.UVGC_706_722,(0,0,13):C.UVGC_706_723,(0,0,14):C.UVGC_706_724,(0,0,15):C.UVGC_706_725,(0,0,16):C.UVGC_706_726,(0,0,17):C.UVGC_706_727,(0,0,18):C.UVGC_706_728,(0,0,19):C.UVGC_706_729,(0,0,20):C.UVGC_706_730,(0,0,21):C.UVGC_706_731,(0,0,22):C.UVGC_706_732,(0,0,23):C.UVGC_706_733,(0,0,24):C.UVGC_706_734,(0,0,25):C.UVGC_706_735,(0,0,26):C.UVGC_706_736,(0,0,0):C.UVGC_706_737})

V_694 = CTVertex(name = 'V_694',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,1):C.UVGC_706_711,(0,0,2):C.UVGC_706_712,(0,0,3):C.UVGC_706_713,(0,0,4):C.UVGC_706_714,(0,0,5):C.UVGC_706_715,(0,0,6):C.UVGC_706_716,(0,0,7):C.UVGC_706_717,(0,0,8):C.UVGC_706_718,(0,0,9):C.UVGC_706_719,(0,0,10):C.UVGC_706_720,(0,0,11):C.UVGC_706_721,(0,0,12):C.UVGC_706_722,(0,0,13):C.UVGC_706_723,(0,0,14):C.UVGC_706_724,(0,0,15):C.UVGC_706_725,(0,0,16):C.UVGC_706_726,(0,0,17):C.UVGC_706_727,(0,0,18):C.UVGC_706_728,(0,0,19):C.UVGC_706_729,(0,0,20):C.UVGC_706_730,(0,0,21):C.UVGC_706_731,(0,0,22):C.UVGC_706_732,(0,0,23):C.UVGC_706_733,(0,0,24):C.UVGC_706_734,(0,0,25):C.UVGC_706_735,(0,0,26):C.UVGC_706_736,(0,0,0):C.UVGC_706_737})

V_695 = CTVertex(name = 'V_695',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,1):C.UVGC_703_684,(0,0,2):C.UVGC_703_685,(0,0,3):C.UVGC_703_686,(0,0,4):C.UVGC_703_687,(0,0,5):C.UVGC_703_688,(0,0,6):C.UVGC_703_689,(0,0,7):C.UVGC_703_690,(0,0,8):C.UVGC_703_691,(0,0,9):C.UVGC_703_692,(0,0,10):C.UVGC_703_693,(0,0,11):C.UVGC_703_694,(0,0,12):C.UVGC_703_695,(0,0,13):C.UVGC_703_696,(0,0,14):C.UVGC_703_697,(0,0,15):C.UVGC_703_698,(0,0,16):C.UVGC_703_699,(0,0,17):C.UVGC_703_700,(0,0,18):C.UVGC_703_701,(0,0,19):C.UVGC_703_702,(0,0,20):C.UVGC_703_703,(0,0,21):C.UVGC_703_704,(0,0,22):C.UVGC_703_705,(0,0,23):C.UVGC_703_706,(0,0,24):C.UVGC_703_707,(0,0,25):C.UVGC_703_708,(0,0,26):C.UVGC_703_709,(0,0,0):C.UVGC_703_710})

V_696 = CTVertex(name = 'V_696',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,1):C.UVGC_703_684,(0,0,2):C.UVGC_703_685,(0,0,3):C.UVGC_703_686,(0,0,4):C.UVGC_703_687,(0,0,5):C.UVGC_703_688,(0,0,6):C.UVGC_703_689,(0,0,7):C.UVGC_703_690,(0,0,8):C.UVGC_703_691,(0,0,9):C.UVGC_703_692,(0,0,10):C.UVGC_703_693,(0,0,11):C.UVGC_703_694,(0,0,12):C.UVGC_703_695,(0,0,13):C.UVGC_703_696,(0,0,14):C.UVGC_703_697,(0,0,15):C.UVGC_703_698,(0,0,16):C.UVGC_703_699,(0,0,17):C.UVGC_703_700,(0,0,18):C.UVGC_703_701,(0,0,19):C.UVGC_703_702,(0,0,20):C.UVGC_703_703,(0,0,21):C.UVGC_703_704,(0,0,22):C.UVGC_703_705,(0,0,23):C.UVGC_703_706,(0,0,24):C.UVGC_703_707,(0,0,25):C.UVGC_703_708,(0,0,26):C.UVGC_703_709,(0,0,0):C.UVGC_703_710})

V_697 = CTVertex(name = 'V_697',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,1):C.UVGC_703_684,(0,0,2):C.UVGC_703_685,(0,0,3):C.UVGC_703_686,(0,0,4):C.UVGC_703_687,(0,0,5):C.UVGC_703_688,(0,0,6):C.UVGC_703_689,(0,0,7):C.UVGC_703_690,(0,0,8):C.UVGC_703_691,(0,0,9):C.UVGC_703_692,(0,0,10):C.UVGC_703_693,(0,0,11):C.UVGC_703_694,(0,0,12):C.UVGC_703_695,(0,0,13):C.UVGC_703_696,(0,0,14):C.UVGC_703_697,(0,0,15):C.UVGC_703_698,(0,0,16):C.UVGC_703_699,(0,0,17):C.UVGC_703_700,(0,0,18):C.UVGC_703_701,(0,0,19):C.UVGC_703_702,(0,0,20):C.UVGC_703_703,(0,0,21):C.UVGC_703_704,(0,0,22):C.UVGC_703_705,(0,0,23):C.UVGC_703_706,(0,0,24):C.UVGC_703_707,(0,0,25):C.UVGC_703_708,(0,0,26):C.UVGC_703_709,(0,0,0):C.UVGC_703_710})

V_698 = CTVertex(name = 'V_698',
                 type = 'UV',
                 particles = [ P.W__plus__, P.Z, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_339_50,(0,0,2):C.UVGC_339_51,(0,0,1):C.UVGC_339_52})

V_699 = CTVertex(name = 'V_699',
                 type = 'UV',
                 particles = [ P.W__minus__, P.Z, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_339_50,(0,0,2):C.UVGC_339_51,(0,0,1):C.UVGC_339_52})

V_700 = CTVertex(name = 'V_700',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,1):C.UVGC_700_657,(0,0,2):C.UVGC_700_658,(0,0,3):C.UVGC_700_659,(0,0,4):C.UVGC_700_660,(0,0,5):C.UVGC_700_661,(0,0,6):C.UVGC_700_662,(0,0,7):C.UVGC_700_663,(0,0,8):C.UVGC_700_664,(0,0,9):C.UVGC_700_665,(0,0,10):C.UVGC_700_666,(0,0,11):C.UVGC_700_667,(0,0,12):C.UVGC_700_668,(0,0,13):C.UVGC_700_669,(0,0,14):C.UVGC_700_670,(0,0,15):C.UVGC_700_671,(0,0,16):C.UVGC_700_672,(0,0,17):C.UVGC_700_673,(0,0,18):C.UVGC_700_674,(0,0,19):C.UVGC_700_675,(0,0,20):C.UVGC_700_676,(0,0,21):C.UVGC_700_677,(0,0,22):C.UVGC_700_678,(0,0,23):C.UVGC_700_679,(0,0,24):C.UVGC_700_680,(0,0,25):C.UVGC_700_681,(0,0,26):C.UVGC_700_682,(0,0,0):C.UVGC_700_683})

V_701 = CTVertex(name = 'V_701',
                 type = 'UV',
                 particles = [ P.W__plus__, P.Z, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_339_50,(0,0,2):C.UVGC_339_51,(0,0,1):C.UVGC_339_52})

V_702 = CTVertex(name = 'V_702',
                 type = 'UV',
                 particles = [ P.W__minus__, P.Z, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_339_50,(0,0,2):C.UVGC_339_51,(0,0,1):C.UVGC_339_52})

V_703 = CTVertex(name = 'V_703',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,1):C.UVGC_700_657,(0,0,2):C.UVGC_700_658,(0,0,3):C.UVGC_700_659,(0,0,4):C.UVGC_700_660,(0,0,5):C.UVGC_700_661,(0,0,6):C.UVGC_700_662,(0,0,7):C.UVGC_700_663,(0,0,8):C.UVGC_700_664,(0,0,9):C.UVGC_700_665,(0,0,10):C.UVGC_700_666,(0,0,11):C.UVGC_700_667,(0,0,12):C.UVGC_700_668,(0,0,13):C.UVGC_700_669,(0,0,14):C.UVGC_700_670,(0,0,15):C.UVGC_700_671,(0,0,16):C.UVGC_700_672,(0,0,17):C.UVGC_700_673,(0,0,18):C.UVGC_700_674,(0,0,19):C.UVGC_700_675,(0,0,20):C.UVGC_700_676,(0,0,21):C.UVGC_700_677,(0,0,22):C.UVGC_700_678,(0,0,23):C.UVGC_700_679,(0,0,24):C.UVGC_700_680,(0,0,25):C.UVGC_700_681,(0,0,26):C.UVGC_700_682,(0,0,0):C.UVGC_700_683})

V_704 = CTVertex(name = 'V_704',
                 type = 'UV',
                 particles = [ P.W__plus__, P.Z, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_339_50,(0,0,2):C.UVGC_339_51,(0,0,1):C.UVGC_339_52})

V_705 = CTVertex(name = 'V_705',
                 type = 'UV',
                 particles = [ P.W__minus__, P.Z, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_339_50,(0,0,2):C.UVGC_339_51,(0,0,1):C.UVGC_339_52})

V_706 = CTVertex(name = 'V_706',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,1):C.UVGC_700_657,(0,0,2):C.UVGC_700_658,(0,0,3):C.UVGC_700_659,(0,0,4):C.UVGC_700_660,(0,0,5):C.UVGC_700_661,(0,0,6):C.UVGC_700_662,(0,0,7):C.UVGC_700_663,(0,0,8):C.UVGC_700_664,(0,0,9):C.UVGC_700_665,(0,0,10):C.UVGC_700_666,(0,0,11):C.UVGC_700_667,(0,0,12):C.UVGC_700_668,(0,0,13):C.UVGC_700_669,(0,0,14):C.UVGC_700_670,(0,0,15):C.UVGC_700_671,(0,0,16):C.UVGC_700_672,(0,0,17):C.UVGC_700_673,(0,0,18):C.UVGC_700_674,(0,0,19):C.UVGC_700_675,(0,0,20):C.UVGC_700_676,(0,0,21):C.UVGC_700_677,(0,0,22):C.UVGC_700_678,(0,0,23):C.UVGC_700_679,(0,0,24):C.UVGC_700_680,(0,0,25):C.UVGC_700_681,(0,0,26):C.UVGC_700_682,(0,0,0):C.UVGC_700_683})

V_707 = CTVertex(name = 'V_707',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,1):C.UVGC_709_738,(0,0,2):C.UVGC_709_739,(0,0,3):C.UVGC_709_740,(0,0,4):C.UVGC_709_741,(0,0,5):C.UVGC_709_742,(0,0,6):C.UVGC_709_743,(0,0,7):C.UVGC_709_744,(0,0,8):C.UVGC_709_745,(0,0,9):C.UVGC_709_746,(0,0,10):C.UVGC_709_747,(0,0,11):C.UVGC_709_748,(0,0,12):C.UVGC_709_749,(0,0,13):C.UVGC_709_750,(0,0,14):C.UVGC_709_751,(0,0,15):C.UVGC_709_752,(0,0,16):C.UVGC_709_753,(0,0,17):C.UVGC_709_754,(0,0,18):C.UVGC_709_755,(0,0,19):C.UVGC_709_756,(0,0,20):C.UVGC_709_757,(0,0,21):C.UVGC_709_758,(0,0,22):C.UVGC_709_759,(0,0,23):C.UVGC_709_760,(0,0,24):C.UVGC_709_761,(0,0,25):C.UVGC_709_762,(0,0,26):C.UVGC_709_763,(0,0,0):C.UVGC_709_764})

V_708 = CTVertex(name = 'V_708',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,1):C.UVGC_709_738,(0,0,2):C.UVGC_709_739,(0,0,3):C.UVGC_709_740,(0,0,4):C.UVGC_709_741,(0,0,5):C.UVGC_709_742,(0,0,6):C.UVGC_709_743,(0,0,7):C.UVGC_709_744,(0,0,8):C.UVGC_709_745,(0,0,9):C.UVGC_709_746,(0,0,10):C.UVGC_709_747,(0,0,11):C.UVGC_709_748,(0,0,12):C.UVGC_709_749,(0,0,13):C.UVGC_709_750,(0,0,14):C.UVGC_709_751,(0,0,15):C.UVGC_709_752,(0,0,16):C.UVGC_709_753,(0,0,17):C.UVGC_709_754,(0,0,18):C.UVGC_709_755,(0,0,19):C.UVGC_709_756,(0,0,20):C.UVGC_709_757,(0,0,21):C.UVGC_709_758,(0,0,22):C.UVGC_709_759,(0,0,23):C.UVGC_709_760,(0,0,24):C.UVGC_709_761,(0,0,25):C.UVGC_709_762,(0,0,26):C.UVGC_709_763,(0,0,0):C.UVGC_709_764})

V_709 = CTVertex(name = 'V_709',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,1):C.UVGC_709_738,(0,0,2):C.UVGC_709_739,(0,0,3):C.UVGC_709_740,(0,0,4):C.UVGC_709_741,(0,0,5):C.UVGC_709_742,(0,0,6):C.UVGC_709_743,(0,0,7):C.UVGC_709_744,(0,0,8):C.UVGC_709_745,(0,0,9):C.UVGC_709_746,(0,0,10):C.UVGC_709_747,(0,0,11):C.UVGC_709_748,(0,0,12):C.UVGC_709_749,(0,0,13):C.UVGC_709_750,(0,0,14):C.UVGC_709_751,(0,0,15):C.UVGC_709_752,(0,0,16):C.UVGC_709_753,(0,0,17):C.UVGC_709_754,(0,0,18):C.UVGC_709_755,(0,0,19):C.UVGC_709_756,(0,0,20):C.UVGC_709_757,(0,0,21):C.UVGC_709_758,(0,0,22):C.UVGC_709_759,(0,0,23):C.UVGC_709_760,(0,0,24):C.UVGC_709_761,(0,0,25):C.UVGC_709_762,(0,0,26):C.UVGC_709_763,(0,0,0):C.UVGC_709_764})

V_710 = CTVertex(name = 'V_710',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3Qu1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_553_208,(0,0,2):C.UVGC_571_232,(0,0,1):C.UVGC_553_210})

V_711 = CTVertex(name = 'V_711',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3Qd1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_553_208,(0,0,2):C.UVGC_553_209,(0,0,1):C.UVGC_553_210})

V_712 = CTVertex(name = 'V_712',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3Qu2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_559_216,(0,0,2):C.UVGC_578_239,(0,0,1):C.UVGC_559_218})

V_713 = CTVertex(name = 'V_713',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3Qd2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_559_216,(0,0,2):C.UVGC_559_217,(0,0,1):C.UVGC_559_218})

V_714 = CTVertex(name = 'V_714',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3Qu3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_585_246,(0,0,2):C.UVGC_585_247,(0,0,1):C.UVGC_565_226})

V_715 = CTVertex(name = 'V_715',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3Qd3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_565_224,(0,0,2):C.UVGC_565_225,(0,0,1):C.UVGC_565_226})

V_716 = CTVertex(name = 'V_716',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3Qu1, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_553_208,(0,0,2):C.UVGC_571_232,(0,0,1):C.UVGC_553_210})

V_717 = CTVertex(name = 'V_717',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3Qd1, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_553_208,(0,0,2):C.UVGC_553_209,(0,0,1):C.UVGC_553_210})

V_718 = CTVertex(name = 'V_718',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3Qu2, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_559_216,(0,0,2):C.UVGC_578_239,(0,0,1):C.UVGC_559_218})

V_719 = CTVertex(name = 'V_719',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3Qd2, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_559_216,(0,0,2):C.UVGC_559_217,(0,0,1):C.UVGC_559_218})

V_720 = CTVertex(name = 'V_720',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3Qu3, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_585_246,(0,0,2):C.UVGC_585_247,(0,0,1):C.UVGC_565_226})

V_721 = CTVertex(name = 'V_721',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3Qd3, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_565_224,(0,0,2):C.UVGC_565_225,(0,0,1):C.UVGC_565_226})

V_722 = CTVertex(name = 'V_722',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_274_29,(0,1,0):C.UVGC_254_6,(0,2,0):C.UVGC_254_6})

V_723 = CTVertex(name = 'V_723',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_274_29,(0,1,0):C.UVGC_254_6,(0,2,0):C.UVGC_254_6})

V_724 = CTVertex(name = 'V_724',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_274_29,(0,1,0):C.UVGC_522_166,(0,2,0):C.UVGC_522_166})

V_725 = CTVertex(name = 'V_725',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_272_27,(0,1,0):C.UVGC_252_5,(0,2,0):C.UVGC_252_5})

V_726 = CTVertex(name = 'V_726',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_272_27,(0,1,0):C.UVGC_252_5,(0,2,0):C.UVGC_252_5})

V_727 = CTVertex(name = 'V_727',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_272_27,(0,1,0):C.UVGC_252_5,(0,2,0):C.UVGC_252_5})

V_728 = CTVertex(name = 'V_728',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_273_28,(0,1,1):C.UVGC_622_330,(0,1,2):C.UVGC_622_331,(0,1,3):C.UVGC_622_332,(0,1,4):C.UVGC_622_333,(0,1,5):C.UVGC_622_334,(0,1,6):C.UVGC_622_335,(0,1,7):C.UVGC_622_336,(0,1,8):C.UVGC_622_337,(0,1,9):C.UVGC_622_338,(0,1,10):C.UVGC_622_339,(0,1,11):C.UVGC_622_340,(0,1,12):C.UVGC_622_341,(0,1,13):C.UVGC_622_342,(0,1,14):C.UVGC_622_343,(0,1,15):C.UVGC_622_344,(0,1,16):C.UVGC_622_345,(0,1,17):C.UVGC_622_346,(0,1,18):C.UVGC_622_347,(0,1,19):C.UVGC_622_348,(0,1,20):C.UVGC_622_349,(0,1,21):C.UVGC_622_350,(0,1,22):C.UVGC_622_351,(0,1,23):C.UVGC_622_352,(0,1,24):C.UVGC_622_353,(0,1,25):C.UVGC_622_354,(0,1,26):C.UVGC_622_355,(0,1,0):C.UVGC_622_356,(0,2,1):C.UVGC_622_330,(0,2,2):C.UVGC_622_331,(0,2,3):C.UVGC_622_332,(0,2,4):C.UVGC_622_333,(0,2,5):C.UVGC_622_334,(0,2,6):C.UVGC_622_335,(0,2,7):C.UVGC_622_336,(0,2,8):C.UVGC_622_337,(0,2,9):C.UVGC_622_338,(0,2,10):C.UVGC_622_339,(0,2,11):C.UVGC_622_340,(0,2,12):C.UVGC_622_341,(0,2,13):C.UVGC_622_342,(0,2,14):C.UVGC_622_343,(0,2,15):C.UVGC_622_344,(0,2,16):C.UVGC_622_345,(0,2,17):C.UVGC_622_346,(0,2,18):C.UVGC_622_347,(0,2,19):C.UVGC_622_348,(0,2,20):C.UVGC_622_349,(0,2,21):C.UVGC_622_350,(0,2,22):C.UVGC_622_351,(0,2,23):C.UVGC_622_352,(0,2,24):C.UVGC_622_353,(0,2,25):C.UVGC_622_354,(0,2,26):C.UVGC_622_355,(0,2,0):C.UVGC_622_356})

V_729 = CTVertex(name = 'V_729',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_273_28,(0,1,1):C.UVGC_622_330,(0,1,2):C.UVGC_622_331,(0,1,3):C.UVGC_622_332,(0,1,4):C.UVGC_622_333,(0,1,5):C.UVGC_622_334,(0,1,6):C.UVGC_622_335,(0,1,7):C.UVGC_622_336,(0,1,8):C.UVGC_622_337,(0,1,9):C.UVGC_622_338,(0,1,10):C.UVGC_622_339,(0,1,11):C.UVGC_622_340,(0,1,12):C.UVGC_622_341,(0,1,13):C.UVGC_622_342,(0,1,14):C.UVGC_622_343,(0,1,15):C.UVGC_622_344,(0,1,16):C.UVGC_622_345,(0,1,17):C.UVGC_622_346,(0,1,18):C.UVGC_622_347,(0,1,19):C.UVGC_622_348,(0,1,20):C.UVGC_622_349,(0,1,21):C.UVGC_622_350,(0,1,22):C.UVGC_622_351,(0,1,23):C.UVGC_622_352,(0,1,24):C.UVGC_622_353,(0,1,25):C.UVGC_622_354,(0,1,26):C.UVGC_622_355,(0,1,0):C.UVGC_622_356,(0,2,1):C.UVGC_622_330,(0,2,2):C.UVGC_622_331,(0,2,3):C.UVGC_622_332,(0,2,4):C.UVGC_622_333,(0,2,5):C.UVGC_622_334,(0,2,6):C.UVGC_622_335,(0,2,7):C.UVGC_622_336,(0,2,8):C.UVGC_622_337,(0,2,9):C.UVGC_622_338,(0,2,10):C.UVGC_622_339,(0,2,11):C.UVGC_622_340,(0,2,12):C.UVGC_622_341,(0,2,13):C.UVGC_622_342,(0,2,14):C.UVGC_622_343,(0,2,15):C.UVGC_622_344,(0,2,16):C.UVGC_622_345,(0,2,17):C.UVGC_622_346,(0,2,18):C.UVGC_622_347,(0,2,19):C.UVGC_622_348,(0,2,20):C.UVGC_622_349,(0,2,21):C.UVGC_622_350,(0,2,22):C.UVGC_622_351,(0,2,23):C.UVGC_622_352,(0,2,24):C.UVGC_622_353,(0,2,25):C.UVGC_622_354,(0,2,26):C.UVGC_622_355,(0,2,0):C.UVGC_622_356})

V_730 = CTVertex(name = 'V_730',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_273_28,(0,1,1):C.UVGC_622_330,(0,1,2):C.UVGC_622_331,(0,1,3):C.UVGC_622_332,(0,1,4):C.UVGC_622_333,(0,1,5):C.UVGC_622_334,(0,1,6):C.UVGC_622_335,(0,1,7):C.UVGC_622_336,(0,1,8):C.UVGC_622_337,(0,1,9):C.UVGC_622_338,(0,1,10):C.UVGC_622_339,(0,1,11):C.UVGC_622_340,(0,1,12):C.UVGC_622_341,(0,1,13):C.UVGC_622_342,(0,1,14):C.UVGC_622_343,(0,1,15):C.UVGC_622_344,(0,1,16):C.UVGC_622_345,(0,1,17):C.UVGC_622_346,(0,1,18):C.UVGC_622_347,(0,1,19):C.UVGC_622_348,(0,1,20):C.UVGC_622_349,(0,1,21):C.UVGC_622_350,(0,1,22):C.UVGC_622_351,(0,1,23):C.UVGC_622_352,(0,1,24):C.UVGC_622_353,(0,1,25):C.UVGC_622_354,(0,1,26):C.UVGC_622_355,(0,1,0):C.UVGC_639_358,(0,2,1):C.UVGC_622_330,(0,2,2):C.UVGC_622_331,(0,2,3):C.UVGC_622_332,(0,2,4):C.UVGC_622_333,(0,2,5):C.UVGC_622_334,(0,2,6):C.UVGC_622_335,(0,2,7):C.UVGC_622_336,(0,2,8):C.UVGC_622_337,(0,2,9):C.UVGC_622_338,(0,2,10):C.UVGC_622_339,(0,2,11):C.UVGC_622_340,(0,2,12):C.UVGC_622_341,(0,2,13):C.UVGC_622_342,(0,2,14):C.UVGC_622_343,(0,2,15):C.UVGC_622_344,(0,2,16):C.UVGC_622_345,(0,2,17):C.UVGC_622_346,(0,2,18):C.UVGC_622_347,(0,2,19):C.UVGC_622_348,(0,2,20):C.UVGC_622_349,(0,2,21):C.UVGC_622_350,(0,2,22):C.UVGC_622_351,(0,2,23):C.UVGC_622_352,(0,2,24):C.UVGC_622_353,(0,2,25):C.UVGC_622_354,(0,2,26):C.UVGC_622_355,(0,2,0):C.UVGC_639_358})

V_731 = CTVertex(name = 'V_731',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_273_28,(0,1,1):C.UVGC_622_330,(0,1,2):C.UVGC_622_331,(0,1,3):C.UVGC_622_332,(0,1,4):C.UVGC_622_333,(0,1,5):C.UVGC_622_334,(0,1,6):C.UVGC_622_335,(0,1,7):C.UVGC_622_336,(0,1,8):C.UVGC_622_337,(0,1,9):C.UVGC_622_338,(0,1,10):C.UVGC_622_339,(0,1,11):C.UVGC_622_340,(0,1,12):C.UVGC_622_341,(0,1,13):C.UVGC_622_342,(0,1,14):C.UVGC_622_343,(0,1,15):C.UVGC_622_344,(0,1,16):C.UVGC_622_345,(0,1,17):C.UVGC_622_346,(0,1,18):C.UVGC_622_347,(0,1,19):C.UVGC_622_348,(0,1,20):C.UVGC_622_349,(0,1,21):C.UVGC_622_350,(0,1,22):C.UVGC_622_351,(0,1,23):C.UVGC_622_352,(0,1,24):C.UVGC_622_353,(0,1,25):C.UVGC_622_354,(0,1,26):C.UVGC_622_355,(0,1,0):C.UVGC_622_356,(0,2,1):C.UVGC_622_330,(0,2,2):C.UVGC_622_331,(0,2,3):C.UVGC_622_332,(0,2,4):C.UVGC_622_333,(0,2,5):C.UVGC_622_334,(0,2,6):C.UVGC_622_335,(0,2,7):C.UVGC_622_336,(0,2,8):C.UVGC_622_337,(0,2,9):C.UVGC_622_338,(0,2,10):C.UVGC_622_339,(0,2,11):C.UVGC_622_340,(0,2,12):C.UVGC_622_341,(0,2,13):C.UVGC_622_342,(0,2,14):C.UVGC_622_343,(0,2,15):C.UVGC_622_344,(0,2,16):C.UVGC_622_345,(0,2,17):C.UVGC_622_346,(0,2,18):C.UVGC_622_347,(0,2,19):C.UVGC_622_348,(0,2,20):C.UVGC_622_349,(0,2,21):C.UVGC_622_350,(0,2,22):C.UVGC_622_351,(0,2,23):C.UVGC_622_352,(0,2,24):C.UVGC_622_353,(0,2,25):C.UVGC_622_354,(0,2,26):C.UVGC_622_355,(0,2,0):C.UVGC_622_356})

V_732 = CTVertex(name = 'V_732',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_273_28,(0,1,1):C.UVGC_622_330,(0,1,2):C.UVGC_622_331,(0,1,3):C.UVGC_622_332,(0,1,4):C.UVGC_622_333,(0,1,5):C.UVGC_622_334,(0,1,6):C.UVGC_622_335,(0,1,7):C.UVGC_622_336,(0,1,8):C.UVGC_622_337,(0,1,9):C.UVGC_622_338,(0,1,10):C.UVGC_622_339,(0,1,11):C.UVGC_622_340,(0,1,12):C.UVGC_622_341,(0,1,13):C.UVGC_622_342,(0,1,14):C.UVGC_622_343,(0,1,15):C.UVGC_622_344,(0,1,16):C.UVGC_622_345,(0,1,17):C.UVGC_622_346,(0,1,18):C.UVGC_622_347,(0,1,19):C.UVGC_622_348,(0,1,20):C.UVGC_622_349,(0,1,21):C.UVGC_622_350,(0,1,22):C.UVGC_622_351,(0,1,23):C.UVGC_622_352,(0,1,24):C.UVGC_622_353,(0,1,25):C.UVGC_622_354,(0,1,26):C.UVGC_622_355,(0,1,0):C.UVGC_622_356,(0,2,1):C.UVGC_622_330,(0,2,2):C.UVGC_622_331,(0,2,3):C.UVGC_622_332,(0,2,4):C.UVGC_622_333,(0,2,5):C.UVGC_622_334,(0,2,6):C.UVGC_622_335,(0,2,7):C.UVGC_622_336,(0,2,8):C.UVGC_622_337,(0,2,9):C.UVGC_622_338,(0,2,10):C.UVGC_622_339,(0,2,11):C.UVGC_622_340,(0,2,12):C.UVGC_622_341,(0,2,13):C.UVGC_622_342,(0,2,14):C.UVGC_622_343,(0,2,15):C.UVGC_622_344,(0,2,16):C.UVGC_622_345,(0,2,17):C.UVGC_622_346,(0,2,18):C.UVGC_622_347,(0,2,19):C.UVGC_622_348,(0,2,20):C.UVGC_622_349,(0,2,21):C.UVGC_622_350,(0,2,22):C.UVGC_622_351,(0,2,23):C.UVGC_622_352,(0,2,24):C.UVGC_622_353,(0,2,25):C.UVGC_622_354,(0,2,26):C.UVGC_622_355,(0,2,0):C.UVGC_622_356})

V_733 = CTVertex(name = 'V_733',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_273_28,(0,1,1):C.UVGC_622_330,(0,1,2):C.UVGC_622_331,(0,1,3):C.UVGC_622_332,(0,1,4):C.UVGC_622_333,(0,1,5):C.UVGC_622_334,(0,1,6):C.UVGC_622_335,(0,1,7):C.UVGC_622_336,(0,1,8):C.UVGC_622_337,(0,1,9):C.UVGC_622_338,(0,1,10):C.UVGC_622_339,(0,1,11):C.UVGC_622_340,(0,1,12):C.UVGC_622_341,(0,1,13):C.UVGC_622_342,(0,1,14):C.UVGC_622_343,(0,1,15):C.UVGC_622_344,(0,1,16):C.UVGC_622_345,(0,1,17):C.UVGC_622_346,(0,1,18):C.UVGC_622_347,(0,1,19):C.UVGC_622_348,(0,1,20):C.UVGC_622_349,(0,1,21):C.UVGC_622_350,(0,1,22):C.UVGC_622_351,(0,1,23):C.UVGC_622_352,(0,1,24):C.UVGC_622_353,(0,1,25):C.UVGC_622_354,(0,1,26):C.UVGC_622_355,(0,1,0):C.UVGC_622_356,(0,2,1):C.UVGC_622_330,(0,2,2):C.UVGC_622_331,(0,2,3):C.UVGC_622_332,(0,2,4):C.UVGC_622_333,(0,2,5):C.UVGC_622_334,(0,2,6):C.UVGC_622_335,(0,2,7):C.UVGC_622_336,(0,2,8):C.UVGC_622_337,(0,2,9):C.UVGC_622_338,(0,2,10):C.UVGC_622_339,(0,2,11):C.UVGC_622_340,(0,2,12):C.UVGC_622_341,(0,2,13):C.UVGC_622_342,(0,2,14):C.UVGC_622_343,(0,2,15):C.UVGC_622_344,(0,2,16):C.UVGC_622_345,(0,2,17):C.UVGC_622_346,(0,2,18):C.UVGC_622_347,(0,2,19):C.UVGC_622_348,(0,2,20):C.UVGC_622_349,(0,2,21):C.UVGC_622_350,(0,2,22):C.UVGC_622_351,(0,2,23):C.UVGC_622_352,(0,2,24):C.UVGC_622_353,(0,2,25):C.UVGC_622_354,(0,2,26):C.UVGC_622_355,(0,2,0):C.UVGC_622_356})

V_734 = CTVertex(name = 'V_734',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_336_44,(0,0,1):C.UVGC_336_45})

V_735 = CTVertex(name = 'V_735',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_336_44,(0,0,1):C.UVGC_336_45})

V_736 = CTVertex(name = 'V_736',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_336_44,(0,0,2):C.UVGC_526_171,(0,0,1):C.UVGC_336_45})

V_737 = CTVertex(name = 'V_737',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_336_44,(0,0,1):C.UVGC_336_45})

V_738 = CTVertex(name = 'V_738',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_336_44,(0,0,1):C.UVGC_336_45})

V_739 = CTVertex(name = 'V_739',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_336_44,(0,0,2):C.UVGC_526_171,(0,0,1):C.UVGC_336_45})

V_740 = CTVertex(name = 'V_740',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_527_172,(0,1,0):C.UVGC_528_173})

V_741 = CTVertex(name = 'V_741',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.u, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_553_208,(0,0,2):C.UVGC_571_232,(0,0,1):C.UVGC_553_210})

V_742 = CTVertex(name = 'V_742',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.d, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_553_208,(0,0,2):C.UVGC_553_209,(0,0,1):C.UVGC_553_210})

V_743 = CTVertex(name = 'V_743',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.c, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_559_216,(0,0,2):C.UVGC_578_239,(0,0,1):C.UVGC_559_218})

V_744 = CTVertex(name = 'V_744',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.s, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_559_216,(0,0,2):C.UVGC_559_217,(0,0,1):C.UVGC_559_218})

V_745 = CTVertex(name = 'V_745',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.t, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_585_246,(0,0,2):C.UVGC_585_247,(0,0,1):C.UVGC_565_226})

V_746 = CTVertex(name = 'V_746',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.b, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_565_224,(0,0,2):C.UVGC_565_225,(0,0,1):C.UVGC_565_226})

V_747 = CTVertex(name = 'V_747',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.u, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_553_208,(0,0,2):C.UVGC_571_232,(0,0,1):C.UVGC_553_210})

V_748 = CTVertex(name = 'V_748',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.d, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_553_208,(0,0,2):C.UVGC_553_209,(0,0,1):C.UVGC_553_210})

V_749 = CTVertex(name = 'V_749',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.c, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_559_216,(0,0,2):C.UVGC_578_239,(0,0,1):C.UVGC_559_218})

V_750 = CTVertex(name = 'V_750',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.s, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_559_216,(0,0,2):C.UVGC_559_217,(0,0,1):C.UVGC_559_218})

V_751 = CTVertex(name = 'V_751',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.t, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_585_246,(0,0,2):C.UVGC_585_247,(0,0,1):C.UVGC_565_226})

V_752 = CTVertex(name = 'V_752',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.b, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_565_224,(0,0,2):C.UVGC_565_225,(0,0,1):C.UVGC_565_226})

V_753 = CTVertex(name = 'V_753',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3d1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_535_184,(0,0,2):C.UVGC_535_185,(0,0,1):C.UVGC_535_186})

V_754 = CTVertex(name = 'V_754',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3d2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_541_192,(0,0,2):C.UVGC_541_193,(0,0,1):C.UVGC_541_194})

V_755 = CTVertex(name = 'V_755',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3d3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_547_200,(0,0,2):C.UVGC_547_201,(0,0,1):C.UVGC_547_202})

V_756 = CTVertex(name = 'V_756',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3u1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_592_254,(0,0,2):C.UVGC_592_255,(0,0,1):C.UVGC_592_256})

V_757 = CTVertex(name = 'V_757',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3u2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_598_262,(0,0,2):C.UVGC_598_263,(0,0,1):C.UVGC_598_264})

V_758 = CTVertex(name = 'V_758',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3u3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_604_270,(0,0,2):C.UVGC_604_271,(0,0,1):C.UVGC_604_272})

V_759 = CTVertex(name = 'V_759',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3d1, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_535_184,(0,0,2):C.UVGC_535_185,(0,0,1):C.UVGC_535_186})

V_760 = CTVertex(name = 'V_760',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3d2, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_541_192,(0,0,2):C.UVGC_541_193,(0,0,1):C.UVGC_541_194})

V_761 = CTVertex(name = 'V_761',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3d3, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_547_200,(0,0,2):C.UVGC_547_201,(0,0,1):C.UVGC_547_202})

V_762 = CTVertex(name = 'V_762',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3u1, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_592_254,(0,0,2):C.UVGC_592_255,(0,0,1):C.UVGC_592_256})

V_763 = CTVertex(name = 'V_763',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3u2, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_598_262,(0,0,2):C.UVGC_598_263,(0,0,1):C.UVGC_598_264})

V_764 = CTVertex(name = 'V_764',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3u3, P.Xw__tilde__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_604_270,(0,0,2):C.UVGC_604_271,(0,0,1):C.UVGC_604_272})

V_765 = CTVertex(name = 'V_765',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.d, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_535_184,(0,0,2):C.UVGC_535_185,(0,0,1):C.UVGC_535_186})

V_766 = CTVertex(name = 'V_766',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.s, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_541_192,(0,0,2):C.UVGC_541_193,(0,0,1):C.UVGC_541_194})

V_767 = CTVertex(name = 'V_767',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.b, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_547_200,(0,0,2):C.UVGC_547_201,(0,0,1):C.UVGC_547_202})

V_768 = CTVertex(name = 'V_768',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.u, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_592_254,(0,0,2):C.UVGC_592_255,(0,0,1):C.UVGC_592_256})

V_769 = CTVertex(name = 'V_769',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.c, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_598_262,(0,0,2):C.UVGC_598_263,(0,0,1):C.UVGC_598_264})

V_770 = CTVertex(name = 'V_770',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.t, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_604_270,(0,0,2):C.UVGC_604_271,(0,0,1):C.UVGC_604_272})

V_771 = CTVertex(name = 'V_771',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.d, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_535_184,(0,0,2):C.UVGC_535_185,(0,0,1):C.UVGC_535_186})

V_772 = CTVertex(name = 'V_772',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.s, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_541_192,(0,0,2):C.UVGC_541_193,(0,0,1):C.UVGC_541_194})

V_773 = CTVertex(name = 'V_773',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.b, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_547_200,(0,0,2):C.UVGC_547_201,(0,0,1):C.UVGC_547_202})

V_774 = CTVertex(name = 'V_774',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.u, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_592_254,(0,0,2):C.UVGC_592_255,(0,0,1):C.UVGC_592_256})

V_775 = CTVertex(name = 'V_775',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.c, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_598_262,(0,0,2):C.UVGC_598_263,(0,0,1):C.UVGC_598_264})

V_776 = CTVertex(name = 'V_776',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.t, P.Xw ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_604_270,(0,0,2):C.UVGC_604_271,(0,0,1):C.UVGC_604_272})

V_777 = CTVertex(name = 'V_777',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF4 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_251_4})

V_778 = CTVertex(name = 'V_778',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF4 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_251_4})

V_779 = CTVertex(name = 'V_779',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_525_170,(0,1,0):C.UVGC_521_165})

V_780 = CTVertex(name = 'V_780',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF4 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_251_4})

V_781 = CTVertex(name = 'V_781',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF4 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_251_4})

V_782 = CTVertex(name = 'V_782',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF4 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_251_4})

V_783 = CTVertex(name = 'V_783',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.YF3Qu1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_573_233,(0,1,0):C.UVGC_569_230})

V_784 = CTVertex(name = 'V_784',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.YF3Qu2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_580_240,(0,1,0):C.UVGC_576_237})

V_785 = CTVertex(name = 'V_785',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.YF3Qu3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_587_248,(0,1,0):C.UVGC_583_244})

V_786 = CTVertex(name = 'V_786',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.YF3Qd1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_555_212,(0,1,0):C.UVGC_551_206})

V_787 = CTVertex(name = 'V_787',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.YF3Qd2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_561_220,(0,1,0):C.UVGC_557_214})

V_788 = CTVertex(name = 'V_788',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.YF3Qd3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_567_228,(0,1,0):C.UVGC_563_222})

V_789 = CTVertex(name = 'V_789',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.YF3u1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_594_258,(0,1,0):C.UVGC_590_252})

V_790 = CTVertex(name = 'V_790',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.YF3u2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_600_266,(0,1,0):C.UVGC_596_260})

V_791 = CTVertex(name = 'V_791',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.YF3u3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_606_274,(0,1,0):C.UVGC_602_268})

V_792 = CTVertex(name = 'V_792',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.YF3d1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_537_188,(0,1,0):C.UVGC_533_182})

V_793 = CTVertex(name = 'V_793',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.YF3d2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_543_196,(0,1,0):C.UVGC_539_190})

V_794 = CTVertex(name = 'V_794',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.YF3d3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_549_204,(0,1,0):C.UVGC_545_198})

V_795 = CTVertex(name = 'V_795',
                 type = 'UV',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_614_282})

V_796 = CTVertex(name = 'V_796',
                 type = 'UV',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_615_283})

V_797 = CTVertex(name = 'V_797',
                 type = 'UV',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_616_284})

V_798 = CTVertex(name = 'V_798',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_611_279})

V_799 = CTVertex(name = 'V_799',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_612_280})

V_800 = CTVertex(name = 'V_800',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_613_281})

V_801 = CTVertex(name = 'V_801',
                 type = 'UV',
                 particles = [ P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_617_285})

V_802 = CTVertex(name = 'V_802',
                 type = 'UV',
                 particles = [ P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_618_286})

V_803 = CTVertex(name = 'V_803',
                 type = 'UV',
                 particles = [ P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_712_765})

V_804 = CTVertex(name = 'V_804',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_608_276})

V_805 = CTVertex(name = 'V_805',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_609_277})

V_806 = CTVertex(name = 'V_806',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_610_278})

V_807 = CTVertex(name = 'V_807',
                 type = 'UV',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV4, L.VV5, L.VV6 ],
                 loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u], [P.YF3d1], [P.YF3d2], [P.YF3d3], [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3], [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3], [P.YF3u1], [P.YF3u2], [P.YF3u3] ], [ [P.g] ], [ [P.ghG] ], [ PRIVATE`PythonFormatLoopParticles[1] ], [ [P.YS3d1], [P.YS3d2], [P.YS3d3], [P.YS3Qd1], [P.YS3Qd2], [P.YS3Qd3], [P.YS3Qu1], [P.YS3Qu2], [P.YS3Qu3], [P.YS3u1], [P.YS3u2], [P.YS3u3] ] ],
                 couplings = {(0,0,3):C.UVGC_268_18,(0,0,0):C.UVGC_268_19,(0,0,4):C.UVGC_268_20,(0,1,1):C.UVGC_248_1,(0,2,2):C.UVGC_250_3})

V_808 = CTVertex(name = 'V_808',
                 type = 'UV',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3Qu1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_371_66,(1,0,0):C.UVGC_377_74,(1,0,3):C.UVGC_371_68,(1,0,5):C.UVGC_377_75,(1,0,1):C.UVGC_377_76,(1,0,4):C.UVGC_377_77,(0,0,2):C.UVGC_371_66,(0,0,0):C.UVGC_377_74,(0,0,3):C.UVGC_371_68,(0,0,5):C.UVGC_377_75,(0,0,1):C.UVGC_377_76,(0,0,4):C.UVGC_377_77})

V_809 = CTVertex(name = 'V_809',
                 type = 'UV',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qu1, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu1, P.YS3Qu2] ], [ [P.g, P.YS3Qu1, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_450_146,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_450_147,(1,0,1):C.UVGC_450_148,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_450_149,(1,0,2):C.UVGC_390_96,(1,0,6):C.UVGC_450_150,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_449_141,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_449_142,(0,0,1):C.UVGC_449_143,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_449_144,(0,0,2):C.UVGC_389_87,(0,0,6):C.UVGC_449_145})

V_810 = CTVertex(name = 'V_810',
                 type = 'UV',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3Qu2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_371_66,(1,0,0):C.UVGC_377_74,(1,0,3):C.UVGC_371_68,(1,0,5):C.UVGC_377_75,(1,0,1):C.UVGC_377_76,(1,0,4):C.UVGC_377_77,(0,0,2):C.UVGC_371_66,(0,0,0):C.UVGC_377_74,(0,0,3):C.UVGC_371_68,(0,0,5):C.UVGC_377_75,(0,0,1):C.UVGC_377_76,(0,0,4):C.UVGC_377_77})

V_811 = CTVertex(name = 'V_811',
                 type = 'UV',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qu1, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qu1, P.YS3Qu3] ], [ [P.g, P.YS3Qu1, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_450_146,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_450_147,(1,0,1):C.UVGC_450_148,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_450_149,(1,0,2):C.UVGC_390_96,(1,0,6):C.UVGC_450_150,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_449_141,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_449_142,(0,0,1):C.UVGC_449_143,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_449_144,(0,0,2):C.UVGC_389_87,(0,0,6):C.UVGC_449_145})

V_812 = CTVertex(name = 'V_812',
                 type = 'UV',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qu2, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qu2, P.YS3Qu3] ], [ [P.g, P.YS3Qu2, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_450_146,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_450_147,(1,0,1):C.UVGC_450_148,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_450_149,(1,0,2):C.UVGC_390_96,(1,0,6):C.UVGC_450_150,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_449_141,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_449_142,(0,0,1):C.UVGC_449_143,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_449_144,(0,0,2):C.UVGC_389_87,(0,0,6):C.UVGC_449_145})

V_813 = CTVertex(name = 'V_813',
                 type = 'UV',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3Qu3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_371_66,(1,0,0):C.UVGC_377_74,(1,0,3):C.UVGC_371_68,(1,0,5):C.UVGC_377_75,(1,0,1):C.UVGC_377_76,(1,0,4):C.UVGC_377_77,(0,0,2):C.UVGC_371_66,(0,0,0):C.UVGC_377_74,(0,0,3):C.UVGC_371_68,(0,0,5):C.UVGC_377_75,(0,0,1):C.UVGC_377_76,(0,0,4):C.UVGC_377_77})

V_814 = CTVertex(name = 'V_814',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qu1] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_406_120,(1,0,4):C.UVGC_383_80,(1,0,7):C.UVGC_390_97,(1,0,11):C.UVGC_444_137,(1,0,1):C.UVGC_406_122,(1,0,5):C.UVGC_384_85,(1,0,8):C.UVGC_390_100,(1,0,10):C.UVGC_444_138,(1,0,2):C.UVGC_406_124,(1,0,6):C.UVGC_444_139,(1,0,9):C.UVGC_444_140,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_371_67,(0,0,4):C.UVGC_384_83,(0,0,7):C.UVGC_389_88,(0,0,11):C.UVGC_443_132,(0,0,1):C.UVGC_371_70,(0,0,5):C.UVGC_443_133,(0,0,8):C.UVGC_389_91,(0,0,10):C.UVGC_443_134,(0,0,2):C.UVGC_405_118,(0,0,6):C.UVGC_443_135,(0,0,9):C.UVGC_443_136})

V_815 = CTVertex(name = 'V_815',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd1, P.YS3Qu2] ], [ [P.g, P.YS3Qd1, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_406_120,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_444_137,(1,0,1):C.UVGC_406_122,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_444_138,(1,0,2):C.UVGC_406_124,(1,0,6):C.UVGC_444_140,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_371_67,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_443_132,(0,0,1):C.UVGC_371_70,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_443_134,(0,0,2):C.UVGC_405_118,(0,0,6):C.UVGC_443_136})

V_816 = CTVertex(name = 'V_816',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd1, P.YS3Qu3] ], [ [P.g, P.YS3Qd1, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_406_120,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_444_137,(1,0,1):C.UVGC_406_122,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_444_138,(1,0,2):C.UVGC_406_124,(1,0,6):C.UVGC_444_140,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_371_67,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_443_132,(0,0,1):C.UVGC_371_70,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_443_134,(0,0,2):C.UVGC_405_118,(0,0,6):C.UVGC_443_136})

V_817 = CTVertex(name = 'V_817',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qd1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_371_66,(1,0,0):C.UVGC_371_67,(1,0,3):C.UVGC_371_68,(1,0,5):C.UVGC_374_72,(1,0,1):C.UVGC_371_70,(1,0,4):C.UVGC_374_73,(0,0,2):C.UVGC_371_66,(0,0,0):C.UVGC_371_67,(0,0,3):C.UVGC_371_68,(0,0,5):C.UVGC_374_72,(0,0,1):C.UVGC_371_70,(0,0,4):C.UVGC_374_73})

V_818 = CTVertex(name = 'V_818',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd2, P.YS3Qu1, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu2] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu2] ] ],
                 couplings = {(1,0,0):C.UVGC_383_80,(1,0,1):C.UVGC_383_81,(1,0,2):C.UVGC_383_82,(0,0,0):C.UVGC_384_83,(0,0,1):C.UVGC_384_84,(0,0,2):C.UVGC_384_85})

V_819 = CTVertex(name = 'V_819',
                 type = 'UV',
                 particles = [ P.YS3Qd1, P.YS3Qd2__tilde__, P.YS3Qu1__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu2] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu2] ] ],
                 couplings = {(1,0,0):C.UVGC_383_80,(1,0,1):C.UVGC_383_81,(1,0,2):C.UVGC_383_82,(0,0,0):C.UVGC_384_83,(0,0,1):C.UVGC_384_84,(0,0,2):C.UVGC_384_85})

V_820 = CTVertex(name = 'V_820',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd2, P.YS3Qu1] ], [ [P.g, P.YS3Qd2, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_406_120,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_444_137,(1,0,1):C.UVGC_406_122,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_444_138,(1,0,2):C.UVGC_406_124,(1,0,6):C.UVGC_444_140,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_371_67,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_443_132,(0,0,1):C.UVGC_371_70,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_443_134,(0,0,2):C.UVGC_405_118,(0,0,6):C.UVGC_443_136})

V_821 = CTVertex(name = 'V_821',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qu2] ], [ [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_406_120,(1,0,4):C.UVGC_383_80,(1,0,7):C.UVGC_390_97,(1,0,11):C.UVGC_444_137,(1,0,1):C.UVGC_406_122,(1,0,5):C.UVGC_384_85,(1,0,8):C.UVGC_390_100,(1,0,10):C.UVGC_444_138,(1,0,2):C.UVGC_406_124,(1,0,6):C.UVGC_444_139,(1,0,9):C.UVGC_444_140,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_371_67,(0,0,4):C.UVGC_384_83,(0,0,7):C.UVGC_389_88,(0,0,11):C.UVGC_443_132,(0,0,1):C.UVGC_371_70,(0,0,5):C.UVGC_443_133,(0,0,8):C.UVGC_389_91,(0,0,10):C.UVGC_443_134,(0,0,2):C.UVGC_405_118,(0,0,6):C.UVGC_443_135,(0,0,9):C.UVGC_443_136})

V_822 = CTVertex(name = 'V_822',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd2, P.YS3Qu3] ], [ [P.g, P.YS3Qd2, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_406_120,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_444_137,(1,0,1):C.UVGC_406_122,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_444_138,(1,0,2):C.UVGC_406_124,(1,0,6):C.UVGC_444_140,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_371_67,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_443_132,(0,0,1):C.UVGC_371_70,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_443_134,(0,0,2):C.UVGC_405_118,(0,0,6):C.UVGC_443_136})

V_823 = CTVertex(name = 'V_823',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd1, P.YS3Qd2] ], [ [P.g, P.YS3Qd1, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_390_96,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_402_113,(1,0,1):C.UVGC_390_99,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_402_114,(1,0,2):C.UVGC_390_102,(1,0,6):C.UVGC_402_115,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_389_87,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_401_110,(0,0,1):C.UVGC_389_90,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_401_111,(0,0,2):C.UVGC_389_93,(0,0,6):C.UVGC_401_112})

V_824 = CTVertex(name = 'V_824',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qd2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_371_66,(1,0,0):C.UVGC_371_67,(1,0,3):C.UVGC_371_68,(1,0,5):C.UVGC_374_72,(1,0,1):C.UVGC_371_70,(1,0,4):C.UVGC_374_73,(0,0,2):C.UVGC_371_66,(0,0,0):C.UVGC_371_67,(0,0,3):C.UVGC_371_68,(0,0,5):C.UVGC_374_72,(0,0,1):C.UVGC_371_70,(0,0,4):C.UVGC_374_73})

V_825 = CTVertex(name = 'V_825',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd3, P.YS3Qu1, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.UVGC_383_80,(1,0,1):C.UVGC_383_81,(1,0,2):C.UVGC_383_82,(0,0,0):C.UVGC_384_83,(0,0,1):C.UVGC_384_84,(0,0,2):C.UVGC_384_85})

V_826 = CTVertex(name = 'V_826',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd3, P.YS3Qu2, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu2, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.UVGC_383_80,(1,0,1):C.UVGC_383_81,(1,0,2):C.UVGC_383_82,(0,0,0):C.UVGC_384_83,(0,0,1):C.UVGC_384_84,(0,0,2):C.UVGC_384_85})

V_827 = CTVertex(name = 'V_827',
                 type = 'UV',
                 particles = [ P.YS3Qd1, P.YS3Qd3__tilde__, P.YS3Qu1__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.UVGC_383_80,(1,0,1):C.UVGC_383_81,(1,0,2):C.UVGC_383_82,(0,0,0):C.UVGC_384_83,(0,0,1):C.UVGC_384_84,(0,0,2):C.UVGC_384_85})

V_828 = CTVertex(name = 'V_828',
                 type = 'UV',
                 particles = [ P.YS3Qd2, P.YS3Qd3__tilde__, P.YS3Qu2__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu2, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.UVGC_383_80,(1,0,1):C.UVGC_383_81,(1,0,2):C.UVGC_383_82,(0,0,0):C.UVGC_384_83,(0,0,1):C.UVGC_384_84,(0,0,2):C.UVGC_384_85})

V_829 = CTVertex(name = 'V_829',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3Qd3, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd3, P.YS3Qu1] ], [ [P.g, P.YS3Qd3, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_406_120,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_444_137,(1,0,1):C.UVGC_406_122,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_444_138,(1,0,2):C.UVGC_406_124,(1,0,6):C.UVGC_444_140,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_371_67,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_443_132,(0,0,1):C.UVGC_371_70,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_443_134,(0,0,2):C.UVGC_405_118,(0,0,6):C.UVGC_443_136})

V_830 = CTVertex(name = 'V_830',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qd3, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd3, P.YS3Qu2] ], [ [P.g, P.YS3Qd3, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_406_120,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_444_137,(1,0,1):C.UVGC_406_122,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_444_138,(1,0,2):C.UVGC_406_124,(1,0,6):C.UVGC_444_140,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_371_67,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_443_132,(0,0,1):C.UVGC_371_70,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_443_134,(0,0,2):C.UVGC_405_118,(0,0,6):C.UVGC_443_136})

V_831 = CTVertex(name = 'V_831',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_406_120,(1,0,4):C.UVGC_383_80,(1,0,7):C.UVGC_390_97,(1,0,11):C.UVGC_444_137,(1,0,1):C.UVGC_406_122,(1,0,5):C.UVGC_384_85,(1,0,8):C.UVGC_390_100,(1,0,10):C.UVGC_444_138,(1,0,2):C.UVGC_406_124,(1,0,6):C.UVGC_444_139,(1,0,9):C.UVGC_444_140,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_371_67,(0,0,4):C.UVGC_384_83,(0,0,7):C.UVGC_389_88,(0,0,11):C.UVGC_443_132,(0,0,1):C.UVGC_371_70,(0,0,5):C.UVGC_443_133,(0,0,8):C.UVGC_389_91,(0,0,10):C.UVGC_443_134,(0,0,2):C.UVGC_405_118,(0,0,6):C.UVGC_443_135,(0,0,9):C.UVGC_443_136})

V_832 = CTVertex(name = 'V_832',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd1, P.YS3Qd3] ], [ [P.g, P.YS3Qd1, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_390_96,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_402_113,(1,0,1):C.UVGC_390_99,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_402_114,(1,0,2):C.UVGC_390_102,(1,0,6):C.UVGC_402_115,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_389_87,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_401_110,(0,0,1):C.UVGC_389_90,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_401_111,(0,0,2):C.UVGC_389_93,(0,0,6):C.UVGC_401_112})

V_833 = CTVertex(name = 'V_833',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd2, P.YS3Qd3] ], [ [P.g, P.YS3Qd2, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_390_96,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_402_113,(1,0,1):C.UVGC_390_99,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_402_114,(1,0,2):C.UVGC_390_102,(1,0,6):C.UVGC_402_115,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_389_87,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_401_110,(0,0,1):C.UVGC_389_90,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_401_111,(0,0,2):C.UVGC_389_93,(0,0,6):C.UVGC_401_112})

V_834 = CTVertex(name = 'V_834',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qd3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_371_66,(1,0,0):C.UVGC_371_67,(1,0,3):C.UVGC_371_68,(1,0,5):C.UVGC_374_72,(1,0,1):C.UVGC_371_70,(1,0,4):C.UVGC_374_73,(0,0,2):C.UVGC_371_66,(0,0,0):C.UVGC_371_67,(0,0,3):C.UVGC_371_68,(0,0,5):C.UVGC_374_72,(0,0,1):C.UVGC_371_70,(0,0,4):C.UVGC_374_73})

V_835 = CTVertex(name = 'V_835',
                 type = 'UV',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qu1, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qu1, P.YS3u1] ], [ [P.g, P.YS3Qu1, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_450_146,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_454_154,(1,0,1):C.UVGC_450_148,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_454_155,(1,0,2):C.UVGC_390_96,(1,0,6):C.UVGC_454_156,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_449_141,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_453_151,(0,0,1):C.UVGC_449_143,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_453_152,(0,0,2):C.UVGC_389_87,(0,0,6):C.UVGC_453_153})

V_836 = CTVertex(name = 'V_836',
                 type = 'UV',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qu2, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qu2, P.YS3u1] ], [ [P.g, P.YS3Qu2, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_450_146,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_454_154,(1,0,1):C.UVGC_450_148,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_454_155,(1,0,2):C.UVGC_390_96,(1,0,6):C.UVGC_454_156,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_449_141,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_453_151,(0,0,1):C.UVGC_449_143,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_453_152,(0,0,2):C.UVGC_389_87,(0,0,6):C.UVGC_453_153})

V_837 = CTVertex(name = 'V_837',
                 type = 'UV',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qu3, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qu3], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qu3, P.YS3u1] ], [ [P.g, P.YS3Qu3, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qu3, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_450_146,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_454_154,(1,0,1):C.UVGC_450_148,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_454_155,(1,0,2):C.UVGC_390_96,(1,0,6):C.UVGC_454_156,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_449_141,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_453_151,(0,0,1):C.UVGC_449_143,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_453_152,(0,0,2):C.UVGC_389_87,(0,0,6):C.UVGC_453_153})

V_838 = CTVertex(name = 'V_838',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qd1, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qd1, P.YS3u1] ], [ [P.g, P.YS3Qd1, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_406_120,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_406_121,(1,0,1):C.UVGC_406_122,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_406_123,(1,0,2):C.UVGC_406_124,(1,0,6):C.UVGC_406_125,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_371_67,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_405_116,(0,0,1):C.UVGC_371_70,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_405_117,(0,0,2):C.UVGC_405_118,(0,0,6):C.UVGC_405_119})

V_839 = CTVertex(name = 'V_839',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qd2, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qd2, P.YS3u1] ], [ [P.g, P.YS3Qd2, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_406_120,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_406_121,(1,0,1):C.UVGC_406_122,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_406_123,(1,0,2):C.UVGC_406_124,(1,0,6):C.UVGC_406_125,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_371_67,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_405_116,(0,0,1):C.UVGC_371_70,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_405_117,(0,0,2):C.UVGC_405_118,(0,0,6):C.UVGC_405_119})

V_840 = CTVertex(name = 'V_840',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qd3, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qd3, P.YS3u1] ], [ [P.g, P.YS3Qd3, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_406_120,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_406_121,(1,0,1):C.UVGC_406_122,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_406_123,(1,0,2):C.UVGC_406_124,(1,0,6):C.UVGC_406_125,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_371_67,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_405_116,(0,0,1):C.UVGC_371_70,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_405_117,(0,0,2):C.UVGC_405_118,(0,0,6):C.UVGC_405_119})

V_841 = CTVertex(name = 'V_841',
                 type = 'UV',
                 particles = [ P.YS3u1__tilde__, P.YS3u1__tilde__, P.YS3u1, P.YS3u1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3u1] ], [ [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_371_66,(1,0,0):C.UVGC_377_74,(1,0,3):C.UVGC_371_68,(1,0,5):C.UVGC_380_78,(1,0,1):C.UVGC_377_76,(1,0,4):C.UVGC_380_79,(0,0,2):C.UVGC_371_66,(0,0,0):C.UVGC_377_74,(0,0,3):C.UVGC_371_68,(0,0,5):C.UVGC_380_78,(0,0,1):C.UVGC_377_76,(0,0,4):C.UVGC_380_79})

V_842 = CTVertex(name = 'V_842',
                 type = 'UV',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qu1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qu1, P.YS3u2] ], [ [P.g, P.YS3Qu1, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_450_146,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_454_154,(1,0,1):C.UVGC_450_148,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_454_155,(1,0,2):C.UVGC_390_96,(1,0,6):C.UVGC_454_156,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_449_141,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_453_151,(0,0,1):C.UVGC_449_143,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_453_152,(0,0,2):C.UVGC_389_87,(0,0,6):C.UVGC_453_153})

V_843 = CTVertex(name = 'V_843',
                 type = 'UV',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qu2, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qu2, P.YS3u2] ], [ [P.g, P.YS3Qu2, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_450_146,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_454_154,(1,0,1):C.UVGC_450_148,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_454_155,(1,0,2):C.UVGC_390_96,(1,0,6):C.UVGC_454_156,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_449_141,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_453_151,(0,0,1):C.UVGC_449_143,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_453_152,(0,0,2):C.UVGC_389_87,(0,0,6):C.UVGC_453_153})

V_844 = CTVertex(name = 'V_844',
                 type = 'UV',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qu3, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qu3], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qu3, P.YS3u2] ], [ [P.g, P.YS3Qu3, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qu3, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_450_146,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_454_154,(1,0,1):C.UVGC_450_148,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_454_155,(1,0,2):C.UVGC_390_96,(1,0,6):C.UVGC_454_156,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_449_141,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_453_151,(0,0,1):C.UVGC_449_143,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_453_152,(0,0,2):C.UVGC_389_87,(0,0,6):C.UVGC_453_153})

V_845 = CTVertex(name = 'V_845',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qd1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qd1, P.YS3u2] ], [ [P.g, P.YS3Qd1, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_406_120,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_406_121,(1,0,1):C.UVGC_406_122,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_406_123,(1,0,2):C.UVGC_406_124,(1,0,6):C.UVGC_406_125,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_371_67,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_405_116,(0,0,1):C.UVGC_371_70,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_405_117,(0,0,2):C.UVGC_405_118,(0,0,6):C.UVGC_405_119})

V_846 = CTVertex(name = 'V_846',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qd2, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qd2, P.YS3u2] ], [ [P.g, P.YS3Qd2, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_406_120,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_406_121,(1,0,1):C.UVGC_406_122,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_406_123,(1,0,2):C.UVGC_406_124,(1,0,6):C.UVGC_406_125,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_371_67,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_405_116,(0,0,1):C.UVGC_371_70,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_405_117,(0,0,2):C.UVGC_405_118,(0,0,6):C.UVGC_405_119})

V_847 = CTVertex(name = 'V_847',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qd3, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qd3, P.YS3u2] ], [ [P.g, P.YS3Qd3, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_406_120,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_406_121,(1,0,1):C.UVGC_406_122,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_406_123,(1,0,2):C.UVGC_406_124,(1,0,6):C.UVGC_406_125,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_371_67,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_405_116,(0,0,1):C.UVGC_371_70,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_405_117,(0,0,2):C.UVGC_405_118,(0,0,6):C.UVGC_405_119})

V_848 = CTVertex(name = 'V_848',
                 type = 'UV',
                 particles = [ P.YS3u1__tilde__, P.YS3u1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3u1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3u1], [P.g, P.YS3u2] ], [ [P.g, P.YS3u1, P.YS3u2] ], [ [P.g, P.YS3u1, P.YS3u2, P.Z] ], [ [P.g, P.YS3u1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_450_146,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_504_163,(1,0,1):C.UVGC_450_148,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_504_164,(1,0,2):C.UVGC_390_96,(1,0,6):C.UVGC_390_98,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_449_141,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_503_161,(0,0,1):C.UVGC_449_143,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_503_162,(0,0,2):C.UVGC_389_87,(0,0,6):C.UVGC_389_89})

V_849 = CTVertex(name = 'V_849',
                 type = 'UV',
                 particles = [ P.YS3u2__tilde__, P.YS3u2__tilde__, P.YS3u2, P.YS3u2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3u2] ], [ [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_371_66,(1,0,0):C.UVGC_377_74,(1,0,3):C.UVGC_371_68,(1,0,5):C.UVGC_380_78,(1,0,1):C.UVGC_377_76,(1,0,4):C.UVGC_380_79,(0,0,2):C.UVGC_371_66,(0,0,0):C.UVGC_377_74,(0,0,3):C.UVGC_371_68,(0,0,5):C.UVGC_380_78,(0,0,1):C.UVGC_377_76,(0,0,4):C.UVGC_380_79})

V_850 = CTVertex(name = 'V_850',
                 type = 'UV',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qu1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qu1, P.YS3u3] ], [ [P.g, P.YS3Qu1, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_450_146,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_454_154,(1,0,1):C.UVGC_450_148,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_454_155,(1,0,2):C.UVGC_390_96,(1,0,6):C.UVGC_454_156,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_449_141,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_453_151,(0,0,1):C.UVGC_449_143,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_453_152,(0,0,2):C.UVGC_389_87,(0,0,6):C.UVGC_453_153})

V_851 = CTVertex(name = 'V_851',
                 type = 'UV',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qu2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qu2, P.YS3u3] ], [ [P.g, P.YS3Qu2, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_450_146,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_454_154,(1,0,1):C.UVGC_450_148,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_454_155,(1,0,2):C.UVGC_390_96,(1,0,6):C.UVGC_454_156,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_449_141,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_453_151,(0,0,1):C.UVGC_449_143,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_453_152,(0,0,2):C.UVGC_389_87,(0,0,6):C.UVGC_453_153})

V_852 = CTVertex(name = 'V_852',
                 type = 'UV',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qu3, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qu3], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qu3, P.YS3u3] ], [ [P.g, P.YS3Qu3, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qu3, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_450_146,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_454_154,(1,0,1):C.UVGC_450_148,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_454_155,(1,0,2):C.UVGC_390_96,(1,0,6):C.UVGC_454_156,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_449_141,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_453_151,(0,0,1):C.UVGC_449_143,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_453_152,(0,0,2):C.UVGC_389_87,(0,0,6):C.UVGC_453_153})

V_853 = CTVertex(name = 'V_853',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qd1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qd1, P.YS3u3] ], [ [P.g, P.YS3Qd1, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_406_120,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_406_121,(1,0,1):C.UVGC_406_122,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_406_123,(1,0,2):C.UVGC_406_124,(1,0,6):C.UVGC_406_125,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_371_67,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_405_116,(0,0,1):C.UVGC_371_70,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_405_117,(0,0,2):C.UVGC_405_118,(0,0,6):C.UVGC_405_119})

V_854 = CTVertex(name = 'V_854',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qd2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qd2, P.YS3u3] ], [ [P.g, P.YS3Qd2, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_406_120,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_406_121,(1,0,1):C.UVGC_406_122,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_406_123,(1,0,2):C.UVGC_406_124,(1,0,6):C.UVGC_406_125,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_371_67,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_405_116,(0,0,1):C.UVGC_371_70,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_405_117,(0,0,2):C.UVGC_405_118,(0,0,6):C.UVGC_405_119})

V_855 = CTVertex(name = 'V_855',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qd3, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qd3, P.YS3u3] ], [ [P.g, P.YS3Qd3, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_406_120,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_406_121,(1,0,1):C.UVGC_406_122,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_406_123,(1,0,2):C.UVGC_406_124,(1,0,6):C.UVGC_406_125,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_371_67,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_405_116,(0,0,1):C.UVGC_371_70,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_405_117,(0,0,2):C.UVGC_405_118,(0,0,6):C.UVGC_405_119})

V_856 = CTVertex(name = 'V_856',
                 type = 'UV',
                 particles = [ P.YS3u1__tilde__, P.YS3u1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3u1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3u1], [P.g, P.YS3u3] ], [ [P.g, P.YS3u1, P.YS3u3] ], [ [P.g, P.YS3u1, P.YS3u3, P.Z] ], [ [P.g, P.YS3u1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_450_146,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_504_163,(1,0,1):C.UVGC_450_148,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_504_164,(1,0,2):C.UVGC_390_96,(1,0,6):C.UVGC_390_98,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_449_141,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_503_161,(0,0,1):C.UVGC_449_143,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_503_162,(0,0,2):C.UVGC_389_87,(0,0,6):C.UVGC_389_89})

V_857 = CTVertex(name = 'V_857',
                 type = 'UV',
                 particles = [ P.YS3u2__tilde__, P.YS3u2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3u2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3u2], [P.g, P.YS3u3] ], [ [P.g, P.YS3u2, P.YS3u3] ], [ [P.g, P.YS3u2, P.YS3u3, P.Z] ], [ [P.g, P.YS3u2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_450_146,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_504_163,(1,0,1):C.UVGC_450_148,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_504_164,(1,0,2):C.UVGC_390_96,(1,0,6):C.UVGC_390_98,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_449_141,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_503_161,(0,0,1):C.UVGC_449_143,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_503_162,(0,0,2):C.UVGC_389_87,(0,0,6):C.UVGC_389_89})

V_858 = CTVertex(name = 'V_858',
                 type = 'UV',
                 particles = [ P.YS3u3__tilde__, P.YS3u3__tilde__, P.YS3u3, P.YS3u3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3u3] ], [ [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_371_66,(1,0,0):C.UVGC_377_74,(1,0,3):C.UVGC_371_68,(1,0,5):C.UVGC_380_78,(1,0,1):C.UVGC_377_76,(1,0,4):C.UVGC_380_79,(0,0,2):C.UVGC_371_66,(0,0,0):C.UVGC_377_74,(0,0,3):C.UVGC_371_68,(0,0,5):C.UVGC_380_78,(0,0,1):C.UVGC_377_76,(0,0,4):C.UVGC_380_79})

V_859 = CTVertex(name = 'V_859',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3d1, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3d1, P.YS3Qu1] ], [ [P.g, P.YS3d1, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_406_120,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_438_129,(1,0,1):C.UVGC_406_122,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_438_130,(1,0,2):C.UVGC_406_124,(1,0,6):C.UVGC_438_131,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_371_67,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_437_126,(0,0,1):C.UVGC_371_70,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_437_127,(0,0,2):C.UVGC_405_118,(0,0,6):C.UVGC_437_128})

V_860 = CTVertex(name = 'V_860',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3d1, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3d1, P.YS3Qu2] ], [ [P.g, P.YS3d1, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_406_120,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_438_129,(1,0,1):C.UVGC_406_122,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_438_130,(1,0,2):C.UVGC_406_124,(1,0,6):C.UVGC_438_131,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_371_67,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_437_126,(0,0,1):C.UVGC_371_70,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_437_127,(0,0,2):C.UVGC_405_118,(0,0,6):C.UVGC_437_128})

V_861 = CTVertex(name = 'V_861',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3d1, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3d1, P.YS3Qu3] ], [ [P.g, P.YS3d1, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_406_120,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_438_129,(1,0,1):C.UVGC_406_122,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_438_130,(1,0,2):C.UVGC_406_124,(1,0,6):C.UVGC_438_131,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_371_67,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_437_126,(0,0,1):C.UVGC_371_70,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_437_127,(0,0,2):C.UVGC_405_118,(0,0,6):C.UVGC_437_128})

V_862 = CTVertex(name = 'V_862',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qd1] ], [ [P.a, P.g, P.YS3d1, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qd1] ], [ [P.g, P.YS3d1, P.YS3Qd1] ], [ [P.g, P.YS3d1, P.YS3Qd1, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_390_96,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_396_107,(1,0,1):C.UVGC_390_99,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_396_108,(1,0,2):C.UVGC_390_102,(1,0,6):C.UVGC_396_109,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_389_87,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_395_104,(0,0,1):C.UVGC_389_90,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_395_105,(0,0,2):C.UVGC_389_93,(0,0,6):C.UVGC_395_106})

V_863 = CTVertex(name = 'V_863',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3d1, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3d1, P.YS3Qd2] ], [ [P.g, P.YS3d1, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_390_96,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_396_107,(1,0,1):C.UVGC_390_99,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_396_108,(1,0,2):C.UVGC_390_102,(1,0,6):C.UVGC_396_109,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_389_87,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_395_104,(0,0,1):C.UVGC_389_90,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_395_105,(0,0,2):C.UVGC_389_93,(0,0,6):C.UVGC_395_106})

V_864 = CTVertex(name = 'V_864',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3d1, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3d1, P.YS3Qd3] ], [ [P.g, P.YS3d1, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_390_96,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_396_107,(1,0,1):C.UVGC_390_99,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_396_108,(1,0,2):C.UVGC_390_102,(1,0,6):C.UVGC_396_109,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_389_87,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_395_104,(0,0,1):C.UVGC_389_90,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_395_105,(0,0,2):C.UVGC_389_93,(0,0,6):C.UVGC_395_106})

V_865 = CTVertex(name = 'V_865',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3d1, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3u1] ], [ [P.g, P.YS3d1, P.YS3u1] ], [ [P.g, P.YS3d1, P.YS3u1, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_406_120,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_498_158,(1,0,1):C.UVGC_406_122,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_498_159,(1,0,2):C.UVGC_406_124,(1,0,6):C.UVGC_498_160,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_371_67,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_371_69,(0,0,1):C.UVGC_371_70,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_371_71,(0,0,2):C.UVGC_405_118,(0,0,6):C.UVGC_497_157})

V_866 = CTVertex(name = 'V_866',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3d1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3u2] ], [ [P.g, P.YS3d1, P.YS3u2] ], [ [P.g, P.YS3d1, P.YS3u2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_406_120,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_498_158,(1,0,1):C.UVGC_406_122,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_498_159,(1,0,2):C.UVGC_406_124,(1,0,6):C.UVGC_498_160,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_371_67,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_371_69,(0,0,1):C.UVGC_371_70,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_371_71,(0,0,2):C.UVGC_405_118,(0,0,6):C.UVGC_497_157})

V_867 = CTVertex(name = 'V_867',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3d1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3u3] ], [ [P.g, P.YS3d1, P.YS3u3] ], [ [P.g, P.YS3d1, P.YS3u3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_406_120,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_498_158,(1,0,1):C.UVGC_406_122,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_498_159,(1,0,2):C.UVGC_406_124,(1,0,6):C.UVGC_498_160,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_371_67,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_371_69,(0,0,1):C.UVGC_371_70,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_371_71,(0,0,2):C.UVGC_405_118,(0,0,6):C.UVGC_497_157})

V_868 = CTVertex(name = 'V_868',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1__tilde__, P.YS3d1, P.YS3d1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1] ], [ [P.g] ], [ [P.g, P.YS3d1] ], [ [P.g, P.YS3d1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_371_66,(1,0,0):C.UVGC_371_67,(1,0,3):C.UVGC_371_68,(1,0,5):C.UVGC_371_69,(1,0,1):C.UVGC_371_70,(1,0,4):C.UVGC_371_71,(0,0,2):C.UVGC_371_66,(0,0,0):C.UVGC_371_67,(0,0,3):C.UVGC_371_68,(0,0,5):C.UVGC_371_69,(0,0,1):C.UVGC_371_70,(0,0,4):C.UVGC_371_71})

V_869 = CTVertex(name = 'V_869',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3d2, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3d2, P.YS3Qu1] ], [ [P.g, P.YS3d2, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_406_120,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_438_129,(1,0,1):C.UVGC_406_122,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_438_130,(1,0,2):C.UVGC_406_124,(1,0,6):C.UVGC_438_131,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_371_67,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_437_126,(0,0,1):C.UVGC_371_70,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_437_127,(0,0,2):C.UVGC_405_118,(0,0,6):C.UVGC_437_128})

V_870 = CTVertex(name = 'V_870',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3d2, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3d2, P.YS3Qu2] ], [ [P.g, P.YS3d2, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_406_120,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_438_129,(1,0,1):C.UVGC_406_122,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_438_130,(1,0,2):C.UVGC_406_124,(1,0,6):C.UVGC_438_131,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_371_67,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_437_126,(0,0,1):C.UVGC_371_70,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_437_127,(0,0,2):C.UVGC_405_118,(0,0,6):C.UVGC_437_128})

V_871 = CTVertex(name = 'V_871',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3d2, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3d2, P.YS3Qu3] ], [ [P.g, P.YS3d2, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_406_120,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_438_129,(1,0,1):C.UVGC_406_122,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_438_130,(1,0,2):C.UVGC_406_124,(1,0,6):C.UVGC_438_131,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_371_67,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_437_126,(0,0,1):C.UVGC_371_70,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_437_127,(0,0,2):C.UVGC_405_118,(0,0,6):C.UVGC_437_128})

V_872 = CTVertex(name = 'V_872',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qd1] ], [ [P.a, P.g, P.YS3d2, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qd1] ], [ [P.g, P.YS3d2, P.YS3Qd1] ], [ [P.g, P.YS3d2, P.YS3Qd1, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_390_96,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_396_107,(1,0,1):C.UVGC_390_99,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_396_108,(1,0,2):C.UVGC_390_102,(1,0,6):C.UVGC_396_109,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_389_87,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_395_104,(0,0,1):C.UVGC_389_90,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_395_105,(0,0,2):C.UVGC_389_93,(0,0,6):C.UVGC_395_106})

V_873 = CTVertex(name = 'V_873',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3d2, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3d2, P.YS3Qd2] ], [ [P.g, P.YS3d2, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_390_96,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_396_107,(1,0,1):C.UVGC_390_99,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_396_108,(1,0,2):C.UVGC_390_102,(1,0,6):C.UVGC_396_109,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_389_87,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_395_104,(0,0,1):C.UVGC_389_90,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_395_105,(0,0,2):C.UVGC_389_93,(0,0,6):C.UVGC_395_106})

V_874 = CTVertex(name = 'V_874',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3d2, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3d2, P.YS3Qd3] ], [ [P.g, P.YS3d2, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_390_96,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_396_107,(1,0,1):C.UVGC_390_99,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_396_108,(1,0,2):C.UVGC_390_102,(1,0,6):C.UVGC_396_109,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_389_87,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_395_104,(0,0,1):C.UVGC_389_90,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_395_105,(0,0,2):C.UVGC_389_93,(0,0,6):C.UVGC_395_106})

V_875 = CTVertex(name = 'V_875',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3d2, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3u1] ], [ [P.g, P.YS3d2, P.YS3u1] ], [ [P.g, P.YS3d2, P.YS3u1, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_406_120,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_498_158,(1,0,1):C.UVGC_406_122,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_498_159,(1,0,2):C.UVGC_406_124,(1,0,6):C.UVGC_498_160,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_371_67,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_371_69,(0,0,1):C.UVGC_371_70,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_371_71,(0,0,2):C.UVGC_405_118,(0,0,6):C.UVGC_497_157})

V_876 = CTVertex(name = 'V_876',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3d2, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3u2] ], [ [P.g, P.YS3d2, P.YS3u2] ], [ [P.g, P.YS3d2, P.YS3u2, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_406_120,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_498_158,(1,0,1):C.UVGC_406_122,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_498_159,(1,0,2):C.UVGC_406_124,(1,0,6):C.UVGC_498_160,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_371_67,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_371_69,(0,0,1):C.UVGC_371_70,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_371_71,(0,0,2):C.UVGC_405_118,(0,0,6):C.UVGC_497_157})

V_877 = CTVertex(name = 'V_877',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3d2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3u3] ], [ [P.g, P.YS3d2, P.YS3u3] ], [ [P.g, P.YS3d2, P.YS3u3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_406_120,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_498_158,(1,0,1):C.UVGC_406_122,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_498_159,(1,0,2):C.UVGC_406_124,(1,0,6):C.UVGC_498_160,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_371_67,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_371_69,(0,0,1):C.UVGC_371_70,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_371_71,(0,0,2):C.UVGC_405_118,(0,0,6):C.UVGC_497_157})

V_878 = CTVertex(name = 'V_878',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3d2] ], [ [P.a, P.g, P.YS3d1, P.YS3d2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3d2] ], [ [P.g, P.YS3d1, P.YS3d2] ], [ [P.g, P.YS3d1, P.YS3d2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3d2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_390_96,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_390_98,(1,0,1):C.UVGC_390_99,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_390_101,(1,0,2):C.UVGC_390_102,(1,0,6):C.UVGC_390_103,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_389_87,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_389_89,(0,0,1):C.UVGC_389_90,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_389_92,(0,0,2):C.UVGC_389_93,(0,0,6):C.UVGC_389_94})

V_879 = CTVertex(name = 'V_879',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2__tilde__, P.YS3d2, P.YS3d2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2] ], [ [P.g] ], [ [P.g, P.YS3d2] ], [ [P.g, P.YS3d2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_371_66,(1,0,0):C.UVGC_371_67,(1,0,3):C.UVGC_371_68,(1,0,5):C.UVGC_371_69,(1,0,1):C.UVGC_371_70,(1,0,4):C.UVGC_371_71,(0,0,2):C.UVGC_371_66,(0,0,0):C.UVGC_371_67,(0,0,3):C.UVGC_371_68,(0,0,5):C.UVGC_371_69,(0,0,1):C.UVGC_371_70,(0,0,4):C.UVGC_371_71})

V_880 = CTVertex(name = 'V_880',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3d3, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3d3, P.YS3Qu1] ], [ [P.g, P.YS3d3, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_406_120,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_438_129,(1,0,1):C.UVGC_406_122,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_438_130,(1,0,2):C.UVGC_406_124,(1,0,6):C.UVGC_438_131,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_371_67,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_437_126,(0,0,1):C.UVGC_371_70,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_437_127,(0,0,2):C.UVGC_405_118,(0,0,6):C.UVGC_437_128})

V_881 = CTVertex(name = 'V_881',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3d3, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3d3, P.YS3Qu2] ], [ [P.g, P.YS3d3, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_406_120,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_438_129,(1,0,1):C.UVGC_406_122,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_438_130,(1,0,2):C.UVGC_406_124,(1,0,6):C.UVGC_438_131,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_371_67,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_437_126,(0,0,1):C.UVGC_371_70,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_437_127,(0,0,2):C.UVGC_405_118,(0,0,6):C.UVGC_437_128})

V_882 = CTVertex(name = 'V_882',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3d3, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3d3, P.YS3Qu3] ], [ [P.g, P.YS3d3, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_406_120,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_438_129,(1,0,1):C.UVGC_406_122,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_438_130,(1,0,2):C.UVGC_406_124,(1,0,6):C.UVGC_438_131,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_371_67,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_437_126,(0,0,1):C.UVGC_371_70,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_437_127,(0,0,2):C.UVGC_405_118,(0,0,6):C.UVGC_437_128})

V_883 = CTVertex(name = 'V_883',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qd1] ], [ [P.a, P.g, P.YS3d3, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qd1] ], [ [P.g, P.YS3d3, P.YS3Qd1] ], [ [P.g, P.YS3d3, P.YS3Qd1, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_390_96,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_396_107,(1,0,1):C.UVGC_390_99,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_396_108,(1,0,2):C.UVGC_390_102,(1,0,6):C.UVGC_396_109,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_389_87,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_395_104,(0,0,1):C.UVGC_389_90,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_395_105,(0,0,2):C.UVGC_389_93,(0,0,6):C.UVGC_395_106})

V_884 = CTVertex(name = 'V_884',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3d3, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3d3, P.YS3Qd2] ], [ [P.g, P.YS3d3, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_390_96,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_396_107,(1,0,1):C.UVGC_390_99,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_396_108,(1,0,2):C.UVGC_390_102,(1,0,6):C.UVGC_396_109,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_389_87,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_395_104,(0,0,1):C.UVGC_389_90,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_395_105,(0,0,2):C.UVGC_389_93,(0,0,6):C.UVGC_395_106})

V_885 = CTVertex(name = 'V_885',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3d3, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3d3, P.YS3Qd3] ], [ [P.g, P.YS3d3, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_390_96,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_396_107,(1,0,1):C.UVGC_390_99,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_396_108,(1,0,2):C.UVGC_390_102,(1,0,6):C.UVGC_396_109,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_389_87,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_395_104,(0,0,1):C.UVGC_389_90,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_395_105,(0,0,2):C.UVGC_389_93,(0,0,6):C.UVGC_395_106})

V_886 = CTVertex(name = 'V_886',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3d3, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3u1] ], [ [P.g, P.YS3d3, P.YS3u1] ], [ [P.g, P.YS3d3, P.YS3u1, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_406_120,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_498_158,(1,0,1):C.UVGC_406_122,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_498_159,(1,0,2):C.UVGC_406_124,(1,0,6):C.UVGC_498_160,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_371_67,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_371_69,(0,0,1):C.UVGC_371_70,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_371_71,(0,0,2):C.UVGC_405_118,(0,0,6):C.UVGC_497_157})

V_887 = CTVertex(name = 'V_887',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3d3, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3u2] ], [ [P.g, P.YS3d3, P.YS3u2] ], [ [P.g, P.YS3d3, P.YS3u2, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_406_120,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_498_158,(1,0,1):C.UVGC_406_122,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_498_159,(1,0,2):C.UVGC_406_124,(1,0,6):C.UVGC_498_160,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_371_67,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_371_69,(0,0,1):C.UVGC_371_70,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_371_71,(0,0,2):C.UVGC_405_118,(0,0,6):C.UVGC_497_157})

V_888 = CTVertex(name = 'V_888',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3d3, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3u3] ], [ [P.g, P.YS3d3, P.YS3u3] ], [ [P.g, P.YS3d3, P.YS3u3, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_406_120,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_498_158,(1,0,1):C.UVGC_406_122,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_498_159,(1,0,2):C.UVGC_406_124,(1,0,6):C.UVGC_498_160,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_371_67,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_371_69,(0,0,1):C.UVGC_371_70,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_371_71,(0,0,2):C.UVGC_405_118,(0,0,6):C.UVGC_497_157})

V_889 = CTVertex(name = 'V_889',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3d3] ], [ [P.a, P.g, P.YS3d1, P.YS3d3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3d3] ], [ [P.g, P.YS3d1, P.YS3d3] ], [ [P.g, P.YS3d1, P.YS3d3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3d3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_390_96,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_390_98,(1,0,1):C.UVGC_390_99,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_390_101,(1,0,2):C.UVGC_390_102,(1,0,6):C.UVGC_390_103,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_389_87,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_389_89,(0,0,1):C.UVGC_389_90,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_389_92,(0,0,2):C.UVGC_389_93,(0,0,6):C.UVGC_389_94})

V_890 = CTVertex(name = 'V_890',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3d3] ], [ [P.a, P.g, P.YS3d2, P.YS3d3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3d3] ], [ [P.g, P.YS3d2, P.YS3d3] ], [ [P.g, P.YS3d2, P.YS3d3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3d3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_390_95,(1,0,0):C.UVGC_390_96,(1,0,4):C.UVGC_390_97,(1,0,8):C.UVGC_390_98,(1,0,1):C.UVGC_390_99,(1,0,5):C.UVGC_390_100,(1,0,7):C.UVGC_390_101,(1,0,2):C.UVGC_390_102,(1,0,6):C.UVGC_390_103,(0,0,3):C.UVGC_389_86,(0,0,0):C.UVGC_389_87,(0,0,4):C.UVGC_389_88,(0,0,8):C.UVGC_389_89,(0,0,1):C.UVGC_389_90,(0,0,5):C.UVGC_389_91,(0,0,7):C.UVGC_389_92,(0,0,2):C.UVGC_389_93,(0,0,6):C.UVGC_389_94})

V_891 = CTVertex(name = 'V_891',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3__tilde__, P.YS3d3, P.YS3d3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3] ], [ [P.g] ], [ [P.g, P.YS3d3] ], [ [P.g, P.YS3d3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_371_66,(1,0,0):C.UVGC_371_67,(1,0,3):C.UVGC_371_68,(1,0,5):C.UVGC_371_69,(1,0,1):C.UVGC_371_70,(1,0,4):C.UVGC_371_71,(0,0,2):C.UVGC_371_66,(0,0,0):C.UVGC_371_67,(0,0,3):C.UVGC_371_68,(0,0,5):C.UVGC_371_69,(0,0,1):C.UVGC_371_70,(0,0,4):C.UVGC_371_71})

V_892 = CTVertex(name = 'V_892',
                 type = 'UV',
                 particles = [ P.g, P.g, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVV10 ],
                 loop_particles = [ [ [P.YS3Qd1], [P.YS3Qd2], [P.YS3Qd3], [P.YS3Qu1], [P.YS3Qu2], [P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_267_17})

