PGraphics g;
int N = 3;
PImage []ims = new PImage[4];

void setup()
{
  size(1200, 400);
  for (int i = 0; i<=3; ++i)
  ims[i] = loadImage(i+".png");
  g = createGraphics(ims[0].width*4, ims[0].height);
  
  g.beginDraw();

  float x = 0;
  for (int i = 0; i< 4; ++i){
    g.image(ims[i], x, 0);
    x+= ims[0].width;
  }
  g.endDraw();
  g.save("boss1.png");
}

void draw()
{
  background(255);
  image(ims[(frameCount/4)%4], 0, 0);              
}