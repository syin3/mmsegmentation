# how _base_ config is overwritten in model config file
from mmengine.config import Config

cfg = Config.fromfile('configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb2-300k_mapillay_v1_65-1280x1280.py')

print(cfg.train_cfg)

# how to specify a subset of classes
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

# # sample output of four selected label
# # label index 255 means to be ignored
# # {
# #     'classes': ('Traffic Island', 'Sidewalk', 'Crosswalk - Plain', 'Lane Marking - Dashed Line'),
# #     'palette': [[128, 196, 128], [244, 35, 232], [140, 140, 200], [255, 255, 255]], 
# #     'label_map': {0: 255, 1: 255, 2: 255, 3: 255, 4: 255, 5: 255, 6: 255, 7: 255, 8: 255, 9: 255, 10: 255, 11: 255, 12: 255, 13: 255, 14: 2, 15: 255, 16: 255, 17: 255, 18: 255, 19: 255, 20: 255, 21: 255, 22: 255, 23: 255, 24: 1, 25: 0, 26: 255, 27: 255, 28: 255, 29: 255, 30: 255, 31: 255, 32: 255, 33: 255, 34: 255, 35: 3, 36: 255, 37: 255, 38: 255, 39: 255, 40: 255, 41: 255, 42: 255, 43: 255, 44: 255, 45: 255, 46: 255, 47: 255, 48: 255, 49: 255, 50: 255, 51: 255, 52: 255, 53: 255, 54: 255, 55: 255, 56: 255, 57: 255, 58: 255, 59: 255, 60: 255, 61: 255, 62: 255, 63: 255, 64: 255, 65: 255, 66: 255, 67: 255, 68: 255, 69: 255, 70: 255, 71: 255, 72: 255, 73: 255, 74: 255, 75: 255, 76: 255, 77: 255, 78: 255, 79: 255, 80: 255, 81: 255, 82: 255, 83: 255, 84: 255, 85: 255, 86: 255, 87: 255, 88: 255, 89: 255, 90: 255, 91: 255, 92: 255, 93: 255, 94: 255, 95: 255, 96: 255, 97: 255, 98: 255, 99: 255, 100: 255, 101: 255, 102: 255, 103: 255, 104: 255, 105: 255, 106: 255, 107: 255, 108: 255, 109: 255, 110: 255, 111: 255, 112: 255, 113: 255, 114: 255, 115: 255, 116: 255, 117: 255, 118: 255, 119: 255, 120: 255, 121: 255, 122: 255, 123: 255}, 
# #     'reduce_zero_label': False
# # }
# # 14: 2, 24: 1, 25: 0, 35: 3


# print(dataset.metainfo)
