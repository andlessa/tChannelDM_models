# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.3.1 for Linux x86 (64-bit) (July 24, 2023)
# Date: Wed 11 Nov 2026 17:52:56


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



R2GC_100_1 = Coupling(name = 'R2GC_100_1',
                      value = '(ee*complex(0,1)*G**2)/(18.*cmath.pi**2)',
                      order = {'QCD':2,'QED':1})

R2GC_101_2 = Coupling(name = 'R2GC_101_2',
                      value = '-0.16666666666666666*(complex(0,1)*G**3)/cmath.pi**2',
                      order = {'QCD':3})

R2GC_102_3 = Coupling(name = 'R2GC_102_3',
                      value = '-0.05555555555555555*(ee*complex(0,1)*G**2*sw)/(cw*cmath.pi**2)',
                      order = {'QCD':2,'QED':1})

R2GC_106_4 = Coupling(name = 'R2GC_106_4',
                      value = '-0.1111111111111111*(ee*complex(0,1)*G**2)/cmath.pi**2',
                      order = {'QCD':2,'QED':1})

R2GC_108_5 = Coupling(name = 'R2GC_108_5',
                      value = '(ee*complex(0,1)*G**2*sw)/(9.*cw*cmath.pi**2)',
                      order = {'QCD':2,'QED':1})

R2GC_109_6 = Coupling(name = 'R2GC_109_6',
                      value = '-0.125*(complex(0,1)*G**2*MB**2)/cmath.pi**2',
                      order = {'QCD':2})

R2GC_109_7 = Coupling(name = 'R2GC_109_7',
                      value = '-0.125*(complex(0,1)*G**2*MT**2)/cmath.pi**2',
                      order = {'QCD':2})

R2GC_110_8 = Coupling(name = 'R2GC_110_8',
                      value = '-0.125*(complex(0,1)*G**2*MB*yb)/(cmath.pi**2*cmath.sqrt(2))',
                      order = {'QCD':2,'QED':1})

R2GC_110_9 = Coupling(name = 'R2GC_110_9',
                      value = '-0.125*(complex(0,1)*G**2*MT*yt)/(cmath.pi**2*cmath.sqrt(2))',
                      order = {'QCD':2,'QED':1})

R2GC_111_10 = Coupling(name = 'R2GC_111_10',
                       value = '-0.0625*(complex(0,1)*G**2*yb**2)/cmath.pi**2',
                       order = {'QCD':2,'QED':2})

R2GC_111_11 = Coupling(name = 'R2GC_111_11',
                       value = '-0.0625*(complex(0,1)*G**2*yt**2)/cmath.pi**2',
                       order = {'QCD':2,'QED':2})

R2GC_112_12 = Coupling(name = 'R2GC_112_12',
                       value = '(ee**2*complex(0,1)*G**2)/(216.*cmath.pi**2)',
                       order = {'QCD':2,'QED':2})

R2GC_112_13 = Coupling(name = 'R2GC_112_13',
                       value = '(ee**2*complex(0,1)*G**2)/(54.*cmath.pi**2)',
                       order = {'QCD':2,'QED':2})

R2GC_113_14 = Coupling(name = 'R2GC_113_14',
                       value = '-0.006944444444444444*(ee*complex(0,1)*G**3)/cmath.pi**2',
                       order = {'QCD':3,'QED':1})

R2GC_113_15 = Coupling(name = 'R2GC_113_15',
                       value = '(ee*complex(0,1)*G**3)/(72.*cmath.pi**2)',
                       order = {'QCD':3,'QED':1})

R2GC_114_16 = Coupling(name = 'R2GC_114_16',
                       value = '(cw*ee**2*complex(0,1)*G**2)/(288.*cmath.pi**2*sw) - (ee**2*complex(0,1)*G**2*sw)/(864.*cw*cmath.pi**2)',
                       order = {'QCD':2,'QED':2})

R2GC_114_17 = Coupling(name = 'R2GC_114_17',
                       value = '(cw*ee**2*complex(0,1)*G**2)/(144.*cmath.pi**2*sw) - (5*ee**2*complex(0,1)*G**2*sw)/(432.*cw*cmath.pi**2)',
                       order = {'QCD':2,'QED':2})

R2GC_115_18 = Coupling(name = 'R2GC_115_18',
                       value = '-0.005208333333333333*(cw*ee*complex(0,1)*G**3)/(cmath.pi**2*sw) + (ee*complex(0,1)*G**3*sw)/(576.*cw*cmath.pi**2)',
                       order = {'QCD':3,'QED':1})

R2GC_115_19 = Coupling(name = 'R2GC_115_19',
                       value = '(cw*ee*complex(0,1)*G**3)/(192.*cmath.pi**2*sw) - (5*ee*complex(0,1)*G**3*sw)/(576.*cw*cmath.pi**2)',
                       order = {'QCD':3,'QED':1})

R2GC_116_20 = Coupling(name = 'R2GC_116_20',
                       value = '(-3*cw*ee*complex(0,1)*G**3)/(64.*cmath.pi**2*sw) - (3*ee*complex(0,1)*G**3*sw)/(64.*cw*cmath.pi**2)',
                       order = {'QCD':3,'QED':1})

R2GC_116_21 = Coupling(name = 'R2GC_116_21',
                       value = '(3*cw*ee*complex(0,1)*G**3)/(64.*cmath.pi**2*sw) + (3*ee*complex(0,1)*G**3*sw)/(64.*cw*cmath.pi**2)',
                       order = {'QCD':3,'QED':1})

R2GC_117_22 = Coupling(name = 'R2GC_117_22',
                       value = '(ee**2*complex(0,1)*G**2)/(288.*cmath.pi**2) + (cw**2*ee**2*complex(0,1)*G**2)/(192.*cmath.pi**2*sw**2) + (5*ee**2*complex(0,1)*G**2*sw**2)/(1728.*cw**2*cmath.pi**2)',
                       order = {'QCD':2,'QED':2})

R2GC_117_23 = Coupling(name = 'R2GC_117_23',
                       value = '-0.003472222222222222*(ee**2*complex(0,1)*G**2)/cmath.pi**2 + (cw**2*ee**2*complex(0,1)*G**2)/(192.*cmath.pi**2*sw**2) + (17*ee**2*complex(0,1)*G**2*sw**2)/(1728.*cw**2*cmath.pi**2)',
                       order = {'QCD':2,'QED':2})

R2GC_118_24 = Coupling(name = 'R2GC_118_24',
                       value = '-0.08333333333333333*(cw*ee*complex(0,1)*G**2)/(cmath.pi**2*sw) + (ee*complex(0,1)*G**2*sw)/(36.*cw*cmath.pi**2)',
                       order = {'QCD':2,'QED':1})

R2GC_119_25 = Coupling(name = 'R2GC_119_25',
                       value = '(cw*ee*complex(0,1)*G**2)/(12.*cmath.pi**2*sw) + (ee*complex(0,1)*G**2*sw)/(36.*cw*cmath.pi**2)',
                       order = {'QCD':2,'QED':1})

R2GC_121_26 = Coupling(name = 'R2GC_121_26',
                       value = '-0.0625*(complex(0,1)*G**2*yb**2)/cmath.pi**2 - (complex(0,1)*G**2*yt**2)/(16.*cmath.pi**2)',
                       order = {'QCD':2,'QED':2})

R2GC_122_27 = Coupling(name = 'R2GC_122_27',
                       value = '(ee**2*complex(0,1)*G**2)/(96.*cmath.pi**2*sw**2)',
                       order = {'QCD':2,'QED':2})

R2GC_137_28 = Coupling(name = 'R2GC_137_28',
                       value = '-0.005208333333333333*G**4/cmath.pi**2',
                       order = {'QCD':4})

R2GC_137_29 = Coupling(name = 'R2GC_137_29',
                       value = 'G**4/(64.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_138_30 = Coupling(name = 'R2GC_138_30',
                       value = '-0.005208333333333333*(complex(0,1)*G**4)/cmath.pi**2',
                       order = {'QCD':4})

R2GC_138_31 = Coupling(name = 'R2GC_138_31',
                       value = '(complex(0,1)*G**4)/(64.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_139_32 = Coupling(name = 'R2GC_139_32',
                       value = '(complex(0,1)*G**4)/(192.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_139_33 = Coupling(name = 'R2GC_139_33',
                       value = '-0.015625*(complex(0,1)*G**4)/cmath.pi**2',
                       order = {'QCD':4})

R2GC_140_34 = Coupling(name = 'R2GC_140_34',
                       value = '-0.020833333333333332*(complex(0,1)*G**4)/cmath.pi**2',
                       order = {'QCD':4})

R2GC_141_35 = Coupling(name = 'R2GC_141_35',
                       value = '(complex(0,1)*G**4)/(288.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_141_36 = Coupling(name = 'R2GC_141_36',
                       value = '-0.03125*(complex(0,1)*G**4)/cmath.pi**2',
                       order = {'QCD':4})

R2GC_143_37 = Coupling(name = 'R2GC_143_37',
                       value = '-0.0625*(complex(0,1)*G**4)/cmath.pi**2',
                       order = {'QCD':4})

R2GC_143_38 = Coupling(name = 'R2GC_143_38',
                       value = '(complex(0,1)*G**4)/(4.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_144_39 = Coupling(name = 'R2GC_144_39',
                       value = '(-3*complex(0,1)*G**4)/(64.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_144_40 = Coupling(name = 'R2GC_144_40',
                       value = '(-23*complex(0,1)*G**4)/(64.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_147_41 = Coupling(name = 'R2GC_147_41',
                       value = '(complex(0,1)*G**2)/(12.*cmath.pi**2)',
                       order = {'QCD':2})

R2GC_149_42 = Coupling(name = 'R2GC_149_42',
                       value = '(13*complex(0,1)*G**4)/(384.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_150_43 = Coupling(name = 'R2GC_150_43',
                       value = '-0.013888888888888888*(complex(0,1)*G**2)/cmath.pi**2',
                       order = {'QCD':2})

R2GC_151_44 = Coupling(name = 'R2GC_151_44',
                       value = '-0.004629629629629629*(ee*complex(0,1)*G**2)/cmath.pi**2',
                       order = {'QCD':2,'QED':1})

R2GC_152_45 = Coupling(name = 'R2GC_152_45',
                       value = '-0.0030864197530864196*(ee**2*complex(0,1)*G**2)/cmath.pi**2',
                       order = {'QCD':2,'QED':2})

R2GC_153_46 = Coupling(name = 'R2GC_153_46',
                       value = '(ee*complex(0,1)*G**2*sw)/(216.*cw*cmath.pi**2)',
                       order = {'QCD':2,'QED':1})

R2GC_154_47 = Coupling(name = 'R2GC_154_47',
                       value = '(ee**2*complex(0,1)*G**2*sw)/(324.*cw*cmath.pi**2)',
                       order = {'QCD':2,'QED':2})

R2GC_155_48 = Coupling(name = 'R2GC_155_48',
                       value = '-0.0030864197530864196*(ee**2*complex(0,1)*G**2*sw**2)/(cw**2*cmath.pi**2)',
                       order = {'QCD':2,'QED':2})

R2GC_156_49 = Coupling(name = 'R2GC_156_49',
                       value = '(complex(0,1)*G**2*lamYdH*vev)/(24.*cmath.pi**2)',
                       order = {'NP':1,'QCD':2,'QED':-1})

R2GC_159_50 = Coupling(name = 'R2GC_159_50',
                       value = '(ee*complex(0,1)*G**2)/(108.*cmath.pi**2)',
                       order = {'QCD':2,'QED':1})

R2GC_160_51 = Coupling(name = 'R2GC_160_51',
                       value = '-0.012345679012345678*(ee**2*complex(0,1)*G**2)/cmath.pi**2',
                       order = {'QCD':2,'QED':2})

R2GC_161_52 = Coupling(name = 'R2GC_161_52',
                       value = '-0.009259259259259259*(ee*complex(0,1)*G**2*sw)/(cw*cmath.pi**2)',
                       order = {'QCD':2,'QED':1})

R2GC_162_53 = Coupling(name = 'R2GC_162_53',
                       value = '(ee**2*complex(0,1)*G**2*sw)/(81.*cw*cmath.pi**2)',
                       order = {'QCD':2,'QED':2})

R2GC_163_54 = Coupling(name = 'R2GC_163_54',
                       value = '-0.012345679012345678*(ee**2*complex(0,1)*G**2*sw**2)/(cw**2*cmath.pi**2)',
                       order = {'QCD':2,'QED':2})

R2GC_164_55 = Coupling(name = 'R2GC_164_55',
                       value = '(complex(0,1)*G**2*lamYuH*vev)/(24.*cmath.pi**2)',
                       order = {'NP':1,'QCD':2,'QED':-1})

R2GC_169_56 = Coupling(name = 'R2GC_169_56',
                       value = '(complex(0,1)*G**2*yFqR)/(24.*cmath.pi**2)',
                       order = {'NP':1,'QCD':2})

R2GC_170_57 = Coupling(name = 'R2GC_170_57',
                       value = '-0.16666666666666666*(ee*complex(0,1)*G**2)/(cmath.pi**2*sw*cmath.sqrt(2))',
                       order = {'QCD':2,'QED':1})

R2GC_177_58 = Coupling(name = 'R2GC_177_58',
                       value = '(complex(0,1)*G**2*MB)/(6.*cmath.pi**2)',
                       order = {'QCD':2})

R2GC_180_59 = Coupling(name = 'R2GC_180_59',
                       value = '(complex(0,1)*G**2*yb)/(3.*cmath.pi**2*cmath.sqrt(2))',
                       order = {'QCD':2,'QED':1})

R2GC_181_60 = Coupling(name = 'R2GC_181_60',
                       value = '-0.3333333333333333*(G**2*yb)/(cmath.pi**2*cmath.sqrt(2))',
                       order = {'QCD':2,'QED':1})

R2GC_182_61 = Coupling(name = 'R2GC_182_61',
                       value = '(complex(0,1)*G**2*yFbR)/(24.*cmath.pi**2)',
                       order = {'NP':1,'QCD':2})

R2GC_185_62 = Coupling(name = 'R2GC_185_62',
                       value = '(complex(0,1)*G**2*MT)/(6.*cmath.pi**2)',
                       order = {'QCD':2})

R2GC_189_63 = Coupling(name = 'R2GC_189_63',
                       value = '(G**2*yb)/(3.*cmath.pi**2)',
                       order = {'QCD':2,'QED':1})

R2GC_190_64 = Coupling(name = 'R2GC_190_64',
                       value = '-0.3333333333333333*(G**2*yb)/cmath.pi**2',
                       order = {'QCD':2,'QED':1})

R2GC_191_65 = Coupling(name = 'R2GC_191_65',
                       value = '(complex(0,1)*G**2*yFtR)/(24.*cmath.pi**2)',
                       order = {'NP':1,'QCD':2})

R2GC_192_66 = Coupling(name = 'R2GC_192_66',
                       value = '(G**2*yt)/(3.*cmath.pi**2)',
                       order = {'QCD':2,'QED':1})

R2GC_193_67 = Coupling(name = 'R2GC_193_67',
                       value = '-0.3333333333333333*(G**2*yt)/cmath.pi**2',
                       order = {'QCD':2,'QED':1})

R2GC_194_68 = Coupling(name = 'R2GC_194_68',
                       value = '(G**2*yt)/(3.*cmath.pi**2*cmath.sqrt(2))',
                       order = {'QCD':2,'QED':1})

R2GC_195_69 = Coupling(name = 'R2GC_195_69',
                       value = '(complex(0,1)*G**2*yt)/(3.*cmath.pi**2*cmath.sqrt(2))',
                       order = {'QCD':2,'QED':1})

R2GC_196_70 = Coupling(name = 'R2GC_196_70',
                       value = '(complex(0,1)*G**2*MYd**2)/(24.*cmath.pi**2)',
                       order = {'QCD':2})

R2GC_197_71 = Coupling(name = 'R2GC_197_71',
                       value = '(complex(0,1)*G**2)/(48.*cmath.pi**2)',
                       order = {'QCD':2})

R2GC_197_72 = Coupling(name = 'R2GC_197_72',
                       value = '(3*complex(0,1)*G**2)/(32.*cmath.pi**2)',
                       order = {'QCD':2})

R2GC_198_73 = Coupling(name = 'R2GC_198_73',
                       value = '-0.0625*(complex(0,1)*G**2)/cmath.pi**2',
                       order = {'QCD':2})

R2GC_199_74 = Coupling(name = 'R2GC_199_74',
                       value = 'G**3/(24.*cmath.pi**2)',
                       order = {'QCD':3})

R2GC_199_75 = Coupling(name = 'R2GC_199_75',
                       value = '(11*G**3)/(64.*cmath.pi**2)',
                       order = {'QCD':3})

R2GC_202_76 = Coupling(name = 'R2GC_202_76',
                       value = '(53*complex(0,1)*G**3)/(576.*cmath.pi**2)',
                       order = {'QCD':3})

R2GC_207_77 = Coupling(name = 'R2GC_207_77',
                       value = '-0.041666666666666664*G**3/cmath.pi**2',
                       order = {'QCD':3})

R2GC_207_78 = Coupling(name = 'R2GC_207_78',
                       value = '(-11*G**3)/(64.*cmath.pi**2)',
                       order = {'QCD':3})

R2GC_210_79 = Coupling(name = 'R2GC_210_79',
                       value = '(53*ee*complex(0,1)*G**3)/(864.*cmath.pi**2)',
                       order = {'QCD':3,'QED':1})

R2GC_211_80 = Coupling(name = 'R2GC_211_80',
                       value = '(-53*ee*complex(0,1)*G**3)/(432.*cmath.pi**2)',
                       order = {'QCD':3,'QED':1})

R2GC_212_81 = Coupling(name = 'R2GC_212_81',
                       value = '(-3*complex(0,1)*G**4)/(32.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_212_82 = Coupling(name = 'R2GC_212_82',
                       value = '(-79*complex(0,1)*G**4)/(1152.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_214_83 = Coupling(name = 'R2GC_214_83',
                       value = '(23*complex(0,1)*G**4)/(192.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_215_84 = Coupling(name = 'R2GC_215_84',
                       value = '(31*complex(0,1)*G**4)/(64.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_216_85 = Coupling(name = 'R2GC_216_85',
                       value = '(5*complex(0,1)*G**4)/(48.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_216_86 = Coupling(name = 'R2GC_216_86',
                       value = '(19*complex(0,1)*G**4)/(32.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_217_87 = Coupling(name = 'R2GC_217_87',
                       value = '(-17*complex(0,1)*G**4)/(64.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_218_88 = Coupling(name = 'R2GC_218_88',
                       value = '(-7*complex(0,1)*G**4)/(32.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_219_89 = Coupling(name = 'R2GC_219_89',
                       value = '(7*complex(0,1)*G**4)/(64.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_220_90 = Coupling(name = 'R2GC_220_90',
                       value = '(-53*ee*complex(0,1)*G**3*sw)/(864.*cw*cmath.pi**2)',
                       order = {'QCD':3,'QED':1})

R2GC_221_91 = Coupling(name = 'R2GC_221_91',
                       value = '(53*ee*complex(0,1)*G**3*sw)/(432.*cw*cmath.pi**2)',
                       order = {'QCD':3,'QED':1})

R2GC_222_92 = Coupling(name = 'R2GC_222_92',
                       value = '(complex(0,1)*G**2*MYu**2)/(24.*cmath.pi**2)',
                       order = {'QCD':2})

UVGC_124_1 = Coupling(name = 'UVGC_124_1',
                      value = {-1:'-0.08333333333333333*(complex(0,1)*G**2)/cmath.pi**2'},
                      order = {'QCD':2})

UVGC_125_2 = Coupling(name = 'UVGC_125_2',
                      value = {-1:'-0.05555555555555555*(ee*complex(0,1)*G**2)/cmath.pi**2'},
                      order = {'QCD':2,'QED':1})

UVGC_126_3 = Coupling(name = 'UVGC_126_3',
                      value = {-1:'(-13*complex(0,1)*G**3)/(48.*cmath.pi**2)'},
                      order = {'QCD':3})

UVGC_128_4 = Coupling(name = 'UVGC_128_4',
                      value = {-1:'(ee*complex(0,1)*G**2)/(36.*cmath.pi**2)'},
                      order = {'QCD':2,'QED':1})

UVGC_136_5 = Coupling(name = 'UVGC_136_5',
                      value = {-1:'(9*G**3)/(128.*cmath.pi**2)'},
                      order = {'QCD':3})

UVGC_136_6 = Coupling(name = 'UVGC_136_6',
                      value = {-1:'-0.0078125*G**3/cmath.pi**2'},
                      order = {'QCD':3})

UVGC_137_7 = Coupling(name = 'UVGC_137_7',
                      value = {-1:'(3*G**4)/(512.*cmath.pi**2)'},
                      order = {'QCD':4})

UVGC_137_8 = Coupling(name = 'UVGC_137_8',
                      value = {-1:'(-3*G**4)/(512.*cmath.pi**2)'},
                      order = {'QCD':4})

UVGC_138_9 = Coupling(name = 'UVGC_138_9',
                      value = {-1:'(3*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                      order = {'QCD':4})

UVGC_138_10 = Coupling(name = 'UVGC_138_10',
                       value = {-1:'(-3*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_140_11 = Coupling(name = 'UVGC_140_11',
                       value = {-1:'-0.0078125*(complex(0,1)*G**4)/cmath.pi**2'},
                       order = {'QCD':4})

UVGC_140_12 = Coupling(name = 'UVGC_140_12',
                       value = {-1:'(complex(0,1)*G**4)/(128.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_141_13 = Coupling(name = 'UVGC_141_13',
                       value = {-1:'(-3*complex(0,1)*G**4)/(256.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_141_14 = Coupling(name = 'UVGC_141_14',
                       value = {-1:'(3*complex(0,1)*G**4)/(256.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_142_15 = Coupling(name = 'UVGC_142_15',
                       value = {-1:'(-9*G**3)/(128.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_142_16 = Coupling(name = 'UVGC_142_16',
                       value = {-1:'G**3/(128.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_142_17 = Coupling(name = 'UVGC_142_17',
                       value = {-1:'G**3/(96.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_143_18 = Coupling(name = 'UVGC_143_18',
                       value = {-1:'-0.041666666666666664*(complex(0,1)*G**4)/cmath.pi**2'},
                       order = {'QCD':4})

UVGC_143_19 = Coupling(name = 'UVGC_143_19',
                       value = {-1:'(47*complex(0,1)*G**4)/(128.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_143_20 = Coupling(name = 'UVGC_143_20',
                       value = {-1:'(complex(0,1)*G**4)/(48.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_144_21 = Coupling(name = 'UVGC_144_21',
                       value = {-1:'(-253*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_144_22 = Coupling(name = 'UVGC_144_22',
                       value = {-1:'(5*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_147_23 = Coupling(name = 'UVGC_147_23',
                       value = {-1:'(complex(0,1)*G**2)/(12.*cmath.pi**2)'},
                       order = {'QCD':2})

UVGC_149_24 = Coupling(name = 'UVGC_149_24',
                       value = {-1:'(-3*complex(0,1)*G**4)/(64.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_149_25 = Coupling(name = 'UVGC_149_25',
                       value = {-1:'(3*complex(0,1)*G**4)/(64.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_150_26 = Coupling(name = 'UVGC_150_26',
                       value = {-1:'( -0.16666666666666666*(complex(0,1)*G**2)/cmath.pi**2 if MYd else -0.16666666666666666*(complex(0,1)*G**2)/cmath.pi**2 ) + (complex(0,1)*G**2)/(6.*cmath.pi**2)',0:'( (complex(0,1)*G**2)/(72.*cmath.pi**2) if MYd else (complex(0,1)*G**2)/(72.*cmath.pi**2) ) - (complex(0,1)*G**2)/(72.*cmath.pi**2)'},
                       order = {'QCD':2})

UVGC_151_27 = Coupling(name = 'UVGC_151_27',
                       value = {-1:'( -0.05555555555555555*(ee*complex(0,1)*G**2)/cmath.pi**2 if MYd else -0.05555555555555555*(ee*complex(0,1)*G**2)/cmath.pi**2 ) + (ee*complex(0,1)*G**2)/(18.*cmath.pi**2)',0:'( (ee*complex(0,1)*G**2)/(216.*cmath.pi**2) if MYd else (ee*complex(0,1)*G**2)/(216.*cmath.pi**2) ) - (ee*complex(0,1)*G**2)/(216.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_152_28 = Coupling(name = 'UVGC_152_28',
                       value = {-1:'( -0.037037037037037035*(ee**2*complex(0,1)*G**2)/cmath.pi**2 if MYd else -0.037037037037037035*(ee**2*complex(0,1)*G**2)/cmath.pi**2 ) + (ee**2*complex(0,1)*G**2)/(27.*cmath.pi**2)',0:'( (ee**2*complex(0,1)*G**2)/(324.*cmath.pi**2) if MYd else (ee**2*complex(0,1)*G**2)/(324.*cmath.pi**2) ) - (ee**2*complex(0,1)*G**2)/(324.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':2})

UVGC_153_29 = Coupling(name = 'UVGC_153_29',
                       value = {-1:'( (ee*complex(0,1)*G**2*sw)/(18.*cw*cmath.pi**2) if MYd else (ee*complex(0,1)*G**2*sw)/(18.*cw*cmath.pi**2) ) - (ee*complex(0,1)*G**2*sw)/(18.*cw*cmath.pi**2)',0:'( -0.004629629629629629*(ee*complex(0,1)*G**2*sw)/(cw*cmath.pi**2) if MYd else -0.004629629629629629*(ee*complex(0,1)*G**2*sw)/(cw*cmath.pi**2) ) + (ee*complex(0,1)*G**2*sw)/(216.*cw*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_154_30 = Coupling(name = 'UVGC_154_30',
                       value = {-1:'( (ee**2*complex(0,1)*G**2*sw)/(27.*cw*cmath.pi**2) if MYd else (ee**2*complex(0,1)*G**2*sw)/(27.*cw*cmath.pi**2) ) - (ee**2*complex(0,1)*G**2*sw)/(27.*cw*cmath.pi**2)',0:'( -0.0030864197530864196*(ee**2*complex(0,1)*G**2*sw)/(cw*cmath.pi**2) if MYd else -0.0030864197530864196*(ee**2*complex(0,1)*G**2*sw)/(cw*cmath.pi**2) ) + (ee**2*complex(0,1)*G**2*sw)/(324.*cw*cmath.pi**2)'},
                       order = {'QCD':2,'QED':2})

UVGC_155_31 = Coupling(name = 'UVGC_155_31',
                       value = {-1:'( -0.037037037037037035*(ee**2*complex(0,1)*G**2*sw**2)/(cw**2*cmath.pi**2) if MYd else -0.037037037037037035*(ee**2*complex(0,1)*G**2*sw**2)/(cw**2*cmath.pi**2) ) + (ee**2*complex(0,1)*G**2*sw**2)/(27.*cw**2*cmath.pi**2)',0:'( (ee**2*complex(0,1)*G**2*sw**2)/(324.*cw**2*cmath.pi**2) if MYd else (ee**2*complex(0,1)*G**2*sw**2)/(324.*cw**2*cmath.pi**2) ) - (ee**2*complex(0,1)*G**2*sw**2)/(324.*cw**2*cmath.pi**2)'},
                       order = {'QCD':2,'QED':2})

UVGC_156_32 = Coupling(name = 'UVGC_156_32',
                       value = {-1:'( (complex(0,1)*G**2*lamYdH*vev)/(6.*cmath.pi**2) if MYd else (complex(0,1)*G**2*lamYdH*vev)/(6.*cmath.pi**2) ) + (complex(0,1)*G**2*lamYdH*vev)/(12.*cmath.pi**2)',0:'( -0.013888888888888888*(complex(0,1)*G**2*lamYdH*vev)/cmath.pi**2 if MYd else -0.013888888888888888*(complex(0,1)*G**2*lamYdH*vev)/cmath.pi**2 ) + (complex(0,1)*G**2*lamYdH*vev)/(72.*cmath.pi**2)'},
                       order = {'NP':1,'QCD':2,'QED':-1})

UVGC_158_33 = Coupling(name = 'UVGC_158_33',
                       value = {-1:'( -0.16666666666666666*(complex(0,1)*G**2)/cmath.pi**2 if MYu else -0.16666666666666666*(complex(0,1)*G**2)/cmath.pi**2 ) + (complex(0,1)*G**2)/(6.*cmath.pi**2)',0:'( (complex(0,1)*G**2)/(72.*cmath.pi**2) if MYu else (complex(0,1)*G**2)/(72.*cmath.pi**2) ) - (complex(0,1)*G**2)/(72.*cmath.pi**2)'},
                       order = {'QCD':2})

UVGC_159_34 = Coupling(name = 'UVGC_159_34',
                       value = {-1:'( (ee*complex(0,1)*G**2)/(9.*cmath.pi**2) if MYu else (ee*complex(0,1)*G**2)/(9.*cmath.pi**2) ) - (ee*complex(0,1)*G**2)/(9.*cmath.pi**2)',0:'( -0.009259259259259259*(ee*complex(0,1)*G**2)/cmath.pi**2 if MYu else -0.009259259259259259*(ee*complex(0,1)*G**2)/cmath.pi**2 ) + (ee*complex(0,1)*G**2)/(108.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_160_35 = Coupling(name = 'UVGC_160_35',
                       value = {-1:'( (-4*ee**2*complex(0,1)*G**2)/(27.*cmath.pi**2) if MYu else (-4*ee**2*complex(0,1)*G**2)/(27.*cmath.pi**2) ) + (4*ee**2*complex(0,1)*G**2)/(27.*cmath.pi**2)',0:'( (ee**2*complex(0,1)*G**2)/(81.*cmath.pi**2) if MYu else (ee**2*complex(0,1)*G**2)/(81.*cmath.pi**2) ) - (ee**2*complex(0,1)*G**2)/(81.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':2})

UVGC_161_36 = Coupling(name = 'UVGC_161_36',
                       value = {-1:'( -0.1111111111111111*(ee*complex(0,1)*G**2*sw)/(cw*cmath.pi**2) if MYu else -0.1111111111111111*(ee*complex(0,1)*G**2*sw)/(cw*cmath.pi**2) ) + (ee*complex(0,1)*G**2*sw)/(9.*cw*cmath.pi**2)',0:'( (ee*complex(0,1)*G**2*sw)/(108.*cw*cmath.pi**2) if MYu else (ee*complex(0,1)*G**2*sw)/(108.*cw*cmath.pi**2) ) - (ee*complex(0,1)*G**2*sw)/(108.*cw*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_162_37 = Coupling(name = 'UVGC_162_37',
                       value = {-1:'( (4*ee**2*complex(0,1)*G**2*sw)/(27.*cw*cmath.pi**2) if MYu else (4*ee**2*complex(0,1)*G**2*sw)/(27.*cw*cmath.pi**2) ) - (4*ee**2*complex(0,1)*G**2*sw)/(27.*cw*cmath.pi**2)',0:'( -0.012345679012345678*(ee**2*complex(0,1)*G**2*sw)/(cw*cmath.pi**2) if MYu else -0.012345679012345678*(ee**2*complex(0,1)*G**2*sw)/(cw*cmath.pi**2) ) + (ee**2*complex(0,1)*G**2*sw)/(81.*cw*cmath.pi**2)'},
                       order = {'QCD':2,'QED':2})

UVGC_163_38 = Coupling(name = 'UVGC_163_38',
                       value = {-1:'( (-4*ee**2*complex(0,1)*G**2*sw**2)/(27.*cw**2*cmath.pi**2) if MYu else (-4*ee**2*complex(0,1)*G**2*sw**2)/(27.*cw**2*cmath.pi**2) ) + (4*ee**2*complex(0,1)*G**2*sw**2)/(27.*cw**2*cmath.pi**2)',0:'( (ee**2*complex(0,1)*G**2*sw**2)/(81.*cw**2*cmath.pi**2) if MYu else (ee**2*complex(0,1)*G**2*sw**2)/(81.*cw**2*cmath.pi**2) ) - (ee**2*complex(0,1)*G**2*sw**2)/(81.*cw**2*cmath.pi**2)'},
                       order = {'QCD':2,'QED':2})

UVGC_164_39 = Coupling(name = 'UVGC_164_39',
                       value = {-1:'( (complex(0,1)*G**2*lamYuH*vev)/(6.*cmath.pi**2) if MYu else (complex(0,1)*G**2*lamYuH*vev)/(6.*cmath.pi**2) ) + (complex(0,1)*G**2*lamYuH*vev)/(12.*cmath.pi**2)',0:'( -0.013888888888888888*(complex(0,1)*G**2*lamYuH*vev)/cmath.pi**2 if MYu else -0.013888888888888888*(complex(0,1)*G**2*lamYuH*vev)/cmath.pi**2 ) + (complex(0,1)*G**2*lamYuH*vev)/(72.*cmath.pi**2)'},
                       order = {'NP':1,'QCD':2,'QED':-1})

UVGC_169_40 = Coupling(name = 'UVGC_169_40',
                       value = {-1:'-0.041666666666666664*(complex(0,1)*G**2*yFqR)/cmath.pi**2'},
                       order = {'NP':1,'QCD':2})

UVGC_169_41 = Coupling(name = 'UVGC_169_41',
                       value = {-1:'( (complex(0,1)*G**2*yFqR)/(12.*cmath.pi**2) if MYu else (complex(0,1)*G**2*yFqR)/(12.*cmath.pi**2) )',0:'( -0.006944444444444444*(complex(0,1)*G**2*yFqR)/cmath.pi**2 if MYu else -0.006944444444444444*(complex(0,1)*G**2*yFqR)/cmath.pi**2 ) + (complex(0,1)*G**2*yFqR)/(144.*cmath.pi**2)'},
                       order = {'NP':1,'QCD':2})

UVGC_169_42 = Coupling(name = 'UVGC_169_42',
                       value = {-1:'(complex(0,1)*G**2*yFqR)/(12.*cmath.pi**2)'},
                       order = {'NP':1,'QCD':2})

UVGC_170_43 = Coupling(name = 'UVGC_170_43',
                       value = {-1:'(ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_170_44 = Coupling(name = 'UVGC_170_44',
                       value = {-1:'-0.08333333333333333*(ee*complex(0,1)*G**2)/(cmath.pi**2*sw*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_171_45 = Coupling(name = 'UVGC_171_45',
                       value = {-1:'( (complex(0,1)*G**2*yFqR)/(12.*cmath.pi**2) if MYd else (complex(0,1)*G**2*yFqR)/(12.*cmath.pi**2) )',0:'( -0.006944444444444444*(complex(0,1)*G**2*yFqR)/cmath.pi**2 if MYd else -0.006944444444444444*(complex(0,1)*G**2*yFqR)/cmath.pi**2 ) + (complex(0,1)*G**2*yFqR)/(144.*cmath.pi**2)'},
                       order = {'NP':1,'QCD':2})

UVGC_175_46 = Coupling(name = 'UVGC_175_46',
                       value = {-1:'( (complex(0,1)*G**2)/(6.*cmath.pi**2) if MB else -0.08333333333333333*(complex(0,1)*G**2)/cmath.pi**2 ) + (complex(0,1)*G**2)/(12.*cmath.pi**2)',0:'( (5*complex(0,1)*G**2)/(12.*cmath.pi**2) - (complex(0,1)*G**2*reglog(MB/MU_R))/(2.*cmath.pi**2) if MB else (complex(0,1)*G**2)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2)/(12.*cmath.pi**2)'},
                       order = {'QCD':2})

UVGC_176_47 = Coupling(name = 'UVGC_176_47',
                       value = {-1:'( (ee*complex(0,1)*G**2)/(18.*cmath.pi**2) if MB else -0.027777777777777776*(ee*complex(0,1)*G**2)/cmath.pi**2 )',0:'( (5*ee*complex(0,1)*G**2)/(36.*cmath.pi**2) - (ee*complex(0,1)*G**2*reglog(MB/MU_R))/(6.*cmath.pi**2) if MB else (ee*complex(0,1)*G**2)/(36.*cmath.pi**2) ) - (ee*complex(0,1)*G**2)/(36.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_177_48 = Coupling(name = 'UVGC_177_48',
                       value = {-1:'( (complex(0,1)*G**2*MB)/(6.*cmath.pi**2) if MB else -0.08333333333333333*(complex(0,1)*G**2*MB)/cmath.pi**2 ) + (complex(0,1)*G**2*MB)/(3.*cmath.pi**2)',0:'( (3*complex(0,1)*G**2*MB)/(4.*cmath.pi**2) - (complex(0,1)*G**2*MB*reglog(MB/MU_R))/cmath.pi**2 if MB else (complex(0,1)*G**2*MB)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2*MB)/(12.*cmath.pi**2)'},
                       order = {'QCD':2})

UVGC_178_49 = Coupling(name = 'UVGC_178_49',
                       value = {-1:'( (cw*ee*complex(0,1)*G**2)/(12.*cmath.pi**2*sw) + (ee*complex(0,1)*G**2*sw)/(36.*cw*cmath.pi**2) if MB else -0.041666666666666664*(cw*ee*complex(0,1)*G**2)/(cmath.pi**2*sw) - (ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2) ) + (cw*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw) + (ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2)',0:'( (5*cw*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw) + (5*ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2) - (cw*ee*complex(0,1)*G**2*reglog(MB/MU_R))/(4.*cmath.pi**2*sw) - (ee*complex(0,1)*G**2*sw*reglog(MB/MU_R))/(12.*cw*cmath.pi**2) if MB else (cw*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw) + (ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2) ) - (cw*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw) - (ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_179_50 = Coupling(name = 'UVGC_179_50',
                       value = {-1:'( -0.05555555555555555*(ee*complex(0,1)*G**2*sw)/(cw*cmath.pi**2) if MB else (ee*complex(0,1)*G**2*sw)/(36.*cw*cmath.pi**2) ) - (ee*complex(0,1)*G**2*sw)/(36.*cw*cmath.pi**2)',0:'( (-5*ee*complex(0,1)*G**2*sw)/(36.*cw*cmath.pi**2) + (ee*complex(0,1)*G**2*sw*reglog(MB/MU_R))/(6.*cw*cmath.pi**2) if MB else -0.027777777777777776*(ee*complex(0,1)*G**2*sw)/(cw*cmath.pi**2) ) + (ee*complex(0,1)*G**2*sw)/(36.*cw*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_180_51 = Coupling(name = 'UVGC_180_51',
                       value = {-1:'( (complex(0,1)*G**2*yb)/(6.*cmath.pi**2*cmath.sqrt(2)) if MB else -0.08333333333333333*(complex(0,1)*G**2*yb)/(cmath.pi**2*cmath.sqrt(2)) ) + (complex(0,1)*G**2*yb)/(3.*cmath.pi**2*cmath.sqrt(2))',0:'( (3*complex(0,1)*G**2*yb)/(4.*cmath.pi**2*cmath.sqrt(2)) - (complex(0,1)*G**2*yb*reglog(MB/MU_R))/(cmath.pi**2*cmath.sqrt(2)) if MB else (complex(0,1)*G**2*yb)/(12.*cmath.pi**2*cmath.sqrt(2)) ) - (complex(0,1)*G**2*yb)/(12.*cmath.pi**2*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_181_52 = Coupling(name = 'UVGC_181_52',
                       value = {-1:'( -0.16666666666666666*(G**2*yb)/(cmath.pi**2*cmath.sqrt(2)) if MB else (G**2*yb)/(12.*cmath.pi**2*cmath.sqrt(2)) ) - (G**2*yb)/(3.*cmath.pi**2*cmath.sqrt(2))',0:'( (-3*G**2*yb)/(4.*cmath.pi**2*cmath.sqrt(2)) + (G**2*yb*reglog(MB/MU_R))/(cmath.pi**2*cmath.sqrt(2)) if MB else -0.08333333333333333*(G**2*yb)/(cmath.pi**2*cmath.sqrt(2)) ) + (G**2*yb)/(12.*cmath.pi**2*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_182_53 = Coupling(name = 'UVGC_182_53',
                       value = {-1:'( (complex(0,1)*G**2*yFbR)/(12.*cmath.pi**2) if MB else -0.041666666666666664*(complex(0,1)*G**2*yFbR)/cmath.pi**2 )',0:'( (5*complex(0,1)*G**2*yFbR)/(24.*cmath.pi**2) - (complex(0,1)*G**2*yFbR*reglog(MB/MU_R))/(4.*cmath.pi**2) if MB else (complex(0,1)*G**2*yFbR)/(24.*cmath.pi**2) ) - (complex(0,1)*G**2*yFbR)/(24.*cmath.pi**2)'},
                       order = {'NP':1,'QCD':2})

UVGC_182_54 = Coupling(name = 'UVGC_182_54',
                       value = {-1:'( (complex(0,1)*G**2*yFbR)/(12.*cmath.pi**2) if MYd else (complex(0,1)*G**2*yFbR)/(12.*cmath.pi**2) )',0:'( -0.006944444444444444*(complex(0,1)*G**2*yFbR)/cmath.pi**2 if MYd else -0.006944444444444444*(complex(0,1)*G**2*yFbR)/cmath.pi**2 ) + (complex(0,1)*G**2*yFbR)/(144.*cmath.pi**2)'},
                       order = {'NP':1,'QCD':2})

UVGC_182_55 = Coupling(name = 'UVGC_182_55',
                       value = {-1:'(complex(0,1)*G**2*yFbR)/(12.*cmath.pi**2)'},
                       order = {'NP':1,'QCD':2})

UVGC_183_56 = Coupling(name = 'UVGC_183_56',
                       value = {-1:'( (complex(0,1)*G**2)/(6.*cmath.pi**2) if MT else -0.08333333333333333*(complex(0,1)*G**2)/cmath.pi**2 ) + (complex(0,1)*G**2)/(12.*cmath.pi**2)',0:'( (5*complex(0,1)*G**2)/(12.*cmath.pi**2) - (complex(0,1)*G**2*reglog(MT/MU_R))/(2.*cmath.pi**2) if MT else (complex(0,1)*G**2)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2)/(12.*cmath.pi**2)'},
                       order = {'QCD':2})

UVGC_184_57 = Coupling(name = 'UVGC_184_57',
                       value = {-1:'( -0.1111111111111111*(ee*complex(0,1)*G**2)/cmath.pi**2 if MT else (ee*complex(0,1)*G**2)/(18.*cmath.pi**2) )',0:'( (-5*ee*complex(0,1)*G**2)/(18.*cmath.pi**2) + (ee*complex(0,1)*G**2*reglog(MT/MU_R))/(3.*cmath.pi**2) if MT else -0.05555555555555555*(ee*complex(0,1)*G**2)/cmath.pi**2 ) + (ee*complex(0,1)*G**2)/(18.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_185_58 = Coupling(name = 'UVGC_185_58',
                       value = {-1:'( (complex(0,1)*G**2*MT)/(6.*cmath.pi**2) if MT else -0.08333333333333333*(complex(0,1)*G**2*MT)/cmath.pi**2 ) + (complex(0,1)*G**2*MT)/(3.*cmath.pi**2)',0:'( (3*complex(0,1)*G**2*MT)/(4.*cmath.pi**2) - (complex(0,1)*G**2*MT*reglog(MT/MU_R))/cmath.pi**2 if MT else (complex(0,1)*G**2*MT)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2*MT)/(12.*cmath.pi**2)'},
                       order = {'QCD':2})

UVGC_186_59 = Coupling(name = 'UVGC_186_59',
                       value = {-1:'( -0.08333333333333333*(ee*complex(0,1)*G**2)/(cmath.pi**2*sw*cmath.sqrt(2)) if MB else (ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2)) )',0:'( (-5*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2)) + (ee*complex(0,1)*G**2*reglog(MB/MU_R))/(4.*cmath.pi**2*sw*cmath.sqrt(2)) if MB else -0.041666666666666664*(ee*complex(0,1)*G**2)/(cmath.pi**2*sw*cmath.sqrt(2)) ) + (ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_186_60 = Coupling(name = 'UVGC_186_60',
                       value = {-1:'( -0.08333333333333333*(ee*complex(0,1)*G**2)/(cmath.pi**2*sw*cmath.sqrt(2)) if MT else (ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2)) )',0:'( (-5*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2)) + (ee*complex(0,1)*G**2*reglog(MT/MU_R))/(4.*cmath.pi**2*sw*cmath.sqrt(2)) if MT else -0.041666666666666664*(ee*complex(0,1)*G**2)/(cmath.pi**2*sw*cmath.sqrt(2)) ) + (ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_187_61 = Coupling(name = 'UVGC_187_61',
                       value = {-1:'( -0.08333333333333333*(cw*ee*complex(0,1)*G**2)/(cmath.pi**2*sw) + (ee*complex(0,1)*G**2*sw)/(36.*cw*cmath.pi**2) if MT else (cw*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw) - (ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2) ) - (cw*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw) + (ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2)',0:'( (-5*cw*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw) + (5*ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2) + (cw*ee*complex(0,1)*G**2*reglog(MT/MU_R))/(4.*cmath.pi**2*sw) - (ee*complex(0,1)*G**2*sw*reglog(MT/MU_R))/(12.*cw*cmath.pi**2) if MT else -0.041666666666666664*(cw*ee*complex(0,1)*G**2)/(cmath.pi**2*sw) + (ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2) ) + (cw*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw) - (ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_188_62 = Coupling(name = 'UVGC_188_62',
                       value = {-1:'( (ee*complex(0,1)*G**2*sw)/(9.*cw*cmath.pi**2) if MT else -0.05555555555555555*(ee*complex(0,1)*G**2*sw)/(cw*cmath.pi**2) ) + (ee*complex(0,1)*G**2*sw)/(18.*cw*cmath.pi**2)',0:'( (5*ee*complex(0,1)*G**2*sw)/(18.*cw*cmath.pi**2) - (ee*complex(0,1)*G**2*sw*reglog(MT/MU_R))/(3.*cw*cmath.pi**2) if MT else (ee*complex(0,1)*G**2*sw)/(18.*cw*cmath.pi**2) ) - (ee*complex(0,1)*G**2*sw)/(18.*cw*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_189_63 = Coupling(name = 'UVGC_189_63',
                       value = {-1:'( (G**2*yb)/(12.*cmath.pi**2) if MB else -0.041666666666666664*(G**2*yb)/cmath.pi**2 )',0:'( (13*G**2*yb)/(24.*cmath.pi**2) - (3*G**2*yb*reglog(MB/MU_R))/(4.*cmath.pi**2) if MB else (G**2*yb)/(24.*cmath.pi**2) ) - (G**2*yb)/(24.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_189_64 = Coupling(name = 'UVGC_189_64',
                       value = {-1:'( (G**2*yb)/(12.*cmath.pi**2) if MT else -0.041666666666666664*(G**2*yb)/cmath.pi**2 )',0:'( (5*G**2*yb)/(24.*cmath.pi**2) - (G**2*yb*reglog(MT/MU_R))/(4.*cmath.pi**2) if MT else (G**2*yb)/(24.*cmath.pi**2) ) - (G**2*yb)/(24.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_189_65 = Coupling(name = 'UVGC_189_65',
                       value = {-1:'(G**2*yb)/(3.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_190_66 = Coupling(name = 'UVGC_190_66',
                       value = {-1:'( -0.08333333333333333*(G**2*yb)/cmath.pi**2 if MB else (G**2*yb)/(24.*cmath.pi**2) )',0:'( (-13*G**2*yb)/(24.*cmath.pi**2) + (3*G**2*yb*reglog(MB/MU_R))/(4.*cmath.pi**2) if MB else -0.041666666666666664*(G**2*yb)/cmath.pi**2 ) + (G**2*yb)/(24.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_190_67 = Coupling(name = 'UVGC_190_67',
                       value = {-1:'( -0.08333333333333333*(G**2*yb)/cmath.pi**2 if MT else (G**2*yb)/(24.*cmath.pi**2) )',0:'( (-5*G**2*yb)/(24.*cmath.pi**2) + (G**2*yb*reglog(MT/MU_R))/(4.*cmath.pi**2) if MT else -0.041666666666666664*(G**2*yb)/cmath.pi**2 ) + (G**2*yb)/(24.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_190_68 = Coupling(name = 'UVGC_190_68',
                       value = {-1:'-0.3333333333333333*(G**2*yb)/cmath.pi**2'},
                       order = {'QCD':2,'QED':1})

UVGC_191_69 = Coupling(name = 'UVGC_191_69',
                       value = {-1:'( (complex(0,1)*G**2*yFtR)/(12.*cmath.pi**2) if MT else -0.041666666666666664*(complex(0,1)*G**2*yFtR)/cmath.pi**2 )',0:'( (5*complex(0,1)*G**2*yFtR)/(24.*cmath.pi**2) - (complex(0,1)*G**2*yFtR*reglog(MT/MU_R))/(4.*cmath.pi**2) if MT else (complex(0,1)*G**2*yFtR)/(24.*cmath.pi**2) ) - (complex(0,1)*G**2*yFtR)/(24.*cmath.pi**2)'},
                       order = {'NP':1,'QCD':2})

UVGC_191_70 = Coupling(name = 'UVGC_191_70',
                       value = {-1:'( (complex(0,1)*G**2*yFtR)/(12.*cmath.pi**2) if MYu else (complex(0,1)*G**2*yFtR)/(12.*cmath.pi**2) )',0:'( -0.006944444444444444*(complex(0,1)*G**2*yFtR)/cmath.pi**2 if MYu else -0.006944444444444444*(complex(0,1)*G**2*yFtR)/cmath.pi**2 ) + (complex(0,1)*G**2*yFtR)/(144.*cmath.pi**2)'},
                       order = {'NP':1,'QCD':2})

UVGC_191_71 = Coupling(name = 'UVGC_191_71',
                       value = {-1:'(complex(0,1)*G**2*yFtR)/(12.*cmath.pi**2)'},
                       order = {'NP':1,'QCD':2})

UVGC_192_72 = Coupling(name = 'UVGC_192_72',
                       value = {-1:'( (G**2*yt)/(12.*cmath.pi**2) if MB else -0.041666666666666664*(G**2*yt)/cmath.pi**2 )',0:'( (5*G**2*yt)/(24.*cmath.pi**2) - (G**2*yt*reglog(MB/MU_R))/(4.*cmath.pi**2) if MB else (G**2*yt)/(24.*cmath.pi**2) ) - (G**2*yt)/(24.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_192_73 = Coupling(name = 'UVGC_192_73',
                       value = {-1:'( (G**2*yt)/(12.*cmath.pi**2) if MT else -0.041666666666666664*(G**2*yt)/cmath.pi**2 )',0:'( (13*G**2*yt)/(24.*cmath.pi**2) - (3*G**2*yt*reglog(MT/MU_R))/(4.*cmath.pi**2) if MT else (G**2*yt)/(24.*cmath.pi**2) ) - (G**2*yt)/(24.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_192_74 = Coupling(name = 'UVGC_192_74',
                       value = {-1:'(G**2*yt)/(3.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_193_75 = Coupling(name = 'UVGC_193_75',
                       value = {-1:'( -0.08333333333333333*(G**2*yt)/cmath.pi**2 if MB else (G**2*yt)/(24.*cmath.pi**2) )',0:'( (-5*G**2*yt)/(24.*cmath.pi**2) + (G**2*yt*reglog(MB/MU_R))/(4.*cmath.pi**2) if MB else -0.041666666666666664*(G**2*yt)/cmath.pi**2 ) + (G**2*yt)/(24.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_193_76 = Coupling(name = 'UVGC_193_76',
                       value = {-1:'( -0.08333333333333333*(G**2*yt)/cmath.pi**2 if MT else (G**2*yt)/(24.*cmath.pi**2) )',0:'( (-13*G**2*yt)/(24.*cmath.pi**2) + (3*G**2*yt*reglog(MT/MU_R))/(4.*cmath.pi**2) if MT else -0.041666666666666664*(G**2*yt)/cmath.pi**2 ) + (G**2*yt)/(24.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_193_77 = Coupling(name = 'UVGC_193_77',
                       value = {-1:'-0.3333333333333333*(G**2*yt)/cmath.pi**2'},
                       order = {'QCD':2,'QED':1})

UVGC_194_78 = Coupling(name = 'UVGC_194_78',
                       value = {-1:'( (G**2*yt)/(6.*cmath.pi**2*cmath.sqrt(2)) if MT else -0.08333333333333333*(G**2*yt)/(cmath.pi**2*cmath.sqrt(2)) ) + (G**2*yt)/(3.*cmath.pi**2*cmath.sqrt(2))',0:'( (3*G**2*yt)/(4.*cmath.pi**2*cmath.sqrt(2)) - (G**2*yt*reglog(MT/MU_R))/(cmath.pi**2*cmath.sqrt(2)) if MT else (G**2*yt)/(12.*cmath.pi**2*cmath.sqrt(2)) ) - (G**2*yt)/(12.*cmath.pi**2*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_195_79 = Coupling(name = 'UVGC_195_79',
                       value = {-1:'( (complex(0,1)*G**2*yt)/(6.*cmath.pi**2*cmath.sqrt(2)) if MT else -0.08333333333333333*(complex(0,1)*G**2*yt)/(cmath.pi**2*cmath.sqrt(2)) ) + (complex(0,1)*G**2*yt)/(3.*cmath.pi**2*cmath.sqrt(2))',0:'( (3*complex(0,1)*G**2*yt)/(4.*cmath.pi**2*cmath.sqrt(2)) - (complex(0,1)*G**2*yt*reglog(MT/MU_R))/(cmath.pi**2*cmath.sqrt(2)) if MT else (complex(0,1)*G**2*yt)/(12.*cmath.pi**2*cmath.sqrt(2)) ) - (complex(0,1)*G**2*yt)/(12.*cmath.pi**2*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_196_80 = Coupling(name = 'UVGC_196_80',
                       value = {-1:'( (complex(0,1)*G**2*MYd**2)/(6.*cmath.pi**2) if MYd else (complex(0,1)*G**2*MYd**2)/(6.*cmath.pi**2) ) + (complex(0,1)*G**2*MYd**2)/(12.*cmath.pi**2)',0:'( (41*complex(0,1)*G**2*MYd**2)/(72.*cmath.pi**2) - (complex(0,1)*G**2*MYd**2*reglog(MYd/MU_R))/(2.*cmath.pi**2) if MYd else -0.013888888888888888*(complex(0,1)*G**2*MYd**2)/cmath.pi**2 ) + (complex(0,1)*G**2*MYd**2)/(72.*cmath.pi**2)'},
                       order = {'QCD':2})

UVGC_197_81 = Coupling(name = 'UVGC_197_81',
                       value = {-1:'( 0 if MB else -0.041666666666666664*(complex(0,1)*G**2)/cmath.pi**2 ) + (complex(0,1)*G**2)/(24.*cmath.pi**2)',0:'( -0.08333333333333333*(complex(0,1)*G**2*reglog(MB/MU_R))/cmath.pi**2 if MB else 0 )'},
                       order = {'QCD':2})

UVGC_197_82 = Coupling(name = 'UVGC_197_82',
                       value = {-1:'( 0 if MT else -0.041666666666666664*(complex(0,1)*G**2)/cmath.pi**2 ) + (complex(0,1)*G**2)/(24.*cmath.pi**2)',0:'( -0.08333333333333333*(complex(0,1)*G**2*reglog(MT/MU_R))/cmath.pi**2 if MT else 0 )'},
                       order = {'QCD':2})

UVGC_197_83 = Coupling(name = 'UVGC_197_83',
                       value = {-1:'( 0 if MYd else -0.010416666666666666*(complex(0,1)*G**2)/cmath.pi**2 ) + (complex(0,1)*G**2)/(96.*cmath.pi**2)',0:'( -0.010416666666666666*(complex(0,1)*G**2)/cmath.pi**2 - (complex(0,1)*G**2*reglog(MYd/MU_R))/(48.*cmath.pi**2) if MYd else -0.010416666666666666*(complex(0,1)*G**2)/cmath.pi**2 ) + (complex(0,1)*G**2)/(96.*cmath.pi**2)'},
                       order = {'QCD':2})

UVGC_197_84 = Coupling(name = 'UVGC_197_84',
                       value = {-1:'( 0 if MYu else -0.010416666666666666*(complex(0,1)*G**2)/cmath.pi**2 ) + (complex(0,1)*G**2)/(96.*cmath.pi**2)',0:'( -0.010416666666666666*(complex(0,1)*G**2)/cmath.pi**2 - (complex(0,1)*G**2*reglog(MYu/MU_R))/(48.*cmath.pi**2) if MYu else -0.010416666666666666*(complex(0,1)*G**2)/cmath.pi**2 ) + (complex(0,1)*G**2)/(96.*cmath.pi**2)'},
                       order = {'QCD':2})

UVGC_198_85 = Coupling(name = 'UVGC_198_85',
                       value = {-1:'( 0 if MB else (complex(0,1)*G**2)/(24.*cmath.pi**2) ) - (complex(0,1)*G**2)/(24.*cmath.pi**2)',0:'( (complex(0,1)*G**2*reglog(MB/MU_R))/(12.*cmath.pi**2) if MB else 0 )'},
                       order = {'QCD':2})

UVGC_198_86 = Coupling(name = 'UVGC_198_86',
                       value = {-1:'(3*complex(0,1)*G**2)/(64.*cmath.pi**2)'},
                       order = {'QCD':2})

UVGC_198_87 = Coupling(name = 'UVGC_198_87',
                       value = {-1:'(-3*complex(0,1)*G**2)/(64.*cmath.pi**2)'},
                       order = {'QCD':2})

UVGC_198_88 = Coupling(name = 'UVGC_198_88',
                       value = {-1:'( 0 if MT else (complex(0,1)*G**2)/(24.*cmath.pi**2) ) - (complex(0,1)*G**2)/(24.*cmath.pi**2)',0:'( (complex(0,1)*G**2*reglog(MT/MU_R))/(12.*cmath.pi**2) if MT else 0 )'},
                       order = {'QCD':2})

UVGC_198_89 = Coupling(name = 'UVGC_198_89',
                       value = {-1:'( 0 if MYd else (complex(0,1)*G**2)/(96.*cmath.pi**2) ) - (complex(0,1)*G**2)/(96.*cmath.pi**2)',0:'( (complex(0,1)*G**2)/(96.*cmath.pi**2) + (complex(0,1)*G**2*reglog(MYd/MU_R))/(48.*cmath.pi**2) if MYd else (complex(0,1)*G**2)/(96.*cmath.pi**2) ) - (complex(0,1)*G**2)/(96.*cmath.pi**2)'},
                       order = {'QCD':2})

UVGC_198_90 = Coupling(name = 'UVGC_198_90',
                       value = {-1:'( 0 if MYu else (complex(0,1)*G**2)/(96.*cmath.pi**2) ) - (complex(0,1)*G**2)/(96.*cmath.pi**2)',0:'( (complex(0,1)*G**2)/(96.*cmath.pi**2) + (complex(0,1)*G**2*reglog(MYu/MU_R))/(48.*cmath.pi**2) if MYu else (complex(0,1)*G**2)/(96.*cmath.pi**2) ) - (complex(0,1)*G**2)/(96.*cmath.pi**2)'},
                       order = {'QCD':2})

UVGC_199_91 = Coupling(name = 'UVGC_199_91',
                       value = {-1:'( 0 if MB else -0.0625*G**3/cmath.pi**2 ) + G**3/(24.*cmath.pi**2)',0:'( -0.125*(G**3*reglog(MB/MU_R))/cmath.pi**2 if MB else 0 )'},
                       order = {'QCD':3})

UVGC_199_92 = Coupling(name = 'UVGC_199_92',
                       value = {-1:'-0.020833333333333332*G**3/cmath.pi**2'},
                       order = {'QCD':3})

UVGC_199_93 = Coupling(name = 'UVGC_199_93',
                       value = {-1:'(51*G**3)/(128.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_199_94 = Coupling(name = 'UVGC_199_94',
                       value = {-1:'( 0 if MT else -0.0625*G**3/cmath.pi**2 ) + G**3/(24.*cmath.pi**2)',0:'( -0.125*(G**3*reglog(MT/MU_R))/cmath.pi**2 if MT else 0 )'},
                       order = {'QCD':3})

UVGC_199_95 = Coupling(name = 'UVGC_199_95',
                       value = {-1:'( 0 if MYd else -0.015625*G**3/cmath.pi**2 ) + G**3/(96.*cmath.pi**2)',0:'( -0.015625*G**3/cmath.pi**2 - (G**3*reglog(MYd/MU_R))/(32.*cmath.pi**2) if MYd else -0.015625*G**3/cmath.pi**2 ) + G**3/(64.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_199_96 = Coupling(name = 'UVGC_199_96',
                       value = {-1:'( 0 if MYu else -0.015625*G**3/cmath.pi**2 ) + G**3/(96.*cmath.pi**2)',0:'( -0.015625*G**3/cmath.pi**2 - (G**3*reglog(MYu/MU_R))/(32.*cmath.pi**2) if MYu else -0.015625*G**3/cmath.pi**2 ) + G**3/(64.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_200_97 = Coupling(name = 'UVGC_200_97',
                       value = {-1:'(21*G**3)/(64.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_200_98 = Coupling(name = 'UVGC_200_98',
                       value = {-1:'G**3/(64.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_201_99 = Coupling(name = 'UVGC_201_99',
                       value = {-1:'(33*G**3)/(128.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_201_100 = Coupling(name = 'UVGC_201_100',
                        value = {-1:'(3*G**3)/(128.*cmath.pi**2)'},
                        order = {'QCD':3})

UVGC_201_101 = Coupling(name = 'UVGC_201_101',
                        value = {-1:'( 0 if MYd else -0.015625*G**3/cmath.pi**2 ) + G**3/(48.*cmath.pi**2)',0:'( -0.015625*G**3/cmath.pi**2 - (G**3*reglog(MYd/MU_R))/(32.*cmath.pi**2) if MYd else -0.015625*G**3/cmath.pi**2 ) + G**3/(64.*cmath.pi**2)'},
                        order = {'QCD':3})

UVGC_201_102 = Coupling(name = 'UVGC_201_102',
                        value = {-1:'( 0 if MYu else -0.015625*G**3/cmath.pi**2 ) + G**3/(48.*cmath.pi**2)',0:'( -0.015625*G**3/cmath.pi**2 - (G**3*reglog(MYu/MU_R))/(32.*cmath.pi**2) if MYu else -0.015625*G**3/cmath.pi**2 ) + G**3/(64.*cmath.pi**2)'},
                        order = {'QCD':3})

UVGC_202_103 = Coupling(name = 'UVGC_202_103',
                        value = {-1:'( 0 if MB else -0.020833333333333332*(complex(0,1)*G**3)/cmath.pi**2 )',0:'( -0.041666666666666664*(complex(0,1)*G**3*reglog(MB/MU_R))/cmath.pi**2 if MB else 0 )'},
                        order = {'QCD':3})

UVGC_202_104 = Coupling(name = 'UVGC_202_104',
                        value = {-1:'-0.020833333333333332*(complex(0,1)*G**3)/cmath.pi**2'},
                        order = {'QCD':3})

UVGC_202_105 = Coupling(name = 'UVGC_202_105',
                        value = {-1:'(19*complex(0,1)*G**3)/(128.*cmath.pi**2)'},
                        order = {'QCD':3})

UVGC_202_106 = Coupling(name = 'UVGC_202_106',
                        value = {-1:'(complex(0,1)*G**3)/(128.*cmath.pi**2)'},
                        order = {'QCD':3})

UVGC_202_107 = Coupling(name = 'UVGC_202_107',
                        value = {-1:'( 0 if MT else -0.020833333333333332*(complex(0,1)*G**3)/cmath.pi**2 )',0:'( -0.041666666666666664*(complex(0,1)*G**3*reglog(MT/MU_R))/cmath.pi**2 if MT else 0 )'},
                        order = {'QCD':3})

UVGC_202_108 = Coupling(name = 'UVGC_202_108',
                        value = {-1:'( 0 if MYd else -0.005208333333333333*(complex(0,1)*G**3)/cmath.pi**2 )',0:'( -0.005208333333333333*(complex(0,1)*G**3)/cmath.pi**2 - (complex(0,1)*G**3*reglog(MYd/MU_R))/(96.*cmath.pi**2) if MYd else -0.005208333333333333*(complex(0,1)*G**3)/cmath.pi**2 ) + (complex(0,1)*G**3)/(192.*cmath.pi**2)'},
                        order = {'QCD':3})

UVGC_202_109 = Coupling(name = 'UVGC_202_109',
                        value = {-1:'( 0 if MYu else -0.005208333333333333*(complex(0,1)*G**3)/cmath.pi**2 )',0:'( -0.005208333333333333*(complex(0,1)*G**3)/cmath.pi**2 - (complex(0,1)*G**3*reglog(MYu/MU_R))/(96.*cmath.pi**2) if MYu else -0.005208333333333333*(complex(0,1)*G**3)/cmath.pi**2 ) + (complex(0,1)*G**3)/(192.*cmath.pi**2)'},
                        order = {'QCD':3})

UVGC_202_110 = Coupling(name = 'UVGC_202_110',
                        value = {-1:'( (complex(0,1)*G**3)/(6.*cmath.pi**2) if MYd else (complex(0,1)*G**3)/(6.*cmath.pi**2) ) + (complex(0,1)*G**3)/(48.*cmath.pi**2)',0:'( -0.013888888888888888*(complex(0,1)*G**3)/cmath.pi**2 if MYd else -0.013888888888888888*(complex(0,1)*G**3)/cmath.pi**2 ) + (complex(0,1)*G**3)/(72.*cmath.pi**2)'},
                        order = {'QCD':3})

UVGC_203_111 = Coupling(name = 'UVGC_203_111',
                        value = {-1:'( (complex(0,1)*G**3)/(6.*cmath.pi**2) if MYu else (complex(0,1)*G**3)/(6.*cmath.pi**2) ) + (complex(0,1)*G**3)/(48.*cmath.pi**2)',0:'( -0.013888888888888888*(complex(0,1)*G**3)/cmath.pi**2 if MYu else -0.013888888888888888*(complex(0,1)*G**3)/cmath.pi**2 ) + (complex(0,1)*G**3)/(72.*cmath.pi**2)'},
                        order = {'QCD':3})

UVGC_204_112 = Coupling(name = 'UVGC_204_112',
                        value = {-1:'( 0 if MB else (complex(0,1)*G**3)/(48.*cmath.pi**2) )',0:'( (complex(0,1)*G**3*reglog(MB/MU_R))/(24.*cmath.pi**2) if MB else 0 )'},
                        order = {'QCD':3})

UVGC_204_113 = Coupling(name = 'UVGC_204_113',
                        value = {-1:'(complex(0,1)*G**3)/(48.*cmath.pi**2)'},
                        order = {'QCD':3})

UVGC_204_114 = Coupling(name = 'UVGC_204_114',
                        value = {-1:'(-19*complex(0,1)*G**3)/(128.*cmath.pi**2)'},
                        order = {'QCD':3})

UVGC_204_115 = Coupling(name = 'UVGC_204_115',
                        value = {-1:'-0.0078125*(complex(0,1)*G**3)/cmath.pi**2'},
                        order = {'QCD':3})

UVGC_204_116 = Coupling(name = 'UVGC_204_116',
                        value = {-1:'( 0 if MT else (complex(0,1)*G**3)/(48.*cmath.pi**2) )',0:'( (complex(0,1)*G**3*reglog(MT/MU_R))/(24.*cmath.pi**2) if MT else 0 )'},
                        order = {'QCD':3})

UVGC_204_117 = Coupling(name = 'UVGC_204_117',
                        value = {-1:'( 0 if MYd else (complex(0,1)*G**3)/(192.*cmath.pi**2) )',0:'( (complex(0,1)*G**3)/(192.*cmath.pi**2) + (complex(0,1)*G**3*reglog(MYd/MU_R))/(96.*cmath.pi**2) if MYd else (complex(0,1)*G**3)/(192.*cmath.pi**2) ) - (complex(0,1)*G**3)/(192.*cmath.pi**2)'},
                        order = {'QCD':3})

UVGC_204_118 = Coupling(name = 'UVGC_204_118',
                        value = {-1:'( 0 if MYu else (complex(0,1)*G**3)/(192.*cmath.pi**2) )',0:'( (complex(0,1)*G**3)/(192.*cmath.pi**2) + (complex(0,1)*G**3*reglog(MYu/MU_R))/(96.*cmath.pi**2) if MYu else (complex(0,1)*G**3)/(192.*cmath.pi**2) ) - (complex(0,1)*G**3)/(192.*cmath.pi**2)'},
                        order = {'QCD':3})

UVGC_205_119 = Coupling(name = 'UVGC_205_119',
                        value = {-1:'( -0.16666666666666666*(complex(0,1)*G**3)/cmath.pi**2 if MB else (complex(0,1)*G**3)/(12.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**3)/(12.*cmath.pi**2) + (complex(0,1)*G**3*reglog(MB/MU_R))/(2.*cmath.pi**2) if MB else -0.08333333333333333*(complex(0,1)*G**3)/cmath.pi**2 ) + (complex(0,1)*G**3)/(12.*cmath.pi**2)'},
                        order = {'QCD':3})

UVGC_206_120 = Coupling(name = 'UVGC_206_120',
                        value = {-1:'( -0.16666666666666666*(complex(0,1)*G**3)/cmath.pi**2 if MT else (complex(0,1)*G**3)/(12.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**3)/(12.*cmath.pi**2) + (complex(0,1)*G**3*reglog(MT/MU_R))/(2.*cmath.pi**2) if MT else -0.08333333333333333*(complex(0,1)*G**3)/cmath.pi**2 ) + (complex(0,1)*G**3)/(12.*cmath.pi**2)'},
                        order = {'QCD':3})

UVGC_207_121 = Coupling(name = 'UVGC_207_121',
                        value = {-1:'( 0 if MB else G**3/(16.*cmath.pi**2) ) - G**3/(24.*cmath.pi**2)',0:'( (G**3*reglog(MB/MU_R))/(8.*cmath.pi**2) if MB else 0 )'},
                        order = {'QCD':3})

UVGC_207_122 = Coupling(name = 'UVGC_207_122',
                        value = {-1:'G**3/(48.*cmath.pi**2)'},
                        order = {'QCD':3})

UVGC_207_123 = Coupling(name = 'UVGC_207_123',
                        value = {-1:'(-51*G**3)/(128.*cmath.pi**2)'},
                        order = {'QCD':3})

UVGC_207_124 = Coupling(name = 'UVGC_207_124',
                        value = {-1:'( 0 if MT else G**3/(16.*cmath.pi**2) ) - G**3/(24.*cmath.pi**2)',0:'( (G**3*reglog(MT/MU_R))/(8.*cmath.pi**2) if MT else 0 )'},
                        order = {'QCD':3})

UVGC_207_125 = Coupling(name = 'UVGC_207_125',
                        value = {-1:'( 0 if MYd else G**3/(64.*cmath.pi**2) )',0:'( G**3/(64.*cmath.pi**2) + (G**3*reglog(MYd/MU_R))/(32.*cmath.pi**2) if MYd else G**3/(64.*cmath.pi**2) ) - G**3/(64.*cmath.pi**2)'},
                        order = {'QCD':3})

UVGC_207_126 = Coupling(name = 'UVGC_207_126',
                        value = {-1:'( 0 if MYu else G**3/(64.*cmath.pi**2) )',0:'( G**3/(64.*cmath.pi**2) + (G**3*reglog(MYu/MU_R))/(32.*cmath.pi**2) if MYu else G**3/(64.*cmath.pi**2) ) - G**3/(64.*cmath.pi**2)'},
                        order = {'QCD':3})

UVGC_208_127 = Coupling(name = 'UVGC_208_127',
                        value = {-1:'(-33*G**3)/(128.*cmath.pi**2)'},
                        order = {'QCD':3})

UVGC_208_128 = Coupling(name = 'UVGC_208_128',
                        value = {-1:'(-3*G**3)/(128.*cmath.pi**2)'},
                        order = {'QCD':3})

UVGC_208_129 = Coupling(name = 'UVGC_208_129',
                        value = {-1:'( 0 if MYd else G**3/(64.*cmath.pi**2) ) - G**3/(96.*cmath.pi**2)',0:'( G**3/(64.*cmath.pi**2) + (G**3*reglog(MYd/MU_R))/(32.*cmath.pi**2) if MYd else G**3/(64.*cmath.pi**2) ) - G**3/(64.*cmath.pi**2)'},
                        order = {'QCD':3})

UVGC_208_130 = Coupling(name = 'UVGC_208_130',
                        value = {-1:'( 0 if MYu else G**3/(64.*cmath.pi**2) ) - G**3/(96.*cmath.pi**2)',0:'( G**3/(64.*cmath.pi**2) + (G**3*reglog(MYu/MU_R))/(32.*cmath.pi**2) if MYu else G**3/(64.*cmath.pi**2) ) - G**3/(64.*cmath.pi**2)'},
                        order = {'QCD':3})

UVGC_209_131 = Coupling(name = 'UVGC_209_131',
                        value = {-1:'(-21*G**3)/(64.*cmath.pi**2)'},
                        order = {'QCD':3})

UVGC_209_132 = Coupling(name = 'UVGC_209_132',
                        value = {-1:'-0.015625*G**3/cmath.pi**2'},
                        order = {'QCD':3})

UVGC_210_133 = Coupling(name = 'UVGC_210_133',
                        value = {-1:'( 0 if MB else -0.013888888888888888*(ee*complex(0,1)*G**3)/cmath.pi**2 )',0:'( -0.027777777777777776*(ee*complex(0,1)*G**3*reglog(MB/MU_R))/cmath.pi**2 if MB else 0 )'},
                        order = {'QCD':3,'QED':1})

UVGC_210_134 = Coupling(name = 'UVGC_210_134',
                        value = {-1:'-0.013888888888888888*(ee*complex(0,1)*G**3)/cmath.pi**2'},
                        order = {'QCD':3,'QED':1})

UVGC_210_135 = Coupling(name = 'UVGC_210_135',
                        value = {-1:'(19*ee*complex(0,1)*G**3)/(192.*cmath.pi**2)'},
                        order = {'QCD':3,'QED':1})

UVGC_210_136 = Coupling(name = 'UVGC_210_136',
                        value = {-1:'(ee*complex(0,1)*G**3)/(192.*cmath.pi**2)'},
                        order = {'QCD':3,'QED':1})

UVGC_210_137 = Coupling(name = 'UVGC_210_137',
                        value = {-1:'( 0 if MT else -0.013888888888888888*(ee*complex(0,1)*G**3)/cmath.pi**2 )',0:'( -0.027777777777777776*(ee*complex(0,1)*G**3*reglog(MT/MU_R))/cmath.pi**2 if MT else 0 )'},
                        order = {'QCD':3,'QED':1})

UVGC_210_138 = Coupling(name = 'UVGC_210_138',
                        value = {-1:'( 0 if MYd else -0.003472222222222222*(ee*complex(0,1)*G**3)/cmath.pi**2 )',0:'( -0.003472222222222222*(ee*complex(0,1)*G**3)/cmath.pi**2 - (ee*complex(0,1)*G**3*reglog(MYd/MU_R))/(144.*cmath.pi**2) if MYd else -0.003472222222222222*(ee*complex(0,1)*G**3)/cmath.pi**2 ) + (ee*complex(0,1)*G**3)/(288.*cmath.pi**2)'},
                        order = {'QCD':3,'QED':1})

UVGC_210_139 = Coupling(name = 'UVGC_210_139',
                        value = {-1:'( 0 if MYu else -0.003472222222222222*(ee*complex(0,1)*G**3)/cmath.pi**2 )',0:'( -0.003472222222222222*(ee*complex(0,1)*G**3)/cmath.pi**2 - (ee*complex(0,1)*G**3*reglog(MYu/MU_R))/(144.*cmath.pi**2) if MYu else -0.003472222222222222*(ee*complex(0,1)*G**3)/cmath.pi**2 ) + (ee*complex(0,1)*G**3)/(288.*cmath.pi**2)'},
                        order = {'QCD':3,'QED':1})

UVGC_210_140 = Coupling(name = 'UVGC_210_140',
                        value = {-1:'( (ee*complex(0,1)*G**3)/(9.*cmath.pi**2) if MYd else (ee*complex(0,1)*G**3)/(9.*cmath.pi**2) ) + (ee*complex(0,1)*G**3)/(72.*cmath.pi**2)',0:'( -0.009259259259259259*(ee*complex(0,1)*G**3)/cmath.pi**2 if MYd else -0.009259259259259259*(ee*complex(0,1)*G**3)/cmath.pi**2 ) + (ee*complex(0,1)*G**3)/(108.*cmath.pi**2)'},
                        order = {'QCD':3,'QED':1})

UVGC_211_141 = Coupling(name = 'UVGC_211_141',
                        value = {-1:'( 0 if MB else (ee*complex(0,1)*G**3)/(36.*cmath.pi**2) )',0:'( (ee*complex(0,1)*G**3*reglog(MB/MU_R))/(18.*cmath.pi**2) if MB else 0 )'},
                        order = {'QCD':3,'QED':1})

UVGC_211_142 = Coupling(name = 'UVGC_211_142',
                        value = {-1:'(ee*complex(0,1)*G**3)/(36.*cmath.pi**2)'},
                        order = {'QCD':3,'QED':1})

UVGC_211_143 = Coupling(name = 'UVGC_211_143',
                        value = {-1:'(-19*ee*complex(0,1)*G**3)/(96.*cmath.pi**2)'},
                        order = {'QCD':3,'QED':1})

UVGC_211_144 = Coupling(name = 'UVGC_211_144',
                        value = {-1:'-0.010416666666666666*(ee*complex(0,1)*G**3)/cmath.pi**2'},
                        order = {'QCD':3,'QED':1})

UVGC_211_145 = Coupling(name = 'UVGC_211_145',
                        value = {-1:'( 0 if MT else (ee*complex(0,1)*G**3)/(36.*cmath.pi**2) )',0:'( (ee*complex(0,1)*G**3*reglog(MT/MU_R))/(18.*cmath.pi**2) if MT else 0 )'},
                        order = {'QCD':3,'QED':1})

UVGC_211_146 = Coupling(name = 'UVGC_211_146',
                        value = {-1:'( 0 if MYd else (ee*complex(0,1)*G**3)/(144.*cmath.pi**2) )',0:'( (ee*complex(0,1)*G**3)/(144.*cmath.pi**2) + (ee*complex(0,1)*G**3*reglog(MYd/MU_R))/(72.*cmath.pi**2) if MYd else (ee*complex(0,1)*G**3)/(144.*cmath.pi**2) ) - (ee*complex(0,1)*G**3)/(144.*cmath.pi**2)'},
                        order = {'QCD':3,'QED':1})

UVGC_211_147 = Coupling(name = 'UVGC_211_147',
                        value = {-1:'( 0 if MYu else (ee*complex(0,1)*G**3)/(144.*cmath.pi**2) )',0:'( (ee*complex(0,1)*G**3)/(144.*cmath.pi**2) + (ee*complex(0,1)*G**3*reglog(MYu/MU_R))/(72.*cmath.pi**2) if MYu else (ee*complex(0,1)*G**3)/(144.*cmath.pi**2) ) - (ee*complex(0,1)*G**3)/(144.*cmath.pi**2)'},
                        order = {'QCD':3,'QED':1})

UVGC_211_148 = Coupling(name = 'UVGC_211_148',
                        value = {-1:'( (-2*ee*complex(0,1)*G**3)/(9.*cmath.pi**2) if MYu else (-2*ee*complex(0,1)*G**3)/(9.*cmath.pi**2) ) - (ee*complex(0,1)*G**3)/(36.*cmath.pi**2)',0:'( (ee*complex(0,1)*G**3)/(54.*cmath.pi**2) if MYu else (ee*complex(0,1)*G**3)/(54.*cmath.pi**2) ) - (ee*complex(0,1)*G**3)/(54.*cmath.pi**2)'},
                        order = {'QCD':3,'QED':1})

UVGC_212_149 = Coupling(name = 'UVGC_212_149',
                        value = {-1:'( 0 if MB else (complex(0,1)*G**4)/(24.*cmath.pi**2) )',0:'( (complex(0,1)*G**4*reglog(MB/MU_R))/(12.*cmath.pi**2) if MB else 0 )'},
                        order = {'QCD':4})

UVGC_212_150 = Coupling(name = 'UVGC_212_150',
                        value = {-1:'(complex(0,1)*G**4)/(24.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_212_151 = Coupling(name = 'UVGC_212_151',
                        value = {-1:'(-7*complex(0,1)*G**4)/(16.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_212_152 = Coupling(name = 'UVGC_212_152',
                        value = {-1:'-0.015625*(complex(0,1)*G**4)/cmath.pi**2'},
                        order = {'QCD':4})

UVGC_212_153 = Coupling(name = 'UVGC_212_153',
                        value = {-1:'( 0 if MT else (complex(0,1)*G**4)/(24.*cmath.pi**2) )',0:'( (complex(0,1)*G**4*reglog(MT/MU_R))/(12.*cmath.pi**2) if MT else 0 )'},
                        order = {'QCD':4})

UVGC_212_154 = Coupling(name = 'UVGC_212_154',
                        value = {-1:'( 0 if MYd else (complex(0,1)*G**4)/(96.*cmath.pi**2) )',0:'( (complex(0,1)*G**4)/(96.*cmath.pi**2) + (complex(0,1)*G**4*reglog(MYd/MU_R))/(48.*cmath.pi**2) if MYd else (complex(0,1)*G**4)/(96.*cmath.pi**2) ) - (complex(0,1)*G**4)/(96.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_212_155 = Coupling(name = 'UVGC_212_155',
                        value = {-1:'( 0 if MYu else (complex(0,1)*G**4)/(96.*cmath.pi**2) )',0:'( (complex(0,1)*G**4)/(96.*cmath.pi**2) + (complex(0,1)*G**4*reglog(MYu/MU_R))/(48.*cmath.pi**2) if MYu else (complex(0,1)*G**4)/(96.*cmath.pi**2) ) - (complex(0,1)*G**4)/(96.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_212_156 = Coupling(name = 'UVGC_212_156',
                        value = {-1:'( -0.16666666666666666*(complex(0,1)*G**4)/cmath.pi**2 if MYd else -0.16666666666666666*(complex(0,1)*G**4)/cmath.pi**2 ) - (13*complex(0,1)*G**4)/(192.*cmath.pi**2)',0:'( (complex(0,1)*G**4)/(72.*cmath.pi**2) if MYd else (complex(0,1)*G**4)/(72.*cmath.pi**2) ) - (complex(0,1)*G**4)/(72.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_213_157 = Coupling(name = 'UVGC_213_157',
                        value = {-1:'( -0.16666666666666666*(complex(0,1)*G**4)/cmath.pi**2 if MYu else -0.16666666666666666*(complex(0,1)*G**4)/cmath.pi**2 ) - (13*complex(0,1)*G**4)/(192.*cmath.pi**2)',0:'( (complex(0,1)*G**4)/(72.*cmath.pi**2) if MYu else (complex(0,1)*G**4)/(72.*cmath.pi**2) ) - (complex(0,1)*G**4)/(72.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_214_158 = Coupling(name = 'UVGC_214_158',
                        value = {-1:'( 0 if MB else -0.08333333333333333*(complex(0,1)*G**4)/cmath.pi**2 ) + (complex(0,1)*G**4)/(12.*cmath.pi**2)',0:'( -0.16666666666666666*(complex(0,1)*G**4*reglog(MB/MU_R))/cmath.pi**2 if MB else 0 )'},
                        order = {'QCD':4})

UVGC_214_159 = Coupling(name = 'UVGC_214_159',
                        value = {-1:'(147*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_214_160 = Coupling(name = 'UVGC_214_160',
                        value = {-1:'(21*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_214_161 = Coupling(name = 'UVGC_214_161',
                        value = {-1:'( 0 if MT else -0.08333333333333333*(complex(0,1)*G**4)/cmath.pi**2 ) + (complex(0,1)*G**4)/(12.*cmath.pi**2)',0:'( -0.16666666666666666*(complex(0,1)*G**4*reglog(MT/MU_R))/cmath.pi**2 if MT else 0 )'},
                        order = {'QCD':4})

UVGC_214_162 = Coupling(name = 'UVGC_214_162',
                        value = {-1:'( 0 if MYd else -0.020833333333333332*(complex(0,1)*G**4)/cmath.pi**2 ) - (complex(0,1)*G**4)/(96.*cmath.pi**2)',0:'( -0.020833333333333332*(complex(0,1)*G**4)/cmath.pi**2 - (complex(0,1)*G**4*reglog(MYd/MU_R))/(24.*cmath.pi**2) if MYd else -0.020833333333333332*(complex(0,1)*G**4)/cmath.pi**2 ) + (complex(0,1)*G**4)/(48.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_214_163 = Coupling(name = 'UVGC_214_163',
                        value = {-1:'( 0 if MYu else -0.020833333333333332*(complex(0,1)*G**4)/cmath.pi**2 ) - (complex(0,1)*G**4)/(96.*cmath.pi**2)',0:'( -0.020833333333333332*(complex(0,1)*G**4)/cmath.pi**2 - (complex(0,1)*G**4*reglog(MYu/MU_R))/(24.*cmath.pi**2) if MYu else -0.020833333333333332*(complex(0,1)*G**4)/cmath.pi**2 ) + (complex(0,1)*G**4)/(48.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_215_164 = Coupling(name = 'UVGC_215_164',
                        value = {-1:'( 0 if MB else -0.08333333333333333*(complex(0,1)*G**4)/cmath.pi**2 )',0:'( -0.16666666666666666*(complex(0,1)*G**4*reglog(MB/MU_R))/cmath.pi**2 if MB else 0 )'},
                        order = {'QCD':4})

UVGC_215_165 = Coupling(name = 'UVGC_215_165',
                        value = {-1:'-0.08333333333333333*(complex(0,1)*G**4)/cmath.pi**2'},
                        order = {'QCD':4})

UVGC_215_166 = Coupling(name = 'UVGC_215_166',
                        value = {-1:'(523*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_215_167 = Coupling(name = 'UVGC_215_167',
                        value = {-1:'(13*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_215_168 = Coupling(name = 'UVGC_215_168',
                        value = {-1:'( 0 if MT else -0.08333333333333333*(complex(0,1)*G**4)/cmath.pi**2 )',0:'( -0.16666666666666666*(complex(0,1)*G**4*reglog(MT/MU_R))/cmath.pi**2 if MT else 0 )'},
                        order = {'QCD':4})

UVGC_215_169 = Coupling(name = 'UVGC_215_169',
                        value = {-1:'( 0 if MYd else -0.020833333333333332*(complex(0,1)*G**4)/cmath.pi**2 ) + (complex(0,1)*G**4)/(32.*cmath.pi**2)',0:'( -0.020833333333333332*(complex(0,1)*G**4)/cmath.pi**2 - (complex(0,1)*G**4*reglog(MYd/MU_R))/(24.*cmath.pi**2) if MYd else -0.020833333333333332*(complex(0,1)*G**4)/cmath.pi**2 ) + (complex(0,1)*G**4)/(48.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_215_170 = Coupling(name = 'UVGC_215_170',
                        value = {-1:'( 0 if MYu else -0.020833333333333332*(complex(0,1)*G**4)/cmath.pi**2 ) + (complex(0,1)*G**4)/(32.*cmath.pi**2)',0:'( -0.020833333333333332*(complex(0,1)*G**4)/cmath.pi**2 - (complex(0,1)*G**4*reglog(MYu/MU_R))/(24.*cmath.pi**2) if MYu else -0.020833333333333332*(complex(0,1)*G**4)/cmath.pi**2 ) + (complex(0,1)*G**4)/(48.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_216_171 = Coupling(name = 'UVGC_216_171',
                        value = {-1:'(147*complex(0,1)*G**4)/(128.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_216_172 = Coupling(name = 'UVGC_216_172',
                        value = {-1:'(3*complex(0,1)*G**4)/(128.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_216_173 = Coupling(name = 'UVGC_216_173',
                        value = {-1:'( 0 if MYd else -0.020833333333333332*(complex(0,1)*G**4)/cmath.pi**2 ) + (5*complex(0,1)*G**4)/(96.*cmath.pi**2)',0:'( -0.020833333333333332*(complex(0,1)*G**4)/cmath.pi**2 - (complex(0,1)*G**4*reglog(MYd/MU_R))/(24.*cmath.pi**2) if MYd else -0.020833333333333332*(complex(0,1)*G**4)/cmath.pi**2 ) + (complex(0,1)*G**4)/(48.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_216_174 = Coupling(name = 'UVGC_216_174',
                        value = {-1:'( 0 if MYu else -0.020833333333333332*(complex(0,1)*G**4)/cmath.pi**2 ) + (5*complex(0,1)*G**4)/(96.*cmath.pi**2)',0:'( -0.020833333333333332*(complex(0,1)*G**4)/cmath.pi**2 - (complex(0,1)*G**4*reglog(MYu/MU_R))/(24.*cmath.pi**2) if MYu else -0.020833333333333332*(complex(0,1)*G**4)/cmath.pi**2 ) + (complex(0,1)*G**4)/(48.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_217_175 = Coupling(name = 'UVGC_217_175',
                        value = {-1:'( 0 if MB else (complex(0,1)*G**4)/(12.*cmath.pi**2) ) - (complex(0,1)*G**4)/(24.*cmath.pi**2)',0:'( (complex(0,1)*G**4*reglog(MB/MU_R))/(6.*cmath.pi**2) if MB else 0 )'},
                        order = {'QCD':4})

UVGC_217_176 = Coupling(name = 'UVGC_217_176',
                        value = {-1:'(-341*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_217_177 = Coupling(name = 'UVGC_217_177',
                        value = {-1:'(-11*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_217_178 = Coupling(name = 'UVGC_217_178',
                        value = {-1:'( 0 if MT else (complex(0,1)*G**4)/(12.*cmath.pi**2) ) - (complex(0,1)*G**4)/(24.*cmath.pi**2)',0:'( (complex(0,1)*G**4*reglog(MT/MU_R))/(6.*cmath.pi**2) if MT else 0 )'},
                        order = {'QCD':4})

UVGC_217_179 = Coupling(name = 'UVGC_217_179',
                        value = {-1:'( 0 if MYd else (complex(0,1)*G**4)/(48.*cmath.pi**2) ) - (complex(0,1)*G**4)/(96.*cmath.pi**2)',0:'( (complex(0,1)*G**4)/(48.*cmath.pi**2) + (complex(0,1)*G**4*reglog(MYd/MU_R))/(24.*cmath.pi**2) if MYd else (complex(0,1)*G**4)/(48.*cmath.pi**2) ) - (complex(0,1)*G**4)/(48.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_217_180 = Coupling(name = 'UVGC_217_180',
                        value = {-1:'( 0 if MYu else (complex(0,1)*G**4)/(48.*cmath.pi**2) ) - (complex(0,1)*G**4)/(96.*cmath.pi**2)',0:'( (complex(0,1)*G**4)/(48.*cmath.pi**2) + (complex(0,1)*G**4*reglog(MYu/MU_R))/(24.*cmath.pi**2) if MYu else (complex(0,1)*G**4)/(48.*cmath.pi**2) ) - (complex(0,1)*G**4)/(48.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_218_181 = Coupling(name = 'UVGC_218_181',
                        value = {-1:'(-83*complex(0,1)*G**4)/(128.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_218_182 = Coupling(name = 'UVGC_218_182',
                        value = {-1:'(-5*complex(0,1)*G**4)/(128.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_219_183 = Coupling(name = 'UVGC_219_183',
                        value = {-1:'( 0 if MB else (complex(0,1)*G**4)/(12.*cmath.pi**2) )',0:'( (complex(0,1)*G**4*reglog(MB/MU_R))/(6.*cmath.pi**2) if MB else 0 )'},
                        order = {'QCD':4})

UVGC_219_184 = Coupling(name = 'UVGC_219_184',
                        value = {-1:'(complex(0,1)*G**4)/(12.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_219_185 = Coupling(name = 'UVGC_219_185',
                        value = {-1:'(-85*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_219_186 = Coupling(name = 'UVGC_219_186',
                        value = {-1:'(-19*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_219_187 = Coupling(name = 'UVGC_219_187',
                        value = {-1:'( 0 if MT else (complex(0,1)*G**4)/(12.*cmath.pi**2) )',0:'( (complex(0,1)*G**4*reglog(MT/MU_R))/(6.*cmath.pi**2) if MT else 0 )'},
                        order = {'QCD':4})

UVGC_219_188 = Coupling(name = 'UVGC_219_188',
                        value = {-1:'( 0 if MYd else (complex(0,1)*G**4)/(48.*cmath.pi**2) ) + (complex(0,1)*G**4)/(32.*cmath.pi**2)',0:'( (complex(0,1)*G**4)/(48.*cmath.pi**2) + (complex(0,1)*G**4*reglog(MYd/MU_R))/(24.*cmath.pi**2) if MYd else (complex(0,1)*G**4)/(48.*cmath.pi**2) ) - (complex(0,1)*G**4)/(48.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_219_189 = Coupling(name = 'UVGC_219_189',
                        value = {-1:'( 0 if MYu else (complex(0,1)*G**4)/(48.*cmath.pi**2) ) + (complex(0,1)*G**4)/(32.*cmath.pi**2)',0:'( (complex(0,1)*G**4)/(48.*cmath.pi**2) + (complex(0,1)*G**4*reglog(MYu/MU_R))/(24.*cmath.pi**2) if MYu else (complex(0,1)*G**4)/(48.*cmath.pi**2) ) - (complex(0,1)*G**4)/(48.*cmath.pi**2)'},
                        order = {'QCD':4})

UVGC_220_190 = Coupling(name = 'UVGC_220_190',
                        value = {-1:'( 0 if MB else (ee*complex(0,1)*G**3*sw)/(72.*cw*cmath.pi**2) )',0:'( (ee*complex(0,1)*G**3*sw*reglog(MB/MU_R))/(36.*cw*cmath.pi**2) if MB else 0 )'},
                        order = {'QCD':3,'QED':1})

UVGC_220_191 = Coupling(name = 'UVGC_220_191',
                        value = {-1:'(ee*complex(0,1)*G**3*sw)/(72.*cw*cmath.pi**2)'},
                        order = {'QCD':3,'QED':1})

UVGC_220_192 = Coupling(name = 'UVGC_220_192',
                        value = {-1:'(-19*ee*complex(0,1)*G**3*sw)/(192.*cw*cmath.pi**2)'},
                        order = {'QCD':3,'QED':1})

UVGC_220_193 = Coupling(name = 'UVGC_220_193',
                        value = {-1:'-0.005208333333333333*(ee*complex(0,1)*G**3*sw)/(cw*cmath.pi**2)'},
                        order = {'QCD':3,'QED':1})

UVGC_220_194 = Coupling(name = 'UVGC_220_194',
                        value = {-1:'( 0 if MT else (ee*complex(0,1)*G**3*sw)/(72.*cw*cmath.pi**2) )',0:'( (ee*complex(0,1)*G**3*sw*reglog(MT/MU_R))/(36.*cw*cmath.pi**2) if MT else 0 )'},
                        order = {'QCD':3,'QED':1})

UVGC_220_195 = Coupling(name = 'UVGC_220_195',
                        value = {-1:'( 0 if MYd else (ee*complex(0,1)*G**3*sw)/(288.*cw*cmath.pi**2) )',0:'( (ee*complex(0,1)*G**3*sw)/(288.*cw*cmath.pi**2) + (ee*complex(0,1)*G**3*sw*reglog(MYd/MU_R))/(144.*cw*cmath.pi**2) if MYd else (ee*complex(0,1)*G**3*sw)/(288.*cw*cmath.pi**2) ) - (ee*complex(0,1)*G**3*sw)/(288.*cw*cmath.pi**2)'},
                        order = {'QCD':3,'QED':1})

UVGC_220_196 = Coupling(name = 'UVGC_220_196',
                        value = {-1:'( 0 if MYu else (ee*complex(0,1)*G**3*sw)/(288.*cw*cmath.pi**2) )',0:'( (ee*complex(0,1)*G**3*sw)/(288.*cw*cmath.pi**2) + (ee*complex(0,1)*G**3*sw*reglog(MYu/MU_R))/(144.*cw*cmath.pi**2) if MYu else (ee*complex(0,1)*G**3*sw)/(288.*cw*cmath.pi**2) ) - (ee*complex(0,1)*G**3*sw)/(288.*cw*cmath.pi**2)'},
                        order = {'QCD':3,'QED':1})

UVGC_220_197 = Coupling(name = 'UVGC_220_197',
                        value = {-1:'( -0.1111111111111111*(ee*complex(0,1)*G**3*sw)/(cw*cmath.pi**2) if MYd else -0.1111111111111111*(ee*complex(0,1)*G**3*sw)/(cw*cmath.pi**2) ) - (ee*complex(0,1)*G**3*sw)/(72.*cw*cmath.pi**2)',0:'( (ee*complex(0,1)*G**3*sw)/(108.*cw*cmath.pi**2) if MYd else (ee*complex(0,1)*G**3*sw)/(108.*cw*cmath.pi**2) ) - (ee*complex(0,1)*G**3*sw)/(108.*cw*cmath.pi**2)'},
                        order = {'QCD':3,'QED':1})

UVGC_221_198 = Coupling(name = 'UVGC_221_198',
                        value = {-1:'( 0 if MB else -0.027777777777777776*(ee*complex(0,1)*G**3*sw)/(cw*cmath.pi**2) )',0:'( -0.05555555555555555*(ee*complex(0,1)*G**3*sw*reglog(MB/MU_R))/(cw*cmath.pi**2) if MB else 0 )'},
                        order = {'QCD':3,'QED':1})

UVGC_221_199 = Coupling(name = 'UVGC_221_199',
                        value = {-1:'-0.027777777777777776*(ee*complex(0,1)*G**3*sw)/(cw*cmath.pi**2)'},
                        order = {'QCD':3,'QED':1})

UVGC_221_200 = Coupling(name = 'UVGC_221_200',
                        value = {-1:'(19*ee*complex(0,1)*G**3*sw)/(96.*cw*cmath.pi**2)'},
                        order = {'QCD':3,'QED':1})

UVGC_221_201 = Coupling(name = 'UVGC_221_201',
                        value = {-1:'(ee*complex(0,1)*G**3*sw)/(96.*cw*cmath.pi**2)'},
                        order = {'QCD':3,'QED':1})

UVGC_221_202 = Coupling(name = 'UVGC_221_202',
                        value = {-1:'( 0 if MT else -0.027777777777777776*(ee*complex(0,1)*G**3*sw)/(cw*cmath.pi**2) )',0:'( -0.05555555555555555*(ee*complex(0,1)*G**3*sw*reglog(MT/MU_R))/(cw*cmath.pi**2) if MT else 0 )'},
                        order = {'QCD':3,'QED':1})

UVGC_221_203 = Coupling(name = 'UVGC_221_203',
                        value = {-1:'( 0 if MYd else -0.006944444444444444*(ee*complex(0,1)*G**3*sw)/(cw*cmath.pi**2) )',0:'( -0.006944444444444444*(ee*complex(0,1)*G**3*sw)/(cw*cmath.pi**2) - (ee*complex(0,1)*G**3*sw*reglog(MYd/MU_R))/(72.*cw*cmath.pi**2) if MYd else -0.006944444444444444*(ee*complex(0,1)*G**3*sw)/(cw*cmath.pi**2) ) + (ee*complex(0,1)*G**3*sw)/(144.*cw*cmath.pi**2)'},
                        order = {'QCD':3,'QED':1})

UVGC_221_204 = Coupling(name = 'UVGC_221_204',
                        value = {-1:'( 0 if MYu else -0.006944444444444444*(ee*complex(0,1)*G**3*sw)/(cw*cmath.pi**2) )',0:'( -0.006944444444444444*(ee*complex(0,1)*G**3*sw)/(cw*cmath.pi**2) - (ee*complex(0,1)*G**3*sw*reglog(MYu/MU_R))/(72.*cw*cmath.pi**2) if MYu else -0.006944444444444444*(ee*complex(0,1)*G**3*sw)/(cw*cmath.pi**2) ) + (ee*complex(0,1)*G**3*sw)/(144.*cw*cmath.pi**2)'},
                        order = {'QCD':3,'QED':1})

UVGC_221_205 = Coupling(name = 'UVGC_221_205',
                        value = {-1:'( (2*ee*complex(0,1)*G**3*sw)/(9.*cw*cmath.pi**2) if MYu else (2*ee*complex(0,1)*G**3*sw)/(9.*cw*cmath.pi**2) ) + (ee*complex(0,1)*G**3*sw)/(36.*cw*cmath.pi**2)',0:'( -0.018518518518518517*(ee*complex(0,1)*G**3*sw)/(cw*cmath.pi**2) if MYu else -0.018518518518518517*(ee*complex(0,1)*G**3*sw)/(cw*cmath.pi**2) ) + (ee*complex(0,1)*G**3*sw)/(54.*cw*cmath.pi**2)'},
                        order = {'QCD':3,'QED':1})

UVGC_222_206 = Coupling(name = 'UVGC_222_206',
                        value = {-1:'( (complex(0,1)*G**2*MYu**2)/(6.*cmath.pi**2) if MYu else (complex(0,1)*G**2*MYu**2)/(6.*cmath.pi**2) ) + (complex(0,1)*G**2*MYu**2)/(12.*cmath.pi**2)',0:'( (41*complex(0,1)*G**2*MYu**2)/(72.*cmath.pi**2) - (complex(0,1)*G**2*MYu**2*reglog(MYu/MU_R))/(2.*cmath.pi**2) if MYu else -0.013888888888888888*(complex(0,1)*G**2*MYu**2)/cmath.pi**2 ) + (complex(0,1)*G**2*MYu**2)/(72.*cmath.pi**2)'},
                        order = {'QCD':2})

