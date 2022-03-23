from typing import List, Union

import numpy as np
import numpy.typing as npt


def precision_at_k(
    relevancies: Union[List[int], npt.NDArray[int]], scores: Union[List[float], npt.NDArray[float]], k: int
) -> float:
    """Precision is the fraction of retrieved documents that are relevant to the query.
    For example, for a text search on a set of documents, precision is the number of correct results
    divided by the number of all returned results.

    Precision@k considers only the documents with the highest `k` scores.
    Please note that in `trec_eval`, the number of relevant documents is always `k`, even
    if there are actually fewer documents, that is, `len(relevancies) < k`.

    Args:
        relevancies: Array of non-negative relevancies.
        scores: Target scores assigned to each document.
        k: The cutoff value, only the documents with the highest `k` scores are considered.

    Returns: The precision at `k` over the inputs.
    """

    relevancies = np.asarray(relevancies)
    scores = np.asarray(scores)

    _check_that_array_has_dimension(relevancies, 1)
    _check_that_array_has_dimension(scores, 1)
    _check_that_arrays_have_the_same_shape(relevancies, scores)
    _check_that_array_contains_only_non_negative_elements(relevancies)
    _check_that_array_contains_only_non_negative_elements(scores)

    n = len(relevancies)

    if k < n:
        top_k_indices = np.argpartition(-scores, k)[:k]
        assert len(top_k_indices) == k
        num_relevant_and_retrieved = np.count_nonzero(relevancies[top_k_indices])
    else:
        num_relevant_and_retrieved = np.count_nonzero(relevancies)

    return num_relevant_and_retrieved / k


def recall_at_k():
    pass


def average_precision():
    pass


def mean_average_precision():
    pass


def r_precision():
    pass


def ndcg():
    pass


def _check_that_array_has_dimension(array: np.ndarray, expected_dim: int):
    if array.ndim != expected_dim:
        raise ValueError(f"Expected input to be of dimension [{expected_dim}], but was [{array.ndim}]")


def _check_that_arrays_have_the_same_shape(a: np.ndarray, b: np.ndarray):
    if a.shape != b.shape:
        raise ValueError(f"Expected input to have same shape, but  [{a.shape}] != [{b.shape}]")


def _check_that_array_contains_only_non_negative_elements(array: np.ndarray):
    if np.any(array < 0):
        raise ValueError("Input contains negative elements")
