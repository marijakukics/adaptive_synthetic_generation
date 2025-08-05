
# Online Python - IDE, Editor, Compiler, Interpreter
import copy
def generate_draws(iterator, numberOfDraws):

    """Function that generates one sequence of draws. Implemented as a
        separate function in order to implement it for parallel
        processing (not implemented yet).

    :param iterator: iterator on the MH draws
    :type iterator: MetropolisHastingsIterator

    :param numberOfDraws: number of draws to generate
    :type numberOfDraws: int

    :return: the generated draws
    :rtype: numpry.array
    """
    #keep deepcopy, otherwise it shifts in the weird way
    lista = []
    for i in range(numberOfDraws):
        item = copy.deepcopy(next(iterator).indicators())
        lista.append(item)                       
    return lista

