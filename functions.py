import math


def heightfactor (z, h, Ta):

  zh = z/h
  a1 = 1/Ta
  a2 = 1 - (0.4 / Ta ) **2
  Hf = 1 + a1 * zh + a2 * zh**10

  return a1, a2, Hf

