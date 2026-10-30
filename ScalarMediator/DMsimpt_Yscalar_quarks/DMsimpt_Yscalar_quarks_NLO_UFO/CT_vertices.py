# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.3.1 for Linux x86 (64-bit) (July 24, 2023)
# Date: Fri 30 Oct 2026 18:09:55


from object_library import all_vertices, all_CTvertices, Vertex, CTVertex
import particles as P
import CT_couplings as C
import lorentz as L


V_1 = CTVertex(name = 'V_1',
               type = 'R2',
               particles = [ P.H, P.YSd__tilde__, P.YSd ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               loop_particles = [ [ [P.g, P.YSd] ] ],
               couplings = {(0,0,0):C.R2GC_206_74})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.H, P.YSu__tilde__, P.YSu ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               loop_particles = [ [ [P.g, P.YSu] ] ],
               couplings = {(0,0,0):C.R2GC_207_75})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV1, L.VVV2, L.VVV4, L.VVV6, L.VVV7, L.VVV8 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_185_58,(0,0,1):C.R2GC_185_59,(0,1,0):C.R2GC_194_62,(0,1,1):C.R2GC_194_63,(0,2,0):C.R2GC_194_62,(0,2,1):C.R2GC_194_63,(0,3,0):C.R2GC_185_58,(0,3,1):C.R2GC_185_59,(0,4,0):C.R2GC_185_58,(0,4,1):C.R2GC_185_59,(0,5,0):C.R2GC_194_62,(0,5,1):C.R2GC_194_63})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(2,0,0):C.R2GC_128_23,(2,0,1):C.R2GC_128_24,(0,0,0):C.R2GC_128_23,(0,0,1):C.R2GC_128_24,(4,0,0):C.R2GC_126_19,(4,0,1):C.R2GC_126_20,(3,0,0):C.R2GC_126_19,(3,0,1):C.R2GC_126_20,(8,0,0):C.R2GC_127_21,(8,0,1):C.R2GC_127_22,(6,0,0):C.R2GC_132_28,(6,0,1):C.R2GC_203_71,(7,0,0):C.R2GC_133_30,(7,0,1):C.R2GC_202_70,(5,0,0):C.R2GC_126_19,(5,0,1):C.R2GC_126_20,(1,0,0):C.R2GC_126_19,(1,0,1):C.R2GC_126_20,(11,0,0):C.R2GC_130_26,(11,0,1):C.R2GC_130_27,(10,0,0):C.R2GC_130_26,(10,0,1):C.R2GC_130_27,(9,0,1):C.R2GC_129_25,(2,1,0):C.R2GC_128_23,(2,1,1):C.R2GC_128_24,(0,1,0):C.R2GC_128_23,(0,1,1):C.R2GC_128_24,(4,1,0):C.R2GC_126_19,(4,1,1):C.R2GC_126_20,(3,1,0):C.R2GC_126_19,(3,1,1):C.R2GC_126_20,(8,1,0):C.R2GC_127_21,(8,1,1):C.R2GC_204_72,(6,1,0):C.R2GC_201_68,(6,1,1):C.R2GC_201_69,(7,1,0):C.R2GC_133_30,(7,1,1):C.R2GC_133_31,(5,1,0):C.R2GC_126_19,(5,1,1):C.R2GC_126_20,(1,1,0):C.R2GC_126_19,(1,1,1):C.R2GC_126_20,(11,1,0):C.R2GC_130_26,(11,1,1):C.R2GC_130_27,(10,1,0):C.R2GC_130_26,(10,1,1):C.R2GC_130_27,(9,1,1):C.R2GC_129_25,(0,2,0):C.R2GC_128_23,(0,2,1):C.R2GC_128_24,(2,2,0):C.R2GC_128_23,(2,2,1):C.R2GC_128_24,(5,2,0):C.R2GC_126_19,(5,2,1):C.R2GC_126_20,(1,2,0):C.R2GC_126_19,(1,2,1):C.R2GC_126_20,(7,2,0):C.R2GC_199_66,(7,2,1):C.R2GC_128_24,(4,2,0):C.R2GC_126_19,(4,2,1):C.R2GC_126_20,(3,2,0):C.R2GC_126_19,(3,2,1):C.R2GC_126_20,(8,2,0):C.R2GC_127_21,(8,2,1):C.R2GC_200_67,(6,2,0):C.R2GC_132_28,(6,2,1):C.R2GC_132_29,(11,2,0):C.R2GC_130_26,(11,2,1):C.R2GC_130_27,(10,2,0):C.R2GC_130_26,(10,2,1):C.R2GC_130_27,(9,2,1):C.R2GC_129_25})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.t__tilde__, P.b, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_176_48,(0,1,0):C.R2GC_178_50})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_167_43})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_166_42})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.b__tilde__, P.t, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_179_51,(0,1,0):C.R2GC_175_47})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_180_52})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_181_53})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.Xm, P.d, P.YSd__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.YSd] ] ],
                couplings = {(0,0,0):C.R2GC_155_38})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.Xm, P.s, P.YSd__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.YSd] ] ],
                couplings = {(0,0,0):C.R2GC_155_38})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.Xm, P.b, P.YSd__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g, P.YSd] ] ],
                couplings = {(0,0,0):C.R2GC_168_44})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.g, P.YSd__tilde__, P.YSd ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS1, L.VSS3 ],
                loop_particles = [ [ [P.g, P.YSd] ] ],
                couplings = {(0,0,0):C.R2GC_188_60,(0,1,0):C.R2GC_191_61})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.d__tilde__, P.Xm, P.YSd ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.YSd] ] ],
                couplings = {(0,0,0):C.R2GC_155_38})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.s__tilde__, P.Xm, P.YSd ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.s, P.YSd] ] ],
                couplings = {(0,0,0):C.R2GC_155_38})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.b__tilde__, P.Xm, P.YSd ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.b, P.g, P.YSd] ] ],
                couplings = {(0,0,0):C.R2GC_168_44})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.g, P.g, P.YSd__tilde__, P.YSd ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g] ], [ [P.g, P.YSd] ] ],
                couplings = {(2,0,0):C.R2GC_197_64,(2,0,1):C.R2GC_197_65,(1,0,0):C.R2GC_197_64,(1,0,1):C.R2GC_197_65,(0,0,0):C.R2GC_130_27,(0,0,1):C.R2GC_138_35})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.Xm, P.u, P.YSu__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.u, P.YSu] ] ],
                couplings = {(0,0,0):C.R2GC_155_38})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.Xm, P.c, P.YSu__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.c, P.g, P.YSu] ] ],
                couplings = {(0,0,0):C.R2GC_155_38})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.Xm, P.t, P.YSu__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.t, P.YSu] ] ],
                couplings = {(0,0,0):C.R2GC_177_49})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.g, P.YSu__tilde__, P.YSu ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.YSu] ] ],
                couplings = {(0,0,0):C.R2GC_188_60})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.u__tilde__, P.Xm, P.YSu ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.u, P.YSu] ] ],
                couplings = {(0,0,0):C.R2GC_155_38})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.c__tilde__, P.Xm, P.YSu ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.YSu] ] ],
                couplings = {(0,0,0):C.R2GC_155_38})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.t__tilde__, P.Xm, P.YSu ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.t, P.YSu] ] ],
                couplings = {(0,0,0):C.R2GC_177_49})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.g, P.g, P.YSu__tilde__, P.YSu ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g] ], [ [P.g, P.YSu] ] ],
                couplings = {(2,0,0):C.R2GC_197_64,(2,0,1):C.R2GC_197_65,(1,0,0):C.R2GC_197_64,(1,0,1):C.R2GC_197_65,(0,0,0):C.R2GC_130_27,(0,0,1):C.R2GC_138_35})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_152_37})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_152_37})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_152_37})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_134_32})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_134_32})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_134_32})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_135_33})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_135_33})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_135_33})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_135_33})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_135_33})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_135_33})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_156_39})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_156_39})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_156_39})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_156_39})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_156_39})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_156_39})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_107_15,(0,1,0):C.R2GC_174_46})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_107_15,(0,1,0):C.R2GC_174_46})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_107_15,(0,1,0):C.R2GC_174_46})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_108_16,(0,1,0):C.R2GC_165_41})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_108_16,(0,1,0):C.R2GC_165_41})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_108_16,(0,1,0):C.R2GC_165_41})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_136_34})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_136_34})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_171_45,(0,2,0):C.R2GC_171_45,(0,1,0):C.R2GC_136_34,(0,3,0):C.R2GC_136_34})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_136_34})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_136_34})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_163_40,(0,2,0):C.R2GC_163_40,(0,1,0):C.R2GC_136_34,(0,3,0):C.R2GC_136_34})

V_57 = CTVertex(name = 'V_57',
                type = 'R2',
                particles = [ P.YSu__tilde__, P.YSu ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SS1, L.SS2 ],
                loop_particles = [ [ [P.g, P.YSu] ] ],
                couplings = {(0,0,0):C.R2GC_205_73,(0,1,0):C.R2GC_139_36})

V_58 = CTVertex(name = 'V_58',
                type = 'R2',
                particles = [ P.YSd__tilde__, P.YSd ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.SS1, L.SS2 ],
                loop_particles = [ [ [P.g, P.YSd] ] ],
                couplings = {(0,0,0):C.R2GC_182_54,(0,1,0):C.R2GC_139_36})

V_59 = CTVertex(name = 'V_59',
                type = 'R2',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV2, L.VV3 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ], [ [P.t] ] ],
                couplings = {(0,0,2):C.R2GC_184_57,(0,1,0):C.R2GC_98_76,(0,1,3):C.R2GC_98_77,(0,2,1):C.R2GC_183_55,(0,2,2):C.R2GC_183_56})

V_60 = CTVertex(name = 'V_60',
                type = 'R2',
                particles = [ P.g, P.g, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_99_78,(0,0,1):C.R2GC_99_79})

V_61 = CTVertex(name = 'V_61',
                type = 'R2',
                particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_111_18,(0,1,0):C.R2GC_111_18,(0,2,0):C.R2GC_111_18})

V_62 = CTVertex(name = 'V_62',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Z ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_103_7,(0,0,1):C.R2GC_103_8,(0,1,0):C.R2GC_103_7,(0,1,1):C.R2GC_103_8,(0,2,0):C.R2GC_103_7,(0,2,1):C.R2GC_103_8})

V_63 = CTVertex(name = 'V_63',
                type = 'R2',
                particles = [ P.g, P.g, P.Z, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_106_13,(0,0,1):C.R2GC_106_14,(0,1,0):C.R2GC_106_13,(0,1,1):C.R2GC_106_14,(0,2,0):C.R2GC_106_13,(0,2,1):C.R2GC_106_14})

V_64 = CTVertex(name = 'V_64',
                type = 'R2',
                particles = [ P.a, P.a, P.g, P.g ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_101_3,(0,0,1):C.R2GC_101_4,(0,1,0):C.R2GC_101_3,(0,1,1):C.R2GC_101_4,(0,2,0):C.R2GC_101_3,(0,2,1):C.R2GC_101_4})

V_65 = CTVertex(name = 'V_65',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Z ],
                color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(1,0,0):C.R2GC_105_11,(1,0,1):C.R2GC_105_12,(0,1,0):C.R2GC_104_9,(0,1,1):C.R2GC_104_10,(0,2,0):C.R2GC_104_9,(0,2,1):C.R2GC_104_10,(0,3,0):C.R2GC_104_9,(0,3,1):C.R2GC_104_10})

V_66 = CTVertex(name = 'V_66',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.g ],
                color = [ 'd(2,3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_102_5,(0,0,1):C.R2GC_102_6,(0,1,0):C.R2GC_102_5,(0,1,1):C.R2GC_102_6,(0,2,0):C.R2GC_102_5,(0,2,1):C.R2GC_102_6})

V_67 = CTVertex(name = 'V_67',
                type = 'R2',
                particles = [ P.g, P.g, P.H, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_100_1,(0,0,1):C.R2GC_100_2})

V_68 = CTVertex(name = 'V_68',
                type = 'R2',
                particles = [ P.g, P.g, P.G0, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_100_1,(0,0,1):C.R2GC_100_2})

V_69 = CTVertex(name = 'V_69',
                type = 'R2',
                particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_110_17})

V_70 = CTVertex(name = 'V_70',
                type = 'UV',
                particles = [ P.H, P.YSd__tilde__, P.YSd ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                loop_particles = [ [ [P.g, P.YSd] ] ],
                couplings = {(0,0,0):C.UVGC_206_165})

V_71 = CTVertex(name = 'V_71',
                type = 'UV',
                particles = [ P.H, P.YSu__tilde__, P.YSu ],
                color = [ '1' ],
                lorentz = [ L.SSS1 ],
                loop_particles = [ [ [P.g, P.YSu] ] ],
                couplings = {(0,0,0):C.UVGC_207_166})

V_72 = CTVertex(name = 'V_72',
                type = 'UV',
                particles = [ P.g, P.g, P.g ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVV1, L.VVV2, L.VVV3, L.VVV4, L.VVV5, L.VVV6, L.VVV7, L.VVV8 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.YSd] ], [ [P.YSd], [P.YSu] ], [ [P.YSu] ] ],
                couplings = {(0,0,0):C.UVGC_185_84,(0,0,1):C.UVGC_185_85,(0,0,2):C.UVGC_185_86,(0,0,3):C.UVGC_131_16,(0,0,4):C.UVGC_185_87,(0,0,5):C.UVGC_185_88,(0,0,7):C.UVGC_185_89,(0,1,0):C.UVGC_194_112,(0,1,1):C.UVGC_194_113,(0,1,2):C.UVGC_195_118,(0,1,3):C.UVGC_195_119,(0,1,4):C.UVGC_194_115,(0,1,5):C.UVGC_195_120,(0,1,7):C.UVGC_195_121,(0,3,0):C.UVGC_194_112,(0,3,1):C.UVGC_194_113,(0,3,2):C.UVGC_194_114,(0,3,3):C.UVGC_125_6,(0,3,4):C.UVGC_194_115,(0,3,5):C.UVGC_194_116,(0,3,7):C.UVGC_194_117,(0,5,0):C.UVGC_185_84,(0,5,1):C.UVGC_185_85,(0,5,2):C.UVGC_187_92,(0,5,3):C.UVGC_187_93,(0,5,4):C.UVGC_185_87,(0,5,5):C.UVGC_187_94,(0,5,7):C.UVGC_187_95,(0,6,0):C.UVGC_185_84,(0,6,1):C.UVGC_185_85,(0,6,2):C.UVGC_186_90,(0,6,3):C.UVGC_186_91,(0,6,4):C.UVGC_185_87,(0,6,5):C.UVGC_185_88,(0,6,7):C.UVGC_185_89,(0,7,0):C.UVGC_194_112,(0,7,1):C.UVGC_194_113,(0,7,2):C.UVGC_196_122,(0,7,3):C.UVGC_196_123,(0,7,4):C.UVGC_194_115,(0,7,5):C.UVGC_195_120,(0,7,7):C.UVGC_195_121,(0,2,2):C.UVGC_125_5,(0,2,3):C.UVGC_125_6,(0,4,2):C.UVGC_131_15,(0,4,3):C.UVGC_131_16,(0,4,6):C.UVGC_131_17})

V_73 = CTVertex(name = 'V_73',
                type = 'UV',
                particles = [ P.g, P.g, P.g, P.g ],
                color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u], [P.YSd], [P.YSu] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.YSd] ], [ [P.YSd], [P.YSu] ], [ [P.YSu] ] ],
                couplings = {(2,0,4):C.UVGC_127_10,(2,0,5):C.UVGC_127_9,(0,0,4):C.UVGC_127_10,(0,0,5):C.UVGC_127_9,(4,0,4):C.UVGC_126_7,(4,0,5):C.UVGC_126_8,(3,0,4):C.UVGC_126_7,(3,0,5):C.UVGC_126_8,(8,0,4):C.UVGC_127_9,(8,0,5):C.UVGC_127_10,(6,0,0):C.UVGC_202_149,(6,0,3):C.UVGC_197_125,(6,0,4):C.UVGC_203_155,(6,0,5):C.UVGC_203_156,(6,0,6):C.UVGC_202_152,(6,0,7):C.UVGC_202_153,(6,0,9):C.UVGC_202_154,(7,0,0):C.UVGC_202_149,(7,0,3):C.UVGC_197_125,(7,0,4):C.UVGC_202_150,(7,0,5):C.UVGC_202_151,(7,0,6):C.UVGC_202_152,(7,0,7):C.UVGC_202_153,(7,0,9):C.UVGC_202_154,(5,0,4):C.UVGC_126_7,(5,0,5):C.UVGC_126_8,(1,0,4):C.UVGC_126_7,(1,0,5):C.UVGC_126_8,(11,0,4):C.UVGC_130_13,(11,0,5):C.UVGC_130_14,(10,0,4):C.UVGC_130_13,(10,0,5):C.UVGC_130_14,(9,0,4):C.UVGC_129_11,(9,0,5):C.UVGC_129_12,(2,1,4):C.UVGC_127_10,(2,1,5):C.UVGC_127_9,(0,1,4):C.UVGC_127_10,(0,1,5):C.UVGC_127_9,(4,1,4):C.UVGC_126_7,(4,1,5):C.UVGC_126_8,(3,1,4):C.UVGC_126_7,(3,1,5):C.UVGC_126_8,(8,1,0):C.UVGC_204_157,(8,1,3):C.UVGC_204_158,(8,1,4):C.UVGC_204_159,(8,1,5):C.UVGC_204_160,(8,1,6):C.UVGC_204_161,(8,1,7):C.UVGC_204_162,(8,1,9):C.UVGC_204_163,(6,1,0):C.UVGC_199_132,(6,1,4):C.UVGC_201_145,(6,1,5):C.UVGC_201_146,(6,1,6):C.UVGC_199_135,(6,1,7):C.UVGC_201_147,(6,1,9):C.UVGC_201_148,(7,1,2):C.UVGC_132_18,(7,1,4):C.UVGC_133_21,(7,1,5):C.UVGC_133_22,(5,1,4):C.UVGC_126_7,(5,1,5):C.UVGC_126_8,(1,1,4):C.UVGC_126_7,(1,1,5):C.UVGC_126_8,(11,1,4):C.UVGC_130_13,(11,1,5):C.UVGC_130_14,(10,1,4):C.UVGC_130_13,(10,1,5):C.UVGC_130_14,(9,1,4):C.UVGC_129_11,(9,1,5):C.UVGC_129_12,(0,2,4):C.UVGC_127_10,(0,2,5):C.UVGC_127_9,(2,2,4):C.UVGC_127_10,(2,2,5):C.UVGC_127_9,(5,2,4):C.UVGC_126_7,(5,2,5):C.UVGC_126_8,(1,2,4):C.UVGC_126_7,(1,2,5):C.UVGC_126_8,(7,2,0):C.UVGC_199_132,(7,2,4):C.UVGC_199_133,(7,2,5):C.UVGC_199_134,(7,2,6):C.UVGC_199_135,(7,2,7):C.UVGC_199_136,(7,2,9):C.UVGC_199_137,(4,2,4):C.UVGC_126_7,(4,2,5):C.UVGC_126_8,(3,2,4):C.UVGC_126_7,(3,2,5):C.UVGC_126_8,(8,2,0):C.UVGC_200_138,(8,2,3):C.UVGC_200_139,(8,2,4):C.UVGC_200_140,(8,2,5):C.UVGC_200_141,(8,2,6):C.UVGC_200_142,(8,2,7):C.UVGC_200_143,(8,2,9):C.UVGC_200_144,(6,2,1):C.UVGC_132_18,(6,2,4):C.UVGC_132_19,(6,2,5):C.UVGC_129_11,(6,2,8):C.UVGC_132_20,(11,2,4):C.UVGC_130_13,(11,2,5):C.UVGC_130_14,(10,2,4):C.UVGC_130_13,(10,2,5):C.UVGC_130_14,(9,2,4):C.UVGC_129_11,(9,2,5):C.UVGC_129_12})

V_74 = CTVertex(name = 'V_74',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_176_60,(0,0,2):C.UVGC_176_61,(0,0,1):C.UVGC_176_62,(0,1,0):C.UVGC_178_65,(0,1,2):C.UVGC_178_66,(0,1,1):C.UVGC_178_67})

V_75 = CTVertex(name = 'V_75',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_167_47})

V_76 = CTVertex(name = 'V_76',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_166_46})

V_77 = CTVertex(name = 'V_77',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_179_68,(0,0,2):C.UVGC_179_69,(0,0,1):C.UVGC_179_70,(0,1,0):C.UVGC_175_57,(0,1,2):C.UVGC_175_58,(0,1,1):C.UVGC_175_59})

V_78 = CTVertex(name = 'V_78',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_180_71})

V_79 = CTVertex(name = 'V_79',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_181_72})

V_80 = CTVertex(name = 'V_80',
                type = 'UV',
                particles = [ P.Xm, P.d, P.YSd__tilde__ ],
                color = [ 'Identity(1,3)', 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YSd] ], [ [P.g, P.YSd] ] ],
                couplings = {(1,0,0):C.UVGC_155_37,(1,0,1):C.UVGC_155_38,(0,0,2):C.UVGC_144_31})

V_81 = CTVertex(name = 'V_81',
                type = 'UV',
                particles = [ P.Xm, P.s, P.YSd__tilde__ ],
                color = [ 'Identity(1,3)', 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YSd] ], [ [P.g, P.YSd] ] ],
                couplings = {(1,0,0):C.UVGC_155_37,(1,0,1):C.UVGC_155_38,(0,0,2):C.UVGC_144_31})

V_82 = CTVertex(name = 'V_82',
                type = 'UV',
                particles = [ P.Xm, P.b, P.YSd__tilde__ ],
                color = [ 'Identity(1,3)', 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YSd] ], [ [P.g, P.YSd] ] ],
                couplings = {(1,0,0):C.UVGC_168_48,(1,0,1):C.UVGC_168_49,(0,0,2):C.UVGC_143_30})

V_83 = CTVertex(name = 'V_83',
                type = 'UV',
                particles = [ P.g, P.YSd__tilde__, P.YSd ],
                color = [ 'T(1,1,2)', 'T(1,3,2)' ],
                lorentz = [ L.VSS1, L.VSS3 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YSd] ], [ [P.t] ], [ [P.YSd] ], [ [P.YSu] ] ],
                couplings = {(1,0,0):C.UVGC_188_96,(1,0,1):C.UVGC_188_97,(1,0,2):C.UVGC_188_98,(1,0,3):C.UVGC_188_99,(1,0,5):C.UVGC_188_100,(1,0,6):C.UVGC_188_101,(1,0,7):C.UVGC_188_102,(1,0,4):C.UVGC_188_103,(1,1,0):C.UVGC_190_104,(1,1,1):C.UVGC_188_103,(1,1,2):C.UVGC_190_105,(1,1,3):C.UVGC_190_106,(1,1,5):C.UVGC_190_107,(1,1,6):C.UVGC_190_108,(1,1,7):C.UVGC_190_109,(1,1,4):C.UVGC_188_97,(0,0,4):C.UVGC_141_28,(0,1,4):C.UVGC_140_27})

V_84 = CTVertex(name = 'V_84',
                type = 'UV',
                particles = [ P.d__tilde__, P.Xm, P.YSd ],
                color = [ 'Identity(1,3)', 'Identity(2,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YSd] ], [ [P.g, P.YSd] ] ],
                couplings = {(0,0,0):C.UVGC_155_37,(0,0,1):C.UVGC_155_38,(1,0,2):C.UVGC_144_31})

V_85 = CTVertex(name = 'V_85',
                type = 'UV',
                particles = [ P.s__tilde__, P.Xm, P.YSd ],
                color = [ 'Identity(1,3)', 'Identity(2,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YSd] ], [ [P.g, P.YSd] ] ],
                couplings = {(0,0,0):C.UVGC_155_37,(0,0,1):C.UVGC_155_38,(1,0,2):C.UVGC_144_31})

V_86 = CTVertex(name = 'V_86',
                type = 'UV',
                particles = [ P.b__tilde__, P.Xm, P.YSd ],
                color = [ 'Identity(1,3)', 'Identity(2,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YSd] ], [ [P.g, P.YSd] ] ],
                couplings = {(0,0,0):C.UVGC_168_48,(0,0,1):C.UVGC_168_49,(1,0,2):C.UVGC_143_30})

V_87 = CTVertex(name = 'V_87',
                type = 'UV',
                particles = [ P.g, P.g, P.YSd__tilde__, P.YSd ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,2)*T(1,-1,3)*T(2,4,-1)', 'Identity(1,2)*T(1,4,-1)*T(2,-1,3)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YSd] ], [ [P.t] ], [ [P.YSd] ], [ [P.YSu] ] ],
                couplings = {(4,0,0):C.UVGC_197_124,(4,0,1):C.UVGC_197_125,(4,0,2):C.UVGC_197_126,(4,0,3):C.UVGC_197_127,(4,0,5):C.UVGC_197_128,(4,0,6):C.UVGC_197_129,(4,0,7):C.UVGC_197_130,(4,0,4):C.UVGC_197_131,(3,0,0):C.UVGC_197_124,(3,0,1):C.UVGC_197_125,(3,0,2):C.UVGC_197_126,(3,0,3):C.UVGC_197_127,(3,0,5):C.UVGC_197_128,(3,0,6):C.UVGC_197_129,(3,0,7):C.UVGC_197_130,(3,0,4):C.UVGC_197_131,(0,0,2):C.UVGC_138_24,(0,0,4):C.UVGC_138_25,(2,0,4):C.UVGC_142_29,(1,0,4):C.UVGC_142_29})

V_88 = CTVertex(name = 'V_88',
                type = 'UV',
                particles = [ P.Xm, P.u, P.YSu__tilde__ ],
                color = [ 'Identity(1,3)', 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YSu] ], [ [P.g, P.YSu] ] ],
                couplings = {(1,0,0):C.UVGC_155_37,(1,0,1):C.UVGC_155_38,(0,0,2):C.UVGC_149_35})

V_89 = CTVertex(name = 'V_89',
                type = 'UV',
                particles = [ P.Xm, P.c, P.YSu__tilde__ ],
                color = [ 'Identity(1,3)', 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YSu] ], [ [P.g, P.YSu] ] ],
                couplings = {(1,0,0):C.UVGC_155_37,(1,0,1):C.UVGC_155_38,(0,0,2):C.UVGC_149_35})

V_90 = CTVertex(name = 'V_90',
                type = 'UV',
                particles = [ P.Xm, P.t, P.YSu__tilde__ ],
                color = [ 'Identity(1,3)', 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YSu] ], [ [P.g, P.YSu] ] ],
                couplings = {(1,0,0):C.UVGC_177_63,(1,0,1):C.UVGC_177_64,(0,0,2):C.UVGC_150_36})

V_91 = CTVertex(name = 'V_91',
                type = 'UV',
                particles = [ P.g, P.YSu__tilde__, P.YSu ],
                color = [ 'T(1,1,2)', 'T(1,3,2)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YSu] ], [ [P.t] ], [ [P.YSd] ], [ [P.YSu] ] ],
                couplings = {(1,0,0):C.UVGC_188_96,(1,0,1):C.UVGC_188_97,(1,0,2):C.UVGC_188_98,(1,0,3):C.UVGC_188_99,(1,0,5):C.UVGC_188_100,(1,0,6):C.UVGC_188_101,(1,0,7):C.UVGC_188_102,(1,0,4):C.UVGC_188_103,(0,0,4):C.UVGC_147_33})

V_92 = CTVertex(name = 'V_92',
                type = 'UV',
                particles = [ P.u__tilde__, P.Xm, P.YSu ],
                color = [ 'Identity(1,3)', 'Identity(2,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YSu] ], [ [P.g, P.YSu] ] ],
                couplings = {(0,0,0):C.UVGC_155_37,(0,0,1):C.UVGC_155_38,(1,0,2):C.UVGC_149_35})

V_93 = CTVertex(name = 'V_93',
                type = 'UV',
                particles = [ P.c__tilde__, P.Xm, P.YSu ],
                color = [ 'Identity(1,3)', 'Identity(2,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YSu] ], [ [P.g, P.YSu] ] ],
                couplings = {(0,0,0):C.UVGC_155_37,(0,0,1):C.UVGC_155_38,(1,0,2):C.UVGC_149_35})

V_94 = CTVertex(name = 'V_94',
                type = 'UV',
                particles = [ P.t__tilde__, P.Xm, P.YSu ],
                color = [ 'Identity(1,3)', 'Identity(2,3)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YSu] ], [ [P.g, P.YSu] ] ],
                couplings = {(0,0,0):C.UVGC_177_63,(0,0,1):C.UVGC_177_64,(1,0,2):C.UVGC_150_36})

V_95 = CTVertex(name = 'V_95',
                type = 'UV',
                particles = [ P.g, P.g, P.YSu__tilde__, P.YSu ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,2)*T(1,-1,3)*T(2,4,-1)', 'Identity(1,2)*T(1,4,-1)*T(2,-1,3)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YSu] ], [ [P.t] ], [ [P.YSd] ], [ [P.YSu] ] ],
                couplings = {(4,0,0):C.UVGC_197_124,(4,0,1):C.UVGC_197_125,(4,0,2):C.UVGC_197_126,(4,0,3):C.UVGC_197_127,(4,0,5):C.UVGC_197_128,(4,0,6):C.UVGC_197_129,(4,0,7):C.UVGC_197_130,(4,0,4):C.UVGC_197_131,(3,0,0):C.UVGC_197_124,(3,0,1):C.UVGC_197_125,(3,0,2):C.UVGC_197_126,(3,0,3):C.UVGC_197_127,(3,0,5):C.UVGC_197_128,(3,0,6):C.UVGC_197_129,(3,0,7):C.UVGC_197_130,(3,0,4):C.UVGC_197_131,(0,0,2):C.UVGC_138_24,(0,0,4):C.UVGC_138_25,(2,0,4):C.UVGC_148_34,(1,0,4):C.UVGC_148_34})

V_96 = CTVertex(name = 'V_96',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_114_2})

V_97 = CTVertex(name = 'V_97',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_114_2})

V_98 = CTVertex(name = 'V_98',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV6 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_114_2,(0,1,0):C.UVGC_170_51})

V_99 = CTVertex(name = 'V_99',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_117_4})

V_100 = CTVertex(name = 'V_100',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV4 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_117_4})

V_101 = CTVertex(name = 'V_101',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV6 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_117_4,(0,1,0):C.UVGC_162_42})

V_102 = CTVertex(name = 'V_102',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV5, L.FFV6 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.t] ], [ [P.YSd] ], [ [P.YSu] ] ],
                 couplings = {(0,0,4):C.UVGC_115_3,(0,1,0):C.UVGC_190_104,(0,1,1):C.UVGC_188_103,(0,1,2):C.UVGC_190_105,(0,1,3):C.UVGC_190_106,(0,1,5):C.UVGC_190_107,(0,1,6):C.UVGC_190_108,(0,1,7):C.UVGC_190_109})

V_103 = CTVertex(name = 'V_103',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV5, L.FFV6 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.c, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.YSd] ], [ [P.YSu] ] ],
                 couplings = {(0,0,2):C.UVGC_115_3,(0,1,0):C.UVGC_190_104,(0,1,1):C.UVGC_188_103,(0,1,3):C.UVGC_190_105,(0,1,4):C.UVGC_190_106,(0,1,5):C.UVGC_190_107,(0,1,6):C.UVGC_190_108,(0,1,7):C.UVGC_190_109})

V_104 = CTVertex(name = 'V_104',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV6 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.t] ], [ [P.YSd] ], [ [P.YSu] ] ],
                 couplings = {(0,0,4):C.UVGC_115_3,(0,1,0):C.UVGC_190_104,(0,1,1):C.UVGC_188_103,(0,1,2):C.UVGC_190_105,(0,1,3):C.UVGC_190_106,(0,1,5):C.UVGC_190_107,(0,1,6):C.UVGC_190_108,(0,1,7):C.UVGC_190_109,(0,1,4):C.UVGC_193_111})

V_105 = CTVertex(name = 'V_105',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV5, L.FFV6 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.YSd] ], [ [P.YSu] ] ],
                 couplings = {(0,0,2):C.UVGC_115_3,(0,1,0):C.UVGC_190_104,(0,1,1):C.UVGC_188_103,(0,1,3):C.UVGC_190_105,(0,1,4):C.UVGC_190_106,(0,1,5):C.UVGC_190_107,(0,1,6):C.UVGC_190_108,(0,1,7):C.UVGC_190_109})

V_106 = CTVertex(name = 'V_106',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV5, L.FFV6 ],
                 loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.t] ], [ [P.YSd] ], [ [P.YSu] ] ],
                 couplings = {(0,0,4):C.UVGC_115_3,(0,1,0):C.UVGC_190_104,(0,1,1):C.UVGC_188_103,(0,1,2):C.UVGC_190_105,(0,1,3):C.UVGC_190_106,(0,1,5):C.UVGC_190_107,(0,1,6):C.UVGC_190_108,(0,1,7):C.UVGC_190_109})

V_107 = CTVertex(name = 'V_107',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV6 ],
                 loop_particles = [ [ [P.b] ], [ [P.b, P.g] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.YSd] ], [ [P.YSu] ] ],
                 couplings = {(0,0,1):C.UVGC_115_3,(0,1,0):C.UVGC_190_104,(0,1,2):C.UVGC_188_103,(0,1,3):C.UVGC_190_105,(0,1,4):C.UVGC_190_106,(0,1,5):C.UVGC_190_107,(0,1,6):C.UVGC_190_108,(0,1,7):C.UVGC_190_109,(0,1,1):C.UVGC_192_110})

V_108 = CTVertex(name = 'V_108',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_156_39,(0,0,1):C.UVGC_156_40})

V_109 = CTVertex(name = 'V_109',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_156_39,(0,0,1):C.UVGC_156_40})

V_110 = CTVertex(name = 'V_110',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_172_53,(0,0,2):C.UVGC_172_54,(0,0,1):C.UVGC_156_40})

V_111 = CTVertex(name = 'V_111',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_156_39,(0,0,1):C.UVGC_156_40})

V_112 = CTVertex(name = 'V_112',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_156_39,(0,0,1):C.UVGC_156_40})

V_113 = CTVertex(name = 'V_113',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_172_53,(0,0,2):C.UVGC_172_54,(0,0,1):C.UVGC_156_40})

V_114 = CTVertex(name = 'V_114',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_173_55,(0,1,0):C.UVGC_174_56})

V_115 = CTVertex(name = 'V_115',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_164_44,(0,1,0):C.UVGC_165_45})

V_116 = CTVertex(name = 'V_116',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_136_23,(0,1,0):C.UVGC_113_1,(0,2,0):C.UVGC_113_1})

V_117 = CTVertex(name = 'V_117',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_136_23,(0,1,0):C.UVGC_113_1,(0,2,0):C.UVGC_113_1})

V_118 = CTVertex(name = 'V_118',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_171_52,(0,2,0):C.UVGC_171_52,(0,1,0):C.UVGC_169_50,(0,3,0):C.UVGC_169_50})

V_119 = CTVertex(name = 'V_119',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_136_23,(0,1,0):C.UVGC_113_1,(0,2,0):C.UVGC_113_1})

V_120 = CTVertex(name = 'V_120',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_136_23,(0,1,0):C.UVGC_113_1,(0,2,0):C.UVGC_113_1})

V_121 = CTVertex(name = 'V_121',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_163_43,(0,2,0):C.UVGC_163_43,(0,1,0):C.UVGC_161_41,(0,3,0):C.UVGC_161_41})

V_122 = CTVertex(name = 'V_122',
                 type = 'UV',
                 particles = [ P.YSu__tilde__, P.YSu ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YSu] ] ],
                 couplings = {(0,0,0):C.UVGC_205_164,(0,1,0):C.UVGC_146_32})

V_123 = CTVertex(name = 'V_123',
                 type = 'UV',
                 particles = [ P.YSd__tilde__, P.YSd ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YSd] ] ],
                 couplings = {(0,0,0):C.UVGC_182_73,(0,1,0):C.UVGC_139_26})

V_124 = CTVertex(name = 'V_124',
                 type = 'UV',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.YSd] ], [ [P.YSu] ] ],
                 couplings = {(0,0,0):C.UVGC_184_78,(0,0,1):C.UVGC_184_79,(0,0,2):C.UVGC_184_80,(0,0,3):C.UVGC_184_81,(0,0,4):C.UVGC_184_82,(0,0,5):C.UVGC_184_83,(0,1,0):C.UVGC_183_74,(0,1,3):C.UVGC_183_75,(0,1,4):C.UVGC_183_76,(0,1,5):C.UVGC_183_77})

V_125 = CTVertex(name = 'V_125',
                 type = 'UV',
                 particles = [ P.g, P.g, P.H ],
                 color = [ '1' ],
                 lorentz = [ L.VVS1 ],
                 loop_particles = [ [ [P.YSd] ], [ [P.YSu] ] ],
                 couplings = {(0,0,0):C.UVGC_208_167,(0,0,1):C.UVGC_208_168})

V_126 = CTVertex(name = 'V_126',
                 type = 'UV',
                 particles = [ P.g, P.g, P.H, P.H ],
                 color = [ '1' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.YSd] ], [ [P.YSu] ] ],
                 couplings = {(0,0,0):C.UVGC_209_169,(0,0,1):C.UVGC_209_170})

V_127 = CTVertex(name = 'V_127',
                 type = 'UV',
                 particles = [ P.g, P.g, P.G0, P.G0 ],
                 color = [ '1' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.YSd] ], [ [P.YSu] ] ],
                 couplings = {(0,0,0):C.UVGC_209_169,(0,0,1):C.UVGC_209_170})

V_128 = CTVertex(name = 'V_128',
                 type = 'UV',
                 particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
                 color = [ '1' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.YSd] ], [ [P.YSu] ] ],
                 couplings = {(0,0,0):C.UVGC_209_169,(0,0,1):C.UVGC_209_170})

