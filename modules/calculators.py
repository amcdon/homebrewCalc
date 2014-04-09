
class OriginalGravityCalculator(object):

    def __init__(self):
        pass

    def extractOG(self, extractWeight, extractPPG, volume):
        points = extractWeight * extractPPG / volume
        return points

    def allGrain(self,maltWeight, maltPPG, efficiency, volume):
        efficiency = efficiency / 100 #set as a decimal
        points = maltWeight * maltPPG * efficiency / volume
        return points

    def og(self, og):
        points = (og / 1000) + 1
        return points

class IBUCalculator(object):

    def __init__(self):
        pass

    def calcAAU(self, weight, alphaAcids):
        aau = weight * alphaAcids
        return aau

    def calcIBU(self, aau, utilization, volume):
        ibu = aau * utilization * 75 / volume
        return ibu

class SRMCalculator(object):

    def __init__(self):
        pass

    def srmEstimator(self, weight, lovibond, volume):
        mcu = weight * lovibond / volume
        srm = 1.4922 * (mcu ** 0.6859)
        return srm