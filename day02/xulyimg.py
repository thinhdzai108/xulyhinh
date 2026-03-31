import cv2 as cv
import numpy as np
import urllib.request

def read_img_url(url):
    resp = urllib.request.urlopen(url)
    img_bytes = np.asarray(bytearray(resp.read()), dtype=np.uint8)
    img = cv.imdecode(img_bytes, cv.IMREAD_COLOR)
    return img
def add_noise(img):
    mean = 0
    sigma = 30
    gauss = np.random.normal(mean, sigma, img.shape).astype(np.uint8)
    noisy_img = cv.add(img, gauss)
    return noisy_img

def add_muoi_tieu(img, ratio=0.02):
    noisy_img = img.copy()
    soluong = (ratio * img.size)
    toado = [np.random.randint(0, i - 1, int(soluong)) for i in img.shape]
    noisy_img[toado[0], toado[1]] = 255
    toado = [np.random.randint(0, i - 1, int(soluong)) for i in img.shape]
    noisy_img[toado[0], toado[1]] = 0
    return noisy_img

def draw_zone(img):
    h, w = img.shape[:2]
    overlay = img.copy()

    pts = np.array([
        [int(0.1*w), h],
        [int(0.45*w), int(0.6*h)],
        [int(0.55*w), int(0.6*h)],
        [int(0.9*w), h]
    ], np.int32)

    cv.polylines(overlay, [pts], True, (0, 255, 0), 3)
    return overlay


if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/udacity/CarND-LaneLines-P1/master/test_images/solidWhiteCurve.jpg"
    img = read_img_url(url)
    img = cv.resize(img, (960, 540))
    

    # cv.imshow("Image 1", img)
    # cv.waitKey(0)
    # cv.destroyAllWindows()

    # noisy_img = add_noise(img)
    # cv.imshow("Noisy Image", noisy_img)
    # cv.waitKey(0)
    # cv.destroyAllWindows()


    # img3 = add_muoi_tieu(img, ratio=0.05)
    # cv.imshow("Muoi Tieu Image", img3)
    # cv.waitKey(0)
    # cv.destroyAllWindows()
    zone_img = draw_zone(img)
    cv.imshow("Zone", zone_img)
    cv.waitKey(0)
    cv.destroyAllWindows()