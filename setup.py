#!/usr/bin/env python


from distutils.core import setup, Extension
import os


scws_dir = os.path.abspath("scws/libscws")
scws_sources = [ "%s/%s" % ( scws_dir, f ) for f in ["charset.c", "crc32.c", "darray.c", "lock.c", "pool.c", "rule.c", "scws.c", "xdb.c", "xdict.c", "xtree.c"]]

scws_module = Extension(name='scws',
                        sources=['pyscws.c',] + scws_sources ,
                        language='c',
                        include_dirs=['/usr/include/python2.7','.', scws_dir],
                        library_dirs=['/usr/local/lib'],
                        libraries=['python'],
                        extra_compile_args=[])


setup(
    name='scws',
    version='0.0.1',
    url='http://code.google.com/p/pyscws/',
    description='a python package for scws',
    author_email='beijixuexiong@gmail.com, ysj.ray@gmail.com, liangjianglou@126.com',
    ext_modules=[scws_module],
    packages=['scwsseg'],
    package_data={'scwsseg': ['data/*.txt', 'data/ext_stopword.dic']},
)
