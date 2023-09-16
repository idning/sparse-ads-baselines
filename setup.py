from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension
setup(name='table_batched_embeddings',
      ext_modules=[
          CUDAExtension(
              name='table_batched_embeddings',
              include_dirs=['/private/home/tulloch/src/'],
              sources=[
                  'table_batched_embeddings.cpp',
                  'table_batched_embeddings_cuda.cu'
              ])
      ],
      cmdclass={'build_ext': BuildExtension})


from torch.utils.cpp_extension import load
module = load(
    name='table_batched_embeddings',
    sources=['table_batched_embeddings.cpp', 'table_batched_embeddings_cuda.cu'],
    extra_cflags=['-O2'],
    verbose=True)
