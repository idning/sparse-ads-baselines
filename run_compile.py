from torch.utils.cpp_extension import load

module = load(
    name='table_batched_embeddings',
    extra_include_paths=['/private/home/tulloch/src/'],
    sources=['table_batched_embeddings.cpp', 'table_batched_embeddings_cuda.cu'],
    extra_cflags=['-O2'],
    verbose=True)

sparse_embedding_cuda = load(
    name='sparse_embedding_cuda',
    extra_include_paths=['/private/home/tulloch/src/'],
    sources=['sparse_embedding_cuda.cpp', 'sparse_embedding_cuda_kernel.cu'],
    extra_cflags=['-O2'],
    verbose=True)

print('loaded ')
