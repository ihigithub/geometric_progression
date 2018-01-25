# this is for geometric progression

def recursion_of_production(ratio, exponent):
    if exponent > 1:
        return ratio*recursion_of_production(ratio, exponent-1)
    else:
        return ratio


def calc_geom_prg(init, ratio, exponent):
    if isinstance(exponent, int):
        return init*recursion_of_production(ratio, exponent)
    else:
        return "number of iteration must be an integer"

# test calculation
# init = 1
# ratio = 2
# exponent = 40
# print calc_geom_prg(init,ratio,exponent)