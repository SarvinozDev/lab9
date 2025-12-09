import cv2
import numpy as np

def adaptive_median_filter(img, max_kernel_size=7):
    result = img.copy()
    rows, cols = img.shape

    for i in range(rows):
        for j in range(cols):

            kernel_size = 3

            while True:
                half = kernel_size // 2

                r1 = max(0, i - half)
                r2 = min(rows, i + half + 1)
                c1 = max(0, j - half)
                c2 = min(cols, j + half + 1)

                window = img[r1:r2, c1:c2]

                Zmin = np.min(window)
                Zmax = np.max(window)
                Zmed = np.median(window)
                A1 = Zmed - Zmin
                A2 = Zmed - Zmax

                if A1 > 0 and A2 < 0:
                    B1 = img[i, j] - Zmin
                    B2 = img[i, j] - Zmax

                    if B1 > 0 and B2 < 0:
                        result[i, j] = img[i, j]
                    else:
                        result[i, j] = Zmed
                    break
                else:
                    kernel_size += 2
                    if kernel_size > max_kernel_size:
                        result[i, j] = Zmed
                        break

    return result


img = cv2.imread("image3.png", 0)

filtered = adaptive_median_filter(img)

cv2.imshow("Asl rasm", img)
cv2.imshow("Adaptive Median Filter", filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("adaptive_filtered.jpg", filtered)
