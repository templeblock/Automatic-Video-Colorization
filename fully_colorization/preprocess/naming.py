import os, cv2, sys
sys.path.append('..')
from pytorch_pwc.utils import get_names

all_dir = '../data/DAVIS/JPEGImages/480p'
store_dir = '../data/DAVIS/frames'
os.makedirs(store_dir, exist_ok=True)

dir_names = [d for d in os.listdir(all_dir) if os.path.isdir(os.path.join(all_dir, d))]

for img_dir in dir_names:
    image_names = get_names(os.path.join(all_dir,img_dir))

    for i,image_name in enumerate(image_names):
        img = cv2.imread(image_name)
        name = os.path.basename(image_name)
        if i % 1000 == 0:
            print(os.path.join(store_dir, img_dir+'%06d.jpg'%i))
        cv2.imwrite(os.path.join(store_dir, img_dir+'%06d.jpg'%i), img)