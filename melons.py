"""This file should have our order classes in it."""

class AbstractMelonOrder(object):

    def __init__(self, species, qty, tax=None, order_type=None):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax


    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


    def get_total(self):
        """Calculate price."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        return total


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        super(DomesticMelonOrder,self).__init__(species, qty, 0.08, "domestic")


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        super(InternationalMelonOrder,self).__init__(species, qty, 0.17, 'international')
        self.country_code = country_code


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        original_total = super(InternationalMelonOrder, self).get_total()
        print original_total
        if self.qty < 10:
            new_total = original_total + 3
            print new_total
            return new_total
        else:
            return original_total