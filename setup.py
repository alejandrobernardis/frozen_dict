from distutils.core import setup
from distutils.extension import Extension

if 3/2 == 1.5:
    ext_modules = [Extension('frozen_dict', ['frozen_dict_py3.c'])]
else:
    ext_modules = [Extension('frozen_dict', ['frozen_dict_py2.c'])]


with open('README.md', 'r') as f:
    readme = f.read()

setup(
    name='frozen-dict',
    version='2.0',
    url='https://github.com/alejandrobernardis/frozen_dict',
    license='MIT',
    author='Steve Zelaznik',
    author_email='zelaznik@users.noreply.github.com',
    description='Creates a class FrozenDict that behaves like dict, but all '\
                'mutable methods are removed. - Compatible with both Python2 '\
                'and Python3. - Like a tuple, FrozenDict is hashable if and '\
                'only if all its items are hashable.',
    long_description=readme,
    package_data={'': ['LICENSE', 'README.md']},
    ext_modules=ext_modules,
    include_package_data=True,
    zip_safe=False,
    platforms=['Linux']
)