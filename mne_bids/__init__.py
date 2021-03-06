"""MNE software for easily interacting with BIDS compatible datasets."""

__version__ = '0.5.dev0'
from mne_bids import commands
from mne_bids.read import (get_head_mri_trans, read_raw_bids,
                           get_matched_empty_room)
from mne_bids.utils import (get_anonymization_daysback,
                            make_bids_basename, make_bids_folders)
from mne_bids.write import (make_dataset_description, write_anat,
                            write_raw_bids)
