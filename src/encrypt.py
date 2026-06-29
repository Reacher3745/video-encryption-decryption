def encrypt_video(pwd , vdo_path , output_vdo_path):

    import cv2
    import random
    import numpy as np
    

    def per_sub(pt , pbox , sbox):
        pt = np.array(pt).flatten().tolist()
        pt1 = pt.copy()
        for i in range(5):
            for k in range(64):
                pt1[k] = pt[pbox[k]]
                pt1[k] = sbox[pt[k]]
                
        return np.array(pt1).reshape(8,8)

    
    def permute(pt , pbox):
        pt = np.array(pt).flatten().tolist()
        pt1 = pt.copy()
        for k in range(64):
            pt1[k] = pt[pbox[k]]
        return np.array(pt1).reshape(8,8)
        
    def sub(pt , sbox):
        pt = np.array(pt).flatten().tolist()
        pt1 = pt.copy()
        for k in range(64):
            pt1[k] = sbox[pt[k]]
        return np.array(pt1).reshape(8,8)
        
    def diffusion(frame , key):
        eframe = frame.copy()
        for ch in range(3):
            for i in range(256):
                for j in range(256):
                    eframe[i ,j , ch] = (frame[i,j,ch] ^ key[i , j , ch])
        return eframe 
        
    seedd = 0
    for i in pwd:
        seedd += ord(str(i))
    
    random.seed(seedd)
    pbox = random.sample(range(1,65) , 64)
    sbox = random.sample(range(1,257) , 256)
    sbox = [i-1 for i in sbox]
    pbox = [i-1 for i in pbox]
    key = [random.randint(0,255) for i in range(256*256*3)]
    key = np.array(key).reshape(256,256,3)
    
    vid = cv2.VideoCapture(vdo_path)
    fps = vid.get(cv2.CAP_PROP_FPS)
    out = cv2.VideoWriter(output_vdo_path , cv2.VideoWriter_fourcc(*'X264') , fps , (256 ,256))
    counter = 1
    while True:
        
        ret , frame = vid.read()
        if ret == False:
            break
        frame = cv2.resize(frame , (256 ,256))
        for ch in range(3):
            for i in range(32):
                for j in range(32):
                    ob = frame[i*8 : i*8 + 8 , j*8 : j*8 + 8, ch]
                    ob = permute(ob , pbox)
                    ob = sub(ob , sbox)
                    
                    frame[i*8 : i*8 + 8 , j*8 : j*8 + 8 , ch] =  ob
        eframe = diffusion(frame , key)
        out.write(eframe)
        cv2.imwrite(f'frame{counter}.png' , eframe)
        key = eframe.copy()
        print(counter , end = ' ')
        counter += 1
      
    vid.release()
    out.release()
