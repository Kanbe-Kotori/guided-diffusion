import numpy as np
import PIL.Image

Alldata = np.load('samples_100x64x64x1.npz', allow_pickle=True)
arr_0 = Alldata['arr_0'].reshape(100, 64, 64)
print(arr_0.shape)
for i in range(arr_0.shape[0]):
    # 将当前图像的数据从numpy数组转换为PIL图像对象
    image_data = arr_0[i]
    image = PIL.Image.fromarray(image_data, 'L')

    # 保存图像
    filename = f'image_{i}.jpg'
    image.save('./images/' + filename)
