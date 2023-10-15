from mmengine.config import Config

cfg = Config.fromfile('configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb2-300k_mapillay_v1_65-1280x1280.py')

print(cfg.train_cfg)