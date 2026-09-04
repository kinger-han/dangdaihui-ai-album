import os, sys
from PIL import Image

BASE = r"D:/hpy/桌面/数熙相关文档/党代会项目/海报"
TARGET_W, TARGET_H = 1080, 1920

names = sys.argv[1:] if len(sys.argv) > 1 else ["海报A-问境", "海报B-纪念相册"]

for name in names:
    src = os.path.join(BASE, f"{name}-原始.png")
    dst = os.path.join(BASE, f"{name}-1080x1920.png")
    img = Image.open(src).convert("RGB")
    w, h = img.size
    # cover 模式：等比放大到满高，中心裁剪到目标宽
    new_h = TARGET_H
    new_w = round(w * new_h / h)
    img = img.resize((new_w, new_h), Image.LANCZOS)
    left = (new_w - TARGET_W) // 2
    img = img.crop((left, 0, left + TARGET_W, TARGET_H))
    img.save(dst)
    print(f"{name}: {w}x{h} -> {img.size[0]}x{img.size[1]}  saved: {dst}")