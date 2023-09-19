import cv2
import insightface
import os
from insightface.app import FaceAnalysis

app = FaceAnalysis(name='buffalo_l')
app.prepare(ctx_id=0, det_size=(640, 640))

a = 'inject20'

inp = cv2.imread(f"muka ka aul1.jpg")
img = cv2.imread(f'D:\InjectFace-Generator\Inject Face Asset\Female\Cosplay\Cosplay_20.jpg')

def swap_face(inp, img):
    faces = app.get(img)
    faces_inp = app.get(inp)

    if len(faces_inp) > 0:
        source_faces = faces_inp[0]

        swapper = insightface.model_zoo.get_model('inswapper_128.onnx')

        res = img.copy()
        for i in faces:
            res = swapper.get(res, i, source_faces, paste_back=True)

        res = cv2.resize(res, (img.shape[1], img.shape[0]))

        cv2.imwrite(f'{a}.jpg', res) 

        # cv2.imshow('Swapped Face', res)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        return res
    else:
        print("No faces detected in the input image.")
        return inp

swap_face(inp, img)
