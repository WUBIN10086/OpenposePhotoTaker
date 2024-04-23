import cv2

def show_image(image_path):
    img = cv2.imread(image_path)
    if img is not None:
        cv2.imshow('Image', img)
        
        # 无限等待直到有键盘输入，检查是否是ESC键 (ASCII 27)
        while True:
            k = cv2.waitKey(0)
            if k == 27:  # ESC key to close
                cv2.destroyAllWindows()
                break
            else:
                print("Press ESC to exit")
    else:
        print(f"Error: The image at '{image_path}' could not be loaded.")

# test
# show_image('PoseRegcognition/DatasetPhoto/LargeView/FullBody/1.jpg')
