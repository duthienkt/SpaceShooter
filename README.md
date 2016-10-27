github:
https://github.com/duthienkt/SpaceShooter.git
File chạy ./build/main.exe 

==================================================================================
# Garfield Library


## garfield.py

### def garfield_load_image(path)
    path: đường dẫn tới hình ảnh
    Trả về surface là hình ảnh với đường dẫn path
    
>    Trong trường hợp ảnh đã được load, thay vì lấy ảnh từ file, sẽ tự động
>    trả về surface cũ, do vậy chỉ nên copy hoặc dùng ảnh trả về cho mục đích
>    chỉ vẽ, không nên thay đổi
    
### def garfield_pick_color(image, position)
    image: surface
    position: (x, y) tọa độ pixel
    Trả về màu của pixel với tọa độ (x, y) là (R, G, B, A)
    
>   Trong trường hợp lấy ở vị trí nằm ngoài giới hạn của hình, hàm trả về
>   ***None***

### def garfield_mixer_init()
    Khởi tạo mixer để chơi nhạc của pygame
    
>   Có thể gọi nhiều lần không bị lỗi, vì đã kiểm tra khởi tạo

### def garfield_music_load(path)
    path: đường dẫn đến file nhạc
    Load nhạc vào bộ nhớ
    
>   Nhạc mỗi lần chỉ có thể chạy duy nhất 1 bài, nên load các định dạng 
>   nhạc không nén để nhạc có thể chơi ngay, có thể dùng nhạc ogg là tốt
>   nhất. Nên tránh dùng nhạc mp3

### def garfield_music_play(times)
    times: số lần chơi nhạc lặp lại, time =-1 lặp mãi mãi
    chơi bài nhạc sau khi load
    
### def garfield_music_stop()
    Dừng chơi nhạc
    
### def garfield_add_music(path)
    path: đường dẫn đến file nhạc
    Thêm bài hát vào danh sách
    
### def garfield_music_is_busy()
    Kiểm tra hiện tại có bài nhạc nào đang chơi hay không
    
>   Để đơn giản, ta chỉ cần dùng hàm ***garfield_add_music*** và ***garfield_music_is_busy***
>   là đủ.
Việc kiểm tra có bài nhạc có đang được chạy hay không rất tốn tài nguyên, 
nên ta có thể mượn các hàm sự kiện như chuột, bàn phím để gọi trigger. Ví dụ

```python3 
    def trigger_music(self):
        if not garfield_music_is_busy():
            garfield_add_music("assets/soundtrack/track2.ogg")
```