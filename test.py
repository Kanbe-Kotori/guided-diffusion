import numpy
import PIL.Image as Image


data = numpy.load('./samples/samples_100x64x64x3.npz')
print(data['arr_0'].shape)
print(data['arr_1'])

for i in range(data['arr_0'].shape[0]):
    image = Image.fromarray(numpy.uint8(data['arr_0'][i]))
    image.save(f"./images/image_{i}.png")
