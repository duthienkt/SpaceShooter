PImage s;
PImage []d = new PImage[15];

void setup()
{
  size(800, 700);
  s = loadImage("endway.png");
  for (int i = 14; i> 14-7; --i)
  {
    d[i] = s.get(0, (14-i)* 690, 800, 690);
    
    d[i].save(i+".png");
  }
  
  
  s = loadImage("way_rv.png");
  for (int i = 7; i> 7-4; --i)
  {
    d[i] = s.get(0, (7-i)* 690, 800, 690);
    
    d[i].save(i+".png");
  }
  
  s = loadImage("way.png");
  for (int i = 3; i> 3-4; --i)
  {
    d[i] = s.get(0, (3-i)* 690, 800, 690);
    d[i].save(i+".png");
  }
}


int y0;
void draw()
{
  background(0);
  y0 = frameCount;
  for (int i = 0; i<=14; ++i)
  {
    if (y0- i*690<-690) continue;
    if (y0- i*690>690) continue;
    
    image(d[i], 0, y0- i*690);
  }
  
}