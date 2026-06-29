def decrypt_video(pwd , evdo_path , out_vdo_path):
    import cv2
    import random
    import numpy as np

    def permuteinv(pt, pbox):
        pt = np.array(pt).flatten().tolist()
        pt1 = pt.copy()
        for k in range(64):
            pt1[pbox[k]] = pt[k]
        return np.array(pt1).reshape(8,8)
        
    def subinv(pt, sbox):
        pt = np.array(pt).flatten().tolist()
        pt1 = pt.copy()
        for k in range(64):
            pt1[k] = sbox.index(pt[k])
        return np.array(pt1).reshape(8,8)
        
    def diffusion(frame , key):
        eframe = frame.copy()
        for ch in range(3):
            for i in range(256):
                for j in range(256):
                    eframe[i ,j , ch] = (frame[i,j,ch] ^ key[i , j , ch])
        return eframe 
        
    seedd = 0
    for i in str(pwd):
        seedd += ord(i)
        
    random.seed(seedd)
    pbox = random.sample(range(1,65) , 64)
    sbox = random.sample(range(1,257) , 256)
    sbox = [i-1 for i in sbox]
    pbox = [i-1 for i in pbox]
    key = [random.randint(0,255) for i in range(256*256*3)]
    key = np.array(key).reshape(256,256,3)
    
    vid = cv2.VideoCapture(evdo_path)
    fps = vid.get(cv2.CAP_PROP_FPS)
    out = cv2.VideoWriter(out_vdo_path , cv2.VideoWriter_fourcc(*'X264') , fps , (256 ,256))
    counter = 1
    while True:
        ret , x = vid.read()
        if ret == False:
            break
        eframe = cv2.imread(f'frame{counter}.png' )
        eframe = cv2.resize(eframe , (256 ,256))    
        frame = diffusion(eframe , key)
        key = eframe.copy()
        for ch in range(3):
            for i in range(32):
                for j in range(32):
                    ob = frame[i*8 : i*8 + 8 , j*8 : j*8 + 8, ch]
                    ob = subinv(ob , sbox)
                    ob = permuteinv(ob , pbox)
                    frame[i*8 : i*8 + 8 , j*8 : j*8 + 8 , ch] =  ob

        out.write(frame)
        print(counter , end = ' ')
        counter += 1
    vid.release()
    out.release()
