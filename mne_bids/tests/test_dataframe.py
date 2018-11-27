"""Test for the dataframe object"""
# Authors: Matt Sanderson <matt.sanderson@mq.edu.au>
#
# License: BSD (3-clause)

import os.path as op
from collections import OrderedDict as odict
from mne_bids.dataframe_odict import (from_tsv, to_tsv, combine, drop,
                                      contains_row)
import pytest

from mne.utils import _TempDir


def test_dataframe():
    # create df
    d = odict([('a', [1, 2, 3, 4]), ('b', [5, 6, 7, 8])])
    assert contains_row(d, [1, 5])
    d2 = odict([('a', [5]), ('b', [9])])
    combine(d, d2)
    assert 5 in d['a']
    d2 = odict([('a', [5]), ('b', [10])])
    combine(d, d2, drop_column='a')
    assert 9 not in d['b']

    tempdir = _TempDir()
    d_path = op.join(tempdir, 'output.tsv')

    # write the MockDataFrame to an output tsv file
    to_tsv(d, d_path)
    # now read it back
    d = from_tsv(d_path)

    # remove any rows with 2 or 5 in them
    drop(d, [2, 5], 'a')
    assert 2 not in d['a']
    drop(d, [], 'a')
    d2 = odict([('a', [5]), ('c', [10])])
    with pytest.raises(KeyError):
        combine(d, d2)
