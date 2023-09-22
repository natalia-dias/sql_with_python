iris = {}

# kwargs = ['id_n', 'species', 'petal_length', 'petal_width']

def add_iris(id_n=0, species=None, petal_length=0, petal_width=0, **kwargs):

    new_iris = {id_n: {'species': species, 'petal_length': petal_length, 'petal_width': petal_width, }}
    iris.update(new_iris)
    for key, value in kwargs.items():
        iris[id_n][key] = value
