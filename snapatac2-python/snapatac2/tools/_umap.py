from anndata import AnnData
import numpy as np
from typing import Optional, Union, List

def umap(
    adata: AnnData,
    n_comps: int = 2,
    use_dims: Optional[Union[int, List[int]]] = None,
    use_rep: Optional[str] = None,
    random_state: int = 0,
    inplace: bool = True,
) -> Optional[np.ndarray]:
    """
    Parameters
    ----------
    data
        AnnData
    n_comps
    use_rep
    random_state
    inplace

    Returns
    -------
    None
    """
    from umap import UMAP

    if use_rep is None: use_rep = "X_spectral"
    if use_dims is None:
        data = adata.obsm[use_rep]
    elif isinstance(use_dims, int):
        data = adata.obsm[use_rep][:, :use_dims]
    else:
        data = adata.obsm[use_rep][:, use_dims]
    umap = UMAP(
        random_state=random_state, n_components=n_comps
        ).fit_transform(data)
    if inplace:
        adata.obsm["X_umap"] = umap
    else:
        return umap