# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.3.1 for Linux x86 (64-bit) (July 24, 2023)
# Date: Mon 22 Jun 2026 18:48:24


from object_library import all_vertices, all_CTvertices, Vertex, CTVertex
import particles as P
import CT_couplings as C
import lorentz as L


V_1 = CTVertex(name = 'V_1',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV1, L.VVV2, L.VVV4, L.VVV6, L.VVV7, L.VVV8 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_154_37,(0,0,1):C.R2GC_154_38,(0,1,0):C.R2GC_159_39,(0,1,1):C.R2GC_159_40,(0,2,0):C.R2GC_159_39,(0,2,1):C.R2GC_159_40,(0,3,0):C.R2GC_154_37,(0,3,1):C.R2GC_154_38,(0,4,0):C.R2GC_154_37,(0,4,1):C.R2GC_154_38,(0,5,0):C.R2GC_159_39,(0,5,1):C.R2GC_159_40})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(2,0,0):C.R2GC_124_13,(2,0,1):C.R2GC_124_14,(0,0,0):C.R2GC_124_13,(0,0,1):C.R2GC_124_14,(4,0,0):C.R2GC_122_9,(4,0,1):C.R2GC_122_10,(3,0,0):C.R2GC_122_9,(3,0,1):C.R2GC_122_10,(8,0,0):C.R2GC_123_11,(8,0,1):C.R2GC_123_12,(6,0,0):C.R2GC_127_18,(6,0,1):C.R2GC_166_46,(7,0,0):C.R2GC_128_20,(7,0,1):C.R2GC_165_45,(5,0,0):C.R2GC_122_9,(5,0,1):C.R2GC_122_10,(1,0,0):C.R2GC_122_9,(1,0,1):C.R2GC_122_10,(11,0,0):C.R2GC_126_16,(11,0,1):C.R2GC_126_17,(10,0,0):C.R2GC_126_16,(10,0,1):C.R2GC_126_17,(9,0,1):C.R2GC_125_15,(2,1,0):C.R2GC_124_13,(2,1,1):C.R2GC_124_14,(0,1,0):C.R2GC_124_13,(0,1,1):C.R2GC_124_14,(4,1,0):C.R2GC_122_9,(4,1,1):C.R2GC_122_10,(3,1,0):C.R2GC_122_9,(3,1,1):C.R2GC_122_10,(8,1,0):C.R2GC_123_11,(8,1,1):C.R2GC_167_47,(6,1,0):C.R2GC_162_41,(6,1,1):C.R2GC_162_42,(7,1,0):C.R2GC_128_20,(7,1,1):C.R2GC_128_21,(5,1,0):C.R2GC_122_9,(5,1,1):C.R2GC_122_10,(1,1,0):C.R2GC_122_9,(1,1,1):C.R2GC_122_10,(11,1,0):C.R2GC_126_16,(11,1,1):C.R2GC_126_17,(10,1,0):C.R2GC_126_16,(10,1,1):C.R2GC_126_17,(9,1,1):C.R2GC_125_15,(0,2,0):C.R2GC_124_13,(0,2,1):C.R2GC_124_14,(2,2,0):C.R2GC_124_13,(2,2,1):C.R2GC_124_14,(5,2,0):C.R2GC_122_9,(5,2,1):C.R2GC_122_10,(1,2,0):C.R2GC_122_9,(1,2,1):C.R2GC_122_10,(7,2,0):C.R2GC_163_43,(7,2,1):C.R2GC_124_14,(4,2,0):C.R2GC_122_9,(4,2,1):C.R2GC_122_10,(3,2,0):C.R2GC_122_9,(3,2,1):C.R2GC_122_10,(8,2,0):C.R2GC_123_11,(8,2,1):C.R2GC_164_44,(6,2,0):C.R2GC_127_18,(6,2,1):C.R2GC_127_19,(11,2,0):C.R2GC_126_16,(11,2,1):C.R2GC_126_17,(10,2,0):C.R2GC_126_16,(10,2,1):C.R2GC_126_17,(9,2,1):C.R2GC_125_15})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.t__tilde__, P.b, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_176_51,(0,1,0):C.R2GC_178_52})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_150_33})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_149_32})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.b__tilde__, P.t, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_179_53,(0,1,0):C.R2GC_175_50})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_180_54})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_181_55})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.u] ] ],
               couplings = {(0,0,0):C.R2GC_137_25})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_137_25})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_137_25})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_129_22})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_129_22})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_129_22})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_130_23})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_130_23})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_130_23})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_130_23})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_130_23})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_130_23})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_142_29})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_142_29})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_142_29})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_142_29})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_142_29})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_142_29})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_102_5,(0,1,0):C.R2GC_174_49})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_102_5,(0,1,0):C.R2GC_174_49})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_102_5,(0,1,0):C.R2GC_174_49})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_103_6,(0,1,0):C.R2GC_148_31})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_103_6,(0,1,0):C.R2GC_148_31})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_103_6,(0,1,0):C.R2GC_148_31})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_146_30,(0,2,0):C.R2GC_146_30,(0,1,0):C.R2GC_131_24,(0,3,0):C.R2GC_131_24})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_131_24})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_131_24})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_131_24})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_171_48,(0,2,0):C.R2GC_171_48,(0,1,0):C.R2GC_131_24,(0,3,0):C.R2GC_131_24})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_131_24})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV2, L.VV3 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ], [ [P.t] ] ],
                couplings = {(0,0,2):C.R2GC_153_36,(0,1,0):C.R2GC_93_56,(0,1,3):C.R2GC_93_57,(0,2,1):C.R2GC_152_34,(0,2,2):C.R2GC_152_35})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.g, P.g, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_94_58,(0,0,1):C.R2GC_94_59})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_106_8,(0,1,0):C.R2GC_106_8,(0,2,0):C.R2GC_106_8})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Z ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_98_66,(0,0,1):C.R2GC_98_67,(0,1,0):C.R2GC_98_66,(0,1,1):C.R2GC_98_67,(0,2,0):C.R2GC_98_66,(0,2,1):C.R2GC_98_67})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.g, P.g, P.Z, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_101_3,(0,0,1):C.R2GC_101_4,(0,1,0):C.R2GC_101_3,(0,1,1):C.R2GC_101_4,(0,2,0):C.R2GC_101_3,(0,2,1):C.R2GC_101_4})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.a, P.a, P.g, P.g ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_96_62,(0,0,1):C.R2GC_96_63,(0,1,0):C.R2GC_96_62,(0,1,1):C.R2GC_96_63,(0,2,0):C.R2GC_96_62,(0,2,1):C.R2GC_96_63})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Z ],
                color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(1,0,0):C.R2GC_100_1,(1,0,1):C.R2GC_100_2,(0,1,0):C.R2GC_99_68,(0,1,1):C.R2GC_99_69,(0,2,0):C.R2GC_99_68,(0,2,1):C.R2GC_99_69,(0,3,0):C.R2GC_99_68,(0,3,1):C.R2GC_99_69})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.g ],
                color = [ 'd(2,3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_97_64,(0,0,1):C.R2GC_97_65,(0,1,0):C.R2GC_97_64,(0,1,1):C.R2GC_97_65,(0,2,0):C.R2GC_97_64,(0,2,1):C.R2GC_97_65})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.g, P.g, P.H, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_95_60,(0,0,1):C.R2GC_95_61})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.g, P.g, P.G0, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_95_60,(0,0,1):C.R2GC_95_61})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_105_7})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.g, P.g, P.Xs, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b, P.YFd] ], [ [P.c, P.YFu], [P.d, P.YFd], [P.s, P.YFd], [P.u, P.YFu] ], [ [P.t, P.YFu] ] ],
                couplings = {(0,0,0):C.R2GC_141_26,(0,0,1):C.R2GC_141_27,(0,0,2):C.R2GC_141_28})

V_51 = CTVertex(name = 'V_51',
                type = 'UV',
                particles = [ P.g, P.g, P.g ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVV1, L.VVV2, L.VVV3, L.VVV4, L.VVV5, L.VVV6, L.VVV7, L.VVV8 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.UVGC_154_45,(0,0,1):C.UVGC_154_46,(0,0,2):C.UVGC_154_47,(0,0,3):C.UVGC_121_8,(0,0,4):C.UVGC_154_48,(0,1,0):C.UVGC_159_59,(0,1,1):C.UVGC_159_60,(0,1,2):C.UVGC_159_61,(0,1,3):C.UVGC_159_62,(0,1,4):C.UVGC_159_63,(0,3,0):C.UVGC_159_59,(0,3,1):C.UVGC_159_60,(0,3,2):C.UVGC_161_66,(0,3,3):C.UVGC_120_6,(0,3,4):C.UVGC_159_63,(0,5,0):C.UVGC_154_45,(0,5,1):C.UVGC_154_46,(0,5,2):C.UVGC_156_51,(0,5,3):C.UVGC_156_52,(0,5,4):C.UVGC_154_48,(0,6,0):C.UVGC_154_45,(0,6,1):C.UVGC_154_46,(0,6,2):C.UVGC_155_49,(0,6,3):C.UVGC_155_50,(0,6,4):C.UVGC_154_48,(0,7,0):C.UVGC_159_59,(0,7,1):C.UVGC_159_60,(0,7,2):C.UVGC_160_64,(0,7,3):C.UVGC_160_65,(0,7,4):C.UVGC_159_63,(0,2,2):C.UVGC_120_5,(0,2,3):C.UVGC_120_6,(0,4,2):C.UVGC_121_7,(0,4,3):C.UVGC_121_8})

V_52 = CTVertex(name = 'V_52',
                type = 'UV',
                particles = [ P.g, P.g, P.g, P.g ],
                color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(2,0,3):C.UVGC_123_12,(2,0,4):C.UVGC_123_11,(0,0,3):C.UVGC_123_12,(0,0,4):C.UVGC_123_11,(4,0,3):C.UVGC_122_9,(4,0,4):C.UVGC_122_10,(3,0,3):C.UVGC_122_9,(3,0,4):C.UVGC_122_10,(8,0,3):C.UVGC_123_11,(8,0,4):C.UVGC_123_12,(6,0,0):C.UVGC_165_78,(6,0,2):C.UVGC_165_79,(6,0,3):C.UVGC_166_83,(6,0,4):C.UVGC_166_84,(6,0,5):C.UVGC_165_82,(7,0,0):C.UVGC_165_78,(7,0,2):C.UVGC_165_79,(7,0,3):C.UVGC_165_80,(7,0,4):C.UVGC_165_81,(7,0,5):C.UVGC_165_82,(5,0,3):C.UVGC_122_9,(5,0,4):C.UVGC_122_10,(1,0,3):C.UVGC_122_9,(1,0,4):C.UVGC_122_10,(11,0,3):C.UVGC_126_15,(11,0,4):C.UVGC_126_16,(10,0,3):C.UVGC_126_15,(10,0,4):C.UVGC_126_16,(9,0,3):C.UVGC_125_13,(9,0,4):C.UVGC_125_14,(2,1,3):C.UVGC_123_12,(2,1,4):C.UVGC_123_11,(0,1,3):C.UVGC_123_12,(0,1,4):C.UVGC_123_11,(4,1,3):C.UVGC_122_9,(4,1,4):C.UVGC_122_10,(3,1,3):C.UVGC_122_9,(3,1,4):C.UVGC_122_10,(8,1,0):C.UVGC_167_85,(8,1,2):C.UVGC_167_86,(8,1,3):C.UVGC_167_87,(8,1,4):C.UVGC_167_88,(8,1,5):C.UVGC_167_89,(6,1,0):C.UVGC_162_67,(6,1,3):C.UVGC_162_68,(6,1,4):C.UVGC_162_69,(6,1,5):C.UVGC_162_70,(7,1,1):C.UVGC_127_17,(7,1,3):C.UVGC_128_19,(7,1,4):C.UVGC_128_20,(5,1,3):C.UVGC_122_9,(5,1,4):C.UVGC_122_10,(1,1,3):C.UVGC_122_9,(1,1,4):C.UVGC_122_10,(11,1,3):C.UVGC_126_15,(11,1,4):C.UVGC_126_16,(10,1,3):C.UVGC_126_15,(10,1,4):C.UVGC_126_16,(9,1,3):C.UVGC_125_13,(9,1,4):C.UVGC_125_14,(0,2,3):C.UVGC_123_12,(0,2,4):C.UVGC_123_11,(2,2,3):C.UVGC_123_12,(2,2,4):C.UVGC_123_11,(5,2,3):C.UVGC_122_9,(5,2,4):C.UVGC_122_10,(1,2,3):C.UVGC_122_9,(1,2,4):C.UVGC_122_10,(7,2,0):C.UVGC_162_67,(7,2,3):C.UVGC_163_71,(7,2,4):C.UVGC_163_72,(7,2,5):C.UVGC_162_70,(4,2,3):C.UVGC_122_9,(4,2,4):C.UVGC_122_10,(3,2,3):C.UVGC_122_9,(3,2,4):C.UVGC_122_10,(8,2,0):C.UVGC_164_73,(8,2,2):C.UVGC_164_74,(8,2,3):C.UVGC_164_75,(8,2,4):C.UVGC_164_76,(8,2,5):C.UVGC_164_77,(6,2,1):C.UVGC_127_17,(6,2,3):C.UVGC_127_18,(6,2,4):C.UVGC_125_13,(11,2,3):C.UVGC_126_15,(11,2,4):C.UVGC_126_16,(10,2,3):C.UVGC_126_15,(10,2,4):C.UVGC_126_16,(9,2,3):C.UVGC_125_13,(9,2,4):C.UVGC_125_14})

V_53 = CTVertex(name = 'V_53',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_176_101,(0,0,2):C.UVGC_176_102,(0,0,1):C.UVGC_176_103,(0,1,0):C.UVGC_178_106,(0,1,2):C.UVGC_178_107,(0,1,1):C.UVGC_178_108})

V_54 = CTVertex(name = 'V_54',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_150_36})

V_55 = CTVertex(name = 'V_55',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_149_35})

V_56 = CTVertex(name = 'V_56',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_179_109,(0,0,2):C.UVGC_179_110,(0,0,1):C.UVGC_179_111,(0,1,0):C.UVGC_175_98,(0,1,2):C.UVGC_175_99,(0,1,1):C.UVGC_175_100})

V_57 = CTVertex(name = 'V_57',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_180_112})

V_58 = CTVertex(name = 'V_58',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_181_113})

V_59 = CTVertex(name = 'V_59',
                type = 'UV',
                particles = [ P.YFd__tilde__, P.d, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g] ], [ PRIVATE`PythonFormatLoopParticles[1] ] ],
                couplings = {(0,0,1):C.UVGC_134_24,(0,0,0):C.UVGC_132_23})

V_60 = CTVertex(name = 'V_60',
                type = 'UV',
                particles = [ P.YFd__tilde__, P.s, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s] ], [ PRIVATE`PythonFormatLoopParticles[1] ] ],
                couplings = {(0,0,1):C.UVGC_134_24,(0,0,0):C.UVGC_132_23})

V_61 = CTVertex(name = 'V_61',
                type = 'UV',
                particles = [ P.YFd__tilde__, P.b, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g] ], [ PRIVATE`PythonFormatLoopParticles[1] ] ],
                couplings = {(0,0,1):C.UVGC_151_37,(0,0,0):C.UVGC_151_38})

V_62 = CTVertex(name = 'V_62',
                type = 'UV',
                particles = [ P.YFu__tilde__, P.u, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.u] ], [ PRIVATE`PythonFormatLoopParticles[1] ] ],
                couplings = {(0,0,1):C.UVGC_132_22,(0,0,0):C.UVGC_132_23})

V_63 = CTVertex(name = 'V_63',
                type = 'UV',
                particles = [ P.YFu__tilde__, P.c, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.c, P.g] ], [ PRIVATE`PythonFormatLoopParticles[1] ] ],
                couplings = {(0,0,1):C.UVGC_132_22,(0,0,0):C.UVGC_132_23})

V_64 = CTVertex(name = 'V_64',
                type = 'UV',
                particles = [ P.YFu__tilde__, P.t, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.t] ], [ PRIVATE`PythonFormatLoopParticles[1] ] ],
                couplings = {(0,0,1):C.UVGC_177_104,(0,0,0):C.UVGC_177_105})

V_65 = CTVertex(name = 'V_65',
                type = 'UV',
                particles = [ P.d__tilde__, P.YFd, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.d, P.g] ], [ PRIVATE`PythonFormatLoopParticles[1] ] ],
                couplings = {(0,0,1):C.UVGC_134_24,(0,0,0):C.UVGC_132_23})

V_66 = CTVertex(name = 'V_66',
                type = 'UV',
                particles = [ P.s__tilde__, P.YFd, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.s] ], [ PRIVATE`PythonFormatLoopParticles[1] ] ],
                couplings = {(0,0,1):C.UVGC_134_24,(0,0,0):C.UVGC_132_23})

V_67 = CTVertex(name = 'V_67',
                type = 'UV',
                particles = [ P.b__tilde__, P.YFd, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.b, P.g] ], [ PRIVATE`PythonFormatLoopParticles[1] ] ],
                couplings = {(0,0,1):C.UVGC_151_37,(0,0,0):C.UVGC_151_38})

V_68 = CTVertex(name = 'V_68',
                type = 'UV',
                particles = [ P.u__tilde__, P.YFu, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.u] ], [ PRIVATE`PythonFormatLoopParticles[1] ] ],
                couplings = {(0,0,1):C.UVGC_132_22,(0,0,0):C.UVGC_132_23})

V_69 = CTVertex(name = 'V_69',
                type = 'UV',
                particles = [ P.c__tilde__, P.YFu, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.c, P.g] ], [ PRIVATE`PythonFormatLoopParticles[1] ] ],
                couplings = {(0,0,1):C.UVGC_132_22,(0,0,0):C.UVGC_132_23})

V_70 = CTVertex(name = 'V_70',
                type = 'UV',
                particles = [ P.t__tilde__, P.YFu, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.t] ], [ PRIVATE`PythonFormatLoopParticles[1] ] ],
                couplings = {(0,0,1):C.UVGC_177_104,(0,0,0):C.UVGC_177_105})

V_71 = CTVertex(name = 'V_71',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_109_2})

V_72 = CTVertex(name = 'V_72',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_109_2})

V_73 = CTVertex(name = 'V_73',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV6 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_109_2,(0,1,0):C.UVGC_169_91})

V_74 = CTVertex(name = 'V_74',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_112_4})

V_75 = CTVertex(name = 'V_75',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_112_4})

V_76 = CTVertex(name = 'V_76',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV6 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_112_4,(0,1,0):C.UVGC_145_31})

V_77 = CTVertex(name = 'V_77',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV5, L.FFV6 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.t] ] ],
                couplings = {(0,0,4):C.UVGC_110_3,(0,1,0):C.UVGC_157_53,(0,1,1):C.UVGC_157_54,(0,1,2):C.UVGC_157_55,(0,1,3):C.UVGC_157_56,(0,1,5):C.UVGC_157_57})

V_78 = CTVertex(name = 'V_78',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV5, L.FFV6 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.c, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,2):C.UVGC_110_3,(0,1,0):C.UVGC_157_53,(0,1,1):C.UVGC_157_54,(0,1,3):C.UVGC_157_55,(0,1,4):C.UVGC_157_56,(0,1,5):C.UVGC_157_57})

V_79 = CTVertex(name = 'V_79',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV6 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.t] ] ],
                couplings = {(0,0,4):C.UVGC_110_3,(0,1,0):C.UVGC_157_53,(0,1,1):C.UVGC_157_54,(0,1,2):C.UVGC_157_55,(0,1,3):C.UVGC_157_56,(0,1,5):C.UVGC_157_57,(0,1,4):C.UVGC_170_92})

V_80 = CTVertex(name = 'V_80',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV5, L.FFV6 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,2):C.UVGC_110_3,(0,1,0):C.UVGC_157_53,(0,1,1):C.UVGC_157_54,(0,1,3):C.UVGC_157_55,(0,1,4):C.UVGC_157_56,(0,1,5):C.UVGC_157_57})

V_81 = CTVertex(name = 'V_81',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV5, L.FFV6 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.t] ] ],
                couplings = {(0,0,4):C.UVGC_110_3,(0,1,0):C.UVGC_157_53,(0,1,1):C.UVGC_157_54,(0,1,2):C.UVGC_157_55,(0,1,3):C.UVGC_157_56,(0,1,5):C.UVGC_157_57})

V_82 = CTVertex(name = 'V_82',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV6 ],
                loop_particles = [ [ [P.b] ], [ [P.b, P.g] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.UVGC_110_3,(0,1,0):C.UVGC_157_53,(0,1,2):C.UVGC_157_54,(0,1,3):C.UVGC_157_55,(0,1,4):C.UVGC_157_56,(0,1,5):C.UVGC_157_57,(0,1,1):C.UVGC_158_58})

V_83 = CTVertex(name = 'V_83',
                type = 'UV',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_142_28,(0,0,1):C.UVGC_142_29})

V_84 = CTVertex(name = 'V_84',
                type = 'UV',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_142_28,(0,0,1):C.UVGC_142_29})

V_85 = CTVertex(name = 'V_85',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_172_94,(0,0,2):C.UVGC_172_95,(0,0,1):C.UVGC_142_29})

V_86 = CTVertex(name = 'V_86',
                type = 'UV',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_142_28,(0,0,1):C.UVGC_142_29})

V_87 = CTVertex(name = 'V_87',
                type = 'UV',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_142_28,(0,0,1):C.UVGC_142_29})

V_88 = CTVertex(name = 'V_88',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_172_94,(0,0,2):C.UVGC_172_95,(0,0,1):C.UVGC_142_29})

V_89 = CTVertex(name = 'V_89',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_173_96,(0,1,0):C.UVGC_174_97})

V_90 = CTVertex(name = 'V_90',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_147_33,(0,1,0):C.UVGC_148_34})

V_91 = CTVertex(name = 'V_91',
                type = 'UV',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_146_32,(0,2,0):C.UVGC_146_32,(0,1,0):C.UVGC_144_30,(0,3,0):C.UVGC_144_30})

V_92 = CTVertex(name = 'V_92',
                type = 'UV',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_131_21,(0,1,0):C.UVGC_108_1,(0,2,0):C.UVGC_108_1})

V_93 = CTVertex(name = 'V_93',
                type = 'UV',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_131_21,(0,1,0):C.UVGC_108_1,(0,2,0):C.UVGC_108_1})

V_94 = CTVertex(name = 'V_94',
                type = 'UV',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_131_21,(0,1,0):C.UVGC_108_1,(0,2,0):C.UVGC_108_1})

V_95 = CTVertex(name = 'V_95',
                type = 'UV',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_171_93,(0,2,0):C.UVGC_171_93,(0,1,0):C.UVGC_168_90,(0,3,0):C.UVGC_168_90})

V_96 = CTVertex(name = 'V_96',
                type = 'UV',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_131_21,(0,1,0):C.UVGC_108_1,(0,2,0):C.UVGC_108_1})

V_97 = CTVertex(name = 'V_97',
                type = 'UV',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV3 ],
                loop_particles = [ [ [P.b] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.UVGC_153_41,(0,0,1):C.UVGC_153_42,(0,0,2):C.UVGC_153_43,(0,0,3):C.UVGC_153_44,(0,1,0):C.UVGC_152_39,(0,1,3):C.UVGC_152_40})

V_98 = CTVertex(name = 'V_98',
                type = 'UV',
                particles = [ P.g, P.g, P.Xs, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b, P.YFd] ], [ [P.c, P.YFu], [P.d, P.YFd], [P.s, P.YFd], [P.u, P.YFu] ], [ [P.t, P.YFu] ] ],
                couplings = {(0,0,0):C.UVGC_141_25,(0,0,1):C.UVGC_141_26,(0,0,2):C.UVGC_141_27})

