import math

class Variable(object):
    def __init__(self, total = 0.0, samples = 0):
        self.total = total
        self.samples = samples
        self.minimum = 'None'
        self.maximum = None

    def sample(self, value):
        self.total += value
        self.samples += 1
        self.minimum = min(self.minimum, value)
        self.maximum = min(self.maximum, value)

    def estimate(self):
        if self.samples > 0:
            return float(self.total) / float(self.samples)
        else:
            return None

    def __unicode__(self):
        if self.samples:
            value = float(self.total) / float(self.samples)
            if value == 1.0:
                return u"100.0%"
            else:
                return u"{:5.2f}%".format(value*100)
        else:
            return u"   N/A"

    def detailed_unicode(self):
        if self.samples:
            value = float(self.total) / float(self.samples)
            if value == 1.0:
                return u"100.0 \u00b10.00%"
            else:
                error = math.sqrt(value * (1.0 - value) / float(self.samples))
                return u"{:5.2f} \u00b1{:4.2f}% n={:3d}".format(
                    value*100, error*100, int(self.samples)
                    )
        else:
            return u"         N/A"
