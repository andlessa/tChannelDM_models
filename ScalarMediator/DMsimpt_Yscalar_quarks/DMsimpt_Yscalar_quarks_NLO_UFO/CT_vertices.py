# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.3.1 for Linux x86 (64-bit) (July 24, 2023)
# Date: Wed 11 Nov 2026 15:27:11


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
               couplings = {(0,0,0):C.R2GC_173_46,(0,0,1):C.R2GC_173_47,(0,1,0):C.R2GC_184_49,(0,1,1):C.R2GC_184_50,(0,2,0):C.R2GC_184_49,(0,2,1):C.R2GC_184_50,(0,3,0):C.R2GC_173_46,(0,3,1):C.R2GC_173_47,(0,4,0):C.R2GC_173_46,(0,4,1):C.R2GC_173_47,(0,5,0):C.R2GC_184_49,(0,5,1):C.R2GC_184_50})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(2,0,0):C.R2GC_115_9,(2,0,1):C.R2GC_115_10,(0,0,0):C.R2GC_115_9,(0,0,1):C.R2GC_115_10,(4,0,0):C.R2GC_113_5,(4,0,1):C.R2GC_113_6,(3,0,0):C.R2GC_113_5,(3,0,1):C.R2GC_113_6,(8,0,0):C.R2GC_114_7,(8,0,1):C.R2GC_114_8,(6,0,0):C.R2GC_119_14,(6,0,1):C.R2GC_193_58,(7,0,0):C.R2GC_120_16,(7,0,1):C.R2GC_192_57,(5,0,0):C.R2GC_113_5,(5,0,1):C.R2GC_113_6,(1,0,0):C.R2GC_113_5,(1,0,1):C.R2GC_113_6,(11,0,0):C.R2GC_117_12,(11,0,1):C.R2GC_117_13,(10,0,0):C.R2GC_117_12,(10,0,1):C.R2GC_117_13,(9,0,1):C.R2GC_116_11,(2,1,0):C.R2GC_115_9,(2,1,1):C.R2GC_115_10,(0,1,0):C.R2GC_115_9,(0,1,1):C.R2GC_115_10,(4,1,0):C.R2GC_113_5,(4,1,1):C.R2GC_113_6,(3,1,0):C.R2GC_113_5,(3,1,1):C.R2GC_113_6,(8,1,0):C.R2GC_114_7,(8,1,1):C.R2GC_194_59,(6,1,0):C.R2GC_191_55,(6,1,1):C.R2GC_191_56,(7,1,0):C.R2GC_120_16,(7,1,1):C.R2GC_120_17,(5,1,0):C.R2GC_113_5,(5,1,1):C.R2GC_113_6,(1,1,0):C.R2GC_113_5,(1,1,1):C.R2GC_113_6,(11,1,0):C.R2GC_117_12,(11,1,1):C.R2GC_117_13,(10,1,0):C.R2GC_117_12,(10,1,1):C.R2GC_117_13,(9,1,1):C.R2GC_116_11,(0,2,0):C.R2GC_115_9,(0,2,1):C.R2GC_115_10,(2,2,0):C.R2GC_115_9,(2,2,1):C.R2GC_115_10,(5,2,0):C.R2GC_113_5,(5,2,1):C.R2GC_113_6,(1,2,0):C.R2GC_113_5,(1,2,1):C.R2GC_113_6,(7,2,0):C.R2GC_189_53,(7,2,1):C.R2GC_115_10,(4,2,0):C.R2GC_113_5,(4,2,1):C.R2GC_113_6,(3,2,0):C.R2GC_113_5,(3,2,1):C.R2GC_113_6,(8,2,0):C.R2GC_114_7,(8,2,1):C.R2GC_190_54,(6,2,0):C.R2GC_119_14,(6,2,1):C.R2GC_119_15,(11,2,0):C.R2GC_117_12,(11,2,1):C.R2GC_117_13,(10,2,0):C.R2GC_117_12,(10,2,1):C.R2GC_117_13,(9,2,1):C.R2GC_116_11})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.t__tilde__, P.b, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS5 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_164_36,(0,1,0):C.R2GC_166_38})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_155_31})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_154_30})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.b__tilde__, P.t, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS5 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_167_39,(0,1,0):C.R2GC_163_35})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_168_40})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_169_41})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.Xm, P.d, P.YSd__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS3 ],
               loop_particles = [ [ [P.d, P.g, P.YSd] ] ],
               couplings = {(0,0,0):C.R2GC_143_26})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.Xm, P.s, P.YSd__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.YSd] ] ],
                couplings = {(0,0,0):C.R2GC_143_26})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.Xm, P.b, P.YSd__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g, P.YSd] ] ],
                couplings = {(0,0,0):C.R2GC_156_32})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.g, P.YSd__tilde__, P.YSd ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.YSd] ] ],
                couplings = {(0,0,0):C.R2GC_176_48})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.d__tilde__, P.Xm, P.YSd ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.YSd] ] ],
                couplings = {(0,0,0):C.R2GC_143_26})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.s__tilde__, P.Xm, P.YSd ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.s, P.YSd] ] ],
                couplings = {(0,0,0):C.R2GC_143_26})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.b__tilde__, P.Xm, P.YSd ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.YSd] ] ],
                couplings = {(0,0,0):C.R2GC_156_32})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.H, P.YSd__tilde__, P.YSd ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                loop_particles = [ [ [P.g, P.YSd] ] ],
                couplings = {(0,0,0):C.R2GC_131_24})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.g, P.g, P.YSd__tilde__, P.YSd ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g] ], [ [P.g, P.YSd] ] ],
                couplings = {(2,0,0):C.R2GC_187_51,(2,0,1):C.R2GC_187_52,(1,0,0):C.R2GC_187_51,(1,0,1):C.R2GC_187_52,(0,0,0):C.R2GC_117_13,(0,0,1):C.R2GC_129_22})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.Xm, P.u, P.YSu__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.u, P.YSu] ] ],
                couplings = {(0,0,0):C.R2GC_143_26})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.Xm, P.c, P.YSu__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.c, P.g, P.YSu] ] ],
                couplings = {(0,0,0):C.R2GC_143_26})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.Xm, P.t, P.YSu__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.t, P.YSu] ] ],
                couplings = {(0,0,0):C.R2GC_165_37})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.g, P.YSu__tilde__, P.YSu ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.YSu] ] ],
                couplings = {(0,0,0):C.R2GC_176_48})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.u__tilde__, P.Xm, P.YSu ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.u, P.YSu] ] ],
                couplings = {(0,0,0):C.R2GC_143_26})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.c__tilde__, P.Xm, P.YSu ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.YSu] ] ],
                couplings = {(0,0,0):C.R2GC_143_26})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.t__tilde__, P.Xm, P.YSu ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.YSu] ] ],
                couplings = {(0,0,0):C.R2GC_165_37})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.H, P.YSu__tilde__, P.YSu ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                loop_particles = [ [ [P.g, P.YSu] ] ],
                couplings = {(0,0,0):C.R2GC_134_25})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.g, P.g, P.YSu__tilde__, P.YSu ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g] ], [ [P.g, P.YSu] ] ],
                couplings = {(2,0,0):C.R2GC_187_51,(2,0,1):C.R2GC_187_52,(1,0,0):C.R2GC_187_51,(1,0,1):C.R2GC_187_52,(0,0,0):C.R2GC_117_13,(0,0,1):C.R2GC_129_22})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_124_21})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_124_21})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_124_21})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_121_18})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_121_18})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_121_18})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_122_19})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_122_19})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_122_19})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_122_19})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_122_19})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_122_19})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_144_27})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_144_27})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_144_27})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_144_27})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_144_27})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_144_27})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_103_4,(0,1,0):C.R2GC_162_34})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_103_4,(0,1,0):C.R2GC_162_34})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_103_4,(0,1,0):C.R2GC_162_34})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_100_1,(0,1,0):C.R2GC_153_29})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_100_1,(0,1,0):C.R2GC_153_29})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_100_1,(0,1,0):C.R2GC_153_29})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_123_20})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_123_20})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_159_33,(0,2,0):C.R2GC_159_33,(0,1,0):C.R2GC_123_20,(0,3,0):C.R2GC_123_20})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_123_20})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_123_20})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_151_28,(0,2,0):C.R2GC_151_28,(0,1,0):C.R2GC_123_20,(0,3,0):C.R2GC_123_20})

V_57 = CTVertex(name = 'V_57',
                type = 'R2',
                particles = [ P.YSu__tilde__, P.YSu ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SS1, L.SS2 ],
                loop_particles = [ [ [P.g, P.YSu] ] ],
                couplings = {(0,0,0):C.R2GC_195_60,(0,1,0):C.R2GC_130_23})

V_58 = CTVertex(name = 'V_58',
                type = 'R2',
                particles = [ P.YSd__tilde__, P.YSd ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SS1, L.SS2 ],
                loop_particles = [ [ [P.g, P.YSd] ] ],
                couplings = {(0,0,0):C.R2GC_170_42,(0,1,0):C.R2GC_130_23})

V_59 = CTVertex(name = 'V_59',
                type = 'R2',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV2, L.VV3 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ], [ [P.t] ] ],
                couplings = {(0,0,2):C.R2GC_172_45,(0,1,0):C.R2GC_89_61,(0,1,3):C.R2GC_89_62,(0,2,1):C.R2GC_171_43,(0,2,2):C.R2GC_171_44})

V_60 = CTVertex(name = 'V_60',
                type = 'R2',
                particles = [ P.g, P.g, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_90_63,(0,0,1):C.R2GC_90_64})

V_61 = CTVertex(name = 'V_61',
                type = 'R2',
                particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_102_3,(0,1,0):C.R2GC_102_3,(0,2,0):C.R2GC_102_3})

V_62 = CTVertex(name = 'V_62',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Z ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_94_71,(0,0,1):C.R2GC_94_72,(0,1,0):C.R2GC_94_71,(0,1,1):C.R2GC_94_72,(0,2,0):C.R2GC_94_71,(0,2,1):C.R2GC_94_72})

V_63 = CTVertex(name = 'V_63',
                type = 'R2',
                particles = [ P.g, P.g, P.Z, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_97_77,(0,0,1):C.R2GC_97_78,(0,1,0):C.R2GC_97_77,(0,1,1):C.R2GC_97_78,(0,2,0):C.R2GC_97_77,(0,2,1):C.R2GC_97_78})

V_64 = CTVertex(name = 'V_64',
                type = 'R2',
                particles = [ P.a, P.a, P.g, P.g ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_92_67,(0,0,1):C.R2GC_92_68,(0,1,0):C.R2GC_92_67,(0,1,1):C.R2GC_92_68,(0,2,0):C.R2GC_92_67,(0,2,1):C.R2GC_92_68})

V_65 = CTVertex(name = 'V_65',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Z ],
                color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(1,0,0):C.R2GC_96_75,(1,0,1):C.R2GC_96_76,(0,1,0):C.R2GC_95_73,(0,1,1):C.R2GC_95_74,(0,2,0):C.R2GC_95_73,(0,2,1):C.R2GC_95_74,(0,3,0):C.R2GC_95_73,(0,3,1):C.R2GC_95_74})

V_66 = CTVertex(name = 'V_66',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.g ],
                color = [ 'd(2,3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_93_69,(0,0,1):C.R2GC_93_70,(0,1,0):C.R2GC_93_69,(0,1,1):C.R2GC_93_70,(0,2,0):C.R2GC_93_69,(0,2,1):C.R2GC_93_70})

V_67 = CTVertex(name = 'V_67',
                type = 'R2',
                particles = [ P.g, P.g, P.H, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_91_65,(0,0,1):C.R2GC_91_66})

V_68 = CTVertex(name = 'V_68',
                type = 'R2',
                particles = [ P.g, P.g, P.G0, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_91_65,(0,0,1):C.R2GC_91_66})

V_69 = CTVertex(name = 'V_69',
                type = 'R2',
                particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_101_2})

V_70 = CTVertex(name = 'V_70',
                type = 'UV',
                particles = [ P.g, P.g, P.g ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVV1, L.VVV2, L.VVV3, L.VVV4, L.VVV5, L.VVV6, L.VVV7, L.VVV8 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.YSd] ], [ [P.YSd], [P.YSu] ], [ [P.YSu] ] ],
                couplings = {(0,0,0):C.UVGC_173_83,(0,0,1):C.UVGC_173_84,(0,0,2):C.UVGC_173_85,(0,0,3):C.UVGC_118_15,(0,0,4):C.UVGC_173_86,(0,0,5):C.UVGC_173_87,(0,0,7):C.UVGC_173_88,(0,1,0):C.UVGC_184_114,(0,1,1):C.UVGC_184_115,(0,1,2):C.UVGC_185_120,(0,1,3):C.UVGC_185_121,(0,1,4):C.UVGC_184_117,(0,1,5):C.UVGC_185_122,(0,1,7):C.UVGC_185_123,(0,3,0):C.UVGC_184_114,(0,3,1):C.UVGC_184_115,(0,3,2):C.UVGC_184_116,(0,3,3):C.UVGC_112_5,(0,3,4):C.UVGC_184_117,(0,3,5):C.UVGC_184_118,(0,3,7):C.UVGC_184_119,(0,5,0):C.UVGC_173_83,(0,5,1):C.UVGC_173_84,(0,5,2):C.UVGC_175_91,(0,5,3):C.UVGC_175_92,(0,5,4):C.UVGC_173_86,(0,5,5):C.UVGC_175_93,(0,5,7):C.UVGC_175_94,(0,6,0):C.UVGC_173_83,(0,6,1):C.UVGC_173_84,(0,6,2):C.UVGC_174_89,(0,6,3):C.UVGC_174_90,(0,6,4):C.UVGC_173_86,(0,6,5):C.UVGC_173_87,(0,6,7):C.UVGC_173_88,(0,7,0):C.UVGC_184_114,(0,7,1):C.UVGC_184_115,(0,7,2):C.UVGC_186_124,(0,7,3):C.UVGC_186_125,(0,7,4):C.UVGC_184_117,(0,7,5):C.UVGC_185_122,(0,7,7):C.UVGC_185_123,(0,2,2):C.UVGC_112_4,(0,2,3):C.UVGC_112_5,(0,4,2):C.UVGC_118_14,(0,4,3):C.UVGC_118_15,(0,4,6):C.UVGC_118_16})

V_71 = CTVertex(name = 'V_71',
                type = 'UV',
                particles = [ P.g, P.g, P.g, P.g ],
                color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u], [P.YSd], [P.YSu] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.YSd] ], [ [P.YSd], [P.YSu] ], [ [P.YSu] ] ],
                couplings = {(2,0,4):C.UVGC_114_9,(2,0,5):C.UVGC_114_8,(0,0,4):C.UVGC_114_9,(0,0,5):C.UVGC_114_8,(4,0,4):C.UVGC_113_6,(4,0,5):C.UVGC_113_7,(3,0,4):C.UVGC_113_6,(3,0,5):C.UVGC_113_7,(8,0,4):C.UVGC_114_8,(8,0,5):C.UVGC_114_9,(6,0,0):C.UVGC_192_152,(6,0,3):C.UVGC_187_127,(6,0,4):C.UVGC_193_158,(6,0,5):C.UVGC_193_159,(6,0,6):C.UVGC_192_155,(6,0,7):C.UVGC_192_156,(6,0,9):C.UVGC_192_157,(7,0,0):C.UVGC_192_152,(7,0,3):C.UVGC_187_127,(7,0,4):C.UVGC_192_153,(7,0,5):C.UVGC_192_154,(7,0,6):C.UVGC_192_155,(7,0,7):C.UVGC_192_156,(7,0,9):C.UVGC_192_157,(5,0,4):C.UVGC_113_6,(5,0,5):C.UVGC_113_7,(1,0,4):C.UVGC_113_6,(1,0,5):C.UVGC_113_7,(11,0,4):C.UVGC_117_12,(11,0,5):C.UVGC_117_13,(10,0,4):C.UVGC_117_12,(10,0,5):C.UVGC_117_13,(9,0,4):C.UVGC_116_10,(9,0,5):C.UVGC_116_11,(2,1,4):C.UVGC_114_9,(2,1,5):C.UVGC_114_8,(0,1,4):C.UVGC_114_9,(0,1,5):C.UVGC_114_8,(4,1,4):C.UVGC_113_6,(4,1,5):C.UVGC_113_7,(3,1,4):C.UVGC_113_6,(3,1,5):C.UVGC_113_7,(8,1,0):C.UVGC_194_160,(8,1,3):C.UVGC_194_161,(8,1,4):C.UVGC_194_162,(8,1,5):C.UVGC_194_163,(8,1,6):C.UVGC_194_164,(8,1,7):C.UVGC_194_165,(8,1,9):C.UVGC_194_166,(6,1,0):C.UVGC_189_135,(6,1,4):C.UVGC_191_148,(6,1,5):C.UVGC_191_149,(6,1,6):C.UVGC_189_138,(6,1,7):C.UVGC_191_150,(6,1,9):C.UVGC_191_151,(7,1,2):C.UVGC_119_17,(7,1,4):C.UVGC_120_20,(7,1,5):C.UVGC_120_21,(5,1,4):C.UVGC_113_6,(5,1,5):C.UVGC_113_7,(1,1,4):C.UVGC_113_6,(1,1,5):C.UVGC_113_7,(11,1,4):C.UVGC_117_12,(11,1,5):C.UVGC_117_13,(10,1,4):C.UVGC_117_12,(10,1,5):C.UVGC_117_13,(9,1,4):C.UVGC_116_10,(9,1,5):C.UVGC_116_11,(0,2,4):C.UVGC_114_9,(0,2,5):C.UVGC_114_8,(2,2,4):C.UVGC_114_9,(2,2,5):C.UVGC_114_8,(5,2,4):C.UVGC_113_6,(5,2,5):C.UVGC_113_7,(1,2,4):C.UVGC_113_6,(1,2,5):C.UVGC_113_7,(7,2,0):C.UVGC_189_135,(7,2,4):C.UVGC_189_136,(7,2,5):C.UVGC_189_137,(7,2,6):C.UVGC_189_138,(7,2,7):C.UVGC_189_139,(7,2,9):C.UVGC_189_140,(4,2,4):C.UVGC_113_6,(4,2,5):C.UVGC_113_7,(3,2,4):C.UVGC_113_6,(3,2,5):C.UVGC_113_7,(8,2,0):C.UVGC_190_141,(8,2,3):C.UVGC_190_142,(8,2,4):C.UVGC_190_143,(8,2,5):C.UVGC_190_144,(8,2,6):C.UVGC_190_145,(8,2,7):C.UVGC_190_146,(8,2,9):C.UVGC_190_147,(6,2,1):C.UVGC_119_17,(6,2,4):C.UVGC_119_18,(6,2,5):C.UVGC_116_10,(6,2,8):C.UVGC_119_19,(11,2,4):C.UVGC_117_12,(11,2,5):C.UVGC_117_13,(10,2,4):C.UVGC_117_12,(10,2,5):C.UVGC_117_13,(9,2,4):C.UVGC_116_10,(9,2,5):C.UVGC_116_11})

V_72 = CTVertex(name = 'V_72',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_164_58,(0,0,2):C.UVGC_164_59,(0,0,1):C.UVGC_164_60,(0,1,0):C.UVGC_166_64,(0,1,2):C.UVGC_166_65,(0,1,1):C.UVGC_166_66})

V_73 = CTVertex(name = 'V_73',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_155_44})

V_74 = CTVertex(name = 'V_74',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_154_43})

V_75 = CTVertex(name = 'V_75',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_167_67,(0,0,2):C.UVGC_167_68,(0,0,1):C.UVGC_167_69,(0,1,0):C.UVGC_163_55,(0,1,2):C.UVGC_163_56,(0,1,1):C.UVGC_163_57})

V_76 = CTVertex(name = 'V_76',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_168_70})

V_77 = CTVertex(name = 'V_77',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_169_71})

V_78 = CTVertex(name = 'V_78',
                type = 'UV',
                particles = [ P.Xm, P.d, P.YSd__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YSd] ], [ [P.g, P.YSd] ] ],
                couplings = {(0,0,0):C.UVGC_143_32,(0,0,2):C.UVGC_145_37,(0,0,1):C.UVGC_143_34})

V_79 = CTVertex(name = 'V_79',
                type = 'UV',
                particles = [ P.Xm, P.s, P.YSd__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YSd] ], [ [P.g, P.YSd] ] ],
                couplings = {(0,0,0):C.UVGC_143_32,(0,0,2):C.UVGC_145_37,(0,0,1):C.UVGC_143_34})

V_80 = CTVertex(name = 'V_80',
                type = 'UV',
                particles = [ P.Xm, P.b, P.YSd__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YSd] ], [ [P.g, P.YSd] ] ],
                couplings = {(0,0,0):C.UVGC_156_45,(0,0,2):C.UVGC_156_46,(0,0,1):C.UVGC_156_47})

V_81 = CTVertex(name = 'V_81',
                type = 'UV',
                particles = [ P.g, P.YSd__tilde__, P.YSd ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YSd] ], [ [P.t] ], [ [P.YSd] ], [ [P.YSu] ] ],
                couplings = {(0,0,0):C.UVGC_176_95,(0,0,1):C.UVGC_176_96,(0,0,2):C.UVGC_176_97,(0,0,3):C.UVGC_176_98,(0,0,5):C.UVGC_176_99,(0,0,6):C.UVGC_176_100,(0,0,7):C.UVGC_176_101,(0,0,4):C.UVGC_176_102})

V_82 = CTVertex(name = 'V_82',
                type = 'UV',
                particles = [ P.d__tilde__, P.Xm, P.YSd ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YSd] ], [ [P.g, P.YSd] ] ],
                couplings = {(0,0,0):C.UVGC_143_32,(0,0,2):C.UVGC_145_37,(0,0,1):C.UVGC_143_34})

V_83 = CTVertex(name = 'V_83',
                type = 'UV',
                particles = [ P.s__tilde__, P.Xm, P.YSd ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YSd] ], [ [P.g, P.YSd] ] ],
                couplings = {(0,0,0):C.UVGC_143_32,(0,0,2):C.UVGC_145_37,(0,0,1):C.UVGC_143_34})

V_84 = CTVertex(name = 'V_84',
                type = 'UV',
                particles = [ P.b__tilde__, P.Xm, P.YSd ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YSd] ], [ [P.g, P.YSd] ] ],
                couplings = {(0,0,0):C.UVGC_156_45,(0,0,2):C.UVGC_156_46,(0,0,1):C.UVGC_156_47})

V_85 = CTVertex(name = 'V_85',
                type = 'UV',
                particles = [ P.H, P.YSd__tilde__, P.YSd ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                loop_particles = [ [ [P.g, P.YSd] ] ],
                couplings = {(0,0,0):C.UVGC_131_29})

V_86 = CTVertex(name = 'V_86',
                type = 'UV',
                particles = [ P.g, P.g, P.YSd__tilde__, P.YSd ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YSd] ], [ [P.t] ], [ [P.YSd] ], [ [P.YSu] ] ],
                couplings = {(2,0,0):C.UVGC_187_126,(2,0,1):C.UVGC_187_127,(2,0,2):C.UVGC_187_128,(2,0,3):C.UVGC_187_129,(2,0,5):C.UVGC_187_130,(2,0,6):C.UVGC_187_131,(2,0,7):C.UVGC_187_132,(2,0,4):C.UVGC_187_133,(1,0,0):C.UVGC_187_126,(1,0,1):C.UVGC_187_127,(1,0,2):C.UVGC_187_128,(1,0,3):C.UVGC_187_129,(1,0,5):C.UVGC_187_130,(1,0,6):C.UVGC_187_131,(1,0,7):C.UVGC_187_132,(1,0,4):C.UVGC_187_133,(0,0,2):C.UVGC_129_26,(0,0,4):C.UVGC_129_27})

V_87 = CTVertex(name = 'V_87',
                type = 'UV',
                particles = [ P.Xm, P.u, P.YSu__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YSu] ], [ [P.g, P.YSu] ] ],
                couplings = {(0,0,0):C.UVGC_143_32,(0,0,2):C.UVGC_143_33,(0,0,1):C.UVGC_143_34})

V_88 = CTVertex(name = 'V_88',
                type = 'UV',
                particles = [ P.Xm, P.c, P.YSu__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YSu] ], [ [P.g, P.YSu] ] ],
                couplings = {(0,0,0):C.UVGC_143_32,(0,0,2):C.UVGC_143_33,(0,0,1):C.UVGC_143_34})

V_89 = CTVertex(name = 'V_89',
                type = 'UV',
                particles = [ P.Xm, P.t, P.YSu__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YSu] ], [ [P.g, P.YSu] ] ],
                couplings = {(0,0,0):C.UVGC_165_61,(0,0,2):C.UVGC_165_62,(0,0,1):C.UVGC_165_63})

V_90 = CTVertex(name = 'V_90',
                type = 'UV',
                particles = [ P.g, P.YSu__tilde__, P.YSu ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YSu] ], [ [P.t] ], [ [P.YSd] ], [ [P.YSu] ] ],
                couplings = {(0,0,0):C.UVGC_176_95,(0,0,1):C.UVGC_176_96,(0,0,2):C.UVGC_176_97,(0,0,3):C.UVGC_176_98,(0,0,5):C.UVGC_176_99,(0,0,6):C.UVGC_176_100,(0,0,7):C.UVGC_176_101,(0,0,4):C.UVGC_177_103})

V_91 = CTVertex(name = 'V_91',
                type = 'UV',
                particles = [ P.u__tilde__, P.Xm, P.YSu ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YSu] ], [ [P.g, P.YSu] ] ],
                couplings = {(0,0,0):C.UVGC_143_32,(0,0,2):C.UVGC_143_33,(0,0,1):C.UVGC_143_34})

V_92 = CTVertex(name = 'V_92',
                type = 'UV',
                particles = [ P.c__tilde__, P.Xm, P.YSu ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YSu] ], [ [P.g, P.YSu] ] ],
                couplings = {(0,0,0):C.UVGC_143_32,(0,0,2):C.UVGC_143_33,(0,0,1):C.UVGC_143_34})

V_93 = CTVertex(name = 'V_93',
                type = 'UV',
                particles = [ P.t__tilde__, P.Xm, P.YSu ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YSu] ], [ [P.g, P.YSu] ] ],
                couplings = {(0,0,0):C.UVGC_165_61,(0,0,2):C.UVGC_165_62,(0,0,1):C.UVGC_165_63})

V_94 = CTVertex(name = 'V_94',
                type = 'UV',
                particles = [ P.H, P.YSu__tilde__, P.YSu ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.SSS1 ],
                loop_particles = [ [ [P.g, P.YSu] ] ],
                couplings = {(0,0,0):C.UVGC_134_31})

V_95 = CTVertex(name = 'V_95',
                type = 'UV',
                particles = [ P.g, P.g, P.YSu__tilde__, P.YSu ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YSu] ], [ [P.t] ], [ [P.YSd] ], [ [P.YSu] ] ],
                couplings = {(2,0,0):C.UVGC_187_126,(2,0,1):C.UVGC_187_127,(2,0,2):C.UVGC_187_128,(2,0,3):C.UVGC_187_129,(2,0,5):C.UVGC_187_130,(2,0,6):C.UVGC_187_131,(2,0,7):C.UVGC_187_132,(2,0,4):C.UVGC_188_134,(1,0,0):C.UVGC_187_126,(1,0,1):C.UVGC_187_127,(1,0,2):C.UVGC_187_128,(1,0,3):C.UVGC_187_129,(1,0,5):C.UVGC_187_130,(1,0,6):C.UVGC_187_131,(1,0,7):C.UVGC_187_132,(1,0,4):C.UVGC_188_134,(0,0,2):C.UVGC_129_26,(0,0,4):C.UVGC_129_27})

V_96 = CTVertex(name = 'V_96',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_124_25,(0,1,0):C.UVGC_105_2,(0,2,0):C.UVGC_105_2})

V_97 = CTVertex(name = 'V_97',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_124_25,(0,1,0):C.UVGC_105_2,(0,2,0):C.UVGC_105_2})

V_98 = CTVertex(name = 'V_98',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_124_25,(0,1,0):C.UVGC_158_49,(0,2,0):C.UVGC_158_49})

V_99 = CTVertex(name = 'V_99',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_121_22,(0,1,0):C.UVGC_107_3,(0,2,0):C.UVGC_107_3})

V_100 = CTVertex(name = 'V_100',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_121_22,(0,1,0):C.UVGC_107_3,(0,2,0):C.UVGC_107_3})

V_101 = CTVertex(name = 'V_101',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_121_22,(0,1,0):C.UVGC_150_39,(0,2,0):C.UVGC_150_39})

V_102 = CTVertex(name = 'V_102',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.t] ], [ [P.YSd] ], [ [P.YSu] ] ],
                 couplings = {(0,0,4):C.UVGC_122_23,(0,1,0):C.UVGC_178_104,(0,1,1):C.UVGC_178_105,(0,1,2):C.UVGC_178_106,(0,1,3):C.UVGC_178_107,(0,1,5):C.UVGC_178_108,(0,1,6):C.UVGC_178_109,(0,1,7):C.UVGC_178_110,(0,1,4):C.UVGC_178_111,(0,2,0):C.UVGC_178_104,(0,2,1):C.UVGC_178_105,(0,2,2):C.UVGC_178_106,(0,2,3):C.UVGC_178_107,(0,2,5):C.UVGC_178_108,(0,2,6):C.UVGC_178_109,(0,2,7):C.UVGC_178_110,(0,2,4):C.UVGC_178_111})

V_103 = CTVertex(name = 'V_103',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.c, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.YSd] ], [ [P.YSu] ] ],
                 couplings = {(0,0,2):C.UVGC_122_23,(0,1,0):C.UVGC_178_104,(0,1,1):C.UVGC_178_105,(0,1,3):C.UVGC_178_106,(0,1,4):C.UVGC_178_107,(0,1,5):C.UVGC_178_108,(0,1,6):C.UVGC_178_109,(0,1,7):C.UVGC_178_110,(0,1,2):C.UVGC_178_111,(0,2,0):C.UVGC_178_104,(0,2,1):C.UVGC_178_105,(0,2,3):C.UVGC_178_106,(0,2,4):C.UVGC_178_107,(0,2,5):C.UVGC_178_108,(0,2,6):C.UVGC_178_109,(0,2,7):C.UVGC_178_110,(0,2,2):C.UVGC_178_111})

V_104 = CTVertex(name = 'V_104',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.t] ], [ [P.YSd] ], [ [P.YSu] ] ],
                 couplings = {(0,0,4):C.UVGC_122_23,(0,1,0):C.UVGC_178_104,(0,1,1):C.UVGC_178_105,(0,1,2):C.UVGC_178_106,(0,1,3):C.UVGC_178_107,(0,1,5):C.UVGC_178_108,(0,1,6):C.UVGC_178_109,(0,1,7):C.UVGC_178_110,(0,1,4):C.UVGC_183_113,(0,2,0):C.UVGC_178_104,(0,2,1):C.UVGC_178_105,(0,2,2):C.UVGC_178_106,(0,2,3):C.UVGC_178_107,(0,2,5):C.UVGC_178_108,(0,2,6):C.UVGC_178_109,(0,2,7):C.UVGC_178_110,(0,2,4):C.UVGC_183_113})

V_105 = CTVertex(name = 'V_105',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.YSd] ], [ [P.YSu] ] ],
                 couplings = {(0,0,2):C.UVGC_122_23,(0,1,0):C.UVGC_178_104,(0,1,1):C.UVGC_178_105,(0,1,3):C.UVGC_178_106,(0,1,4):C.UVGC_178_107,(0,1,5):C.UVGC_178_108,(0,1,6):C.UVGC_178_109,(0,1,7):C.UVGC_178_110,(0,1,2):C.UVGC_178_111,(0,2,0):C.UVGC_178_104,(0,2,1):C.UVGC_178_105,(0,2,3):C.UVGC_178_106,(0,2,4):C.UVGC_178_107,(0,2,5):C.UVGC_178_108,(0,2,6):C.UVGC_178_109,(0,2,7):C.UVGC_178_110,(0,2,2):C.UVGC_178_111})

V_106 = CTVertex(name = 'V_106',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.t] ], [ [P.YSd] ], [ [P.YSu] ] ],
                 couplings = {(0,0,4):C.UVGC_122_23,(0,1,0):C.UVGC_178_104,(0,1,1):C.UVGC_178_105,(0,1,2):C.UVGC_178_106,(0,1,3):C.UVGC_178_107,(0,1,5):C.UVGC_178_108,(0,1,6):C.UVGC_178_109,(0,1,7):C.UVGC_178_110,(0,1,4):C.UVGC_178_111,(0,2,0):C.UVGC_178_104,(0,2,1):C.UVGC_178_105,(0,2,2):C.UVGC_178_106,(0,2,3):C.UVGC_178_107,(0,2,5):C.UVGC_178_108,(0,2,6):C.UVGC_178_109,(0,2,7):C.UVGC_178_110,(0,2,4):C.UVGC_178_111})

V_107 = CTVertex(name = 'V_107',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.b, P.g] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.YSd] ], [ [P.YSu] ] ],
                 couplings = {(0,0,1):C.UVGC_122_23,(0,1,0):C.UVGC_178_104,(0,1,2):C.UVGC_178_105,(0,1,3):C.UVGC_178_106,(0,1,4):C.UVGC_178_107,(0,1,5):C.UVGC_178_108,(0,1,6):C.UVGC_178_109,(0,1,7):C.UVGC_178_110,(0,1,1):C.UVGC_182_112,(0,2,0):C.UVGC_178_104,(0,2,2):C.UVGC_178_105,(0,2,3):C.UVGC_178_106,(0,2,4):C.UVGC_178_107,(0,2,5):C.UVGC_178_108,(0,2,6):C.UVGC_178_109,(0,2,7):C.UVGC_178_110,(0,2,1):C.UVGC_182_112})

V_108 = CTVertex(name = 'V_108',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_144_35,(0,0,1):C.UVGC_144_36})

V_109 = CTVertex(name = 'V_109',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_144_35,(0,0,1):C.UVGC_144_36})

V_110 = CTVertex(name = 'V_110',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_160_51,(0,0,2):C.UVGC_160_52,(0,0,1):C.UVGC_144_36})

V_111 = CTVertex(name = 'V_111',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_144_35,(0,0,1):C.UVGC_144_36})

V_112 = CTVertex(name = 'V_112',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_144_35,(0,0,1):C.UVGC_144_36})

V_113 = CTVertex(name = 'V_113',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_160_51,(0,0,2):C.UVGC_160_52,(0,0,1):C.UVGC_144_36})

V_114 = CTVertex(name = 'V_114',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_161_53,(0,1,0):C.UVGC_162_54})

V_115 = CTVertex(name = 'V_115',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_152_41,(0,1,0):C.UVGC_153_42})

V_116 = CTVertex(name = 'V_116',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_123_24,(0,1,0):C.UVGC_104_1,(0,2,0):C.UVGC_104_1})

V_117 = CTVertex(name = 'V_117',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_123_24,(0,1,0):C.UVGC_104_1,(0,2,0):C.UVGC_104_1})

V_118 = CTVertex(name = 'V_118',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_159_50,(0,2,0):C.UVGC_159_50,(0,1,0):C.UVGC_157_48,(0,3,0):C.UVGC_157_48})

V_119 = CTVertex(name = 'V_119',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_123_24,(0,1,0):C.UVGC_104_1,(0,2,0):C.UVGC_104_1})

V_120 = CTVertex(name = 'V_120',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_123_24,(0,1,0):C.UVGC_104_1,(0,2,0):C.UVGC_104_1})

V_121 = CTVertex(name = 'V_121',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_151_40,(0,2,0):C.UVGC_151_40,(0,1,0):C.UVGC_149_38,(0,3,0):C.UVGC_149_38})

V_122 = CTVertex(name = 'V_122',
                 type = 'UV',
                 particles = [ P.YSu__tilde__, P.YSu ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YSu] ] ],
                 couplings = {(0,0,0):C.UVGC_195_167,(0,1,0):C.UVGC_133_30})

V_123 = CTVertex(name = 'V_123',
                 type = 'UV',
                 particles = [ P.YSd__tilde__, P.YSd ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YSd] ] ],
                 couplings = {(0,0,0):C.UVGC_170_72,(0,1,0):C.UVGC_130_28})

V_124 = CTVertex(name = 'V_124',
                 type = 'UV',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.YSd] ], [ [P.YSu] ] ],
                 couplings = {(0,0,0):C.UVGC_172_77,(0,0,1):C.UVGC_172_78,(0,0,2):C.UVGC_172_79,(0,0,3):C.UVGC_172_80,(0,0,4):C.UVGC_172_81,(0,0,5):C.UVGC_172_82,(0,1,0):C.UVGC_171_73,(0,1,3):C.UVGC_171_74,(0,1,4):C.UVGC_171_75,(0,1,5):C.UVGC_171_76})

