# model.py
from ultralytics import YOLO
import torch

model = YOLO("Arrow_250802.pt")  # 로딩은 한 번만

def get_answer(img):
    detect_res = model(img, conf=0.8, verbose=False)[0].boxes
    detect_final = torch.cat((detect_res.xywhn, detect_res.data), dim=1)

    res_sorted_conf = sorted(detect_final, key=lambda x: x[8], reverse=True)[:4]
    res_sorted_x = sorted(res_sorted_conf, key=lambda x: x[4], reverse=False)

    res_converter = ['left', 'down', 'right', 'up', 'rotate']
    final_res = []
    total = []

    for i in range(4):
        try:
            val = int(res_sorted_x[i][9].item())
            final_res.append(res_converter[val])
            if val != 4:
                total.append((val, res_sorted_x[i][0:4].tolist()))
        except:
            pass

    count_rotate = final_res.count('rotate')
    return final_res, count_rotate, total
