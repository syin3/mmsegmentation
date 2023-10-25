"""
similar to mmsegmentation/configs/_base_/datasets/mapillary_v1_65.py, only look at a subset of classes in label images

Usage: mmsegmentation/configs/
"""

# dataset settings
_base_ = './mapillary_v2.py'
metainfo = dict(
    classes=('Traffic Island', 'Sidewalk', 'Crosswalk - Plain', 'Lane Marking - Dashed Line', 
             'Lane Marking - Straight Line'),
    palette=[[128, 196, 128], [244, 35, 232], [140, 140, 200], [255, 255, 255], 
             [255, 255, 255]])

train_dataloader = dict(dataset=dict(metainfo=metainfo))
val_dataloader = dict(dataset=dict(metainfo=metainfo))
test_dataloader = val_dataloader


# create a standalone mapillary v2 dataset, from https://github.com/syin3/mmsegmentation/blob/main/docs/en/advanced_guides/datasets.md#modification-of-dataset-classes

# from mmseg.datasets import MapillaryDataset_v2

# data_root = 'data/mapillary/'
# data_prefix = dict(img_path='training/images', seg_map_path='training/v2.0/labels')

# # metainfo to only keep specified classes
# metainfo = dict(
#     classes=(
#         'Traffic Island', 
#         'Sidewalk', 
#         'Crosswalk - Plain', 
#         'Lane Marking - Dashed Line'
#     )
# )

# dataset = MapillaryDataset_v2(
#     data_root=data_root, 
#     data_prefix=data_prefix, 
#     metainfo=metainfo
# )

# print(dataset.metainfo)