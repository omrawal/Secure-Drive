import cv2
import os
import shutil

# current_dir = os.getcwd()
# print(current_dir)
# folder_path = current_dir+'\\temp\\'
# print(folder_path)


def capture_image_from_cam_into_temp():
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    cv2.namedWindow("Camera")

    # img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("Camera", frame)

        k = cv2.waitKey(1)
        if k % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k % 256 == 32:
            # SPACE pressed
            if not os.path.isdir('temp'):
                os.mkdir('temp', mode=0o777)  # make sure the directory exists
            # img_name = "./temp/opencv_frame_{}.png".format(img_counter)
            img_name = "./temp/test_img.png"
            print('imwrite=', cv2.imwrite(filename=img_name, img=frame))
            print("{} written!".format(img_name))
            # img_counter += 1

    cam.release()

    cv2.destroyAllWindows()

    return True


def empty_temp_folder():
    folder = 'temp'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def empty_decrypted_folder():
    folder = 'decrypted_files'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def save_profile_pic(profile_pic_loc):
    if not os.path.isdir('profile_pics'):
        os.mkdir('profile_pics', mode=0o777)
    source_loc = profile_pic_loc.replace('/', '\\')
    destination_loc = os.getcwd()+'\profile_pics\\'
    img = cv2.imread(source_loc)
    file_name = (source_loc.split('\\')[-1])
    save_file_loc = destination_loc+file_name
    print('destination=', save_file_loc)
    # do some transformations on img
    # save matrix/array as image file
    isWritten = cv2.imwrite(save_file_loc, img)
    if isWritten:
        print('Image is successfully saved as file.')
        return save_file_loc
    else:
        print('Some Error')
        return False


def is_temp_empty():
    if len(os.listdir('temp/')) == 0:
        # print("Directory is empty")
        return True
    else:
        return False


# capture_image_from_cam_into_temp()
