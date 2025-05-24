import cv2
import time
import numpy as np
import HandTrackingModule as htm
import pyautogui
import win32gui
import win32con
import win32api
import os

wCam,hCam=640,480
frameR=100
smoothening=5
window_name="AI Virtual Mouse"

plocX,plocY=0,0
clocX,clocY=0,0
prev_y=0
scroll_active=False
dragging=False
toggle_triggered=False
prev_pinch_dist=None

cap=cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

detector=htm.handDetector(maxHands=1)
wScr,hScr=pyautogui.size()

cv2.namedWindow(window_name)
time.sleep(1)

def bring_window_to_front(window_name):
    hwnd=win32gui.FindWindow(None,window_name)
    if hwnd:
        try:
            win32gui.ShowWindow(hwnd,win32con.SW_RESTORE)
            win32gui.SetForegroundWindow(hwnd)
        except Exception as e:
            print(f"[!] could not bring window to front: {e}")
bring_window_to_front(window_name)

hand_detected_last_time=time.time()

while True:
    success,img=cap.read()
    img=detector.findHands(img)
    lmList,bbox=detector.findPosition(img)
    if len(lmList)!=0:
        hand_detected_last_time=time.time()
        x1,y1=lmList[8][1:]
        x2,y2=lmList[12][1:]
        fingers=detector.fingersUp()


        if fingers[1]==1 and fingers[2]==0:
            x3=np.interp(x1,(frameR,wCam-frameR),(0,wScr))
            y3=np.interp(y1,(frameR,hCam-frameR),(0,hScr))
            clocX=plocX+(x3-plocX)/smoothening
            clocY=plocY+(y3-plocY)/smoothening
            pyautogui.moveTo(wScr-clocX,clocY)
            cv2.circle(img,(x1,y1),10,(255,0,255),cv2.FILLED)
            plocX,plocY=clocX,clocY

        if fingers[1]==1 and fingers[2]==1:
            length,img,lineInfo=detector.findDistance(8,12,img)
            if length<40:
                cv2.circle(img,(lineInfo[4],lineInfo[5]),15,(0,255,0),cv2.FILLED)
                pyautogui.click()

        if fingers==[0,1,1,0,0]:
            if abs(y2-prev_y)>10:
                pyautogui.scroll(30 if y2<prev_y else -30)
            prev_y=y2

        if fingers[0]==1 and fingers[1]==1:
            length,img,_=detector.findDistance(4,8,img)
            if length<40:
                if not dragging:
                    pyautogui.mouseDown()
                    dragging=True
            else:
                if dragging:
                    pyautogui.mouseUp()
                    dragging=False

        if fingers[0]==1 and fingers[1]==1:
            length,img,_=detector.findDistance(4,8,img)
            if prev_pinch_dist is not None:
                if length-prev_pinch_dist>30:
                    win32gui.ShowWindow(win32gui.GetForegroundWindow(),win32con.SW_MAXIMIZE)
                elif prev_pinch_dist-length>30:
                    win32gui.ShowWindow(win32gui.GetForegroundWindow(),win32con.SW_MINIMIZE)
            prev_pinch_dist=length
        else:
            prev_pinch_dist=None

        if fingers==[0,1,1,1,0]:
            if not toggle_triggered:
                pyautogui.press("volumemute")
                os.system("start msedge")
                toggle_triggered=True
        else:
            toggle_triggered=False
    else:
        if time.time()-hand_detected_last_time>5:
            print("Hand not detected for too long.wating....")
    cv2.imshow(window_name,img)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()