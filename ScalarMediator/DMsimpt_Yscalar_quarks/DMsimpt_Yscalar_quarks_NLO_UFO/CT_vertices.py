# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.3.1 for Linux x86 (64-bit) (July 24, 2023)
# Date: Wed 11 Nov 2026 17:52:56


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
               couplings = {(0,0,0):C.R2GC_199_74,(0,0,1):C.R2GC_199_75,(0,1,0):C.R2GC_207_77,(0,1,1):C.R2GC_207_78,(0,2,0):C.R2GC_207_77,(0,2,1):C.R2GC_207_78,(0,3,0):C.R2GC_199_74,(0,3,1):C.R2GC_199_75,(0,4,0):C.R2GC_199_74,(0,4,1):C.R2GC_199_75,(0,5,0):C.R2GC_207_77,(0,5,1):C.R2GC_207_78})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(2,0,0):C.R2GC_139_32,(2,0,1):C.R2GC_139_33,(0,0,0):C.R2GC_139_32,(0,0,1):C.R2GC_139_33,(4,0,0):C.R2GC_137_28,(4,0,1):C.R2GC_137_29,(3,0,0):C.R2GC_137_28,(3,0,1):C.R2GC_137_29,(8,0,0):C.R2GC_138_30,(8,0,1):C.R2GC_138_31,(6,0,0):C.R2GC_143_37,(6,0,1):C.R2GC_218_88,(7,0,0):C.R2GC_144_39,(7,0,1):C.R2GC_217_87,(5,0,0):C.R2GC_137_28,(5,0,1):C.R2GC_137_29,(1,0,0):C.R2GC_137_28,(1,0,1):C.R2GC_137_29,(11,0,0):C.R2GC_141_35,(11,0,1):C.R2GC_141_36,(10,0,0):C.R2GC_141_35,(10,0,1):C.R2GC_141_36,(9,0,1):C.R2GC_140_34,(2,1,0):C.R2GC_139_32,(2,1,1):C.R2GC_139_33,(0,1,0):C.R2GC_139_32,(0,1,1):C.R2GC_139_33,(4,1,0):C.R2GC_137_28,(4,1,1):C.R2GC_137_29,(3,1,0):C.R2GC_137_28,(3,1,1):C.R2GC_137_29,(8,1,0):C.R2GC_138_30,(8,1,1):C.R2GC_219_89,(6,1,0):C.R2GC_216_85,(6,1,1):C.R2GC_216_86,(7,1,0):C.R2GC_144_39,(7,1,1):C.R2GC_144_40,(5,1,0):C.R2GC_137_28,(5,1,1):C.R2GC_137_29,(1,1,0):C.R2GC_137_28,(1,1,1):C.R2GC_137_29,(11,1,0):C.R2GC_141_35,(11,1,1):C.R2GC_141_36,(10,1,0):C.R2GC_141_35,(10,1,1):C.R2GC_141_36,(9,1,1):C.R2GC_140_34,(0,2,0):C.R2GC_139_32,(0,2,1):C.R2GC_139_33,(2,2,0):C.R2GC_139_32,(2,2,1):C.R2GC_139_33,(5,2,0):C.R2GC_137_28,(5,2,1):C.R2GC_137_29,(1,2,0):C.R2GC_137_28,(1,2,1):C.R2GC_137_29,(7,2,0):C.R2GC_214_83,(7,2,1):C.R2GC_139_33,(4,2,0):C.R2GC_137_28,(4,2,1):C.R2GC_137_29,(3,2,0):C.R2GC_137_28,(3,2,1):C.R2GC_137_29,(8,2,0):C.R2GC_138_30,(8,2,1):C.R2GC_215_84,(6,2,0):C.R2GC_143_37,(6,2,1):C.R2GC_143_38,(11,2,0):C.R2GC_141_35,(11,2,1):C.R2GC_141_36,(10,2,0):C.R2GC_141_35,(10,2,1):C.R2GC_141_36,(9,2,1):C.R2GC_140_34})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.t__tilde__, P.b, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_190_64,(0,1,0):C.R2GC_192_66})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_181_60})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_180_59})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.b__tilde__, P.t, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_193_67,(0,1,0):C.R2GC_189_63})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_194_68})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_195_69})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.a, P.YSd__tilde__, P.YSd ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               loop_particles = [ [ [P.g, P.YSd] ] ],
               couplings = {(0,0,0):C.R2GC_151_44})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.Xm, P.d, P.YSd__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.YSd] ] ],
                couplings = {(0,0,0):C.R2GC_169_56})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.Xm, P.s, P.YSd__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.YSd] ] ],
                couplings = {(0,0,0):C.R2GC_169_56})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.Xm, P.b, P.YSd__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g, P.YSd] ] ],
                couplings = {(0,0,0):C.R2GC_182_61})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.g, P.YSd__tilde__, P.YSd ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.YSd] ] ],
                couplings = {(0,0,0):C.R2GC_202_76})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.d__tilde__, P.Xm, P.YSd ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.YSd] ] ],
                couplings = {(0,0,0):C.R2GC_169_56})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.s__tilde__, P.Xm, P.YSd ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.s, P.YSd] ] ],
                couplings = {(0,0,0):C.R2GC_169_56})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.b__tilde__, P.Xm, P.YSd ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.b, P.g, P.YSd] ] ],
                couplings = {(0,0,0):C.R2GC_182_61})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.H, P.YSd__tilde__, P.YSd ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                loop_particles = [ [ [P.g, P.YSd] ] ],
                couplings = {(0,0,0):C.R2GC_156_49})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.a, P.a, P.YSd__tilde__, P.YSd ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.YSd] ] ],
                couplings = {(0,0,0):C.R2GC_152_45})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.a, P.g, P.YSd__tilde__, P.YSd ],
                color = [ 'T(2,4,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.YSd] ] ],
                couplings = {(0,0,0):C.R2GC_210_79})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.g, P.g, P.YSd__tilde__, P.YSd ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g] ], [ [P.g, P.YSd] ] ],
                couplings = {(2,0,0):C.R2GC_212_81,(2,0,1):C.R2GC_212_82,(1,0,0):C.R2GC_212_81,(1,0,1):C.R2GC_212_82,(0,0,0):C.R2GC_141_36,(0,0,1):C.R2GC_149_42})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.a, P.YSu__tilde__, P.YSu ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.YSu] ] ],
                couplings = {(0,0,0):C.R2GC_159_50})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.Xm, P.u, P.YSu__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.u, P.YSu] ] ],
                couplings = {(0,0,0):C.R2GC_169_56})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.Xm, P.c, P.YSu__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.c, P.g, P.YSu] ] ],
                couplings = {(0,0,0):C.R2GC_169_56})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.Xm, P.t, P.YSu__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.t, P.YSu] ] ],
                couplings = {(0,0,0):C.R2GC_191_65})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.g, P.YSu__tilde__, P.YSu ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.YSu] ] ],
                couplings = {(0,0,0):C.R2GC_202_76})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.u__tilde__, P.Xm, P.YSu ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.u, P.YSu] ] ],
                couplings = {(0,0,0):C.R2GC_169_56})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.c__tilde__, P.Xm, P.YSu ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.YSu] ] ],
                couplings = {(0,0,0):C.R2GC_169_56})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.t__tilde__, P.Xm, P.YSu ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.t, P.YSu] ] ],
                couplings = {(0,0,0):C.R2GC_191_65})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.H, P.YSu__tilde__, P.YSu ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                loop_particles = [ [ [P.g, P.YSu] ] ],
                couplings = {(0,0,0):C.R2GC_164_55})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.a, P.a, P.YSu__tilde__, P.YSu ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.YSu] ] ],
                couplings = {(0,0,0):C.R2GC_160_51})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.a, P.g, P.YSu__tilde__, P.YSu ],
                color = [ 'T(2,4,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.YSu] ] ],
                couplings = {(0,0,0):C.R2GC_211_80})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.g, P.g, P.YSu__tilde__, P.YSu ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g] ], [ [P.g, P.YSu] ] ],
                couplings = {(2,0,0):C.R2GC_212_81,(2,0,1):C.R2GC_212_82,(1,0,0):C.R2GC_212_81,(1,0,1):C.R2GC_212_82,(0,0,0):C.R2GC_141_36,(0,0,1):C.R2GC_149_42})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.Z, P.YSd__tilde__, P.YSd ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.YSd] ] ],
                couplings = {(0,0,0):C.R2GC_153_46})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.a, P.Z, P.YSd__tilde__, P.YSd ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.YSd] ] ],
                couplings = {(0,0,0):C.R2GC_154_47})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.g, P.Z, P.YSd__tilde__, P.YSd ],
                color = [ 'T(1,4,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.YSd] ] ],
                couplings = {(0,0,0):C.R2GC_220_90})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.Z, P.YSu__tilde__, P.YSu ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.YSu] ] ],
                couplings = {(0,0,0):C.R2GC_161_52})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.a, P.Z, P.YSu__tilde__, P.YSu ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.YSu] ] ],
                couplings = {(0,0,0):C.R2GC_162_53})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.g, P.Z, P.YSu__tilde__, P.YSu ],
                color = [ 'T(1,4,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.YSu] ] ],
                couplings = {(0,0,0):C.R2GC_221_91})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.Z, P.Z, P.YSd__tilde__, P.YSd ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.YSd] ] ],
                couplings = {(0,0,0):C.R2GC_155_48})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.Z, P.Z, P.YSu__tilde__, P.YSu ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.YSu] ] ],
                couplings = {(0,0,0):C.R2GC_163_54})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_106_4})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_106_4})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_106_4})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_100_1})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_100_1})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_100_1})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_101_2})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_101_2})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_101_2})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_101_2})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_101_2})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_101_2})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_170_57})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_170_57})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_170_57})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_170_57})

V_57 = CTVertex(name = 'V_57',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_170_57})

V_58 = CTVertex(name = 'V_58',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_170_57})

V_59 = CTVertex(name = 'V_59',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_118_24,(0,1,0):C.R2GC_108_5})

V_60 = CTVertex(name = 'V_60',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_118_24,(0,1,0):C.R2GC_108_5})

V_61 = CTVertex(name = 'V_61',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_118_24,(0,1,0):C.R2GC_108_5})

V_62 = CTVertex(name = 'V_62',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_119_25,(0,1,0):C.R2GC_102_3})

V_63 = CTVertex(name = 'V_63',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_119_25,(0,1,0):C.R2GC_102_3})

V_64 = CTVertex(name = 'V_64',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_119_25,(0,1,0):C.R2GC_102_3})

V_65 = CTVertex(name = 'V_65',
                type = 'R2',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_147_41})

V_66 = CTVertex(name = 'V_66',
                type = 'R2',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_147_41})

V_67 = CTVertex(name = 'V_67',
                type = 'R2',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_185_62,(0,2,0):C.R2GC_185_62,(0,1,0):C.R2GC_147_41,(0,3,0):C.R2GC_147_41})

V_68 = CTVertex(name = 'V_68',
                type = 'R2',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_147_41})

V_69 = CTVertex(name = 'V_69',
                type = 'R2',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_147_41})

V_70 = CTVertex(name = 'V_70',
                type = 'R2',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_177_58,(0,2,0):C.R2GC_177_58,(0,1,0):C.R2GC_147_41,(0,3,0):C.R2GC_147_41})

V_71 = CTVertex(name = 'V_71',
                type = 'R2',
                particles = [ P.YSu__tilde__, P.YSu ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SS1, L.SS2 ],
                loop_particles = [ [ [P.g, P.YSu] ] ],
                couplings = {(0,0,0):C.R2GC_222_92,(0,1,0):C.R2GC_150_43})

V_72 = CTVertex(name = 'V_72',
                type = 'R2',
                particles = [ P.YSd__tilde__, P.YSd ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SS1, L.SS2 ],
                loop_particles = [ [ [P.g, P.YSd] ] ],
                couplings = {(0,0,0):C.R2GC_196_70,(0,1,0):C.R2GC_150_43})

V_73 = CTVertex(name = 'V_73',
                type = 'R2',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV2, L.VV3 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ], [ [P.t] ] ],
                couplings = {(0,0,2):C.R2GC_198_73,(0,1,0):C.R2GC_109_6,(0,1,3):C.R2GC_109_7,(0,2,1):C.R2GC_197_71,(0,2,2):C.R2GC_197_72})

V_74 = CTVertex(name = 'V_74',
                type = 'R2',
                particles = [ P.g, P.g, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_110_8,(0,0,1):C.R2GC_110_9})

V_75 = CTVertex(name = 'V_75',
                type = 'R2',
                particles = [ P.a, P.a, P.g, P.g ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_112_12,(0,0,1):C.R2GC_112_13,(0,1,0):C.R2GC_112_12,(0,1,1):C.R2GC_112_13,(0,2,0):C.R2GC_112_12,(0,2,1):C.R2GC_112_13})

V_76 = CTVertex(name = 'V_76',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Z ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_114_16,(0,0,1):C.R2GC_114_17,(0,1,0):C.R2GC_114_16,(0,1,1):C.R2GC_114_17,(0,2,0):C.R2GC_114_16,(0,2,1):C.R2GC_114_17})

V_77 = CTVertex(name = 'V_77',
                type = 'R2',
                particles = [ P.g, P.g, P.Z, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_117_22,(0,0,1):C.R2GC_117_23,(0,1,0):C.R2GC_117_22,(0,1,1):C.R2GC_117_23,(0,2,0):C.R2GC_117_22,(0,2,1):C.R2GC_117_23})

V_78 = CTVertex(name = 'V_78',
                type = 'R2',
                particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_122_27,(0,1,0):C.R2GC_122_27,(0,2,0):C.R2GC_122_27})

V_79 = CTVertex(name = 'V_79',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.g ],
                color = [ 'd(2,3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_113_14,(0,0,1):C.R2GC_113_15,(0,1,0):C.R2GC_113_14,(0,1,1):C.R2GC_113_15,(0,2,0):C.R2GC_113_14,(0,2,1):C.R2GC_113_15})

V_80 = CTVertex(name = 'V_80',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Z ],
                color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(1,0,0):C.R2GC_116_20,(1,0,1):C.R2GC_116_21,(0,1,0):C.R2GC_115_18,(0,1,1):C.R2GC_115_19,(0,2,0):C.R2GC_115_18,(0,2,1):C.R2GC_115_19,(0,3,0):C.R2GC_115_18,(0,3,1):C.R2GC_115_19})

V_81 = CTVertex(name = 'V_81',
                type = 'R2',
                particles = [ P.g, P.g, P.H, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_111_10,(0,0,1):C.R2GC_111_11})

V_82 = CTVertex(name = 'V_82',
                type = 'R2',
                particles = [ P.g, P.g, P.G0, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_111_10,(0,0,1):C.R2GC_111_11})

V_83 = CTVertex(name = 'V_83',
                type = 'R2',
                particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_121_26})

V_84 = CTVertex(name = 'V_84',
                type = 'UV',
                particles = [ P.g, P.g, P.g ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVV1, L.VVV2, L.VVV3, L.VVV4, L.VVV5, L.VVV6, L.VVV7, L.VVV8 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.YSd] ], [ [P.YSd], [P.YSu] ], [ [P.YSu] ] ],
                couplings = {(0,0,0):C.UVGC_199_91,(0,0,1):C.UVGC_199_92,(0,0,2):C.UVGC_199_93,(0,0,3):C.UVGC_142_16,(0,0,4):C.UVGC_199_94,(0,0,5):C.UVGC_199_95,(0,0,7):C.UVGC_199_96,(0,1,0):C.UVGC_207_121,(0,1,1):C.UVGC_207_122,(0,1,2):C.UVGC_208_127,(0,1,3):C.UVGC_208_128,(0,1,4):C.UVGC_207_124,(0,1,5):C.UVGC_208_129,(0,1,7):C.UVGC_208_130,(0,3,0):C.UVGC_207_121,(0,3,1):C.UVGC_207_122,(0,3,2):C.UVGC_207_123,(0,3,3):C.UVGC_136_6,(0,3,4):C.UVGC_207_124,(0,3,5):C.UVGC_207_125,(0,3,7):C.UVGC_207_126,(0,5,0):C.UVGC_199_91,(0,5,1):C.UVGC_199_92,(0,5,2):C.UVGC_201_99,(0,5,3):C.UVGC_201_100,(0,5,4):C.UVGC_199_94,(0,5,5):C.UVGC_201_101,(0,5,7):C.UVGC_201_102,(0,6,0):C.UVGC_199_91,(0,6,1):C.UVGC_199_92,(0,6,2):C.UVGC_200_97,(0,6,3):C.UVGC_200_98,(0,6,4):C.UVGC_199_94,(0,6,5):C.UVGC_199_95,(0,6,7):C.UVGC_199_96,(0,7,0):C.UVGC_207_121,(0,7,1):C.UVGC_207_122,(0,7,2):C.UVGC_209_131,(0,7,3):C.UVGC_209_132,(0,7,4):C.UVGC_207_124,(0,7,5):C.UVGC_208_129,(0,7,7):C.UVGC_208_130,(0,2,2):C.UVGC_136_5,(0,2,3):C.UVGC_136_6,(0,4,2):C.UVGC_142_15,(0,4,3):C.UVGC_142_16,(0,4,6):C.UVGC_142_17})

V_85 = CTVertex(name = 'V_85',
                type = 'UV',
                particles = [ P.g, P.g, P.g, P.g ],
                color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u], [P.YSd], [P.YSu] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.YSd] ], [ [P.YSd], [P.YSu] ], [ [P.YSu] ] ],
                couplings = {(2,0,4):C.UVGC_138_10,(2,0,5):C.UVGC_138_9,(0,0,4):C.UVGC_138_10,(0,0,5):C.UVGC_138_9,(4,0,4):C.UVGC_137_7,(4,0,5):C.UVGC_137_8,(3,0,4):C.UVGC_137_7,(3,0,5):C.UVGC_137_8,(8,0,4):C.UVGC_138_9,(8,0,5):C.UVGC_138_10,(6,0,0):C.UVGC_217_175,(6,0,3):C.UVGC_212_150,(6,0,4):C.UVGC_218_181,(6,0,5):C.UVGC_218_182,(6,0,6):C.UVGC_217_178,(6,0,7):C.UVGC_217_179,(6,0,9):C.UVGC_217_180,(7,0,0):C.UVGC_217_175,(7,0,3):C.UVGC_212_150,(7,0,4):C.UVGC_217_176,(7,0,5):C.UVGC_217_177,(7,0,6):C.UVGC_217_178,(7,0,7):C.UVGC_217_179,(7,0,9):C.UVGC_217_180,(5,0,4):C.UVGC_137_7,(5,0,5):C.UVGC_137_8,(1,0,4):C.UVGC_137_7,(1,0,5):C.UVGC_137_8,(11,0,4):C.UVGC_141_13,(11,0,5):C.UVGC_141_14,(10,0,4):C.UVGC_141_13,(10,0,5):C.UVGC_141_14,(9,0,4):C.UVGC_140_11,(9,0,5):C.UVGC_140_12,(2,1,4):C.UVGC_138_10,(2,1,5):C.UVGC_138_9,(0,1,4):C.UVGC_138_10,(0,1,5):C.UVGC_138_9,(4,1,4):C.UVGC_137_7,(4,1,5):C.UVGC_137_8,(3,1,4):C.UVGC_137_7,(3,1,5):C.UVGC_137_8,(8,1,0):C.UVGC_219_183,(8,1,3):C.UVGC_219_184,(8,1,4):C.UVGC_219_185,(8,1,5):C.UVGC_219_186,(8,1,6):C.UVGC_219_187,(8,1,7):C.UVGC_219_188,(8,1,9):C.UVGC_219_189,(6,1,0):C.UVGC_214_158,(6,1,4):C.UVGC_216_171,(6,1,5):C.UVGC_216_172,(6,1,6):C.UVGC_214_161,(6,1,7):C.UVGC_216_173,(6,1,9):C.UVGC_216_174,(7,1,2):C.UVGC_143_18,(7,1,4):C.UVGC_144_21,(7,1,5):C.UVGC_144_22,(5,1,4):C.UVGC_137_7,(5,1,5):C.UVGC_137_8,(1,1,4):C.UVGC_137_7,(1,1,5):C.UVGC_137_8,(11,1,4):C.UVGC_141_13,(11,1,5):C.UVGC_141_14,(10,1,4):C.UVGC_141_13,(10,1,5):C.UVGC_141_14,(9,1,4):C.UVGC_140_11,(9,1,5):C.UVGC_140_12,(0,2,4):C.UVGC_138_10,(0,2,5):C.UVGC_138_9,(2,2,4):C.UVGC_138_10,(2,2,5):C.UVGC_138_9,(5,2,4):C.UVGC_137_7,(5,2,5):C.UVGC_137_8,(1,2,4):C.UVGC_137_7,(1,2,5):C.UVGC_137_8,(7,2,0):C.UVGC_214_158,(7,2,4):C.UVGC_214_159,(7,2,5):C.UVGC_214_160,(7,2,6):C.UVGC_214_161,(7,2,7):C.UVGC_214_162,(7,2,9):C.UVGC_214_163,(4,2,4):C.UVGC_137_7,(4,2,5):C.UVGC_137_8,(3,2,4):C.UVGC_137_7,(3,2,5):C.UVGC_137_8,(8,2,0):C.UVGC_215_164,(8,2,3):C.UVGC_215_165,(8,2,4):C.UVGC_215_166,(8,2,5):C.UVGC_215_167,(8,2,6):C.UVGC_215_168,(8,2,7):C.UVGC_215_169,(8,2,9):C.UVGC_215_170,(6,2,1):C.UVGC_143_18,(6,2,4):C.UVGC_143_19,(6,2,5):C.UVGC_140_11,(6,2,8):C.UVGC_143_20,(11,2,4):C.UVGC_141_13,(11,2,5):C.UVGC_141_14,(10,2,4):C.UVGC_141_13,(10,2,5):C.UVGC_141_14,(9,2,4):C.UVGC_140_11,(9,2,5):C.UVGC_140_12})

V_86 = CTVertex(name = 'V_86',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_190_66,(0,0,2):C.UVGC_190_67,(0,0,1):C.UVGC_190_68,(0,1,0):C.UVGC_192_72,(0,1,2):C.UVGC_192_73,(0,1,1):C.UVGC_192_74})

V_87 = CTVertex(name = 'V_87',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_181_52})

V_88 = CTVertex(name = 'V_88',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_180_51})

V_89 = CTVertex(name = 'V_89',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_193_75,(0,0,2):C.UVGC_193_76,(0,0,1):C.UVGC_193_77,(0,1,0):C.UVGC_189_63,(0,1,2):C.UVGC_189_64,(0,1,1):C.UVGC_189_65})

V_90 = CTVertex(name = 'V_90',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_194_78})

V_91 = CTVertex(name = 'V_91',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_195_79})

V_92 = CTVertex(name = 'V_92',
                type = 'UV',
                particles = [ P.a, P.YSd__tilde__, P.YSd ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.YSd] ] ],
                couplings = {(0,0,0):C.UVGC_151_27})

V_93 = CTVertex(name = 'V_93',
                type = 'UV',
                particles = [ P.Xm, P.d, P.YSd__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YSd] ], [ [P.g, P.YSd] ] ],
                couplings = {(0,0,0):C.UVGC_169_40,(0,0,2):C.UVGC_171_45,(0,0,1):C.UVGC_169_42})

V_94 = CTVertex(name = 'V_94',
                type = 'UV',
                particles = [ P.Xm, P.s, P.YSd__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YSd] ], [ [P.g, P.YSd] ] ],
                couplings = {(0,0,0):C.UVGC_169_40,(0,0,2):C.UVGC_171_45,(0,0,1):C.UVGC_169_42})

V_95 = CTVertex(name = 'V_95',
                type = 'UV',
                particles = [ P.Xm, P.b, P.YSd__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YSd] ], [ [P.g, P.YSd] ] ],
                couplings = {(0,0,0):C.UVGC_182_53,(0,0,2):C.UVGC_182_54,(0,0,1):C.UVGC_182_55})

V_96 = CTVertex(name = 'V_96',
                type = 'UV',
                particles = [ P.g, P.YSd__tilde__, P.YSd ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YSd] ], [ [P.t] ], [ [P.YSd] ], [ [P.YSu] ] ],
                couplings = {(0,0,0):C.UVGC_202_103,(0,0,1):C.UVGC_202_104,(0,0,2):C.UVGC_202_105,(0,0,3):C.UVGC_202_106,(0,0,5):C.UVGC_202_107,(0,0,6):C.UVGC_202_108,(0,0,7):C.UVGC_202_109,(0,0,4):C.UVGC_202_110})

V_97 = CTVertex(name = 'V_97',
                type = 'UV',
                particles = [ P.d__tilde__, P.Xm, P.YSd ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YSd] ], [ [P.g, P.YSd] ] ],
                couplings = {(0,0,0):C.UVGC_169_40,(0,0,2):C.UVGC_171_45,(0,0,1):C.UVGC_169_42})

V_98 = CTVertex(name = 'V_98',
                type = 'UV',
                particles = [ P.s__tilde__, P.Xm, P.YSd ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YSd] ], [ [P.g, P.YSd] ] ],
                couplings = {(0,0,0):C.UVGC_169_40,(0,0,2):C.UVGC_171_45,(0,0,1):C.UVGC_169_42})

V_99 = CTVertex(name = 'V_99',
                type = 'UV',
                particles = [ P.b__tilde__, P.Xm, P.YSd ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YSd] ], [ [P.g, P.YSd] ] ],
                couplings = {(0,0,0):C.UVGC_182_53,(0,0,2):C.UVGC_182_54,(0,0,1):C.UVGC_182_55})

V_100 = CTVertex(name = 'V_100',
                 type = 'UV',
                 particles = [ P.H, P.YSd__tilde__, P.YSd ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.g, P.YSd] ] ],
                 couplings = {(0,0,0):C.UVGC_156_32})

V_101 = CTVertex(name = 'V_101',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YSd__tilde__, P.YSd ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YSd] ] ],
                 couplings = {(0,0,0):C.UVGC_152_28})

V_102 = CTVertex(name = 'V_102',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YSd__tilde__, P.YSd ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YSd] ], [ [P.t] ], [ [P.YSd] ], [ [P.YSu] ] ],
                 couplings = {(0,0,0):C.UVGC_210_133,(0,0,1):C.UVGC_210_134,(0,0,2):C.UVGC_210_135,(0,0,3):C.UVGC_210_136,(0,0,5):C.UVGC_210_137,(0,0,6):C.UVGC_210_138,(0,0,7):C.UVGC_210_139,(0,0,4):C.UVGC_210_140})

V_103 = CTVertex(name = 'V_103',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YSd__tilde__, P.YSd ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YSd] ], [ [P.t] ], [ [P.YSd] ], [ [P.YSu] ] ],
                 couplings = {(2,0,0):C.UVGC_212_149,(2,0,1):C.UVGC_212_150,(2,0,2):C.UVGC_212_151,(2,0,3):C.UVGC_212_152,(2,0,5):C.UVGC_212_153,(2,0,6):C.UVGC_212_154,(2,0,7):C.UVGC_212_155,(2,0,4):C.UVGC_212_156,(1,0,0):C.UVGC_212_149,(1,0,1):C.UVGC_212_150,(1,0,2):C.UVGC_212_151,(1,0,3):C.UVGC_212_152,(1,0,5):C.UVGC_212_153,(1,0,6):C.UVGC_212_154,(1,0,7):C.UVGC_212_155,(1,0,4):C.UVGC_212_156,(0,0,2):C.UVGC_149_24,(0,0,4):C.UVGC_149_25})

V_104 = CTVertex(name = 'V_104',
                 type = 'UV',
                 particles = [ P.a, P.YSu__tilde__, P.YSu ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YSu] ] ],
                 couplings = {(0,0,0):C.UVGC_159_34})

V_105 = CTVertex(name = 'V_105',
                 type = 'UV',
                 particles = [ P.Xm, P.u, P.YSu__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YSu] ], [ [P.g, P.YSu] ] ],
                 couplings = {(0,0,0):C.UVGC_169_40,(0,0,2):C.UVGC_169_41,(0,0,1):C.UVGC_169_42})

V_106 = CTVertex(name = 'V_106',
                 type = 'UV',
                 particles = [ P.Xm, P.c, P.YSu__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YSu] ], [ [P.g, P.YSu] ] ],
                 couplings = {(0,0,0):C.UVGC_169_40,(0,0,2):C.UVGC_169_41,(0,0,1):C.UVGC_169_42})

V_107 = CTVertex(name = 'V_107',
                 type = 'UV',
                 particles = [ P.Xm, P.t, P.YSu__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YSu] ], [ [P.g, P.YSu] ] ],
                 couplings = {(0,0,0):C.UVGC_191_69,(0,0,2):C.UVGC_191_70,(0,0,1):C.UVGC_191_71})

V_108 = CTVertex(name = 'V_108',
                 type = 'UV',
                 particles = [ P.g, P.YSu__tilde__, P.YSu ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YSu] ], [ [P.t] ], [ [P.YSd] ], [ [P.YSu] ] ],
                 couplings = {(0,0,0):C.UVGC_202_103,(0,0,1):C.UVGC_202_104,(0,0,2):C.UVGC_202_105,(0,0,3):C.UVGC_202_106,(0,0,5):C.UVGC_202_107,(0,0,6):C.UVGC_202_108,(0,0,7):C.UVGC_202_109,(0,0,4):C.UVGC_203_111})

V_109 = CTVertex(name = 'V_109',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.Xm, P.YSu ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YSu] ], [ [P.g, P.YSu] ] ],
                 couplings = {(0,0,0):C.UVGC_169_40,(0,0,2):C.UVGC_169_41,(0,0,1):C.UVGC_169_42})

V_110 = CTVertex(name = 'V_110',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.Xm, P.YSu ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YSu] ], [ [P.g, P.YSu] ] ],
                 couplings = {(0,0,0):C.UVGC_169_40,(0,0,2):C.UVGC_169_41,(0,0,1):C.UVGC_169_42})

V_111 = CTVertex(name = 'V_111',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.Xm, P.YSu ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS4 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YSu] ], [ [P.g, P.YSu] ] ],
                 couplings = {(0,0,0):C.UVGC_191_69,(0,0,2):C.UVGC_191_70,(0,0,1):C.UVGC_191_71})

V_112 = CTVertex(name = 'V_112',
                 type = 'UV',
                 particles = [ P.H, P.YSu__tilde__, P.YSu ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.SSS1 ],
                 loop_particles = [ [ [P.g, P.YSu] ] ],
                 couplings = {(0,0,0):C.UVGC_164_39})

V_113 = CTVertex(name = 'V_113',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YSu__tilde__, P.YSu ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YSu] ] ],
                 couplings = {(0,0,0):C.UVGC_160_35})

V_114 = CTVertex(name = 'V_114',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YSu__tilde__, P.YSu ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YSu] ], [ [P.t] ], [ [P.YSd] ], [ [P.YSu] ] ],
                 couplings = {(0,0,0):C.UVGC_211_141,(0,0,1):C.UVGC_211_142,(0,0,2):C.UVGC_211_143,(0,0,3):C.UVGC_211_144,(0,0,5):C.UVGC_211_145,(0,0,6):C.UVGC_211_146,(0,0,7):C.UVGC_211_147,(0,0,4):C.UVGC_211_148})

V_115 = CTVertex(name = 'V_115',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YSu__tilde__, P.YSu ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YSu] ], [ [P.t] ], [ [P.YSd] ], [ [P.YSu] ] ],
                 couplings = {(2,0,0):C.UVGC_212_149,(2,0,1):C.UVGC_212_150,(2,0,2):C.UVGC_212_151,(2,0,3):C.UVGC_212_152,(2,0,5):C.UVGC_212_153,(2,0,6):C.UVGC_212_154,(2,0,7):C.UVGC_212_155,(2,0,4):C.UVGC_213_157,(1,0,0):C.UVGC_212_149,(1,0,1):C.UVGC_212_150,(1,0,2):C.UVGC_212_151,(1,0,3):C.UVGC_212_152,(1,0,5):C.UVGC_212_153,(1,0,6):C.UVGC_212_154,(1,0,7):C.UVGC_212_155,(1,0,4):C.UVGC_213_157,(0,0,2):C.UVGC_149_24,(0,0,4):C.UVGC_149_25})

V_116 = CTVertex(name = 'V_116',
                 type = 'UV',
                 particles = [ P.Z, P.YSd__tilde__, P.YSd ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YSd] ] ],
                 couplings = {(0,0,0):C.UVGC_153_29})

V_117 = CTVertex(name = 'V_117',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YSd__tilde__, P.YSd ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YSd] ] ],
                 couplings = {(0,0,0):C.UVGC_154_30})

V_118 = CTVertex(name = 'V_118',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YSd__tilde__, P.YSd ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YSd] ], [ [P.t] ], [ [P.YSd] ], [ [P.YSu] ] ],
                 couplings = {(0,0,0):C.UVGC_220_190,(0,0,1):C.UVGC_220_191,(0,0,2):C.UVGC_220_192,(0,0,3):C.UVGC_220_193,(0,0,5):C.UVGC_220_194,(0,0,6):C.UVGC_220_195,(0,0,7):C.UVGC_220_196,(0,0,4):C.UVGC_220_197})

V_119 = CTVertex(name = 'V_119',
                 type = 'UV',
                 particles = [ P.Z, P.YSu__tilde__, P.YSu ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YSu] ] ],
                 couplings = {(0,0,0):C.UVGC_161_36})

V_120 = CTVertex(name = 'V_120',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YSu__tilde__, P.YSu ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YSu] ] ],
                 couplings = {(0,0,0):C.UVGC_162_37})

V_121 = CTVertex(name = 'V_121',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YSu__tilde__, P.YSu ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YSu] ], [ [P.t] ], [ [P.YSd] ], [ [P.YSu] ] ],
                 couplings = {(0,0,0):C.UVGC_221_198,(0,0,1):C.UVGC_221_199,(0,0,2):C.UVGC_221_200,(0,0,3):C.UVGC_221_201,(0,0,5):C.UVGC_221_202,(0,0,6):C.UVGC_221_203,(0,0,7):C.UVGC_221_204,(0,0,4):C.UVGC_221_205})

V_122 = CTVertex(name = 'V_122',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YSd__tilde__, P.YSd ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YSd] ] ],
                 couplings = {(0,0,0):C.UVGC_155_31})

V_123 = CTVertex(name = 'V_123',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YSu__tilde__, P.YSu ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YSu] ] ],
                 couplings = {(0,0,0):C.UVGC_163_38})

V_124 = CTVertex(name = 'V_124',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV4 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_125_2})

V_125 = CTVertex(name = 'V_125',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV4 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_125_2})

V_126 = CTVertex(name = 'V_126',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV6 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_125_2,(0,1,0):C.UVGC_184_57})

V_127 = CTVertex(name = 'V_127',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV4 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_128_4})

V_128 = CTVertex(name = 'V_128',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV4 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_128_4})

V_129 = CTVertex(name = 'V_129',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV6 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_128_4,(0,1,0):C.UVGC_176_47})

V_130 = CTVertex(name = 'V_130',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV5, L.FFV6 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.t] ], [ [P.YSd] ], [ [P.YSu] ] ],
                 couplings = {(0,0,4):C.UVGC_126_3,(0,1,0):C.UVGC_204_112,(0,1,1):C.UVGC_204_113,(0,1,2):C.UVGC_204_114,(0,1,3):C.UVGC_204_115,(0,1,5):C.UVGC_204_116,(0,1,6):C.UVGC_204_117,(0,1,7):C.UVGC_204_118})

V_131 = CTVertex(name = 'V_131',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV5, L.FFV6 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.c, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.YSd] ], [ [P.YSu] ] ],
                 couplings = {(0,0,2):C.UVGC_126_3,(0,1,0):C.UVGC_204_112,(0,1,1):C.UVGC_204_113,(0,1,3):C.UVGC_204_114,(0,1,4):C.UVGC_204_115,(0,1,5):C.UVGC_204_116,(0,1,6):C.UVGC_204_117,(0,1,7):C.UVGC_204_118})

V_132 = CTVertex(name = 'V_132',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV6 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.t] ], [ [P.YSd] ], [ [P.YSu] ] ],
                 couplings = {(0,0,4):C.UVGC_126_3,(0,1,0):C.UVGC_204_112,(0,1,1):C.UVGC_204_113,(0,1,2):C.UVGC_204_114,(0,1,3):C.UVGC_204_115,(0,1,5):C.UVGC_204_116,(0,1,6):C.UVGC_204_117,(0,1,7):C.UVGC_204_118,(0,1,4):C.UVGC_206_120})

V_133 = CTVertex(name = 'V_133',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV5, L.FFV6 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.YSd] ], [ [P.YSu] ] ],
                 couplings = {(0,0,2):C.UVGC_126_3,(0,1,0):C.UVGC_204_112,(0,1,1):C.UVGC_204_113,(0,1,3):C.UVGC_204_114,(0,1,4):C.UVGC_204_115,(0,1,5):C.UVGC_204_116,(0,1,6):C.UVGC_204_117,(0,1,7):C.UVGC_204_118})

V_134 = CTVertex(name = 'V_134',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV5, L.FFV6 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.t] ], [ [P.YSd] ], [ [P.YSu] ] ],
                 couplings = {(0,0,4):C.UVGC_126_3,(0,1,0):C.UVGC_204_112,(0,1,1):C.UVGC_204_113,(0,1,2):C.UVGC_204_114,(0,1,3):C.UVGC_204_115,(0,1,5):C.UVGC_204_116,(0,1,6):C.UVGC_204_117,(0,1,7):C.UVGC_204_118})

V_135 = CTVertex(name = 'V_135',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV6 ],
                 loop_particles = [ [ [P.b] ], [ [P.b, P.g] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.YSd] ], [ [P.YSu] ] ],
                 couplings = {(0,0,1):C.UVGC_126_3,(0,1,0):C.UVGC_204_112,(0,1,2):C.UVGC_204_113,(0,1,3):C.UVGC_204_114,(0,1,4):C.UVGC_204_115,(0,1,5):C.UVGC_204_116,(0,1,6):C.UVGC_204_117,(0,1,7):C.UVGC_204_118,(0,1,1):C.UVGC_205_119})

V_136 = CTVertex(name = 'V_136',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_170_43,(0,0,1):C.UVGC_170_44})

V_137 = CTVertex(name = 'V_137',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_170_43,(0,0,1):C.UVGC_170_44})

V_138 = CTVertex(name = 'V_138',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_186_59,(0,0,2):C.UVGC_186_60,(0,0,1):C.UVGC_170_44})

V_139 = CTVertex(name = 'V_139',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_170_43,(0,0,1):C.UVGC_170_44})

V_140 = CTVertex(name = 'V_140',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_170_43,(0,0,1):C.UVGC_170_44})

V_141 = CTVertex(name = 'V_141',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_186_59,(0,0,2):C.UVGC_186_60,(0,0,1):C.UVGC_170_44})

V_142 = CTVertex(name = 'V_142',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_187_61,(0,1,0):C.UVGC_188_62})

V_143 = CTVertex(name = 'V_143',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_178_49,(0,1,0):C.UVGC_179_50})

V_144 = CTVertex(name = 'V_144',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_147_23,(0,1,0):C.UVGC_124_1,(0,2,0):C.UVGC_124_1})

V_145 = CTVertex(name = 'V_145',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_147_23,(0,1,0):C.UVGC_124_1,(0,2,0):C.UVGC_124_1})

V_146 = CTVertex(name = 'V_146',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_185_58,(0,2,0):C.UVGC_185_58,(0,1,0):C.UVGC_183_56,(0,3,0):C.UVGC_183_56})

V_147 = CTVertex(name = 'V_147',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_147_23,(0,1,0):C.UVGC_124_1,(0,2,0):C.UVGC_124_1})

V_148 = CTVertex(name = 'V_148',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_147_23,(0,1,0):C.UVGC_124_1,(0,2,0):C.UVGC_124_1})

V_149 = CTVertex(name = 'V_149',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_177_48,(0,2,0):C.UVGC_177_48,(0,1,0):C.UVGC_175_46,(0,3,0):C.UVGC_175_46})

V_150 = CTVertex(name = 'V_150',
                 type = 'UV',
                 particles = [ P.YSu__tilde__, P.YSu ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YSu] ] ],
                 couplings = {(0,0,0):C.UVGC_222_206,(0,1,0):C.UVGC_158_33})

V_151 = CTVertex(name = 'V_151',
                 type = 'UV',
                 particles = [ P.YSd__tilde__, P.YSd ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YSd] ] ],
                 couplings = {(0,0,0):C.UVGC_196_80,(0,1,0):C.UVGC_150_26})

V_152 = CTVertex(name = 'V_152',
                 type = 'UV',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.YSd] ], [ [P.YSu] ] ],
                 couplings = {(0,0,0):C.UVGC_198_85,(0,0,1):C.UVGC_198_86,(0,0,2):C.UVGC_198_87,(0,0,3):C.UVGC_198_88,(0,0,4):C.UVGC_198_89,(0,0,5):C.UVGC_198_90,(0,1,0):C.UVGC_197_81,(0,1,3):C.UVGC_197_82,(0,1,4):C.UVGC_197_83,(0,1,5):C.UVGC_197_84})

