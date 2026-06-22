# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.3.1 for Linux x86 (64-bit) (July 24, 2023)
# Date: Mon 22 Jun 2026 15:25:16


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
               couplings = {(0,0,0):C.R2GC_149_36,(0,0,1):C.R2GC_149_37,(0,1,0):C.R2GC_154_38,(0,1,1):C.R2GC_154_39,(0,2,0):C.R2GC_154_38,(0,2,1):C.R2GC_154_39,(0,3,0):C.R2GC_149_36,(0,3,1):C.R2GC_149_37,(0,4,0):C.R2GC_149_36,(0,4,1):C.R2GC_149_37,(0,5,0):C.R2GC_154_38,(0,5,1):C.R2GC_154_39})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(2,0,0):C.R2GC_125_15,(2,0,1):C.R2GC_125_16,(0,0,0):C.R2GC_125_15,(0,0,1):C.R2GC_125_16,(4,0,0):C.R2GC_123_11,(4,0,1):C.R2GC_123_12,(3,0,0):C.R2GC_123_11,(3,0,1):C.R2GC_123_12,(8,0,0):C.R2GC_124_13,(8,0,1):C.R2GC_124_14,(6,0,0):C.R2GC_128_20,(6,0,1):C.R2GC_161_45,(7,0,0):C.R2GC_129_22,(7,0,1):C.R2GC_160_44,(5,0,0):C.R2GC_123_11,(5,0,1):C.R2GC_123_12,(1,0,0):C.R2GC_123_11,(1,0,1):C.R2GC_123_12,(11,0,0):C.R2GC_127_18,(11,0,1):C.R2GC_127_19,(10,0,0):C.R2GC_127_18,(10,0,1):C.R2GC_127_19,(9,0,1):C.R2GC_126_17,(2,1,0):C.R2GC_125_15,(2,1,1):C.R2GC_125_16,(0,1,0):C.R2GC_125_15,(0,1,1):C.R2GC_125_16,(4,1,0):C.R2GC_123_11,(4,1,1):C.R2GC_123_12,(3,1,0):C.R2GC_123_11,(3,1,1):C.R2GC_123_12,(8,1,0):C.R2GC_124_13,(8,1,1):C.R2GC_162_46,(6,1,0):C.R2GC_157_40,(6,1,1):C.R2GC_157_41,(7,1,0):C.R2GC_129_22,(7,1,1):C.R2GC_129_23,(5,1,0):C.R2GC_123_11,(5,1,1):C.R2GC_123_12,(1,1,0):C.R2GC_123_11,(1,1,1):C.R2GC_123_12,(11,1,0):C.R2GC_127_18,(11,1,1):C.R2GC_127_19,(10,1,0):C.R2GC_127_18,(10,1,1):C.R2GC_127_19,(9,1,1):C.R2GC_126_17,(0,2,0):C.R2GC_125_15,(0,2,1):C.R2GC_125_16,(2,2,0):C.R2GC_125_15,(2,2,1):C.R2GC_125_16,(5,2,0):C.R2GC_123_11,(5,2,1):C.R2GC_123_12,(1,2,0):C.R2GC_123_11,(1,2,1):C.R2GC_123_12,(7,2,0):C.R2GC_158_42,(7,2,1):C.R2GC_125_16,(4,2,0):C.R2GC_123_11,(4,2,1):C.R2GC_123_12,(3,2,0):C.R2GC_123_11,(3,2,1):C.R2GC_123_12,(8,2,0):C.R2GC_124_13,(8,2,1):C.R2GC_159_43,(6,2,0):C.R2GC_128_20,(6,2,1):C.R2GC_128_21,(11,2,0):C.R2GC_127_18,(11,2,1):C.R2GC_127_19,(10,2,0):C.R2GC_127_18,(10,2,1):C.R2GC_127_19,(9,2,1):C.R2GC_126_17})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.t__tilde__, P.b, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_171_50,(0,1,0):C.R2GC_172_51})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_146_32})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_145_31})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.b__tilde__, P.t, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_173_52,(0,1,0):C.R2GC_170_49})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_174_53})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_175_54})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.u] ] ],
               couplings = {(0,0,0):C.R2GC_135_27})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_135_27})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_135_27})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_130_24})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_130_24})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_130_24})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_131_25})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_131_25})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_131_25})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_131_25})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_131_25})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_131_25})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_138_28})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_138_28})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_138_28})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_138_28})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_138_28})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_138_28})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_103_7,(0,1,0):C.R2GC_169_48})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_103_7,(0,1,0):C.R2GC_169_48})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_103_7,(0,1,0):C.R2GC_169_48})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_104_8,(0,1,0):C.R2GC_144_30})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_104_8,(0,1,0):C.R2GC_144_30})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_104_8,(0,1,0):C.R2GC_144_30})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_132_26})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_132_26})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_166_47,(0,2,0):C.R2GC_166_47,(0,1,0):C.R2GC_132_26,(0,3,0):C.R2GC_132_26})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_132_26})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_132_26})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_142_29,(0,2,0):C.R2GC_142_29,(0,1,0):C.R2GC_132_26,(0,3,0):C.R2GC_132_26})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV2, L.VV3 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ], [ [P.t] ] ],
                couplings = {(0,0,2):C.R2GC_148_35,(0,1,0):C.R2GC_94_55,(0,1,3):C.R2GC_94_56,(0,2,1):C.R2GC_147_33,(0,2,2):C.R2GC_147_34})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.g, P.g, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_95_57,(0,0,1):C.R2GC_95_58})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_107_10,(0,1,0):C.R2GC_107_10,(0,2,0):C.R2GC_107_10})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Z ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_99_65,(0,0,1):C.R2GC_99_66,(0,1,0):C.R2GC_99_65,(0,1,1):C.R2GC_99_66,(0,2,0):C.R2GC_99_65,(0,2,1):C.R2GC_99_66})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.g, P.g, P.Z, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_102_5,(0,0,1):C.R2GC_102_6,(0,1,0):C.R2GC_102_5,(0,1,1):C.R2GC_102_6,(0,2,0):C.R2GC_102_5,(0,2,1):C.R2GC_102_6})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.a, P.a, P.g, P.g ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_97_61,(0,0,1):C.R2GC_97_62,(0,1,0):C.R2GC_97_61,(0,1,1):C.R2GC_97_62,(0,2,0):C.R2GC_97_61,(0,2,1):C.R2GC_97_62})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Z ],
                color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(1,0,0):C.R2GC_101_3,(1,0,1):C.R2GC_101_4,(0,1,0):C.R2GC_100_1,(0,1,1):C.R2GC_100_2,(0,2,0):C.R2GC_100_1,(0,2,1):C.R2GC_100_2,(0,3,0):C.R2GC_100_1,(0,3,1):C.R2GC_100_2})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.g ],
                color = [ 'd(2,3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_98_63,(0,0,1):C.R2GC_98_64,(0,1,0):C.R2GC_98_63,(0,1,1):C.R2GC_98_64,(0,2,0):C.R2GC_98_63,(0,2,1):C.R2GC_98_64})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.g, P.g, P.H, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_96_59,(0,0,1):C.R2GC_96_60})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.g, P.g, P.G0, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_96_59,(0,0,1):C.R2GC_96_60})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_106_9})

V_50 = CTVertex(name = 'V_50',
                type = 'UV',
                particles = [ P.g, P.g, P.g ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVV1, L.VVV2, L.VVV3, L.VVV4, L.VVV5, L.VVV6, L.VVV7, L.VVV8 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.UVGC_149_37,(0,0,1):C.UVGC_149_38,(0,0,2):C.UVGC_149_39,(0,0,3):C.UVGC_122_8,(0,0,4):C.UVGC_149_40,(0,1,0):C.UVGC_154_51,(0,1,1):C.UVGC_154_52,(0,1,2):C.UVGC_154_53,(0,1,3):C.UVGC_154_54,(0,1,4):C.UVGC_154_55,(0,3,0):C.UVGC_154_51,(0,3,1):C.UVGC_154_52,(0,3,2):C.UVGC_156_58,(0,3,3):C.UVGC_121_6,(0,3,4):C.UVGC_154_55,(0,5,0):C.UVGC_149_37,(0,5,1):C.UVGC_149_38,(0,5,2):C.UVGC_151_43,(0,5,3):C.UVGC_151_44,(0,5,4):C.UVGC_149_40,(0,6,0):C.UVGC_149_37,(0,6,1):C.UVGC_149_38,(0,6,2):C.UVGC_150_41,(0,6,3):C.UVGC_150_42,(0,6,4):C.UVGC_149_40,(0,7,0):C.UVGC_154_51,(0,7,1):C.UVGC_154_52,(0,7,2):C.UVGC_155_56,(0,7,3):C.UVGC_155_57,(0,7,4):C.UVGC_154_55,(0,2,2):C.UVGC_121_5,(0,2,3):C.UVGC_121_6,(0,4,2):C.UVGC_122_7,(0,4,3):C.UVGC_122_8})

V_51 = CTVertex(name = 'V_51',
                type = 'UV',
                particles = [ P.g, P.g, P.g, P.g ],
                color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(2,0,3):C.UVGC_124_12,(2,0,4):C.UVGC_124_11,(0,0,3):C.UVGC_124_12,(0,0,4):C.UVGC_124_11,(4,0,3):C.UVGC_123_9,(4,0,4):C.UVGC_123_10,(3,0,3):C.UVGC_123_9,(3,0,4):C.UVGC_123_10,(8,0,3):C.UVGC_124_11,(8,0,4):C.UVGC_124_12,(6,0,0):C.UVGC_160_70,(6,0,2):C.UVGC_160_71,(6,0,3):C.UVGC_161_75,(6,0,4):C.UVGC_161_76,(6,0,5):C.UVGC_160_74,(7,0,0):C.UVGC_160_70,(7,0,2):C.UVGC_160_71,(7,0,3):C.UVGC_160_72,(7,0,4):C.UVGC_160_73,(7,0,5):C.UVGC_160_74,(5,0,3):C.UVGC_123_9,(5,0,4):C.UVGC_123_10,(1,0,3):C.UVGC_123_9,(1,0,4):C.UVGC_123_10,(11,0,3):C.UVGC_127_15,(11,0,4):C.UVGC_127_16,(10,0,3):C.UVGC_127_15,(10,0,4):C.UVGC_127_16,(9,0,3):C.UVGC_126_13,(9,0,4):C.UVGC_126_14,(2,1,3):C.UVGC_124_12,(2,1,4):C.UVGC_124_11,(0,1,3):C.UVGC_124_12,(0,1,4):C.UVGC_124_11,(4,1,3):C.UVGC_123_9,(4,1,4):C.UVGC_123_10,(3,1,3):C.UVGC_123_9,(3,1,4):C.UVGC_123_10,(8,1,0):C.UVGC_162_77,(8,1,2):C.UVGC_162_78,(8,1,3):C.UVGC_162_79,(8,1,4):C.UVGC_162_80,(8,1,5):C.UVGC_162_81,(6,1,0):C.UVGC_157_59,(6,1,3):C.UVGC_157_60,(6,1,4):C.UVGC_157_61,(6,1,5):C.UVGC_157_62,(7,1,1):C.UVGC_128_17,(7,1,3):C.UVGC_129_19,(7,1,4):C.UVGC_129_20,(5,1,3):C.UVGC_123_9,(5,1,4):C.UVGC_123_10,(1,1,3):C.UVGC_123_9,(1,1,4):C.UVGC_123_10,(11,1,3):C.UVGC_127_15,(11,1,4):C.UVGC_127_16,(10,1,3):C.UVGC_127_15,(10,1,4):C.UVGC_127_16,(9,1,3):C.UVGC_126_13,(9,1,4):C.UVGC_126_14,(0,2,3):C.UVGC_124_12,(0,2,4):C.UVGC_124_11,(2,2,3):C.UVGC_124_12,(2,2,4):C.UVGC_124_11,(5,2,3):C.UVGC_123_9,(5,2,4):C.UVGC_123_10,(1,2,3):C.UVGC_123_9,(1,2,4):C.UVGC_123_10,(7,2,0):C.UVGC_157_59,(7,2,3):C.UVGC_158_63,(7,2,4):C.UVGC_158_64,(7,2,5):C.UVGC_157_62,(4,2,3):C.UVGC_123_9,(4,2,4):C.UVGC_123_10,(3,2,3):C.UVGC_123_9,(3,2,4):C.UVGC_123_10,(8,2,0):C.UVGC_159_65,(8,2,2):C.UVGC_159_66,(8,2,3):C.UVGC_159_67,(8,2,4):C.UVGC_159_68,(8,2,5):C.UVGC_159_69,(6,2,1):C.UVGC_128_17,(6,2,3):C.UVGC_128_18,(6,2,4):C.UVGC_126_13,(11,2,3):C.UVGC_127_15,(11,2,4):C.UVGC_127_16,(10,2,3):C.UVGC_127_15,(10,2,4):C.UVGC_127_16,(9,2,3):C.UVGC_126_13,(9,2,4):C.UVGC_126_14})

V_52 = CTVertex(name = 'V_52',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_171_93,(0,0,2):C.UVGC_171_94,(0,0,1):C.UVGC_171_95,(0,1,0):C.UVGC_172_96,(0,1,2):C.UVGC_172_97,(0,1,1):C.UVGC_172_98})

V_53 = CTVertex(name = 'V_53',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_146_30})

V_54 = CTVertex(name = 'V_54',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_145_29})

V_55 = CTVertex(name = 'V_55',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_173_99,(0,0,2):C.UVGC_173_100,(0,0,1):C.UVGC_173_101,(0,1,0):C.UVGC_170_90,(0,1,2):C.UVGC_170_91,(0,1,1):C.UVGC_170_92})

V_56 = CTVertex(name = 'V_56',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_174_102})

V_57 = CTVertex(name = 'V_57',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_175_103})

V_58 = CTVertex(name = 'V_58',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_110_2})

V_59 = CTVertex(name = 'V_59',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_110_2})

V_60 = CTVertex(name = 'V_60',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV6 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_110_2,(0,1,0):C.UVGC_164_83})

V_61 = CTVertex(name = 'V_61',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_113_4})

V_62 = CTVertex(name = 'V_62',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_113_4})

V_63 = CTVertex(name = 'V_63',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV6 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_113_4,(0,1,0):C.UVGC_141_25})

V_64 = CTVertex(name = 'V_64',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV5, L.FFV6 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.t] ] ],
                couplings = {(0,0,4):C.UVGC_111_3,(0,1,0):C.UVGC_152_45,(0,1,1):C.UVGC_152_46,(0,1,2):C.UVGC_152_47,(0,1,3):C.UVGC_152_48,(0,1,5):C.UVGC_152_49})

V_65 = CTVertex(name = 'V_65',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV5, L.FFV6 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.c, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,2):C.UVGC_111_3,(0,1,0):C.UVGC_152_45,(0,1,1):C.UVGC_152_46,(0,1,3):C.UVGC_152_47,(0,1,4):C.UVGC_152_48,(0,1,5):C.UVGC_152_49})

V_66 = CTVertex(name = 'V_66',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV6 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.t] ] ],
                couplings = {(0,0,4):C.UVGC_111_3,(0,1,0):C.UVGC_152_45,(0,1,1):C.UVGC_152_46,(0,1,2):C.UVGC_152_47,(0,1,3):C.UVGC_152_48,(0,1,5):C.UVGC_152_49,(0,1,4):C.UVGC_165_84})

V_67 = CTVertex(name = 'V_67',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV5, L.FFV6 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,2):C.UVGC_111_3,(0,1,0):C.UVGC_152_45,(0,1,1):C.UVGC_152_46,(0,1,3):C.UVGC_152_47,(0,1,4):C.UVGC_152_48,(0,1,5):C.UVGC_152_49})

V_68 = CTVertex(name = 'V_68',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV5, L.FFV6 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.t] ] ],
                couplings = {(0,0,4):C.UVGC_111_3,(0,1,0):C.UVGC_152_45,(0,1,1):C.UVGC_152_46,(0,1,2):C.UVGC_152_47,(0,1,3):C.UVGC_152_48,(0,1,5):C.UVGC_152_49})

V_69 = CTVertex(name = 'V_69',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV6 ],
                loop_particles = [ [ [P.b] ], [ [P.b, P.g] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.UVGC_111_3,(0,1,0):C.UVGC_152_45,(0,1,2):C.UVGC_152_46,(0,1,3):C.UVGC_152_47,(0,1,4):C.UVGC_152_48,(0,1,5):C.UVGC_152_49,(0,1,1):C.UVGC_153_50})

V_70 = CTVertex(name = 'V_70',
                type = 'UV',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_138_22,(0,0,1):C.UVGC_138_23})

V_71 = CTVertex(name = 'V_71',
                type = 'UV',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_138_22,(0,0,1):C.UVGC_138_23})

V_72 = CTVertex(name = 'V_72',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_167_86,(0,0,2):C.UVGC_167_87,(0,0,1):C.UVGC_138_23})

V_73 = CTVertex(name = 'V_73',
                type = 'UV',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_138_22,(0,0,1):C.UVGC_138_23})

V_74 = CTVertex(name = 'V_74',
                type = 'UV',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_138_22,(0,0,1):C.UVGC_138_23})

V_75 = CTVertex(name = 'V_75',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_167_86,(0,0,2):C.UVGC_167_87,(0,0,1):C.UVGC_138_23})

V_76 = CTVertex(name = 'V_76',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_168_88,(0,1,0):C.UVGC_169_89})

V_77 = CTVertex(name = 'V_77',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_143_27,(0,1,0):C.UVGC_144_28})

V_78 = CTVertex(name = 'V_78',
                type = 'UV',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_132_21,(0,1,0):C.UVGC_109_1,(0,2,0):C.UVGC_109_1})

V_79 = CTVertex(name = 'V_79',
                type = 'UV',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_132_21,(0,1,0):C.UVGC_109_1,(0,2,0):C.UVGC_109_1})

V_80 = CTVertex(name = 'V_80',
                type = 'UV',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_166_85,(0,2,0):C.UVGC_166_85,(0,1,0):C.UVGC_163_82,(0,3,0):C.UVGC_163_82})

V_81 = CTVertex(name = 'V_81',
                type = 'UV',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_132_21,(0,1,0):C.UVGC_109_1,(0,2,0):C.UVGC_109_1})

V_82 = CTVertex(name = 'V_82',
                type = 'UV',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_132_21,(0,1,0):C.UVGC_109_1,(0,2,0):C.UVGC_109_1})

V_83 = CTVertex(name = 'V_83',
                type = 'UV',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_142_26,(0,2,0):C.UVGC_142_26,(0,1,0):C.UVGC_140_24,(0,3,0):C.UVGC_140_24})

V_84 = CTVertex(name = 'V_84',
                type = 'UV',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV3 ],
                loop_particles = [ [ [P.b] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.UVGC_148_33,(0,0,1):C.UVGC_148_34,(0,0,2):C.UVGC_148_35,(0,0,3):C.UVGC_148_36,(0,1,0):C.UVGC_147_31,(0,1,3):C.UVGC_147_32})

