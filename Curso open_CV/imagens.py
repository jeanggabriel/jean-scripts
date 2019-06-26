import cv2

imagemCarregada = cv2.imread("../sonic.jpg",0)
cv2.imshow("imagemCarregada",imagemCarregada)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("imagemSalva.png",imagemCarregada)