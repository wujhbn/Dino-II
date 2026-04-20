from PIL import Image, ImageDraw
import math

def draw_icon(size):
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    s = size / 512
    
    # Rounded background
    bg_color = (168, 230, 168, 255)
    # Draw rounded rect background
    r = int(80*s)
    d.rounded_rectangle([0, 0, size, size], radius=r, fill=(168, 230, 168, 255))
    
    # Ground
    gr = int(80*s)
    d.rounded_rectangle([0, int(size*0.75), size, size], radius=gr, fill=(100, 180, 100, 255))
    
    # Tail
    from PIL import ImageDraw
    tail_pts = []
    for t in range(20):
        tt = t/19
        # Quadratic bezier: P0=(0.28,0.52), P1=(0.15,0.58), P2=(0.20,0.68)
        x = (1-tt)**2*0.28*size + 2*(1-tt)*tt*0.15*size + tt**2*0.20*size
        y = (1-tt)**2*0.52*size + 2*(1-tt)*tt*0.58*size + tt**2*0.68*size
        tail_pts.append((x,y))
    # reverse for return path
    tail_back = []
    for t in range(20):
        tt = t/19
        x = (1-tt)**2*0.32*size + 2*(1-tt)*tt*0.25*size + tt**2*0.20*size
        y = (1-tt)**2*0.60*size + 2*(1-tt)*tt*0.65*size + tt**2*0.68*size
        tail_back.append((x,y))
    d.polygon(tail_pts + tail_back[::-1], fill=(90, 158, 90, 255))
    
    # Spikes
    spikes = [(0.38,0.16),(0.44,0.13),(0.50,0.12),(0.56,0.13)]
    for bx,by in spikes:
        pts = [(bx*size, by*size), ((bx-0.035)*size,(by+0.085)*size), ((bx+0.035)*size,(by+0.085)*size)]
        d.polygon(pts, fill=(61, 122, 61, 255))
    
    # Body
    bx,by,bw,bh = int(size*0.48),int(size*0.52),int(size*0.22),int(size*0.20)
    d.ellipse([bx-bw,by-bh,bx+bw,by+bh], fill=(90,158,90,255))
    
    # Head
    hx,hy,hw,hh = int(size*0.52),int(size*0.30),int(size*0.18),int(size*0.17)
    d.ellipse([hx-hw,hy-hh,hx+hw,hy+hh], fill=(90,158,90,255))
    
    # Snout
    sx,sy,sw,sh = int(size*0.65),int(size*0.33),int(size*0.08),int(size*0.06)
    d.ellipse([sx-sw,sy-sh,sx+sw,sy+sh], fill=(125,200,125,255))
    
    # Belly
    ex,ey,ew,eh = int(size*0.45),int(size*0.54),int(size*0.13),int(size*0.12)
    d.ellipse([ex-ew,ey-eh,ex+ew,ey+eh], fill=(168,216,168,255))
    
    # Arms
    ax,ay,aw,ah = int(size*0.60),int(size*0.50),int(size*0.045),int(size*0.07)
    d.ellipse([ax-aw,ay-ah,ax+aw,ay+ah], fill=(90,158,90,255))
    
    # Legs
    leg_r = int(6*s)
    d.rounded_rectangle([int(size*0.38),int(size*0.65),int(size*0.46),int(size*0.77)], radius=leg_r, fill=(74,138,74,255))
    d.rounded_rectangle([int(size*0.49),int(size*0.65),int(size*0.57),int(size*0.77)], radius=leg_r, fill=(74,138,74,255))
    
    # Feet
    fx1,fy1 = int(size*0.42),int(size*0.775)
    fw,fh = int(size*0.055),int(size*0.03)
    d.ellipse([fx1-fw,fy1-fh,fx1+fw,fy1+fh], fill=(61,122,61,255))
    fx2,fy2 = int(size*0.53),int(size*0.775)
    d.ellipse([fx2-fw,fy2-fh,fx2+fw,fy2+fh], fill=(61,122,61,255))
    
    # Eye white
    ex1,ey1,ew1,eh1 = int(size*0.55),int(size*0.26),int(size*0.065),int(size*0.07)
    d.ellipse([ex1-ew1,ey1-eh1,ex1+ew1,ey1+eh1], fill=(255,255,255,255))
    
    # Pupil
    px,py,pr = int(size*0.565),int(size*0.265),int(size*0.038)
    d.ellipse([px-pr,py-int(size*0.045),px+pr,py+int(size*0.045)], fill=(26,26,46,255))
    
    # Eye shine
    sx2,sy2,sr = int(size*0.578),int(size*0.252),int(size*0.013)
    d.ellipse([sx2-sr,sy2-int(size*0.015),sx2+sr,sy2+int(size*0.015)], fill=(255,255,255,255))
    
    # Blush
    cx,cy,cr1,cr2 = int(size*0.63),int(size*0.31),int(size*0.04),int(size*0.025)
    d.ellipse([cx-cr1,cy-cr2,cx+cr1,cy+cr2], fill=(255,150,150,128))
    
    # Stars
    for sx3,sy3 in [(0.15,0.20),(0.82,0.15),(0.85,0.55)]:
        sr = int(8*s)
        cx3,cy3 = int(sx3*size),int(sy3*size)
        d.ellipse([cx3-sr,cy3-sr,cx3+sr,cy3+sr], fill=(255,255,150,200))
    
    return img

img512 = draw_icon(512)
img512.save('icon-512.png')
img192 = draw_icon(192)
img192.save('icon-192.png')
img180 = draw_icon(180)
img180.save('icon-180.png')
print("Icons generated!")
