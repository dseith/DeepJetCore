from glob import glob
from os import environ
from os.path import basename, dirname
from pdb import set_trace

#gather all the files here
modules = [basename(i.replace('.py','')) for i in glob('%s/[A-Za-z]*.py' % dirname(__file__))]
print ('\n\npreprocessing modules:', modules)
__all__ = []
for module_name in modules:
    module = __import__(module_name, globals(), locals(), [module_name])
    print('preprocessing module: ', module)
    for model_name in [i for i in dir(module)]:
        model = getattr(module, model_name)
        globals()[model_name] = model
        locals( )[model_name] = model
        __all__.append(model_name)
        print('preprocessing: ', model_name)
        
        if __all__ is not None:
            if model_name not in __all__:
                __all__.append(model_name)
        else:
            __all__ = [model_name]
