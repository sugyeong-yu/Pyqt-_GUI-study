"""
 * Requirements

pip install PyQt5
pip install opencv-python

https://pytorch.org/

conda install pytorch torchvision torchaudio cudatoolkit=11.0 -c pytorch
or
conda install pytorch torchvision torchaudio cpuonly -c pytorch

"""

import cv2
import numpy as np

import torch
import torchvision.datasets as dsets
import torchvision.transforms as transforms
# 데이터를 불러와서 저장하는 process

def download_mnist_dataset(path='../mnist_data'):
    dsets.MNIST(root=path, train=True, transform=transforms.ToTensor(), download=True) # 데이터를 다운해서 폴더안에 저장하는 코드.
    dsets.MNIST(root=path, train=False, transform=transforms.ToTensor(), download=True)


def save_mnist_test_images(mnist_path='../mnist_data', save_path='../mnist_data/test_images/'):
    # test set만 가져오는 코드
    # test_images라는 폴더는 자동으로 생성되는 코드를 안적어놓음 따라서 코드 추가 하던가 ㅇ님 폴더를 미리만들어야함.
    batch_size = 1
    test_dataset = dsets.MNIST(root=mnist_path, train=False, transform=transforms.ToTensor(), download=False)
    test_loader = torch.utils.data.DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=False)

    for i, (images, labels) in enumerate(test_loader):
        image = (images.numpy()[0][0]*255).astype(np.uint8)
        cv2.imwrite(save_path+'image%04d.png' % i, image)


if __name__ == '__main__':
    download_mnist_dataset()
    save_mnist_test_images()
