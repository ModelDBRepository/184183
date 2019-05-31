'''
Defines a class, Neuron472349114, of neurons from Allen Brain Institute's model 472349114

A demo is available by running:

    python -i mosinit.py
'''
class Neuron472349114:
    def __init__(self, name="Neuron472349114", x=0, y=0, z=0):
        '''Instantiate Neuron472349114.
        
        Parameters:
            x, y, z -- position offset
            
        Note: if name is not specified, Neuron472349114_instance is used instead
        '''
        
        # load the morphology
        from load_swc import load_swc
        load_swc('Pvalb-IRES-Cre_Ai14_IVSCC_-176852.02.02.01_470548840_m.swc', self,
                 use_axon=False, xshift=x, yshift=y, zshift=z)

        # custom axon (works because dropping axon during import)
        from neuron import h
        self.axon = [h.Section(cell=self, name='axon[0]'),
                     h.Section(cell=self, name='axon[1]')]
        for sec in self.axon:
            sec.L = 30
            sec.diam = 1
            sec.nseg = 1
        self.axon[0].connect(self.soma[0](0.5))
        self.axon[1].connect(self.axon[0](1))
        self.all += self.axon
        
        self._name = name
        self._insert_mechanisms()
        self._discretize_model()
        self._set_mechanism_parameters()
    
    def __str__(self):
        if self._name is not None:
            return self._name
        else:
            return "Neuron472349114_instance"
                
    def _insert_mechanisms(self):
        from neuron import h
        for sec in self.all:
            sec.insert("pas")
        for mech in [u'CaDynamics', u'Ca_HVA', u'Ca_LVA', u'Ih', u'Im_v2', u'K_T', u'Kd', u'Kv2like', u'Kv3_1', u'NaV', u'SK']:
            self.soma[0].insert(mech)
    
    def _set_mechanism_parameters(self):
        from neuron import h
        for sec in self.all:
            sec.Ra = 136.92
            sec.e_pas = -92.7634175618
        
        for sec in self.axon:
            sec.cm = 2.14
            sec.g_pas = 0.000297528735429
        for sec in self.dend:
            sec.cm = 2.14
            sec.g_pas = 1.96762859094e-05
        for sec in self.soma:
            sec.cm = 2.14
            sec.ena = 53.0
            sec.ek = -107.0
            sec.gbar_Ih = 6.96153e-05
            sec.gbar_NaV = 0.0664573
            sec.gbar_Kd = 0.0103793
            sec.gbar_Kv2like = 0.00211382
            sec.gbar_Kv3_1 = 1.57251
            sec.gbar_K_T = 0.00510266
            sec.gbar_Im_v2 = 0.000170346
            sec.gbar_SK = 0.00659834
            sec.gbar_Ca_HVA = 0.000177714
            sec.gbar_Ca_LVA = 1.45878e-06
            sec.gamma_CaDynamics = 0.0182063
            sec.decay_CaDynamics = 570.991
            sec.g_pas = 0.000126356
    
    def _discretize_model(self):
        for sec in self.all:
            sec.nseg = 1 + 2 * int(sec.L / 40)

