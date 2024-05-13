import numpy as np
from numpy.typing import NDArray
from typing import Tuple

def count_twofolds(
        tagsA: NDArray[np.int64],
        tagsB: NDArray[np.int64],
        sizeA: int,
        sizeB: int,
        tcc: int
) -> int:...

def get_twofold_tags(
        tagsA: NDArray[np.int64],
        tagsB: NDArray[np.int64],
        sizeA: int,
        sizeB: int,
        tcc: int
) -> Tuple[list, list]: ...

def get_threefold_tags(
        tagsA: NDArray[np.int64],
        tagsB: NDArray[np.int64],
        tagsC: NDArray[np.int64],
        sizeA: int,
        sizeB: int,
        sizeC: int,
        tcc: int
) -> Tuple[list, list, list]: ...

def get_fourfold_tags(
        tagsA: NDArray[np.int64],
        tagsB: NDArray[np.int64],
        tagsC: NDArray[np.int64],
        tagsD: NDArray[np.int64],
        sizeA: int,
        sizeB: int,
        sizeC: int,
        sizeD: int,
        tcc: int
) -> Tuple[list, list, list, list]: ...

def histogram(
        tagsA: NDArray[np.int64],
        tagsB: NDArray[np.int64],
        sizeA: int,
        sizeB: int,
        tcc: int,
        sizeDelay: int,
        delays_obj: NDArray[np.int64]
) -> list: ...

def sync_to_clock(
        tags: NDArray[np.int64],
        synctags: NDArray[np.int64],
        sizeTags: int,
        sizeSyncTags: int,
        syncPeriod: int
) -> list: ...
