import cv2
import time
import os
#proje.vaşak\vidio.1.mp4
# Video dosyasını aç C:\Users\izzet uzunıııııııı\Desktop\proje.foto işlem\proje.vaşak\vidio.1.mp4
video_path = 'proje.ayi\\vid.mp4'  # Videonuzun yolu
cap = cv2.VideoCapture(video_path)

# Video bilgilerini alın
fps = cap.get(cv2.CAP_PROP_FPS)  # Video FPS (saniyede kare sayısı)
frame_rate = int(fps)  # Her saniyede bir kare alacağız
print(frame_rate)
# Çıkartılan resimlerin kaydedileceği dizini oluşturun
output_dir = 'output_ayi2'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

frame_count = 0
frame_num = 0

# Video karelerini al ve kaydet
while True:
    ret, frame = cap.read()
    if not ret:
        break  # Video bittiğinde döngüyü sonlandır

    # Eğer bu kare, her saniyede bir kareyi temsil ediyorsa
    if frame_count % (frame_rate) == 0:
        frame_filename = os.path.join(output_dir, f"frame_{frame_num}.jpg")
        #frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
        cv2.imwrite(frame_filename, frame)  # Kareyi kaydet
        cv2.imshow("vid",frame)
        cv2.waitKey(100)
        print(frame_filename)
        
        frame_num += 1

    frame_count += 1
# Video dosyasını kapat
cap.release()
print(f"Toplam {frame_num} kare çıkarıldı ve kaydedildi.")
