import numpy as np
import array
import cv2
import ColorRecognition as color

cap = cv2.VideoCapture(0)

if __name__ == '__main__':
    while(True):
        # Capture frame-by-frame
        ret, frame= cap.read()
        #image_byte_array = array.array('b', frame)
        #image_buffer = I.frombuffer("RGB", (resolution[0],resolution[1]), bytes(image_byte_array), "raw", "RGB", 0, 1)
        #img2 = numpy.asarray(image_buffer)
        #ColorRecognition
        ret_green = color.track_green_object(frame)
        ret_red = color.track_red_object(frame)
        ret_blue = color.track_blue_object(frame)
        if ret_blue:
            for i in range(len(ret_blue)):
                cv2.rectangle(frame,(int(ret_blue[i][0] - 10),int(ret_blue[i][1] - 10)), (int(ret_blue[i][0] + 10),int(ret_blue[i][1] + 10)), (0,255,0), 2)
        '''
        if ret_red:
            cv2.rectangle( frame, (ret_red[0]-10, ret_red[1] - 10), (ret_red[0]+10,ret_red[1]+10), (255,0,0), 2)
            print('find red')
            
        if ret_green:
            cv2.rectangle( frame, (ret_green[0]-10, ret_green[1]-10), (ret_green[0]+10,ret_green[1]+10), (0,0,255), 2)
            print('find green')
        '''
        # Our operations on the frame come here

        # Display the resulting frame
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()