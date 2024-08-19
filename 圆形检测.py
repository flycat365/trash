

import numpy as np
import cv2

cap = cv2.imread('D:/fu/1847338981106795.png')

ret = cap.set(3, 640)  # ����֡��
ret = cap.set(4, 480)  # ����֡��
font = cv2.FONT_HERSHEY_SIMPLEX  # ����������ʽ
kernel = np.ones((5, 5), np.uint8)  # �����

if cap is True:  # �������ͷ�Ƿ���������
    while True:
        frame = cap.read('D:/fu/1847338981106795.png')
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # ת��Ϊ��ɫͨ��
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # ת��ΪHSV�ռ�

        #  ��������
        opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)  # ��̬ѧ������
        bila = cv2.bilateralFilter(opening, 10, 100, 200)  # ˫���˲���������
        edges = cv2.Canny(opening, 50, 100)  # ��Եʶ��
        # ʶ��Բ��
        circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 50, param1=100, param2=75, minRadius=10, maxRadius=240)
        if circles is not None:  # ���ʶ���Բ
            for circle in circles[0]:
                #  ��ȡԲ��������뾶
                x = int(circle[0])
                y = int(circle[1])
                r = int(circle[2])
                cv2.circle(frame, (x, y), r, (0, 255, 0), 3)  # ���Բ
                cv2.circle(frame, (x, y), 6, (255, 255, 0), -1)  # ���Բ��
                text = 'x:  ' + str(x) + ' y:  ' + str(y)
                cv2.putText(frame, text, (10, 30), font, 1, (0, 255, 0), 2, cv2.LINE_AA, 0)  # ��ʾԲ��λ��
        else:
            # ���ʶ�𲻳�����ʾԲ�Ĳ�����
            cv2.putText(frame, 'x: None y: None', (10, 30), font, 1, (0, 255, 0), 2, cv2.LINE_AA, 0)
        cv2.imshow('frame', frame)
        cv2.imshow('edges', edges)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
else:
    print('cap is not opened!')