from torch.utils.cpp_extension import load

module = load(
    name='table_batched_embeddings',
    extra_include_paths=['/private/home/tulloch/src/'],
    sources=['table_batched_embeddings.cpp', 'table_batched_embeddings_cuda.cu'],
    extra_cflags=['-O2'],
    verbose=True)
