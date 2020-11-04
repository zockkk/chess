import math
import random

class Neuro:
    def __init__(self, list_in, list_out):
        self.__in = list_in
        self.__out = list_out
        self.value = 0

    @property
    def list_in(self):
        return self.__in

    @list_in.setter
    def list_in(self, lst):
        self.__in = lst

    @property
    def list_out(self):
        return self.__out

    @list_out.setter
    def list_out(self, lst):
        self.__out = lst

    def act(self, x):
        return 1 / (1 + math.exp(-x))


class Link:
    def __init__(self, n_in, n_out, w=0):
        self.__in = n_in
        self.__out = n_out
        self.__w = w

    @property
    def n_in(self):
        return self.__in

    @property
    def n_out(self):
        return self.__out

    @property
    def w(self):
        return self.w


class Network:
    def __init(self, *args):
        self.__nlayers = len(args)
        self.__neuros = args
        self.__layers = []

        for i in range(self.__nlayers):
            self.__layers.append([Neuro([], []) for n in range(self.__neuros[i])])

        for i in range(self.__nlayers):
            for neuro in self.__layers[i]:
                list_in = 0 if i==0 else [Link(n_in, neuro, random.random()) for n_in in self.__layers[i-1]]
                list_out= 0 if i==self.__nlayers-1 else [Link(neuro, n_out, random.random()) for n_out in self.__layers[i+1]]
                neuro.list_in=list_in
                neuro.list_out = list_out

    def run(self, v):
        for neuro, inp in zip(self.__layers[0], v):
            neuro.value=neuro.list_in=inp

        for i in range(1, self.__nlayers):
            for neuro in self.__layers[i]:
                v=[(link.n_in.value*link.w) for link in neuro.list_in]
                neuro.value=neuro.act(sum(v))

    def output(self):
        return [neuro.value for neuro in self.__layers[-1]]

