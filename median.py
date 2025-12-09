import cv2
def apply_median_filter(image_path, kernel_size=5):
    img = cv2.imread(image_path)

    median_filtered = cv2.medianBlur(img, kernel_size)

    cv2.imshow('Asl rasm', img)
    cv2.imshow(f'Mediana filtri (kernel = {kernel_size})', median_filtered)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite('median_filtered_output.jpg', median_filtered)

apply_median_filter('Segment_rasm.jpg', kernel_size=7)
