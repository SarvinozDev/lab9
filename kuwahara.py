import cv2
import numpy as np

def kuwahara_filter(img, ksize=5):
    if ksize % 2 == 0:
        raise ValueError("Kernel o'lchami toq bo'lishi kerak!")

    h, w = img.shape
    pad = ksize // 2
    padded = cv2.copyMakeBorder(img, pad, pad, pad, pad, cv2.BORDER_REFLECT)
    result = np.zeros_like(img)

    for y in range(h):
        for x in range(w):
            region1 = padded[y:y+pad+1, x:x+pad+1]
            region2 = padded[y:y+pad+1, x+pad:x+ksize]
            region3 = padded[y+pad:y+ksize, x:x+pad+1]
            region4 = padded[y+pad:y+ksize, x+pad:x+ksize]

            regions = [region1, region2, region3, region4]

            means = [np.mean(r) for r in regions]
            vars_ = [np.var(r) for r in regions]

            min_index = np.argmin(vars_)
            result[y, x] = means[min_index]

    return result


img = cv2.imread("image3.png", 0)
if img is None:
    print("Rasm topilmadi.")
    exit()

filtered = kuwahara_filter(img, ksize=5)

cv2.imshow("Asl rasm", img)
cv2.imshow("Kuwahara Filter", filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("kuwahara_filtered.jpg", filtered)
