def split_to_chunks(size, chunk_size):
    """Return half-open ranges of (start, end) chunks up to size,
    each chunk <= chunk_size.

    >>> list(split_to_chunks(10, 3))
    [(0, 3), (3, 6), (6, 9), (9, 10)]
    """
    if chunk_size <= 0:
        raise ValueError(f'chunk_size must be > 0, got {chunk_size}')

    if size < 0:
        raise ValueError(f'size must be >= 0, got {size}')

    # Return iterator *after* we check arguments
    return _split_to_chunks(size, chunk_size)


def _split_to_chunks(size, chunk_size):
    start = 0
    while start < size:
        end = min(start + chunk_size, size)
        yield start, end
        start = end
