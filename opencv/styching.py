import cv2
image_paths=['1.jpg', '2.jpg', '3.jpg', '4.jpg']

imgs = []

for i in range(len(image_paths)):
    imgs.append(cv2.imread(image_paths[i]))
    imgs[i] = cv2.resize(imgs[i], (0,0), fx=0.4, fy=0.4)

cv2.imshow('1',imgs[0])
cv2.imshow('2',imgs[1])
cv2.imshow('3',imgs[2])

stitchy = cv2.Stitcher.create()
(dummy, output) = stitchy.stitch(imgs)

if dummy != cv2.STITCHER_OK:
    print("stitching ain't successful")
else:
    print("Your Panorama is ready!!!")

cv2.imshow('final result', output)

cv2.waitKey(0)